# Grade 2 goose-eggs — deep spot-check

5 rendered records per subject (22 subjects × 5 = 110 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G2-01: Multi-arg arithmetic

**examples (6):**

- ex0: form=`(+ 1 2 3 4)` expected=`10`
    concept_phrase: `the sum (+ 1 2 3 4)`
    question_what: `the result of (+ 1 2 3 4)`
- ex1: form=`(* 2 3 4)` expected=`24`
    concept_phrase: `the product (* 2 3 4)`
    question_what: `the result of (* 2 3 4)`
- ex2: form=`(- 100 1 2 3)` expected=`94`
    concept_phrase: `the chain (- 100 1 2 3)`
    question_what: `the result of (- 100 1 2 3)`
- ex3: form=`(+ 1 2 3 4 5 6 7 8 9 10)` expected=`55`
    concept_phrase: `the sum 1+2+...+10`
    question_what: `the sum of integers 1 through 10`
- ex4: form=`(* 1 2 3 4 5)` expected=`120`
    concept_phrase: `the product 1*2*3*4*5`
    question_what: `the product of 1 through 5 (5!)`
- ex5: form=`(+ 10 20 30)` expected=`60`
    concept_phrase: `the sum (+ 10 20 30)`
    question_what: `the sum of 10, 20, and 30`

### G2-01 sample 1/N (form: `(+ 1 2 3 4)`, expected: `10`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Whatever `(+ 1 2 3 4)` comes to," Carol declared,
puffed up with pride, near the market, "I'll wager a basket of eggs I know it without
typing it." Alice, without complaint, picked up a piece of chalk
and drew the sum (+ 1 2 3 4) on the side of the egg-crate. "Then write
the form," she said. "The REPL will have the last word, the
way Plume the goose has the last word on the morning's count."

Write a Clojure expression that computes the result of (+ 1 2 3 4).
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-01 sample 2/N (form: `(* 2 3 4)`, expected: `24`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of small coins lay on the kitchen table at the edge of the farm, one for each
operand in the day's reckoning. Alice had written
`(* 2 3 4)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Frank pointed at the coins and
guessed loudly, calculating in silence, but Alice said the product (* 2 3 4) would
not be answered by guessing; the REPL would tell, calmly, the way
Quill the goose laid the next egg without rushing.

Question: write a Clojure expression for the result of (* 2 3 4).
---asst---
I let the REPL settle the chain one operator at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 3 4)"}}]}
```

### G2-01 sample 3/N (form: `(- 100 1 2 3)`, expected: `94`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(- 100 1 2 3)`.
Morgan laughed, puffed up with pride, and declared it too easy.
Robin said, with steady, careful steps, that the only honest way to know
the chain (- 100 1 2 3) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the result of (- 100 1 2 3)? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 1 2 3)"}}]}
```

### G2-01 sample 4/N (form: `(+ 1 2 3 4 5 6 7 8 9 10)`, expected: `55`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Whatever `(+ 1 2 3 4 5 6 7 8 9 10)` comes to," Robin declared,
as if the race were already won, deep inside the cellar, "I'll wager a basket of eggs I know it without
typing it." Frank, saying very little, picked up a piece of chalk
and drew the sum 1+2+...+10 on the side of the egg-crate. "Then write
the form," he said. "The REPL will have the last word, the
way Honk the goose has the last word on the morning's count."

Question: write a Clojure expression for the sum of integers 1 through 10.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4 5 6 7 8 9 10)"}}]}
```

### G2-01 sample 5/N (form: `(* 1 2 3 4 5)`, expected: `120`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table in the kitchen, set out as a
wager between Alice and Charlie. The bet was
simple: predict what `(* 1 2 3 4 5)` would return. Alice,
with hands itching to count more, was certain about the answer. Charlie asked
her, with steady, careful steps, to actually write the form into the
REPL — the product 1*2*3*4*5 would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the product of 1 through 5 (5!).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 1 2 3 4 5)"}}]}
```

## G2-02: Comparison chains

**examples (5):**

- ex0: form=`(< 1 2 3)` expected=`True`
    concept_phrase: `the chain (< 1 2 3)`
    question_what: `whether 1 < 2 < 3`
- ex1: form=`(< 3 2 1)` expected=`False`
    concept_phrase: `the chain (< 3 2 1)`
    question_what: `whether 3 < 2 < 1`
- ex2: form=`(<= 1 1 2)` expected=`True`
    concept_phrase: `the chain (<= 1 1 2)`
    question_what: `whether 1 ≤ 1 ≤ 2`
- ex3: form=`(> 5 4 3 2 1)` expected=`True`
    concept_phrase: `the chain (> 5 4 3 2 1)`
    question_what: `whether the numbers 5,4,3,2,1 are strictly decreasing`
- ex4: form=`(>= 3 3 2)` expected=`True`
    concept_phrase: `the chain (>= 3 3 2)`
    question_what: `whether 3 ≥ 3 ≥ 2`

### G2-02 sample 1/N (form: `(< 1 2 3)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what the chain (< 1 2 3) comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(< 1 2 3)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes whether 1 < 2 < 3.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-02 sample 2/N (form: `(< 3 2 1)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of small coins lay on the kitchen table at the edge of the village, one for each
operand in the day's reckoning. Oliver had written
`(< 3 2 1)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Frank pointed at the coins and
guessed loudly, with a hungry gleam in the eye, but Oliver said the chain (< 3 2 1) would
not be answered by guessing; the REPL would tell, calmly, the way
Quill the goose laid the next egg without rushing.

Write a Clojure expression that computes whether 3 < 2 < 1.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 2 1)"}}]}
```

### G2-02 sample 3/N (form: `(<= 1 1 2)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(<= 1 1 2)`.
Sam laughed, as if the race were already won, and declared it too easy.
Robin said, saying very little, that the only honest way to know
the chain (<= 1 1 2) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives whether 1 ≤ 1 ≤ 2.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(<= 1 1 2)"}}]}
```

### G2-02 sample 4/N (form: `(> 5 4 3 2 1)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened inside the barn.

A small audience of neighbors had gathered inside the barn to watch
Charlie attempt to outguess Sam at reading the
REPL. Sam pointed to the chain (> 5 4 3 2 1) and read out the form
aloud: `(> 5 4 3 2 1)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes whether the numbers 5,4,3,2,1 are strictly decreasing.
---asst---
I let the REPL settle the chain one operator at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(> 5 4 3 2 1)"}}]}
```

### G2-02 sample 5/N (form: `(>= 3 3 2)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Frank had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today deep inside the barn, the
next entry was the chain (>= 3 3 2). Beatrice peered over
his shoulder at the form `(>= 3 3 2)` and asked what
it would come out to.

