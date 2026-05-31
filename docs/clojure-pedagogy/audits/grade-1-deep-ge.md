# Grade 1 goose-eggs — deep spot-check

5 rendered records per subject (18 subjects × 5 = 90 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G1-01: Eval as substitution

**examples (8):**

- ex0: form=`42` expected=`42`
    concept_phrase: `the value 42`
    question_what: `the value of 42`
- ex1: form=`0` expected=`0`
    concept_phrase: `the value 0`
    question_what: `the value of 0`
- ex2: form=`(+ 1 2)` expected=`3`
    concept_phrase: `the form (+ 1 2)`
    question_what: `the result of (+ 1 2)`
- ex3: form=`(* 4 5)` expected=`20`
    concept_phrase: `the form (* 4 5)`
    question_what: `the result of (* 4 5)`
- ex4: form=`(- 10 (+ 2 3))` expected=`5`
    concept_phrase: `the nested form (- 10 (+ 2 3))`
    question_what: `the result of (- 10 (+ 2 3))`
- ex5: form=`(+ 1 (* 2 3))` expected=`7`
    concept_phrase: `the form (+ 1 (* 2 3))`
    question_what: `the result of (+ 1 (* 2 3))`
- ex6: form=`"hello"` expected=`'hello'`
    concept_phrase: `the string "hello"`
    question_what: `the value of "hello"`
- ex7: form=`nil` expected=`None`
    concept_phrase: `the literal nil`
    question_what: `the value of nil`

### G1-01 sample 1/N (form: `42`, expected: `42`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Carol said, puffed up with pride.
"Anyone with eyes can see what the value 42 comes to."
Alice, who near the market had grown used to such claims, asked
her to actually write the form `42` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of 42.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 sample 2/N (form: `0`, expected: `0`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post at the edge of the farm carried a puzzle for
the village. The riddle asked the reader to evaluate `0`.
Frank laughed, as if the race were already won, and declared it too easy.
Alice said, saying very little, that the only honest way to know
the value 0 was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the value of 0.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### G1-01 sample 3/N (form: `(+ 1 2)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Diana had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the farm, the
next entry was the form (+ 1 2). Casey peered over
her shoulder at the form `(+ 1 2)` and asked what
it would come out to.

Write a form whose evaluation gives the result of (+ 1 2).
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-01 sample 4/N (form: `(* 4 5)`, expected: `20`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered deep inside the barn to watch
Casey attempt to outguess Alice at reading the
REPL. Alice pointed to the form (* 4 5) and read out the form
aloud: `(* 4 5)`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the result of (* 4 5).
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### G1-01 sample 5/N (form: `(- 10 (+ 2 3))`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

At a small stall in the kitchen, someone had chalked a wager: whoever
predicted the result of `(- 10 (+ 2 3))` first would set the asking
price for the morning's eggs. Charlie, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the nested form (- 10 (+ 2 3)) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the result of (- 10 (+ 2 3)).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(- 10 (+ 2 3))"}}]}
```

## G1-02: Integer numbers

**examples (6):**

- ex0: form=`7` expected=`7`
    concept_phrase: `the integer 7`
    question_what: `the value of the integer 7`
- ex1: form=`-3` expected=`-3`
    concept_phrase: `the integer -3`
    question_what: `the value of the integer -3`
- ex2: form=`0` expected=`0`
    concept_phrase: `the integer 0`
    question_what: `the value of zero`
- ex3: form=`100` expected=`100`
    concept_phrase: `the integer 100`
    question_what: `the value of one hundred`
- ex4: form=`-25` expected=`-25`
    concept_phrase: `the integer -25`
    question_what: `the value of negative twenty-five`
- ex5: form=`12345` expected=`12345`
    concept_phrase: `the integer 12345`
    question_what: `the value of 12345`

### G1-02 sample 1/N (form: `7`, expected: `7`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

Halfway through the morning errand, Oliver stopped inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `7` evaluated to. Oliver called it
impossible. Henry, walking up at an unhurried pace, simply
said: "Submit the integer 7 to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of the integer 7.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 sample 2/N (form: `-3`, expected: `-3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in the village.

Helen and Emily stood at the edge of the village where someone had
scratched the integer -3 into a smooth slate by the egg-basket.
Emily, as if the race were already won, declared the answer was obvious — no need to
evaluate anything. Helen, stepping deliberately, suggested they
actually submit the form `-3` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a Clojure expression that computes the value of the integer -3.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"-3"}}]}
```

### G1-02 sample 3/N (form: `0`, expected: `0`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in the meadow.

Alex offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `0` first would keep them.
Robin, with steady, careful steps, said it would be simpler to type the
form into the REPL than to bicker about the integer 0; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for the value of zero.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### G1-02 sample 4/N (form: `100`, expected: `100`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Emily stopped at the edge of the village
with a basket of eggs and refused to move on until someone could
prove what the form `100` evaluated to. Emily called it
impossible. Charlie, walking up at an unhurried pace, simply
said: "Submit the integer 100 to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the value of one hundred.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"100"}}]}
```

