# Grade 9 goose-eggs — deep spot-check

5 rendered records per subject (18 subjects × 5 = 90 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G9-01: Immutability as default — review

**examples (2):**

- ex0: form=`(let [m {:a 1}] (assoc m :b 2) m)` expected=`{':a': 1}`
    concept_phrase: `binding m, calling (assoc m :b 2), then returning m unchanged`
    question_what: `the original map after a non-mutating assoc`
- ex1: form=`(let [v [1 2 3]] (conj v 4) v)` expected=`[1, 2, 3]`
    concept_phrase: `binding v, calling (conj v 4), then returning v unchanged`
    question_what: `the original vector after conj`

### G9-01 sample 1/N (form: `(let [m {:a 1}] (assoc m :b 2) m)`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Why count one coin at a time?" Carol demanded near the market, eyeing
the chest. "She could just take the lot at once!"
Alice, without complaint, sketched out binding m, calling (assoc m :b 2), then returning m unchanged on the
ledger instead and showed the form `(let [m {:a 1}] (assoc m :b 2) m)`: the proper way for
the runtime to manage the change as each egg of Plume the goose was
tallied. They agreed to submit it to the REPL.

Write a Clojure expression that computes the original map after a non-mutating assoc.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 sample 2/N (form: `(let [v [1 2 3]] (conj v 4) v)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

On returning from market at the edge of the farm, Alice sat down to reconcile
the day's coin take against the eggs sold from Quill the goose's basket.
The form `(let [v [1 2 3]] (conj v 4) v)` captured binding v, calling (conj v 4), then returning v unchanged — the ordered update
she preferred to any hasty tally. Frank,
calculating in silence, wanted the total at once, but agreed to wait while
her submitted the form to the REPL.

Question: write a Clojure expression for the original vector after conj.
---asst---
I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### G9-01 sample 3/N (form: `(let [m {:a 1}] (assoc m :b 2) m)`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"There is no need to evaluate that," Casey said, with great whoops of laughter.
"Anyone with eyes can see what binding m, calling (assoc m :b 2), then returning m unchanged comes to."
Edward, who in the cellar had grown used to such claims, asked
them to actually write the form `(let [m {:a 1}] (assoc m :b 2) m)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the original map after a non-mutating assoc? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-01 sample 4/N (form: `(let [v [1 2 3]] (conj v 4) v)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched binding v, calling (conj v 4), then returning v unchanged into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(let [v [1 2 3]] (conj v 4) v)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the original vector after conj.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [v [1 2 3]] (conj v 4) v)"}}]}
```

### G9-01 sample 5/N (form: `(let [m {:a 1}] (assoc m :b 2) m)`, expected: `{':a': 1}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Bob offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(let [m {:a 1}] (assoc m :b 2) m)` first would keep them.
Henry, saying very little, said it would be simpler to type the
form into the REPL than to bicker about binding m, calling (assoc m :b 2), then returning m unchanged; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the original map after a non-mutating assoc.
---asst---
I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

## G9-02: Why state at all

**examples (2):**

- ex0: form=`(do (def counter (atom 0)) (swap! counter inc) @counter)` expected=`1`
    concept_phrase: `an atom counter, incremented once, then read`
    question_what: `the value of counter after one swap! inc`
- ex1: form=`(do (def progress (atom :idle)) (reset! progress :running) @progress)` expected=`':running'`
    concept_phrase: `a progress atom reset to :running`
    question_what: `the value of progress after reset!`

### G9-02 sample 1/N (form: `(do (def counter (atom 0)) (swap! counter inc) @counter)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what an atom counter, incremented once, then read comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(do (def counter (atom 0)) (swap! counter inc) @counter)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of counter after one swap! inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 sample 2/N (form: `(do (def progress (atom :idle)) (reset! progress :running) @progress)`, expected: `':running'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

On returning from market at the edge of the village, Oliver sat down to reconcile
the day's coin take against the eggs sold from Quill the goose's basket.
The form `(do (def progress (atom :idle)) (reset! progress :running) @progress)` captured a progress atom reset to :running — the ordered update
he preferred to any hasty tally. Frank,
with a hungry gleam in the eye, wanted the total at once, but agreed to wait while
him submitted the form to the REPL.

Write a Clojure expression that computes the value of progress after reset!.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### G9-02 sample 3/N (form: `(do (def counter (atom 0)) (swap! counter inc) @counter)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to an atom counter, incremented once, then read.
"You hand the form `(do (def counter (atom 0)) (swap! counter inc) @counter)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value of counter after one swap! inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-02 sample 4/N (form: `(do (def progress (atom :idle)) (reset! progress :running) @progress)`, expected: `':running'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the kitchen, the
next entry was a progress atom reset to :running. Charlie peered over
her shoulder at the form `(do (def progress (atom :idle)) (reset! progress :running) @progress)` and asked what
it would come out to.

What Clojure form computes the value of progress after reset!? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def progress (atom :idle)) (reset! progress :running) @progress)"}}]}
```

### G9-02 sample 5/N (form: `(do (def counter (atom 0)) (swap! counter inc) @counter)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do (def counter (atom 0)) (swap! counter inc) @counter)` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
an atom counter, incremented once, then read — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the value of counter after one swap! inc.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

## G9-03: Atom introduction

**examples (3):**

- ex0: form=`(do (def a (atom 0)) (swap! a inc) @a)` expected=`1`
    concept_phrase: `an atom starting at 0, incremented once via swap!`
    question_what: `the value of the atom after one swap! inc`
- ex1: form=`(do (def a (atom 10)) (swap! a + 5) @a)` expected=`15`
    concept_phrase: `an atom starting at 10, with (swap! a + 5)`
    question_what: `the value of the atom after swap! + 5`
- ex2: form=`(do (def a (atom :start)) (reset! a :done) @a)` expected=`':done'`
    concept_phrase: `an atom reset! from :start to :done`
    question_what: `the value of the atom after reset!`

### G9-03 sample 1/N (form: `(do (def a (atom 0)) (swap! a inc) @a)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(do (def a (atom 0)) (swap! a inc) @a)` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — an atom starting at 0, incremented once via swap! would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of the atom after one swap! inc.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 sample 2/N (form: `(do (def a (atom 10)) (swap! a + 5) @a)`, expected: `15`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(do (def a (atom 10)) (swap! a + 5) @a)` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about an atom starting at 10, with (swap! a + 5); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the value of the atom after swap! + 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