Question: write a Clojure expression for whether 3 ≥ 3 ≥ 2.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(>= 3 3 2)"}}]}
```

## G2-03: not= and = with multiple args

**examples (5):**

- ex0: form=`(not= 1 2)` expected=`True`
    concept_phrase: `the form (not= 1 2)`
    question_what: `whether 1 differs from 2`
- ex1: form=`(not= 1 1)` expected=`False`
    concept_phrase: `the form (not= 1 1)`
    question_what: `whether 1 differs from 1`
- ex2: form=`(= 1 1 1)` expected=`True`
    concept_phrase: `the form (= 1 1 1)`
    question_what: `whether all of 1,1,1 are equal`
- ex3: form=`(= 1 1 2)` expected=`False`
    concept_phrase: `the form (= 1 1 2)`
    question_what: `whether 1,1,2 are all equal`
- ex4: form=`(not= 1 1 2)` expected=`True`
    concept_phrase: `the form (not= 1 1 2)`
    question_what: `whether at least one of 1,1,2 differs`

### G2-03 sample 1/N (form: `(not= 1 2)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(not= 1 2)` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — the form (not= 1 2) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for whether 1 differs from 2.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-03 sample 2/N (form: `(not= 1 1)`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(not= 1 1)` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form (not= 1 1); the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for whether 1 differs from 1.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1)"}}]}
```

### G2-03 sample 3/N (form: `(= 1 1 1)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Carol stopped inside the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(= 1 1 1)` evaluated to. Carol called it
impossible. Emily, walking up at an unhurried pace, simply
said: "Submit the form (= 1 1 1) to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for whether all of 1,1,1 are equal.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 1)"}}]}
```

### G2-03 sample 4/N (form: `(= 1 1 2)`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," David said, boasting at every turn.
"Anyone with eyes can see what the form (= 1 1 2) comes to."
Alex, who in the meadow had grown used to such claims, asked
him to actually write the form `(= 1 1 2)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives whether 1,1,2 are all equal.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1 2)"}}]}
```

### G2-03 sample 5/N (form: `(not= 1 1 2)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the village.

Henry offered a small basket of eggs as a wager near the village:
whoever guessed the result of `(not= 1 1 2)` first would keep them.
Casey, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the form (not= 1 1 2); the eggs,
after all, would still be there once Plume the goose laid the next
one.

What Clojure form computes whether at least one of 1,1,2 differs? Submit it via `eval`.
---asst---
I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 1 2)"}}]}
```

## G2-04: min and max

**examples (5):**

- ex0: form=`(min 1 2 3)` expected=`1`
    concept_phrase: `the form (min 1 2 3)`
    question_what: `the minimum of 1, 2, 3`
- ex1: form=`(max 1 2 3)` expected=`3`
    concept_phrase: `the form (max 1 2 3)`
    question_what: `the maximum of 1, 2, 3`
- ex2: form=`(min 7 3 9 1 5)` expected=`1`
    concept_phrase: `the form (min 7 3 9 1 5)`
    question_what: `the minimum of 7, 3, 9, 1, 5`
- ex3: form=`(max 7 3 9 1 5)` expected=`9`
    concept_phrase: `the form (max 7 3 9 1 5)`
    question_what: `the maximum of 7, 3, 9, 1, 5`
- ex4: form=`(min -3 -1 -5)` expected=`-5`
    concept_phrase: `the form (min -3 -1 -5)`
    question_what: `the minimum of -3, -1, -5`

### G2-04 sample 1/N (form: `(min 1 2 3)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to the form (min 1 2 3).
"You hand the form `(min 1 2 3)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the minimum of 1, 2, 3.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-04 sample 2/N (form: `(max 1 2 3)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

A small audience of neighbors had gathered in the orchard to watch
Bob attempt to outguess Grace at reading the
REPL. Grace pointed to the form (max 1 2 3) and read out the form
aloud: `(max 1 2 3)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the maximum of 1, 2, 3.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(max 1 2 3)"}}]}
```

### G2-04 sample 3/N (form: `(min 7 3 9 1 5)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," David said, boasting at every turn.
"Anyone with eyes can see what the form (min 7 3 9 1 5) comes to."
Alice, who by the market had grown used to such claims, asked
him to actually write the form `(min 7 3 9 1 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the minimum of 7, 3, 9, 1, 5.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(min 7 3 9 1 5)"}}]}
```

### G2-04 sample 4/N (form: `(max 7 3 9 1 5)`, expected: `9`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

A small wooden notice nailed to a post near the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(max 7 3 9 1 5)`.
George laughed, puffed up with pride, and declared it too easy.
David said, untroubled by what others thought, that the only honest way to know
the form (max 7 3 9 1 5) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the maximum of 7, 3, 9, 1, 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(max 7 3 9 1 5)"}}]}
```