### G1-02 sample 5/N (form: `-25`, expected: `-25`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Robin stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `-25` evaluated to. Robin called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit the integer -25 to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of negative twenty-five.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"-25"}}]}
```

## G1-03: Ratios

**examples (5):**

- ex0: form=`1/2` expected=`'1/2'`
    concept_phrase: `the ratio 1/2`
    question_what: `the value of the ratio 1/2`
- ex1: form=`3/4` expected=`'3/4'`
    concept_phrase: `the ratio 3/4`
    question_what: `the value of three-quarters`
- ex2: form=`(+ 1/2 1/4)` expected=`'3/4'`
    concept_phrase: `the form (+ 1/2 1/4)`
    question_what: `the value of (+ 1/2 1/4)`
- ex3: form=`(* 2 1/2)` expected=`1`
    concept_phrase: `the form (* 2 1/2)`
    question_what: `the value of (* 2 1/2)`
- ex4: form=`(- 1 1/3)` expected=`'2/3'`
    concept_phrase: `the form (- 1 1/3)`
    question_what: `the value of (- 1 1/3)`

### G1-03 sample 1/N (form: `1/2`, expected: `'1/2'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

At a small stall in the meadow, someone had chalked a wager: whoever
predicted the result of `1/2` first would set the asking
price for the morning's eggs. Henry, stepping deliberately, said it
was easier to type the form into the REPL than to argue about
the ratio 1/2 — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the value of the ratio 1/2.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 sample 2/N (form: `3/4`, expected: `'3/4'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Robin and Alex. The bet was
simple: predict what `3/4` would return. Robin,
with hands itching to count more, was certain about the answer. Alex asked
them, without complaint, to actually write the form into the
REPL — the ratio 3/4 would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of three-quarters.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"3/4"}}]}
```

### G1-03 sample 3/N (form: `(+ 1/2 1/4)`, expected: `'3/4'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside a cottage.

A small wooden notice nailed to a post in a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 1/2 1/4)`.
Fiona laughed, puffed up with pride, and declared it too easy.
Beatrice said, stepping deliberately, that the only honest way to know
the form (+ 1/2 1/4) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value of (+ 1/2 1/4).
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G1-03 sample 4/N (form: `(* 2 1/2)`, expected: `1`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Bob had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today deep inside the barn, the
next entry was the form (* 2 1/2). Casey peered over
his shoulder at the form `(* 2 1/2)` and asked what
it would come out to.

Write a form whose evaluation gives the value of (* 2 1/2).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 1/2)"}}]}
```

### G1-03 sample 5/N (form: `(- 1 1/3)`, expected: `'2/3'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post near the farm carried a puzzle for
the village. The riddle asked the reader to evaluate `(- 1 1/3)`.
Carol laughed, puffed up with pride, and declared it too easy.
Helen said, saying very little, that the only honest way to know
the form (- 1 1/3) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value of (- 1 1/3).
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

## G1-04: Strings

**examples (5):**

- ex0: form=`"hello"` expected=`'hello'`
    concept_phrase: `the string "hello"`
    question_what: `the value of "hello"`
- ex1: form=`"egg"` expected=`'egg'`
    concept_phrase: `the string "egg"`
    question_what: `the value of "egg"`
- ex2: form=`"golden egg"` expected=`'golden egg'`
    concept_phrase: `the string "golden egg"`
    question_what: `the value of "golden egg"`
- ex3: form=`""` expected=`''`
    concept_phrase: `the empty string`
    question_what: `the value of the empty string`
- ex4: form=`"42"` expected=`'42'`
    concept_phrase: `the string "42"`
    question_what: `the value of the string "42"`

### G1-04 sample 1/N (form: `"hello"`, expected: `'hello'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Charlie offered a small basket of eggs as a wager inside the cellar:
whoever guessed the result of `"hello"` first would keep them.
Alice, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the string "hello"; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a Clojure expression that computes the value of "hello".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 sample 2/N (form: `"egg"`, expected: `'egg'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

Grace had been trying to teach Bob how the REPL
works. "Here," she said, pointing to the string "egg".
"You hand the form `"egg"` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the value of "egg".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"\"egg\""}}]}
```

### G1-04 sample 3/N (form: `"golden egg"`, expected: `'golden egg'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, David stopped by the market
with a basket of eggs and refused to move on until someone could
prove what the form `"golden egg"` evaluated to. David called it
impossible. Alice, walking up at an unhurried pace, simply
said: "Submit the string "golden egg" to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the value of "golden egg".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"\"golden egg\""}}]}
```

### G1-04 sample 4/N (form: `""`, expected: `''`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

David had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the village, the
next entry was the empty string. George peered over
his shoulder at the form `""` and asked what
it would come out to.

Write a form whose evaluation gives the value of the empty string.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"\"\""}}]}
```

