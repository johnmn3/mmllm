# Deep spot-check: grade 12 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G12-01: Transducers introduction

### G12-01 record 1

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
Two creatures of the meadow approached the coming winter very differently.

The summer had ended atop the hilltop and the two were sitting beneath an old
tree, comparing notes. Toc the ant drew the transducer (map inc) used via into into the
dust. "We've come a long way," she said. "The form
`(into [] (map inc) [1 2 3])` is the kind of thing we'd reach for now." Skip
nodded — for once weary from the morning's effort enough to listen.

What Clojure form computes [1 2 3] each incremented through a transducer? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 2

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Halfway through the morning's work, Hum the grasshopper blocked
Bit the ant's path in the farm and refused to step aside until someone
could prove what the form `(into [] (map inc) [1 2 3])` evaluated to. Hum
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the transducer (map inc) used via into to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 3

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Skip the grasshopper marked out a wager on the hilltop: whoever
guessed the result of `(into [] (map inc) [1 2 3])` first would win the right to
choose the next song. Bit the ant, untroubled by what others thought, said it was easier
to ask the REPL about the transducer (map inc) used via into than to argue.

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 4

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
All summer long, the Ant worked while the Grasshopper sang.

Skip the grasshopper, her legs heavy from sprinting from a season of song, was finally
willing to study patterns. Bit the ant pointed by the orchard at
the transducer (map inc) used via into. The form `(into [] (map inc) [1 2 3])` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 record 5

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path at the edge of the forest and refused to step aside until someone
could prove what the form `(into [] (map inc) [1 2 3])` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the transducer (map inc) used via into to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for [1 2 3] each incremented through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

## G12-02: Transducer composition

### G12-02 record 1

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Chirp the grasshopper said,
with great whoops of laughter. "Anyone can see what the composed transducer (comp (map inc) (filter even?)) comes to."
Bit the ant, who atop the hilltop had grown used to such claims, asked
him to actually write the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the result of inc-then-keep-evens via a composed transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 2

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," they said, pointing to the composed transducer (comp (map inc) (filter even?)).
"You hand the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

What Clojure form computes the result of inc-then-keep-evens via a composed transducer? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 3

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

Hum the grasshopper, weary from the morning's effort from a season of song, was finally
willing to study patterns. Toc the ant pointed by the orchard at
the composed transducer (comp (map inc) (filter even?)). The form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` was the canonical example;
the REPL would confirm what it produced.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 4

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to the composed transducer (comp (map inc) (filter even?)).
"You hand the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, drowsy from the warm sun, agreed to
try.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 record 5

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A banquet at the end of the season by the orchard brought together every
creature who'd ever stockpiled. The day's discussion was
the composed transducer (comp (map inc) (filter even?)). Tic wrote the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` on a square of
parchment and passed it across the table; Skip, lulled by the gentle wind
but pleased, agreed to read it into the REPL.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

## G12-03: into with a transducer (xform)

### G12-03 record 1

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

A small audience of meadow creatures had gathered near the garden to watch
Skip the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to into a set with the (map inc) transducer and read out the form aloud:
`(into #{} (map inc) [1 2 3])`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the set produced by mapping inc into an empty set.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 2

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate in the meadow: whoever
predicted the result of `(into #{} (map inc) [1 2 3])` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about into a set with the (map inc) transducer.

What Clojure form computes the set produced by mapping inc into an empty set? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 3

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
swaggering through the underbrush. "Anyone can see what into a set with the (map inc) transducer comes to."
Bit the ant, who by the garden had grown used to such claims, asked
him to actually write the form `(into #{} (map inc) [1 2 3])` and
submit it to the REPL — just to be sure.

What Clojure form computes the set produced by mapping inc into an empty set? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 4

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

"This isn't a song trick," Toc said in the orchard, saying very little. "It's a
tool." Skip the grasshopper looked at into a set with the (map inc) transducer and admitted
she would not have known what to write. Toc sketched
`(into #{} (map inc) [1 2 3])` on a slate so the runtime could speak for itself.