### G2-04 sample 5/N (form: `(min -3 -1 -5)`, expected: `-5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Morgan had been laying out a chain of small computations on a
slate in the village — one operation, then another, all to settle a question
Emily had raised about the morning's eggs. The current form
on the slate was `(min -3 -1 -5)`, and Morgan explained, untroubled by what others thought,
that the form (min -3 -1 -5) would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for the minimum of -3, -1, -5.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(min -3 -1 -5)"}}]}
```

## G2-05: quot, rem, mod

**examples (6):**

- ex0: form=`(quot 17 5)` expected=`3`
    concept_phrase: `the integer quotient of 17 and 5`
    question_what: `the result of (quot 17 5)`
- ex1: form=`(rem 17 5)` expected=`2`
    concept_phrase: `the remainder of 17 divided by 5`
    question_what: `the result of (rem 17 5)`
- ex2: form=`(mod 17 5)` expected=`2`
    concept_phrase: `17 mod 5`
    question_what: `the result of (mod 17 5)`
- ex3: form=`(quot 100 7)` expected=`14`
    concept_phrase: `the integer quotient of 100 and 7`
    question_what: `the result of (quot 100 7)`
- ex4: form=`(rem 100 7)` expected=`2`
    concept_phrase: `the remainder of 100 divided by 7`
    question_what: `the result of (rem 100 7)`
- ex5: form=`(mod -7 3)` expected=`2`
    concept_phrase: `the form (mod -7 3)`
    question_what: `the result of (mod -7 3)`

### G2-05 sample 1/N (form: `(quot 17 5)`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(quot 17 5)` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the integer quotient of 17 and 5 to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the result of (quot 17 5).
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-05 sample 2/N (form: `(rem 17 5)`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Charlie had been laying out a chain of small computations on a
slate near the market — one operation, then another, all to settle a question
Beatrice had raised about the morning's eggs. The current form
on the slate was `(rem 17 5)`, and Charlie explained, with steady, careful steps,
that the remainder of 17 divided by 5 would be settled the moment the form was handed
to the REPL — the way Quill the goose settled each morning's tally with
one egg, no more, no less.

Write a form whose evaluation gives the result of (rem 17 5).
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(rem 17 5)"}}]}
```

### G2-05 sample 3/N (form: `(mod 17 5)`, expected: `2`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob offered a small basket of eggs as a wager near the farm:
whoever guessed the result of `(mod 17 5)` first would keep them.
Frank, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about 17 mod 5; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the result of (mod 17 5).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(mod 17 5)"}}]}
```

### G2-05 sample 4/N (form: `(quot 100 7)`, expected: `14`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(quot 100 7)`.
Fiona laughed, puffed up with pride, and declared it too easy.
Sam said, with steady, careful steps, that the only honest way to know
the integer quotient of 100 and 7 was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the result of (quot 100 7).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(quot 100 7)"}}]}
```

### G2-05 sample 5/N (form: `(rem 100 7)`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place by the market.

Alice had been trying to teach Carol how the REPL
works. "Here," she said, pointing to the remainder of 100 divided by 7.
"You hand the form `(rem 100 7)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the result of (rem 100 7).
---asst---
I let the REPL settle the chain one operator at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(rem 100 7)"}}]}
```

## G2-06: inc and dec

**examples (5):**

- ex0: form=`(inc 5)` expected=`6`
    concept_phrase: `the form (inc 5)`
    question_what: `5 plus 1`
- ex1: form=`(dec 5)` expected=`4`
    concept_phrase: `the form (dec 5)`
    question_what: `5 minus 1`
- ex2: form=`(inc 0)` expected=`1`
    concept_phrase: `the form (inc 0)`
    question_what: `the successor of 0`
- ex3: form=`(dec 0)` expected=`-1`
    concept_phrase: `the form (dec 0)`
    question_what: `the predecessor of 0`
- ex4: form=`(inc -1)` expected=`0`
    concept_phrase: `the form (inc -1)`
    question_what: `the successor of -1`

### G2-06 sample 1/N (form: `(inc 5)`, expected: `6`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what the form (inc 5) comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `(inc 5)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives 5 plus 1.
---asst---
I submit the whole form and let the runtime reduce it patiently, the way the goose lays one egg at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(inc 5)"}}]}
```

### G2-06 sample 2/N (form: `(dec 5)`, expected: `4`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of small coins lay on the kitchen table at the edge of the market, one for each
operand in the day's reckoning. Casey had written
`(dec 5)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Fiona pointed at the coins and
guessed loudly, imagining all that might be gained, but Casey said the form (dec 5) would
not be answered by guessing; the REPL would tell, calmly, the way
Plume the goose laid the next egg without rushing.

Question: write a Clojure expression for 5 minus 1.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(dec 5)"}}]}
```

### G2-06 sample 3/N (form: `(inc 0)`, expected: `1`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of small coins lay on the kitchen table inside the cellar, one for each
operand in the day's reckoning. Alice had written
`(inc 0)` at the top of the ledger — the next entry, just below
yesterday's egg-count. George pointed at the coins and
guessed loudly, imagining all that might be gained, but Alice said the form (inc 0) would
not be answered by guessing; the REPL would tell, calmly, the way
Plume the goose laid the next egg without rushing.

Write a form whose evaluation gives the successor of 0.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(inc 0)"}}]}
```

### G2-06 sample 4/N (form: `(dec 0)`, expected: `-1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Fiona had been trying to teach Grace how the REPL
works. "Here," she said, pointing to the form (dec 0).
"You hand the form `(dec 0)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the predecessor of 0.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(dec 0)"}}]}
```

### G2-06 sample 5/N (form: `(inc -1)`, expected: `0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Frank stopped by the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(inc -1)` evaluated to. Frank called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the form (inc -1) to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the successor of -1.
---asst---
I let the runtime hand back one value, the way the goose gives one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(inc -1)"}}]}
```

## G2-07: Absolute value

**examples (4):**

- ex0: form=`(abs 5)` expected=`5`
    concept_phrase: `the form (abs 5)`
    question_what: `the absolute value of 5`
- ex1: form=`(abs -5)` expected=`5`
    concept_phrase: `the form (abs -5)`
    question_what: `the absolute value of -5`
- ex2: form=`(abs 0)` expected=`0`
    concept_phrase: `the form (abs 0)`
    question_what: `the absolute value of 0`
- ex3: form=`(abs (- 3 8))` expected=`5`
    concept_phrase: `the form (abs (- 3 8))`
    question_what: `the absolute value of 3 minus 8`

### G2-07 sample 1/N (form: `(abs 5)`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David had been laying out a chain of small computations on a
slate by the market — one operation, then another, all to settle a question
Robin had raised about the morning's eggs. The current form
on the slate was `(abs 5)`, and David explained, her eyes always on the path,
that the form (abs 5) would be settled the moment the form was handed
to the REPL — the way Quill the goose settled each morning's tally with
one egg, no more, no less.

What Clojure form computes the absolute value of 5? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

### G2-07 sample 2/N (form: `(abs -5)`, expected: `5`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

"Whatever `(abs -5)` comes to," Edward declared,
boasting at every turn, deep inside the kitchen, "I'll wager a basket of eggs I know it without
typing it." David, her eyes always on the path, picked up a piece of chalk
and drew the form (abs -5) on the side of the egg-crate. "Then write
the form," he said. "The REPL will have the last word, the
way Plume the goose has the last word on the morning's count."

What Clojure form computes the absolute value of -5? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(abs -5)"}}]}
```

### G2-07 sample 3/N (form: `(abs 0)`, expected: `0`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered deep inside the cellar to watch
Beatrice attempt to outguess Henry at reading the
REPL. Henry pointed to the form (abs 0) and read out the form
aloud: `(abs 0)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

What Clojure form computes the absolute value of 0? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(abs 0)"}}]}
```

### G2-07 sample 4/N (form: `(abs (- 3 8))`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Jordan had been laying out a chain of small computations on a
slate inside a cottage — one operation, then another, all to settle a question
Grace had raised about the morning's eggs. The current form
on the slate was `(abs (- 3 8))`, and Jordan explained, with steady, careful steps,
that the form (abs (- 3 8)) would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for the absolute value of 3 minus 8.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(abs (- 3 8))"}}]}
```

### G2-07 sample 5/N (form: `(abs 5)`, expected: `5`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of small coins lay on the kitchen table deep inside the cellar, one for each
operand in the day's reckoning. Fiona had written
`(abs 5)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Sam pointed at the coins and
guessed loudly, with a glint of impatience, but Fiona said the form (abs 5) would
not be answered by guessing; the REPL would tell, calmly, the way
Plume the goose laid the next egg without rushing.

What Clojure form computes the absolute value of 5? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

## G2-08: Arithmetic on ratios

**examples (3):**

- ex0: form=`(+ 1/2 1/4)` expected=`'3/4'`
    concept_phrase: `the sum 1/2 + 1/4`
    question_what: `the value of (+ 1/2 1/4)`
- ex1: form=`(* 2/3 3/4)` expected=`'1/2'`
    concept_phrase: `the product 2/3 × 3/4`
    question_what: `the value of (* 2/3 3/4)`
- ex2: form=`(- 1 1/3)` expected=`'2/3'`
    concept_phrase: `1 minus 1/3`
    question_what: `the value of (- 1 1/3)`

### G2-08 sample 1/N (form: `(+ 1/2 1/4)`, expected: `'3/4'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

"Whatever `(+ 1/2 1/4)` comes to," Oliver declared,
with a smug grin, in the village, "I'll wager a basket of eggs I know it without
typing it." Bob, stepping deliberately, picked up a piece of chalk
and drew the sum 1/2 + 1/4 on the side of the egg-crate. "Then write
the form," he said. "The REPL will have the last word, the
way Plume the goose has the last word on the morning's count."

