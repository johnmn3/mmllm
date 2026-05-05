# crow-pitcher grade 7 — deep spot-check

5 records per subject for hand-audit.

---

## G7-01: throw

### G7-01 record 1  •  form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  expected `':thrown'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today on the road, the next entry was
throwing an exception that is then caught. Sable the crow peered over his shoulder
at the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and asked what it would come out to.

Write a form whose evaluation gives the keyword :thrown returned after the throw is caught.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 record 2  •  form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  expected `':thrown'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the farm: whoever guessed the result of `(try (throw (Exception. "bad")) (catch Exception e :thrown))`
first would win the right to claim the next clear water they found.
Sable the crow, with steady, careful steps, said it was easier to ask the REPL
about throwing an exception that is then caught than to argue.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 record 3  •  form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  expected `':thrown'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the hilltop, the next entry was
throwing an exception that is then caught. Sable the crow peered over his shoulder
at the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and asked what it would come out to.

Write a form whose evaluation gives the keyword :thrown returned after the throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 record 4  •  form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  expected `':thrown'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the market, the next entry was
throwing an exception that is then caught. Korvus the crow peered over her shoulder
at the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` and asked what it would come out to.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-01 record 5  •  form `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  expected `':thrown'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted by the farm on the rim of an old
pitcher where someone had scratched throwing an exception that is then caught. Caw,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(try (throw (Exception. "bad")) (catch Exception e :thrown))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the keyword :thrown returned after the throw is caught? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

## G7-02: try / catch

### G7-02 record 1  •  form `(try (/ 1 0) (catch Exception e :caught))`  •  expected `':caught'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small slip of bark atop the hilltop carried the form `(try (/ 1 0) (catch Exception e :caught))`. Sable
glanced at it and flew on, certain there was no trouble.
Korvus the crow settled in, untroubled by what others thought, and worked through
a division by zero wrapped in try/catch step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for the keyword :caught returned by the catch branch.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### G7-02 record 2  •  form `(try 42 (catch Exception e :caught))`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree near the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(try 42 (catch Exception e :caught))`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
a try with no error — the body's value is returned was to drop it into the REPL.

Write a form whose evaluation gives the value 42 from the no-error branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### G7-02 record 3  •  form `(try (/ 1 0) (catch Exception e :caught))`  •  expected `':caught'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched a division by zero wrapped in try/catch. Sable,
shouting until her voice cracked, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(try (/ 1 0) (catch Exception e :caught))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the keyword :caught returned by the catch branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### G7-02 record 4  •  form `(try 42 (catch Exception e :caught))`  •  expected `42`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place in the orchard.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the orchard and refused to fly on until someone could prove what the form
`(try 42 (catch Exception e :caught))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a try with no error — the body's value is returned into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the value 42 from the no-error branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 42 (catch Exception e :caught))"}}]}
```

### G7-02 record 5  •  form `(try (/ 1 0) (catch Exception e :caught))`  •  expected `':caught'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the garden.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to a division by zero wrapped in try/catch.
"You hand the form `(try (/ 1 0) (catch Exception e :caught))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

## G7-03: try / finally

### G7-03 record 1  •  form `(try 7 (finally :cleanup))`  •  expected `7`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(try 7 (finally :cleanup))` first would drink
first when the water rose. Caw the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
a try whose finally clause runs but doesn't change the value.

Write a form whose evaluation gives the value 7 from the body (finally is for side effects).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### G7-03 record 2  •  form `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))`  •  expected `':caught'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Sable the crow alighted
near the garden and refused to fly on until someone could prove what the form
`(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` evaluated to. Sable called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a finally that runs before the outer catch fires into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the keyword :caught (the outer catch handles the divide-by-zero).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### G7-03 record 3  •  form `(try 7 (finally :cleanup))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the garden.

Sable the crow had learned not to trust a form on first reading.
in the garden, they dropped `(try 7 (finally :cleanup))` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Caw the crow, as if the race were already won, laughed and said no error would ever
come — but Sable insisted on letting the runtime decide, then
reading a try whose finally clause runs but doesn't change the value from whatever it returned.

What Clojure form computes the value 7 from the body (finally is for side effects)? Submit it via `eval`.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### G7-03 record 4  •  form `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))`  •  expected `':caught'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the garden.

