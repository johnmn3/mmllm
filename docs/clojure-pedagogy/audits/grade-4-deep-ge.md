# Grade 4 goose-eggs — deep spot-check

5 rendered records per subject (20 subjects × 5 = 100 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G4-01: Vector literal

**examples (3):**

- ex0: form=`[1 2 3]` expected=`[1, 2, 3]`
    concept_phrase: `the vector [1 2 3]`
    question_what: `the value [1 2 3]`
- ex1: form=`[]` expected=`[]`
    concept_phrase: `the empty vector []`
    question_what: `the empty vector`
- ex2: form=`["a" "b"]` expected=`['a', 'b']`
    concept_phrase: `the vector of strings`
    question_what: `the vector ["a" "b"]`

### G4-01 sample 1/N (form: `[1 2 3]`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol, puffed up with pride, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Alice
wrote `[1 2 3]` on a slate near the market, calmly. "It's not about
plain or fancy," she said, without complaint. "It's about
whether the runtime agrees with what we think we're describing.

Write a Clojure expression that computes the value [1 2 3].
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### G4-01 sample 2/N (form: `[]`, expected: `[]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A wooden tally board hung on the barn wall at the edge of the farm, half-filled with
the morning's marks. Alice wanted to add one more entry: the
result of `[]`. Frank, calculating in silence, blurted out a
guess. Alice, saying very little, simply submitted the form to
the REPL — one form, one return, the way Quill the goose laid one
egg per morning, never a flock at once.

Question: write a Clojure expression for the empty vector.
---asst---
I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

### G4-01 sample 3/N (form: `["a" "b"]`, expected: `['a', 'b']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `["a" "b"]`.
Morgan laughed, puffed up with pride, and declared it too easy.
Robin said, with steady, careful steps, that the only honest way to know
the vector of strings was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the vector ["a" "b"]? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"[\"a\" \"b\"]"}}]}
```

### G4-01 sample 4/N (form: `[1 2 3]`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"There is no need to evaluate that," Casey said, with great whoops of laughter.
"Anyone with eyes can see what the vector [1 2 3] comes to."
Edward, who in the cellar had grown used to such claims, asked
them to actually write the form `[1 2 3]` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the value [1 2 3]? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### G4-01 sample 5/N (form: `[]`, expected: `[]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the empty vector [] into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `[]` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the empty vector.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"[]"}}]}
```

## G4-02: nth — vector access

**examples (2):**

- ex0: form=`(nth [10 20 30] 0)` expected=`10`
    concept_phrase: `the form (nth [10 20 30] 0)`
    question_what: `the value at index 0`
- ex1: form=`(nth [10 20 30] 2)` expected=`30`
    concept_phrase: `the form (nth [10 20 30] 2)`
    question_what: `the value at index 2`

### G4-02 sample 1/N (form: `(nth [10 20 30] 0)`, expected: `10`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what the form (nth [10 20 30] 0) comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(nth [10 20 30] 0)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value at index 0.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### G4-02 sample 2/N (form: `(nth [10 20 30] 2)`, expected: `30`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A wooden tally board hung on the barn wall at the edge of the village, half-filled with
the morning's marks. Oliver wanted to add one more entry: the
result of `(nth [10 20 30] 2)`. Frank, with a hungry gleam in the eye, blurted out a
guess. Oliver, untroubled by what others thought, simply submitted the form to
the REPL — one form, one return, the way Quill the goose laid one
egg per morning, never a flock at once.

Write a Clojure expression that computes the value at index 2.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### G4-02 sample 3/N (form: `(nth [10 20 30] 0)`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to the form (nth [10 20 30] 0).
"You hand the form `(nth [10 20 30] 0)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value at index 0.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### G4-02 sample 4/N (form: `(nth [10 20 30] 2)`, expected: `30`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the kitchen, the
next entry was the form (nth [10 20 30] 2). Charlie peered over
her shoulder at the form `(nth [10 20 30] 2)` and asked what
it would come out to.

What Clojure form computes the value at index 2? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 2)"}}]}
```

### G4-02 sample 5/N (form: `(nth [10 20 30] 0)`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(nth [10 20 30] 0)` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the form (nth [10 20 30] 0) — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the value at index 0.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

## G4-03: conj — append to vector

**examples (2):**

- ex0: form=`(conj [1 2] 3)` expected=`[1, 2, 3]`
    concept_phrase: `the form (conj [1 2] 3)`
    question_what: `[1 2] with 3 conjed`
- ex1: form=`(conj [] :hare)` expected=`[':hare']`
    concept_phrase: `the form (conj [] :hare)`
    question_what: `the empty vector with :hare conjed`