Write a form whose evaluation gives the value of (+ 1/2 1/4).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 sample 2/N (form: `(* 2/3 3/4)`, expected: `'1/2'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(* 2/3 3/4)` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit the product 2/3 × 3/4 to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of (* 2/3 3/4).
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

### G2-08 sample 3/N (form: `(- 1 1/3)`, expected: `'2/3'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall deep inside the cellar, someone had chalked a wager: whoever
predicted the result of `(- 1 1/3)` first would set the asking
price for the morning's eggs. David, her eyes always on the path, said it
was easier to type the form into the REPL than to argue about
1 minus 1/3 — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the value of (- 1 1/3).
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

### G2-08 sample 4/N (form: `(+ 1/2 1/4)`, expected: `'3/4'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(+ 1/2 1/4)` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — the sum 1/2 + 1/4 would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of (+ 1/2 1/4).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-08 sample 5/N (form: `(* 2/3 3/4)`, expected: `'1/2'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

George had been laying out a chain of small computations on a
slate deep inside the cellar — one operation, then another, all to settle a question
Casey had raised about the morning's eggs. The current form
on the slate was `(* 2/3 3/4)`, and George explained, stepping deliberately,
that the product 2/3 × 3/4 would be settled the moment the form was handed
to the REPL — the way Honk the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for the value of (* 2/3 3/4).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2/3 3/4)"}}]}
```

## G2-09: Floats vs ints (the / operator)

**examples (3):**

- ex0: form=`(/ 10 2)` expected=`5`
    concept_phrase: `the integer division 10 ÷ 2`
    question_what: `the value of (/ 10 2)`
- ex1: form=`(/ 10 3)` expected=`'10/3'`
    concept_phrase: `the form (/ 10 3)`
    question_what: `the exact rational result of (/ 10 3)`
- ex2: form=`(/ 1.0 2)` expected=`0.5`
    concept_phrase: `the float division 1.0 ÷ 2`
    question_what: `the value of (/ 1.0 2)`

### G2-09 sample 1/N (form: `(/ 10 2)`, expected: `5`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was the integer division 10 ÷ 2. George peered over
his shoulder at the form `(/ 10 2)` and asked what
it would come out to.

Write a Clojure expression that computes the value of (/ 10 2).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 sample 2/N (form: `(/ 10 3)`, expected: `'10/3'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the barn to watch
David attempt to outguess Fiona at reading the
REPL. Fiona pointed to the form (/ 10 3) and read out the form
aloud: `(/ 10 3)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the exact rational result of (/ 10 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

### G2-09 sample 3/N (form: `(/ 1.0 2)`, expected: `0.5`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place by the orchard.

Diana offered a small basket of eggs as a wager at the edge of the orchard:
whoever guessed the result of `(/ 1.0 2)` first would keep them.
George, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about the float division 1.0 ÷ 2; the eggs,
after all, would still be there once Quill the goose laid the next
one.

What Clojure form computes the value of (/ 1.0 2)? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 1.0 2)"}}]}
```

### G2-09 sample 4/N (form: `(/ 10 2)`, expected: `5`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was the integer division 10 ÷ 2. George peered over
their shoulder at the form `(/ 10 2)` and asked what
it would come out to.

Write a form whose evaluation gives the value of (/ 10 2).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-09 sample 5/N (form: `(/ 10 3)`, expected: `'10/3'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered inside a cottage to watch
Jordan attempt to outguess Charlie at reading the
REPL. Charlie pointed to the form (/ 10 3) and read out the form
aloud: `(/ 10 3)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the exact rational result of (/ 10 3).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 3)"}}]}
```

## G2-10: Powers via repeated multiplication

**examples (4):**

- ex0: form=`(* 2 2 2)` expected=`8`
    concept_phrase: `two cubed`
    question_what: `2 to the third power`
- ex1: form=`(* 5 5)` expected=`25`
    concept_phrase: `five squared`
    question_what: `5 squared`
- ex2: form=`(* 3 3 3 3)` expected=`81`
    concept_phrase: `three to the fourth`
    question_what: `3 to the fourth power`
- ex3: form=`(* 10 10)` expected=`100`
    concept_phrase: `ten squared`
    question_what: `10 squared`

### G2-10 sample 1/N (form: `(* 2 2 2)`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A row of small coins lay on the kitchen table deep inside the kitchen, one for each
operand in the day's reckoning. Alex had written
`(* 2 2 2)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Fiona pointed at the coins and
guessed loudly, with hands itching to count more, but Alex said two cubed would
not be answered by guessing; the REPL would tell, calmly, the way
Honk the goose laid the next egg without rushing.

Write a Clojure expression that computes 2 to the third power.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-10 sample 2/N (form: `(* 5 5)`, expected: `25`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to five squared.
"You hand the form `(* 5 5)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes 5 squared? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 5 5)"}}]}
```

### G2-10 sample 3/N (form: `(* 3 3 3 3)`, expected: `81`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place in the barn.

Frank had been laying out a chain of small computations on a
slate inside the barn — one operation, then another, all to settle a question
David had raised about the morning's eggs. The current form
on the slate was `(* 3 3 3 3)`, and Frank explained, without complaint,
that three to the fourth would be settled the moment the form was handed
to the REPL — the way Honk the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for 3 to the fourth power.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 3 3 3 3)"}}]}
```

### G2-10 sample 4/N (form: `(* 10 10)`, expected: `100`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

Alice had been laying out a chain of small computations on a
slate at the edge of the village — one operation, then another, all to settle a question
Grace had raised about the morning's eggs. The current form
on the slate was `(* 10 10)`, and Alice explained, with steady, careful steps,
that ten squared would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for 10 squared.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(* 10 10)"}}]}
```

### G2-10 sample 5/N (form: `(* 2 2 2)`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was two cubed. Emily peered over
her shoulder at the form `(* 2 2 2)` and asked what
it would come out to.

Write a form whose evaluation gives 2 to the third power.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

## G2-11: String concatenation with str

**examples (4):**

- ex0: form=`(str "tor" "toise")` expected=`'tortoise'`
    concept_phrase: `the form (str "tor" "toise")`
    question_what: `the joined string "tortoise"`
- ex1: form=`(str "race")` expected=`'race'`
    concept_phrase: `the form (str "race")`
    question_what: `the value of (str "race")`
- ex2: form=`(str "x" "y" "z")` expected=`'xyz'`
    concept_phrase: `the form (str "x" "y" "z")`
    question_what: `the joined string "xyz"`
- ex3: form=`(str 1 "+" 2 "=" 3)` expected=`'1+2=3'`
    concept_phrase: `the form (str 1 "+" 2 "=" 3)`
    question_what: `the joined string "1+2=3"`

### G2-11 sample 1/N (form: `(str "tor" "toise")`, expected: `'tortoise'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(str "tor" "toise")` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (str "tor" "toise") — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the joined string "tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(str \"tor\" \"toise\")"}}]}
```

### G2-11 sample 2/N (form: `(str "race")`, expected: `'race'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to the form (str "race") and read out the form
aloud: `(str "race")`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the value of (str "race").
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(str \"race\")"}}]}
```

### G2-11 sample 3/N (form: `(str "x" "y" "z")`, expected: `'xyz'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Oliver had been trying to teach Charlie how the REPL
works. "Here," he said, pointing to the form (str "x" "y" "z").
"You hand the form `(str "x" "y" "z")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the joined string "xyz".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"x\" \"y\" \"z\")"}}]}
```

### G2-11 sample 4/N (form: `(str 1 "+" 2 "=" 3)`, expected: `'1+2=3'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was inside a cottage.