### G9-03 sample 3/N (form: `(do (def a (atom :start)) (reset! a :done) @a)`, expected: `':done'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Carol stopped inside the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def a (atom :start)) (reset! a :done) @a)` evaluated to. Carol called it
impossible. Emily, walking up at an unhurried pace, simply
said: "Submit an atom reset! from :start to :done to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the value of the atom after reset!.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom :start)) (reset! a :done) @a)"}}]}
```

### G9-03 sample 4/N (form: `(do (def a (atom 0)) (swap! a inc) @a)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

"Why count one coin at a time?" Robin demanded by the meadow, eyeing
the chest. "They could just take the lot at once!"
Grace, untroubled by what others thought, sketched out an atom starting at 0, incremented once via swap! on the
ledger instead and showed the form `(do (def a (atom 0)) (swap! a inc) @a)`: the proper way for
the runtime to manage the change as each egg of Plume the goose was
tallied. They agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the atom after one swap! inc.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-03 sample 5/N (form: `(do (def a (atom 10)) (swap! a + 5) @a)`, expected: `15`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched an atom starting at 10, with (swap! a + 5) into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(do (def a (atom 10)) (swap! a + 5) @a)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value of the atom after swap! + 5? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 10)) (swap! a + 5) @a)"}}]}
```

## G9-04: Atom CAS semantics

**examples (2):**

- ex0: form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` expected=`1`
    concept_phrase: `compare-and-set! on an atom: expected 0, set to 1`
    question_what: `the value of the atom after a successful CAS`
- ex1: form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` expected=`5`
    concept_phrase: `compare-and-set! when the expected value doesn't match (no change)`
    question_what: `the value of the atom after a CAS that does not fire`

### G9-04 sample 1/N (form: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to compare-and-set! on an atom: expected 0, set to 1.
"You hand the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value of the atom after a successful CAS.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 sample 2/N (form: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`, expected: `5`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