Korvus the crow etched a wager along the rim of a chipped pitcher
in the garden: whoever predicted the result of `(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))` first would set
the next day's foraging route. Sable the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
a finally that runs before the outer catch fires.

Question: write a Clojure expression for the keyword :caught (the outer catch handles the divide-by-zero).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))"}}]}
```

### G7-03 record 5  •  form `(try 7 (finally :cleanup))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the village and refused to fly on until someone could prove what the form
`(try 7 (finally :cleanup))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a try whose finally clause runs but doesn't change the value into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the value 7 from the body (finally is for side effects).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

## G7-04: ex-info

### G7-04 record 1  •  form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`  •  expected `{':a': 1}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the farm.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to throwing an ex-info with attached data, then reading it back.
"You hand the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### G7-04 record 2  •  form `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`  •  expected `':v'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was in the garden.

At a moss-flecked pitcher in the garden, Caw the crow sketched a small
wager: whoever guessed the result of `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
extracting a single key from the caught ex-info's data.

Write a Clojure expression that computes the value :v at key :k in the ex-data.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### G7-04 record 3  •  form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`  •  expected `{':a': 1}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Sable the crow alighted at the edge of the garden on the rim of an old
pitcher where someone had scratched throwing an ex-info with attached data, then reading it back. Korvus,
with growing alarm, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the data map {:a 1} pulled from the caught ex-info.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### G7-04 record 4  •  form `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))`  •  expected `':v'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Beyond the REPL the world had files, streams, and surprises.
Sable the crow opened a small notebook by the farm, copying down
extracting a single key from the caught ex-info's data. Korvus, her legs heavy from sprinting, watched as they
wrote the form `(try (throw (ex-info "x" {:k :v})) (catch Exception e (:k (ex-data e))))` so the runtime could carry the work
the rest of the way.

Question: write a Clojure expression for the value :v at key :k in the ex-data.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))"}}]}
```

### G7-04 record 5  •  form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`  •  expected `{':a': 1}`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
throwing an ex-info with attached data, then reading it back.

Write a Clojure expression that computes the data map {:a 1} pulled from the caught ex-info.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

## G7-05: nil punning

### G7-05 record 1  •  form `(some? nil)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the market.

At a moss-flecked pitcher in the market, Korvus the crow sketched a small
wager: whoever guessed the result of `(some? nil)` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the predicate (some? nil).

Write a Clojure expression that computes whether nil counts as some?.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

### G7-05 record 2  •  form `(some? 0)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place along the road.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the road: whoever guessed the result of `(some? 0)`
first would win the right to claim the next clear water they found.
Caw the crow, stepping deliberately, said it was easier to ask the REPL
about the predicate (some? 0) — 0 is not nil than to argue.

What Clojure form computes whether 0 counts as some?? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(some? 0)"}}]}
```

### G7-05 record 3  •  form `(first nil)`  •  expected `None`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the village.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the village and refused to fly on until someone could prove what the form
`(first nil)` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
calling first on nil into the REPL. Whatever rises is the answer."

Write a Clojure expression that computes the value of (first nil), which is nil.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(first nil)"}}]}
```

### G7-05 record 4  •  form `(count nil)`  •  expected `0`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened on the road.

Caw the crow had learned not to trust a form on first reading.
along the road, she dropped `(count nil)` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Korvus the crow, swaggering through the underbrush, laughed and said no error would ever
come — but Caw insisted on letting the runtime decide, then
reading counting a nil collection from whatever it returned.

Write a Clojure expression that computes the count of nil, which is 0.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count nil)"}}]}
```

### G7-05 record 5  •  form `(some? nil)`  •  expected `False`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened in the meadow.

A small slip of bark by the meadow carried the form `(some? nil)`. Caw
glanced at it and flew on, certain there was no trouble.
Sable the crow settled in, her eyes always on the path, and worked through
the predicate (some? nil) step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for whether nil counts as some?.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

## G7-06: pre and post conditions

### G7-06 record 1  •  form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`  •  expected `10`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the market.