Grace and George stood in a cottage where someone had
scratched the form (str 1 "+" 2 "=" 3) into a smooth slate by the egg-basket.
George, boasting at every turn, declared the answer was obvious — no need to
evaluate anything. Grace, stepping deliberately, suggested they
actually submit the form `(str 1 "+" 2 "=" 3)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the joined string "1+2=3".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(str 1 \"+\" 2 \"=\" 3)"}}]}
```

### G2-11 sample 5/N (form: `(str "tor" "toise")`, expected: `'tortoise'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(str "tor" "toise")` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the form (str "tor" "toise") — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the joined string "tortoise".
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"tor\" \"toise\")"}}]}
```

## G2-12: print and println — return values

**examples (2):**

- ex0: form=`(println "hello")` expected=`None`
    concept_phrase: `the form (println "hello")`
    question_what: `the return value of (println "hello") (it is nil)`
- ex1: form=`(print "x")` expected=`None`
    concept_phrase: `the form (print "x")`
    question_what: `the return value of (print "x") (it is nil)`

### G2-12 sample 1/N (form: `(println "hello")`, expected: `None`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to the form (println "hello").
"You hand the form `(println "hello")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the return value of (println "hello") (it is nil).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### G2-12 sample 2/N (form: `(print "x")`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(print "x")` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the form (print "x") — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the return value of (print "x") (it is nil).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### G2-12 sample 3/N (form: `(println "hello")`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(println "hello")` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the form (println "hello") — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the return value of (println "hello") (it is nil).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### G2-12 sample 4/N (form: `(print "x")`, expected: `None`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(print "x")`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
the form (print "x") was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the return value of (print "x") (it is nil)? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(print \"x\")"}}]}
```

### G2-12 sample 5/N (form: `(println "hello")`, expected: `None`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of small coins lay on the kitchen table by the meadow, one for each
operand in the day's reckoning. Morgan had written
`(println "hello")` at the top of the ledger — the next entry, just below
yesterday's egg-count. Oliver pointed at the coins and
guessed loudly, imagining all that might be gained, but Morgan said the form (println "hello") would
not be answered by guessing; the REPL would tell, calmly, the way
Quill the goose laid the next egg without rushing.

What Clojure form computes the return value of (println "hello") (it is nil)? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

## G2-13: and / or — short circuit, return values

**examples (6):**

- ex0: form=`(and true true)` expected=`True`
    concept_phrase: `the form (and true true)`
    question_what: `the value of (and true true)`
- ex1: form=`(and true false)` expected=`False`
    concept_phrase: `the form (and true false)`
    question_what: `the value of (and true false)`
- ex2: form=`(or false true)` expected=`True`
    concept_phrase: `the form (or false true)`
    question_what: `the value of (or false true)`
- ex3: form=`(or false false)` expected=`False`
    concept_phrase: `the form (or false false)`
    question_what: `the value of (or false false)`
- ex4: form=`(and 1 2 3)` expected=`3`
    concept_phrase: `the form (and 1 2 3)`
    question_what: `the value of (and 1 2 3)`
- ex5: form=`(or nil false 5)` expected=`5`
    concept_phrase: `the form (or nil false 5)`
    question_what: `the value of (or nil false 5)`

### G2-13 sample 1/N (form: `(and true true)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice had been laying out a chain of small computations on a
slate at the edge of the market — one operation, then another, all to settle a question
Sam had raised about the morning's eggs. The current form
on the slate was `(and true true)`, and Alice explained, untroubled by what others thought,
that the form (and true true) would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

Write a form whose evaluation gives the value of (and true true).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
```

### G2-13 sample 2/N (form: `(and true false)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `(and true false)` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — the form (and true false) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of (and true false).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(and true false)"}}]}
```

### G2-13 sample 3/N (form: `(or false true)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the market.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today by the market, the
next entry was the form (or false true). Henry peered over
their shoulder at the form `(or false true)` and asked what
it would come out to.

Write a form whose evaluation gives the value of (or false true).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(or false true)"}}]}
```

### G2-13 sample 4/N (form: `(or false false)`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"Whatever `(or false false)` comes to," Alex declared,
boasting at every turn, in the cellar, "I'll wager a basket of eggs I know it without
typing it." Grace, with steady, careful steps, picked up a piece of chalk
and drew the form (or false false) on the side of the egg-crate. "Then write
the form," she said. "The REPL will have the last word, the
way Quill the goose has the last word on the morning's count."

Write a form whose evaluation gives the value of (or false false).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(or false false)"}}]}
```

### G2-13 sample 5/N (form: `(and 1 2 3)`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Diana had been trying to teach Sam how the REPL
works. "Here," she said, pointing to the form (and 1 2 3).
"You hand the form `(and 1 2 3)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value of (and 1 2 3).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

## G2-14: not — turning truthy to false

**examples (5):**

- ex0: form=`(not true)` expected=`False`
    concept_phrase: `the form (not true)`
    question_what: `the value of (not true)`
- ex1: form=`(not false)` expected=`True`
    concept_phrase: `the form (not false)`
    question_what: `the value of (not false)`
- ex2: form=`(not nil)` expected=`True`
    concept_phrase: `the form (not nil)`
    question_what: `the value of (not nil)`
- ex3: form=`(not 0)` expected=`False`
    concept_phrase: `the form (not 0)`
    question_what: `the value of (not 0)`
- ex4: form=`(not "")` expected=`False`
    concept_phrase: `the form (not "")`
    question_what: `the value of (not "")`

### G2-14 sample 1/N (form: `(not true)`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what the form (not true) comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(not true)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of (not true).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-14 sample 2/N (form: `(not false)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward had been laying out a chain of small computations on a
slate in the market — one operation, then another, all to settle a question
George had raised about the morning's eggs. The current form
on the slate was `(not false)`, and Edward explained, saying very little,
that the form (not false) would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

What Clojure form computes the value of (not false)? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(not false)"}}]}
```

### G2-14 sample 3/N (form: `(not nil)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"Whatever `(not nil)` comes to," George declared,
with a smug grin, in the barn, "I'll wager a basket of eggs I know it without
typing it." Alex, her eyes always on the path, picked up a piece of chalk
and drew the form (not nil) on the side of the egg-crate. "Then write
the form," they said. "The REPL will have the last word, the
way Honk the goose has the last word on the morning's count."

Question: write a Clojure expression for the value of (not nil).
---asst---
I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(not nil)"}}]}
```

### G2-14 sample 4/N (form: `(not 0)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened by the orchard.

Oliver and Fiona stood by the orchard where someone had
scratched the form (not 0) into a smooth slate by the egg-basket.
Fiona, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Oliver, without complaint, suggested they
actually submit the form `(not 0)` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

