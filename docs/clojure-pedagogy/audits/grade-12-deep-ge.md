# Grade 12 goose-eggs — deep spot-check

5 rendered records per subject (18 subjects × 5 = 90 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G12-01: Transducers introduction

**examples (2):**

- ex0: form=`(into [] (map inc) [1 2 3])` expected=`[2, 3, 4]`
    concept_phrase: `the transducer (map inc) used via into`
    question_what: `[1 2 3] each incremented through a transducer`
- ex1: form=`(into [] (filter even?) [1 2 3 4 5])` expected=`[2, 4]`
    concept_phrase: `the transducer (filter even?) used via into`
    question_what: `the even elements via a filter transducer`

### G12-01 sample 1/N (form: `(into [] (map inc) [1 2 3])`, expected: `[2, 3, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At the kitchen table near the market, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the transducer (map inc) used via into. Alice touched it
with a careful finger and said the form to remember was `(into [] (map inc) [1 2 3])`;
Carol agreed to submit it, untroubled by the village gossip that the basket
of eggs from Plume the goose no longer needed defending against
guesswork.

Write a Clojure expression that computes [1 2 3] each incremented through a transducer.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 sample 2/N (form: `(into [] (filter even?) [1 2 3 4 5])`, expected: `[2, 4]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small banquet at the close of the season at the edge of the farm brought together
every neighbour who'd traded with the farm. The day's discussion was
the transducer (filter even?) used via into. Alice wrote the form `(into [] (filter even?) [1 2 3 4 5])` on a square
of parchment and passed it across the table; Frank, untroubled by the village gossip
but pleased, agreed to read it into the REPL — Quill the goose watched
from the corner, untroubled by the long talk.

Question: write a Clojure expression for the even elements via a filter transducer.
---asst---
I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### G12-01 sample 3/N (form: `(into [] (map inc) [1 2 3])`, expected: `[2, 3, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

The season of morning-eggs had ended in the cellar, and Edward sat
with Casey comparing the year's ledgers. Edward drew
the transducer (map inc) used via into into the dust beside the basket. "We've come a long
way," he said, stepping deliberately. "The form `(into [] (map inc) [1 2 3])` is
the kind of thing we'd reach for now." Casey nodded — for once
calm in the morning routine enough to listen, with Plume the goose settled quietly
nearby.

What Clojure form computes [1 2 3] each incremented through a transducer? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-01 sample 4/N (form: `(into [] (filter even?) [1 2 3 4 5])`, expected: `[2, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the transducer (filter even?) used via into into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(into [] (filter even?) [1 2 3 4 5])` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the even elements via a filter transducer.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (filter even?) [1 2 3 4 5])"}}]}
```

### G12-01 sample 5/N (form: `(into [] (map inc) [1 2 3])`, expected: `[2, 3, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Bob offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(into [] (map inc) [1 2 3])` first would keep them.
Henry, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the transducer (map inc) used via into; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for [1 2 3] each incremented through a transducer.
---asst---
I let the REPL exercise the library form, the way the goose yields one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

## G12-02: Transducer composition

**examples (2):**

- ex0: form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4])` expected=`[2, 4]`
    concept_phrase: `the composed transducer (comp (map inc) (filter even?))`
    question_what: `the result of inc-then-keep-evens via a composed transducer`
- ex1: form=`(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` expected=`12`
    concept_phrase: `transduce with a composed transducer summing the kept items`
    question_what: `the sum after inc-then-keep-evens via transduce`

### G12-02 sample 1/N (form: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`, expected: `[2, 4]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

A small wooden notice nailed to a post inside the cellar carried a puzzle for
the village. The riddle asked the reader to evaluate `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`.
Oliver laughed, swaggering through the underbrush, and declared it too easy.
Henry said, her eyes always on the path, that the only honest way to know
the composed transducer (comp (map inc) (filter even?)) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 sample 2/N (form: `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])`, expected: `12`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small banquet at the close of the season at the edge of the village brought together
every neighbour who'd traded with the farm. The day's discussion was
transduce with a composed transducer summing the kept items. Oliver wrote the form `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])` on a square
of parchment and passed it across the table; Frank, untroubled by the village gossip
but pleased, agreed to read it into the REPL — Quill the goose watched
from the corner, untroubled by the long talk.

Write a Clojure expression that computes the sum after inc-then-keep-evens via transduce.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### G12-02 sample 3/N (form: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`, expected: `[2, 4]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

A small audience of neighbors had gathered by the farm to watch
Helen attempt to outguess Casey at reading the
REPL. Casey pointed to the composed transducer (comp (map inc) (filter even?)) and read out the form
aloud: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the result of inc-then-keep-evens via a composed transducer.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-02 sample 4/N (form: `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])`, expected: `12`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])`.
Charlie laughed, boasting at every turn, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
transduce with a composed transducer summing the kept items was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the sum after inc-then-keep-evens via transduce? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])"}}]}
```

### G12-02 sample 5/N (form: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`, expected: `[2, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

A row of three coins sat on the kitchen table near the market, set out as a
wager between George and Edward. The bet was
simple: predict what `(into [] (comp (map inc) (filter even?)) [1 2 3 4])` would return. George,
with hands itching to count more, was certain about the answer. Edward asked
him, untroubled by what others thought, to actually write the form into the
REPL — the composed transducer (comp (map inc) (filter even?)) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the result of inc-then-keep-evens via a composed transducer.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

## G12-03: into with a transducer (xform)

**examples (2):**

- ex0: form=`(into #{} (map inc) [1 2 3])` expected=`{2, 3, 4}`
    concept_phrase: `into a set with the (map inc) transducer`
    question_what: `the set produced by mapping inc into an empty set`
- ex1: form=`(into [] (take 3) (range 100))` expected=`[0, 1, 2]`
    concept_phrase: `into [] with the (take 3) transducer over (range 100)`
    question_what: `the first three items collected through a transducer`

### G12-03 sample 1/N (form: `(into #{} (map inc) [1 2 3])`, expected: `{2, 3, 4}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(into #{} (map inc) [1 2 3])` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — into a set with the (map inc) transducer would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the set produced by mapping inc into an empty set.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 sample 2/N (form: `(into [] (take 3) (range 100))`, expected: `[0, 1, 2]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alex had been trying to teach Robin how the REPL
works. "Here," they said, pointing to into [] with the (take 3) transducer over (range 100).
"You hand the form `(into [] (take 3) (range 100))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the first three items collected through a transducer.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### G12-03 sample 3/N (form: `(into #{} (map inc) [1 2 3])`, expected: `{2, 3, 4}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

Robin, regretting the hasty thought after a season of trying to
shortcut every egg-count, was finally willing to study patterns.
Grace pointed by the meadow at into a set with the (map inc) transducer. The form
`(into #{} (map inc) [1 2 3])` was the canonical example; the REPL would confirm what
it produced, the way Plume the goose would yield the next morning's
egg in its own time.

Question: write a Clojure expression for the set produced by mapping inc into an empty set.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-03 sample 4/N (form: `(into [] (take 3) (range 100))`, expected: `[0, 1, 2]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched into [] with the (take 3) transducer over (range 100) into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(into [] (take 3) (range 100))` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the first three items collected through a transducer? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into [] (take 3) (range 100))"}}]}
```

### G12-03 sample 5/N (form: `(into #{} (map inc) [1 2 3])`, expected: `{2, 3, 4}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Emily had filled an entire leather ledger over the long
season with tools and patterns: transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines. at the edge of the market, the next entry was
into a set with the (map inc) transducer, and the form was `(into #{} (map inc) [1 2 3])`. Carol,
with great whoops of laughter but more reflective than usual, agreed to write the form
into the REPL while Quill the goose watched.

Write a Clojure expression that computes the set produced by mapping inc into an empty set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

## G12-04: core.async introduction

**examples (2):**

- ex0: form=`(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` expected=`':studied'`
    concept_phrase: `the core.async primitives chan/go/<!/>!`
    question_what: `the marker for the core.async lesson`
- ex1: form=`(do "go-blocks let you write async code as if it were synchronous" :async)` expected=`':async'`
    concept_phrase: `what go blocks give you`
    question_what: `the marker keyword for go-blocks`

### G12-04 sample 1/N (form: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the cellar to watch
Charlie attempt to outguess Alice at reading the
REPL. Alice pointed to the core.async primitives chan/go/<!/>! and read out the form
aloud: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the marker for the core.async lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 sample 2/N (form: `(do "go-blocks let you write async code as if it were synchronous" :async)`, expected: `':async'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

Halfway through the morning errand, Bob stopped in the orchard
with a basket of eggs and refused to move on until someone could
prove what the form `(do "go-blocks let you write async code as if it were synchronous" :async)` evaluated to. Bob called it
impossible. Grace, walking up at an unhurried pace, simply
said: "Submit what go blocks give you to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a form whose evaluation gives the marker keyword for go-blocks.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### G12-04 sample 3/N (form: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Henry said, with great whoops of laughter.
"Anyone with eyes can see what the core.async primitives chan/go/<!/>! comes to."
Robin, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the marker for the core.async lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-04 sample 4/N (form: `(do "go-blocks let you write async code as if it were synchronous" :async)`, expected: `':async'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry offered a small basket of eggs as a wager inside a cottage:
whoever guessed the result of `(do "go-blocks let you write async code as if it were synchronous" :async)` first would keep them.
Charlie, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about what go blocks give you; the eggs,
after all, would still be there once Quill the goose laid the next
one.

What Clojure form computes the marker keyword for go-blocks? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"go-blocks let you write async code as if it were synchronous\" :async)"}}]}
```

### G12-04 sample 5/N (form: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Frank had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the farm, the
next entry was the core.async primitives chan/go/<!/>!. Helen peered over
his shoulder at the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` and asked what
it would come out to.

Write a Clojure expression that computes the marker for the core.async lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

## G12-05: Channels and pipelines

**examples (2):**

- ex0: form=`(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` expected=`':studied'`
    concept_phrase: `the pipeline operators in core.async`
    question_what: `the marker for the channel-pipeline lesson`
- ex1: form=`(do "pipelines transform streams of values channel-to-channel" :pipelines)` expected=`':pipelines'`
    concept_phrase: `the role of pipelines in async code`
    question_what: `the marker keyword for pipelines`

### G12-05 sample 1/N (form: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Beatrice said, as if the race were already won.
"Anyone with eyes can see what the pipeline operators in core.async comes to."
Fiona, who deep inside the cellar had grown used to such claims, asked
her to actually write the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the marker for the channel-pipeline lesson.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 sample 2/N (form: `(do "pipelines transform streams of values channel-to-channel" :pipelines)`, expected: `':pipelines'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At the kitchen table near the market, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the role of pipelines in async code. Charlie touched it
with a careful finger and said the form to remember was `(do "pipelines transform streams of values channel-to-channel" :pipelines)`;
Beatrice agreed to submit it, settled and unhurried that the basket
of eggs from Quill the goose no longer needed defending against
guesswork.

Write a form whose evaluation gives the marker keyword for pipelines.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### G12-05 sample 3/N (form: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

"There is no need to evaluate that," Carol said, swaggering through the underbrush.
"Anyone with eyes can see what the pipeline operators in core.async comes to."
David, who in the village had grown used to such claims, asked
her to actually write the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the marker for the channel-pipeline lesson.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-05 sample 4/N (form: `(do "pipelines transform streams of values channel-to-channel" :pipelines)`, expected: `':pipelines'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small banquet at the close of the season near the meadow brought together
every neighbour who'd traded with the farm. The day's discussion was
the role of pipelines in async code. Frank wrote the form `(do "pipelines transform streams of values channel-to-channel" :pipelines)` on a square
of parchment and passed it across the table; Emily, grateful for every coin
but pleased, agreed to read it into the REPL — Quill the goose watched
from the corner, untroubled by the long talk.

What Clojure form computes the marker keyword for pipelines? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipelines transform streams of values channel-to-channel\" :pipelines)"}}]}
```

### G12-05 sample 5/N (form: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

David had been trying to teach Frank how the REPL
works. "Here," he said, pointing to the pipeline operators in core.async.
"You hand the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the marker for the channel-pipeline lesson.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

## G12-06: clojure.spec

**examples (2):**

- ex0: form=`(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` expected=`True`
    concept_phrase: `(s/valid? int? 42) — a basic spec check`
    question_what: `whether 42 conforms to the int? spec`
- ex1: form=`(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` expected=`False`
    concept_phrase: `(s/valid? string? 42) — a failing spec check`
    question_what: `whether 42 conforms to the string? spec`

### G12-06 sample 1/N (form: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

The season of morning-eggs had ended by the farm, and Henry sat
with Edward comparing the year's ledgers. Henry drew
(s/valid? int? 42) — a basic spec check into the dust beside the basket. "We've come a long
way," he said, saying very little. "The form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` is
the kind of thing we'd reach for now." Edward nodded — for once
settled and unhurried enough to listen, with Honk the goose settled quietly
nearby.

Write a form whose evaluation gives whether 42 conforms to the int? spec.
---asst---
I let the REPL exercise the library form, the way the goose yields one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 sample 2/N (form: `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small banquet at the close of the season at the edge of the market brought together
every neighbour who'd traded with the farm. The day's discussion was
(s/valid? string? 42) — a failing spec check. Casey wrote the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))` on a square
of parchment and passed it across the table; Fiona, pleased with the steady fortune
but pleased, agreed to read it into the REPL — Plume the goose watched
from the corner, untroubled by the long talk.

Question: write a Clojure expression for whether 42 conforms to the string? spec.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### G12-06 sample 3/N (form: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched (s/valid? int? 42) — a basic spec check into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes whether 42 conforms to the int? spec? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-06 sample 4/N (form: `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Emily had filled an entire leather ledger over the long
season with tools and patterns: transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines. deep inside the kitchen, the next entry was
(s/valid? string? 42) — a failing spec check, and the form was `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))`. Edward,
swaggering through the underbrush but more reflective than usual, agreed to write the form
into the REPL while Honk the goose watched.

Write a Clojure expression that computes whether 42 conforms to the string? spec.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? string? 42))"}}]}
```

### G12-06 sample 5/N (form: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

"This isn't a market trick to fool the buyers," Alice said in the barn,
untroubled by what others thought. "It's a tool for the whole farmhouse." Fiona
looked at (s/valid? int? 42) — a basic spec check and admitted she would not
have known what to write — the old greed for quick answers had
nothing to offer here. Alice sketched `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` on a slate so
the runtime could speak for itself, the way Plume the goose let each
egg speak for the morning.

Write a Clojure expression that computes whether 42 conforms to the int? spec.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

## G12-07: Spec generators

**examples (2):**

- ex0: form=`(do "s/exercise produces sample inputs for a spec" :studied)` expected=`':studied'`
    concept_phrase: `what s/exercise does`
    question_what: `the marker for the spec-generators lesson`
- ex1: form=`(do "spec generators turn specs into property-based test inputs" :gens)` expected=`':gens'`
    concept_phrase: `the role of spec generators`
    question_what: `the marker keyword for spec generators`

### G12-07 sample 1/N (form: `(do "s/exercise produces sample inputs for a spec" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

At the kitchen table by the market, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured what s/exercise does. David touched it
with a careful finger and said the form to remember was `(do "s/exercise produces sample inputs for a spec" :studied)`;
Robin agreed to submit it, pleased with the steady fortune that the basket
of eggs from Quill the goose no longer needed defending against
guesswork.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 sample 2/N (form: `(do "spec generators turn specs into property-based test inputs" :gens)`, expected: `':gens'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

At the kitchen table deep inside the kitchen, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the role of spec generators. David touched it
with a careful finger and said the form to remember was `(do "spec generators turn specs into property-based test inputs" :gens)`;
Edward agreed to submit it, pleased with the steady fortune that the basket
of eggs from Plume the goose no longer needed defending against
guesswork.

What Clojure form computes the marker keyword for spec generators? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### G12-07 sample 3/N (form: `(do "s/exercise produces sample inputs for a spec" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small banquet at the close of the season deep inside the cellar brought together
every neighbour who'd traded with the farm. The day's discussion was
what s/exercise does. Fiona wrote the form `(do "s/exercise produces sample inputs for a spec" :studied)` on a square
of parchment and passed it across the table; Sam, pleased with the steady fortune
but pleased, agreed to read it into the REPL — Plume the goose watched
from the corner, untroubled by the long talk.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-07 sample 4/N (form: `(do "spec generators turn specs into property-based test inputs" :gens)`, expected: `':gens'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the market, the
next entry was the role of spec generators. George peered over
their shoulder at the form `(do "spec generators turn specs into property-based test inputs" :gens)` and asked what
it would come out to.

What Clojure form computes the marker keyword for spec generators? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"spec generators turn specs into property-based test inputs\" :gens)"}}]}
```

### G12-07 sample 5/N (form: `(do "s/exercise produces sample inputs for a spec" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

"This isn't a market trick to fool the buyers," Helen said deep inside a cottage,
untroubled by what others thought. "It's a tool for the whole farmhouse." Robin
looked at what s/exercise does and admitted they would not
have known what to write — the old greed for quick answers had
nothing to offer here. Helen sketched `(do "s/exercise produces sample inputs for a spec" :studied)` on a slate so
the runtime could speak for itself, the way Plume the goose let each
egg speak for the morning.

What Clojure form computes the marker for the spec-generators lesson? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

## G12-08: clojure.test

**examples (2):**

- ex0: form=`(= (+ 1 2) 3)` expected=`True`
    concept_phrase: `(= (+ 1 2) 3) — what an `is` would test`
    question_what: `the truth value an `is` assertion would record`
- ex1: form=`(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` expected=`':studied'`
    concept_phrase: `the clojure.test core forms`
    question_what: `the marker for the clojure.test lesson`

### G12-08 sample 1/N (form: `(= (+ 1 2) 3)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

Oliver, wishing for more careful counting after a season of trying to
shortcut every egg-count, was finally willing to study patterns.
Bob pointed in the village at (= (+ 1 2) 3) — what an `is` would test. The form
`(= (+ 1 2) 3)` was the canonical example; the REPL would confirm what
it produced, the way Plume the goose would yield the next morning's
egg in its own time.

Write a form whose evaluation gives the truth value an `is` assertion would record.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 sample 2/N (form: `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Morgan said, puffed up with pride.
"Anyone with eyes can see what the clojure.test core forms comes to."
George, who in the barn had grown used to such claims, asked
them to actually write the form `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the marker for the clojure.test lesson.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### G12-08 sample 3/N (form: `(= (+ 1 2) 3)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(= (+ 1 2) 3)` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — (= (+ 1 2) 3) — what an `is` would test would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the truth value an `is` assertion would record.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-08 sample 4/N (form: `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

At the kitchen table deep inside the cellar, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the clojure.test core forms. George touched it
with a careful finger and said the form to remember was `(do "(deftest …), (is …), (testing …) are the core test forms" :studied)`;
Casey agreed to submit it, calm in the morning routine that the basket
of eggs from Honk the goose no longer needed defending against
guesswork.

Question: write a Clojure expression for the marker for the clojure.test lesson.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(deftest …), (is …), (testing …) are the core test forms\" :studied)"}}]}
```

### G12-08 sample 5/N (form: `(= (+ 1 2) 3)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

A small audience of neighbors had gathered in the cellar to watch
Bob attempt to outguess Helen at reading the
REPL. Helen pointed to (= (+ 1 2) 3) — what an `is` would test and read out the form
aloud: `(= (+ 1 2) 3)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

What Clojure form computes the truth value an `is` assertion would record? Submit it via `eval`.
---asst---
I let the REPL exercise the library form, the way the goose yields one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

## G12-09: Test fixtures

**examples (2):**

- ex0: form=`(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` expected=`':studied'`
    concept_phrase: `use-fixtures and the fixture pattern`
    question_what: `the marker for the fixtures lesson`
- ex1: form=`(do "fixtures provide setup/teardown around deftests" :fixtures)` expected=`':fixtures'`
    concept_phrase: `the purpose of fixtures`
    question_what: `the marker keyword for the fixture lesson`

### G12-09 sample 1/N (form: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," George said, swaggering through the underbrush.
"Anyone with eyes can see what use-fixtures and the fixture pattern comes to."
Oliver, who in the village had grown used to such claims, asked
him to actually write the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the marker for the fixtures lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 sample 2/N (form: `(do "fixtures provide setup/teardown around deftests" :fixtures)`, expected: `':fixtures'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, David stopped inside the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do "fixtures provide setup/teardown around deftests" :fixtures)` evaluated to. David called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the purpose of fixtures to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the marker keyword for the fixture lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### G12-09 sample 3/N (form: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

A small wooden notice nailed to a post at the edge of the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`.
George laughed, boasting at every turn, and declared it too easy.
Casey said, untroubled by what others thought, that the only honest way to know
use-fixtures and the fixture pattern was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the marker for the fixtures lesson.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-09 sample 4/N (form: `(do "fixtures provide setup/teardown around deftests" :fixtures)`, expected: `':fixtures'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Charlie had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today inside a cottage, the
next entry was the purpose of fixtures. Jordan peered over
his shoulder at the form `(do "fixtures provide setup/teardown around deftests" :fixtures)` and asked what
it would come out to.

Write a Clojure expression that computes the marker keyword for the fixture lesson.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"fixtures provide setup/teardown around deftests\" :fixtures)"}}]}
```

### G12-09 sample 5/N (form: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

Beatrice had been trying to teach George how the REPL
works. "Here," she said, pointing to use-fixtures and the fixture pattern.
"You hand the form `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the marker for the fixtures lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

## G12-10: Property-based testing

**examples (2):**

- ex0: form=`(= (reverse (reverse [1 2 3])) [1 2 3])` expected=`True`
    concept_phrase: `the property that double-reverse is identity`
    question_what: `the truth value of the double-reverse property on [1 2 3]`
- ex1: form=`(do "test.check generates inputs and checks properties hold" :studied)` expected=`':studied'`
    concept_phrase: `what test.check does`
    question_what: `the marker for property-based testing`

### G12-10 sample 1/N (form: `(= (reverse (reverse [1 2 3])) [1 2 3])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A small banquet at the close of the season deep inside the kitchen brought together
every neighbour who'd traded with the farm. The day's discussion was
the property that double-reverse is identity. Alex wrote the form `(= (reverse (reverse [1 2 3])) [1 2 3])` on a square
of parchment and passed it across the table; Fiona, calm in the morning routine
but pleased, agreed to read it into the REPL — Honk the goose watched
from the corner, untroubled by the long talk.

Write a Clojure expression that computes the truth value of the double-reverse property on [1 2 3].
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 sample 2/N (form: `(do "test.check generates inputs and checks properties hold" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do "test.check generates inputs and checks properties hold" :studied)` evaluated to. Morgan called it
impossible. Bob, walking up at an unhurried pace, simply
said: "Submit what test.check does to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

What Clojure form computes the marker for property-based testing? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### G12-10 sample 3/N (form: `(= (reverse (reverse [1 2 3])) [1 2 3])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

A small wooden notice nailed to a post in the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(= (reverse (reverse [1 2 3])) [1 2 3])`.
Emily laughed, swaggering through the underbrush, and declared it too easy.
Carol said, saying very little, that the only honest way to know
the property that double-reverse is identity was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the truth value of the double-reverse property on [1 2 3].
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-10 sample 4/N (form: `(do "test.check generates inputs and checks properties hold" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Grace had filled an entire leather ledger over the long
season with tools and patterns: transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines. in the village, the next entry was
what test.check does, and the form was `(do "test.check generates inputs and checks properties hold" :studied)`. Robin,
swaggering through the underbrush but more reflective than usual, agreed to write the form
into the REPL while Plume the goose watched.

Write a form whose evaluation gives the marker for property-based testing.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"test.check generates inputs and checks properties hold\" :studied)"}}]}
```

### G12-10 sample 5/N (form: `(= (reverse (reverse [1 2 3])) [1 2 3])`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Fiona had been trying to teach Frank how the REPL
works. "Here," she said, pointing to the property that double-reverse is identity.
"You hand the form `(= (reverse (reverse [1 2 3])) [1 2 3])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the truth value of the double-reverse property on [1 2 3].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

## G12-11: Leiningen project.clj

**examples (2):**

- ex0: form=`(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` expected=`':studied'`
    concept_phrase: `the project.clj manifest for Leiningen`
    question_what: `the marker for the project.clj lesson`
- ex1: form=`(do "Leiningen reads project.clj at the project root" :lein)` expected=`':lein'`
    concept_phrase: `where Leiningen finds project.clj`
    question_what: `the marker keyword for the Leiningen lesson`

### G12-11 sample 1/N (form: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

A row of three coins sat on the kitchen table in the village, set out as a
wager between Charlie and George. The bet was
simple: predict what `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` would return. Charlie,
imagining all that might be gained, was certain about the answer. George asked
him, with steady, careful steps, to actually write the form into the
REPL — the project.clj manifest for Leiningen would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the marker for the project.clj lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 sample 2/N (form: `(do "Leiningen reads project.clj at the project root" :lein)`, expected: `':lein'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Morgan stopped in the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(do "Leiningen reads project.clj at the project root" :lein)` evaluated to. Morgan called it
impossible. Edward, walking up at an unhurried pace, simply
said: "Submit where Leiningen finds project.clj to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the marker keyword for the Leiningen lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### G12-11 sample 3/N (form: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the project.clj manifest for Leiningen — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the marker for the project.clj lesson.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-11 sample 4/N (form: `(do "Leiningen reads project.clj at the project root" :lein)`, expected: `':lein'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(do "Leiningen reads project.clj at the project root" :lein)` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about where Leiningen finds project.clj; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the marker keyword for the Leiningen lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Leiningen reads project.clj at the project root\" :lein)"}}]}
```

### G12-11 sample 5/N (form: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Fiona had filled an entire leather ledger over the long
season with tools and patterns: transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines. deep inside the kitchen, the next entry was
the project.clj manifest for Leiningen, and the form was `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`. Sam,
swaggering through the underbrush but more reflective than usual, agreed to write the form
into the REPL while Quill the goose watched.

Write a form whose evaluation gives the marker for the project.clj lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

## G12-12: deps.edn projects

**examples (2):**

- ex0: form=`(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` expected=`':studied'`
    concept_phrase: `the deps.edn manifest for the Clojure CLI`
    question_what: `the marker for the deps.edn lesson`
- ex1: form=`(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` expected=`':deps'`
    concept_phrase: `who reads deps.edn`
    question_what: `the marker keyword for the deps.edn lesson`

### G12-12 sample 1/N (form: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

A small audience of neighbors had gathered near the village to watch
Fiona attempt to outguess Helen at reading the
REPL. Helen pointed to the deps.edn manifest for the Clojure CLI and read out the form
aloud: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the marker for the deps.edn lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 sample 2/N (form: `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`, expected: `':deps'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

A row of three coins sat on the kitchen table in a cottage, set out as a
wager between Robin and Bob. The bet was
simple: predict what `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` would return. Robin,
with a hungry gleam in the eye, was certain about the answer. Bob asked
them, with steady, careful steps, to actually write the form into the
REPL — who reads deps.edn would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes the marker keyword for the deps.edn lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### G12-12 sample 3/N (form: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the deps.edn manifest for the Clojure CLI — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the marker for the deps.edn lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-12 sample 4/N (form: `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)`, expected: `':deps'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"This isn't a market trick to fool the buyers," Morgan said inside the barn,
stepping deliberately. "It's a tool for the whole farmhouse." Sam
looked at who reads deps.edn and admitted they would not
have known what to write — the old greed for quick answers had
nothing to offer here. Morgan sketched `(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)` on a slate so
the runtime could speak for itself, the way Quill the goose let each
egg speak for the morning.

What Clojure form computes the marker keyword for the deps.edn lesson? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn is read by the official `clj`/`clojure` tools\" :deps)"}}]}
```

### G12-12 sample 5/N (form: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small banquet at the close of the season by the meadow brought together
every neighbour who'd traded with the farm. The day's discussion was
the deps.edn manifest for the Clojure CLI. Morgan wrote the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` on a square
of parchment and passed it across the table; Oliver, happy with the day's small gift
but pleased, agreed to read it into the REPL — Quill the goose watched
from the corner, untroubled by the long talk.