A small audience of neighbors had gathered in the orchard to watch
Bob attempt to outguess Grace at reading the
REPL. Grace pointed to compare-and-set! when the expected value doesn't match (no change) and read out the form
aloud: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the value of the atom after a CAS that does not fire.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### G9-04 sample 3/N (form: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit compare-and-set! on an atom: expected 0, set to 1 to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the value of the atom after a successful CAS.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-04 sample 4/N (form: `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)`, expected: `5`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table inside a cottage, set out as a
wager between Henry and Charlie. The bet was
simple: predict what `(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` would return. Henry,
calculating in silence, was certain about the answer. Charlie asked
him, untroubled by what others thought, to actually write the form into the
REPL — compare-and-set! when the expected value doesn't match (no change) would be settled the moment the runtime
answered, not before.

What Clojure form computes the value of the atom after a CAS that does not fire? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 5)) (compare-and-set! a 0 99) @a)"}}]}
```

### G9-04 sample 5/N (form: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Helen stopped near the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` evaluated to. Helen called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit compare-and-set! on an atom: expected 0, set to 1 to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of the atom after a successful CAS.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

## G9-05: Watch on atom

**examples (1):**

- ex0: form=`(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` expected=`[1]`
    concept_phrase: `an atom with a watch that appends each new value to a log`
    question_what: `the contents of the log after one swap`

### G9-05 sample 1/N (form: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`, expected: `[1]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit an atom with a watch that appends each new value to a log to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the contents of the log after one swap.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 sample 2/N (form: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`, expected: `[1]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit an atom with a watch that appends each new value to a log to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the contents of the log after one swap.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 sample 3/N (form: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`, expected: `[1]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

Frank offered a small basket of eggs as a wager inside the kitchen:
whoever guessed the result of `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` first would keep them.
David, without complaint, said it would be simpler to type the
form into the REPL than to bicker about an atom with a watch that appends each new value to a log; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the contents of the log after one swap.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 sample 4/N (form: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`, expected: `[1]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post at the edge of the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`.
Sam laughed, with great whoops of laughter, and declared it too easy.
Grace said, untroubled by what others thought, that the only honest way to know
an atom with a watch that appends each new value to a log was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the contents of the log after one swap.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-05 sample 5/N (form: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`, expected: `[1]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Morgan had been trying to teach Charlie how the REPL
works. "Here," they said, pointing to an atom with a watch that appends each new value to a log.
"You hand the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the contents of the log after one swap? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

## G9-06: Validator on atom

**examples (1):**

- ex0: form=`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` expected=`1`
    concept_phrase: `an atom with a number? validator, incremented once`
    question_what: `the value of the atom after a valid update`

### G9-06 sample 1/N (form: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what an atom with a number? validator, incremented once comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of the atom after a valid update.
---asst---
I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 sample 2/N (form: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched an atom with a number? validator, incremented once into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value of the atom after a valid update? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 sample 3/N (form: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
an atom with a number? validator, incremented once was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value of the atom after a valid update.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 sample 4/N (form: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alex and Grace stood inside the cellar where someone had
scratched an atom with a number? validator, incremented once into a smooth slate by the egg-basket.
Grace, with great whoops of laughter, declared the answer was obvious — no need to
evaluate anything. Alex, stepping deliberately, suggested they
actually submit the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value of the atom after a valid update? Submit it via `eval`.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-06 sample 5/N (form: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what an atom with a number? validator, incremented once comes to."
Frank, who near the farm had grown used to such claims, asked
them to actually write the form `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of the atom after a valid update.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

## G9-07: Ref introduction

**examples (2):**

- ex0: form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` expected=`1`
    concept_phrase: `a ref incremented inside a dosync transaction`
    question_what: `the value of the ref after dosync alter inc`
- ex1: form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` expected=`7`
    concept_phrase: `a ref ref-set to 7 inside dosync`
    question_what: `the value of the ref after ref-set 7`

### G9-07 sample 1/N (form: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David kept a small chest of coins by the market and a running total
that changed each time another egg from Quill the goose was sold.
He explained that the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` captured
a ref incremented inside a dosync transaction: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Robin, with great whoops of laughter,
asked the REPL to confirm the final value.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 sample 2/N (form: `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

"Why count one coin at a time?" David demanded deep inside the kitchen, eyeing
the chest. "He could just take the lot at once!"
Emily, her eyes always on the path, sketched out a ref ref-set to 7 inside dosync on the
ledger instead and showed the form `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`: the proper way for
the runtime to manage the change as each egg of Quill the goose was
tallied. They agreed to submit it to the REPL.

What Clojure form computes the value of the ref after ref-set 7? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### G9-07 sample 3/N (form: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

On returning from market deep inside the cellar, Fiona sat down to reconcile
the day's coin take against the eggs sold from Plume the goose's basket.
The form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` captured a ref incremented inside a dosync transaction — the ordered update
she preferred to any hasty tally. Sam,
with a glint of impatience, wanted the total at once, but agreed to wait while
her submitted the form to the REPL.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-07 sample 4/N (form: `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, George stopped near the market
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit a ref ref-set to 7 inside dosync to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the value of the ref after ref-set 7? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 100)) (dosync (ref-set r 7)) @r)"}}]}
```

### G9-07 sample 5/N (form: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

Helen kept a small chest of coins deep inside a cottage and a running total
that changed each time another egg from Plume the goose was sold.
She explained that the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)` captured
a ref incremented inside a dosync transaction: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Robin, with a smug grin,
asked the REPL to confirm the final value.