A small slip of bark near the market carried the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`. Korvus
glanced at it and flew on, certain there was no trouble.
Sable the crow settled in, untroubled by what others thought, and worked through
a fn with a :pre condition that is satisfied step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for the value returned when the precondition holds and 5 is doubled.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### G7-06 record 2  •  form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`  •  expected `':pre-failed'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow etched a wager along the rim of a chipped pitcher
by the farm: whoever predicted the result of `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` first would set
the next day's foraging route. Sable the crow, without complaint, said it
would be simpler to drop the form into the REPL than to bicker about
a :pre condition that fails, caught by surrounding try.

Question: write a Clojure expression for the keyword :pre-failed when the pre-check rejects -1.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### G7-06 record 3  •  form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`  •  expected `10`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened in the garden.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a fn with a :pre condition that is satisfied.
"You hand the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, parched from the long flight, agreed to try.

Write a form whose evaluation gives the value returned when the precondition holds and 5 is doubled.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### G7-06 record 4  •  form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))`  •  expected `':pre-failed'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the orchard.

"There is no need to evaluate that," Sable the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what a :pre condition that fails, caught by surrounding try comes to."
Caw the crow, who near the orchard had grown used to such claims, asked
them to actually write the form `(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the keyword :pre-failed when the pre-check rejects -1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))"}}]}
```

### G7-06 record 5  •  form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`  •  expected `10`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small slip of bark near the market carried the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`. Sable
glanced at it and flew on, certain there was no trouble.
Caw the crow settled in, her eyes always on the path, and worked through
a fn with a :pre condition that is satisfied step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

What Clojure form computes the value returned when the precondition holds and 5 is doubled? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

## G7-07: assert

### G7-07 record 1  •  form `(do (assert (= 1 1)) :ok)`  •  expected `':ok'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was at the edge of the market.

A small slip of bark by the market carried the form `(do (assert (= 1 1)) :ok)`. Caw
glanced at it and flew on, certain there was no trouble.
Korvus the crow settled in, stepping deliberately, and worked through
an assert that passes, followed by a return value step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for the keyword :ok returned after the assert succeeds.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### G7-07 record 2  •  form `(try (assert (= 1 2)) (catch Throwable e :asserted))`  •  expected `':asserted'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had learned not to trust a form on first reading.
at the edge of the village, they dropped `(try (assert (= 1 2)) (catch Throwable e :asserted))` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Korvus the crow, boasting at every turn, laughed and said no error would ever
come — but Sable insisted on letting the runtime decide, then
reading an assert that fails, caught by surrounding try from whatever it returned.

Write a form whose evaluation gives the keyword :asserted when the assertion rejects (= 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### G7-07 record 3  •  form `(do (assert (= 1 1)) :ok)`  •  expected `':ok'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the road.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the road: whoever guessed the result of `(do (assert (= 1 1)) :ok)`
first would win the right to claim the next clear water they found.
Caw the crow, with steady, careful steps, said it was easier to ask the REPL
about an assert that passes, followed by a return value than to argue.

Question: write a Clojure expression for the keyword :ok returned after the assert succeeds.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### G7-07 record 4  •  form `(try (assert (= 1 2)) (catch Throwable e :asserted))`  •  expected `':asserted'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Beyond the REPL the world had files, streams, and surprises.
Caw the crow opened a small notebook in the meadow, copying down
an assert that fails, caught by surrounding try. Korvus, drowsy from the warm sun, watched as she
wrote the form `(try (assert (= 1 2)) (catch Throwable e :asserted))` so the runtime could carry the work
the rest of the way.

Write a form whose evaluation gives the keyword :asserted when the assertion rejects (= 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (assert (= 1 2)) (catch Throwable e :asserted))"}}]}
```

### G7-07 record 5  •  form `(do (assert (= 1 1)) :ok)`  •  expected `':ok'`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher on the hilltop, Caw the crow sketched a small
wager: whoever guessed the result of `(do (assert (= 1 1)) :ok)` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
an assert that passes, followed by a return value.

Question: write a Clojure expression for the keyword :ok returned after the assert succeeds.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

## G7-08: prn and pprint

### G7-08 record 1  •  form `(with-out-str (prn 42))`  •  expected `'42\n'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place by the farm.

Korvus the crow etched a wager along the rim of a chipped pitcher
by the farm: whoever predicted the result of `(with-out-str (prn 42))` first would set
the next day's foraging route. Caw the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
capturing the output of (prn 42).

What Clojure form computes the string "42\n" produced by prn? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### G7-08 record 2  •  form `(with-out-str (prn :crow))`  •  expected `':crow\n'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened by the farm.

Korvus the crow had been trying to teach Caw the crow how the REPL
works. "Look here," he said, pointing to capturing prn applied to the keyword :crow.
"You hand the form `(with-out-str (prn :crow))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, dry-throated and desperate, agreed to try.

Question: write a Clojure expression for the string ":crow\n" produced by prn.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :crow))"}}]}
```

### G7-08 record 3  •  form `(with-out-str (prn 42))`  •  expected `'42\n'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place in the market.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to capturing the output of (prn 42).
"You hand the form `(with-out-str (prn 42))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, parched from the long flight, agreed to try.