### G1-04 sample 5/N (form: `"42"`, expected: `'42'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Emily said, swaggering through the underbrush.
"Anyone with eyes can see what the string "42" comes to."
Morgan, who in the village had grown used to such claims, asked
her to actually write the form `"42"` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the value of the string "42".
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"\"42\""}}]}
```

## G1-05: Booleans

**examples (6):**

- ex0: form=`true` expected=`True`
    concept_phrase: `the literal true`
    question_what: `the value of true`
- ex1: form=`false` expected=`False`
    concept_phrase: `the literal false`
    question_what: `the value of false`
- ex2: form=`(= 1 1)` expected=`True`
    concept_phrase: `the equality (= 1 1)`
    question_what: `the value of (= 1 1)`
- ex3: form=`(= 1 2)` expected=`False`
    concept_phrase: `the equality (= 1 2)`
    question_what: `the value of (= 1 2)`
- ex4: form=`(< 3 5)` expected=`True`
    concept_phrase: `the comparison (< 3 5)`
    question_what: `the value of (< 3 5)`
- ex5: form=`(> 3 5)` expected=`False`
    concept_phrase: `the comparison (> 3 5)`
    question_what: `the value of (> 3 5)`

### G1-05 sample 1/N (form: `true`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered deep inside the cellar to watch
Beatrice attempt to outguess Fiona at reading the
REPL. Fiona pointed to the literal true and read out the form
aloud: `true`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the value of true.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 sample 2/N (form: `false`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Beatrice said, swaggering through the underbrush.
"Anyone with eyes can see what the literal false comes to."
Charlie, who near the market had grown used to such claims, asked
her to actually write the form `false` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of false.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"false"}}]}
```

### G1-05 sample 3/N (form: `(= 1 1)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table near the farm, set out as a
wager between Bob and Frank. The bet was
simple: predict what `(= 1 1)` would return. Bob,
eyeing the next morning's gift, was certain about the answer. Frank asked
him, her eyes always on the path, to actually write the form into the
REPL — the equality (= 1 1) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value of (= 1 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-05 sample 4/N (form: `(= 1 2)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today near the market, the
next entry was the equality (= 1 2). Fiona peered over
their shoulder at the form `(= 1 2)` and asked what
it would come out to.

Write a Clojure expression that computes the value of (= 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### G1-05 sample 5/N (form: `(< 3 5)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place by the market.

Carol offered a small basket of eggs as a wager in the market:
whoever guessed the result of `(< 3 5)` first would keep them.
Alice, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about the comparison (< 3 5); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the value of (< 3 5).
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 5)"}}]}
```

## G1-06: nil

**examples (5):**

- ex0: form=`nil` expected=`None`
    concept_phrase: `the literal nil`
    question_what: `the value of nil`
- ex1: form=`(nil? nil)` expected=`True`
    concept_phrase: `the predicate (nil? nil)`
    question_what: `whether nil is nil`
- ex2: form=`(nil? 0)` expected=`False`
    concept_phrase: `the predicate (nil? 0)`
    question_what: `whether 0 is nil`
- ex3: form=`(nil? false)` expected=`False`
    concept_phrase: `the predicate (nil? false)`
    question_what: `whether false is nil`
- ex4: form=`(= nil nil)` expected=`True`
    concept_phrase: `the equality (= nil nil)`
    question_what: `the value of (= nil nil)`

### G1-06 sample 1/N (form: `nil`, expected: `None`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Edward stopped by the farm
with a basket of eggs and refused to move on until someone could
prove what the form `nil` evaluated to. Edward called it
impossible. Henry, walking up at an unhurried pace, simply
said: "Submit the literal nil to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the value of nil.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 sample 2/N (form: `(nil? nil)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post at the edge of the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(nil? nil)`.
Fiona laughed, as if the race were already won, and declared it too easy.
Casey said, without complaint, that the only honest way to know
the predicate (nil? nil) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for whether nil is nil.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(nil? nil)"}}]}
```

### G1-06 sample 3/N (form: `(nil? 0)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the cellar carried a puzzle for
the village. The riddle asked the reader to evaluate `(nil? 0)`.
George laughed, swaggering through the underbrush, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
the predicate (nil? 0) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives whether 0 is nil.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(nil? 0)"}}]}
```

### G1-06 sample 4/N (form: `(nil? false)`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Grace offered a small basket of eggs as a wager at the edge of the market:
whoever guessed the result of `(nil? false)` first would keep them.
Fiona, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the predicate (nil? false); the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a form whose evaluation gives whether false is nil.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(nil? false)"}}]}
```

### G1-06 sample 5/N (form: `(= nil nil)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Fiona had been trying to teach Frank how the REPL
works. "Here," she said, pointing to the equality (= nil nil).
"You hand the form `(= nil nil)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the value of (= nil nil).
---asst---
I let the runtime hand back one value, the way the goose gives one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(= nil nil)"}}]}
```

## G1-07: Keywords

**examples (5):**

- ex0: form=`:egg` expected=`':egg'`
    concept_phrase: `the keyword :egg`
    question_what: `the value of :egg`
- ex1: form=`:goose` expected=`':goose'`
    concept_phrase: `the keyword :goose`
    question_what: `the value of :goose`
- ex2: form=`:gold` expected=`':gold'`
    concept_phrase: `the keyword :gold`
    question_what: `the value of :gold`
- ex3: form=`(keyword? :egg)` expected=`True`
    concept_phrase: `the predicate (keyword? :egg)`
    question_what: `whether :egg is a keyword`
- ex4: form=`(= :egg :egg)` expected=`True`
    concept_phrase: `the equality of two :egg keywords`
    question_what: `whether :egg equals :egg`

### G1-07 sample 1/N (form: `:egg`, expected: `':egg'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Robin said, with great whoops of laughter.
"Anyone with eyes can see what the keyword :egg comes to."
David, who by the market had grown used to such claims, asked
them to actually write the form `:egg` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the value of :egg? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":":egg"}}]}
```

### G1-07 sample 2/N (form: `:goose`, expected: `':goose'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

"There is no need to evaluate that," Edward said, boasting at every turn.
"Anyone with eyes can see what the keyword :goose comes to."
David, who deep inside the kitchen had grown used to such claims, asked
him to actually write the form `:goose` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the value of :goose? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":":goose"}}]}
```

### G1-07 sample 3/N (form: `:gold`, expected: `':gold'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Henry had been trying to teach Beatrice how the REPL
works. "Here," he said, pointing to the keyword :gold.
"You hand the form `:gold` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

What Clojure form computes the value of :gold? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":":gold"}}]}
```

### G1-07 sample 4/N (form: `(keyword? :egg)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Grace said, swaggering through the underbrush.
"Anyone with eyes can see what the predicate (keyword? :egg) comes to."
Jordan, who inside a cottage had grown used to such claims, asked
her to actually write the form `(keyword? :egg)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for whether :egg is a keyword.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(keyword? :egg)"}}]}
```

### G1-07 sample 5/N (form: `(= :egg :egg)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Alex had been trying to teach Beatrice how the REPL
works. "Here," they said, pointing to the equality of two :egg keywords.
"You hand the form `(= :egg :egg)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for whether :egg equals :egg.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= :egg :egg)"}}]}
```

## G1-08: Characters

**examples (4):**

- ex0: form=`\g` expected=`'g'`
    concept_phrase: `the character \g`
    question_what: `the value of \g`
- ex1: form=`\space` expected=`' '`
    concept_phrase: `the character \space`
    question_what: `the value of \space`
- ex2: form=`\E` expected=`'E'`
    concept_phrase: `the character \E`
    question_what: `the value of \E`
- ex3: form=`(char? \g)` expected=`True`
    concept_phrase: `the predicate (char? \g)`
    question_what: `whether \g is a character`

### G1-08 sample 1/N (form: `\g`, expected: `'g'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

