# Grade 6 goose-eggs — deep spot-check

5 rendered records per subject (16 subjects × 5 = 80 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G6-01: Namespace as file

**examples (3):**

- ex0: form=`(name 'foo.bar)` expected=`'foo.bar'`
    concept_phrase: `the symbol foo.bar standing in for a namespace name`
    question_what: `the string form of the namespace symbol foo.bar`
- ex1: form=`(name 'clojure.string)` expected=`'clojure.string'`
    concept_phrase: `the namespace symbol clojure.string`
    question_what: `the string "clojure.string"`
- ex2: form=`(symbol? 'tortoise.race)` expected=`True`
    concept_phrase: `whether tortoise.race is a symbol`
    question_what: `the value of (symbol? 'tortoise.race)`

### G6-01 sample 1/N (form: `(name 'foo.bar)`, expected: `'foo.bar'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

The two of them ran market stalls on opposite sides near the market —
Alice at one stall, Carol at the other. Each kept
their own ledger of forms beside the egg-baskets. When the time came
to compare notes, Alice read aloud the symbol foo.bar standing in for a namespace name and asked,
without complaint, what the form `(name 'foo.bar)` would return when the
REPL reached across the shared path between the stalls.

Write a Clojure expression that computes the string form of the namespace symbol foo.bar.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### G6-01 sample 2/N (form: `(name 'clojure.string)`, expected: `'clojure.string'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice wrote forms on a slate in the barn while
Frank kept another slate in the kitchen at the edge of the farm. Each
slate carried its own labels, and Quill the goose laid one egg per
morning regardless of which room counted it. Alice, saying very little,
read out the namespace symbol clojure.string and asked the REPL to return what
`(name 'clojure.string)` resolved to when the right slate's labels were in
view.

Question: write a Clojure expression for the string "clojure.string".
---asst---
I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

### G6-01 sample 3/N (form: `(symbol? 'tortoise.race)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(symbol? 'tortoise.race)`.
Morgan laughed, puffed up with pride, and declared it too easy.
Robin said, with steady, careful steps, that the only honest way to know
whether tortoise.race is a symbol was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the value of (symbol? 'tortoise.race)? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'tortoise.race)"}}]}
```

### G6-01 sample 4/N (form: `(name 'foo.bar)`, expected: `'foo.bar'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

"There is no need to evaluate that," Casey said, with great whoops of laughter.
"Anyone with eyes can see what the symbol foo.bar standing in for a namespace name comes to."
Edward, who in the cellar had grown used to such claims, asked
them to actually write the form `(name 'foo.bar)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

What Clojure form computes the string form of the namespace symbol foo.bar? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### G6-01 sample 5/N (form: `(name 'clojure.string)`, expected: `'clojure.string'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the namespace symbol clojure.string into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(name 'clojure.string)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the string "clojure.string".
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

## G6-02: ns form

**examples (2):**

- ex0: form=`(name 'race.tortoise)` expected=`'race.tortoise'`
    concept_phrase: `the namespace name 'race.tortoise as a string`
    question_what: `the string "race.tortoise"`
- ex1: form=`(= 'race.tortoise 'race.tortoise)` expected=`True`
    concept_phrase: `two identical namespace symbols`
    question_what: `whether the two namespace symbols are equal`

### G6-02 sample 1/N (form: `(name 'race.tortoise)`, expected: `'race.tortoise'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

"There is no need to evaluate that," Oliver said, swaggering through the underbrush.
"Anyone with eyes can see what the namespace name 'race.tortoise as a string comes to."
Henry, who inside the cellar had grown used to such claims, asked
him to actually write the form `(name 'race.tortoise)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the string "race.tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(name 'race.tortoise)"}}]}
```

### G6-02 sample 2/N (form: `(= 'race.tortoise 'race.tortoise)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver wrote forms on a slate in the barn while
Frank kept another slate in the kitchen at the edge of the village. Each
slate carried its own labels, and Quill the goose laid one egg per
morning regardless of which room counted it. Oliver, untroubled by what others thought,
read out two identical namespace symbols and asked the REPL to return what
`(= 'race.tortoise 'race.tortoise)` resolved to when the right slate's labels were in
view.

Write a Clojure expression that computes whether the two namespace symbols are equal.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'race.tortoise 'race.tortoise)"}}]}
```

### G6-02 sample 3/N (form: `(name 'race.tortoise)`, expected: `'race.tortoise'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to the namespace name 'race.tortoise as a string.
"You hand the form `(name 'race.tortoise)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the string "race.tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(name 'race.tortoise)"}}]}
```

### G6-02 sample 4/N (form: `(= 'race.tortoise 'race.tortoise)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the kitchen, the
next entry was two identical namespace symbols. Charlie peered over
her shoulder at the form `(= 'race.tortoise 'race.tortoise)` and asked what
it would come out to.

What Clojure form computes whether the two namespace symbols are equal? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= 'race.tortoise 'race.tortoise)"}}]}
```

### G6-02 sample 5/N (form: `(name 'race.tortoise)`, expected: `'race.tortoise'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(name 'race.tortoise)` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the namespace name 'race.tortoise as a string — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the string "race.tortoise".
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'race.tortoise)"}}]}
```

## G6-03: require

**examples (2):**

- ex0: form=`(clojure.string/upper-case "hare")` expected=`'HARE'`
    concept_phrase: `the form using clojure.string/upper-case on "hare"`
    question_what: `the upper-cased string "HARE"`
- ex1: form=`(clojure.string/lower-case "HARE")` expected=`'hare'`
    concept_phrase: `the form using clojure.string/lower-case`
    question_what: `the lower-cased string "hare"`

### G6-03 sample 1/N (form: `(clojure.string/upper-case "hare")`, expected: `'HARE'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(clojure.string/upper-case "hare")` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — the form using clojure.string/upper-case on "hare" would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the upper-cased string "HARE".
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

### G6-03 sample 2/N (form: `(clojure.string/lower-case "HARE")`, expected: `'hare'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(clojure.string/lower-case "HARE")` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the form using clojure.string/lower-case; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the lower-cased string "hare".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"HARE\")"}}]}
```

### G6-03 sample 3/N (form: `(clojure.string/upper-case "hare")`, expected: `'HARE'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

The two of them ran market stalls on opposite sides by the meadow —
Grace at one stall, Robin at the other. Each kept
their own ledger of forms beside the egg-baskets. When the time came
to compare notes, Grace read aloud the form using clojure.string/upper-case on "hare" and asked,
untroubled by what others thought, what the form `(clojure.string/upper-case "hare")` would return when the
REPL reached across the shared path between the stalls.

Question: write a Clojure expression for the upper-cased string "HARE".
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

### G6-03 sample 4/N (form: `(clojure.string/lower-case "HARE")`, expected: `'hare'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched the form using clojure.string/lower-case into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(clojure.string/lower-case "HARE")` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the lower-cased string "hare"? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"HARE\")"}}]}
```

### G6-03 sample 5/N (form: `(clojure.string/upper-case "hare")`, expected: `'HARE'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Carol said, with great whoops of laughter.
"Anyone with eyes can see what the form using clojure.string/upper-case on "hare" comes to."
Emily, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(clojure.string/upper-case "hare")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the upper-cased string "HARE".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

## G6-04: refer and use

**examples (1):**

- ex0: form=`(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` expected=`True`
    concept_phrase: `whether two calls to the same fully-qualified function agree`
    question_what: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

### G6-04 sample 1/N (form: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to whether two calls to the same fully-qualified function agree.
"You hand the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 sample 2/N (form: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit whether two calls to the same fully-qualified function agree to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 sample 3/N (form: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Helen stopped near the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` evaluated to. Helen called it
impossible. Frank, walking up at an unhurried pace, simply
said: "Submit whether two calls to the same fully-qualified function agree to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 sample 4/N (form: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Oliver offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` first would keep them.
David, stepping deliberately, said it would be simpler to type the
form into the REPL than to bicker about whether two calls to the same fully-qualified function agree; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-04 sample 5/N (form: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Sam wrote forms on a slate in the barn while
Bob kept another slate in the kitchen in the cellar. Each
slate carried its own labels, and Honk the goose laid one egg per
morning regardless of which room counted it. Sam, saying very little,
read out whether two calls to the same fully-qualified function agree and asked the REPL to return what
`(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` resolved to when the right slate's labels were in
view.

What Clojure form computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))? Submit it via `eval`.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

## G6-05: Fully qualified names

**examples (4):**

- ex0: form=`(clojure.string/upper-case "tortoise")` expected=`'TORTOISE'`
    concept_phrase: `clojure.string/upper-case applied to "tortoise"`
    question_what: `the upper-cased string "TORTOISE"`
- ex1: form=`(clojure.string/reverse "hare")` expected=`'erah'`
    concept_phrase: `clojure.string/reverse applied to "hare"`
    question_what: `the reversed string "erah"`
- ex2: form=`(namespace :race/tortoise)` expected=`'race'`
    concept_phrase: `the namespace portion of the keyword :race/tortoise`
    question_what: `the string "race"`
- ex3: form=`(name :race/tortoise)` expected=`'tortoise'`
    concept_phrase: `the name portion of the keyword :race/tortoise`
    question_what: `the string "tortoise"`

### G6-05 sample 1/N (form: `(clojure.string/upper-case "tortoise")`, expected: `'TORTOISE'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(clojure.string/upper-case "tortoise")` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit clojure.string/upper-case applied to "tortoise" to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for the upper-cased string "TORTOISE".
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"tortoise\")"}}]}
```

### G6-05 sample 2/N (form: `(clojure.string/reverse "hare")`, expected: `'erah'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Charlie kept a small farm near the market, where every form had its
own labeled column in the egg-ledger. Beatrice preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Charlie pointed to clojure.string/reverse applied to "hare" and asked her to
evaluate the form `(clojure.string/reverse "hare")` so they could see what name belonged
with what value, the way Quill the goose laid one egg into one labeled
basket.