Write a Clojure expression that computes the string "42\n" produced by prn.

---

I let each form raise the surface a little closer to the answer.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### G7-08 record 4  •  form `(with-out-str (prn :crow))`  •  expected `':crow\n'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small slip of bark in the orchard carried the form `(with-out-str (prn :crow))`. Caw
glanced at it and flew on, certain there was no trouble.
Korvus the crow settled in, untroubled by what others thought, and worked through
capturing prn applied to the keyword :crow step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

What Clojure form computes the string ":crow\n" produced by prn? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn :crow))"}}]}
```

### G7-08 record 5  •  form `(with-out-str (prn 42))`  •  expected `'42\n'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow and Korvus the crow alighted near the road on the rim of an old
pitcher where someone had scratched capturing the output of (prn 42). Caw,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(with-out-str (prn 42))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the string "42\n" produced by prn.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

## G7-09: tap>

### G7-09 record 1  •  form `(tap> :hello)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow had learned not to trust a form on first reading.
in the orchard, he dropped `(tap> :hello)` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Caw the crow, as if the race were already won, laughed and said no error would ever
come — but Korvus insisted on letting the runtime decide, then
reading tapping a value into the tap pool from whatever it returned.

Write a Clojure expression that computes the boolean true returned by tap>.

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### G7-09 record 2  •  form `(tap> 42)`  •  expected `True`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the garden.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to tapping the number 42 into the tap pool.
"You hand the form `(tap> 42)` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes the boolean true (tap> always returns true on send).

---