"There is no need to evaluate that," Oliver said, with a smug grin.
"Anyone with eyes can see what the character \g comes to."
Bob, who in the village had grown used to such claims, asked
him to actually write the form `\g` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of \g.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"\\g"}}]}
```

### G1-08 sample 2/N (form: `\space`, expected: `' '`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened by the farm.

"There is no need to evaluate that," George said, with a smug grin.
"Anyone with eyes can see what the character \space comes to."
Robin, who in the farm had grown used to such claims, asked
him to actually write the form `\space` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the value of \space? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"\\space"}}]}
```

### G1-08 sample 3/N (form: `\E`, expected: `'E'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin had been trying to teach Sam how the REPL
works. "Here," they said, pointing to the character \E.
"You hand the form `\E` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the value of \E.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"\\E"}}]}
```

### G1-08 sample 4/N (form: `(char? \g)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Charlie and George stood near the market where someone had
scratched the predicate (char? \g) into a smooth slate by the egg-basket.
George, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Charlie, without complaint, suggested they
actually submit the form `(char? \g)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Question: write a Clojure expression for whether \g is a character.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(char? \\g)"}}]}
```

### G1-08 sample 5/N (form: `\g`, expected: `'g'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

At a small stall near the orchard, someone had chalked a wager: whoever
predicted the result of `\g` first would set the asking
price for the morning's eggs. Jordan, stepping deliberately, said it
was easier to type the form into the REPL than to argue about
the character \g — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the value of \g.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"\\g"}}]}
```

## G1-09: Symbols vs values

**examples (4):**

- ex0: form=`(symbol? 'goose)` expected=`True`
    concept_phrase: `the predicate (symbol? 'goose)`
    question_what: `whether 'goose is a symbol`
- ex1: form=`(symbol? 42)` expected=`False`
    concept_phrase: `the predicate (symbol? 42)`
    question_what: `whether 42 is a symbol`
- ex2: form=`'goose` expected=`'goose'`
    concept_phrase: `the quoted symbol 'goose`
    question_what: `the value of 'goose`
- ex3: form=`(= 'goose 'goose)` expected=`True`
    concept_phrase: `the equality of two 'goose symbols`
    question_what: `whether 'goose equals 'goose`

### G1-09 sample 1/N (form: `(symbol? 'goose)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered in the village to watch
George attempt to outguess Oliver at reading the
REPL. Oliver pointed to the predicate (symbol? 'goose) and read out the form
aloud: `(symbol? 'goose)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes whether 'goose is a symbol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'goose)"}}]}
```

### G1-09 sample 2/N (form: `(symbol? 42)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been trying to teach David how the REPL
works. "Here," she said, pointing to the predicate (symbol? 42).
"You hand the form `(symbol? 42)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for whether 42 is a symbol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 42)"}}]}
```

### G1-09 sample 3/N (form: `'goose`, expected: `'goose'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place by the orchard.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Diana and George. The bet was
simple: predict what `'goose` would return. Diana,
with hands itching to count more, was certain about the answer. George asked
her, untroubled by what others thought, to actually write the form into the
REPL — the quoted symbol 'goose would be settled the moment the runtime
answered, not before.