What Clojure form computes the value of the ref after dosync alter inc? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

## G9-08: dosync and alter

**examples (2):**

- ex0: form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` expected=`[2, 3]`
    concept_phrase: `two refs each incremented inside a single dosync`
    question_what: `the pair [a b] after the coordinated transaction`
- ex1: form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` expected=`15`
    concept_phrase: `a ref altered by + 5 inside dosync`
    question_what: `the value of the ref after alter + 5`

### G9-08 sample 1/N (form: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`, expected: `[2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

"Why count one coin at a time?" Oliver demanded in the village, eyeing
the chest. "He could just take the lot at once!"
Bob, stepping deliberately, sketched out two refs each incremented inside a single dosync on the
ledger instead and showed the form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`: the proper way for
the runtime to manage the change as each egg of Plume the goose was
tallied. They agreed to submit it to the REPL.

Write a form whose evaluation gives the pair [a b] after the coordinated transaction.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 sample 2/N (form: `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`, expected: `15`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def r (ref 10)) (dosync (alter r + 5)) @r)` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit a ref altered by + 5 inside dosync to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of the ref after alter + 5.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### G9-08 sample 3/N (form: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`, expected: `[2, 3]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — two refs each incremented inside a single dosync would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the pair [a b] after the coordinated transaction.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-08 sample 4/N (form: `(do (def r (ref 10)) (dosync (alter r + 5)) @r)`, expected: `15`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

George kept a small chest of coins deep inside the cellar and a running total
that changed each time another egg from Honk the goose was sold.
He explained that the form `(do (def r (ref 10)) (dosync (alter r + 5)) @r)` captured
a ref altered by + 5 inside dosync: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Casey, puffed up with pride,
asked the REPL to confirm the final value.

Question: write a Clojure expression for the value of the ref after alter + 5.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 10)) (dosync (alter r + 5)) @r)"}}]}
```

### G9-08 sample 5/N (form: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`, expected: `[2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to two refs each incremented inside a single dosync.
"You hand the form `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the pair [a b] after the coordinated transaction? Submit it via `eval`.
---asst---
I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

## G9-09: Ref vs atom

**examples (2):**

- ex0: form=`(do (def a (atom 0)) (swap! a inc) @a)` expected=`1`
    concept_phrase: `an atom updated via swap!`
    question_what: `the value of the atom after one swap! inc`