Write a form whose evaluation gives the reversed string "erah".
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/reverse \"hare\")"}}]}
```

### G6-05 sample 3/N (form: `(namespace :race/tortoise)`, expected: `'race'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob offered a small basket of eggs as a wager near the farm:
whoever guessed the result of `(namespace :race/tortoise)` first would keep them.
Frank, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the namespace portion of the keyword :race/tortoise; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the string "race".
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(namespace :race/tortoise)"}}]}
```

### G6-05 sample 4/N (form: `(name :race/tortoise)`, expected: `'tortoise'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the barn.

Fiona had been trying to teach Frank how the REPL
works. "Here," she said, pointing to the name portion of the keyword :race/tortoise.
"You hand the form `(name :race/tortoise)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the string "tortoise"? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(name :race/tortoise)"}}]}
```

### G6-05 sample 5/N (form: `(clojure.string/upper-case "tortoise")`, expected: `'TORTOISE'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(clojure.string/upper-case "tortoise")` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit clojure.string/upper-case applied to "tortoise" to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the upper-cased string "TORTOISE".
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"tortoise\")"}}]}
```

## G6-06: Private defs

**examples (2):**

- ex0: form=`(:private (meta '^:private x))` expected=`True`
    concept_phrase: `the :private flag on metadata of '^:private x`
    question_what: `whether the :private metadata is true`