Write a Clojure expression that computes the value of (not 0).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(not 0)"}}]}
```

### G2-14 sample 5/N (form: `(not "")`, expected: `False`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Jordan offered a small basket of eggs as a wager near the orchard:
whoever guessed the result of `(not "")` first would keep them.
Alice, with steady, careful steps, said it would be simpler to type the
form into the REPL than to bicker about the form (not ""); the eggs,
after all, would still be there once Plume the goose laid the next
one.

What Clojure form computes the value of (not "")? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(not \"\")"}}]}
```

## G2-15: Falsey values: only false and nil

**examples (4):**

- ex0: form=`(if 0 :truthy :falsey)` expected=`':truthy'`
    concept_phrase: `the form (if 0 :truthy :falsey)`
    question_what: `which keyword (if 0 :truthy :falsey) returns`
- ex1: form=`(if "" :truthy :falsey)` expected=`':truthy'`
    concept_phrase: `the form (if "" :truthy :falsey)`
    question_what: `which keyword (if "" :truthy :falsey) returns`
- ex2: form=`(if nil :truthy :falsey)` expected=`':falsey'`
    concept_phrase: `the form (if nil :truthy :falsey)`
    question_what: `which keyword (if nil :truthy :falsey) returns`
- ex3: form=`(if false :truthy :falsey)` expected=`':falsey'`
    concept_phrase: `the form (if false :truthy :falsey)`
    question_what: `which keyword (if false :truthy :falsey) returns`

### G2-15 sample 1/N (form: `(if 0 :truthy :falsey)`, expected: `':truthy'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(if 0 :truthy :falsey)` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the form (if 0 :truthy :falsey); the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes which keyword (if 0 :truthy :falsey) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

### G2-15 sample 2/N (form: `(if "" :truthy :falsey)`, expected: `':truthy'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the form (if "" :truthy :falsey) comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(if "" :truthy :falsey)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for which keyword (if "" :truthy :falsey) returns.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if \"\" :truthy :falsey)"}}]}
```

### G2-15 sample 3/N (form: `(if nil :truthy :falsey)`, expected: `':falsey'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the farm.

George and Morgan stood near the farm where someone had
scratched the form (if nil :truthy :falsey) into a smooth slate by the egg-basket.
Morgan, boasting at every turn, declared the answer was obvious — no need to
evaluate anything. George, without complaint, suggested they
actually submit the form `(if nil :truthy :falsey)` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

What Clojure form computes which keyword (if nil :truthy :falsey) returns? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if nil :truthy :falsey)"}}]}
```

### G2-15 sample 4/N (form: `(if false :truthy :falsey)`, expected: `':falsey'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Oliver stopped near the meadow
with a basket of eggs and refused to move on until someone could
prove what the form `(if false :truthy :falsey)` evaluated to. Oliver called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit the form (if false :truthy :falsey) to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes which keyword (if false :truthy :falsey) returns? Submit it via `eval`.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(if false :truthy :falsey)"}}]}
```

### G2-15 sample 5/N (form: `(if 0 :truthy :falsey)`, expected: `':truthy'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what the form (if 0 :truthy :falsey) comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `(if 0 :truthy :falsey)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives which keyword (if 0 :truthy :falsey) returns.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

## G2-16: Truthy 0 and empty string

**examples (4):**

- ex0: form=`(boolean 0)` expected=`True`
    concept_phrase: `the form (boolean 0)`
    question_what: `the truthiness of 0`
- ex1: form=`(boolean "")` expected=`True`
    concept_phrase: `the form (boolean "")`
    question_what: `the truthiness of the empty string`
- ex2: form=`(boolean nil)` expected=`False`
    concept_phrase: `the form (boolean nil)`
    question_what: `the truthiness of nil`
- ex3: form=`(boolean false)` expected=`False`
    concept_phrase: `the form (boolean false)`
    question_what: `the truthiness of false`

### G2-16 sample 1/N (form: `(boolean 0)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what the form (boolean 0) comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `(boolean 0)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the truthiness of 0.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

### G2-16 sample 2/N (form: `(boolean "")`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(boolean "")` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — the form (boolean "") would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the truthiness of the empty string.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(boolean \"\")"}}]}
```

### G2-16 sample 3/N (form: `(boolean nil)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Morgan said, as if the race were already won.
"Anyone with eyes can see what the form (boolean nil) comes to."
Sam, who in the market had grown used to such claims, asked
them to actually write the form `(boolean nil)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the truthiness of nil.
---asst---
I let the REPL settle the chain one operator at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean nil)"}}]}
```

### G2-16 sample 4/N (form: `(boolean false)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Oliver and Morgan stood inside the barn where someone had
scratched the form (boolean false) into a smooth slate by the egg-basket.
Morgan, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Oliver, untroubled by what others thought, suggested they
actually submit the form `(boolean false)` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

Question: write a Clojure expression for the truthiness of false.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(boolean false)"}}]}
```

### G2-16 sample 5/N (form: `(boolean 0)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(boolean 0)` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — the form (boolean 0) would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the truthiness of 0.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

## G2-17: Keyword as function for map lookup

**examples (3):**

- ex0: form=`(:hare {:hare 1 :tortoise 2})` expected=`1`
    concept_phrase: `the form (:hare {:hare 1 :tortoise 2})`
    question_what: `the value (:hare {:hare 1 :tortoise 2}) returns`
- ex1: form=`(:tortoise {:hare 1 :tortoise 2})` expected=`2`
    concept_phrase: `the form (:tortoise {:hare 1 :tortoise 2})`
    question_what: `the value (:tortoise {:hare 1 :tortoise 2}) returns`
- ex2: form=`(:missing {:hare 1})` expected=`None`
    concept_phrase: `the form (:missing {:hare 1})`
    question_what: `the value when a missing keyword is looked up`

### G2-17 sample 1/N (form: `(:hare {:hare 1 :tortoise 2})`, expected: `1`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(:hare {:hare 1 :tortoise 2})`.
Grace laughed, boasting at every turn, and declared it too easy.
Oliver said, her eyes always on the path, that the only honest way to know
the form (:hare {:hare 1 :tortoise 2}) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value (:hare {:hare 1 :tortoise 2}) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
```

### G2-17 sample 2/N (form: `(:tortoise {:hare 1 :tortoise 2})`, expected: `2`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of small coins lay on the kitchen table in the village, one for each
operand in the day's reckoning. Fiona had written
`(:tortoise {:hare 1 :tortoise 2})` at the top of the ledger — the next entry, just below
yesterday's egg-count. Alex pointed at the coins and
guessed loudly, thoughts already on more, but Fiona said the form (:tortoise {:hare 1 :tortoise 2}) would
not be answered by guessing; the REPL would tell, calmly, the way
Plume the goose laid the next egg without rushing.

Question: write a Clojure expression for the value (:tortoise {:hare 1 :tortoise 2}) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:tortoise {:hare 1 :tortoise 2})"}}]}
```

### G2-17 sample 3/N (form: `(:missing {:hare 1})`, expected: `None`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

A row of small coins lay on the kitchen table inside the cellar, one for each
operand in the day's reckoning. Fiona had written
`(:missing {:hare 1})` at the top of the ledger — the next entry, just below
yesterday's egg-count. Morgan pointed at the coins and
guessed loudly, imagining all that might be gained, but Fiona said the form (:missing {:hare 1}) would
not be answered by guessing; the REPL would tell, calmly, the way
Honk the goose laid the next egg without rushing.