{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### G7-09 record 3  •  form `(tap> :hello)`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small slip of bark near the village carried the form `(tap> :hello)`. Korvus
glanced at it and flew on, certain there was no trouble.
Caw the crow settled in, untroubled by what others thought, and worked through
tapping a value into the tap pool step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

What Clojure form computes the boolean true returned by tap>? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### G7-09 record 4  •  form `(tap> 42)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered at the edge of the village to watch
Sable the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to tapping the number 42 into the tap pool and read out the form
aloud: `(tap> 42)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the boolean true (tap> always returns true on send).

---

{"tool_calls":[{"name":"eval","args":{"form":"(tap> 42)"}}]}
```

### G7-09 record 5  •  form `(tap> :hello)`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what tapping a value into the tap pool comes to."
Caw the crow, who near the farm had grown used to such claims, asked
him to actually write the form `(tap> :hello)` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the boolean true returned by tap>.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

## G7-10: doc and source

### G7-10 record 1  •  form `(:doc (meta '^{:doc "adds two"} plus))`  •  expected `'adds two'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust at the edge of the village: whoever guessed the result of `(:doc (meta '^{:doc "adds two"} plus))`
first would win the right to claim the next clear water they found.
Sable the crow, her eyes always on the path, said it was easier to ask the REPL
about the :doc metadata on a symbol — what doc would print than to argue.

Question: write a Clojure expression for the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 record 2  •  form `(:doc (meta '^{:doc "adds two"} plus))`  •  expected `'adds two'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. All this took place near the road.

Caw the crow and Korvus the crow alighted on the road on the rim of an old
pitcher where someone had scratched the :doc metadata on a symbol — what doc would print. Caw,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(:doc (meta '^{:doc "adds two"} plus))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 record 3  •  form `(:doc (meta '^{:doc "adds two"} plus))`  •  expected `'adds two'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the village to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the :doc metadata on a symbol — what doc would print and read out the form
aloud: `(:doc (meta '^{:doc "adds two"} plus))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 record 4  •  form `(:doc (meta '^{:doc "adds two"} plus))`  •  expected `'adds two'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the orchard, the next entry was
the :doc metadata on a symbol — what doc would print. Korvus the crow peered over her shoulder
at the form `(:doc (meta '^{:doc "adds two"} plus))` and asked what it would come out to.

Question: write a Clojure expression for the string "adds two" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-10 record 5  •  form `(:doc (meta '^{:doc "adds two"} plus))`  •  expected `'adds two'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

At a moss-flecked pitcher along the road, Caw the crow sketched a small
wager: whoever guessed the result of `(:doc (meta '^{:doc "adds two"} plus))` first would drink
first when the water rose. Korvus the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the :doc metadata on a symbol — what doc would print.

Write a Clojure expression that computes the string "adds two" from the metadata.

---

I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

## G7-11: Reading stack traces

### G7-11 record 1  •  form `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`  •  expected `'oops'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was atop the hilltop.

At a moss-flecked pitcher near the hilltop, Caw the crow sketched a small
wager: whoever guessed the result of `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` first would drink
first when the water rose. Sable the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
extracting the message from a caught exception.

Write a form whose evaluation gives the string "oops" from the caught Exception.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 record 2  •  form `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`  •  expected `'trouble'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the orchard.

"There is no need to evaluate that," Caw the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what the message of a caught ex-info comes to."
Sable the crow, who by the orchard had grown used to such claims, asked
her to actually write the form `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` and drop it
into the REPL — just to be sure.

Write a Clojure expression that computes the string "trouble".

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 record 3  •  form `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`  •  expected `'oops'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the garden.

Beyond the REPL the world had files, streams, and surprises.
Caw the crow opened a small notebook at the edge of the garden, copying down
extracting the message from a caught exception. Korvus, yawning at the soft moss, watched as she
wrote the form `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` so the runtime could carry the work
the rest of the way.

What Clojure form computes the string "oops" from the caught Exception? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 record 4  •  form `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))`  •  expected `'trouble'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher at the edge of the orchard, Sable the crow sketched a small
wager: whoever guessed the result of `(try (throw (ex-info "trouble" {})) (catch Exception e (.getMessage e)))` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
the message of a caught ex-info.

Question: write a Clojure expression for the string "trouble".

---

I wrap the form in try/catch and let the REPL handle the error.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))"}}]}
```

### G7-11 record 5  •  form `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`  •  expected `'oops'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` first would set
the next day's foraging route. Sable the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
extracting the message from a caught exception.

Question: write a Clojure expression for the string "oops" from the caught Exception.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

## G7-12: slurp and spit

### G7-12 record 1  •  form `(count "crow\npitcher\n")`  •  expected `13`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had learned not to trust a form on first reading.
near the orchard, she dropped `(count "crow\npitcher\n")` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Sable the crow, as if the race were already won, laughed and said no error would ever
come — but Caw insisted on letting the runtime decide, then
reading the length of a multi-line string (as if read by slurp) from whatever it returned.

Write a form whose evaluation gives the count of characters in "crow\npitcher\n".

---

I use ex-info to attach data to the error.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\\npitcher\\n\")"}}]}
```

### G7-12 record 2  •  form `(clojure.string/split "a\nb\nc" #"\n")`  •  expected `['a', 'b', 'c']`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the garden, the next entry was
splitting a slurped-style string on newlines. Korvus the crow peered over their shoulder
at the form `(clojure.string/split "a\nb\nc" #"\n")` and asked what it would come out to.

Write a Clojure expression that computes the vector ["a" "b""c"] of three lines.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### G7-12 record 3  •  form `(count "crow\npitcher\n")`  •  expected `13`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the farm.

A wooden sign nailed to a tree at the edge of the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(count "crow\npitcher\n")`. Korvus laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
the length of a multi-line string (as if read by slurp) was to drop it into the REPL.

What Clojure form computes the count of characters in "crow\npitcher\n"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\\npitcher\\n\")"}}]}
```

### G7-12 record 4  •  form `(clojure.string/split "a\nb\nc" #"\n")`  •  expected `['a', 'b', 'c']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place atop the hilltop.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to splitting a slurped-style string on newlines.
"You hand the form `(clojure.string/split "a\nb\nc" #"\n")` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the vector ["a" "b""c"] of three lines.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"a\\nb\\nc\" #\"\\n\")"}}]}
```

### G7-12 record 5  •  form `(count "crow\npitcher\n")`  •  expected `13`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the orchard.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the orchard, the next entry was
the length of a multi-line string (as if read by slurp). Korvus the crow peered over their shoulder
at the form `(count "crow\npitcher\n")` and asked what it would come out to.

Question: write a Clojure expression for the count of characters in "crow\npitcher\n".

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"crow\\npitcher\\n\")"}}]}
```

