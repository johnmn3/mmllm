# Grade 5 goose-eggs — deep spot-check

5 rendered records per subject (22 subjects × 5 = 110 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G5-01: if

**examples (3):**

- ex0: form=`(if true :a :b)` expected=`':a'`
    concept_phrase: `the form (if true :a :b)`
    question_what: `which of :a or :b is returned`
- ex1: form=`(if false :a :b)` expected=`':b'`
    concept_phrase: `the form (if false :a :b)`
    question_what: `which of :a or :b is returned`
- ex2: form=`(if (> 5 3) :a :b)` expected=`':a'`
    concept_phrase: `the form (if (> 5 3) :a :b)`
    question_what: `the if's branch`

### G5-01 sample 1/N (form: `(if true :a :b)`, expected: `':a'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

On the way to market near the market, Alice explained to
Carol how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form `(if true :a :b)` did exactly that for
the form (if true :a :b). Carol, puffed up with pride, guessed the result aloud;
Alice said, without complaint, that Plume the goose taught a
better habit: count by submitting, not by sky-gazing.

Write a Clojure expression that computes which of :a or :b is returned.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### G5-01 sample 2/N (form: `(if false :a :b)`, expected: `':b'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"Morning by morning, the goose lays one egg, and the days compound,"
Alice said at the edge of the farm, sketching the form `(if false :a :b)` into the
margin of the kitchen ledger. the form (if false :a :b) was, she
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Frank, wondering how the temptation had risen after an earlier wrong guess,
agreed this time to let the runtime decide.

Question: write a Clojure expression for which of :a or :b is returned.
---asst---
I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

### G5-01 sample 3/N (form: `(if (> 5 3) :a :b)`, expected: `':a'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(if (> 5 3) :a :b)`.
Morgan laughed, puffed up with pride, and declared it too easy.
Robin said, with steady, careful steps, that the only honest way to know
the form (if (> 5 3) :a :b) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the if's branch? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if (> 5 3) :a :b)"}}]}
```

### G5-01 sample 4/N (form: `(if true :a :b)`, expected: `':a'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"There is no need to evaluate that," Casey said, with great whoops of laughter.
"Anyone with eyes can see what the form (if true :a :b) comes to."
Edward, who in the cellar had grown used to such claims, asked
them to actually write the form `(if true :a :b)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes which of :a or :b is returned? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### G5-01 sample 5/N (form: `(if false :a :b)`, expected: `':b'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the form (if false :a :b) into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(if false :a :b)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives which of :a or :b is returned.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :a :b)"}}]}
```

## G5-02: if as expression

**examples (1):**

- ex0: form=`(+ 1 (if true 10 20))` expected=`11`
    concept_phrase: `the form (+ 1 (if true 10 20))`
    question_what: `the result of adding 1 to the if expression`

### G5-02 sample 1/N (form: `(+ 1 (if true 10 20))`, expected: `11`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what the form (+ 1 (if true 10 20)) comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(+ 1 (if true 10 20))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the result of adding 1 to the if expression.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 sample 2/N (form: `(+ 1 (if true 10 20))`, expected: `11`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to the form (+ 1 (if true 10 20)).
"You hand the form `(+ 1 (if true 10 20))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the result of adding 1 to the if expression.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 sample 3/N (form: `(+ 1 (if true 10 20))`, expected: `11`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(+ 1 (if true 10 20))` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the form (+ 1 (if true 10 20)) — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the result of adding 1 to the if expression.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 sample 4/N (form: `(+ 1 (if true 10 20))`, expected: `11`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam had been trying to teach David how the REPL
works. "Here," they said, pointing to the form (+ 1 (if true 10 20)).
"You hand the form `(+ 1 (if true 10 20))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes the result of adding 1 to the if expression? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-02 sample 5/N (form: `(+ 1 (if true 10 20))`, expected: `11`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Sam and Beatrice stood by the meadow where someone had
scratched the form (+ 1 (if true 10 20)) into a smooth slate by the egg-basket.
Beatrice, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Sam, saying very little, suggested they
actually submit the form `(+ 1 (if true 10 20))` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the result of adding 1 to the if expression.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

## G5-03: when

**examples (2):**

- ex0: form=`(when true :yes)` expected=`':yes'`
    concept_phrase: `the form (when true :yes)`
    question_what: `the value of (when true :yes)`
- ex1: form=`(when false :yes)` expected=`None`
    concept_phrase: `the form (when false :yes)`
    question_what: `the value of (when false :yes)`

### G5-03 sample 1/N (form: `(when true :yes)`, expected: `':yes'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(when true :yes)` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — the form (when true :yes) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of (when true :yes).
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### G5-03 sample 2/N (form: `(when false :yes)`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(when false :yes)` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form (when false :yes); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the value of (when false :yes).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### G5-03 sample 3/N (form: `(when true :yes)`, expected: `':yes'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

On the way to market by the meadow, Grace explained to
Robin how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form `(when true :yes)` did exactly that for
the form (when true :yes). Robin, with a smug grin, guessed the result aloud;
Grace said, untroubled by what others thought, that Plume the goose taught a
better habit: count by submitting, not by sky-gazing.

Question: write a Clojure expression for the value of (when true :yes).
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### G5-03 sample 4/N (form: `(when false :yes)`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched the form (when false :yes) into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(when false :yes)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value of (when false :yes)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(when false :yes)"}}]}
```

### G5-03 sample 5/N (form: `(when true :yes)`, expected: `':yes'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Carol said, with great whoops of laughter.
"Anyone with eyes can see what the form (when true :yes) comes to."
Emily, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(when true :yes)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of (when true :yes).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

## G5-04: cond

**examples (1):**

- ex0: form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` expected=`':b'`
    concept_phrase: `the cond form`
    question_what: `which clause of the cond fires`

### G5-04 sample 1/N (form: `(cond (= 1 2) :a (= 1 1) :b :else :c)`, expected: `':b'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to the cond form.
"You hand the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes which clause of the cond fires.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 sample 2/N (form: `(cond (= 1 2) :a (= 1 1) :b :else :c)`, expected: `':b'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit the cond form to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives which clause of the cond fires.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 sample 3/N (form: `(cond (= 1 2) :a (= 1 1) :b :else :c)`, expected: `':b'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Helen stopped near the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` evaluated to. Helen called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit the cond form to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes which clause of the cond fires.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 sample 4/N (form: `(cond (= 1 2) :a (= 1 1) :b :else :c)`, expected: `':b'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Oliver offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(cond (= 1 2) :a (= 1 1) :b :else :c)` first would keep them.
David, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the cond form; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for which clause of the cond fires.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-04 sample 5/N (form: `(cond (= 1 2) :a (= 1 1) :b :else :c)`, expected: `':b'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"Morning by morning, the goose lays one egg, and the days compound,"
Sam said in the cellar, sketching the form `(cond (= 1 2) :a (= 1 1) :b :else :c)` into the
margin of the kitchen ledger. the cond form was, they
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Bob, wishing for more careful counting after an earlier wrong guess,
agreed this time to let the runtime decide.

What Clojure form computes which clause of the cond fires? Submit it via `eval`.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

## G5-05: cond — :else

**examples (1):**

- ex0: form=`(cond false :a false :b :else :c)` expected=`':c'`
    concept_phrase: `the cond falling through to :else`
    question_what: `the :else value`

### G5-05 sample 1/N (form: `(cond false :a false :b :else :c)`, expected: `':c'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(cond false :a false :b :else :c)` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the cond falling through to :else to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the :else value.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 sample 2/N (form: `(cond false :a false :b :else :c)`, expected: `':c'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(cond false :a false :b :else :c)` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit the cond falling through to :else to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the :else value.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 sample 3/N (form: `(cond false :a false :b :else :c)`, expected: `':c'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

Frank offered a small basket of eggs as a wager inside the kitchen:
whoever guessed the result of `(cond false :a false :b :else :c)` first would keep them.
David, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the cond falling through to :else; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the :else value.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 sample 4/N (form: `(cond false :a false :b :else :c)`, expected: `':c'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post at the edge of the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(cond false :a false :b :else :c)`.
Sam laughed, with great whoops of laughter, and declared it too easy.
Grace said, untroubled by what others thought, that the only honest way to know
the cond falling through to :else was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the :else value.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-05 sample 5/N (form: `(cond false :a false :b :else :c)`, expected: `':c'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Morgan had been trying to teach Charlie how the REPL
works. "Here," they said, pointing to the cond falling through to :else.
"You hand the form `(cond false :a false :b :else :c)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the :else value? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

## G5-06: case

**examples (2):**

- ex0: form=`(case 2 1 :one 2 :two 3 :three :default)` expected=`':two'`
    concept_phrase: `the case form`
    question_what: `the matched branch`
- ex1: form=`(case 99 1 :one 2 :two :default)` expected=`':default'`
    concept_phrase: `case falling through to default`
    question_what: `the default branch`

### G5-06 sample 1/N (form: `(case 2 1 :one 2 :two 3 :three :default)`, expected: `':two'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what the case form comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `(case 2 1 :one 2 :two 3 :three :default)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the matched branch.
---asst---
I let the REPL apply the same operation across the basket.

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### G5-06 sample 2/N (form: `(case 99 1 :one 2 :two :default)`, expected: `':default'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Morning by morning, the goose lays one egg, and the days compound,"
Casey said at the edge of the market, sketching the form `(case 99 1 :one 2 :two :default)` into the
margin of the kitchen ledger. case falling through to default was, they
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Fiona, regretting the hasty thought after an earlier wrong guess,
agreed this time to let the runtime decide.

Question: write a Clojure expression for the default branch.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### G5-06 sample 3/N (form: `(case 2 1 :one 2 :two 3 :three :default)`, expected: `':two'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched the case form into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(case 2 1 :one 2 :two 3 :three :default)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the matched branch? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### G5-06 sample 4/N (form: `(case 99 1 :one 2 :two :default)`, expected: `':default'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(case 99 1 :one 2 :two :default)`.
Edward laughed, swaggering through the underbrush, and declared it too easy.
Emily said, her eyes always on the path, that the only honest way to know
case falling through to default was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the default branch.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(case 99 1 :one 2 :two :default)"}}]}
```

### G5-06 sample 5/N (form: `(case 2 1 :one 2 :two 3 :three :default)`, expected: `':two'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(case 2 1 :one 2 :two 3 :three :default)`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
the case form was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the matched branch.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

## G5-07: and / or as control flow

**examples (2):**

- ex0: form=`(and 1 2 3)` expected=`3`
    concept_phrase: `the form (and 1 2 3) returns last truthy`
    question_what: `the last truthy value`
- ex1: form=`(or nil false :found)` expected=`':found'`
    concept_phrase: `the form (or nil false :found)`
    question_what: `the first truthy value`

### G5-07 sample 1/N (form: `(and 1 2 3)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David kept a long ledger by the market where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(and 1 2 3)` captured the form (and 1 2 3) returns last truthy:
the same trick, repeated cleverly across the basket. Robin,
with hands itching to count more, claimed to know what would come back without running it;
David, her eyes always on the path, asked them to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes the last truthy value? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G5-07 sample 2/N (form: `(or nil false :found)`, expected: `':found'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

On the way to market deep inside the kitchen, David explained to
Edward how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form `(or nil false :found)` did exactly that for
the form (or nil false :found). Edward, boasting at every turn, guessed the result aloud;
David said, her eyes always on the path, that Plume the goose taught a
better habit: count by submitting, not by sky-gazing.

What Clojure form computes the first truthy value? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### G5-07 sample 3/N (form: `(and 1 2 3)`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"Morning by morning, the goose lays one egg, and the days compound,"
Fiona said deep inside the cellar, sketching the form `(and 1 2 3)` into the
margin of the kitchen ledger. the form (and 1 2 3) returns last truthy was, she
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Sam, wishing for more careful counting after an earlier wrong guess,
agreed this time to let the runtime decide.

What Clojure form computes the last truthy value? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G5-07 sample 4/N (form: `(or nil false :found)`, expected: `':found'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, George stopped near the market
with a basket of eggs and refused to move on until someone could
prove what the form `(or nil false :found)` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit the form (or nil false :found) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the first truthy value? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(or nil false :found)"}}]}
```

### G5-07 sample 5/N (form: `(and 1 2 3)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

Helen kept a long ledger deep inside a cottage where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(and 1 2 3)` captured the form (and 1 2 3) returns last truthy:
the same trick, repeated cleverly across the basket. Robin,
imagining all that might be gained, claimed to know what would come back without running it;
Helen, untroubled by what others thought, asked them to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes the last truthy value? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

## G5-08: not

**examples (1):**

- ex0: form=`(not (> 1 2))` expected=`True`
    concept_phrase: `the form (not (> 1 2))`
    question_what: `the negated comparison`

### G5-08 sample 1/N (form: `(not (> 1 2))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

On the way to market in the village, Bob explained to
Oliver how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form `(not (> 1 2))` did exactly that for
the form (not (> 1 2)). Oliver, with a smug grin, guessed the result aloud;
Bob said, stepping deliberately, that Plume the goose taught a
better habit: count by submitting, not by sky-gazing.

Write a form whose evaluation gives the negated comparison.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 sample 2/N (form: `(not (> 1 2))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(not (> 1 2))` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — the form (not (> 1 2)) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the negated comparison.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 sample 3/N (form: `(not (> 1 2))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to the form (not (> 1 2)).
"You hand the form `(not (> 1 2))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the negated comparison? Submit it via `eval`.
---asst---
I let the REPL apply the same operation across the basket.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 sample 4/N (form: `(not (> 1 2))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"Morning by morning, the goose lays one egg, and the days compound,"
Oliver said in the barn, sketching the form `(not (> 1 2))` into the
margin of the kitchen ledger. the form (not (> 1 2)) was, he
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Casey, wishing for more careful counting after an earlier wrong guess,
agreed this time to let the runtime decide.

What Clojure form computes the negated comparison? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-08 sample 5/N (form: `(not (> 1 2))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened inside the barn.

A row of three coins sat on the kitchen table in the barn, set out as a
wager between David and Frank. The bet was
simple: predict what `(not (> 1 2))` would return. David,
imagining all that might be gained, was certain about the answer. Frank asked
him, without complaint, to actually write the form into the
REPL — the form (not (> 1 2)) would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes the negated comparison.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

## G5-09: fn as value

**examples (1):**

- ex0: form=`((fn [f x] (f (f x))) inc 5)` expected=`7`
    concept_phrase: `applying f twice to x where f is inc`
    question_what: `the result of inc applied twice`

### G5-09 sample 1/N (form: `((fn [f x] (f (f x))) inc 5)`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was applying f twice to x where f is inc. George peered over
his shoulder at the form `((fn [f x] (f (f x))) inc 5)` and asked what
it would come out to.

Write a Clojure expression that computes the result of inc applied twice.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 sample 2/N (form: `((fn [f x] (f (f x))) inc 5)`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was applying f twice to x where f is inc. George peered over
their shoulder at the form `((fn [f x] (f (f x))) inc 5)` and asked what
it would come out to.

Write a form whose evaluation gives the result of inc applied twice.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 sample 3/N (form: `((fn [f x] (f (f x))) inc 5)`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `((fn [f x] (f (f x))) inc 5)` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about applying f twice to x where f is inc; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the result of inc applied twice.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 sample 4/N (form: `((fn [f x] (f (f x))) inc 5)`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in the kitchen.

Alex had been trying to teach Oliver how the REPL
works. "Here," they said, pointing to applying f twice to x where f is inc.
"You hand the form `((fn [f x] (f (f x))) inc 5)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the result of inc applied twice? Submit it via `eval`.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-09 sample 5/N (form: `((fn [f x] (f (f x))) inc 5)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Oliver stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `((fn [f x] (f (f x))) inc 5)` evaluated to. Oliver called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit applying f twice to x where f is inc to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for the result of inc applied twice.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

## G5-10: map

**examples (2):**

- ex0: form=`(map inc [1 2 3])` expected=`[2, 3, 4]`
    concept_phrase: `the form (map inc [1 2 3])`
    question_what: `[1 2 3] each incremented`
- ex1: form=`(map #(* % %) [1 2 3 4])` expected=`[1, 4, 9, 16]`
    concept_phrase: `the form (map #(* % %) [1 2 3 4])`
    question_what: `[1 2 3 4] each squared`

### G5-10 sample 1/N (form: `(map inc [1 2 3])`, expected: `[2, 3, 4]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

"Morning by morning, the goose lays one egg, and the days compound,"
Alex said deep inside the kitchen, sketching the form `(map inc [1 2 3])` into the
margin of the kitchen ledger. the form (map inc [1 2 3]) was, they
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Fiona, wondering how the temptation had risen after an earlier wrong guess,
agreed this time to let the runtime decide.

Write a Clojure expression that computes [1 2 3] each incremented.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### G5-10 sample 2/N (form: `(map #(* % %) [1 2 3 4])`, expected: `[1, 4, 9, 16]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to the form (map #(* % %) [1 2 3 4]).
"You hand the form `(map #(* % %) [1 2 3 4])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes [1 2 3 4] each squared? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### G5-10 sample 3/N (form: `(map inc [1 2 3])`, expected: `[2, 3, 4]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was the form (map inc [1 2 3]). Emily peered over
her shoulder at the form `(map inc [1 2 3])` and asked what
it would come out to.

Write a form whose evaluation gives [1 2 3] each incremented.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### G5-10 sample 4/N (form: `(map #(* % %) [1 2 3 4])`, expected: `[1, 4, 9, 16]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post in the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(map #(* % %) [1 2 3 4])`.
Robin laughed, swaggering through the underbrush, and declared it too easy.
Grace said, her eyes always on the path, that the only honest way to know
the form (map #(* % %) [1 2 3 4]) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives [1 2 3 4] each squared.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(map #(* % %) [1 2 3 4])"}}]}
```

### G5-10 sample 5/N (form: `(map inc [1 2 3])`, expected: `[2, 3, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(map inc [1 2 3])` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the form (map inc [1 2 3]); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives [1 2 3] each incremented.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

## G5-11: filter

**examples (2):**

- ex0: form=`(filter even? [1 2 3 4])` expected=`[2, 4]`
    concept_phrase: `the form (filter even? [1 2 3 4])`
    question_what: `the even numbers from [1 2 3 4]`
- ex1: form=`(filter pos? [-2 -1 0 1 2])` expected=`[1, 2]`
    concept_phrase: `the form (filter pos? ...)`
    question_what: `the positive numbers`

### G5-11 sample 1/N (form: `(filter even? [1 2 3 4])`, expected: `[2, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(filter even? [1 2 3 4])` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (filter even? [1 2 3 4]) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the even numbers from [1 2 3 4].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### G5-11 sample 2/N (form: `(filter pos? [-2 -1 0 1 2])`, expected: `[1, 2]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to the form (filter pos? ...) and read out the form
aloud: `(filter pos? [-2 -1 0 1 2])`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the positive numbers.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### G5-11 sample 3/N (form: `(filter even? [1 2 3 4])`, expected: `[2, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(filter even? [1 2 3 4])` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the form (filter even? [1 2 3 4]) — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the even numbers from [1 2 3 4].
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### G5-11 sample 4/N (form: `(filter pos? [-2 -1 0 1 2])`, expected: `[1, 2]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(filter pos? [-2 -1 0 1 2])` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the form (filter pos? ...); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the positive numbers.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(filter pos? [-2 -1 0 1 2])"}}]}
```

### G5-11 sample 5/N (form: `(filter even? [1 2 3 4])`, expected: `[2, 4]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(filter even? [1 2 3 4])`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
the form (filter even? [1 2 3 4]) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the even numbers from [1 2 3 4].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

## G5-12: reduce

**examples (3):**

- ex0: form=`(reduce + [1 2 3 4])` expected=`10`
    concept_phrase: `the form (reduce + [1 2 3 4])`
    question_what: `the sum`
- ex1: form=`(reduce * [1 2 3 4 5])` expected=`120`
    concept_phrase: `the form (reduce * [1 2 3 4 5])`
    question_what: `5!`
- ex2: form=`(reduce max [3 1 4 1 5 9 2 6])` expected=`9`
    concept_phrase: `the form (reduce max [...])`
    question_what: `the maximum`

### G5-12 sample 1/N (form: `(reduce + [1 2 3 4])`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to the form (reduce + [1 2 3 4]).
"You hand the form `(reduce + [1 2 3 4])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the sum.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### G5-12 sample 2/N (form: `(reduce * [1 2 3 4 5])`, expected: `120`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(reduce * [1 2 3 4 5])` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (reduce * [1 2 3 4 5]) — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes 5!.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

### G5-12 sample 3/N (form: `(reduce max [3 1 4 1 5 9 2 6])`, expected: `9`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Alice said, with great whoops of laughter.
"Anyone with eyes can see what the form (reduce max [...]) comes to."
Grace, who in the market had grown used to such claims, asked
her to actually write the form `(reduce max [3 1 4 1 5 9 2 6])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the maximum.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce max [3 1 4 1 5 9 2 6])"}}]}
```

### G5-12 sample 4/N (form: `(reduce + [1 2 3 4])`, expected: `10`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(reduce + [1 2 3 4])` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the form (reduce + [1 2 3 4]) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the sum.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### G5-12 sample 5/N (form: `(reduce * [1 2 3 4 5])`, expected: `120`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(reduce * [1 2 3 4 5])`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
the form (reduce * [1 2 3 4 5]) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes 5!? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce * [1 2 3 4 5])"}}]}
```

## G5-13: reduce with init

**examples (2):**

- ex0: form=`(reduce + 100 [1 2 3])` expected=`106`
    concept_phrase: `the form (reduce + 100 [1 2 3])`
    question_what: `100 + sum of [1 2 3]`
- ex1: form=`(reduce + 0 [])` expected=`0`
    concept_phrase: `the form (reduce + 0 [])`
    question_what: `the value when reducing over empty seq with init 0`

### G5-13 sample 1/N (form: `(reduce + 100 [1 2 3])`, expected: `106`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice kept a long ledger at the edge of the market where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(reduce + 100 [1 2 3])` captured the form (reduce + 100 [1 2 3]):
the same trick, repeated cleverly across the basket. Sam,
imagining all that might be gained, claimed to know what would come back without running it;
Alice, untroubled by what others thought, asked them to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

Write a form whose evaluation gives 100 + sum of [1 2 3].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### G5-13 sample 2/N (form: `(reduce + 0 [])`, expected: `0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `(reduce + 0 [])` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — the form (reduce + 0 []) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value when reducing over empty seq with init 0.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### G5-13 sample 3/N (form: `(reduce + 100 [1 2 3])`, expected: `106`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Diana kept a long ledger inside a cottage where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(reduce + 100 [1 2 3])` captured the form (reduce + 100 [1 2 3]):
the same trick, repeated cleverly across the basket. Robin,
with a glint of impatience, claimed to know what would come back without running it;
Diana, untroubled by what others thought, asked them to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes 100 + sum of [1 2 3]? Submit it via `eval`.
---asst---
I use map / filter / reduce as appropriate.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### G5-13 sample 4/N (form: `(reduce + 0 [])`, expected: `0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Grace had been trying to teach Carol how the REPL
works. "Here," she said, pointing to the form (reduce + 0 []).
"You hand the form `(reduce + 0 [])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value when reducing over empty seq with init 0.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 0 [])"}}]}
```

### G5-13 sample 5/N (form: `(reduce + 100 [1 2 3])`, expected: `106`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(reduce + 100 [1 2 3])` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — the form (reduce + 100 [1 2 3]) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives 100 + sum of [1 2 3].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

## G5-14: apply

**examples (2):**

- ex0: form=`(apply + [1 2 3 4])` expected=`10`
    concept_phrase: `the form (apply + [1 2 3 4])`
    question_what: `+ applied to the elements of the vector`
- ex1: form=`(apply max [3 1 4 1 5])` expected=`5`
    concept_phrase: `the form (apply max ...)`
    question_what: `max of the vector via apply`

### G5-14 sample 1/N (form: `(apply + [1 2 3 4])`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what the form (apply + [1 2 3 4]) comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(apply + [1 2 3 4])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes + applied to the elements of the vector.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### G5-14 sample 2/N (form: `(apply max [3 1 4 1 5])`, expected: `5`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward kept a long ledger in the market where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(apply max [3 1 4 1 5])` captured the form (apply max ...):
the same trick, repeated cleverly across the basket. George,
with a glint of impatience, claimed to know what would come back without running it;
Edward, saying very little, asked him to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes max of the vector via apply? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### G5-14 sample 3/N (form: `(apply + [1 2 3 4])`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the form (apply + [1 2 3 4]) comes to."
Edward, who in the meadow had grown used to such claims, asked
him to actually write the form `(apply + [1 2 3 4])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for + applied to the elements of the vector.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### G5-14 sample 4/N (form: `(apply max [3 1 4 1 5])`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

On the way to market in the barn, Casey explained to
Jordan how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form `(apply max [3 1 4 1 5])` did exactly that for
the form (apply max ...). Jordan, with great whoops of laughter, guessed the result aloud;
Casey said, with steady, careful steps, that Quill the goose taught a
better habit: count by submitting, not by sky-gazing.

Question: write a Clojure expression for max of the vector via apply.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(apply max [3 1 4 1 5])"}}]}
```

### G5-14 sample 5/N (form: `(apply + [1 2 3 4])`, expected: `10`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Alice kept a long ledger deep inside a cottage where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(apply + [1 2 3 4])` captured the form (apply + [1 2 3 4]):
the same trick, repeated cleverly across the basket. Bob,
eyeing the next morning's gift, claimed to know what would come back without running it;
Alice, without complaint, asked him to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes + applied to the elements of the vector? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

## G5-15: comp

**examples (2):**

- ex0: form=`((comp inc inc) 5)` expected=`7`
    concept_phrase: `the form ((comp inc inc) 5)`
    question_what: `inc twice applied to 5`
- ex1: form=`((comp str inc) 9)` expected=`'10'`
    concept_phrase: `the form ((comp str inc) 9)`
    question_what: `inc then str of 9`

### G5-15 sample 1/N (form: `((comp inc inc) 5)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `((comp inc inc) 5)` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the form ((comp inc inc) 5); the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes inc twice applied to 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### G5-15 sample 2/N (form: `((comp str inc) 9)`, expected: `'10'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the form ((comp str inc) 9) comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `((comp str inc) 9)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for inc then str of 9.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### G5-15 sample 3/N (form: `((comp inc inc) 5)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what the form ((comp inc inc) 5) comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `((comp inc inc) 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives inc twice applied to 5.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### G5-15 sample 4/N (form: `((comp str inc) 9)`, expected: `'10'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `((comp str inc) 9)`.
Robin laughed, with a smug grin, and declared it too easy.
Diana said, stepping deliberately, that the only honest way to know
the form ((comp str inc) 9) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for inc then str of 9.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((comp str inc) 9)"}}]}
```

### G5-15 sample 5/N (form: `((comp inc inc) 5)`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the market, the
next entry was the form ((comp inc inc) 5). Bob peered over
their shoulder at the form `((comp inc inc) 5)` and asked what
it would come out to.

Question: write a Clojure expression for inc twice applied to 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

## G5-16: partial

**examples (2):**

- ex0: form=`((partial + 10) 5)` expected=`15`
    concept_phrase: `the form ((partial + 10) 5)`
    question_what: `10 + 5`
- ex1: form=`(map (partial * 3) [1 2 3])` expected=`[3, 6, 9]`
    concept_phrase: `(partial * 3) mapped over [1 2 3]`
    question_what: `each element times 3`

### G5-16 sample 1/N (form: `((partial + 10) 5)`, expected: `15`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what the form ((partial + 10) 5) comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `((partial + 10) 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives 10 + 5.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### G5-16 sample 2/N (form: `(map (partial * 3) [1 2 3])`, expected: `[3, 6, 9]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(map (partial * 3) [1 2 3])` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — (partial * 3) mapped over [1 2 3] would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for each element times 3.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### G5-16 sample 3/N (form: `((partial + 10) 5)`, expected: `15`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `((partial + 10) 5)` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — the form ((partial + 10) 5) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives 10 + 5.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### G5-16 sample 4/N (form: `(map (partial * 3) [1 2 3])`, expected: `[3, 6, 9]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," David said, swaggering through the underbrush.
"Anyone with eyes can see what (partial * 3) mapped over [1 2 3] comes to."
Carol, who in the market had grown used to such claims, asked
him to actually write the form `(map (partial * 3) [1 2 3])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes each element times 3.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(map (partial * 3) [1 2 3])"}}]}
```

### G5-16 sample 5/N (form: `((partial + 10) 5)`, expected: `15`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Bob said, with a smug grin.
"Anyone with eyes can see what the form ((partial + 10) 5) comes to."
Emily, who inside the barn had grown used to such claims, asked
him to actually write the form `((partial + 10) 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes 10 + 5.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

## G5-17: juxt

**examples (1):**

- ex0: form=`((juxt inc dec) 5)` expected=`[6, 4]`
    concept_phrase: `the form ((juxt inc dec) 5)`
    question_what: `inc and dec of 5 in parallel`

### G5-17 sample 1/N (form: `((juxt inc dec) 5)`, expected: `[6, 4]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `((juxt inc dec) 5)`.
Grace laughed, boasting at every turn, and declared it too easy.
Oliver said, her eyes always on the path, that the only honest way to know
the form ((juxt inc dec) 5) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes inc and dec of 5 in parallel.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 sample 2/N (form: `((juxt inc dec) 5)`, expected: `[6, 4]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched the form ((juxt inc dec) 5) into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `((juxt inc dec) 5)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives inc and dec of 5 in parallel.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 sample 3/N (form: `((juxt inc dec) 5)`, expected: `[6, 4]`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Emily said, boasting at every turn.
"Anyone with eyes can see what the form ((juxt inc dec) 5) comes to."
Carol, who in the village had grown used to such claims, asked
her to actually write the form `((juxt inc dec) 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes inc and dec of 5 in parallel.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 sample 4/N (form: `((juxt inc dec) 5)`, expected: `[6, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was in the orchard.

David had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the orchard, the
next entry was the form ((juxt inc dec) 5). Oliver peered over
his shoulder at the form `((juxt inc dec) 5)` and asked what
it would come out to.

Question: write a Clojure expression for inc and dec of 5 in parallel.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-17 sample 5/N (form: `((juxt inc dec) 5)`, expected: `[6, 4]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened near the market.

Halfway through the morning errand, George stopped at the edge of the market
with a basket of eggs and refused to move on until someone could
prove what the form `((juxt inc dec) 5)` evaluated to. George called it
impossible. Oliver, walking up at an unhurried pace, simply
said: "Submit the form ((juxt inc dec) 5) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for inc and dec of 5 in parallel.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

## G5-18: some

**examples (2):**

- ex0: form=`(some even? [1 3 5 8 7])` expected=`True`
    concept_phrase: `the form (some even? [...])`
    question_what: `whether any element is even`
- ex1: form=`(some neg? [1 2 3])` expected=`None`
    concept_phrase: `the form (some neg? [1 2 3])`
    question_what: `the value when no element is negative (it's nil)`

### G5-18 sample 1/N (form: `(some even? [1 3 5 8 7])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol kept a long ledger inside the barn where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(some even? [1 3 5 8 7])` captured the form (some even? [...]):
the same trick, repeated cleverly across the basket. Alice,
with a glint of impatience, claimed to know what would come back without running it;
Carol, with steady, careful steps, asked her to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes whether any element is even? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### G5-18 sample 2/N (form: `(some neg? [1 2 3])`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice offered a small basket of eggs as a wager in the farm:
whoever guessed the result of `(some neg? [1 2 3])` first would keep them.
Emily, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the form (some neg? [1 2 3]); the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a form whose evaluation gives the value when no element is negative (it's nil).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### G5-18 sample 3/N (form: `(some even? [1 3 5 8 7])`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the form (some even? [...]) into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(some even? [1 3 5 8 7])` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives whether any element is even.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### G5-18 sample 4/N (form: `(some neg? [1 2 3])`, expected: `None`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

At a small stall in the kitchen, someone had chalked a wager: whoever
predicted the result of `(some neg? [1 2 3])` first would set the asking
price for the morning's eggs. David, her eyes always on the path, said it
was easier to type the form into the REPL than to argue about
the form (some neg? [1 2 3]) — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the value when no element is negative (it's nil).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(some neg? [1 2 3])"}}]}
```

### G5-18 sample 5/N (form: `(some even? [1 3 5 8 7])`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between Diana and Morgan. The bet was
simple: predict what `(some even? [1 3 5 8 7])` would return. Diana,
with a glint of impatience, was certain about the answer. Morgan asked
her, with steady, careful steps, to actually write the form into the
REPL — the form (some even? [...]) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives whether any element is even.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

## G5-19: every?

**examples (2):**

- ex0: form=`(every? pos? [1 2 3])` expected=`True`
    concept_phrase: `the form (every? pos? [1 2 3])`
    question_what: `whether all are positive`
- ex1: form=`(every? even? [1 2 3])` expected=`False`
    concept_phrase: `the form (every? even? [1 2 3])`
    question_what: `whether all are even`

### G5-19 sample 1/N (form: `(every? pos? [1 2 3])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"Morning by morning, the goose lays one egg, and the days compound,"
Grace said deep inside a cottage, sketching the form `(every? pos? [1 2 3])` into the
margin of the kitchen ledger. the form (every? pos? [1 2 3]) was, she
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. Carol, regretting the hasty thought after an earlier wrong guess,
agreed this time to let the runtime decide.

What Clojure form computes whether all are positive? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### G5-19 sample 2/N (form: `(every? even? [1 2 3])`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the farm, the
next entry was the form (every? even? [1 2 3]). Jordan peered over
their shoulder at the form `(every? even? [1 2 3])` and asked what
it would come out to.

Question: write a Clojure expression for whether all are even.
---asst---
I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### G5-19 sample 3/N (form: `(every? pos? [1 2 3])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been trying to teach Alex how the REPL
works. "Here," she said, pointing to the form (every? pos? [1 2 3]).
"You hand the form `(every? pos? [1 2 3])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes whether all are positive.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### G5-19 sample 4/N (form: `(every? even? [1 2 3])`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the kitchen.

"There is no need to evaluate that," Robin said, boasting at every turn.
"Anyone with eyes can see what the form (every? even? [1 2 3]) comes to."
Helen, who deep inside the kitchen had grown used to such claims, asked
them to actually write the form `(every? even? [1 2 3])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for whether all are even.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(every? even? [1 2 3])"}}]}
```

### G5-19 sample 5/N (form: `(every? pos? [1 2 3])`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the farm, the
next entry was the form (every? pos? [1 2 3]). Robin peered over
her shoulder at the form `(every? pos? [1 2 3])` and asked what
it would come out to.

Write a Clojure expression that computes whether all are positive.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

## G5-20: take and drop

**examples (2):**

- ex0: form=`(take 3 [10 20 30 40 50])` expected=`[10, 20, 30]`
    concept_phrase: `the form (take 3 ...)`
    question_what: `the first three elements`
- ex1: form=`(drop 2 [10 20 30 40 50])` expected=`[30, 40, 50]`
    concept_phrase: `the form (drop 2 ...)`
    question_what: `all but the first two`

### G5-20 sample 1/N (form: `(take 3 [10 20 30 40 50])`, expected: `[10, 20, 30]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the kitchen, the
next entry was the form (take 3 ...). David peered over
his shoulder at the form `(take 3 [10 20 30 40 50])` and asked what
it would come out to.

Write a Clojure expression that computes the first three elements.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### G5-20 sample 2/N (form: `(drop 2 [10 20 30 40 50])`, expected: `[30, 40, 50]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Jordan said, with great whoops of laughter.
"Anyone with eyes can see what the form (drop 2 ...) comes to."
Alice, who in the cellar had grown used to such claims, asked
them to actually write the form `(drop 2 [10 20 30 40 50])` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes all but the first two.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### G5-20 sample 3/N (form: `(take 3 [10 20 30 40 50])`, expected: `[10, 20, 30]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post at the edge of the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(take 3 [10 20 30 40 50])`.
Bob laughed, with great whoops of laughter, and declared it too easy.
Fiona said, her eyes always on the path, that the only honest way to know
the form (take 3 ...) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the first three elements? Submit it via `eval`.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### G5-20 sample 4/N (form: `(drop 2 [10 20 30 40 50])`, expected: `[30, 40, 50]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today by the meadow, the
next entry was the form (drop 2 ...). Bob peered over
his shoulder at the form `(drop 2 [10 20 30 40 50])` and asked what
it would come out to.

Question: write a Clojure expression for all but the first two.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(drop 2 [10 20 30 40 50])"}}]}
```

### G5-20 sample 5/N (form: `(take 3 [10 20 30 40 50])`, expected: `[10, 20, 30]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the kitchen.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today inside the kitchen, the
next entry was the form (take 3 ...). Jordan peered over
her shoulder at the form `(take 3 [10 20 30 40 50])` and asked what
it would come out to.

What Clojure form computes the first three elements? Submit it via `eval`.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

## G5-21: distinct and sort

**examples (2):**

- ex0: form=`(distinct [1 1 2 3 3 4])` expected=`[1, 2, 3, 4]`
    concept_phrase: `the form (distinct [1 1 2 3 3 4])`
    question_what: `the deduplicated seq`
- ex1: form=`(sort [3 1 2])` expected=`[1, 2, 3]`
    concept_phrase: `the form (sort [3 1 2])`
    question_what: `the sorted seq`

### G5-21 sample 1/N (form: `(distinct [1 1 2 3 3 4])`, expected: `[1, 2, 3, 4]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the village, the
next entry was the form (distinct [1 1 2 3 3 4]). Morgan peered over
his shoulder at the form `(distinct [1 1 2 3 3 4])` and asked what
it would come out to.

Question: write a Clojure expression for the deduplicated seq.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### G5-21 sample 2/N (form: `(sort [3 1 2])`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the village.

Frank kept a long ledger at the edge of the village where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(sort [3 1 2])` captured the form (sort [3 1 2]):
the same trick, repeated cleverly across the basket. Grace,
thoughts already on more, claimed to know what would come back without running it;
Frank, without complaint, asked her to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

Write a Clojure expression that computes the sorted seq.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### G5-21 sample 3/N (form: `(distinct [1 1 2 3 3 4])`, expected: `[1, 2, 3, 4]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Frank and Helen stood in the barn where someone had
scratched the form (distinct [1 1 2 3 3 4]) into a smooth slate by the egg-basket.
Helen, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Frank, untroubled by what others thought, suggested they
actually submit the form `(distinct [1 1 2 3 3 4])` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Question: write a Clojure expression for the deduplicated seq.
---asst---
I let the runtime hand back one value, the way the goose gives one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### G5-21 sample 4/N (form: `(sort [3 1 2])`, expected: `[1, 2, 3]`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Diana had been trying to teach Jordan how the REPL
works. "Here," she said, pointing to the form (sort [3 1 2]).
"You hand the form `(sort [3 1 2])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the sorted seq.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(sort [3 1 2])"}}]}
```

### G5-21 sample 5/N (form: `(distinct [1 1 2 3 3 4])`, expected: `[1, 2, 3, 4]`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside a cottage.

Edward had been trying to teach Robin how the REPL
works. "Here," he said, pointing to the form (distinct [1 1 2 3 3 4]).
"You hand the form `(distinct [1 1 2 3 3 4])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the deduplicated seq.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

## G5-22: recur — first taste

**examples (1):**

- ex0: form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` expected=`120`
    concept_phrase: `a loop computing factorial of 5 via recur`
    question_what: `5! computed via loop/recur`

### G5-22 sample 1/N (form: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`, expected: `120`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered near the orchard to watch
David attempt to outguess Helen at reading the
REPL. Helen pointed to a loop computing factorial of 5 via recur and read out the form
aloud: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes 5! computed via loop/recur.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 sample 2/N (form: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`, expected: `120`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered near the farm to watch
Bob attempt to outguess Sam at reading the
REPL. Sam pointed to a loop computing factorial of 5 via recur and read out the form
aloud: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes 5! computed via loop/recur.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 sample 3/N (form: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`, expected: `120`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the kitchen.

A small audience of neighbors had gathered in the kitchen to watch
Alex attempt to outguess Beatrice at reading the
REPL. Beatrice pointed to a loop computing factorial of 5 via recur and read out the form
aloud: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes 5! computed via loop/recur.
---asst---
I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 sample 4/N (form: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`, expected: `120`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice had been trying to teach George how the REPL
works. "Here," she said, pointing to a loop computing factorial of 5 via recur.
"You hand the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for 5! computed via loop/recur.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

### G5-22 sample 5/N (form: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`, expected: `120`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the meadow.

Sam kept a long ledger by the meadow where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` captured a loop computing factorial of 5 via recur:
the same trick, repeated cleverly across the basket. Carol,
eyeing the next morning's gift, claimed to know what would come back without running it;
Sam, her eyes always on the path, asked her to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg.

What Clojure form computes 5! computed via loop/recur? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