Write a form whose evaluation gives the value when a missing keyword is looked up.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:missing {:hare 1})"}}]}
```

### G2-17 sample 4/N (form: `(:hare {:hare 1 :tortoise 2})`, expected: `1`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was by the farm.

Edward and Alice stood in the farm where someone had
scratched the form (:hare {:hare 1 :tortoise 2}) into a smooth slate by the egg-basket.
Alice, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Edward, her eyes always on the path, suggested they
actually submit the form `(:hare {:hare 1 :tortoise 2})` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the value (:hare {:hare 1 :tortoise 2}) returns.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
```

### G2-17 sample 5/N (form: `(:tortoise {:hare 1 :tortoise 2})`, expected: `2`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"Whatever `(:tortoise {:hare 1 :tortoise 2})` comes to," Carol declared,
as if the race were already won, inside the kitchen, "I'll wager a basket of eggs I know it without
typing it." Alex, her eyes always on the path, picked up a piece of chalk
and drew the form (:tortoise {:hare 1 :tortoise 2}) on the side of the egg-crate. "Then write
the form," they said. "The REPL will have the last word, the
way Honk the goose has the last word on the morning's count."

Write a Clojure expression that computes the value (:tortoise {:hare 1 :tortoise 2}) returns.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(:tortoise {:hare 1 :tortoise 2})"}}]}
```

## G2-18: Quoting symbols

**examples (3):**

- ex0: form=`(quote hare)` expected=`'hare'`
    concept_phrase: `the quoted symbol (quote hare)`
    question_what: `the value of (quote hare)`
- ex1: form=`'tortoise` expected=`'tortoise'`
    concept_phrase: `the quoted symbol 'tortoise`
    question_what: `the value of 'tortoise`
- ex2: form=`'(1 2 3)` expected=`[1, 2, 3]`
    concept_phrase: `the quoted list '(1 2 3)`
    question_what: `the value of '(1 2 3) (a list, not a function call)`

### G2-18 sample 1/N (form: `(quote hare)`, expected: `'hare'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Carol had been laying out a chain of small computations on a
slate inside the barn — one operation, then another, all to settle a question
Alice had raised about the morning's eggs. The current form
on the slate was `(quote hare)`, and Carol explained, with steady, careful steps,
that the quoted symbol (quote hare) would be settled the moment the form was handed
to the REPL — the way Quill the goose settled each morning's tally with
one egg, no more, no less.

What Clojure form computes the value of (quote hare)? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(quote hare)"}}]}
```

### G2-18 sample 2/N (form: `'tortoise`, expected: `'tortoise'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice offered a small basket of eggs as a wager in the farm:
whoever guessed the result of `'tortoise` first would keep them.
Emily, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about the quoted symbol 'tortoise; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a form whose evaluation gives the value of 'tortoise.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"'tortoise"}}]}
```

### G2-18 sample 3/N (form: `'(1 2 3)`, expected: `[1, 2, 3]`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Fiona said, boasting at every turn.
"Anyone with eyes can see what the quoted list '(1 2 3) comes to."
Robin, who in the farm had grown used to such claims, asked
her to actually write the form `'(1 2 3)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of '(1 2 3) (a list, not a function call).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G2-18 sample 4/N (form: `(quote hare)`, expected: `'hare'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the village.

Diana and Sam stood by the village where someone had
scratched the quoted symbol (quote hare) into a smooth slate by the egg-basket.
Sam, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Diana, saying very little, suggested they
actually submit the form `(quote hare)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the value of (quote hare).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(quote hare)"}}]}
```

### G2-18 sample 5/N (form: `'tortoise`, expected: `'tortoise'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

At a small stall in the kitchen, someone had chalked a wager: whoever
predicted the result of `'tortoise` first would set the asking
price for the morning's eggs. David, her eyes always on the path, said it
was easier to type the form into the REPL than to argue about
the quoted symbol 'tortoise — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the value of 'tortoise.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"'tortoise"}}]}
```

## G2-19: Auto-promotion to bigint

**examples (2):**

- ex0: form=`(* 1000000 1000000)` expected=`1000000000000`
    concept_phrase: `the form (* 1000000 1000000)`
    question_what: `the result of one million times one million`
- ex1: form=`(+ 99999999999 1)` expected=`100000000000`
    concept_phrase: `the form (+ 99999999999 1)`
    question_what: `the result of 99999999999 plus 1`

### G2-19 sample 1/N (form: `(* 1000000 1000000)`, expected: `1000000000000`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of small coins lay on the kitchen table deep inside a cottage, one for each
operand in the day's reckoning. Grace had written
`(* 1000000 1000000)` at the top of the ledger — the next entry, just below
yesterday's egg-count. Carol pointed at the coins and
guessed loudly, with a hungry gleam in the eye, but Grace said the form (* 1000000 1000000) would
not be answered by guessing; the REPL would tell, calmly, the way
Quill the goose laid the next egg without rushing.

What Clojure form computes the result of one million times one million? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### G2-19 sample 2/N (form: `(+ 99999999999 1)`, expected: `100000000000`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the farm, the
next entry was the form (+ 99999999999 1). Jordan peered over
their shoulder at the form `(+ 99999999999 1)` and asked what
it would come out to.

Question: write a Clojure expression for the result of 99999999999 plus 1.
---asst---
I let the REPL settle the chain one operator at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### G2-19 sample 3/N (form: `(* 1000000 1000000)`, expected: `1000000000000`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been trying to teach Alex how the REPL
works. "Here," she said, pointing to the form (* 1000000 1000000).
"You hand the form `(* 1000000 1000000)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the result of one million times one million.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### G2-19 sample 4/N (form: `(+ 99999999999 1)`, expected: `100000000000`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the kitchen.

"There is no need to evaluate that," Robin said, boasting at every turn.
"Anyone with eyes can see what the form (+ 99999999999 1) comes to."
Helen, who deep inside the kitchen had grown used to such claims, asked
them to actually write the form `(+ 99999999999 1)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the result of 99999999999 plus 1.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 99999999999 1)"}}]}
```

### G2-19 sample 5/N (form: `(* 1000000 1000000)`, expected: `1000000000000`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the farm, the
next entry was the form (* 1000000 1000000). Robin peered over
her shoulder at the form `(* 1000000 1000000)` and asked what
it would come out to.

Write a Clojure expression that computes the result of one million times one million.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

## G2-20: Counting

**examples (3):**

- ex0: form=`(count [1 2 3])` expected=`3`
    concept_phrase: `the count of [1 2 3]`
    question_what: `the count of the vector [1 2 3]`
- ex1: form=`(count "hello")` expected=`5`
    concept_phrase: `the count of "hello"`
    question_what: `the length of the string "hello"`
- ex2: form=`(count [])` expected=`0`
    concept_phrase: `the count of an empty vector`
    question_what: `the count of an empty vector`

### G2-20 sample 1/N (form: `(count [1 2 3])`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today in the kitchen, the
next entry was the count of [1 2 3]. David peered over
his shoulder at the form `(count [1 2 3])` and asked what
it would come out to.