## G7-13: line-seq

### G7-13 record 1  •  form `(count (clojure.string/split-lines "a\nb\nc"))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A small audience of sparrows had gathered near the hilltop to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to the number of lines in a small text and read out the form
aloud: `(count (clojure.string/split-lines "a\nb\nc"))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the count of lines in "a\nb\nc".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### G7-13 record 2  •  form `(first (clojure.string/split-lines "first\nsecond"))`  •  expected `'first'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small slip of bark along the road carried the form `(first (clojure.string/split-lines "first\nsecond"))`. Caw
glanced at it and flew on, certain there was no trouble.
Sable the crow settled in, without complaint, and worked through
the first line of a small text step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for the string "first".

---

{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### G7-13 record 3  •  form `(count (clojure.string/split-lines "a\nb\nc"))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was at the edge of the orchard.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the number of lines in a small text.
"You hand the form `(count (clojure.string/split-lines "a\nb\nc"))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

What Clojure form computes the count of lines in "a\nb\nc"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### G7-13 record 4  •  form `(first (clojure.string/split-lines "first\nsecond"))`  •  expected `'first'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
the first line of a small text. Caw the crow peered over their shoulder
at the form `(first (clojure.string/split-lines "first\nsecond"))` and asked what it would come out to.

Write a form whose evaluation gives the string "first".

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(first (clojure.string/split-lines \"first\\nsecond\"))"}}]}
```

### G7-13 record 5  •  form `(count (clojure.string/split-lines "a\nb\nc"))`  •  expected `3`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what the number of lines in a small text comes to."
Sable the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(count (clojure.string/split-lines "a\nb\nc"))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the count of lines in "a\nb\nc".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

## G7-14: with-open

### G7-14 record 1  •  form `(with-out-str (println "crow"))`  •  expected `'crow\n'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree in the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(with-out-str (println "crow"))`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
a resource-scoped capture of println output was to drop it into the REPL.

What Clojure form computes the string "crow\n" from the scoped block? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"crow\"))"}}]}
```

### G7-14 record 2  •  form `(with-out-str (println "crow"))`  •  expected `'crow\n'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

With a careful tap of their beak, Sable the crow marked out a
wager in the dust by the village: whoever guessed the result of `(with-out-str (println "crow"))`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about a resource-scoped capture of println output than to argue.

What Clojure form computes the string "crow\n" from the scoped block? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"crow\"))"}}]}
```

### G7-14 record 3  •  form `(with-out-str (println "crow"))`  •  expected `'crow\n'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had learned not to trust a form on first reading.
at the edge of the meadow, he dropped `(with-out-str (println "crow"))` carefully into the
REPL, ready to catch whatever the runtime might throw back.
Caw the crow, with great whoops of laughter, laughed and said no error would ever
come — but Korvus insisted on letting the runtime decide, then
reading a resource-scoped capture of println output from whatever it returned.

Question: write a Clojure expression for the string "crow\n" from the scoped block.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"crow\"))"}}]}
```

### G7-14 record 4  •  form `(with-out-str (println "crow"))`  •  expected `'crow\n'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the market.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the market and refused to fly on until someone could prove what the form
`(with-out-str (println "crow"))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a resource-scoped capture of println output into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the string "crow\n" from the scoped block.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"crow\"))"}}]}
```

### G7-14 record 5  •  form `(with-out-str (println "crow"))`  •  expected `'crow\n'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the market.

A wooden sign nailed to a tree near the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(with-out-str (println "crow"))`. Sable laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
a resource-scoped capture of println output was to drop it into the REPL.

Write a form whose evaluation gives the string "crow\n" from the scoped block.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"crow\"))"}}]}
```