What Clojure form computes the marker for the deps.edn lesson? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

## G12-13: Aliases and tools

**examples (2):**

- ex0: form=`(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` expected=`':studied'`
    concept_phrase: `the alias-execution pattern with the Clojure CLI`
    question_what: `the marker for the aliases lesson`
- ex1: form=`(do "aliases compose extra paths, deps, and main opts" :aliases)` expected=`':aliases'`
    concept_phrase: `what aliases let you compose`
    question_what: `the marker keyword for the aliases lesson`

### G12-13 sample 1/N (form: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

At the kitchen table at the edge of the market, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the alias-execution pattern with the Clojure CLI. Alice touched it
with a careful finger and said the form to remember was `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`;
Sam agreed to submit it, settled and unhurried that the basket
of eggs from Plume the goose no longer needed defending against
guesswork.

Write a form whose evaluation gives the marker for the aliases lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 sample 2/N (form: `(do "aliases compose extra paths, deps, and main opts" :aliases)`, expected: `':aliases'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

Helen offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do "aliases compose extra paths, deps, and main opts" :aliases)` first would keep them.
Oliver, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about what aliases let you compose; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for the marker keyword for the aliases lesson.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### G12-13 sample 3/N (form: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

"This isn't a market trick to fool the buyers," Diana said inside a cottage,
untroubled by what others thought. "It's a tool for the whole farmhouse." Robin
looked at the alias-execution pattern with the Clojure CLI and admitted they would not
have known what to write — the old greed for quick answers had
nothing to offer here. Diana sketched `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` on a slate so
the runtime could speak for itself, the way Honk the goose let each
egg speak for the morning.

What Clojure form computes the marker for the aliases lesson? Submit it via `eval`.
---asst---
I write the form using the appropriate library or tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-13 sample 4/N (form: `(do "aliases compose extra paths, deps, and main opts" :aliases)`, expected: `':aliases'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered in the kitchen to watch
Carol attempt to outguess Grace at reading the
REPL. Grace pointed to what aliases let you compose and read out the form
aloud: `(do "aliases compose extra paths, deps, and main opts" :aliases)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the marker keyword for the aliases lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"aliases compose extra paths, deps, and main opts\" :aliases)"}}]}
```

### G12-13 sample 5/N (form: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — the alias-execution pattern with the Clojure CLI would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the marker for the aliases lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

## G12-14: Pedestal / Ring (web stack brief)

**examples (2):**

- ex0: form=`(do "Ring models HTTP as request-map -> response-map" :studied)` expected=`':studied'`
    concept_phrase: `the Ring HTTP-as-data abstraction`
    question_what: `the marker for the Ring lesson`
- ex1: form=`(do "Pedestal layers interceptors over Ring for richer pipelines" :web)` expected=`':web'`
    concept_phrase: `the Pedestal interceptor model`
    question_what: `the marker keyword for the Pedestal lesson`

### G12-14 sample 1/N (form: `(do "Ring models HTTP as request-map -> response-map" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

The season of morning-eggs had ended by the village, and Grace sat
with Diana comparing the year's ledgers. Grace drew
the Ring HTTP-as-data abstraction into the dust beside the basket. "We've come a long
way," she said, with steady, careful steps. "The form `(do "Ring models HTTP as request-map -> response-map" :studied)` is
the kind of thing we'd reach for now." Diana nodded — for once
pleased with the steady fortune enough to listen, with Quill the goose settled quietly
nearby.

Write a Clojure expression that computes the marker for the Ring lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 sample 2/N (form: `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`, expected: `':web'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At the kitchen table in the market, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the Pedestal interceptor model. Edward touched it
with a careful finger and said the form to remember was `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`;
George agreed to submit it, untroubled by the village gossip that the basket
of eggs from Plume the goose no longer needed defending against
guesswork.

What Clojure form computes the marker keyword for the Pedestal lesson? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### G12-14 sample 3/N (form: `(do "Ring models HTTP as request-map -> response-map" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

The season of morning-eggs had ended in the meadow, and Edward sat
with David comparing the year's ledgers. Edward drew
the Ring HTTP-as-data abstraction into the dust beside the basket. "We've come a long
way," he said, her eyes always on the path. "The form `(do "Ring models HTTP as request-map -> response-map" :studied)` is
the kind of thing we'd reach for now." David nodded — for once
settled and unhurried enough to listen, with Plume the goose settled quietly
nearby.

Question: write a Clojure expression for the marker for the Ring lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-14 sample 4/N (form: `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`, expected: `':web'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

At the kitchen table in the barn, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the Pedestal interceptor model. Casey touched it
with a careful finger and said the form to remember was `(do "Pedestal layers interceptors over Ring for richer pipelines" :web)`;
Jordan agreed to submit it, settled and unhurried that the basket
of eggs from Quill the goose no longer needed defending against
guesswork.

Question: write a Clojure expression for the marker keyword for the Pedestal lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Pedestal layers interceptors over Ring for richer pipelines\" :web)"}}]}
```

### G12-14 sample 5/N (form: `(do "Ring models HTTP as request-map -> response-map" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

At the kitchen table deep inside a cottage, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured the Ring HTTP-as-data abstraction. Alice touched it
with a careful finger and said the form to remember was `(do "Ring models HTTP as request-map -> response-map" :studied)`;
Bob agreed to submit it, grateful for every coin that the basket
of eggs from Quill the goose no longer needed defending against
guesswork.

What Clojure form computes the marker for the Ring lesson? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

## G12-15: Datomic / XTDB (datalog db brief)

**examples (2):**

- ex0: form=`(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` expected=`':studied'`
    concept_phrase: `the Datomic / XTDB family`
    question_what: `the marker for the datalog-DB lesson`
- ex1: form=`(do "queries are written in datalog over EDN-shaped data" :datalog)` expected=`':datalog'`
    concept_phrase: `how queries look in these databases`
    question_what: `the marker keyword for datalog queries`

### G12-15 sample 1/N (form: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the Datomic / XTDB family; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the marker for the datalog-DB lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 sample 2/N (form: `(do "queries are written in datalog over EDN-shaped data" :datalog)`, expected: `':datalog'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

The season of morning-eggs had ended deep inside the cellar, and Charlie sat
with David comparing the year's ledgers. Charlie drew
how queries look in these databases into the dust beside the basket. "We've come a long
way," he said, with steady, careful steps. "The form `(do "queries are written in datalog over EDN-shaped data" :datalog)` is
the kind of thing we'd reach for now." David nodded — for once
pleased with the steady fortune enough to listen, with Quill the goose settled quietly
nearby.

Question: write a Clojure expression for the marker keyword for datalog queries.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### G12-15 sample 3/N (form: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

The season of morning-eggs had ended at the edge of the meadow, and Casey sat
with Alex comparing the year's ledgers. Casey drew
the Datomic / XTDB family into the dust beside the basket. "We've come a long
way," they said, with steady, careful steps. "The form `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)` is
the kind of thing we'd reach for now." Alex nodded — for once
settled and unhurried enough to listen, with Plume the goose settled quietly
nearby.

Write a form whose evaluation gives the marker for the datalog-DB lesson.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-15 sample 4/N (form: `(do "queries are written in datalog over EDN-shaped data" :datalog)`, expected: `':datalog'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Diana had filled an entire leather ledger over the long
season with tools and patterns: transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines. near the orchard, the next entry was
how queries look in these databases, and the form was `(do "queries are written in datalog over EDN-shaped data" :datalog)`. Robin,
with a smug grin but more reflective than usual, agreed to write the form
into the REPL while Honk the goose watched.

Question: write a Clojure expression for the marker keyword for datalog queries.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"queries are written in datalog over EDN-shaped data\" :datalog)"}}]}
```

### G12-15 sample 5/N (form: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post in the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`.
Bob laughed, boasting at every turn, and declared it too easy.
Sam said, her eyes always on the path, that the only honest way to know
the Datomic / XTDB family was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the marker for the datalog-DB lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

## G12-16: Reagent (cljs UI brief)

**examples (2):**

- ex0: form=`(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` expected=`':studied'`
    concept_phrase: `the Reagent wrapper around React`
    question_what: `the marker for the Reagent lesson`
- ex1: form=`(do "components are functions returning Hiccup vectors" :reagent)` expected=`':reagent'`
    concept_phrase: `how Reagent components are written`
    question_what: `the marker keyword for Reagent components`

### G12-16 sample 1/N (form: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post by the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`.
Sam laughed, as if the race were already won, and declared it too easy.
Alice said, stepping deliberately, that the only honest way to know
the Reagent wrapper around React was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the marker for the Reagent lesson.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 sample 2/N (form: `(do "components are functions returning Hiccup vectors" :reagent)`, expected: `':reagent'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Fiona offered a small basket of eggs as a wager deep inside the barn:
whoever guessed the result of `(do "components are functions returning Hiccup vectors" :reagent)` first would keep them.
Frank, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about how Reagent components are written; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the marker keyword for Reagent components.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### G12-16 sample 3/N (form: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — the Reagent wrapper around React would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the marker for the Reagent lesson.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-16 sample 4/N (form: `(do "components are functions returning Hiccup vectors" :reagent)`, expected: `':reagent'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

The season of morning-eggs had ended in the market, and Carol sat
with David comparing the year's ledgers. Carol drew
how Reagent components are written into the dust beside the basket. "We've come a long
way," she said, stepping deliberately. "The form `(do "components are functions returning Hiccup vectors" :reagent)` is
the kind of thing we'd reach for now." David nodded — for once
settled and unhurried enough to listen, with Quill the goose settled quietly
nearby.

Write a Clojure expression that computes the marker keyword for Reagent components.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"components are functions returning Hiccup vectors\" :reagent)"}}]}
```

### G12-16 sample 5/N (form: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

The season of morning-eggs had ended inside the barn, and Emily sat
with Bob comparing the year's ledgers. Emily drew
the Reagent wrapper around React into the dust beside the basket. "We've come a long
way," she said, stepping deliberately. "The form `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)` is
the kind of thing we'd reach for now." Bob nodded — for once
settled and unhurried enough to listen, with Plume the goose settled quietly
nearby.

Write a Clojure expression that computes the marker for the Reagent lesson.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

## G12-17: Library design patterns

**examples (3):**

- ex0: form=`(do "good libraries expose data, then functions, then macros sparingly" :studied)` expected=`':studied'`
    concept_phrase: `the Clojure library-design hierarchy`
    question_what: `the marker for the library-design lesson`
- ex1: form=`(do "small public API surface, plain data inputs, return values" :design)` expected=`':design'`
    concept_phrase: `the conventional Clojure API shape`
    question_what: `the marker keyword for the API-shape lesson`
- ex2: form=`(= [1 2 3] (vec '(1 2 3)))` expected=`True`
    concept_phrase: `a tiny example of a data-first conversion at the API edge`
    question_what: `whether the vector and the converted seq are equal`

### G12-17 sample 1/N (form: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"This isn't a market trick to fool the buyers," Oliver said in the kitchen,
her eyes always on the path. "It's a tool for the whole farmhouse." Grace
looked at the Clojure library-design hierarchy and admitted she would not
have known what to write — the old greed for quick answers had
nothing to offer here. Oliver sketched `(do "good libraries expose data, then functions, then macros sparingly" :studied)` on a slate so
the runtime could speak for itself, the way Quill the goose let each
egg speak for the morning.

Write a Clojure expression that computes the marker for the library-design lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 sample 2/N (form: `(do "small public API surface, plain data inputs, return values" :design)`, expected: `':design'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alex, thinking better of the rash impulse after a season of trying to
shortcut every egg-count, was finally willing to study patterns.
Fiona pointed in the village at the conventional Clojure API shape. The form
`(do "small public API surface, plain data inputs, return values" :design)` was the canonical example; the REPL would confirm what
it produced, the way Plume the goose would yield the next morning's
egg in its own time.

Question: write a Clojure expression for the marker keyword for the API-shape lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

### G12-17 sample 3/N (form: `(= [1 2 3] (vec '(1 2 3)))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

A small banquet at the close of the season inside the cellar brought together
every neighbour who'd traded with the farm. The day's discussion was
a tiny example of a data-first conversion at the API edge. Fiona wrote the form `(= [1 2 3] (vec '(1 2 3)))` on a square
of parchment and passed it across the table; Morgan, content with the quiet life
but pleased, agreed to read it into the REPL — Honk the goose watched
from the corner, untroubled by the long talk.

Write a form whose evaluation gives whether the vector and the converted seq are equal.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] (vec '(1 2 3)))"}}]}
```

### G12-17 sample 4/N (form: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

At a small stall in the farm, someone had chalked a wager: whoever
predicted the result of `(do "good libraries expose data, then functions, then macros sparingly" :studied)` first would set the asking
price for the morning's eggs. Edward, her eyes always on the path, said it
was easier to type the form into the REPL than to argue about
the Clojure library-design hierarchy — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the marker for the library-design lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-17 sample 5/N (form: `(do "small public API surface, plain data inputs, return values" :design)`, expected: `':design'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol, shaking off a careless idea after a season of trying to
shortcut every egg-count, was finally willing to study patterns.
Alex pointed inside the kitchen at the conventional Clojure API shape. The form
`(do "small public API surface, plain data inputs, return values" :design)` was the canonical example; the REPL would confirm what
it produced, the way Honk the goose would yield the next morning's
egg in its own time.

Write a Clojure expression that computes the marker keyword for the API-shape lesson.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"small public API surface, plain data inputs, return values\" :design)"}}]}
```

## G12-18: Clojure style guide

**examples (2):**

- ex0: form=`(do "kebab-case names, two-space indent, threading for deep nests" :studied)` expected=`':studied'`
    concept_phrase: `the community-style basics`
    question_what: `the marker for the style-guide lesson`
- ex1: form=`(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` expected=`':style'`
    concept_phrase: `two naming conventions from the style guide`
    question_what: `the marker keyword for the naming-conventions lesson`

### G12-18 sample 1/N (form: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"This isn't a market trick to fool the buyers," Carol said inside the barn,
with steady, careful steps. "It's a tool for the whole farmhouse." Alice
looked at the community-style basics and admitted she would not
have known what to write — the old greed for quick answers had
nothing to offer here. Carol sketched `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` on a slate so
the runtime could speak for itself, the way Quill the goose let each
egg speak for the morning.

What Clojure form computes the marker for the style-guide lesson? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 sample 2/N (form: `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)`, expected: `':style'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Emily had been trying to teach Alice how the REPL
works. "Here," she said, pointing to two naming conventions from the style guide.
"You hand the form `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the marker keyword for the naming-conventions lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### G12-18 sample 3/N (form: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the community-style basics into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the marker for the style-guide lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

### G12-18 sample 4/N (form: `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)`, expected: `':style'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

At a small stall in the kitchen, someone had chalked a wager: whoever
predicted the result of `(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)` first would set the asking
price for the morning's eggs. David, her eyes always on the path, said it
was easier to type the form into the REPL than to argue about
two naming conventions from the style guide — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the marker keyword for the naming-conventions lesson.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer pure functions, name predicates with ?, danger! ops with !\" :style)"}}]}
```

### G12-18 sample 5/N (form: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between Diana and Morgan. The bet was
simple: predict what `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` would return. Diana,
with a glint of impatience, was certain about the answer. Morgan asked
her, with steady, careful steps, to actually write the form into the
REPL — the community-style basics would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the marker for the style-guide lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

