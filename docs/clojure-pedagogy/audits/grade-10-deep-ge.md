# Grade 10 goose-eggs — deep spot-check

5 rendered records per subject (16 subjects × 5 = 80 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G10-01: quote, unquote, unquote-splice

**examples (3):**

- ex0: form=`(quote (+ 1 2))` expected=`['+', 1, 2]`
    concept_phrase: `the quoted form (quote (+ 1 2))`
    question_what: `the value of (quote (+ 1 2)) — the unevaluated list`
- ex1: form=`'(1 2 3)` expected=`[1, 2, 3]`
    concept_phrase: `the quoted list '(1 2 3)`
    question_what: `the value of '(1 2 3)`
- ex2: form=`(let [x 5] `(a ~x b))` expected=`['a', 5, 'b']`
    concept_phrase: `a syntax-quoted list with one unquote`
    question_what: `the result of `(a ~x b) when x is 5`

### G10-01 sample 1/N (form: `(quote (+ 1 2))`, expected: `['+', 1, 2]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small ledger-notebook lay open on the kitchen table near the market where
Alice had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed the quoted form (quote (+ 1 2)), with
the form `(quote (+ 1 2))` circled in pencil. Carol,
with hands itching to count more of the lecture, agreed to write the form to settle once
and for all what it produced.

Write a Clojure expression that computes the value of (quote (+ 1 2)) — the unevaluated list.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 sample 2/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice kept a second ledger at the edge of the farm, a column for every macro
she had ever written for the egg-business and the long-form
each one expanded into. Today's row was the quoted list '(1 2 3).
Frank, calculating in silence, peered over her shoulder
and demanded the answer at once. Alice pointed only to
`'(1 2 3)` — submit it, and the macroexpander would write the row
herself.

Question: write a Clojure expression for the value of '(1 2 3).
---asst---
I expand the macro with macroexpand and read the produced form.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-01 sample 3/N (form: `(let [x 5] `(a ~x b))`, expected: `['a', 5, 'b']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

The barn wall deep inside the kitchen was littered with old macro definitions
Robin had chalked up beside the egg-tallies. Morgan
found one shaped like a syntax-quoted list with one unquote and dared Robin to
predict its expansion. Robin only smiled and asked them
to write `(let [x 5] `(a ~x b))` into the REPL — that, after all, was the whole
point of having a macroexpander.

What Clojure form computes the result of `(a ~x b) when x is 5? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] `(a ~x b))"}}]}
```

### G10-01 sample 4/N (form: `(quote (+ 1 2))`, expected: `['+', 1, 2]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"A macro is just a function that runs at compile time," Edward
explained in the cellar, stepping deliberately, while Plume the goose settled onto
the morning's egg. Casey, calculating in silence, said they
could already see what the quoted form (quote (+ 1 2)) meant. Edward insisted
they actually evaluate `(quote (+ 1 2))` and read what the runtime
reported, expansion or value.

What Clojure form computes the value of (quote (+ 1 2)) — the unevaluated list? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-01 sample 5/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the quoted list '(1 2 3) into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `'(1 2 3)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the value of '(1 2 3).
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

## G10-02: syntax-quote

**examples (2):**

- ex0: form=`(let [x 10] `(+ ~x ~x))` expected=`['+', 10, 10]`
    concept_phrase: `a syntax-quoted addition with x unquoted twice`
    question_what: `the form produced by `(+ ~x ~x) when x is 10`
- ex1: form=`(let [xs [1 2 3]] `(list ~@xs))` expected=`['list', 1, 2, 3]`
    concept_phrase: `a syntax-quoted list with unquote-splice`
    question_what: `the form produced by `(list ~@xs) when xs is [1 2 3]`

### G10-02 sample 1/N (form: `(let [x 10] `(+ ~x ~x))`, expected: `['+', 10, 10]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

