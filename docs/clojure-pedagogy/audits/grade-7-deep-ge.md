# Grade 7 goose-eggs — deep spot-check

5 rendered records per subject (18 subjects × 5 = 90 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G7-01: throw

**examples (1):**

- ex0: form=`(try (throw (Exception. "bad")) (catch Exception e :thrown))` expected=`':thrown'`
    concept_phrase: `throwing an exception that is then caught`
    question_what: `the keyword :thrown returned after the throw is caught`

### G7-01 sample 1/N (form: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`, expected: `':thrown'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small slip of paper near the market carried the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`.
Carol glanced at it and hurried on toward the market, certain
there was no trouble. Alice sat down by the egg-basket,
without complaint, and worked through throwing an exception that is then caught step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again.

Write a Clojure expression that computes the keyword :thrown returned after the throw is caught.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 sample 2/N (form: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`, expected: `':thrown'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"There is no need to evaluate that," Casey said, with great whoops of laughter.
"Anyone with eyes can see what throwing an exception that is then caught comes to."
Edward, who in the cellar had grown used to such claims, asked
them to actually write the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 sample 3/N (form: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`, expected: `':thrown'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Bob offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(try (throw (Exception. "bad")) (catch Exception e :thrown))` first would keep them.
Henry, saying very little, said it would be simpler to type the
form into the REPL than to bicker about throwing an exception that is then caught; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the keyword :thrown returned after the throw is caught.
---asst---
I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 sample 4/N (form: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`, expected: `':thrown'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the farm.

"There is no need to evaluate that," Alex said, as if the race were already won.
"Anyone with eyes can see what throwing an exception that is then caught comes to."
Diana, who in the farm had grown used to such claims, asked
them to actually write the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 sample 5/N (form: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`, expected: `':thrown'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside a cottage.

Fiona offered a small basket of eggs as a wager inside a cottage:
whoever guessed the result of `(try (throw (Exception. "bad")) (catch Exception e :thrown))` first would keep them.
Alex, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about throwing an exception that is then caught; the eggs,
after all, would still be there once Honk the goose laid the next
one.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

## G7-02: try / catch

**examples (2):**

- ex0: form=`(try (/ 1 0) (catch Exception e :caught))` expected=`':caught'`
    concept_phrase: `a division by zero wrapped in try/catch`
    question_what: `the keyword :caught returned by the catch branch`
- ex1: form=`(try 42 (catch Exception e :caught))` expected=`42`
    concept_phrase: `a try with no error — the body's value is returned`
    question_what: `the value 42 from the no-error branch`

### G7-02 sample 1/N (form: `(try (/ 1 0) (catch Exception e :caught))`, expected: `':caught'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what a division by zero wrapped in try/catch comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(try (/ 1 0) (catch Exception e :caught))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the keyword :caught returned by the catch branch.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### G7-02 sample 2/N (form: `(try 42 (catch Exception e :caught))`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Beyond the REPL the world had files, streams, and small surprises.
Oliver opened a leather ledger at the edge of the village, copying down
a try with no error — the body's value is returned beside the morning's egg-tally. Frank,
untroubled by the village gossip, watched as he wrote the form `(try 42 (catch Exception e :caught))`
so the runtime could carry the work the rest of the way.

Write a Clojure expression that computes the value 42 from the no-error branch.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### G7-02 sample 3/N (form: `(try (/ 1 0) (catch Exception e :caught))`, expected: `':caught'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to a division by zero wrapped in try/catch.
"You hand the form `(try (/ 1 0) (catch Exception e :caught))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the keyword :caught returned by the catch branch.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### G7-02 sample 4/N (form: `(try 42 (catch Exception e :caught))`, expected: `42`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the kitchen, the
next entry was a try with no error — the body's value is returned. Charlie peered over
her shoulder at the form `(try 42 (catch Exception e :caught))` and asked what
it would come out to.

What Clojure form computes the value 42 from the no-error branch? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### G7-02 sample 5/N (form: `(try (/ 1 0) (catch Exception e :caught))`, expected: `':caught'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(try (/ 1 0) (catch Exception e :caught))` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
a division by zero wrapped in try/catch — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

## G7-03: try / finally

**examples (2):**

- ex0: form=`(try 7 (finally :cleanup))` expected=`7`
    concept_phrase: `a try whose finally clause runs but doesn't change the value`
    question_what: `the value 7 from the body (finally is for side effects)`
- ex1: form=`(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` expected=`':caught'`
    concept_phrase: `a finally that runs before the outer catch fires`
    question_what: `the keyword :caught (the outer catch handles the divide-by-zero)`

### G7-03 sample 1/N (form: `(try 7 (finally :cleanup))`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(try 7 (finally :cleanup))` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — a try whose finally clause runs but doesn't change the value would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value 7 from the body (finally is for side effects).
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### G7-03 sample 2/N (form: `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))`, expected: `':caught'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about a finally that runs before the outer catch fires; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the keyword :caught (the outer catch handles the divide-by-zero).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### G7-03 sample 3/N (form: `(try 7 (finally :cleanup))`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

A small slip of paper by the meadow carried the form `(try 7 (finally :cleanup))`.
Robin glanced at it and hurried on toward the market, certain
there was no trouble. Grace sat down by the egg-basket,
untroubled by what others thought, and worked through a try whose finally clause runs but doesn't change the value step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again.

Question: write a Clojure expression for the value 7 from the body (finally is for side effects).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### G7-03 sample 4/N (form: `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))`, expected: `':caught'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

At a small stall in the orchard, someone had chalked a wager: whoever
predicted the result of `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` first would set the asking
price for the morning's eggs. George, without complaint, said it
was easier to type the form into the REPL than to argue about
a finally that runs before the outer catch fires — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

What Clojure form computes the keyword :caught (the outer catch handles the divide-by-zero)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### G7-03 sample 5/N (form: `(try 7 (finally :cleanup))`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Carol said, with great whoops of laughter.
"Anyone with eyes can see what a try whose finally clause runs but doesn't change the value comes to."
Emily, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(try 7 (finally :cleanup))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value 7 from the body (finally is for side effects).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

## G7-04: ex-info

**examples (2):**

- ex0: form=`(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` expected=`{':a': 1}`
    concept_phrase: `throwing an ex-info with attached data, then reading it back`
    question_what: `the data map {:a 1} pulled from the caught ex-info`
- ex1: form=`(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` expected=`':v'`
    concept_phrase: `extracting a single key from the caught ex-info's data`
    question_what: `the value :v at key :k in the ex-data`

### G7-04 sample 1/N (form: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`, expected: `{':a': 1}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to throwing an ex-info with attached data, then reading it back.
"You hand the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### G7-04 sample 2/N (form: `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`, expected: `':v'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

A small audience of neighbors had gathered in the orchard to watch
Bob attempt to outguess Grace at reading the
REPL. Grace pointed to extracting a single key from the caught ex-info's data and read out the form
aloud: `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the value :v at key :k in the ex-data.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### G7-04 sample 3/N (form: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`, expected: `{':a': 1}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit throwing an ex-info with attached data, then reading it back to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the data map {:a 1} pulled from the caught ex-info.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### G7-04 sample 4/N (form: `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`, expected: `':v'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table inside a cottage, set out as a
wager between Henry and Charlie. The bet was
simple: predict what `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` would return. Henry,
calculating in silence, was certain about the answer. Charlie asked
him, untroubled by what others thought, to actually write the form into the
REPL — extracting a single key from the caught ex-info's data would be settled the moment the runtime
answered, not before.

What Clojure form computes the value :v at key :k in the ex-data? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### G7-04 sample 5/N (form: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`, expected: `{':a': 1}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Helen stopped near the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` evaluated to. Helen called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit throwing an ex-info with attached data, then reading it back to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

## G7-05: nil punning

**examples (4):**

- ex0: form=`(some? nil)` expected=`False`
    concept_phrase: `the predicate (some? nil)`
    question_what: `whether nil counts as some?`
- ex1: form=`(some? 0)` expected=`True`
    concept_phrase: `the predicate (some? 0) — 0 is not nil`
    question_what: `whether 0 counts as some?`
- ex2: form=`(first nil)` expected=`None`
    concept_phrase: `calling first on nil`
    question_what: `the value of (first nil), which is nil`
- ex3: form=`(count nil)` expected=`0`
    concept_phrase: `counting a nil collection`
    question_what: `the count of nil, which is 0`

### G7-05 sample 1/N (form: `(some? nil)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(some? nil)` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the predicate (some? nil) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for whether nil counts as some?.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

### G7-05 sample 2/N (form: `(some? 0)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Charlie had learned not to trust the morning basket on first
glance. near the market, he typed `(some? 0)` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Beatrice,
tempted by the thought of plenty, laughed and said no error would ever come — but Charlie
insisted on letting the runtime decide, then reading the predicate (some? 0) — 0 is not nil
from whatever it returned.

Write a form whose evaluation gives whether 0 counts as some?.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(some? 0)"}}]}
```

### G7-05 sample 3/N (form: `(first nil)`, expected: `None`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob offered a small basket of eggs as a wager near the farm:
whoever guessed the result of `(first nil)` first would keep them.
Frank, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about calling first on nil; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the value of (first nil), which is nil.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(first nil)"}}]}
```

### G7-05 sample 4/N (form: `(count nil)`, expected: `0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post deep inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(count nil)`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Jordan said, with steady, careful steps, that the only honest way to know
counting a nil collection was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the count of nil, which is 0? Submit it via `eval`.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count nil)"}}]}
```

### G7-05 sample 5/N (form: `(some? nil)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(some? nil)` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit the predicate (some? nil) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes whether nil counts as some?.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

## G7-06: pre and post conditions

**examples (2):**

- ex0: form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` expected=`10`
    concept_phrase: `a fn with a :pre condition that is satisfied`
    question_what: `the value returned when the precondition holds and 5 is doubled`
- ex1: form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` expected=`':pre-failed'`
    concept_phrase: `a :pre condition that fails, caught by surrounding try`
    question_what: `the keyword :pre-failed when the pre-check rejects -1`

### G7-06 sample 1/N (form: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`, expected: `10`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what a fn with a :pre condition that is satisfied comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value returned when the precondition holds and 5 is doubled.
---asst---
I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### G7-06 sample 2/N (form: `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`, expected: `':pre-failed'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Beyond the REPL the world had files, streams, and small surprises.
Casey opened a leather ledger at the edge of the market, copying down
a :pre condition that fails, caught by surrounding try beside the morning's egg-tally. Fiona,
pleased with the steady fortune, watched as they wrote the form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`
so the runtime could carry the work the rest of the way.

Question: write a Clojure expression for the keyword :pre-failed when the pre-check rejects -1.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### G7-06 sample 3/N (form: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched a fn with a :pre condition that is satisfied into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value returned when the precondition holds and 5 is doubled? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### G7-06 sample 4/N (form: `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`, expected: `':pre-failed'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`.
Edward laughed, swaggering through the underbrush, and declared it too easy.
Emily said, her eyes always on the path, that the only honest way to know
a :pre condition that fails, caught by surrounding try was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the keyword :pre-failed when the pre-check rejects -1.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### G7-06 sample 5/N (form: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
a fn with a :pre condition that is satisfied was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value returned when the precondition holds and 5 is doubled.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

## G7-07: assert

**examples (2):**

- ex0: form=`(do (assert (= 1 1)) :ok)` expected=`':ok'`
    concept_phrase: `an assert that passes, followed by a return value`
    question_what: `the keyword :ok returned after the assert succeeds`
- ex1: form=`(try (assert (= 1 2)) (catch Throwable e :asserted))` expected=`':asserted'`
    concept_phrase: `an assert that fails, caught by surrounding try`
    question_what: `the keyword :asserted when the assertion rejects (= 1 2)`

### G7-07 sample 1/N (form: `(do (assert (= 1 1)) :ok)`, expected: `':ok'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David had learned not to trust the morning basket on first
glance. by the market, he typed `(do (assert (= 1 1)) :ok)` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Robin,
with hands itching to count more, laughed and said no error would ever come — but David
insisted on letting the runtime decide, then reading an assert that passes, followed by a return value
from whatever it returned.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### G7-07 sample 2/N (form: `(try (assert (= 1 2)) (catch Throwable e :asserted))`, expected: `':asserted'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

A small slip of paper deep inside the kitchen carried the form `(try (assert (= 1 2)) (catch Throwable e :asserted))`.
David glanced at it and hurried on toward the market, certain
there was no trouble. Emily sat down by the egg-basket,
her eyes always on the path, and worked through an assert that fails, caught by surrounding try step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again.

What Clojure form computes the keyword :asserted when the assertion rejects (= 1 2)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### G7-07 sample 3/N (form: `(do (assert (= 1 1)) :ok)`, expected: `':ok'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Beyond the REPL the world had files, streams, and small surprises.
Fiona opened a leather ledger deep inside the cellar, copying down
an assert that passes, followed by a return value beside the morning's egg-tally. Sam,
pleased with the steady fortune, watched as she wrote the form `(do (assert (= 1 1)) :ok)`
so the runtime could carry the work the rest of the way.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### G7-07 sample 4/N (form: `(try (assert (= 1 2)) (catch Throwable e :asserted))`, expected: `':asserted'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, George stopped near the market
with a basket of eggs and refused to move on until someone could
prove what the form `(try (assert (= 1 2)) (catch Throwable e :asserted))` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit an assert that fails, caught by surrounding try to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the keyword :asserted when the assertion rejects (= 1 2)? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### G7-07 sample 5/N (form: `(do (assert (= 1 1)) :ok)`, expected: `':ok'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

Helen had learned not to trust the morning basket on first
glance. deep inside a cottage, she typed `(do (assert (= 1 1)) :ok)` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Robin,
imagining all that might be gained, laughed and said no error would ever come — but Helen
insisted on letting the runtime decide, then reading an assert that passes, followed by a return value
from whatever it returned.

What Clojure form computes the keyword :ok returned after the assert succeeds? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

## G7-08: prn and pprint

**examples (2):**

- ex0: form=`(with-out-str (prn 42))` expected=`'42\n'`
    concept_phrase: `capturing the output of (prn 42)`
    question_what: `the string "42\n" produced by prn`
- ex1: form=`(with-out-str (prn :hare))` expected=`':hare\n'`
    concept_phrase: `capturing prn applied to the keyword :hare`
    question_what: `the string ":hare\n" produced by prn`

### G7-08 sample 1/N (form: `(with-out-str (prn 42))`, expected: `'42\n'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

A small slip of paper in the village carried the form `(with-out-str (prn 42))`.
Oliver glanced at it and hurried on toward the market, certain
there was no trouble. Bob sat down by the egg-basket,
stepping deliberately, and worked through capturing the output of (prn 42) step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again.

Write a form whose evaluation gives the string "42\n" produced by prn.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### G7-08 sample 2/N (form: `(with-out-str (prn :hare))`, expected: `':hare\n'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(with-out-str (prn :hare))` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit capturing prn applied to the keyword :hare to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the string ":hare\n" produced by prn.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :hare))"}}]}
```

### G7-08 sample 3/N (form: `(with-out-str (prn 42))`, expected: `'42\n'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(with-out-str (prn 42))` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — capturing the output of (prn 42) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the string "42\n" produced by prn.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### G7-08 sample 4/N (form: `(with-out-str (prn :hare))`, expected: `':hare\n'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

George had learned not to trust the morning basket on first
glance. deep inside the cellar, he typed `(with-out-str (prn :hare))` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Casey,
with a glint of impatience, laughed and said no error would ever come — but George
insisted on letting the runtime decide, then reading capturing prn applied to the keyword :hare
from whatever it returned.

Question: write a Clojure expression for the string ":hare\n" produced by prn.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :hare))"}}]}
```

### G7-08 sample 5/N (form: `(with-out-str (prn 42))`, expected: `'42\n'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to capturing the output of (prn 42).
"You hand the form `(with-out-str (prn 42))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the string "42\n" produced by prn? Submit it via `eval`.
---asst---
I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