What Clojure form computes the value of 'goose? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"'goose"}}]}
```

### G1-09 sample 4/N (form: `(= 'goose 'goose)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

At a small stall inside a cottage, someone had chalked a wager: whoever
predicted the result of `(= 'goose 'goose)` first would set the asking
price for the morning's eggs. Charlie, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the equality of two 'goose symbols — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for whether 'goose equals 'goose.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'goose 'goose)"}}]}
```

### G1-09 sample 5/N (form: `(symbol? 'goose)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Halfway through the morning errand, George stopped at the edge of the orchard
with a basket of eggs and refused to move on until someone could
prove what the form `(symbol? 'goose)` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit the predicate (symbol? 'goose) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives whether 'goose is a symbol.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'goose)"}}]}
```

## G1-10: Comments

**examples (2):**

- ex0: form=`(+ 1 2) ; sum of one and two` expected=`3`
    concept_phrase: `the form (+ 1 2) followed by a comment`
    question_what: `the result of (+ 1 2) ignoring the comment`
- ex1: form=`42 ;; the answer` expected=`42`
    concept_phrase: `the literal 42 with a trailing comment`
    question_what: `the value of 42`

### G1-10 sample 1/N (form: `(+ 1 2) ; sum of one and two`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 1 2) ; sum of one and two`.
Fiona laughed, boasting at every turn, and declared it too easy.
Alex said, stepping deliberately, that the only honest way to know
the form (+ 1 2) followed by a comment was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 sample 2/N (form: `42 ;; the answer`, expected: `42`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Morgan offered a small basket of eggs as a wager in the barn:
whoever guessed the result of `42 ;; the answer` first would keep them.
Bob, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the literal 42 with a trailing comment; the eggs,
after all, would still be there once Honk the goose laid the next
one.

What Clojure form computes the value of 42? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### G1-10 sample 3/N (form: `(+ 1 2) ; sum of one and two`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

A small audience of neighbors had gathered in the orchard to watch
Emily attempt to outguess Carol at reading the
REPL. Carol pointed to the form (+ 1 2) followed by a comment and read out the form
aloud: `(+ 1 2) ; sum of one and two`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the result of (+ 1 2) ignoring the comment.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 sample 4/N (form: `42 ;; the answer`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Grace had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the village, the
next entry was the literal 42 with a trailing comment. Robin peered over
her shoulder at the form `42 ;; the answer` and asked what
it would come out to.

Write a form whose evaluation gives the value of 42.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### G1-10 sample 5/N (form: `(+ 1 2) ; sum of one and two`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(+ 1 2) ; sum of one and two` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the form (+ 1 2) followed by a comment; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the result of (+ 1 2) ignoring the comment.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

## G1-11: Whitespace doesn't matter

**examples (2):**

- ex0: form=`(+    1    2)` expected=`3`
    concept_phrase: `the form (+ 1 2) with extra spaces`
    question_what: `the result of the form`
- ex1: form=`(+
  1
  2)` expected=`3`
    concept_phrase: `the form (+ 1 2) split across lines`
    question_what: `the result of the form`

### G1-11 sample 1/N (form: `(+    1    2)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(+    1    2)` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (+ 1 2) with extra spaces — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the result of the form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 sample 2/N (form: `(+
  1
  2)`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Edward had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to the form (+ 1 2) split across lines.
"You hand the form `(+
  1
  2)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the result of the form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### G1-11 sample 3/N (form: `(+    1    2)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Grace and Charlie stood by the orchard where someone had
scratched the form (+ 1 2) with extra spaces into a smooth slate by the egg-basket.
Charlie, with great whoops of laughter, declared the answer was obvious — no need to
evaluate anything. Grace, untroubled by what others thought, suggested they
actually submit the form `(+    1    2)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the result of the form.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 sample 4/N (form: `(+
  1
  2)`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

A row of three coins sat on the kitchen table by the village, set out as a
wager between Sam and Oliver. The bet was
simple: predict what `(+
  1
  2)` would return. Sam,
with hands itching to count more, was certain about the answer. Oliver asked
them, her eyes always on the path, to actually write the form into the
REPL — the form (+ 1 2) split across lines would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the result of the form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### G1-11 sample 5/N (form: `(+    1    2)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today deep inside the kitchen, the
next entry was the form (+ 1 2) with extra spaces. Sam peered over
her shoulder at the form `(+    1    2)` and asked what
it would come out to.

Write a form whose evaluation gives the result of the form.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

## G1-12: Parens group; they don't multiply

**examples (2):**

- ex0: form=`(+ 2 3)` expected=`5`
    concept_phrase: `the form (+ 2 3)`
    question_what: `the result of (+ 2 3)`
- ex1: form=`(* (+ 1 2) 3)` expected=`9`
    concept_phrase: `the form (* (+ 1 2) 3)`
    question_what: `the result of (* (+ 1 2) 3)`

### G1-12 sample 1/N (form: `(+ 2 3)`, expected: `5`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Fiona offered a small basket of eggs as a wager near the village:
whoever guessed the result of `(+ 2 3)` first would keep them.
Helen, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the form (+ 2 3); the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the result of (+ 2 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 sample 2/N (form: `(* (+ 1 2) 3)`, expected: `9`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(* (+ 1 2) 3)` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (* (+ 1 2) 3) — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the result of (* (+ 1 2) 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### G1-12 sample 3/N (form: `(+ 2 3)`, expected: `5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

Robin and Helen stood near the market where someone had
scratched the form (+ 2 3) into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Robin, without complaint, suggested they
actually submit the form `(+ 2 3)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Question: write a Clojure expression for the result of (+ 2 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 sample 4/N (form: `(* (+ 1 2) 3)`, expected: `9`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Morgan had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today inside the barn, the
next entry was the form (* (+ 1 2) 3). Sam peered over
their shoulder at the form `(* (+ 1 2) 3)` and asked what
it would come out to.

What Clojure form computes the result of (* (+ 1 2) 3)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### G1-12 sample 5/N (form: `(+ 2 3)`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post by the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 2 3)`.
Oliver laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, without complaint, that the only honest way to know
the form (+ 2 3) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the result of (+ 2 3)? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

## G1-13: First arithmetic call

**examples (6):**

- ex0: form=`(+ 1 2)` expected=`3`
    concept_phrase: `the form (+ 1 2)`
    question_what: `the result of (+ 1 2)`
- ex1: form=`(- 5 3)` expected=`2`
    concept_phrase: `the form (- 5 3)`
    question_what: `the result of (- 5 3)`
- ex2: form=`(* 4 5)` expected=`20`
    concept_phrase: `the form (* 4 5)`
    question_what: `the result of (* 4 5)`
- ex3: form=`(/ 10 2)` expected=`5`
    concept_phrase: `the form (/ 10 2)`
    question_what: `the result of (/ 10 2)`
- ex4: form=`(+ 7 8)` expected=`15`
    concept_phrase: `the form (+ 7 8)`
    question_what: `the result of (+ 7 8)`
- ex5: form=`(- 20 7)` expected=`13`
    concept_phrase: `the form (- 20 7)`
    question_what: `the result of (- 20 7)`

### G1-13 sample 1/N (form: `(+ 1 2)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Sam said, with great whoops of laughter.
"Anyone with eyes can see what the form (+ 1 2) comes to."
Alice, who at the edge of the market had grown used to such claims, asked
them to actually write the form `(+ 1 2)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the result of (+ 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 sample 2/N (form: `(- 5 3)`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

At a small stall in the meadow, someone had chalked a wager: whoever
predicted the result of `(- 5 3)` first would set the asking
price for the morning's eggs. Oliver, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the form (- 5 3) — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the result of (- 5 3).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(- 5 3)"}}]}
```

### G1-13 sample 3/N (form: `(* 4 5)`, expected: `20`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the market.

A small audience of neighbors had gathered by the market to watch
Henry attempt to outguess Casey at reading the
REPL. Casey pointed to the form (* 4 5) and read out the form
aloud: `(* 4 5)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the result of (* 4 5).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### G1-13 sample 4/N (form: `(/ 10 2)`, expected: `5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Alex said, boasting at every turn.
"Anyone with eyes can see what the form (/ 10 2) comes to."
Grace, who in the cellar had grown used to such claims, asked
them to actually write the form `(/ 10 2)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the result of (/ 10 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G1-13 sample 5/N (form: `(+ 7 8)`, expected: `15`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Sam offered a small basket of eggs as a wager near the farm:
whoever guessed the result of `(+ 7 8)` first would keep them.
Diana, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form (+ 7 8); the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a Clojure expression that computes the result of (+ 7 8).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 7 8)"}}]}
```

## G1-14: Nested call evaluation

**examples (4):**

- ex0: form=`(+ 1 (* 2 3))` expected=`7`
    concept_phrase: `the nested form (+ 1 (* 2 3))`
    question_what: `the result of (+ 1 (* 2 3))`
- ex1: form=`(* (+ 1 2) (+ 3 4))` expected=`21`
    concept_phrase: `the nested form (* (+ 1 2) (+ 3 4))`
    question_what: `the result of (* (+ 1 2) (+ 3 4))`
- ex2: form=`(- 100 (* 5 5))` expected=`75`
    concept_phrase: `the nested form (- 100 (* 5 5))`
    question_what: `the result of (- 100 (* 5 5))`
- ex3: form=`(+ (* 2 3) (* 4 5))` expected=`26`
    concept_phrase: `the sum of two products`
    question_what: `the result of (+ (* 2 3) (* 4 5))`

### G1-14 sample 1/N (form: `(+ 1 (* 2 3))`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

Halfway through the morning errand, Diana stopped by the village
with a basket of eggs and refused to move on until someone could
prove what the form `(+ 1 (* 2 3))` evaluated to. Diana called it
impossible. Grace, walking up at an unhurried pace, simply
said: "Submit the nested form (+ 1 (* 2 3)) to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 sample 2/N (form: `(* (+ 1 2) (+ 3 4))`, expected: `21`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Oliver stopped at the edge of the meadow
with a basket of eggs and refused to move on until someone could
prove what the form `(* (+ 1 2) (+ 3 4))` evaluated to. Oliver called it
impossible. Sam, walking up at an unhurried pace, simply
said: "Submit the nested form (* (+ 1 2) (+ 3 4)) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for the result of (* (+ 1 2) (+ 3 4)).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) (+ 3 4))"}}]}
```

### G1-14 sample 3/N (form: `(- 100 (* 5 5))`, expected: `75`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Bob stopped in the kitchen
with a basket of eggs and refused to move on until someone could
prove what the form `(- 100 (* 5 5))` evaluated to. Bob called it
impossible. Helen, walking up at an unhurried pace, simply
said: "Submit the nested form (- 100 (* 5 5)) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the result of (- 100 (* 5 5)).
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 (* 5 5))"}}]}
```

### G1-14 sample 4/N (form: `(+ (* 2 3) (* 4 5))`, expected: `26`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside the kitchen.

A small audience of neighbors had gathered inside the kitchen to watch
David attempt to outguess Oliver at reading the
REPL. Oliver pointed to the sum of two products and read out the form
aloud: `(+ (* 2 3) (* 4 5))`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the result of (+ (* 2 3) (* 4 5)).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 2 3) (* 4 5))"}}]}
```

### G1-14 sample 5/N (form: `(+ 1 (* 2 3))`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

Halfway through the morning errand, David stopped in the meadow
with a basket of eggs and refused to move on until someone could
prove what the form `(+ 1 (* 2 3))` evaluated to. David called it
impossible. Edward, walking up at an unhurried pace, simply
said: "Submit the nested form (+ 1 (* 2 3)) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for the result of (+ 1 (* 2 3)).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

## G1-15: Equality

**examples (6):**

- ex0: form=`(= 1 1)` expected=`True`
    concept_phrase: `the equality (= 1 1)`
    question_what: `the value of (= 1 1)`
- ex1: form=`(= 1 2)` expected=`False`
    concept_phrase: `the equality (= 1 2)`
    question_what: `the value of (= 1 2)`
- ex2: form=`(= "a" "a")` expected=`True`
    concept_phrase: `the equality (= "a" "a")`
    question_what: `the value of (= "a" "a")`
- ex3: form=`(= :gold :gold)` expected=`True`
    concept_phrase: `the equality (= :gold :gold)`
    question_what: `the value of (= :gold :gold)`
- ex4: form=`(= :gold :silver)` expected=`False`
    concept_phrase: `the equality (= :gold :silver)`
    question_what: `the value of (= :gold :silver)`
- ex5: form=`(= 1 1 1 1)` expected=`True`
    concept_phrase: `the multi-arg equality (= 1 1 1 1)`
    question_what: `the value of (= 1 1 1 1)`

### G1-15 sample 1/N (form: `(= 1 1)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