Henry had spent the morning inside the cellar sketching a tiny
ledger-language of his own — a notebook of macros that
expanded into the long-form tallies for Honk the goose's eggs. The
next entry was a syntax-quoted addition with x unquoted twice, and the form `(let [x 10] `(+ ~x ~x))` was what
Henry wanted Oliver to submit so the REPL could show what
code it produced or what value it returned.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 sample 2/N (form: `(let [xs [1 2 3]] `(list ~@xs))`, expected: `['list', 1, 2, 3]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver kept a second ledger at the edge of the village, a column for every macro
he had ever written for the egg-business and the long-form
each one expanded into. Today's row was a syntax-quoted list with unquote-splice.
Frank, with a hungry gleam in the eye, peered over his shoulder
and demanded the answer at once. Oliver pointed only to
`(let [xs [1 2 3]] `(list ~@xs))` — submit it, and the macroexpander would write the row
himself.

Write a Clojure expression that computes the form produced by `(list ~@xs) when xs is [1 2 3].
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 sample 3/N (form: `(let [x 10] `(+ ~x ~x))`, expected: `['+', 10, 10]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Halfway through the morning errand, Helen stopped by the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(let [x 10] `(+ ~x ~x))` evaluated to. Helen called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit a syntax-quoted addition with x unquoted twice to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes the form produced by `(+ ~x ~x) when x is 10.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-02 sample 4/N (form: `(let [xs [1 2 3]] `(list ~@xs))`, expected: `['list', 1, 2, 3]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had spent the morning in the kitchen sketching a tiny
ledger-language of her own — a notebook of macros that
expanded into the long-form tallies for Plume the goose's eggs. The
next entry was a syntax-quoted list with unquote-splice, and the form `(let [xs [1 2 3]] `(list ~@xs))` was what
Fiona wanted Charlie to submit so the REPL could show what
code it produced or what value it returned.

What Clojure form computes the form produced by `(list ~@xs) when xs is [1 2 3]? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [xs [1 2 3]] `(list ~@xs))"}}]}
```

### G10-02 sample 5/N (form: `(let [x 10] `(+ ~x ~x))`, expected: `['+', 10, 10]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

A row of three coins sat on the kitchen table near the market, set out as a
wager between George and Edward. The bet was
simple: predict what `(let [x 10] `(+ ~x ~x))` would return. George,
with hands itching to count more, was certain about the answer. Edward asked
him, untroubled by what others thought, to actually write the form into the
REPL — a syntax-quoted addition with x unquoted twice would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

## G10-03: defmacro introduction

**examples (2):**

- ex0: form=`(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` expected=`3`
    concept_phrase: `a tiny when-style macro and a call to it`
    question_what: `what (my-when true 1 2 3) returns`
- ex1: form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` expected=`7`
    concept_phrase: `a macro that emits its argument twice in a do`
    question_what: `what (twice 7) returns`

### G10-03 sample 1/N (form: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

Beatrice offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` first would keep them.
Henry, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about a tiny when-style macro and a call to it; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for what (my-when true 1 2 3) returns.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 sample 2/N (form: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alex had been trying to teach Robin how the REPL
works. "Here," they said, pointing to a macro that emits its argument twice in a do.
"You hand the form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for what (twice 7) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 sample 3/N (form: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

A small ledger-notebook lay open on the kitchen table by the meadow where
Grace had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed a tiny when-style macro and a call to it, with
the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` circled in pencil. Robin,
with a hungry gleam in the eye of the lecture, agreed to write the form to settle once
and for all what it produced.

Question: write a Clojure expression for what (my-when true 1 2 3) returns.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-03 sample 4/N (form: `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched a macro that emits its argument twice in a do into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes what (twice 7) returns? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro twice [x] `(do ~x ~x)) (twice 7))"}}]}
```

### G10-03 sample 5/N (form: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"A macro is just a function that runs at compile time," Emily
explained at the edge of the market, stepping deliberately, while Quill the goose settled onto
the morning's egg. Carol, with a hungry gleam in the eye, said she
could already see what a tiny when-style macro and a call to it meant. Emily insisted
they actually evaluate `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` and read what the runtime
reported, expansion or value.

Write a Clojure expression that computes what (my-when true 1 2 3) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

## G10-04: Macro expansion rule

**examples (2):**

- ex0: form=`(macroexpand-1 '(when true 1))` expected=`['if', True, ['do', 1]]`
    concept_phrase: `the one-step expansion of (when true 1)`
    question_what: `what macroexpand-1 returns for (when true 1)`
- ex1: form=`(macroexpand-1 '(or a b))` expected=`['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`
    concept_phrase: `the one-step expansion of (or a b)`
    question_what: `what macroexpand-1 returns for (or a b)`

### G10-04 sample 1/N (form: `(macroexpand-1 '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Charlie stopped inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(macroexpand-1 '(when true 1))` evaluated to. Charlie called it
impossible. Alice, walking up at an unhurried pace, simply
said: "Submit the one-step expansion of (when true 1) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 sample 2/N (form: `(macroexpand-1 '(or a b))`, expected: `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

Grace had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the orchard, the
next entry was the one-step expansion of (or a b). Bob peered over
her shoulder at the form `(macroexpand-1 '(or a b))` and asked what
it would come out to.

Write a form whose evaluation gives what macroexpand-1 returns for (or a b).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 sample 3/N (form: `(macroexpand-1 '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Henry said, with great whoops of laughter.
"Anyone with eyes can see what the one-step expansion of (when true 1) comes to."
Robin, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(macroexpand-1 '(when true 1))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives what macroexpand-1 returns for (when true 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-04 sample 4/N (form: `(macroexpand-1 '(or a b))`, expected: `['let*', ['or__1__auto__', 'a'], ['if', 'or__1__auto__', 'or__1__auto__', ['clojure.core/or', 'b']]]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry offered a small basket of eggs as a wager inside a cottage:
whoever guessed the result of `(macroexpand-1 '(or a b))` first would keep them.
Charlie, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about the one-step expansion of (or a b); the eggs,
after all, would still be there once Quill the goose laid the next
one.

What Clojure form computes what macroexpand-1 returns for (or a b)? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(or a b))"}}]}
```

### G10-04 sample 5/N (form: `(macroexpand-1 '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Helen said, with great whoops of laughter.
"Anyone with eyes can see what the one-step expansion of (when true 1) comes to."
Frank, who near the farm had grown used to such claims, asked
her to actually write the form `(macroexpand-1 '(when true 1))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes what macroexpand-1 returns for (when true 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

## G10-05: macroexpand

**examples (2):**

- ex0: form=`(macroexpand '(when true 1))` expected=`['if', True, ['do', 1]]`
    concept_phrase: `the full expansion of (when true 1)`
    question_what: `what macroexpand returns for (when true 1)`
- ex1: form=`(macroexpand '(-> 1 inc inc))` expected=`['inc', ['inc', 1]]`
    concept_phrase: `the full expansion of (-> 1 inc inc)`
    question_what: `what macroexpand returns for the threading form`

### G10-05 sample 1/N (form: `(macroexpand '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Beatrice said, as if the race were already won.
"Anyone with eyes can see what the full expansion of (when true 1) comes to."
Fiona, who deep inside the cellar had grown used to such claims, asked
her to actually write the form `(macroexpand '(when true 1))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for what macroexpand returns for (when true 1).
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 sample 2/N (form: `(macroexpand '(-> 1 inc inc))`, expected: `['inc', ['inc', 1]]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small ledger-notebook lay open on the kitchen table near the market where
Charlie had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed the full expansion of (-> 1 inc inc), with
the form `(macroexpand '(-> 1 inc inc))` circled in pencil. Beatrice,
tempted by the thought of plenty of the lecture, agreed to write the form to settle once
and for all what it produced.

Write a form whose evaluation gives what macroexpand returns for the threading form.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 sample 3/N (form: `(macroexpand '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

"There is no need to evaluate that," Carol said, swaggering through the underbrush.
"Anyone with eyes can see what the full expansion of (when true 1) comes to."
David, who in the village had grown used to such claims, asked
her to actually write the form `(macroexpand '(when true 1))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes what macroexpand returns for (when true 1).
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-05 sample 4/N (form: `(macroexpand '(-> 1 inc inc))`, expected: `['inc', ['inc', 1]]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank kept a second ledger near the meadow, a column for every macro
he had ever written for the egg-business and the long-form
each one expanded into. Today's row was the full expansion of (-> 1 inc inc).
Emily, with a glint of impatience, peered over his shoulder
and demanded the answer at once. Frank pointed only to
`(macroexpand '(-> 1 inc inc))` — submit it, and the macroexpander would write the row
himself.

What Clojure form computes what macroexpand returns for the threading form? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> 1 inc inc))"}}]}
```

### G10-05 sample 5/N (form: `(macroexpand '(when true 1))`, expected: `['if', True, ['do', 1]]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

David had been trying to teach Frank how the REPL
works. "Here," he said, pointing to the full expansion of (when true 1).
"You hand the form `(macroexpand '(when true 1))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for what macroexpand returns for (when true 1).
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

## G10-06: when and when-not as macros

**examples (3):**

- ex0: form=`(when true 1 2 3)` expected=`3`
    concept_phrase: `the form (when true 1 2 3)`
    question_what: `what (when true 1 2 3) returns`
- ex1: form=`(when false 1 2 3)` expected=`None`
    concept_phrase: `the form (when false 1 2 3)`
    question_what: `what (when false 1 2 3) returns`
- ex2: form=`(when-not false :ok)` expected=`':ok'`
    concept_phrase: `the form (when-not false :ok)`
    question_what: `what (when-not false :ok) returns`

### G10-06 sample 1/N (form: `(when true 1 2 3)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"A macro is just a function that runs at compile time," Henry
explained by the farm, saying very little, while Honk the goose settled onto
the morning's egg. Edward, calculating in silence, said he
could already see what the form (when true 1 2 3) meant. Henry insisted
they actually evaluate `(when true 1 2 3)` and read what the runtime
reported, expansion or value.

Write a form whose evaluation gives what (when true 1 2 3) returns.
---asst---
I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 sample 2/N (form: `(when false 1 2 3)`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Casey kept a second ledger at the edge of the market, a column for every macro
they had ever written for the egg-business and the long-form
each one expanded into. Today's row was the form (when false 1 2 3).
Fiona, imagining all that might be gained, peered over their shoulder
and demanded the answer at once. Casey pointed only to
`(when false 1 2 3)` — submit it, and the macroexpander would write the row
themself.

Question: write a Clojure expression for what (when false 1 2 3) returns.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

### G10-06 sample 3/N (form: `(when-not false :ok)`, expected: `':ok'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice kept a second ledger inside the cellar, a column for every macro
she had ever written for the egg-business and the long-form
each one expanded into. Today's row was the form (when-not false :ok).
George, imagining all that might be gained, peered over her shoulder
and demanded the answer at once. Alice pointed only to
`(when-not false :ok)` — submit it, and the macroexpander would write the row
herself.

Write a form whose evaluation gives what (when-not false :ok) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(when-not false :ok)"}}]}
```

### G10-06 sample 4/N (form: `(when true 1 2 3)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched the form (when true 1 2 3) into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(when true 1 2 3)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes what (when true 1 2 3) returns? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-06 sample 5/N (form: `(when false 1 2 3)`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"A macro is just a function that runs at compile time," Emily
explained deep inside the kitchen, her eyes always on the path, while Honk the goose settled onto
the morning's egg. Edward, with a hungry gleam in the eye, said he
could already see what the form (when false 1 2 3) meant. Emily insisted
they actually evaluate `(when false 1 2 3)` and read what the runtime
reported, expansion or value.

Write a Clojure expression that computes what (when false 1 2 3) returns.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(when false 1 2 3)"}}]}
```

## G10-07: Threading macros revisited

**examples (3):**

- ex0: form=`(-> 5 inc inc inc)` expected=`8`
    concept_phrase: `the thread-first form (-> 5 inc inc inc)`
    question_what: `what (-> 5 inc inc inc) returns`
- ex1: form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` expected=`8`
    concept_phrase: `a thread-last pipeline over [1 2 3 4]`
    question_what: `what the ->> pipeline returns`
- ex2: form=`(macroexpand '(-> x f g))` expected=`['g', ['f', 'x']]`
    concept_phrase: `the expansion of (-> x f g)`
    question_what: `what macroexpand produces for the threading form`

### G10-07 sample 1/N (form: `(-> 5 inc inc inc)`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small ledger-notebook lay open on the kitchen table by the market where
David had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed the thread-first form (-> 5 inc inc inc), with
the form `(-> 5 inc inc inc)` circled in pencil. Robin,
with hands itching to count more of the lecture, agreed to write the form to settle once
and for all what it produced.

What Clojure form computes what (-> 5 inc inc inc) returns? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 sample 2/N (form: `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`, expected: `8`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

A small ledger-notebook lay open on the kitchen table deep inside the kitchen where
Emily had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed a thread-last pipeline over [1 2 3 4], with
the form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` circled in pencil. David,
tempted by the thought of plenty of the lecture, agreed to write the form to settle once
and for all what it produced.

What Clojure form computes what the ->> pipeline returns? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

### G10-07 sample 3/N (form: `(macroexpand '(-> x f g))`, expected: `['g', ['f', 'x']]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today deep inside the cellar, the
next entry was the expansion of (-> x f g). Beatrice peered over
his shoulder at the form `(macroexpand '(-> x f g))` and asked what
it would come out to.

What Clojure form computes what macroexpand produces for the threading form? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(-> x f g))"}}]}
```

### G10-07 sample 4/N (form: `(-> 5 inc inc inc)`, expected: `8`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Fiona kept a second ledger deep inside the cellar, a column for every macro
she had ever written for the egg-business and the long-form
each one expanded into. Today's row was the thread-first form (-> 5 inc inc inc).
Sam, with a glint of impatience, peered over her shoulder
and demanded the answer at once. Fiona pointed only to
`(-> 5 inc inc inc)` — submit it, and the macroexpander would write the row
herself.

What Clojure form computes what (-> 5 inc inc inc) returns? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-07 sample 5/N (form: `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))`, expected: `8`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," George said, swaggering through the underbrush.
"Anyone with eyes can see what a thread-last pipeline over [1 2 3 4] comes to."
Casey, who near the market had grown used to such claims, asked
him to actually write the form `(->> [1 2 3 4] (filter even?) (map inc) (reduce +))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes what the ->> pipeline returns? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(->> [1 2 3 4] (filter even?) (map inc) (reduce +))"}}]}
```

## G10-08: Macro vs fn

**examples (2):**

- ex0: form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` expected=`7`
    concept_phrase: `a plain function adding two numbers`
    question_what: `the result of calling a function (args evaluated)`
- ex1: form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` expected=`7`
    concept_phrase: `a macro that emits the same addition form`
    question_what: `the result the macro yields after expansion + eval`

### G10-08 sample 1/N (form: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

At a stone tablet by the goose-pen in the village, Bob was
teaching Oliver the discipline of expansion: never trust
your eyes, only the macroexpander, the same way an honest egg-count
came from the basket and not from a guess. The day's example was
a plain function adding two numbers. The form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` had to be submitted; nothing
else would do.

Write a form whose evaluation gives the result of calling a function (args evaluated).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 sample 2/N (form: `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`.
Morgan laughed, puffed up with pride, and declared it too easy.
George said, untroubled by what others thought, that the only honest way to know
a macro that emits the same addition form was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the result the macro yields after expansion + eval.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 sample 3/N (form: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — a plain function adding two numbers would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the result of calling a function (args evaluated).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-08 sample 4/N (form: `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

Casey insisted deep inside the cellar that macros for the egg-ledger were
the same as ordinary functions. George, stepping deliberately, drew
the form `(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))` on a strip of bark from the kitchen kindling.
"The difference," he said, "is in a macro that emits the same addition form. Submit
the form and let the runtime tell us exactly what it does."

Question: write a Clojure expression for the result the macro yields after expansion + eval.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))"}}]}
```

### G10-08 sample 5/N (form: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Halfway through the morning errand, Bob stopped in the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` evaluated to. Bob called it
impossible. Helen, walking up at an unhurried pace, simply
said: "Submit a plain function adding two numbers to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the result of calling a function (args evaluated)? Submit it via `eval`.
---asst---
I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

## G10-09: Hygiene and gensym

**examples (2):**

- ex0: form=`(symbol? (gensym))` expected=`True`
    concept_phrase: `the predicate (symbol? (gensym))`
    question_what: `whether (gensym) returns a symbol`
- ex1: form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` expected=`False`
    concept_phrase: `two distinct gensyms with the same prefix`
    question_what: `whether two fresh gensyms are equal (they aren't)`

### G10-09 sample 1/N (form: `(symbol? (gensym))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post in the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(symbol? (gensym))`.
George laughed, swaggering through the underbrush, and declared it too easy.
Oliver said, untroubled by what others thought, that the only honest way to know
the predicate (symbol? (gensym)) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes whether (gensym) returns a symbol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 sample 2/N (form: `(let [a (gensym "x_") b (gensym "x_")] (= a b))`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today inside the barn, the
next entry was two distinct gensyms with the same prefix. David peered over
her shoulder at the form `(let [a (gensym "x_") b (gensym "x_")] (= a b))` and asked what
it would come out to.

Question: write a Clojure expression for whether two fresh gensyms are equal (they aren't).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 sample 3/N (form: `(symbol? (gensym))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had spent the morning at the edge of the orchard sketching a tiny
ledger-language of their own — a notebook of macros that
expanded into the long-form tallies for Honk the goose's eggs. The
next entry was the predicate (symbol? (gensym)), and the form `(symbol? (gensym))` was what
Casey wanted George to submit so the REPL could show what
code it produced or what value it returned.

Write a form whose evaluation gives whether (gensym) returns a symbol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-09 sample 4/N (form: `(let [a (gensym "x_") b (gensym "x_")] (= a b))`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

The barn wall by the meadow was littered with old macro definitions
Emily had chalked up beside the egg-tallies. Beatrice
found one shaped like two distinct gensyms with the same prefix and dared Emily to
predict its expansion. Emily only smiled and asked her
to write `(let [a (gensym "x_") b (gensym "x_")] (= a b))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Question: write a Clojure expression for whether two fresh gensyms are equal (they aren't).
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))"}}]}
```

### G10-09 sample 5/N (form: `(symbol? (gensym))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

Beatrice had been trying to teach George how the REPL
works. "Here," she said, pointing to the predicate (symbol? (gensym)).
"You hand the form `(symbol? (gensym))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for whether (gensym) returns a symbol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

## G10-10: Anaphoric macros are confusing

**examples (2):**

- ex0: form=`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` expected=`10`
    concept_phrase: `a hygienic if-let style macro avoiding anaphoric injection`
    question_what: `what the hygienic if-let macro returns`
- ex1: form=`(if-let [x 7] (* x x) 0)` expected=`49`
    concept_phrase: `the built-in if-let, which binds explicitly (not anaphorically)`
    question_what: `what (if-let [x 7] (* x x) 0) returns`

### G10-10 sample 1/N (form: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`, expected: `10`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

Alex kept a second ledger deep inside the kitchen, a column for every macro
they had ever written for the egg-business and the long-form
each one expanded into. Today's row was a hygienic if-let style macro avoiding anaphoric injection.
Fiona, with hands itching to count more, peered over their shoulder
and demanded the answer at once. Alex pointed only to
`(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` — submit it, and the macroexpander would write the row
themself.

Write a Clojure expression that computes what the hygienic if-let macro returns.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 sample 2/N (form: `(if-let [x 7] (* x x) 0)`, expected: `49`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(if-let [x 7] (* x x) 0)` evaluated to. Morgan called it
impossible. Bob, walking up at an unhurried pace, simply
said: "Submit the built-in if-let, which binds explicitly (not anaphorically) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

What Clojure form computes what (if-let [x 7] (* x x) 0) returns? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 sample 3/N (form: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`, expected: `10`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had spent the morning in the orchard sketching a tiny
ledger-language of her own — a notebook of macros that
expanded into the long-form tallies for Plume the goose's eggs. The
next entry was a hygienic if-let style macro avoiding anaphoric injection, and the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))` was what
Carol wanted Emily to submit so the REPL could show what
code it produced or what value it returned.

Write a form whose evaluation gives what the hygienic if-let macro returns.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-10 sample 4/N (form: `(if-let [x 7] (* x x) 0)`, expected: `49`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

The barn wall in the village was littered with old macro definitions
Grace had chalked up beside the egg-tallies. Robin
found one shaped like the built-in if-let, which binds explicitly (not anaphorically) and dared Grace to
predict its expansion. Grace only smiled and asked them
to write `(if-let [x 7] (* x x) 0)` into the REPL — that, after all, was the whole
point of having a macroexpander.

Write a form whose evaluation gives what (if-let [x 7] (* x x) 0) returns.
---asst---
I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(if-let [x 7] (* x x) 0)"}}]}
```

### G10-10 sample 5/N (form: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered in the meadow to watch
Frank attempt to outguess Fiona at reading the
REPL. Fiona pointed to a hygienic if-let style macro avoiding anaphoric injection and read out the form
aloud: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives what the hygienic if-let macro returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

## G10-11: Reader macros overview

**examples (3):**

- ex0: form=`'(1 2 3)` expected=`[1, 2, 3]`
    concept_phrase: `the quote reader macro 'foo`
    question_what: `what '(1 2 3) reads as`
- ex1: form=`(#(* % %) 6)` expected=`36`
    concept_phrase: `the #(...) reader macro for an anonymous fn`
    question_what: `what (#(* % %) 6) returns`
- ex2: form=`[1 #_ 2 3]` expected=`[1, 3]`
    concept_phrase: `the #_ form-skip reader macro`
    question_what: `what [1 #_ 2 3] reads as (the 2 is dropped)`

### G10-11 sample 1/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

A row of three coins sat on the kitchen table in the village, set out as a
wager between Charlie and George. The bet was
simple: predict what `'(1 2 3)` would return. Charlie,
imagining all that might be gained, was certain about the answer. George asked
him, with steady, careful steps, to actually write the form into the
REPL — the quote reader macro 'foo would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for what '(1 2 3) reads as.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 sample 2/N (form: `(#(* % %) 6)`, expected: `36`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Edward had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the farm, the
next entry was the #(...) reader macro for an anonymous fn. Morgan peered over
his shoulder at the form `(#(* % %) 6)` and asked what
it would come out to.

Write a form whose evaluation gives what (#(* % %) 6) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

### G10-11 sample 3/N (form: `[1 #_ 2 3]`, expected: `[1, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Charlie stopped in the kitchen
with a basket of eggs and refused to move on until someone could
prove what the form `[1 #_ 2 3]` evaluated to. Charlie called it
impossible. Oliver, walking up at an unhurried pace, simply
said: "Submit the #_ form-skip reader macro to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes what [1 #_ 2 3] reads as (the 2 is dropped).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"[1 #_ 2 3]"}}]}
```

### G10-11 sample 4/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `'(1 2 3)` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the quote reader macro 'foo — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives what '(1 2 3) reads as.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-11 sample 5/N (form: `(#(* % %) 6)`, expected: `36`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Oliver had been trying to teach Sam how the REPL
works. "Here," he said, pointing to the #(...) reader macro for an anonymous fn.
"You hand the form `(#(* % %) 6)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for what (#(* % %) 6) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(#(* % %) 6)"}}]}
```

## G10-12: Tagged literals

**examples (2):**

- ex0: form=`(inst? #inst "2024-01-01")` expected=`True`
    concept_phrase: `the predicate (inst? #inst "2024-01-01")`
    question_what: `whether the #inst tagged literal reads to an inst`
- ex1: form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000")` expected=`True`
    concept_phrase: `the predicate on a #uuid tagged literal`
    question_what: `whether the #uuid tagged literal reads to a uuid`

### G10-12 sample 1/N (form: `(inst? #inst "2024-01-01")`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

A small audience of neighbors had gathered near the village to watch
Fiona attempt to outguess Helen at reading the
REPL. Helen pointed to the predicate (inst? #inst "2024-01-01") and read out the form
aloud: `(inst? #inst "2024-01-01")`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for whether the #inst tagged literal reads to an inst.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 sample 2/N (form: `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

A row of three coins sat on the kitchen table in a cottage, set out as a
wager between Robin and Bob. The bet was
simple: predict what `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` would return. Robin,
with a hungry gleam in the eye, was certain about the answer. Bob asked
them, with steady, careful steps, to actually write the form into the
REPL — the predicate on a #uuid tagged literal would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes whether the #uuid tagged literal reads to a uuid.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 sample 3/N (form: `(inst? #inst "2024-01-01")`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(inst? #inst "2024-01-01")` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the predicate (inst? #inst "2024-01-01") — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for whether the #inst tagged literal reads to an inst.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-12 sample 4/N (form: `(uuid? #uuid "00000000-0000-0000-0000-000000000000")`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Sam insisted inside the barn that macros for the egg-ledger were
the same as ordinary functions. Morgan, stepping deliberately, drew
the form `(uuid? #uuid "00000000-0000-0000-0000-000000000000")` on a strip of bark from the kitchen kindling.
"The difference," they said, "is in the predicate on a #uuid tagged literal. Submit
the form and let the runtime tell us exactly what it does."

What Clojure form computes whether the #uuid tagged literal reads to a uuid? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")"}}]}
```

### G10-12 sample 5/N (form: `(inst? #inst "2024-01-01")`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Morgan kept a second ledger by the meadow, a column for every macro
they had ever written for the egg-business and the long-form
each one expanded into. Today's row was the predicate (inst? #inst "2024-01-01").
Oliver, imagining all that might be gained, peered over their shoulder
and demanded the answer at once. Morgan pointed only to
`(inst? #inst "2024-01-01")` — submit it, and the macroexpander would write the row
themself.

What Clojure form computes whether the #inst tagged literal reads to an inst? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

## G10-13: Data readers and EDN extension

**examples (2):**

- ex0: form=`(clojure.edn/read-string "42")` expected=`42`
    concept_phrase: `edn read-string of "42"`
    question_what: `what edn/read-string returns for the source "42"`
- ex1: form=`(clojure.edn/read-string "[:a :b :c]")` expected=`[':a', ':b', ':c']`
    concept_phrase: `edn read-string of a vector source`
    question_what: `what edn/read-string returns for "[:a :b :c]"`

### G10-13 sample 1/N (form: `(clojure.edn/read-string "42")`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small ledger-notebook lay open on the kitchen table at the edge of the market where
Alice had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed edn read-string of "42", with
the form `(clojure.edn/read-string "42")` circled in pencil. Sam,
imagining all that might be gained of the lecture, agreed to write the form to settle once
and for all what it produced.

Write a form whose evaluation gives what edn/read-string returns for the source "42".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 sample 2/N (form: `(clojure.edn/read-string "[:a :b :c]")`, expected: `[':a', ':b', ':c']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

Helen offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(clojure.edn/read-string "[:a :b :c]")` first would keep them.
Oliver, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about edn read-string of a vector source; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for what edn/read-string returns for "[:a :b :c]".
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 sample 3/N (form: `(clojure.edn/read-string "42")`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Robin insisted inside a cottage that macros for the egg-ledger were
the same as ordinary functions. Diana, untroubled by what others thought, drew
the form `(clojure.edn/read-string "42")` on a strip of bark from the kitchen kindling.
"The difference," she said, "is in edn read-string of "42". Submit
the form and let the runtime tell us exactly what it does."

What Clojure form computes what edn/read-string returns for the source "42"? Submit it via `eval`.
---asst---
I write the form and let the macroexpander or REPL show the result.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-13 sample 4/N (form: `(clojure.edn/read-string "[:a :b :c]")`, expected: `[':a', ':b', ':c']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered in the kitchen to watch
Carol attempt to outguess Grace at reading the
REPL. Grace pointed to edn read-string of a vector source and read out the form
aloud: `(clojure.edn/read-string "[:a :b :c]")`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes what edn/read-string returns for "[:a :b :c]".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"[:a :b :c]\")"}}]}
```

### G10-13 sample 5/N (form: `(clojure.edn/read-string "42")`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(clojure.edn/read-string "42")` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — edn read-string of "42" would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives what edn/read-string returns for the source "42".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

## G10-14: eval (the function)

**examples (2):**

- ex0: form=`(eval '(+ 1 2 3))` expected=`6`
    concept_phrase: `the form (eval '(+ 1 2 3))`
    question_what: `what eval returns for the quoted (+ 1 2 3)`
- ex1: form=`(eval (list '+ 4 5))` expected=`9`
    concept_phrase: `eval applied to a constructed list`
    question_what: `what eval returns when handed (list '+ 4 5)`

### G10-14 sample 1/N (form: `(eval '(+ 1 2 3))`, expected: `6`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

Grace had spent the morning by the village sketching a tiny
ledger-language of her own — a notebook of macros that
expanded into the long-form tallies for Quill the goose's eggs. The
next entry was the form (eval '(+ 1 2 3)), and the form `(eval '(+ 1 2 3))` was what
Grace wanted Diana to submit so the REPL could show what
code it produced or what value it returned.

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 sample 2/N (form: `(eval (list '+ 4 5))`, expected: `9`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small ledger-notebook lay open on the kitchen table in the market where
Edward had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed eval applied to a constructed list, with
the form `(eval (list '+ 4 5))` circled in pencil. George,
with a glint of impatience of the lecture, agreed to write the form to settle once
and for all what it produced.

What Clojure form computes what eval returns when handed (list '+ 4 5)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 sample 3/N (form: `(eval '(+ 1 2 3))`, expected: `6`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

Edward had spent the morning in the meadow sketching a tiny
ledger-language of his own — a notebook of macros that
expanded into the long-form tallies for Plume the goose's eggs. The
next entry was the form (eval '(+ 1 2 3)), and the form `(eval '(+ 1 2 3))` was what
Edward wanted David to submit so the REPL could show what
code it produced or what value it returned.

Question: write a Clojure expression for what eval returns for the quoted (+ 1 2 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-14 sample 4/N (form: `(eval (list '+ 4 5))`, expected: `9`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

A small ledger-notebook lay open on the kitchen table in the barn where
Casey had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed eval applied to a constructed list, with
the form `(eval (list '+ 4 5))` circled in pencil. Jordan,
eyeing the next morning's gift of the lecture, agreed to write the form to settle once
and for all what it produced.

Question: write a Clojure expression for what eval returns when handed (list '+ 4 5).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(eval (list '+ 4 5))"}}]}
```

### G10-14 sample 5/N (form: `(eval '(+ 1 2 3))`, expected: `6`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

A small ledger-notebook lay open on the kitchen table deep inside a cottage where
Alice had been studying syntax-quote, the morning's eggs
counted in a column beside it. The page showed the form (eval '(+ 1 2 3)), with
the form `(eval '(+ 1 2 3))` circled in pencil. Bob,
eyeing the next morning's gift of the lecture, agreed to write the form to settle once
and for all what it produced.

What Clojure form computes what eval returns for the quoted (+ 1 2 3)? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

## G10-15: When not to write a macro

**examples (2):**

- ex0: form=`(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` expected=`7`
    concept_phrase: `a function call where no macro is justified`
    question_what: `what the plain function call returns`
- ex1: form=`(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` expected=`[2, 3, 4]`
    concept_phrase: `map applied to inc — no macro needed`
    question_what: `the result of mapping inc`

### G10-15 sample 1/N (form: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Robin had been trying to teach Emily how the REPL
works. "Here," they said, pointing to a function call where no macro is justified.
"You hand the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes what the plain function call returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 sample 2/N (form: `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`, expected: `[2, 3, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"A macro is just a function that runs at compile time," Charlie
explained deep inside the cellar, with steady, careful steps, while Quill the goose settled onto
the morning's egg. David, calculating in silence, said he
could already see what map applied to inc — no macro needed meant. Charlie insisted
they actually evaluate `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` and read what the runtime
reported, expansion or value.

Question: write a Clojure expression for the result of mapping inc.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 sample 3/N (form: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"A macro is just a function that runs at compile time," Casey
explained at the edge of the meadow, with steady, careful steps, while Plume the goose settled onto
the morning's egg. Alex, eyeing the next morning's gift, said they
could already see what a function call where no macro is justified meant. Casey insisted
they actually evaluate `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` and read what the runtime
reported, expansion or value.

Write a form whose evaluation gives what the plain function call returns.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-15 sample 4/N (form: `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))`, expected: `[2, 3, 4]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

The barn wall near the orchard was littered with old macro definitions
Diana had chalked up beside the egg-tallies. Robin
found one shaped like map applied to inc — no macro needed and dared Diana to
predict its expansion. Diana only smiled and asked them
to write `(do "prefer fn unless you must shape syntax" (map inc [1 2 3]))` into the REPL — that, after all, was the whole
point of having a macroexpander.

Question: write a Clojure expression for the result of mapping inc.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"prefer fn unless you must shape syntax\" (map inc [1 2 3]))"}}]}
```

### G10-15 sample 5/N (form: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post in the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`.
Bob laughed, boasting at every turn, and declared it too easy.
Sam said, her eyes always on the path, that the only honest way to know
a function call where no macro is justified was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for what the plain function call returns.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

## G10-16: Macro pattern library

**examples (2):**

- ex0: form=`(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` expected=`42`
    concept_phrase: `a with-X macro pattern that binds a local and runs body`
    question_what: `what the with- macro yields`
- ex1: form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` expected=`':slow'`
    concept_phrase: `a def-X-thing macro that introduces a named binding`
    question_what: `the value of the symbol the macro defined`

### G10-16 sample 1/N (form: `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))`, expected: `42`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Alice had spent the morning by the meadow sketching a tiny
ledger-language of her own — a notebook of macros that
expanded into the long-form tallies for Quill the goose's eggs. The
next entry was a with-X macro pattern that binds a local and runs body, and the form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` was what
Alice wanted Sam to submit so the REPL could show what
code it produced or what value it returned.

Write a form whose evaluation gives what the with- macro yields.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 sample 2/N (form: `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`, expected: `':slow'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Fiona offered a small basket of eggs as a wager deep inside the barn:
whoever guessed the result of `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` first would keep them.
Frank, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about a def-X-thing macro that introduces a named binding; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the value of the symbol the macro defined.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 sample 3/N (form: `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Bob offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` first would keep them.
Sam, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about a with-X macro pattern that binds a local and runs body; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a form whose evaluation gives what the with- macro yields.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

### G10-16 sample 4/N (form: `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)`, expected: `':slow'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"A macro is just a function that runs at compile time," Carol
explained in the market, stepping deliberately, while Quill the goose settled onto
the morning's egg. David, thoughts already on more, said he
could already see what a def-X-thing macro that introduces a named binding meant. Carol insisted
they actually evaluate `(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)` and read what the runtime
reported, expansion or value.

Write a Clojure expression that computes the value of the symbol the macro defined.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro def-pace [name v] `(def ~name ~v)) (def-pace race-pace :slow) race-pace)"}}]}
```

### G10-16 sample 5/N (form: `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))`, expected: `42`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"A macro is just a function that runs at compile time," Emily
explained inside the barn, stepping deliberately, while Plume the goose settled onto
the morning's egg. Bob, imagining all that might be gained, said he
could already see what a with-X macro pattern that binds a local and runs body meant. Emily insisted
they actually evaluate `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` and read what the runtime
reported, expansion or value.

Write a Clojure expression that computes what the with- macro yields.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