## G7-15: *in* and *out*

### G7-15 record 1  •  form `(with-out-str (print "x"))`  •  expected `'x'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the village.

A small slip of bark in the village carried the form `(with-out-str (print "x"))`. Caw
glanced at it and flew on, certain there was no trouble.
Sable the crow settled in, with steady, careful steps, and worked through
redirecting *out* via with-out-str and printing step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Write a form whose evaluation gives the string "x" captured from *out*.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G7-15 record 2  •  form `(with-out-str (println))`  •  expected `'\n'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small slip of bark at the edge of the hilltop carried the form `(with-out-str (println))`. Caw
glanced at it and flew on, certain there was no trouble.
Korvus the crow settled in, without complaint, and worked through
a bare println redirected through *out* step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

Question: write a Clojure expression for the string "\n".

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### G7-15 record 3  •  form `(with-out-str (print "x"))`  •  expected `'x'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow and Sable the crow alighted at the edge of the village on the rim of an old
pitcher where someone had scratched redirecting *out* via with-out-str and printing. Caw,
wide-eyed with fear, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(with-out-str (print "x"))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the string "x" captured from *out*.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G7-15 record 4  •  form `(with-out-str (println))`  •  expected `'\n'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the garden.

Caw the crow etched a wager along the rim of a chipped pitcher
in the garden: whoever predicted the result of `(with-out-str (println))` first would set
the next day's foraging route. Korvus the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
a bare println redirected through *out*.

Write a form whose evaluation gives the string "\n".

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println))"}}]}
```

### G7-15 record 5  •  form `(with-out-str (print "x"))`  •  expected `'x'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the orchard.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the orchard, the next entry was
redirecting *out* via with-out-str and printing. Korvus the crow peered over her shoulder
at the form `(with-out-str (print "x"))` and asked what it would come out to.

Write a form whose evaluation gives the string "x" captured from *out*.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

## G7-16: edn read

### G7-16 record 1  •  form `(clojure.edn/read-string "42")`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the garden.

Korvus the crow and Caw the crow alighted in the garden on the rim of an old
pitcher where someone had scratched reading an edn integer from a string. Korvus,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(clojure.edn/read-string "42")` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Question: write a Clojure expression for the integer 42 read from "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G7-16 record 2  •  form `(clojure.edn/read-string "{:a 1}")`  •  expected `{':a': 1}`

```
Hunger and thirst had driven the Crow far from her usual perch.

"There is no need to evaluate that," Sable the crow said, as if the race were already won.
"Anyone with a sharp eye can see what reading an edn map from a string comes to."
Caw the crow, who by the village had grown used to such claims, asked
them to actually write the form `(clojure.edn/read-string "{:a 1}")` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the map {:a 1} read from "{:a 1}".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

### G7-16 record 3  •  form `(clojure.edn/read-string "[:hare :tortoise]")`  •  expected `[':hare', ':tortoise']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the hilltop.

Korvus the crow etched a wager along the rim of a chipped pitcher
near the hilltop: whoever predicted the result of `(clojure.edn/read-string "[:hare :tortoise]")` first would set
the next day's foraging route. Caw the crow, untroubled by what others thought, said it
would be simpler to drop the form into the REPL than to bicker about
reading an edn vector of keywords.

Write a form whose evaluation gives the vector [:hare :tortoise].

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:hare :tortoise]\")"}}]}
```

### G7-16 record 4  •  form `(clojure.edn/read-string "42")`  •  expected `42`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small slip of bark in the garden carried the form `(clojure.edn/read-string "42")`. Caw
glanced at it and flew on, certain there was no trouble.
Sable the crow settled in, her eyes always on the path, and worked through
reading an edn integer from a string step by step — ready, if anything went wrong, to
read the stack trace from top to bottom and try again.

What Clojure form computes the integer 42 read from "42"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G7-16 record 5  •  form `(clojure.edn/read-string "{:a 1}")`  •  expected `{':a': 1}`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened on the hilltop.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to reading an edn map from a string.
"You hand the form `(clojure.edn/read-string "{:a 1}")` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

Write a form whose evaluation gives the map {:a 1} read from "{:a 1}".

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"{:a 1}\")"}}]}
```