A row of three coins sat on the kitchen table by the village, set out as a
wager between Emily and Robin. The bet was
simple: predict what `(= 1 1)` would return. Emily,
with hands itching to count more, was certain about the answer. Robin asked
her, saying very little, to actually write the form into the
REPL — the equality (= 1 1) would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes the value of (= 1 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 sample 2/N (form: `(= 1 2)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

Halfway through the morning errand, David stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(= 1 2)` evaluated to. David called it
impossible. Charlie, walking up at an unhurried pace, simply
said: "Submit the equality (= 1 2) to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the value of (= 1 2).
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### G1-15 sample 3/N (form: `(= "a" "a")`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the farm.

George and Morgan stood near the farm where someone had
scratched the equality (= "a" "a") into a smooth slate by the egg-basket.
Morgan, boasting at every turn, declared the answer was obvious — no need to
evaluate anything. George, without complaint, suggested they
actually submit the form `(= "a" "a")` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the value of (= "a" "a")? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= \"a\" \"a\")"}}]}
```

### G1-15 sample 4/N (form: `(= :gold :gold)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered near the meadow to watch
Oliver attempt to outguess Robin at reading the
REPL. Robin pointed to the equality (= :gold :gold) and read out the form
aloud: `(= :gold :gold)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

What Clojure form computes the value of (= :gold :gold)? Submit it via `eval`.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(= :gold :gold)"}}]}
```