Write a Clojure expression that computes the count of the vector [1 2 3].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### G2-20 sample 2/N (form: `(count "hello")`, expected: `5`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Jordan said, with great whoops of laughter.
"Anyone with eyes can see what the count of "hello" comes to."
Alice, who in the cellar had grown used to such claims, asked
them to actually write the form `(count "hello")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the length of the string "hello".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

### G2-20 sample 3/N (form: `(count [])`, expected: `0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of small coins lay on the kitchen table at the edge of the village, one for each
operand in the day's reckoning. Henry had written
`(count [])` at the top of the ledger — the next entry, just below
yesterday's egg-count. Robin pointed at the coins and
guessed loudly, with a hungry gleam in the eye, but Henry said the count of an empty vector would
not be answered by guessing; the REPL would tell, calmly, the way
Quill the goose laid the next egg without rushing.

Question: write a Clojure expression for the count of an empty vector.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count [])"}}]}
```

### G2-20 sample 4/N (form: `(count [1 2 3])`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post at the edge of the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(count [1 2 3])`.
Bob laughed, with great whoops of laughter, and declared it too easy.
Fiona said, her eyes always on the path, that the only honest way to know
the count of [1 2 3] was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the count of the vector [1 2 3]? Submit it via `eval`.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### G2-20 sample 5/N (form: `(count "hello")`, expected: `5`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today by the meadow, the
next entry was the count of "hello". Bob peered over
his shoulder at the form `(count "hello")` and asked what
it would come out to.

Question: write a Clojure expression for the length of the string "hello".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hello\")"}}]}
```

## G2-21: String length and substring

**examples (3):**

- ex0: form=`(count "tortoise")` expected=`8`
    concept_phrase: `the length of "tortoise"`
    question_what: `the length of the string "tortoise"`
- ex1: form=`(count "hare")` expected=`4`
    concept_phrase: `the length of "hare"`
    question_what: `the length of the string "hare"`
- ex2: form=`(subs "tortoise" 0 3)` expected=`'tor'`
    concept_phrase: `the form (subs "tortoise" 0 3)`
    question_what: `the first three characters of "tortoise"`

### G2-21 sample 1/N (form: `(count "tortoise")`, expected: `8`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the village, the
next entry was the length of "tortoise". Morgan peered over
his shoulder at the form `(count "tortoise")` and asked what
it would come out to.

Question: write a Clojure expression for the length of the string "tortoise".
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G2-21 sample 2/N (form: `(count "hare")`, expected: `4`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the village.

Frank had been laying out a chain of small computations on a
slate at the edge of the village — one operation, then another, all to settle a question
Grace had raised about the morning's eggs. The current form
on the slate was `(count "hare")`, and Frank explained, without complaint,
that the length of "hare" would be settled the moment the form was handed
to the REPL — the way Honk the goose settled each morning's tally with
one egg, no more, no less.

Write a Clojure expression that computes the length of the string "hare".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\")"}}]}
```

### G2-21 sample 3/N (form: `(subs "tortoise" 0 3)`, expected: `'tor'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Helen said, boasting at every turn.
"Anyone with eyes can see what the form (subs "tortoise" 0 3) comes to."
Beatrice, who deep inside a cottage had grown used to such claims, asked
her to actually write the form `(subs "tortoise" 0 3)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the first three characters of "tortoise".
---asst---
I submit the whole form and let the runtime reduce it patiently, the way the goose lays one egg at a time.

{"tool_calls":[{"name":"eval","args":{"form":"(subs \"tortoise\" 0 3)"}}]}
```

### G2-21 sample 4/N (form: `(count "tortoise")`, expected: `8`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Frank and Helen stood in the barn where someone had
scratched the length of "tortoise" into a smooth slate by the egg-basket.
Helen, puffed up with pride, declared the answer was obvious — no need to
evaluate anything. Frank, untroubled by what others thought, suggested they
actually submit the form `(count "tortoise")` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Question: write a Clojure expression for the length of the string "tortoise".
---asst---
I let the runtime hand back one value, the way the goose gives one egg.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G2-21 sample 5/N (form: `(count "hare")`, expected: `4`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Diana had been trying to teach Jordan how the REPL
works. "Here," she said, pointing to the length of "hare".
"You hand the form `(count "hare")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the length of the string "hare".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\")"}}]}
```

## G2-22: Compose pure arithmetic (multi-step calculation)

**examples (3):**

- ex0: form=`(- (* 5 4) 7)` expected=`13`
    concept_phrase: `the form (- (* 5 4) 7)`
    question_what: `5 mph for 4 hours, minus a 7-mile head start`
- ex1: form=`(+ (* 3 8) (* 2 4))` expected=`32`
    concept_phrase: `the sum of two products`
    question_what: `3*8 + 2*4`
- ex2: form=`(quot (+ 100 50) 5)` expected=`30`
    concept_phrase: `the form (quot (+ 100 50) 5)`
    question_what: `150 divided by 5`

### G2-22 sample 1/N (form: `(- (* 5 4) 7)`, expected: `13`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered near the orchard to watch
David attempt to outguess Helen at reading the
REPL. Helen pointed to the form (- (* 5 4) 7) and read out the form
aloud: `(- (* 5 4) 7)`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes 5 mph for 4 hours, minus a 7-mile head start.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### G2-22 sample 2/N (form: `(+ (* 3 8) (* 2 4))`, expected: `32`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened by the orchard.

Emily had been laying out a chain of small computations on a
slate by the orchard — one operation, then another, all to settle a question
Robin had raised about the morning's eggs. The current form
on the slate was `(+ (* 3 8) (* 2 4))`, and Emily explained, untroubled by what others thought,
that the sum of two products would be settled the moment the form was handed
to the REPL — the way Plume the goose settled each morning's tally with
one egg, no more, no less.

Question: write a Clojure expression for 3*8 + 2*4.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

### G2-22 sample 3/N (form: `(quot (+ 100 50) 5)`, expected: `30`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Grace had been laying out a chain of small computations on a
slate by the farm — one operation, then another, all to settle a question
Casey had raised about the morning's eggs. The current form
on the slate was `(quot (+ 100 50) 5)`, and Grace explained, stepping deliberately,
that the form (quot (+ 100 50) 5) would be settled the moment the form was handed
to the REPL — the way Honk the goose settled each morning's tally with
one egg, no more, no less.

Write a Clojure expression that computes 150 divided by 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(quot (+ 100 50) 5)"}}]}
```

### G2-22 sample 4/N (form: `(- (* 5 4) 7)`, expected: `13`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small audience of neighbors had gathered near the farm to watch
Bob attempt to outguess Sam at reading the
REPL. Sam pointed to the form (- (* 5 4) 7) and read out the form
aloud: `(- (* 5 4) 7)`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes 5 mph for 4 hours, minus a 7-mile head start.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

### G2-22 sample 5/N (form: `(+ (* 3 8) (* 2 4))`, expected: `32`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol had been trying to teach Alex how the REPL
works. "Here," she said, pointing to the sum of two products.
"You hand the form `(+ (* 3 8) (* 2 4))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes 3*8 + 2*4.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 3 8) (* 2 4))"}}]}
```