## G7-17: JSON roundtrip

### G7-17 record 1  •  form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`  •  expected `{':a': 1, ':b': 2}`

```
Hunger and thirst had driven the Crow far from her usual perch.

Beyond the REPL the world had files, streams, and surprises.
Korvus the crow opened a small notebook at the edge of the hilltop, copying down
writing then reading back a small map (edn-shaped roundtrip). Sable, yawning at the soft moss, watched as he
wrote the form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))` so the runtime could carry the work
the rest of the way.

Question: write a Clojure expression for the map {:a 1 :b 2} after the roundtrip.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### G7-17 record 2  •  form `(clojure.edn/read-string (pr-str [1 2 3]))`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the hilltop and refused to fly on until someone could prove what the form
`(clojure.edn/read-string (pr-str [1 2 3]))` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
round-tripping a vector through pr-str then edn/read-string into the REPL. Whatever rises is the answer."

What Clojure form computes the vector [1 2 3]? Submit it via `eval`.

---

I use ex-info to attach data to the error.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### G7-17 record 3  •  form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`  •  expected `{':a': 1, ':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree by the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`. Korvus laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
writing then reading back a small map (edn-shaped roundtrip) was to drop it into the REPL.

Write a Clojure expression that computes the map {:a 1 :b 2} after the roundtrip.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### G7-17 record 4  •  form `(clojure.edn/read-string (pr-str [1 2 3]))`  •  expected `[1, 2, 3]`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust near the road: whoever guessed the result of `(clojure.edn/read-string (pr-str [1 2 3]))`
first would win the right to claim the next clear water they found.
Caw the crow, saying very little, said it was easier to ask the REPL
about round-tripping a vector through pr-str then edn/read-string than to argue.

Question: write a Clojure expression for the vector [1 2 3].

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str [1 2 3]))"}}]}
```

### G7-17 record 5  •  form `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`  •  expected `{':a': 1, ':b': 2}`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the garden.

A small audience of sparrows had gathered by the garden to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to writing then reading back a small map (edn-shaped roundtrip) and read out the form
aloud: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the map {:a 1 :b 2} after the roundtrip? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

## G7-18: Shell command

### G7-18 record 1  •  form `(:cmd {:cmd "ls" :args ["-l"]})`  •  expected `'ls'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the market.

Korvus the crow had been trying to teach Sable the crow how the REPL
works. "Look here," he said, pointing to the :cmd portion of a shell-call descriptor map.
"You hand the form `(:cmd {:cmd "ls" :args ["-l"]})` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the string "ls".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### G7-18 record 2  •  form `(count (:args {:cmd "echo" :args ["hello" "world"]}))`  •  expected `2`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the orchard.

Sable the crow and Korvus the crow alighted by the orchard on the rim of an old
pitcher where someone had scratched the number of args in a shell-call descriptor. Sable,
in a panic, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(count (:args {:cmd "echo" :args ["hello" "world"]}))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the count of args, which is 2? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### G7-18 record 3  •  form `(:cmd {:cmd "ls" :args ["-l"]})`  •  expected `'ls'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place atop the hilltop.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(:cmd {:cmd "ls" :args ["-l"]})`. Sable laughed, with a smug grin, and declared it
too easy. Caw said patiently that the only way to be sure of
the :cmd portion of a shell-call descriptor map was to drop it into the REPL.

Question: write a Clojure expression for the string "ls".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

### G7-18 record 4  •  form `(count (:args {:cmd "echo" :args ["hello" "world"]}))`  •  expected `2`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
at the edge of the meadow and refused to fly on until someone could prove what the form
`(count (:args {:cmd "echo" :args ["hello" "world"]}))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
the number of args in a shell-call descriptor into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the count of args, which is 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))"}}]}
```

### G7-18 record 5  •  form `(:cmd {:cmd "ls" :args ["-l"]})`  •  expected `'ls'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow and Caw the crow alighted by the village on the rim of an old
pitcher where someone had scratched the :cmd portion of a shell-call descriptor map. Korvus,
with growing alarm, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(:cmd {:cmd "ls" :args ["-l"]})` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a form whose evaluation gives the string "ls".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