### G1-15 sample 5/N (form: `(= :gold :silver)`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Diana and Robin. The bet was
simple: predict what `(= :gold :silver)` would return. Diana,
calculating in silence, was certain about the answer. Robin asked
her, stepping deliberately, to actually write the form into the
REPL — the equality (= :gold :silver) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of (= :gold :silver).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= :gold :silver)"}}]}
```

## G1-16: Numeric predicates

**examples (6):**

- ex0: form=`(zero? 0)` expected=`True`
    concept_phrase: `the predicate (zero? 0)`
    question_what: `whether 0 is zero`
- ex1: form=`(zero? 5)` expected=`False`
    concept_phrase: `the predicate (zero? 5)`
    question_what: `whether 5 is zero`
- ex2: form=`(pos? 7)` expected=`True`
    concept_phrase: `the predicate (pos? 7)`
    question_what: `whether 7 is positive`
- ex3: form=`(pos? -2)` expected=`False`
    concept_phrase: `the predicate (pos? -2)`
    question_what: `whether -2 is positive`
- ex4: form=`(neg? -3)` expected=`True`
    concept_phrase: `the predicate (neg? -3)`
    question_what: `whether -3 is negative`
- ex5: form=`(neg? 4)` expected=`False`
    concept_phrase: `the predicate (neg? 4)`
    question_what: `whether 4 is negative`

### G1-16 sample 1/N (form: `(zero? 0)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Sam stopped by the meadow
with a basket of eggs and refused to move on until someone could
prove what the form `(zero? 0)` evaluated to. Sam called it
impossible. Alice, walking up at an unhurried pace, simply
said: "Submit the predicate (zero? 0) to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a form whose evaluation gives whether 0 is zero.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 sample 2/N (form: `(zero? 5)`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(zero? 5)` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — the predicate (zero? 5) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for whether 5 is zero.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(zero? 5)"}}]}
```

### G1-16 sample 3/N (form: `(pos? 7)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Morgan stopped in the market
with a basket of eggs and refused to move on until someone could
prove what the form `(pos? 7)` evaluated to. Morgan called it
impossible. Sam, walking up at an unhurried pace, simply
said: "Submit the predicate (pos? 7) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Question: write a Clojure expression for whether 7 is positive.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? 7)"}}]}
```

### G1-16 sample 4/N (form: `(pos? -2)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Sam offered a small basket of eggs as a wager in the market:
whoever guessed the result of `(pos? -2)` first would keep them.
Casey, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the predicate (pos? -2); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for whether -2 is positive.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(pos? -2)"}}]}
```

### G1-16 sample 5/N (form: `(neg? -3)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