## G7-09: tap>

**examples (2):**

- ex0: form=`(tap> :hello)` expected=`True`
    concept_phrase: `tapping a value into the tap pool`
    question_what: `the boolean true returned by tap>`
- ex1: form=`(tap> 42)` expected=`True`
    concept_phrase: `tapping the number 42 into the tap pool`
    question_what: `the boolean true (tap> always returns true on send)`

### G7-09 sample 1/N (form: `(tap> :hello)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was tapping a value into the tap pool. George peered over
his shoulder at the form `(tap> :hello)` and asked what
it would come out to.

Write a Clojure expression that computes the boolean true returned by tap>.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### G7-09 sample 2/N (form: `(tap> 42)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the barn to watch
David attempt to outguess Fiona at reading the
REPL. Fiona pointed to tapping the number 42 into the tap pool and read out the form
aloud: `(tap> 42)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the boolean true (tap> always returns true on send).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### G7-09 sample 3/N (form: `(tap> :hello)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was tapping a value into the tap pool. George peered over
their shoulder at the form `(tap> :hello)` and asked what
it would come out to.

Write a form whose evaluation gives the boolean true returned by tap>.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### G7-09 sample 4/N (form: `(tap> 42)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post by the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(tap> 42)`.
Beatrice laughed, with great whoops of laughter, and declared it too easy.
Emily said, without complaint, that the only honest way to know
tapping the number 42 into the tap pool was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the boolean true (tap> always returns true on send).
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### G7-09 sample 5/N (form: `(tap> :hello)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(tap> :hello)` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about tapping a value into the tap pool; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the boolean true returned by tap>.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