### G4-03 sample 1/N (form: `(conj [1 2] 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(conj [1 2] 3)` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — the form (conj [1 2] 3) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for [1 2] with 3 conjed.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### G4-03 sample 2/N (form: `(conj [] :hare)`, expected: `[':hare']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(conj [] :hare)` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form (conj [] :hare); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the empty vector with :hare conjed.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :hare)"}}]}
```

### G4-03 sample 3/N (form: `(conj [1 2] 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

Robin, with a smug grin, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Grace
wrote `(conj [1 2] 3)` on a slate by the meadow, calmly. "It's not about
plain or fancy," she said, untroubled by what others thought. "It's about
whether the runtime agrees with what we think we're describing.

Question: write a Clojure expression for [1 2] with 3 conjed.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### G4-03 sample 4/N (form: `(conj [] :hare)`, expected: `[':hare']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched the form (conj [] :hare) into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(conj [] :hare)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the empty vector with :hare conjed? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(conj [] :hare)"}}]}
```

### G4-03 sample 5/N (form: `(conj [1 2] 3)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Carol said, with great whoops of laughter.
"Anyone with eyes can see what the form (conj [1 2] 3) comes to."
Emily, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(conj [1 2] 3)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes [1 2] with 3 conjed.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

## G4-04: List literal

**examples (2):**

- ex0: form=`'(1 2 3)` expected=`[1, 2, 3]`
    concept_phrase: `the list '(1 2 3)`
    question_what: `the list of three numbers`
- ex1: form=`'()` expected=`[]`
    concept_phrase: `the empty list`
    question_what: `the empty list`

### G4-04 sample 1/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to the list '(1 2 3).
"You hand the form `'(1 2 3)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the list of three numbers.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G4-04 sample 2/N (form: `'()`, expected: `[]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

A small audience of neighbors had gathered in the orchard to watch
Bob attempt to outguess Grace at reading the
REPL. Grace pointed to the empty list and read out the form
aloud: `'()`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the empty list.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### G4-04 sample 3/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `'(1 2 3)` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit the list '(1 2 3) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the list of three numbers.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G4-04 sample 4/N (form: `'()`, expected: `[]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table inside a cottage, set out as a
wager between Henry and Charlie. The bet was
simple: predict what `'()` would return. Henry,
calculating in silence, was certain about the answer. Charlie asked
him, untroubled by what others thought, to actually write the form into the
REPL — the empty list would be settled the moment the runtime
answered, not before.

What Clojure form computes the empty list? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"'()"}}]}
```

### G4-04 sample 5/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Helen stopped near the farm
with a basket of eggs and refused to move on until someone could
prove what the form `'(1 2 3)` evaluated to. Helen called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit the list '(1 2 3) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes the list of three numbers.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

## G4-05: cons — prepend to seq

**examples (1):**

- ex0: form=`(cons 0 '(1 2 3))` expected=`[0, 1, 2, 3]`
    concept_phrase: `the form (cons 0 '(1 2 3))`
    question_what: `the seq with 0 cons'd at the front`

### G4-05 sample 1/N (form: `(cons 0 '(1 2 3))`, expected: `[0, 1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(cons 0 '(1 2 3))` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the form (cons 0 '(1 2 3)) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the seq with 0 cons'd at the front.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 sample 2/N (form: `(cons 0 '(1 2 3))`, expected: `[0, 1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(cons 0 '(1 2 3))` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit the form (cons 0 '(1 2 3)) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the seq with 0 cons'd at the front.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 sample 3/N (form: `(cons 0 '(1 2 3))`, expected: `[0, 1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