Write a Clojure expression that computes the set produced by mapping inc into an empty set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 record 5

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path by the farm and refused to step aside until someone
could prove what the form `(into #{} (map inc) [1 2 3])` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit into a set with the (map inc) transducer to the REPL. Whatever comes
back is the answer."

What Clojure form computes the set produced by mapping inc into an empty set? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

## G12-04: core.async introduction

### G12-04 record 1

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered on the hilltop to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the core.async primitives chan/go/<!/>! and read out the form aloud:
`(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the marker for the core.async lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 2

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path near the hilltop and refused to step aside until someone
could prove what the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the core.async primitives chan/go/<!/>! to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the marker for the core.async lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 3

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," he said, pointing to the core.async primitives chan/go/<!/>!.
"You hand the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, weary from the morning's effort, agreed to
try.

What Clojure form computes the marker for the core.async lesson? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 4

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the orchard, the next entry
was the core.async primitives chan/go/<!/>!. Chirp the grasshopper peered over
her shoulder at the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` and asked what it
would come out to.

Write a Clojure expression that computes the marker for the core.async lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 record 5

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

"This isn't a song trick," Toc said by the orchard, untroubled by what others thought. "It's a
tool." Skip the grasshopper looked at the core.async primitives chan/go/<!/>! and admitted
she would not have known what to write. Toc sketched
`(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` on a slate so the runtime could speak for itself.

Write a Clojure expression that computes the marker for the core.async lesson.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

## G12-05: Channels and pipelines

### G12-05 record 1

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what the pipeline operators in core.async comes to."
Toc the ant, who at the edge of the woods had grown used to such claims, asked
her to actually write the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the marker for the channel-pipeline lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 2

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

Tic the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. atop the hilltop, the
next entry was the pipeline operators in core.async, and the form was `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`.
Hum the grasshopper, with great whoops of laughter but more reflective than usual,
agreed to write the form into the REPL.