## G7-10: doc and source

**examples (1):**

- ex0: form=`(:doc (meta '^{:doc "adds two"} plus))` expected=`'adds two'`
    concept_phrase: `the :doc metadata on a symbol — what doc would print`
    question_what: `the string "adds two" from the metadata`

### G7-10 sample 1/N (form: `(:doc (meta '^{:doc "adds two"} plus))`, expected: `'adds two'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

Beyond the REPL the world had files, streams, and small surprises.
Alex opened a leather ledger deep inside the kitchen, copying down
the :doc metadata on a symbol — what doc would print beside the morning's egg-tally. Fiona,
calm in the morning routine, watched as they wrote the form `(:doc (meta '^{:doc "adds two"} plus))`
so the runtime could carry the work the rest of the way.

Write a Clojure expression that computes the string "adds two" from the metadata.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 sample 2/N (form: `(:doc (meta '^{:doc "adds two"} plus))`, expected: `'adds two'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was the :doc metadata on a symbol — what doc would print. Emily peered over
her shoulder at the form `(:doc (meta '^{:doc "adds two"} plus))` and asked what
it would come out to.

Write a form whose evaluation gives the string "adds two" from the metadata.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 sample 3/N (form: `(:doc (meta '^{:doc "adds two"} plus))`, expected: `'adds two'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(:doc (meta '^{:doc "adds two"} plus))` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the :doc metadata on a symbol — what doc would print; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the string "adds two" from the metadata.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 sample 4/N (form: `(:doc (meta '^{:doc "adds two"} plus))`, expected: `'adds two'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post deep inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(:doc (meta '^{:doc "adds two"} plus))`.
Diana laughed, swaggering through the underbrush, and declared it too easy.
Helen said, without complaint, that the only honest way to know
the :doc metadata on a symbol — what doc would print was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the string "adds two" from the metadata? Submit it via `eval`.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 sample 5/N (form: `(:doc (meta '^{:doc "adds two"} plus))`, expected: `'adds two'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

Halfway through the morning errand, Sam stopped inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(:doc (meta '^{:doc "adds two"} plus))` evaluated to. Sam called it
impossible. Helen, walking up at an unhurried pace, simply
said: "Submit the :doc metadata on a symbol — what doc would print to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

What Clojure form computes the string "adds two" from the metadata? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

## G7-11: Reading stack traces

**examples (2):**

- ex0: form=`(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` expected=`'oops'`
    concept_phrase: `extracting the message from a caught exception`
    question_what: `the string "oops" from the caught Exception`
- ex1: form=`(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` expected=`'trouble'`
    concept_phrase: `the message of a caught ex-info`
    question_what: `the string "trouble"`

### G7-11 sample 1/N (form: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`, expected: `'oops'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
extracting the message from a caught exception — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the string "oops" from the caught Exception.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 sample 2/N (form: `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`, expected: `'trouble'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to the message of a caught ex-info and read out the form
aloud: `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the string "trouble".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 sample 3/N (form: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`, expected: `'oops'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
extracting the message from a caught exception — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the string "oops" from the caught Exception.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 sample 4/N (form: `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`, expected: `'trouble'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the message of a caught ex-info; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the string "trouble".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 sample 5/N (form: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`, expected: `'oops'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
extracting the message from a caught exception was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the string "oops" from the caught Exception.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

## G7-12: slurp and spit

**examples (2):**

- ex0: form=`(count "hare\ntortoise\n")` expected=`14`
    concept_phrase: `the length of a multi-line string (as if read by slurp)`
    question_what: `the count of characters in "hare\ntortoise\n"`
- ex1: form=`(clojure.string/split "a\nb\nc" #"\n")` expected=`['a', 'b', 'c']`
    concept_phrase: `splitting a slurped-style string on newlines`
    question_what: `the vector ["a" "b""c"] of three lines`

### G7-12 sample 1/N (form: `(count "hare\ntortoise\n")`, expected: `14`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to the length of a multi-line string (as if read by slurp).
"You hand the form `(count "hare\ntortoise\n")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the count of characters in "hare\ntortoise\n".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
```

### G7-12 sample 2/N (form: `(clojure.string/split "a\nb\nc" #"\n")`, expected: `['a', 'b', 'c']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(clojure.string/split "a\nb\nc" #"\n")` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
splitting a slurped-style string on newlines — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the vector ["a" "b""c"] of three lines.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### G7-12 sample 3/N (form: `(count "hare\ntortoise\n")`, expected: `14`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(count "hare\ntortoise\n")` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the length of a multi-line string (as if read by slurp) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the count of characters in "hare\ntortoise\n".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
```

### G7-12 sample 4/N (form: `(clojure.string/split "a\nb\nc" #"\n")`, expected: `['a', 'b', 'c']`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(clojure.string/split "a\nb\nc" #"\n")`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
splitting a slurped-style string on newlines was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the vector ["a" "b""c"] of three lines? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### G7-12 sample 5/N (form: `(count "hare\ntortoise\n")`, expected: `14`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Beyond the REPL the world had files, streams, and small surprises.
Morgan opened a leather ledger by the meadow, copying down
the length of a multi-line string (as if read by slurp) beside the morning's egg-tally. Oliver,
happy with the day's small gift, watched as they wrote the form `(count "hare\ntortoise\n")`
so the runtime could carry the work the rest of the way.

What Clojure form computes the count of characters in "hare\ntortoise\n"? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
```

## G7-13: line-seq

**examples (2):**

- ex0: form=`(count (clojure.string/split-lines "a\nb\nc"))` expected=`3`
    concept_phrase: `the number of lines in a small text`
    question_what: `the count of lines in "a\nb\nc"`
- ex1: form=`(first (clojure.string/split-lines "first\nsecond"))` expected=`'first'`
    concept_phrase: `the first line of a small text`
    question_what: `the string "first"`

### G7-13 sample 1/N (form: `(count (clojure.string/split-lines "a\nb\nc"))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice had learned not to trust the morning basket on first
glance. at the edge of the market, she typed `(count (clojure.string/split-lines "a\nb\nc"))` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Sam,
imagining all that might be gained, laughed and said no error would ever come — but Alice
insisted on letting the runtime decide, then reading the number of lines in a small text
from whatever it returned.

Write a form whose evaluation gives the count of lines in "a\nb\nc".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### G7-13 sample 2/N (form: `(first (clojure.string/split-lines "first\nsecond"))`, expected: `'first'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `(first (clojure.string/split-lines "first\nsecond"))` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — the first line of a small text would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the string "first".
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### G7-13 sample 3/N (form: `(count (clojure.string/split-lines "a\nb\nc"))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Diana had learned not to trust the morning basket on first
glance. inside a cottage, she typed `(count (clojure.string/split-lines "a\nb\nc"))` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Robin,
with a glint of impatience, laughed and said no error would ever come — but Diana
insisted on letting the runtime decide, then reading the number of lines in a small text
from whatever it returned.

What Clojure form computes the count of lines in "a\nb\nc"? Submit it via `eval`.
---asst---
I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### G7-13 sample 4/N (form: `(first (clojure.string/split-lines "first\nsecond"))`, expected: `'first'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Grace had been trying to teach Carol how the REPL
works. "Here," she said, pointing to the first line of a small text.
"You hand the form `(first (clojure.string/split-lines "first\nsecond"))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the string "first".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### G7-13 sample 5/N (form: `(count (clojure.string/split-lines "a\nb\nc"))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(count (clojure.string/split-lines "a\nb\nc"))` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — the number of lines in a small text would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the count of lines in "a\nb\nc".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

## G7-14: with-open

**examples (1):**

- ex0: form=`(with-out-str (println "hare"))` expected=`'hare\n'`
    concept_phrase: `a resource-scoped capture of println output`
    question_what: `the string "hare\n" from the scoped block`

### G7-14 sample 1/N (form: `(with-out-str (println "hare"))`, expected: `'hare\n'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what a resource-scoped capture of println output comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(with-out-str (println "hare"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the string "hare\n" from the scoped block.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

### G7-14 sample 2/N (form: `(with-out-str (println "hare"))`, expected: `'hare\n'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what a resource-scoped capture of println output comes to."
Edward, who in the meadow had grown used to such claims, asked
him to actually write the form `(with-out-str (println "hare"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the string "hare\n" from the scoped block.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

### G7-14 sample 3/N (form: `(with-out-str (println "hare"))`, expected: `'hare\n'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Alice had learned not to trust the morning basket on first
glance. deep inside a cottage, she typed `(with-out-str (println "hare"))` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Bob,
eyeing the next morning's gift, laughed and said no error would ever come — but Alice
insisted on letting the runtime decide, then reading a resource-scoped capture of println output
from whatever it returned.

What Clojure form computes the string "hare\n" from the scoped block? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

### G7-14 sample 4/N (form: `(with-out-str (println "hare"))`, expected: `'hare\n'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered in the farm to watch
George attempt to outguess Edward at reading the
REPL. Edward pointed to a resource-scoped capture of println output and read out the form
aloud: `(with-out-str (println "hare"))`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the string "hare\n" from the scoped block.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

### G7-14 sample 5/N (form: `(with-out-str (println "hare"))`, expected: `'hare\n'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

At a small stall inside the kitchen, someone had chalked a wager: whoever
predicted the result of `(with-out-str (println "hare"))` first would set the asking
price for the morning's eggs. Carol, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
a resource-scoped capture of println output — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the string "hare\n" from the scoped block.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

## G7-15: *in* and *out*

**examples (2):**

- ex0: form=`(with-out-str (print "x"))` expected=`'x'`
    concept_phrase: `redirecting *out* via with-out-str and printing`
    question_what: `the string "x" captured from *out*`
- ex1: form=`(with-out-str (println))` expected=`'\n'`
    concept_phrase: `a bare println redirected through *out*`
    question_what: `the string "\n"`

### G7-15 sample 1/N (form: `(with-out-str (print "x"))`, expected: `'x'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(with-out-str (print "x"))` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about redirecting *out* via with-out-str and printing; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the string "x" captured from *out*.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G7-15 sample 2/N (form: `(with-out-str (println))`, expected: `'\n'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what a bare println redirected through *out* comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(with-out-str (println))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the string "\n".
---asst---
I set a careful trap with try/catch the way one watches the basket.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### G7-15 sample 3/N (form: `(with-out-str (print "x"))`, expected: `'x'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what redirecting *out* via with-out-str and printing comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `(with-out-str (print "x"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the string "x" captured from *out*.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G7-15 sample 4/N (form: `(with-out-str (println))`, expected: `'\n'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(with-out-str (println))`.
Robin laughed, with a smug grin, and declared it too easy.
Diana said, stepping deliberately, that the only honest way to know
a bare println redirected through *out* was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the string "\n".
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### G7-15 sample 5/N (form: `(with-out-str (print "x"))`, expected: `'x'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the market, the
next entry was redirecting *out* via with-out-str and printing. Bob peered over
their shoulder at the form `(with-out-str (print "x"))` and asked what
it would come out to.

Question: write a Clojure expression for the string "x" captured from *out*.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

## G7-16: edn read

**examples (3):**

- ex0: form=`(clojure.edn/read-string "42")` expected=`42`
    concept_phrase: `reading an edn integer from a string`
    question_what: `the integer 42 read from "42"`
- ex1: form=`(clojure.edn/read-string "{:a 1}")` expected=`{':a': 1}`
    concept_phrase: `reading an edn map from a string`
    question_what: `the map {:a 1} read from "{:a 1}"`
- ex2: form=`(clojure.edn/read-string "[:hare :tortoise]")` expected=`[':hare', ':tortoise']`
    concept_phrase: `reading an edn vector of keywords`
    question_what: `the vector [:hare :tortoise]`

### G7-16 sample 1/N (form: `(clojure.edn/read-string "42")`, expected: `42`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what reading an edn integer from a string comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `(clojure.edn/read-string "42")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the integer 42 read from "42".
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G7-16 sample 2/N (form: `(clojure.edn/read-string "{:a 1}")`, expected: `{':a': 1}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(clojure.edn/read-string "{:a 1}")` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — reading an edn map from a string would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the map {:a 1} read from "{:a 1}".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

### G7-16 sample 3/N (form: `(clojure.edn/read-string "[:hare :tortoise]")`, expected: `[':hare', ':tortoise']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Morgan said, as if the race were already won.
"Anyone with eyes can see what reading an edn vector of keywords comes to."
Sam, who in the market had grown used to such claims, asked
them to actually write the form `(clojure.edn/read-string "[:hare :tortoise]")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the vector [:hare :tortoise].
---asst---
I use ex-info to attach data to the error.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:hare :tortoise]\")"}}]}
```

### G7-16 sample 4/N (form: `(clojure.edn/read-string "42")`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(clojure.edn/read-string "42")` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — reading an edn integer from a string would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the integer 42 read from "42".
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G7-16 sample 5/N (form: `(clojure.edn/read-string "{:a 1}")`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," David said, swaggering through the underbrush.
"Anyone with eyes can see what reading an edn map from a string comes to."
Carol, who in the market had grown used to such claims, asked
him to actually write the form `(clojure.edn/read-string "{:a 1}")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the map {:a 1} read from "{:a 1}".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

## G7-17: JSON roundtrip

**examples (2):**

- ex0: form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` expected=`{':a': 1, ':b': 2}`
    concept_phrase: `writing then reading back a small map (edn-shaped roundtrip)`
    question_what: `the map {:a 1 :b 2} after the roundtrip`
- ex1: form=`(clojure.edn/read-string (pr-str [1 2 3]))` expected=`[1, 2, 3]`
    concept_phrase: `round-tripping a vector through pr-str then edn/read-string`
    question_what: `the vector [1 2 3]`

### G7-17 sample 1/N (form: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`, expected: `{':a': 1, ':b': 2}`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`.
Grace laughed, boasting at every turn, and declared it too easy.
Oliver said, her eyes always on the path, that the only honest way to know
writing then reading back a small map (edn-shaped roundtrip) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the map {:a 1 :b 2} after the roundtrip.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### G7-17 sample 2/N (form: `(clojure.edn/read-string (pr-str [1 2 3]))`, expected: `[1, 2, 3]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Beyond the REPL the world had files, streams, and small surprises.
Fiona opened a leather ledger in the village, copying down
round-tripping a vector through pr-str then edn/read-string beside the morning's egg-tally. Alex,
untroubled by the village gossip, watched as she wrote the form `(clojure.edn/read-string (pr-str [1 2 3]))`
so the runtime could carry the work the rest of the way.

Question: write a Clojure expression for the vector [1 2 3].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### G7-17 sample 3/N (form: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`, expected: `{':a': 1, ':b': 2}`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched writing then reading back a small map (edn-shaped roundtrip) into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the map {:a 1 :b 2} after the roundtrip.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### G7-17 sample 4/N (form: `(clojure.edn/read-string (pr-str [1 2 3]))`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small slip of paper inside the kitchen carried the form `(clojure.edn/read-string (pr-str [1 2 3]))`.
Carol glanced at it and hurried on toward the market, certain
there was no trouble. Alex sat down by the egg-basket,
her eyes always on the path, and worked through round-tripping a vector through pr-str then edn/read-string step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again.

Write a Clojure expression that computes the vector [1 2 3].
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### G7-17 sample 5/N (form: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`, expected: `{':a': 1, ':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Emily said, boasting at every turn.
"Anyone with eyes can see what writing then reading back a small map (edn-shaped roundtrip) comes to."
Carol, who in the village had grown used to such claims, asked
her to actually write the form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the map {:a 1 :b 2} after the roundtrip.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

## G7-18: Shell command

**examples (2):**

- ex0: form=`(:cmd {:cmd "ls" :args ["-l"]})` expected=`'ls'`
    concept_phrase: `the :cmd portion of a shell-call descriptor map`
    question_what: `the string "ls"`
- ex1: form=`(count (:args {:cmd "echo" :args ["hello" "world"]}))` expected=`2`
    concept_phrase: `the number of args in a shell-call descriptor`
    question_what: `the count of args, which is 2`

### G7-18 sample 1/N (form: `(:cmd {:cmd "ls" :args ["-l"]})`, expected: `'ls'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol had learned not to trust the morning basket on first
glance. inside the barn, she typed `(:cmd {:cmd "ls" :args ["-l"]})` carefully, ready
to catch whatever the REPL might throw back, the way one sets a quiet
trap for whatever takes an egg in the night. Alice,
with a glint of impatience, laughed and said no error would ever come — but Carol
insisted on letting the runtime decide, then reading the :cmd portion of a shell-call descriptor map
from whatever it returned.

What Clojure form computes the string "ls"? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### G7-18 sample 2/N (form: `(count (:args {:cmd "echo" :args ["hello" "world"]}))`, expected: `2`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice offered a small basket of eggs as a wager in the farm:
whoever guessed the result of `(count (:args {:cmd "echo" :args ["hello" "world"]}))` first would keep them.
Emily, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the number of args in a shell-call descriptor; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a form whose evaluation gives the count of args, which is 2.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### G7-18 sample 3/N (form: `(:cmd {:cmd "ls" :args ["-l"]})`, expected: `'ls'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the :cmd portion of a shell-call descriptor map into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(:cmd {:cmd "ls" :args ["-l"]})` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the string "ls".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### G7-18 sample 4/N (form: `(count (:args {:cmd "echo" :args ["hello" "world"]}))`, expected: `2`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, David stopped inside a cottage
with a basket of eggs and refused to move on until someone could
prove what the form `(count (:args {:cmd "echo" :args ["hello" "world"]}))` evaluated to. David called it
impossible. Sam, walking up at an unhurried pace, simply
said: "Submit the number of args in a shell-call descriptor to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the count of args, which is 2.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### G7-18 sample 5/N (form: `(:cmd {:cmd "ls" :args ["-l"]})`, expected: `'ls'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between Diana and Morgan. The bet was
simple: predict what `(:cmd {:cmd "ls" :args ["-l"]})` would return. Diana,
with a glint of impatience, was certain about the answer. Morgan asked
her, with steady, careful steps, to actually write the form into the
REPL — the :cmd portion of a shell-call descriptor map would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the string "ls".
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