Emily had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today inside the cellar, the
next entry was the predicate (neg? -3). George peered over
her shoulder at the form `(neg? -3)` and asked what
it would come out to.

Question: write a Clojure expression for whether -3 is negative.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(neg? -3)"}}]}
```

## G1-17: Printing vs returning

**examples (2):**

- ex0: form=`42` expected=`42`
    concept_phrase: `the value 42`
    question_what: `the value of 42`
- ex1: form=`(+ 1 2)` expected=`3`
    concept_phrase: `the form (+ 1 2)`
    question_what: `the result of (+ 1 2)`

### G1-17 sample 1/N (form: `42`, expected: `42`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the kitchen, the
next entry was the value 42. Grace peered over
his shoulder at the form `42` and asked what
it would come out to.

Write a Clojure expression that computes the value of 42.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 sample 2/N (form: `(+ 1 2)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post in the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 1 2)`.
Alex laughed, as if the race were already won, and declared it too easy.
Fiona said, untroubled by what others thought, that the only honest way to know
the form (+ 1 2) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the result of (+ 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-17 sample 3/N (form: `42`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched the value 42 into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `42` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the value of 42.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 sample 4/N (form: `(+ 1 2)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 1 2)`.
Carol laughed, as if the race were already won, and declared it too easy.
Alex said, her eyes always on the path, that the only honest way to know
the form (+ 1 2) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the result of (+ 1 2).
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-17 sample 5/N (form: `42`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Emily stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `42` evaluated to. Emily called it
impossible. Carol, walking up at an unhurried pace, simply
said: "Submit the value 42 to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of 42.
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

## G1-18: Errors are safe in the REPL

**examples (2):**

- ex0: form=`(+ 1 2)` expected=`3`
    concept_phrase: `the form (+ 1 2)`
    question_what: `the result of (+ 1 2)`
- ex1: form=`(* 7 6)` expected=`42`
    concept_phrase: `the form (* 7 6)`
    question_what: `the result of (* 7 6)`

### G1-18 sample 1/N (form: `(+ 1 2)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today inside the barn, the
next entry was the form (+ 1 2). Alice peered over
her shoulder at the form `(+ 1 2)` and asked what
it would come out to.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 sample 2/N (form: `(* 7 6)`, expected: `42`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table in the farm, set out as a
wager between Alice and Emily. The bet was
simple: predict what `(* 7 6)` would return. Alice,
eyeing the next morning's gift, was certain about the answer. Emily asked
her, stepping deliberately, to actually write the form into the
REPL — the form (* 7 6) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the result of (* 7 6).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### G1-18 sample 3/N (form: `(+ 1 2)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the form (+ 1 2) into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(+ 1 2)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the result of (+ 1 2).
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 sample 4/N (form: `(* 7 6)`, expected: `42`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place near the orchard.

Alex had been trying to teach Sam how the REPL
works. "Here," they said, pointing to the form (* 7 6).
"You hand the form `(* 7 6)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the result of (* 7 6).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### G1-18 sample 5/N (form: `(+ 1 2)`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in a cottage.

At a small stall deep inside a cottage, someone had chalked a wager: whoever
predicted the result of `(+ 1 2)` first would set the asking
price for the morning's eggs. Morgan, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (+ 1 2) — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the result of (+ 1 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