Question: write a Clojure expression for the marker for the channel-pipeline lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 3

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written the pipeline operators in core.async on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` in the REPL and read off whatever it returned.

What Clojure form computes the marker for the channel-pipeline lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 4

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"This isn't a song trick," Tic said at the edge of the farm, her eyes always on the path. "It's a
tool." Hum the grasshopper looked at the pipeline operators in core.async and admitted
they would not have known what to write. Tic sketched
`(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` on a slate so the runtime could speak for itself.

Write a Clojure expression that computes the marker for the channel-pipeline lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 record 5

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile atop the hilltop, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about the pipeline operators in core.async.

What Clojure form computes the marker for the channel-pipeline lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

## G12-06: clojure.spec

### G12-06 record 1

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper, weary from the morning's effort from a season of song, was finally
willing to study patterns. Tic the ant pointed near the woods at
(s/valid? int? 42) — a basic spec check. The form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives whether 42 conforms to the int? spec.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 2

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`. Hum
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of (s/valid? int? 42) — a basic spec check was to put it in the
REPL.

Write a Clojure expression that computes whether 42 conforms to the int? spec.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 3

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A banquet at the end of the season in the orchard brought together every
creature who'd ever stockpiled. The day's discussion was
(s/valid? int? 42) — a basic spec check. Toc wrote the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` on a square of
parchment and passed it across the table; Hum, her legs heavy from sprinting
but pleased, agreed to read it into the REPL.

Write a Clojure expression that computes whether 42 conforms to the int? spec.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 4

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path in the forest and refused to step aside until someone
could prove what the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit (s/valid? int? 42) — a basic spec check to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for whether 42 conforms to the int? spec.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 record 5

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

A small audience of meadow creatures had gathered by the meadow to watch
Skip the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to (s/valid? int? 42) — a basic spec check and read out the form aloud:
`(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for whether 42 conforms to the int? spec.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

## G12-07: Spec generators

### G12-07 record 1

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today by the forest, the next entry
was what s/exercise does. Hum the grasshopper peered over
his shoulder at the form `(do "s/exercise produces sample inputs for a spec" :studied)` and asked what it
would come out to.

Question: write a Clojure expression for the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 2

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

At the end of the harvest in the farm, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured what s/exercise does. Toc the ant touched it with a feeler and
said the form to remember was `(do "s/exercise produces sample inputs for a spec" :studied)`; Hum the grasshopper
agreed to submit it.

Write a Clojure expression that computes the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 3

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to what s/exercise does.
"You hand the form `(do "s/exercise produces sample inputs for a spec" :studied)` to the runtime, and the runtime hands
you back what it evaluates to." Skip, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 4

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Hum the grasshopper, yawning at the soft moss from a season of song, was finally
willing to study patterns. Toc the ant pointed near the orchard at
what s/exercise does. The form `(do "s/exercise produces sample inputs for a spec" :studied)` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives the marker for the spec-generators lesson.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 record 5

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

A banquet at the end of the season near the hilltop brought together every
creature who'd ever stockpiled. The day's discussion was
what s/exercise does. Toc wrote the form `(do "s/exercise produces sample inputs for a spec" :studied)` on a square of
parchment and passed it across the table; Chirp, yawning at the soft moss
but pleased, agreed to read it into the REPL.

Question: write a Clojure expression for the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

## G12-08: clojure.test

### G12-08 record 1

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(= (+ 1 2) 3)`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about (= (+ 1 2) 3) — what an `is` would test.

What Clojure form computes the truth value an `is` assertion would record? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 2

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

With a twig, Skip the grasshopper marked out a wager by the garden: whoever
guessed the result of `(= (+ 1 2) 3)` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about (= (+ 1 2) 3) — what an `is` would test than to argue.

Question: write a Clojure expression for the truth value an `is` assertion would record.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 3

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

A small audience of meadow creatures had gathered in the forest to watch
Hum the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to (= (+ 1 2) 3) — what an `is` would test and read out the form aloud:
`(= (+ 1 2) 3)`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives the truth value an `is` assertion would record.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 4

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate near the farm: whoever
predicted the result of `(= (+ 1 2) 3)` first would set the next day's
ration. Tic the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about (= (+ 1 2) 3) — what an `is` would test.

Question: write a Clojure expression for the truth value an `is` assertion would record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 record 5

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang.

Chirp the grasshopper, drowsy from the warm sun from a season of song, was finally
willing to study patterns. Toc the ant pointed at the edge of the garden at
(= (+ 1 2) 3) — what an `is` would test. The form `(= (+ 1 2) 3)` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives the truth value an `is` assertion would record.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

## G12-09: Test fixtures

### G12-09 record 1

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
as if the race were already won. "Anyone can see what use-fixtures and the fixture pattern comes to."
Tic the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the marker for the fixtures lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 2

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written use-fixtures and the fixture pattern on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the marker for the fixtures lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 3

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

A wooden sign nailed to a stalk in the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`. Skip
laughed, swaggering through the underbrush, and declared it too easy. Toc said patiently
that the only way to be sure of use-fixtures and the fixture pattern was to put it in the
REPL.

Write a form whose evaluation gives the marker for the fixtures lesson.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 4

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

At the end of the harvest near the garden, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured use-fixtures and the fixture pattern. Tic the ant touched it with a feeler and
said the form to remember was `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`; Skip the grasshopper
agreed to submit it.

Write a form whose evaluation gives the marker for the fixtures lesson.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 record 5

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

Toc the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," she said, pointing to use-fixtures and the fixture pattern.
"You hand the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

What Clojure form computes the marker for the fixtures lesson? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

## G12-10: Property-based testing

### G12-10 record 1

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written the property that double-reverse is identity on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(= (reverse (reverse [1 2 3])) [1 2 3])` in the REPL and read off whatever it returned.

What Clojure form computes the truth value of the double-reverse property on [1 2 3]? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 2

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager at the edge of the garden: whoever
guessed the result of `(= (reverse (reverse [1 2 3])) [1 2 3])` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about the property that double-reverse is identity than to argue.

Write a form whose evaluation gives the truth value of the double-reverse property on [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 3

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang.

Toc the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. by the garden, the
next entry was the property that double-reverse is identity, and the form was `(= (reverse (reverse [1 2 3])) [1 2 3])`.
Chirp the grasshopper, with a smug grin but more reflective than usual,
agreed to write the form into the REPL.

Write a form whose evaluation gives the truth value of the double-reverse property on [1 2 3].

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 4

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the farm, the next entry
was the property that double-reverse is identity. Skip the grasshopper peered over
their shoulder at the form `(= (reverse (reverse [1 2 3])) [1 2 3])` and asked what it
would come out to.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 record 5

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

At the end of the harvest in the farm, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the property that double-reverse is identity. Bit the ant touched it with a feeler and
said the form to remember was `(= (reverse (reverse [1 2 3])) [1 2 3])`; Chirp the grasshopper
agreed to submit it.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

## G12-11: Leiningen project.clj

### G12-11 record 1

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

A wooden sign nailed to a stalk in the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`. Chirp
laughed, boasting at every turn, and declared it too easy. Tic said patiently
that the only way to be sure of the project.clj manifest for Leiningen was to put it in the
REPL.

Question: write a Clojure expression for the marker for the project.clj lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 2

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

At the edge of a stockpile at the edge of the forest, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the project.clj manifest for Leiningen.

Write a form whose evaluation gives the marker for the project.clj lesson.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 3

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

At the end of the harvest in the forest, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the project.clj manifest for Leiningen. Bit the ant touched it with a feeler and
said the form to remember was `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`; Skip the grasshopper
agreed to submit it.

Question: write a Clojure expression for the marker for the project.clj lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 4

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk in the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`. Hum
laughed, with a smug grin, and declared it too easy. Tic said patiently
that the only way to be sure of the project.clj manifest for Leiningen was to put it in the
REPL.

What Clojure form computes the marker for the project.clj lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 record 5

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

At the end of the harvest by the garden, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the project.clj manifest for Leiningen. Bit the ant touched it with a feeler and
said the form to remember was `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`; Skip the grasshopper
agreed to submit it.

Write a form whose evaluation gives the marker for the project.clj lesson.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

## G12-12: deps.edn projects

### G12-12 record 1

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate atop the hilltop: whoever
predicted the result of `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` first would set the next day's
ration. Toc the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the deps.edn manifest for the Clojure CLI.

Write a form whose evaluation gives the marker for the deps.edn lesson.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 2

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Hum the grasshopper, weary from the morning's effort from a season of song, was finally
willing to study patterns. Bit the ant pointed at the edge of the garden at
the deps.edn manifest for the Clojure CLI. The form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` was the canonical example;
the REPL would confirm what it produced.

Write a form whose evaluation gives the marker for the deps.edn lesson.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 3

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

"This isn't a song trick," Toc said in the woods, untroubled by what others thought. "It's a
tool." Hum the grasshopper looked at the deps.edn manifest for the Clojure CLI and admitted
they would not have known what to write. Toc sketched
`(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` on a slate so the runtime could speak for itself.

Write a form whose evaluation gives the marker for the deps.edn lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 4

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

"This isn't a song trick," Tic said in the garden, stepping deliberately. "It's a
tool." Skip the grasshopper looked at the deps.edn manifest for the Clojure CLI and admitted
she would not have known what to write. Tic sketched
`(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` on a slate so the runtime could speak for itself.

Write a Clojure expression that computes the marker for the deps.edn lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 record 5

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

"There is no need to evaluate that," Chirp the grasshopper said,
puffed up with pride. "Anyone can see what the deps.edn manifest for the Clojure CLI comes to."
Toc the ant, who at the edge of the forest had grown used to such claims, asked
him to actually write the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the marker for the deps.edn lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

## G12-13: Aliases and tools

### G12-13 record 1

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the alias-execution pattern with the Clojure CLI.

Write a form whose evaluation gives the marker for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 2

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the end of the harvest by the farm, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the alias-execution pattern with the Clojure CLI. Tic the ant touched it with a feeler and
said the form to remember was `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`; Chirp the grasshopper
agreed to submit it.

Write a Clojure expression that computes the marker for the aliases lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 3

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

The summer had ended on the hilltop and the two were sitting beneath an old
tree, comparing notes. Tic the ant drew the alias-execution pattern with the Clojure CLI into the
dust. "We've come a long way," he said. "The form
`(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` is the kind of thing we'd reach for now." Chirp
nodded — for once yawning at the soft moss enough to listen.

Write a Clojure expression that computes the marker for the aliases lesson.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 4

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

With a twig, Chirp the grasshopper marked out a wager by the farm: whoever
guessed the result of `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` first would win the right to
choose the next song. Tic the ant, without complaint, said it was easier
to ask the REPL about the alias-execution pattern with the Clojure CLI than to argue.

What Clojure form computes the marker for the aliases lesson? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 record 5

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Bit the ant had been keeping a small leather notebook of every form
they had successfully evaluated. Today in the forest, the next entry
was the alias-execution pattern with the Clojure CLI. Chirp the grasshopper peered over
their shoulder at the form `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` and asked what it
would come out to.

Question: write a Clojure expression for the marker for the aliases lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

## G12-14: Pedestal / Ring (web stack brief)

### G12-14 record 1

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered at the edge of the forest to watch
Skip the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the Ring HTTP-as-data abstraction and read out the form aloud:
`(do "Ring models HTTP as request-map -> response-map" :studied)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the marker for the Ring lesson.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 2

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(do "Ring models HTTP as request-map -> response-map" :studied)`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the Ring HTTP-as-data abstraction.

Write a form whose evaluation gives the marker for the Ring lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 3

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager at the edge of the hilltop: whoever
guessed the result of `(do "Ring models HTTP as request-map -> response-map" :studied)` first would win the right to
choose the next song. Bit the ant, stepping deliberately, said it was easier
to ask the REPL about the Ring HTTP-as-data abstraction than to argue.

What Clojure form computes the marker for the Ring lesson? Submit it via `eval`.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 4

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager at the edge of the farm: whoever
guessed the result of `(do "Ring models HTTP as request-map -> response-map" :studied)` first would win the right to
choose the next song. Tic the ant, saying very little, said it was easier
to ask the REPL about the Ring HTTP-as-data abstraction than to argue.

Write a form whose evaluation gives the marker for the Ring lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 record 5

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. near the hilltop, the
next entry was the Ring HTTP-as-data abstraction, and the form was `(do "Ring models HTTP as request-map -> response-map" :studied)`.
Chirp the grasshopper, puffed up with pride but more reflective than usual,
agreed to write the form into the REPL.

Write a Clojure expression that computes the marker for the Ring lesson.

---

I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

## G12-15: Datomic / XTDB (datalog db brief)

### G12-15 record 1

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

At the end of the harvest near the meadow, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the Datomic / XTDB family. Bit the ant touched it with a feeler and
said the form to remember was `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`; Skip the grasshopper
agreed to submit it.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 2

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Hum the grasshopper marked out a wager by the garden: whoever
guessed the result of `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` first would win the right to
choose the next song. Toc the ant, her eyes always on the path, said it was easier
to ask the REPL about the Datomic / XTDB family than to argue.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 3

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to the Datomic / XTDB family.
"You hand the form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, weary from the morning's effort, agreed to
try.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 4

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path in the forest and refused to step aside until someone
could prove what the form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the Datomic / XTDB family to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the marker for the datalog-DB lesson.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 record 5

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written the Datomic / XTDB family on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the marker for the datalog-DB lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

## G12-16: Reagent (cljs UI brief)

### G12-16 record 1

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

Toc the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. by the farm, the
next entry was the Reagent wrapper around React, and the form was `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`.
Hum the grasshopper, as if the race were already won but more reflective than usual,
agreed to write the form into the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 2

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Hum the grasshopper marked out a wager in the woods: whoever
guessed the result of `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` first would win the right to
choose the next song. Tic the ant, her eyes always on the path, said it was easier
to ask the REPL about the Reagent wrapper around React than to argue.

What Clojure form computes the marker for the Reagent lesson? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 3

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

Tic the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. by the woods, the
next entry was the Reagent wrapper around React, and the form was `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`.
Chirp the grasshopper, with a smug grin but more reflective than usual,
agreed to write the form into the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 4

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

At the end of the harvest near the forest, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the Reagent wrapper around React. Bit the ant touched it with a feeler and
said the form to remember was `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`; Chirp the grasshopper
agreed to submit it.

Write a Clojure expression that computes the marker for the Reagent lesson.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 record 5

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

Bit the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. at the edge of the garden, the
next entry was the Reagent wrapper around React, and the form was `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`.
Skip the grasshopper, swaggering through the underbrush but more reflective than usual,
agreed to write the form into the REPL.

Write a form whose evaluation gives the marker for the Reagent lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

## G12-17: Library design patterns

### G12-17 record 1

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place by the meadow.

Tic the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. in the meadow, the
next entry was the Clojure library-design hierarchy, and the form was `(do "good libraries expose data, then functions, then macros sparingly" :studied)`.
Skip the grasshopper, with a smug grin but more reflective than usual,
agreed to write the form into the REPL.

Question: write a Clojure expression for the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 2

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A banquet at the end of the season near the forest brought together every
creature who'd ever stockpiled. The day's discussion was
the Clojure library-design hierarchy. Bit wrote the form `(do "good libraries expose data, then functions, then macros sparingly" :studied)` on a square of
parchment and passed it across the table; Hum, her legs heavy from sprinting
but pleased, agreed to read it into the REPL.

Write a form whose evaluation gives the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 3

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. It happened in the orchard.

Toc the ant and Hum the grasshopper stopped in the orchard where someone had
written the Clojure library-design hierarchy on a flat stone. Hum, with great whoops of laughter,
declared that they could see the answer at a glance.
Toc, saying very little, suggested they actually evaluate the form
`(do "good libraries expose data, then functions, then macros sparingly" :studied)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 4

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"This isn't a song trick," Toc said in the garden, with steady, careful steps. "It's a
tool." Chirp the grasshopper looked at the Clojure library-design hierarchy and admitted
he would not have known what to write. Toc sketched
`(do "good libraries expose data, then functions, then macros sparingly" :studied)` on a slate so the runtime could speak for itself.

Write a Clojure expression that computes the marker for the library-design lesson.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 record 5

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the end of the harvest by the farm, a row of small monuments commemorated
the libraries the foragers had learned along the way. The newest one
honoured the Clojure library-design hierarchy. Toc the ant touched it with a feeler and
said the form to remember was `(do "good libraries expose data, then functions, then macros sparingly" :studied)`; Hum the grasshopper
agreed to submit it.

What Clojure form computes the marker for the library-design lesson? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

## G12-18: Clojure style guide

### G12-18 record 1

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

Skip the grasshopper, lulled by the gentle wind from a season of song, was finally
willing to study patterns. Toc the ant pointed by the farm at
the community-style basics. The form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` was the canonical example;
the REPL would confirm what it produced.

What Clojure form computes the marker for the style-guide lesson? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 2

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to the community-style basics.
"You hand the form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` to the runtime, and the runtime hands
you back what it evaluates to." Hum, weary from the morning's effort, agreed to
try.

Write a form whose evaluation gives the marker for the style-guide lesson.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 3

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had filled an entire notebook over the long summer with
tools and patterns: transducers, channels, specs, tests. in the farm, the
next entry was the community-style basics, and the form was `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`.
Hum the grasshopper, as if the race were already won but more reflective than usual,
agreed to write the form into the REPL.

Write a Clojure expression that computes the marker for the style-guide lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 4

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
All summer long, the Ant worked while the Grasshopper sang.

A small audience of meadow creatures had gathered atop the hilltop to watch
Skip the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the community-style basics and read out the form aloud:
`(do "kebab-case names, two-space indent, threading for deep nests" :studied)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the marker for the style-guide lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 record 5

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the garden.

A wooden sign nailed to a stalk near the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`. Hum
laughed, with great whoops of laughter, and declared it too easy. Toc said patiently
that the only way to be sure of the community-style basics was to put it in the
REPL.

Write a form whose evaluation gives the marker for the style-guide lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```


---

**Grade 12 totals: 18 subjects, 90 records.**