- ex1: form=`(:private (meta 'x))` expected=`None`
    concept_phrase: `the :private flag on plain metadata of 'x (none set)`
    question_what: `the value of (:private (meta 'x)), which is nil`

### G6-06 sample 1/N (form: `(:private (meta '^:private x))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what the :private flag on metadata of '^:private x comes to."
Henry, who by the farm had grown used to such claims, asked
him to actually write the form `(:private (meta '^:private x))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives whether the :private metadata is true.
---asst---
I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### G6-06 sample 2/N (form: `(:private (meta 'x))`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Casey wrote forms on a slate in the barn while
Fiona kept another slate in the kitchen at the edge of the market. Each
slate carried its own labels, and Plume the goose laid one egg per
morning regardless of which room counted it. Casey, without complaint,
read out the :private flag on plain metadata of 'x (none set) and asked the REPL to return what
`(:private (meta 'x))` resolved to when the right slate's labels were in
view.

Question: write a Clojure expression for the value of (:private (meta 'x)), which is nil.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### G6-06 sample 3/N (form: `(:private (meta '^:private x))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched the :private flag on metadata of '^:private x into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(:private (meta '^:private x))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes whether the :private metadata is true? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### G6-06 sample 4/N (form: `(:private (meta 'x))`, expected: `None`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(:private (meta 'x))`.
Edward laughed, swaggering through the underbrush, and declared it too easy.
Emily said, her eyes always on the path, that the only honest way to know
the :private flag on plain metadata of 'x (none set) was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the value of (:private (meta 'x)), which is nil.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### G6-06 sample 5/N (form: `(:private (meta '^:private x))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(:private (meta '^:private x))`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
the :private flag on metadata of '^:private x was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes whether the :private metadata is true.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

## G6-07: Public vs private API

**examples (2):**

- ex0: form=`(boolean (:private (meta '^:private hidden)))` expected=`True`
    concept_phrase: `whether the symbol 'hidden carries the :private flag`
    question_what: `the boolean of (:private (meta '^:private hidden))`
- ex1: form=`(boolean (:private (meta 'public)))` expected=`False`
    concept_phrase: `whether 'public carries the :private flag`
    question_what: `the boolean of (:private (meta 'public))`

### G6-07 sample 1/N (form: `(boolean (:private (meta '^:private hidden)))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

David kept a small farm by the market, where every form had its
own labeled column in the egg-ledger. Robin preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
David pointed to whether the symbol 'hidden carries the :private flag and asked them to
evaluate the form `(boolean (:private (meta '^:private hidden)))` so they could see what name belonged
with what value, the way Quill the goose laid one egg into one labeled
basket.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### G6-07 sample 2/N (form: `(boolean (:private (meta 'public)))`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