Frank offered a small basket of eggs as a wager inside the kitchen:
whoever guessed the result of `(cons 0 '(1 2 3))` first would keep them.
David, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form (cons 0 '(1 2 3)); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the seq with 0 cons'd at the front.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 sample 4/N (form: `(cons 0 '(1 2 3))`, expected: `[0, 1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post at the edge of the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(cons 0 '(1 2 3))`.
Sam laughed, with great whoops of laughter, and declared it too easy.
Grace said, untroubled by what others thought, that the only honest way to know
the form (cons 0 '(1 2 3)) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the seq with 0 cons'd at the front.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-05 sample 5/N (form: `(cons 0 '(1 2 3))`, expected: `[0, 1, 2, 3]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Morgan had been trying to teach Charlie how the REPL
works. "Here," they said, pointing to the form (cons 0 '(1 2 3)).
"You hand the form `(cons 0 '(1 2 3))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the seq with 0 cons'd at the front? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

## G4-06: Map literal

**examples (1):**

- ex0: form=`{:hare 1 :tortoise 2}` expected=`{':hare': 1, ':tortoise': 2}`
    concept_phrase: `the map {:hare 1 :tortoise 2}`
    question_what: `the map with two entries`

### G4-06 sample 1/N (form: `{:hare 1 :tortoise 2}`, expected: `{':hare': 1, ':tortoise': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what the map {:hare 1 :tortoise 2} comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `{:hare 1 :tortoise 2}` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the map with two entries.
---asst---
I let the REPL count the basket the way one counts eggs.

{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

### G4-06 sample 2/N (form: `{:hare 1 :tortoise 2}`, expected: `{':hare': 1, ':tortoise': 2}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched the map {:hare 1 :tortoise 2} into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `{:hare 1 :tortoise 2}` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the map with two entries? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

### G4-06 sample 3/N (form: `{:hare 1 :tortoise 2}`, expected: `{':hare': 1, ':tortoise': 2}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `{:hare 1 :tortoise 2}`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
the map {:hare 1 :tortoise 2} was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the map with two entries.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

### G4-06 sample 4/N (form: `{:hare 1 :tortoise 2}`, expected: `{':hare': 1, ':tortoise': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alex and Grace stood inside the cellar where someone had
scratched the map {:hare 1 :tortoise 2} into a smooth slate by the egg-basket.
Grace, with great whoops of laughter, declared the answer was obvious — no need to
evaluate anything. Alex, stepping deliberately, suggested they
actually submit the form `{:hare 1 :tortoise 2}` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the map with two entries? Submit it via `eval`.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

### G4-06 sample 5/N (form: `{:hare 1 :tortoise 2}`, expected: `{':hare': 1, ':tortoise': 2}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what the map {:hare 1 :tortoise 2} comes to."
Frank, who near the farm had grown used to such claims, asked
them to actually write the form `{:hare 1 :tortoise 2}` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the map with two entries.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

## G4-07: get — map lookup

**examples (2):**

- ex0: form=`(get {:a 1 :b 2} :a)` expected=`1`
    concept_phrase: `the form (get {:a 1 :b 2} :a)`
    question_what: `the value at :a`
- ex1: form=`(get {:a 1} :missing :default)` expected=`':default'`
    concept_phrase: `the form (get {:a 1} :missing :default)`
    question_what: `the default value when key missing`

### G4-07 sample 1/N (form: `(get {:a 1 :b 2} :a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David had been laying out a small collection by the market —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. David wrote `(get {:a 1 :b 2} :a)` on a slate
and asked Robin to write the form into the REPL so they
could confirm it together, the way Quill the goose settled each
morning's count by laying one more egg.

What Clojure form computes the value at :a? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### G4-07 sample 2/N (form: `(get {:a 1} :missing :default)`, expected: `':default'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

Edward, boasting at every turn, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. David
wrote `(get {:a 1} :missing :default)` on a slate deep inside the kitchen, calmly. "It's not about
plain or fancy," he said, her eyes always on the path. "It's about
whether the runtime agrees with what we think we're describing.

What Clojure form computes the default value when key missing? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### G4-07 sample 3/N (form: `(get {:a 1 :b 2} :a)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A wooden tally board hung on the barn wall deep inside the cellar, half-filled with
the morning's marks. Fiona wanted to add one more entry: the
result of `(get {:a 1 :b 2} :a)`. Sam, with a glint of impatience, blurted out a
guess. Fiona, untroubled by what others thought, simply submitted the form to
the REPL — one form, one return, the way Plume the goose laid one
egg per morning, never a flock at once.

What Clojure form computes the value at :a? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### G4-07 sample 4/N (form: `(get {:a 1} :missing :default)`, expected: `':default'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, George stopped near the market
with a basket of eggs and refused to move on until someone could
prove what the form `(get {:a 1} :missing :default)` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit the form (get {:a 1} :missing :default) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the default value when key missing? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1} :missing :default)"}}]}
```

### G4-07 sample 5/N (form: `(get {:a 1 :b 2} :a)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

Helen had been laying out a small collection deep inside a cottage —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Helen wrote `(get {:a 1 :b 2} :a)` on a slate
and asked Robin to write the form into the REPL so they
could confirm it together, the way Plume the goose settled each
morning's count by laying one more egg.

What Clojure form computes the value at :a? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

## G4-08: assoc — map update

**examples (2):**

- ex0: form=`(assoc {:a 1} :b 2)` expected=`{':a': 1, ':b': 2}`
    concept_phrase: `the form (assoc {:a 1} :b 2)`
    question_what: `the map after assoc'ing :b 2`
- ex1: form=`(assoc {:a 1} :a 99)` expected=`{':a': 99}`
    concept_phrase: `the form (assoc {:a 1} :a 99)`
    question_what: `the map after updating :a to 99`

### G4-08 sample 1/N (form: `(assoc {:a 1} :b 2)`, expected: `{':a': 1, ':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

Oliver, with a smug grin, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Bob
wrote `(assoc {:a 1} :b 2)` on a slate in the village, calmly. "It's not about
plain or fancy," he said, stepping deliberately. "It's about
whether the runtime agrees with what we think we're describing.

Write a form whose evaluation gives the map after assoc'ing :b 2.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### G4-08 sample 2/N (form: `(assoc {:a 1} :a 99)`, expected: `{':a': 99}`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(assoc {:a 1} :a 99)` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit the form (assoc {:a 1} :a 99) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the map after updating :a to 99.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### G4-08 sample 3/N (form: `(assoc {:a 1} :b 2)`, expected: `{':a': 1, ':b': 2}`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(assoc {:a 1} :b 2)` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — the form (assoc {:a 1} :b 2) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the map after assoc'ing :b 2.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### G4-08 sample 4/N (form: `(assoc {:a 1} :a 99)`, expected: `{':a': 99}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

George had been laying out a small collection deep inside the cellar —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. George wrote `(assoc {:a 1} :a 99)` on a slate
and asked Casey to write the form into the REPL so they
could confirm it together, the way Honk the goose settled each
morning's count by laying one more egg.

Question: write a Clojure expression for the map after updating :a to 99.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :a 99)"}}]}
```

### G4-08 sample 5/N (form: `(assoc {:a 1} :b 2)`, expected: `{':a': 1, ':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to the form (assoc {:a 1} :b 2).
"You hand the form `(assoc {:a 1} :b 2)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the map after assoc'ing :b 2? Submit it via `eval`.
---asst---
I let the REPL count the basket the way one counts eggs.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

## G4-09: dissoc — map remove key

**examples (1):**

- ex0: form=`(dissoc {:a 1 :b 2} :a)` expected=`{':b': 2}`
    concept_phrase: `the form (dissoc {:a 1 :b 2} :a)`
    question_what: `the map without :a`

### G4-09 sample 1/N (form: `(dissoc {:a 1 :b 2} :a)`, expected: `{':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was the form (dissoc {:a 1 :b 2} :a). George peered over
his shoulder at the form `(dissoc {:a 1 :b 2} :a)` and asked what
it would come out to.

Write a Clojure expression that computes the map without :a.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 sample 2/N (form: `(dissoc {:a 1 :b 2} :a)`, expected: `{':b': 2}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was the form (dissoc {:a 1 :b 2} :a). George peered over
their shoulder at the form `(dissoc {:a 1 :b 2} :a)` and asked what
it would come out to.

Write a form whose evaluation gives the map without :a.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 sample 3/N (form: `(dissoc {:a 1 :b 2} :a)`, expected: `{':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(dissoc {:a 1 :b 2} :a)` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the form (dissoc {:a 1 :b 2} :a); the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the map without :a.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 sample 4/N (form: `(dissoc {:a 1 :b 2} :a)`, expected: `{':b': 2}`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in the kitchen.

Alex had been trying to teach Oliver how the REPL
works. "Here," they said, pointing to the form (dissoc {:a 1 :b 2} :a).
"You hand the form `(dissoc {:a 1 :b 2} :a)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the map without :a? Submit it via `eval`.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-09 sample 5/N (form: `(dissoc {:a 1 :b 2} :a)`, expected: `{':b': 2}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Oliver stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(dissoc {:a 1 :b 2} :a)` evaluated to. Oliver called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit the form (dissoc {:a 1 :b 2} :a) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for the map without :a.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

## G4-10: keys and vals

**examples (1):**

- ex0: form=`(count (keys {:a 1 :b 2 :c 3}))` expected=`3`
    concept_phrase: `the form (count (keys ...))`
    question_what: `the number of keys in the map`

### G4-10 sample 1/N (form: `(count (keys {:a 1 :b 2 :c 3}))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A wooden tally board hung on the barn wall deep inside the kitchen, half-filled with
the morning's marks. Alex wanted to add one more entry: the
result of `(count (keys {:a 1 :b 2 :c 3}))`. Fiona, with hands itching to count more, blurted out a
guess. Alex, stepping deliberately, simply submitted the form to
the REPL — one form, one return, the way Honk the goose laid one
egg per morning, never a flock at once.

Write a Clojure expression that computes the number of keys in the map.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 sample 2/N (form: `(count (keys {:a 1 :b 2 :c 3}))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was the form (count (keys ...)). Emily peered over
her shoulder at the form `(count (keys {:a 1 :b 2 :c 3}))` and asked what
it would come out to.

Write a form whose evaluation gives the number of keys in the map.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 sample 3/N (form: `(count (keys {:a 1 :b 2 :c 3}))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(count (keys {:a 1 :b 2 :c 3}))` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the form (count (keys ...)); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the number of keys in the map.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 sample 4/N (form: `(count (keys {:a 1 :b 2 :c 3}))`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post deep inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(count (keys {:a 1 :b 2 :c 3}))`.
Diana laughed, swaggering through the underbrush, and declared it too easy.
Helen said, without complaint, that the only honest way to know
the form (count (keys ...)) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the number of keys in the map? Submit it via `eval`.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-10 sample 5/N (form: `(count (keys {:a 1 :b 2 :c 3}))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

Halfway through the morning errand, Sam stopped inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(count (keys {:a 1 :b 2 :c 3}))` evaluated to. Sam called it
impossible. Helen, walking up at an unhurried pace, simply
said: "Submit the form (count (keys ...)) to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

What Clojure form computes the number of keys in the map? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

## G4-11: Set literal

**examples (2):**

- ex0: form=`(count #{1 2 3})` expected=`3`
    concept_phrase: `the count of #{1 2 3}`
    question_what: `the size of the set`
- ex1: form=`(count #{1 1 1})` expected=`1`
    concept_phrase: `the count of #{1 1 1} (dedup'd)`
    question_what: `the size of the set`

### G4-11 sample 1/N (form: `(count #{1 2 3})`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(count #{1 2 3})` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the count of #{1 2 3} — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the size of the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### G4-11 sample 2/N (form: `(count #{1 1 1})`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to the count of #{1 1 1} (dedup'd) and read out the form
aloud: `(count #{1 1 1})`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the size of the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### G4-11 sample 3/N (form: `(count #{1 2 3})`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(count #{1 2 3})` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the count of #{1 2 3} — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the size of the set.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### G4-11 sample 4/N (form: `(count #{1 1 1})`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(count #{1 1 1})` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the count of #{1 1 1} (dedup'd); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the size of the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 1 1})"}}]}
```

### G4-11 sample 5/N (form: `(count #{1 2 3})`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(count #{1 2 3})`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
the count of #{1 2 3} was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the size of the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

## G4-12: Set membership

**examples (2):**

- ex0: form=`(contains? #{1 2 3} 2)` expected=`True`
    concept_phrase: `the form (contains? #{1 2 3} 2)`
    question_what: `whether 2 is in the set`
- ex1: form=`(contains? #{1 2 3} 4)` expected=`False`
    concept_phrase: `the form (contains? #{1 2 3} 4)`
    question_what: `whether 4 is in the set`

### G4-12 sample 1/N (form: `(contains? #{1 2 3} 2)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to the form (contains? #{1 2 3} 2).
"You hand the form `(contains? #{1 2 3} 2)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for whether 2 is in the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### G4-12 sample 2/N (form: `(contains? #{1 2 3} 4)`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(contains? #{1 2 3} 4)` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (contains? #{1 2 3} 4) — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes whether 4 is in the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### G4-12 sample 3/N (form: `(contains? #{1 2 3} 2)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(contains? #{1 2 3} 2)` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the form (contains? #{1 2 3} 2) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for whether 2 is in the set.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### G4-12 sample 4/N (form: `(contains? #{1 2 3} 4)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(contains? #{1 2 3} 4)`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
the form (contains? #{1 2 3} 4) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes whether 4 is in the set? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 4)"}}]}
```

### G4-12 sample 5/N (form: `(contains? #{1 2 3} 2)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A wooden tally board hung on the barn wall by the meadow, half-filled with
the morning's marks. Morgan wanted to add one more entry: the
result of `(contains? #{1 2 3} 2)`. Oliver, imagining all that might be gained, blurted out a
guess. Morgan, without complaint, simply submitted the form to
the REPL — one form, one return, the way Quill the goose laid one
egg per morning, never a flock at once.

What Clojure form computes whether 2 is in the set? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

## G4-13: count — universal

**examples (4):**

- ex0: form=`(count [1 2 3 4 5])` expected=`5`
    concept_phrase: `the count of a 5-element vector`
    question_what: `the count`
- ex1: form=`(count {:a 1 :b 2})` expected=`2`
    concept_phrase: `the count of a 2-key map`
    question_what: `the count`
- ex2: form=`(count #{:a :b :c})` expected=`3`
    concept_phrase: `the count of a 3-element set`
    question_what: `the count`
- ex3: form=`(count "tortoise")` expected=`8`
    concept_phrase: `the count of "tortoise"`
    question_what: `the string length`

### G4-13 sample 1/N (form: `(count [1 2 3 4 5])`, expected: `5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice had been laying out a small collection at the edge of the market —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Alice wrote `(count [1 2 3 4 5])` on a slate
and asked Sam to write the form into the REPL so they
could confirm it together, the way Plume the goose settled each
morning's count by laying one more egg.

Write a form whose evaluation gives the count.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

### G4-13 sample 2/N (form: `(count {:a 1 :b 2})`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `(count {:a 1 :b 2})` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — the count of a 2-key map would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the count.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count {:a 1 :b 2})"}}]}
```

### G4-13 sample 3/N (form: `(count #{:a :b :c})`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the market.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today by the market, the
next entry was the count of a 3-element set. Henry peered over
their shoulder at the form `(count #{:a :b :c})` and asked what
it would come out to.

Write a form whose evaluation gives the count.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count #{:a :b :c})"}}]}
```

### G4-13 sample 4/N (form: `(count "tortoise")`, expected: `8`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alex, boasting at every turn, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Grace
wrote `(count "tortoise")` on a slate in the cellar, calmly. "It's not about
plain or fancy," she said, with steady, careful steps. "It's about
whether the runtime agrees with what we think we're describing.

Write a form whose evaluation gives the string length.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G4-13 sample 5/N (form: `(count [1 2 3 4 5])`, expected: `5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Diana had been laying out a small collection inside a cottage —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Diana wrote `(count [1 2 3 4 5])` on a slate
and asked Robin to write the form into the REPL so they
could confirm it together, the way Honk the goose settled each
morning's count by laying one more egg.

What Clojure form computes the count? Submit it via `eval`.
---asst---
I write the collection literal and let the REPL evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

## G4-14: empty?

**examples (3):**

- ex0: form=`(empty? [])` expected=`True`
    concept_phrase: `the form (empty? [])`
    question_what: `whether [] is empty`
- ex1: form=`(empty? [1])` expected=`False`
    concept_phrase: `the form (empty? [1])`
    question_what: `whether [1] is empty`
- ex2: form=`(empty? "")` expected=`True`
    concept_phrase: `the form (empty? "")`
    question_what: `whether the empty string is empty`

### G4-14 sample 1/N (form: `(empty? [])`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what the form (empty? []) comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(empty? [])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes whether [] is empty.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### G4-14 sample 2/N (form: `(empty? [1])`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward had been laying out a small collection in the market —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Edward wrote `(empty? [1])` on a slate
and asked George to write the form into the REPL so they
could confirm it together, the way Plume the goose settled each
morning's count by laying one more egg.

What Clojure form computes whether [1] is empty? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

### G4-14 sample 3/N (form: `(empty? "")`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

George, with a smug grin, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Alex
wrote `(empty? "")` on a slate in the barn, calmly. "It's not about
plain or fancy," they said, her eyes always on the path. "It's about
whether the runtime agrees with what we think we're describing.

Question: write a Clojure expression for whether the empty string is empty.
---asst---
I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(empty? \"\")"}}]}
```

### G4-14 sample 4/N (form: `(empty? [])`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the form (empty? []) comes to."
Edward, who in the meadow had grown used to such claims, asked
him to actually write the form `(empty? [])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for whether [] is empty.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### G4-14 sample 5/N (form: `(empty? [1])`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

Jordan, with great whoops of laughter, declared the collection plain — a row
of eggs, a stack of coins, nothing worth a second look. Casey
wrote `(empty? [1])` on a slate in the barn, calmly. "It's not about
plain or fancy," they said, with steady, careful steps. "It's about
whether the runtime agrees with what we think we're describing.

Question: write a Clojure expression for whether [1] is empty.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(empty? [1])"}}]}
```

## G4-15: first, rest, last

**examples (3):**

- ex0: form=`(first [10 20 30])` expected=`10`
    concept_phrase: `the first of the vector`
    question_what: `the first element`
- ex1: form=`(last  [10 20 30])` expected=`30`
    concept_phrase: `the last of the vector`
    question_what: `the last element`
- ex2: form=`(count (rest [10 20 30]))` expected=`2`
    concept_phrase: `the rest of [10 20 30] (count)`
    question_what: `the count after removing first`

### G4-15 sample 1/N (form: `(first [10 20 30])`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(first [10 20 30])` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the first of the vector; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the first element.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### G4-15 sample 2/N (form: `(last  [10 20 30])`, expected: `30`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the last of the vector comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(last  [10 20 30])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the last element.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

### G4-15 sample 3/N (form: `(count (rest [10 20 30]))`, expected: `2`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the farm.

George and Morgan stood near the farm where someone had
scratched the rest of [10 20 30] (count) into a smooth slate by the egg-basket.
Morgan, boasting at every turn, declared the answer was obvious — no need to
evaluate anything. George, without complaint, suggested they
actually submit the form `(count (rest [10 20 30]))` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the count after removing first? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count (rest [10 20 30]))"}}]}
```

### G4-15 sample 4/N (form: `(first [10 20 30])`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what the first of the vector comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `(first [10 20 30])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the first element.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### G4-15 sample 5/N (form: `(last  [10 20 30])`, expected: `30`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(last  [10 20 30])`.
Robin laughed, with a smug grin, and declared it too easy.
Diana said, stepping deliberately, that the only honest way to know
the last of the vector was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the last element.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(last  [10 20 30])"}}]}
```

## G4-16: into and conj on collections

**examples (2):**

- ex0: form=`(into [] '(1 2 3))` expected=`[1, 2, 3]`
    concept_phrase: `the form (into [] '(1 2 3))`
    question_what: `the vector built from a list`
- ex1: form=`(into #{} [1 2 2 3])` expected=`[1, 2, 3]`
    concept_phrase: `the form (into #{} [1 2 2 3])`
    question_what: `the set built from a vector (dups removed)`

### G4-16 sample 1/N (form: `(into [] '(1 2 3))`, expected: `[1, 2, 3]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what the form (into [] '(1 2 3)) comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `(into [] '(1 2 3))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the vector built from a list.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### G4-16 sample 2/N (form: `(into #{} [1 2 2 3])`, expected: `[1, 2, 3]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(into #{} [1 2 2 3])` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — the form (into #{} [1 2 2 3]) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the set built from a vector (dups removed).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### G4-16 sample 3/N (form: `(into [] '(1 2 3))`, expected: `[1, 2, 3]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(into [] '(1 2 3))` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — the form (into [] '(1 2 3)) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the vector built from a list.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### G4-16 sample 4/N (form: `(into #{} [1 2 2 3])`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," David said, swaggering through the underbrush.
"Anyone with eyes can see what the form (into #{} [1 2 2 3]) comes to."
Carol, who in the market had grown used to such claims, asked
him to actually write the form `(into #{} [1 2 2 3])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the set built from a vector (dups removed).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} [1 2 2 3])"}}]}
```

### G4-16 sample 5/N (form: `(into [] '(1 2 3))`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Bob said, with a smug grin.
"Anyone with eyes can see what the form (into [] '(1 2 3)) comes to."
Emily, who inside the barn had grown used to such claims, asked
him to actually write the form `(into [] '(1 2 3))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the vector built from a list.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

## G4-17: Immutability — assoc returns new

**examples (1):**

- ex0: form=`(let [m {:a 1}] (assoc m :a 99) m)` expected=`{':a': 1}`
    concept_phrase: `the form showing assoc returns a new map`
    question_what: `the original map after assoc`

### G4-17 sample 1/N (form: `(let [m {:a 1}] (assoc m :a 99) m)`, expected: `{':a': 1}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(let [m {:a 1}] (assoc m :a 99) m)`.
Grace laughed, boasting at every turn, and declared it too easy.
Oliver said, her eyes always on the path, that the only honest way to know
the form showing assoc returns a new map was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the original map after assoc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 sample 2/N (form: `(let [m {:a 1}] (assoc m :a 99) m)`, expected: `{':a': 1}`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched the form showing assoc returns a new map into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `(let [m {:a 1}] (assoc m :a 99) m)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the original map after assoc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 sample 3/N (form: `(let [m {:a 1}] (assoc m :a 99) m)`, expected: `{':a': 1}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Emily said, boasting at every turn.
"Anyone with eyes can see what the form showing assoc returns a new map comes to."
Carol, who in the village had grown used to such claims, asked
her to actually write the form `(let [m {:a 1}] (assoc m :a 99) m)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the original map after assoc.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 sample 4/N (form: `(let [m {:a 1}] (assoc m :a 99) m)`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was in the orchard.

David had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the orchard, the
next entry was the form showing assoc returns a new map. Oliver peered over
his shoulder at the form `(let [m {:a 1}] (assoc m :a 99) m)` and asked what
it would come out to.

Question: write a Clojure expression for the original map after assoc.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-17 sample 5/N (form: `(let [m {:a 1}] (assoc m :a 99) m)`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened near the market.

Halfway through the morning errand, George stopped at the edge of the market
with a basket of eggs and refused to move on until someone could
prove what the form `(let [m {:a 1}] (assoc m :a 99) m)` evaluated to. George called it
impossible. Oliver, walking up at an unhurried pace, simply
said: "Submit the form showing assoc returns a new map to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for the original map after assoc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

## G4-18: Equality of vectors and lists

**examples (1):**

- ex0: form=`(= [1 2 3] '(1 2 3))` expected=`True`
    concept_phrase: `the form (= [1 2 3] '(1 2 3))`
    question_what: `whether vector and list with same elements are equal`

### G4-18 sample 1/N (form: `(= [1 2 3] '(1 2 3))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol had been laying out a small collection inside the barn —
eggs from the morning, coins from the market, tallies from the barn,
whatever the day produced. Carol wrote `(= [1 2 3] '(1 2 3))` on a slate
and asked Alice to write the form into the REPL so they
could confirm it together, the way Quill the goose settled each
morning's count by laying one more egg.

What Clojure form computes whether vector and list with same elements are equal? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 sample 2/N (form: `(= [1 2 3] '(1 2 3))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the form (= [1 2 3] '(1 2 3)) into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(= [1 2 3] '(1 2 3))` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives whether vector and list with same elements are equal.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 sample 3/N (form: `(= [1 2 3] '(1 2 3))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between Diana and Morgan. The bet was
simple: predict what `(= [1 2 3] '(1 2 3))` would return. Diana,
with a glint of impatience, was certain about the answer. Morgan asked
her, with steady, careful steps, to actually write the form into the
REPL — the form (= [1 2 3] '(1 2 3)) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives whether vector and list with same elements are equal.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 sample 4/N (form: `(= [1 2 3] '(1 2 3))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Robin had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today at the edge of the village, the
next entry was the form (= [1 2 3] '(1 2 3)). Helen peered over
their shoulder at the form `(= [1 2 3] '(1 2 3))` and asked what
it would come out to.

Question: write a Clojure expression for whether vector and list with same elements are equal.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-18 sample 5/N (form: `(= [1 2 3] '(1 2 3))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened near the orchard.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between David and Diana. The bet was
simple: predict what `(= [1 2 3] '(1 2 3))` would return. David,
eyeing the next morning's gift, was certain about the answer. Diana asked
him, without complaint, to actually write the form into the
REPL — the form (= [1 2 3] '(1 2 3)) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives whether vector and list with same elements are equal.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

## G4-19: range and seq

**examples (2):**

- ex0: form=`(count (range 5))` expected=`5`
    concept_phrase: `the count of (range 5)`
    question_what: `the count of range 0..4`
- ex1: form=`(first (range 1 100))` expected=`1`
    concept_phrase: `the first of (range 1 100)`
    question_what: `the first of range 1..99`

### G4-19 sample 1/N (form: `(count (range 5))`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A wooden tally board hung on the barn wall deep inside a cottage, half-filled with
the morning's marks. Grace wanted to add one more entry: the
result of `(count (range 5))`. Carol, with a hungry gleam in the eye, blurted out a
guess. Grace, saying very little, simply submitted the form to
the REPL — one form, one return, the way Quill the goose laid one
egg per morning, never a flock at once.

What Clojure form computes the count of range 0..4? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### G4-19 sample 2/N (form: `(first (range 1 100))`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the farm, the
next entry was the first of (range 1 100). Jordan peered over
their shoulder at the form `(first (range 1 100))` and asked what
it would come out to.

Question: write a Clojure expression for the first of range 1..99.
---asst---
I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### G4-19 sample 3/N (form: `(count (range 5))`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been trying to teach Alex how the REPL
works. "Here," she said, pointing to the count of (range 5).
"You hand the form `(count (range 5))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the count of range 0..4.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### G4-19 sample 4/N (form: `(first (range 1 100))`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the kitchen.

"There is no need to evaluate that," Robin said, boasting at every turn.
"Anyone with eyes can see what the first of (range 1 100) comes to."
Helen, who deep inside the kitchen had grown used to such claims, asked
them to actually write the form `(first (range 1 100))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the first of range 1..99.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(first (range 1 100))"}}]}
```

### G4-19 sample 5/N (form: `(count (range 5))`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the farm, the
next entry was the count of (range 5). Robin peered over
her shoulder at the form `(count (range 5))` and asked what
it would come out to.

Write a Clojure expression that computes the count of range 0..4.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

## G4-20: Collection vs sequence

**examples (2):**

- ex0: form=`(count (seq [1 2 3]))` expected=`3`
    concept_phrase: `the form (count (seq [1 2 3]))`
    question_what: `the count of seq over a vector`
- ex1: form=`(seq [])` expected=`None`
    concept_phrase: `the form (seq [])`
    question_what: `what (seq []) returns`

### G4-20 sample 1/N (form: `(count (seq [1 2 3]))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the kitchen, the
next entry was the form (count (seq [1 2 3])). David peered over
his shoulder at the form `(count (seq [1 2 3]))` and asked what
it would come out to.

Write a Clojure expression that computes the count of seq over a vector.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### G4-20 sample 2/N (form: `(seq [])`, expected: `None`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Jordan said, with great whoops of laughter.
"Anyone with eyes can see what the form (seq []) comes to."
Alice, who in the cellar had grown used to such claims, asked
them to actually write the form `(seq [])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes what (seq []) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### G4-20 sample 3/N (form: `(count (seq [1 2 3]))`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post at the edge of the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(count (seq [1 2 3]))`.
Bob laughed, with great whoops of laughter, and declared it too easy.
Fiona said, her eyes always on the path, that the only honest way to know
the form (count (seq [1 2 3])) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the count of seq over a vector? Submit it via `eval`.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

### G4-20 sample 4/N (form: `(seq [])`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today by the meadow, the
next entry was the form (seq []). Bob peered over
his shoulder at the form `(seq [])` and asked what
it would come out to.

Question: write a Clojure expression for what (seq []) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(seq [])"}}]}
```

### G4-20 sample 5/N (form: `(count (seq [1 2 3]))`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the kitchen.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today inside the kitchen, the
next entry was the form (count (seq [1 2 3])). Jordan peered over
her shoulder at the form `(count (seq [1 2 3]))` and asked what
it would come out to.

What Clojure form computes the count of seq over a vector? Submit it via `eval`.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