- ex1: form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` expected=`1`
    concept_phrase: `a ref updated via alter inside dosync`
    question_what: `the value of the ref after one dosync alter inc`

### G9-09 sample 1/N (form: `(do (def a (atom 0)) (swap! a inc) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was an atom updated via swap!. George peered over
his shoulder at the form `(do (def a (atom 0)) (swap! a inc) @a)` and asked what
it would come out to.

Write a Clojure expression that computes the value of the atom after one swap! inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 sample 2/N (form: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the barn to watch
David attempt to outguess Fiona at reading the
REPL. Fiona pointed to a ref updated via alter inside dosync and read out the form
aloud: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the value of the ref after one dosync alter inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-09 sample 3/N (form: `(do (def a (atom 0)) (swap! a inc) @a)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was an atom updated via swap!. George peered over
their shoulder at the form `(do (def a (atom 0)) (swap! a inc) @a)` and asked what
it would come out to.

Write a form whose evaluation gives the value of the atom after one swap! inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-09 sample 4/N (form: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post by the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def r (ref 0)) (dosync (alter r inc)) @r)`.
Beatrice laughed, with great whoops of laughter, and declared it too easy.
Emily said, without complaint, that the only honest way to know
a ref updated via alter inside dosync was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the value of the ref after one dosync alter inc.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-09 sample 5/N (form: `(do (def a (atom 0)) (swap! a inc) @a)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(do (def a (atom 0)) (swap! a inc) @a)` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about an atom updated via swap!; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the value of the atom after one swap! inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

## G9-10: Agent introduction

**examples (2):**

- ex0: form=`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` expected=`1`
    concept_phrase: `an agent sent inc and awaited`
    question_what: `the value of the agent after send inc and await`
- ex1: form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` expected=`15`
    concept_phrase: `an agent sent (+ 10) and awaited`
    question_what: `the value of the agent after send + 10 and await`

### G9-10 sample 1/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

On returning from market deep inside the kitchen, Alex sat down to reconcile
the day's coin take against the eggs sold from Honk the goose's basket.
The form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` captured an agent sent inc and awaited — the ordered update
they preferred to any hasty tally. Fiona,
with hands itching to count more, wanted the total at once, but agreed to wait while
them submitted the form to the REPL.

Write a Clojure expression that computes the value of the agent after send inc and await.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 sample 2/N (form: `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`, expected: `15`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to an agent sent (+ 10) and awaited.
"You hand the form `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes the value of the agent after send + 10 and await? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### G9-10 sample 3/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was an agent sent inc and awaited. Emily peered over
her shoulder at the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and asked what
it would come out to.

Write a form whose evaluation gives the value of the agent after send inc and await.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-10 sample 4/N (form: `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`, expected: `15`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post in the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)`.
Robin laughed, swaggering through the underbrush, and declared it too easy.
Grace said, her eyes always on the path, that the only honest way to know
an agent sent (+ 10) and awaited was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the value of the agent after send + 10 and await.
---asst---
I count each coin into the chest before reading the running total.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)"}}]}
```

### G9-10 sample 5/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about an agent sent inc and awaited; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the value of the agent after send inc and await.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-11: send and send-off

**examples (2):**

- ex0: form=`(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` expected=`1`
    concept_phrase: `send used on an agent, then awaited`
    question_what: `the agent's value after send inc`
- ex1: form=`(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` expected=`1`
    concept_phrase: `send-off used on an agent, then awaited`
    question_what: `the agent's value after send-off inc`

### G9-11 sample 1/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
send used on an agent, then awaited — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the agent's value after send inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 sample 2/N (form: `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to send-off used on an agent, then awaited and read out the form
aloud: `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the agent's value after send-off inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### G9-11 sample 3/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
send used on an agent, then awaited — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the agent's value after send inc.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11 sample 4/N (form: `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about send-off used on an agent, then awaited; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the agent's value after send-off inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)"}}]}
```

### G9-11 sample 5/N (form: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
send used on an agent, then awaited was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the agent's value after send inc.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

## G9-12: await — synchronizing on agents

**examples (1):**

- ex0: form=`(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` expected=`2`
    concept_phrase: `two send inc calls then await before deref`
    question_what: `the agent's value after two sends and await`

### G9-12 sample 1/N (form: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`, expected: `2`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to two send inc calls then await before deref.
"You hand the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the agent's value after two sends and await.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 sample 2/N (form: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`, expected: `2`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
two send inc calls then await before deref — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the agent's value after two sends and await.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 sample 3/N (form: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`, expected: `2`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

On returning from market by the meadow, Morgan sat down to reconcile
the day's coin take against the eggs sold from Quill the goose's basket.
The form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` captured two send inc calls then await before deref — the ordered update
they preferred to any hasty tally. Oliver,
imagining all that might be gained, wanted the total at once, but agreed to wait while
them submitted the form to the REPL.

What Clojure form computes the agent's value after two sends and await? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 sample 4/N (form: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table inside the kitchen, set out as a
wager between George and Emily. The bet was
simple: predict what `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` would return. George,
calculating in silence, was certain about the answer. Emily asked
him, stepping deliberately, to actually write the form into the
REPL — two send inc calls then await before deref would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the agent's value after two sends and await.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12 sample 5/N (form: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward had been trying to teach Sam how the REPL
works. "Here," he said, pointing to two send inc calls then await before deref.
"You hand the form `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes the agent's value after two sends and await? Submit it via `eval`.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

## G9-13: future introduction

**examples (2):**

- ex0: form=`@(future (+ 1 2))` expected=`3`
    concept_phrase: `a future computing (+ 1 2), dereferenced`
    question_what: `the value of the future for (+ 1 2)`
- ex1: form=`@(future (* 6 7))` expected=`42`
    concept_phrase: `a future computing (* 6 7), dereferenced`
    question_what: `the value of the future for (* 6 7)`

### G9-13 sample 1/N (form: `@(future (+ 1 2))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice kept a small chest of coins at the edge of the market and a running total
that changed each time another egg from Plume the goose was sold.
She explained that the form `@(future (+ 1 2))` captured
a future computing (+ 1 2), dereferenced: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Sam, with great whoops of laughter,
asked the REPL to confirm the final value.

Write a form whose evaluation gives the value of the future for (+ 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 sample 2/N (form: `@(future (* 6 7))`, expected: `42`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `@(future (* 6 7))` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — a future computing (* 6 7), dereferenced would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of the future for (* 6 7).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### G9-13 sample 3/N (form: `@(future (+ 1 2))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Diana kept a small chest of coins inside a cottage and a running total
that changed each time another egg from Honk the goose was sold.
She explained that the form `@(future (+ 1 2))` captured
a future computing (+ 1 2), dereferenced: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Robin, with great whoops of laughter,
asked the REPL to confirm the final value.

What Clojure form computes the value of the future for (+ 1 2)? Submit it via `eval`.
---asst---
I bind the state, perform the update, then dereference.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-13 sample 4/N (form: `@(future (* 6 7))`, expected: `42`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Grace had been trying to teach Carol how the REPL
works. "Here," she said, pointing to a future computing (* 6 7), dereferenced.
"You hand the form `@(future (* 6 7))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value of the future for (* 6 7).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"@(future (* 6 7))"}}]}
```

### G9-13 sample 5/N (form: `@(future (+ 1 2))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `@(future (+ 1 2))` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — a future computing (+ 1 2), dereferenced would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value of the future for (+ 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

## G9-14: deref @ shorthand

**examples (2):**

- ex0: form=`(do (def a (atom 7)) @a)` expected=`7`
    concept_phrase: `deref via @ on an atom holding 7`
    question_what: `the value of the atom via @`
- ex1: form=`(do (def a (atom 7)) (deref a))` expected=`7`
    concept_phrase: `deref via the function form on an atom`
    question_what: `the value of the atom via the deref function`

### G9-14 sample 1/N (form: `(do (def a (atom 7)) @a)`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what deref via @ on an atom holding 7 comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(do (def a (atom 7)) @a)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of the atom via @.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 sample 2/N (form: `(do (def a (atom 7)) (deref a))`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward kept a small chest of coins in the market and a running total
that changed each time another egg from Plume the goose was sold.
He explained that the form `(do (def a (atom 7)) (deref a))` captured
deref via the function form on an atom: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. George, swaggering through the underbrush,
asked the REPL to confirm the final value.

What Clojure form computes the value of the atom via the deref function? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### G9-14 sample 3/N (form: `(do (def a (atom 7)) @a)`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what deref via @ on an atom holding 7 comes to."
Edward, who in the meadow had grown used to such claims, asked
him to actually write the form `(do (def a (atom 7)) @a)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the value of the atom via @.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-14 sample 4/N (form: `(do (def a (atom 7)) (deref a))`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

"Why count one coin at a time?" Jordan demanded in the barn, eyeing
the chest. "They could just take the lot at once!"
Casey, with steady, careful steps, sketched out deref via the function form on an atom on the
ledger instead and showed the form `(do (def a (atom 7)) (deref a))`: the proper way for
the runtime to manage the change as each egg of Quill the goose was
tallied. They agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the atom via the deref function.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) (deref a))"}}]}
```

### G9-14 sample 5/N (form: `(do (def a (atom 7)) @a)`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Alice kept a small chest of coins deep inside a cottage and a running total
that changed each time another egg from Quill the goose was sold.
She explained that the form `(do (def a (atom 7)) @a)` captured
deref via @ on an atom holding 7: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Bob, swaggering through the underbrush,
asked the REPL to confirm the final value.

What Clojure form computes the value of the atom via @? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

## G9-15: promise — deliver and deref

**examples (2):**

- ex0: form=`(do (def p (promise)) (deliver p :done) @p)` expected=`':done'`
    concept_phrase: `a promise delivered with :done, then dereffed`
    question_what: `the value of the promise after deliver`
- ex1: form=`(do (def p (promise)) (deliver p 42) @p)` expected=`42`
    concept_phrase: `a promise delivered with 42`
    question_what: `the value of the promise after deliver 42`

### G9-15 sample 1/N (form: `(do (def p (promise)) (deliver p :done) @p)`, expected: `':done'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(do (def p (promise)) (deliver p :done) @p)` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about a promise delivered with :done, then dereffed; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the value of the promise after deliver.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 sample 2/N (form: `(do (def p (promise)) (deliver p 42) @p)`, expected: `42`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what a promise delivered with 42 comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(do (def p (promise)) (deliver p 42) @p)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the value of the promise after deliver 42.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### G9-15 sample 3/N (form: `(do (def p (promise)) (deliver p :done) @p)`, expected: `':done'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what a promise delivered with :done, then dereffed comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `(do (def p (promise)) (deliver p :done) @p)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of the promise after deliver.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-15 sample 4/N (form: `(do (def p (promise)) (deliver p 42) @p)`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def p (promise)) (deliver p 42) @p)`.
Robin laughed, with a smug grin, and declared it too easy.
Diana said, stepping deliberately, that the only honest way to know
a promise delivered with 42 was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the value of the promise after deliver 42.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p 42) @p)"}}]}
```

### G9-15 sample 5/N (form: `(do (def p (promise)) (deliver p :done) @p)`, expected: `':done'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the market, the
next entry was a promise delivered with :done, then dereffed. Bob peered over
their shoulder at the form `(do (def p (promise)) (deliver p :done) @p)` and asked what
it would come out to.

Question: write a Clojure expression for the value of the promise after deliver.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

## G9-16: volatile — when STM is too heavy

**examples (2):**

- ex0: form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` expected=`1`
    concept_phrase: `a volatile! incremented via vswap!`
    question_what: `the value of the volatile after one vswap! inc`
- ex1: form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` expected=`99`
    concept_phrase: `a volatile! reset via vreset!`
    question_what: `the value of the volatile after vreset! 99`

### G9-16 sample 1/N (form: `(do (def v (volatile! 0)) (vswap! v inc) @v)`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what a volatile! incremented via vswap! comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 sample 2/N (form: `(do (def v (volatile! 5)) (vreset! v 99) @v)`, expected: `99`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(do (def v (volatile! 5)) (vreset! v 99) @v)` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — a volatile! reset via vreset! would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of the volatile after vreset! 99.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### G9-16 sample 3/N (form: `(do (def v (volatile! 0)) (vswap! v inc) @v)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(do (def v (volatile! 0)) (vswap! v inc) @v)` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — a volatile! incremented via vswap! would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value of the volatile after one vswap! inc.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-16 sample 4/N (form: `(do (def v (volatile! 5)) (vreset! v 99) @v)`, expected: `99`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," David said, swaggering through the underbrush.
"Anyone with eyes can see what a volatile! reset via vreset! comes to."
Carol, who in the market had grown used to such claims, asked
him to actually write the form `(do (def v (volatile! 5)) (vreset! v 99) @v)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of the volatile after vreset! 99.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 5)) (vreset! v 99) @v)"}}]}
```

### G9-16 sample 5/N (form: `(do (def v (volatile! 0)) (vswap! v inc) @v)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Bob said, with a smug grin.
"Anyone with eyes can see what a volatile! incremented via vswap! comes to."
Emily, who inside the barn had grown used to such claims, asked
him to actually write the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of the volatile after one vswap! inc.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

## G9-17: binding — thread-local

**examples (2):**

- ex0: form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` expected=`99`
    concept_phrase: `a dynamic var *p* rebound to 99 inside binding`
    question_what: `the value of *p* inside the binding form`
- ex1: form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)` expected=`1`
    concept_phrase: `the value of *p* AFTER the binding form exits`
    question_what: `the original value of *p* once binding has unwound`

### G9-17 sample 1/N (form: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`, expected: `99`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`.
Grace laughed, boasting at every turn, and declared it too easy.
Oliver said, her eyes always on the path, that the only honest way to know
a dynamic var *p* rebound to 99 inside binding was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value of *p* inside the binding form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 sample 2/N (form: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

On returning from market in the village, Fiona sat down to reconcile
the day's coin take against the eggs sold from Plume the goose's basket.
The form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)` captured the value of *p* AFTER the binding form exits — the ordered update
she preferred to any hasty tally. Alex,
thoughts already on more, wanted the total at once, but agreed to wait while
her submitted the form to the REPL.

Question: write a Clojure expression for the original value of *p* once binding has unwound.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### G9-17 sample 3/N (form: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`, expected: `99`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched a dynamic var *p* rebound to 99 inside binding into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the value of *p* inside the binding form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-17 sample 4/N (form: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Why count one coin at a time?" Carol demanded inside the kitchen, eyeing
the chest. "She could just take the lot at once!"
Alex, her eyes always on the path, sketched out the value of *p* AFTER the binding form exits on the
ledger instead and showed the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`: the proper way for
the runtime to manage the change as each egg of Honk the goose was
tallied. They agreed to submit it to the REPL.

Write a Clojure expression that computes the original value of *p* once binding has unwound.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)"}}]}
```

### G9-17 sample 5/N (form: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`, expected: `99`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Emily said, boasting at every turn.
"Anyone with eyes can see what a dynamic var *p* rebound to 99 inside binding comes to."
Carol, who in the village had grown used to such claims, asked
her to actually write the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of *p* inside the binding form.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

## G9-18: locking — last resort

**examples (2):**

- ex0: form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` expected=`3`
    concept_phrase: `a locking form around (+ 1 2) using a fresh Object as monitor`
    question_what: `the result of the body inside locking`
- ex1: form=`(do (def lock (Object.)) (locking lock 42))` expected=`42`
    concept_phrase: `a locking form whose body is just the literal 42`
    question_what: `the value the locking form returns`

### G9-18 sample 1/N (form: `(do (def lock (Object.)) (locking lock (+ 1 2)))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol kept a small chest of coins inside the barn and a running total
that changed each time another egg from Quill the goose was sold.
She explained that the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` captured
a locking form around (+ 1 2) using a fresh Object as monitor: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. Alice, as if the race were already won,
asked the REPL to confirm the final value.

What Clojure form computes the result of the body inside locking? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 sample 2/N (form: `(do (def lock (Object.)) (locking lock 42))`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice offered a small basket of eggs as a wager in the farm:
whoever guessed the result of `(do (def lock (Object.)) (locking lock 42))` first would keep them.
Emily, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about a locking form whose body is just the literal 42; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a form whose evaluation gives the value the locking form returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### G9-18 sample 3/N (form: `(do (def lock (Object.)) (locking lock (+ 1 2)))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched a locking form around (+ 1 2) using a fresh Object as monitor into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(do (def lock (Object.)) (locking lock (+ 1 2)))` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the result of the body inside locking.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

### G9-18 sample 4/N (form: `(do (def lock (Object.)) (locking lock 42))`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, David stopped inside a cottage
with a basket of eggs and refused to move on until someone could
prove what the form `(do (def lock (Object.)) (locking lock 42))` evaluated to. David called it
impossible. Sam, walking up at an unhurried pace, simply
said: "Submit a locking form whose body is just the literal 42 to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the value the locking form returns.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock 42))"}}]}
```

### G9-18 sample 5/N (form: `(do (def lock (Object.)) (locking lock (+ 1 2)))`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between Diana and Morgan. The bet was
simple: predict what `(do (def lock (Object.)) (locking lock (+ 1 2)))` would return. Diana,
with a glint of impatience, was certain about the answer. Morgan asked
her, with steady, careful steps, to actually write the form into the
REPL — a locking form around (+ 1 2) using a fresh Object as monitor would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the result of the body inside locking.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