The two of them ran market stalls on opposite sides deep inside the kitchen —
Emily at one stall, David at the other. Each kept
their own ledger of forms beside the egg-baskets. When the time came
to compare notes, Emily read aloud whether 'public carries the :private flag and asked,
her eyes always on the path, what the form `(boolean (:private (meta 'public)))` would return when the
REPL reached across the shared path between the stalls.

What Clojure form computes the boolean of (:private (meta 'public))? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### G6-07 sample 3/N (form: `(boolean (:private (meta '^:private hidden)))`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Fiona wrote forms on a slate in the barn while
Sam kept another slate in the kitchen deep inside the cellar. Each
slate carried its own labels, and Plume the goose laid one egg per
morning regardless of which room counted it. Fiona, untroubled by what others thought,
read out whether the symbol 'hidden carries the :private flag and asked the REPL to return what
`(boolean (:private (meta '^:private hidden)))` resolved to when the right slate's labels were in
view.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### G6-07 sample 4/N (form: `(boolean (:private (meta 'public)))`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, George stopped near the market
with a basket of eggs and refused to move on until someone could
prove what the form `(boolean (:private (meta 'public)))` evaluated to. George called it
impossible. Casey, walking up at an unhurried pace, simply
said: "Submit whether 'public carries the :private flag to the REPL. Whatever comes back is
the answer." Plume the goose watched the basket, calm as ever.

What Clojure form computes the boolean of (:private (meta 'public))? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### G6-07 sample 5/N (form: `(boolean (:private (meta '^:private hidden)))`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

Helen kept a small farm deep inside a cottage, where every form had its
own labeled column in the egg-ledger. Robin preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Helen pointed to whether the symbol 'hidden carries the :private flag and asked them to
evaluate the form `(boolean (:private (meta '^:private hidden)))` so they could see what name belonged
with what value, the way Plume the goose laid one egg into one labeled
basket.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

## G6-08: Circular dependencies

**examples (2):**

- ex0: form=`(clojure.string/upper-case "a")` expected=`'A'`
    concept_phrase: `a single-direction call from one namespace to clojure.string`
    question_what: `the upper-cased string "A"`
- ex1: form=`(= 'a.b 'a.b)` expected=`True`
    concept_phrase: `whether two references to the same namespace symbol agree`
    question_what: `the value of (= 'a.b 'a.b)`

### G6-08 sample 1/N (form: `(clojure.string/upper-case "a")`, expected: `'A'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

The two of them ran market stalls on opposite sides in the village —
Bob at one stall, Oliver at the other. Each kept
their own ledger of forms beside the egg-baskets. When the time came
to compare notes, Bob read aloud a single-direction call from one namespace to clojure.string and asked,
stepping deliberately, what the form `(clojure.string/upper-case "a")` would return when the
REPL reached across the shared path between the stalls.

Write a form whose evaluation gives the upper-cased string "A".
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### G6-08 sample 2/N (form: `(= 'a.b 'a.b)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(= 'a.b 'a.b)` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit whether two references to the same namespace symbol agree to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes the value of (= 'a.b 'a.b).
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### G6-08 sample 3/N (form: `(clojure.string/upper-case "a")`, expected: `'A'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(clojure.string/upper-case "a")` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — a single-direction call from one namespace to clojure.string would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the upper-cased string "A".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### G6-08 sample 4/N (form: `(= 'a.b 'a.b)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

George kept a small farm deep inside the cellar, where every form had its
own labeled column in the egg-ledger. Casey preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
George pointed to whether two references to the same namespace symbol agree and asked them to
evaluate the form `(= 'a.b 'a.b)` so they could see what name belonged
with what value, the way Honk the goose laid one egg into one labeled
basket.

Question: write a Clojure expression for the value of (= 'a.b 'a.b).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### G6-08 sample 5/N (form: `(clojure.string/upper-case "a")`, expected: `'A'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to a single-direction call from one namespace to clojure.string.
"You hand the form `(clojure.string/upper-case "a")` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes the upper-cased string "A"? Submit it via `eval`.
---asst---
I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

## G6-09: Loading order

**examples (2):**

- ex0: form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` expected=`2`
    concept_phrase: `two defs evaluated in order, the second using the first`
    question_what: `the final value step2 after sequential loading`
- ex1: form=`(let [a 1 b (+ a 1)] (+ a b))` expected=`3`
    concept_phrase: `an in-expression analogue of file-loading order via let`
    question_what: `the value of (+ a b) given a=1 b=(+ a 1)`

### G6-09 sample 1/N (form: `(do (def step1 1) (def step2 (+ step1 1)) step2)`, expected: `2`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Oliver had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the village, the
next entry was two defs evaluated in order, the second using the first. George peered over
his shoulder at the form `(do (def step1 1) (def step2 (+ step1 1)) step2)` and asked what
it would come out to.

Write a Clojure expression that computes the final value step2 after sequential loading.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### G6-09 sample 2/N (form: `(let [a 1 b (+ a 1)] (+ a b))`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the barn to watch
David attempt to outguess Fiona at reading the
REPL. Fiona pointed to an in-expression analogue of file-loading order via let and read out the form
aloud: `(let [a 1 b (+ a 1)] (+ a b))`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the value of (+ a b) given a=1 b=(+ a 1).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### G6-09 sample 3/N (form: `(do (def step1 1) (def step2 (+ step1 1)) step2)`, expected: `2`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was two defs evaluated in order, the second using the first. George peered over
their shoulder at the form `(do (def step1 1) (def step2 (+ step1 1)) step2)` and asked what
it would come out to.

Write a form whose evaluation gives the final value step2 after sequential loading.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### G6-09 sample 4/N (form: `(let [a 1 b (+ a 1)] (+ a b))`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small wooden notice nailed to a post by the meadow carried a puzzle for
the village. The riddle asked the reader to evaluate `(let [a 1 b (+ a 1)] (+ a b))`.
Beatrice laughed, with great whoops of laughter, and declared it too easy.
Emily said, without complaint, that the only honest way to know
an in-expression analogue of file-loading order via let was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the value of (+ a b) given a=1 b=(+ a 1).
---asst---
I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### G6-09 sample 5/N (form: `(do (def step1 1) (def step2 (+ step1 1)) step2)`, expected: `2`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(do (def step1 1) (def step2 (+ step1 1)) step2)` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about two defs evaluated in order, the second using the first; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the final value step2 after sequential loading.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

## G6-10: Leiningen and deps.edn

**examples (2):**

- ex0: form=`(:deps {:deps {:a 1 :b 2}})` expected=`{':a': 1, ':b': 2}`
    concept_phrase: `the :deps key from a small deps-map literal`
    question_what: `the value at :deps in {:deps {:a 1 :b 2}}`
- ex1: form=`(get-in {:paths ["src"]} [:paths 0])` expected=`'src'`
    concept_phrase: `the first :paths entry from a tiny deps-style map`
    question_what: `the string "src" at [:paths 0]`

### G6-10 sample 1/N (form: `(:deps {:deps {:a 1 :b 2}})`, expected: `{':a': 1, ':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

Alex wrote forms on a slate in the barn while
Fiona kept another slate in the kitchen deep inside the kitchen. Each
slate carried its own labels, and Honk the goose laid one egg per
morning regardless of which room counted it. Alex, stepping deliberately,
read out the :deps key from a small deps-map literal and asked the REPL to return what
`(:deps {:deps {:a 1 :b 2}})` resolved to when the right slate's labels were in
view.

Write a Clojure expression that computes the value at :deps in {:deps {:a 1 :b 2}}.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### G6-10 sample 2/N (form: `(get-in {:paths ["src"]} [:paths 0])`, expected: `'src'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to the first :paths entry from a tiny deps-style map.
"You hand the form `(get-in {:paths ["src"]} [:paths 0])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes the string "src" at [:paths 0]? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### G6-10 sample 3/N (form: `(:deps {:deps {:a 1 :b 2}})`, expected: `{':a': 1, ':b': 2}`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was the :deps key from a small deps-map literal. Emily peered over
her shoulder at the form `(:deps {:deps {:a 1 :b 2}})` and asked what
it would come out to.

Write a form whose evaluation gives the value at :deps in {:deps {:a 1 :b 2}}.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### G6-10 sample 4/N (form: `(get-in {:paths ["src"]} [:paths 0])`, expected: `'src'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post in the village carried a puzzle for
the village. The riddle asked the reader to evaluate `(get-in {:paths ["src"]} [:paths 0])`.
Robin laughed, swaggering through the underbrush, and declared it too easy.
Grace said, her eyes always on the path, that the only honest way to know
the first :paths entry from a tiny deps-style map was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the string "src" at [:paths 0].
---asst---
I label the form by its farm and let the runtime read across.

{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### G6-10 sample 5/N (form: `(:deps {:deps {:a 1 :b 2}})`, expected: `{':a': 1, ':b': 2}`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(:deps {:deps {:a 1 :b 2}})` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the :deps key from a small deps-map literal; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the value at :deps in {:deps {:a 1 :b 2}}.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

## G6-11: Classpath

**examples (2):**

- ex0: form=`(clojure.string/split "src:test" #":")` expected=`['src', 'test']`
    concept_phrase: `splitting a colon-separated classpath-like string`
    question_what: `the vector ["src" "test"]`
- ex1: form=`(count ["src" "test" "resources"])` expected=`3`
    concept_phrase: `the number of entries in a classpath-like vector`
    question_what: `the count of three classpath entries`

### G6-11 sample 1/N (form: `(clojure.string/split "src:test" #":")`, expected: `['src', 'test']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(clojure.string/split "src:test" #":")` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
splitting a colon-separated classpath-like string — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the vector ["src" "test"].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### G6-11 sample 2/N (form: `(count ["src" "test" "resources"])`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered in the farm to watch
Morgan attempt to outguess Edward at reading the
REPL. Edward pointed to the number of entries in a classpath-like vector and read out the form
aloud: `(count ["src" "test" "resources"])`. The crowd waited to see who would correctly
write the form to submit; Honk the goose watched too, untroubled by
the noise.

Write a form whose evaluation gives the count of three classpath entries.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### G6-11 sample 3/N (form: `(clojure.string/split "src:test" #":")`, expected: `['src', 'test']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(clojure.string/split "src:test" #":")` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
splitting a colon-separated classpath-like string — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the vector ["src" "test"].
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### G6-11 sample 4/N (form: `(count ["src" "test" "resources"])`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(count ["src" "test" "resources"])` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about the number of entries in a classpath-like vector; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the count of three classpath entries.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### G6-11 sample 5/N (form: `(clojure.string/split "src:test" #":")`, expected: `['src', 'test']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post deep inside the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(clojure.string/split "src:test" #":")`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
splitting a colon-separated classpath-like string was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the vector ["src" "test"].
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

## G6-12: Multiple files in one project

**examples (2):**

- ex0: form=`(count ['race.tortoise 'race.hare 'race.shared])` expected=`3`
    concept_phrase: `the number of namespaces in a small project`
    question_what: `the count of namespace symbols in the vector`
- ex1: form=`(map name ['race.tortoise 'race.hare])` expected=`['race.tortoise', 'race.hare']`
    concept_phrase: `the names of two namespaces as strings`
    question_what: `the vector of namespace name strings`

### G6-12 sample 1/N (form: `(count ['race.tortoise 'race.hare 'race.shared])`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Helen had been trying to teach Fiona how the REPL
works. "Here," she said, pointing to the number of namespaces in a small project.
"You hand the form `(count ['race.tortoise 'race.hare 'race.shared])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the count of namespace symbols in the vector.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count ['race.tortoise 'race.hare 'race.shared])"}}]}
```

### G6-12 sample 2/N (form: `(map name ['race.tortoise 'race.hare])`, expected: `['race.tortoise', 'race.hare']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(map name ['race.tortoise 'race.hare])` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
the names of two namespaces as strings — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the vector of namespace name strings.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(map name ['race.tortoise 'race.hare])"}}]}
```

### G6-12 sample 3/N (form: `(count ['race.tortoise 'race.hare 'race.shared])`, expected: `3`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(count ['race.tortoise 'race.hare 'race.shared])` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the number of namespaces in a small project — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the count of namespace symbols in the vector.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count ['race.tortoise 'race.hare 'race.shared])"}}]}
```

### G6-12 sample 4/N (form: `(map name ['race.tortoise 'race.hare])`, expected: `['race.tortoise', 'race.hare']`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(map name ['race.tortoise 'race.hare])`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
the names of two namespaces as strings was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the vector of namespace name strings? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(map name ['race.tortoise 'race.hare])"}}]}
```

### G6-12 sample 5/N (form: `(count ['race.tortoise 'race.hare 'race.shared])`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Morgan wrote forms on a slate in the barn while
Oliver kept another slate in the kitchen by the meadow. Each
slate carried its own labels, and Quill the goose laid one egg per
morning regardless of which room counted it. Morgan, without complaint,
read out the number of namespaces in a small project and asked the REPL to return what
`(count ['race.tortoise 'race.hare 'race.shared])` resolved to when the right slate's labels were in
view.

What Clojure form computes the count of namespace symbols in the vector? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(count ['race.tortoise 'race.hare 'race.shared])"}}]}
```

## G6-13: Aliasing conventions

**examples (1):**

- ex0: form=`(let [s clojure.string/upper-case] (s "hare"))` expected=`'HARE'`
    concept_phrase: `binding the function clojure.string/upper-case to a local s`
    question_what: `the value (s "hare") where s is upper-case`

### G6-13 sample 1/N (form: `(let [s clojure.string/upper-case] (s "hare"))`, expected: `'HARE'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice kept a small farm at the edge of the market, where every form had its
own labeled column in the egg-ledger. Sam preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Alice pointed to binding the function clojure.string/upper-case to a local s and asked them to
evaluate the form `(let [s clojure.string/upper-case] (s "hare"))` so they could see what name belonged
with what value, the way Plume the goose laid one egg into one labeled
basket.

Write a form whose evaluation gives the value (s "hare") where s is upper-case.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

### G6-13 sample 2/N (form: `(let [s clojure.string/upper-case] (s "hare"))`, expected: `'HARE'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

Diana kept a small farm inside a cottage, where every form had its
own labeled column in the egg-ledger. Robin preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Diana pointed to binding the function clojure.string/upper-case to a local s and asked them to
evaluate the form `(let [s clojure.string/upper-case] (s "hare"))` so they could see what name belonged
with what value, the way Honk the goose laid one egg into one labeled
basket.

What Clojure form computes the value (s "hare") where s is upper-case? Submit it via `eval`.
---asst---
I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

### G6-13 sample 3/N (form: `(let [s clojure.string/upper-case] (s "hare"))`, expected: `'HARE'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(let [s clojure.string/upper-case] (s "hare"))` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — binding the function clojure.string/upper-case to a local s would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value (s "hare") where s is upper-case.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

### G6-13 sample 4/N (form: `(let [s clojure.string/upper-case] (s "hare"))`, expected: `'HARE'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Diana wrote forms on a slate in the barn while
Henry kept another slate in the kitchen by the farm. Each
slate carried its own labels, and Quill the goose laid one egg per
morning regardless of which room counted it. Diana, her eyes always on the path,
read out binding the function clojure.string/upper-case to a local s and asked the REPL to return what
`(let [s clojure.string/upper-case] (s "hare"))` resolved to when the right slate's labels were in
view.

Write a Clojure expression that computes the value (s "hare") where s is upper-case.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

### G6-13 sample 5/N (form: `(let [s clojure.string/upper-case] (s "hare"))`, expected: `'HARE'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Alex offered a small basket of eggs as a wager deep inside the cellar:
whoever guessed the result of `(let [s clojure.string/upper-case] (s "hare"))` first would keep them.
Carol, without complaint, said it would be simpler to type the
form into the REPL than to bicker about binding the function clojure.string/upper-case to a local s; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Write a form whose evaluation gives the value (s "hare") where s is upper-case.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

## G6-14: Import for host classes

**examples (2):**

- ex0: form=`(symbol? 'java.util.Date)` expected=`True`
    concept_phrase: `whether 'java.util.Date is a symbol`
    question_what: `the value of (symbol? 'java.util.Date)`
- ex1: form=`(name 'java.util.Date)` expected=`'java.util.Date'`
    concept_phrase: `the dotted-class symbol's name`
    question_what: `the string "java.util.Date"`

### G6-14 sample 1/N (form: `(symbol? 'java.util.Date)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

"There is no need to evaluate that," Diana said, swaggering through the underbrush.
"Anyone with eyes can see what whether 'java.util.Date is a symbol comes to."
Grace, who by the village had grown used to such claims, asked
her to actually write the form `(symbol? 'java.util.Date)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of (symbol? 'java.util.Date).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### G6-14 sample 2/N (form: `(name 'java.util.Date)`, expected: `'java.util.Date'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Edward kept a small farm in the market, where every form had its
own labeled column in the egg-ledger. George preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Edward pointed to the dotted-class symbol's name and asked him to
evaluate the form `(name 'java.util.Date)` so they could see what name belonged
with what value, the way Plume the goose laid one egg into one labeled
basket.

What Clojure form computes the string "java.util.Date"? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### G6-14 sample 3/N (form: `(symbol? 'java.util.Date)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what whether 'java.util.Date is a symbol comes to."
Edward, who in the meadow had grown used to such claims, asked
him to actually write the form `(symbol? 'java.util.Date)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the value of (symbol? 'java.util.Date).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### G6-14 sample 4/N (form: `(name 'java.util.Date)`, expected: `'java.util.Date'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

The two of them ran market stalls on opposite sides in the barn —
Casey at one stall, Jordan at the other. Each kept
their own ledger of forms beside the egg-baskets. When the time came
to compare notes, Casey read aloud the dotted-class symbol's name and asked,
with steady, careful steps, what the form `(name 'java.util.Date)` would return when the
REPL reached across the shared path between the stalls.

Question: write a Clojure expression for the string "java.util.Date".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### G6-14 sample 5/N (form: `(symbol? 'java.util.Date)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Alice kept a small farm deep inside a cottage, where every form had its
own labeled column in the egg-ledger. Bob preferred to
scribble each expression in a single notebook, the way one might
toss every coin into one purse. To settle a question that morning,
Alice pointed to whether 'java.util.Date is a symbol and asked him to
evaluate the form `(symbol? 'java.util.Date)` so they could see what name belonged
with what value, the way Quill the goose laid one egg into one labeled
basket.

What Clojure form computes the value of (symbol? 'java.util.Date)? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

## G6-15: Namespace meta

**examples (2):**

- ex0: form=`(:doc (meta '^{:doc "steady wins"} race))` expected=`'steady wins'`
    concept_phrase: `the :doc metadata attached to the symbol 'race`
    question_what: `the docstring "steady wins" from the metadata`
- ex1: form=`(:author (meta '^{:author "Aesop"} race))` expected=`'Aesop'`
    concept_phrase: `the :author metadata on 'race`
    question_what: `the string "Aesop"`

### G6-15 sample 1/N (form: `(:doc (meta '^{:doc "steady wins"} race))`, expected: `'steady wins'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

Emily offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(:doc (meta '^{:doc "steady wins"} race))` first would keep them.
Robin, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the :doc metadata attached to the symbol 'race; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the docstring "steady wins" from the metadata.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"steady wins\"} race))"}}]}
```

### G6-15 sample 2/N (form: `(:author (meta '^{:author "Aesop"} race))`, expected: `'Aesop'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the :author metadata on 'race comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(:author (meta '^{:author "Aesop"} race))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the string "Aesop".
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} race))"}}]}
```

### G6-15 sample 3/N (form: `(:doc (meta '^{:doc "steady wins"} race))`, expected: `'steady wins'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Alex said, with a smug grin.
"Anyone with eyes can see what the :doc metadata attached to the symbol 'race comes to."
Casey, who at the edge of the meadow had grown used to such claims, asked
them to actually write the form `(:doc (meta '^{:doc "steady wins"} race))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the docstring "steady wins" from the metadata.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"steady wins\"} race))"}}]}
```

### G6-15 sample 4/N (form: `(:author (meta '^{:author "Aesop"} race))`, expected: `'Aesop'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post near the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(:author (meta '^{:author "Aesop"} race))`.
Robin laughed, with a smug grin, and declared it too easy.
Diana said, stepping deliberately, that the only honest way to know
the :author metadata on 'race was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for the string "Aesop".
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} race))"}}]}
```

### G6-15 sample 5/N (form: `(:doc (meta '^{:doc "steady wins"} race))`, expected: `'steady wins'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the market, the
next entry was the :doc metadata attached to the symbol 'race. Bob peered over
their shoulder at the form `(:doc (meta '^{:doc "steady wins"} race))` and asked what
it would come out to.

Question: write a Clojure expression for the docstring "steady wins" from the metadata.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"steady wins\"} race))"}}]}
```

## G6-16: Cleaning up requires

**examples (2):**

- ex0: form=`(contains? #{'clojure.string} 'clojure.string)` expected=`True`
    concept_phrase: `whether the require list still contains 'clojure.string`
    question_what: `the value of (contains? #{'clojure.string} 'clojure.string)`
- ex1: form=`(contains? #{'clojure.string} 'clojure.set)` expected=`False`
    concept_phrase: `whether the require list contains an unused 'clojure.set`
    question_what: `the value of (contains? #{'clojure.string} 'clojure.set)`

### G6-16 sample 1/N (form: `(contains? #{'clojure.string} 'clojure.string)`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

"There is no need to evaluate that," Sam said, as if the race were already won.
"Anyone with eyes can see what whether the require list still contains 'clojure.string comes to."
Alice, who by the meadow had grown used to such claims, asked
them to actually write the form `(contains? #{'clojure.string} 'clojure.string)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the value of (contains? #{'clojure.string} 'clojure.string).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### G6-16 sample 2/N (form: `(contains? #{'clojure.string} 'clojure.set)`, expected: `False`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(contains? #{'clojure.string} 'clojure.set)` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — whether the require list contains an unused 'clojure.set would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.set).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### G6-16 sample 3/N (form: `(contains? #{'clojure.string} 'clojure.string)`, expected: `True`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(contains? #{'clojure.string} 'clojure.string)` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — whether the require list still contains 'clojure.string would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the value of (contains? #{'clojure.string} 'clojure.string).
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### G6-16 sample 4/N (form: `(contains? #{'clojure.string} 'clojure.set)`, expected: `False`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," David said, swaggering through the underbrush.
"Anyone with eyes can see what whether the require list contains an unused 'clojure.set comes to."
Carol, who in the market had grown used to such claims, asked
him to actually write the form `(contains? #{'clojure.string} 'clojure.set)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of (contains? #{'clojure.string} 'clojure.set).
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### G6-16 sample 5/N (form: `(contains? #{'clojure.string} 'clojure.string)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Bob said, with a smug grin.
"Anyone with eyes can see what whether the require list still contains 'clojure.string comes to."
Emily, who inside the barn had grown used to such claims, asked
him to actually write the form `(contains? #{'clojure.string} 'clojure.string)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the value of (contains? #{'clojure.string} 'clojure.string).
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

