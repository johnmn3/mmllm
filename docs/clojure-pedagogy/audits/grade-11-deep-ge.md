# Grade 11 goose-eggs — deep spot-check

5 rendered records per subject (14 subjects × 5 = 70 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G11-01: JVM vs CLR vs JS vs Python (host overview)

**examples (2):**

- ex0: form=`(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` expected=`':studied'`
    concept_phrase: `the idea that Clojure has multiple host runtimes`
    question_what: `the marker value when the host overview has been studied`
- ex1: form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` expected=`':hosts'`
    concept_phrase: `the family of Clojure host runtimes`
    question_what: `the marker keyword for the host family`

### G11-01 sample 1/N (form: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol insisted the foreign-runtime forms were "just like
home." Alice tapped a stone near the market where someone had
inscribed the idea that Clojure has multiple host runtimes above the day's egg-prices. "Then write
`(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` into the REPL," Alice said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

Write a Clojure expression that computes the marker value when the host overview has been studied.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 sample 2/N (form: `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)`, expected: `':hosts'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A merchant's stall at the edge of the farm sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
the family of Clojure host runtimes. Alice copied the form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` from
the page into her ledger, and Frank agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

Question: write a Clojure expression for the marker keyword for the host family.
---asst---
I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### G11-01 sample 3/N (form: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

Edward and Casey had carried a basket of eggs in the cellar
into territory where the REPL spoke to another runtime entirely.
Edward read the market sign and pointed at the idea that Clojure has multiple host runtimes; the form
to submit, written in the foreign convention, was `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`.
Plume the goose had stayed at home, but his ledger came along.

What Clojure form computes the marker value when the host overview has been studied? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-01 sample 4/N (form: `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)`, expected: `':hosts'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched the family of Clojure host runtimes into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives the marker keyword for the host family.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp\" :hosts)"}}]}
```

### G11-01 sample 5/N (form: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Bob offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` first would keep them.
Henry, saying very little, said it would be simpler to type the
form into the REPL than to bicker about the idea that Clojure has multiple host runtimes; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the marker value when the host overview has been studied.
---asst---
I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

## G11-02: Method call syntax

**examples (3):**

- ex0: form=`(.toUpperCase "abc")` expected=`'ABC'`
    concept_phrase: `the method call (.toUpperCase "abc")`
    question_what: `the uppercased string returned by the method`
- ex1: form=`(.startsWith "hare-tortoise" "hare")` expected=`True`
    concept_phrase: `a method call (.startsWith ...) returning a boolean`
    question_what: `whether the string starts with the prefix`
- ex2: form=`(. "abc" toUpperCase)` expected=`'ABC'`
    concept_phrase: `the alternate dot form (. obj method)`
    question_what: `the uppercased result via the longer dot syntax`

### G11-02 sample 1/N (form: `(.toUpperCase "abc")`, expected: `'ABC'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

A small wooden notice nailed to a post inside the cellar carried a puzzle for
the village. The riddle asked the reader to evaluate `(.toUpperCase "abc")`.
Oliver laughed, swaggering through the underbrush, and declared it too easy.
Henry said, her eyes always on the path, that the only honest way to know
the method call (.toUpperCase "abc") was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the uppercased string returned by the method.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 sample 2/N (form: `(.startsWith "hare-tortoise" "hare")`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A merchant's stall at the edge of the village sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
a method call (.startsWith ...) returning a boolean. Oliver copied the form `(.startsWith "hare-tortoise" "hare")` from
the page into his ledger, and Frank agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

Write a Clojure expression that computes whether the string starts with the prefix.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"hare-tortoise\" \"hare\")"}}]}
```

### G11-02 sample 3/N (form: `(. "abc" toUpperCase)`, expected: `'ABC'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"This is not our farmyard," Robin said inside a cottage, saying very little.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
Sam, calculating in silence, said they could read the
foreign form anyway. Robin sketched `(. "abc" toUpperCase)` on a slate beside
the egg-basket; let the runtime, they insisted, declare what
the alternate dot form (. obj method) returned.

Write a form whose evaluation gives the uppercased result via the longer dot syntax.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(. \"abc\" toUpperCase)"}}]}
```

### G11-02 sample 4/N (form: `(.toUpperCase "abc")`, expected: `'ABC'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

A small audience of neighbors had gathered by the farm to watch
Helen attempt to outguess Casey at reading the
REPL. Casey pointed to the method call (.toUpperCase "abc") and read out the form
aloud: `(.toUpperCase "abc")`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the uppercased string returned by the method.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-02 sample 5/N (form: `(.startsWith "hare-tortoise" "hare")`, expected: `True`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

A small wooden notice nailed to a post in the kitchen carried a puzzle for
the village. The riddle asked the reader to evaluate `(.startsWith "hare-tortoise" "hare")`.
Charlie laughed, boasting at every turn, and declared it too easy.
Fiona said, stepping deliberately, that the only honest way to know
a method call (.startsWith ...) returning a boolean was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes whether the string starts with the prefix? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(.startsWith \"hare-tortoise\" \"hare\")"}}]}
```

## G11-03: Static method call

**examples (2):**

- ex0: form=`(Math/abs -7)` expected=`7`
    concept_phrase: `the static call (Math/abs -7)`
    question_what: `the absolute value of -7 via the static method`
- ex1: form=`(Math/max 3 9)` expected=`9`
    concept_phrase: `the static call (Math/max 3 9)`
    question_what: `the larger of 3 and 9 via the static method`

### G11-03 sample 1/N (form: `(Math/abs -7)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(Math/abs -7)` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — the static call (Math/abs -7) would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the absolute value of -7 via the static method.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 sample 2/N (form: `(Math/max 3 9)`, expected: `9`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alex had been trying to teach Robin how the REPL
works. "Here," they said, pointing to the static call (Math/max 3 9).
"You hand the form `(Math/max 3 9)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the larger of 3 and 9 via the static method.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### G11-03 sample 3/N (form: `(Math/abs -7)`, expected: `7`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

At a wayside shrine by the meadow dedicated to safe interop and honest
weights, the day's offering was the static call (Math/abs -7). Grace knelt
and placed the form `(Math/abs -7)` on the stone beside a single egg
from the morning's basket. Robin, watching, agreed to be the one
to submit it to the runtime.

Question: write a Clojure expression for the absolute value of -7 via the static method.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-03 sample 4/N (form: `(Math/max 3 9)`, expected: `9`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched the static call (Math/max 3 9) into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(Math/max 3 9)` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the larger of 3 and 9 via the static method? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(Math/max 3 9)"}}]}
```

### G11-03 sample 5/N (form: `(Math/abs -7)`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"This is not our farmyard," Emily said at the edge of the market, stepping deliberately.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
Carol, with a hungry gleam in the eye, said she could read the
foreign form anyway. Emily sketched `(Math/abs -7)` on a slate beside
the egg-basket; let the runtime, she insisted, declare what
the static call (Math/abs -7) returned.

Write a Clojure expression that computes the absolute value of -7 via the static method.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

## G11-04: Field access

**examples (2):**

- ex0: form=`(count "tortoise")` expected=`8`
    concept_phrase: `the count of "tortoise" — host-portable length`
    question_what: `the length of "tortoise"`
- ex1: form=`(count "hare")` expected=`4`
    concept_phrase: `the count of "hare"`
    question_what: `the length of "hare"`

### G11-04 sample 1/N (form: `(count "tortoise")`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered inside the cellar to watch
Charlie attempt to outguess Alice at reading the
REPL. Alice pointed to the count of "tortoise" — host-portable length and read out the form
aloud: `(count "tortoise")`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the length of "tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G11-04 sample 2/N (form: `(count "hare")`, expected: `4`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

Halfway through the morning errand, Bob stopped in the orchard
with a basket of eggs and refused to move on until someone could
prove what the form `(count "hare")` evaluated to. Bob called it
impossible. Grace, walking up at an unhurried pace, simply
said: "Submit the count of "hare" to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a form whose evaluation gives the length of "hare".
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\")"}}]}
```

### G11-04 sample 3/N (form: `(count "tortoise")`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Henry said, with great whoops of laughter.
"Anyone with eyes can see what the count of "tortoise" — host-portable length comes to."
Robin, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(count "tortoise")` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the length of "tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G11-04 sample 4/N (form: `(count "hare")`, expected: `4`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Henry offered a small basket of eggs as a wager inside a cottage:
whoever guessed the result of `(count "hare")` first would keep them.
Charlie, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about the count of "hare"; the eggs,
after all, would still be there once Quill the goose laid the next
one.

What Clojure form computes the length of "hare"? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\")"}}]}
```

### G11-04 sample 5/N (form: `(count "tortoise")`, expected: `8`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Frank had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the farm, the
next entry was the count of "tortoise" — host-portable length. Helen peered over
his shoulder at the form `(count "tortoise")` and asked what
it would come out to.

Write a Clojure expression that computes the length of "tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

## G11-05: Import form

**examples (2):**

- ex0: form=`(do "(:import (java.util Date)) imports a host class" :imported)` expected=`':imported'`
    concept_phrase: `the (:import ...) ns clause for host classes`
    question_what: `the marker for the import-form lesson`
- ex1: form=`(do "import is a top-of-file ns clause" :studied)` expected=`':studied'`
    concept_phrase: `the role of import in a Clojure file`
    question_what: `the marker for studying import`

### G11-05 sample 1/N (form: `(do "(:import (java.util Date)) imports a host class" :imported)`, expected: `':imported'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

"There is no need to evaluate that," Beatrice said, as if the race were already won.
"Anyone with eyes can see what the (:import ...) ns clause for host classes comes to."
Fiona, who deep inside the cellar had grown used to such claims, asked
her to actually write the form `(do "(:import (java.util Date)) imports a host class" :imported)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for the marker for the import-form lesson.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 sample 2/N (form: `(do "import is a top-of-file ns clause" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Beatrice insisted the foreign-runtime forms were "just like
home." Charlie tapped a stone near the market where someone had
inscribed the role of import in a Clojure file above the day's egg-prices. "Then write
`(do "import is a top-of-file ns clause" :studied)` into the REPL," Charlie said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

Write a form whose evaluation gives the marker for studying import.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### G11-05 sample 3/N (form: `(do "(:import (java.util Date)) imports a host class" :imported)`, expected: `':imported'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

"There is no need to evaluate that," Carol said, swaggering through the underbrush.
"Anyone with eyes can see what the (:import ...) ns clause for host classes comes to."
David, who in the village had grown used to such claims, asked
her to actually write the form `(do "(:import (java.util Date)) imports a host class" :imported)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the marker for the import-form lesson.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-05 sample 4/N (form: `(do "import is a top-of-file ns clause" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A merchant's stall near the meadow sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
the role of import in a Clojure file. Frank copied the form `(do "import is a top-of-file ns clause" :studied)` from
the page into his ledger, and Emily agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

What Clojure form computes the marker for studying import? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"import is a top-of-file ns clause\" :studied)"}}]}
```

### G11-05 sample 5/N (form: `(do "(:import (java.util Date)) imports a host class" :imported)`, expected: `':imported'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

David had been trying to teach Frank how the REPL
works. "Here," he said, pointing to the (:import ...) ns clause for host classes.
"You hand the form `(do "(:import (java.util Date)) imports a host class" :imported)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the marker for the import-form lesson.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

## G11-06: new and dot-construct

**examples (2):**

- ex0: form=`(String. "hello")` expected=`'hello'`
    concept_phrase: `the constructor call (String. "hello")`
    question_what: `the string built by the dot-construct`
- ex1: form=`(new String "world")` expected=`'world'`
    concept_phrase: `the (new String "world") form`
    question_what: `the string built by (new ...)`

### G11-06 sample 1/N (form: `(String. "hello")`, expected: `'hello'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Henry and Edward had carried a basket of eggs by the farm
into territory where the REPL spoke to another runtime entirely.
Henry read the market sign and pointed at the constructor call (String. "hello"); the form
to submit, written in the foreign convention, was `(String. "hello")`.
Honk the goose had stayed at home, but his ledger came along.

Write a form whose evaluation gives the string built by the dot-construct.
---asst---
I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 sample 2/N (form: `(new String "world")`, expected: `'world'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A merchant's stall at the edge of the market sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
the (new String "world") form. Casey copied the form `(new String "world")` from
the page into their ledger, and Fiona agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

Question: write a Clojure expression for the string built by (new ...).
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### G11-06 sample 3/N (form: `(String. "hello")`, expected: `'hello'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched the constructor call (String. "hello") into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(String. "hello")` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the string built by the dot-construct? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-06 sample 4/N (form: `(new String "world")`, expected: `'world'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"This is not our farmyard," Emily said deep inside the kitchen, her eyes always on the path.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
Edward, with a hungry gleam in the eye, said he could read the
foreign form anyway. Emily sketched `(new String "world")` on a slate beside
the egg-basket; let the runtime, she insisted, declare what
the (new String "world") form returned.

Write a Clojure expression that computes the string built by (new ...).
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(new String \"world\")"}}]}
```

### G11-06 sample 5/N (form: `(String. "hello")`, expected: `'hello'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A wooden border-post in the barn marked the edge of the host runtime's
territory, and beneath it a stall weighed eggs in foreign measures.
The form chalked on the post — `(String. "hello")` — captured
the constructor call (String. "hello"). Fiona, regretting the hasty thought from a recent bad guess,
agreed for once that crossing into foreign syntax called for actual
evaluation, not greedy assumption.

Write a Clojure expression that computes the string built by the dot-construct.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

## G11-07: Arrays

**examples (2):**

- ex0: form=`(let [a (int-array [10 20 30])] (aget a 1))` expected=`20`
    concept_phrase: `indexing into an int-array via aget`
    question_what: `the value at index 1 of the array`
- ex1: form=`(let [a (int-array [1 2 3])] (alength a))` expected=`3`
    concept_phrase: `the length of an int-array via alength`
    question_what: `the length of the array`

### G11-07 sample 1/N (form: `(let [a (int-array [10 20 30])] (aget a 1))`, expected: `20`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Robin insisted the foreign-runtime forms were "just like
home." David tapped a stone by the market where someone had
inscribed indexing into an int-array via aget above the day's egg-prices. "Then write
`(let [a (int-array [10 20 30])] (aget a 1))` into the REPL," David said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 sample 2/N (form: `(let [a (int-array [1 2 3])] (alength a))`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

Edward insisted the foreign-runtime forms were "just like
home." David tapped a stone deep inside the kitchen where someone had
inscribed the length of an int-array via alength above the day's egg-prices. "Then write
`(let [a (int-array [1 2 3])] (alength a))` into the REPL," David said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

What Clojure form computes the length of the array? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### G11-07 sample 3/N (form: `(let [a (int-array [10 20 30])] (aget a 1))`, expected: `20`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A merchant's stall deep inside the cellar sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
indexing into an int-array via aget. Fiona copied the form `(let [a (int-array [10 20 30])] (aget a 1))` from
the page into her ledger, and Sam agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-07 sample 4/N (form: `(let [a (int-array [1 2 3])] (alength a))`, expected: `3`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today near the market, the
next entry was the length of an int-array via alength. George peered over
their shoulder at the form `(let [a (int-array [1 2 3])] (alength a))` and asked what
it would come out to.

What Clojure form computes the length of the array? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [1 2 3])] (alength a))"}}]}
```

### G11-07 sample 5/N (form: `(let [a (int-array [10 20 30])] (aget a 1))`, expected: `20`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

A wooden border-post deep inside a cottage marked the edge of the host runtime's
territory, and beneath it a stall weighed eggs in foreign measures.
The form chalked on the post — `(let [a (int-array [10 20 30])] (aget a 1))` — captured
indexing into an int-array via aget. Robin, thinking better of the rash impulse from a recent bad guess,
agreed for once that crossing into foreign syntax called for actual
evaluation, not greedy assumption.

What Clojure form computes the value at index 1 of the array? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

## G11-08: Type hints

**examples (2):**

- ex0: form=`(let [^String s "abc"] (.toUpperCase s))` expected=`'ABC'`
    concept_phrase: `a let-binding with a ^String type hint`
    question_what: `the uppercased string after a type-hinted binding`
- ex1: form=`(do "type hints are metadata that guide compilation" :studied)` expected=`':studied'`
    concept_phrase: `the role of ^Type metadata as a hint`
    question_what: `the marker keyword for the type-hint lesson`

### G11-08 sample 1/N (form: `(let [^String s "abc"] (.toUpperCase s))`, expected: `'ABC'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

At a wayside shrine in the village dedicated to safe interop and honest
weights, the day's offering was a let-binding with a ^String type hint. Bob knelt
and placed the form `(let [^String s "abc"] (.toUpperCase s))` on the stone beside a single egg
from the morning's basket. Oliver, watching, agreed to be the one
to submit it to the runtime.

Write a form whose evaluation gives the uppercased string after a type-hinted binding.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 sample 2/N (form: `(do "type hints are metadata that guide compilation" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Morgan said, puffed up with pride.
"Anyone with eyes can see what the role of ^Type metadata as a hint comes to."
George, who in the barn had grown used to such claims, asked
them to actually write the form `(do "type hints are metadata that guide compilation" :studied)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the marker keyword for the type-hint lesson.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### G11-08 sample 3/N (form: `(let [^String s "abc"] (.toUpperCase s))`, expected: `'ABC'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

A row of three coins sat on the kitchen table near the orchard, set out as a
wager between Diana and Jordan. The bet was
simple: predict what `(let [^String s "abc"] (.toUpperCase s))` would return. Diana,
tempted by the thought of plenty, was certain about the answer. Jordan asked
her, stepping deliberately, to actually write the form into the
REPL — a let-binding with a ^String type hint would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the uppercased string after a type-hinted binding.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-08 sample 4/N (form: `(do "type hints are metadata that guide compilation" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

Casey insisted the foreign-runtime forms were "just like
home." George tapped a stone deep inside the cellar where someone had
inscribed the role of ^Type metadata as a hint above the day's egg-prices. "Then write
`(do "type hints are metadata that guide compilation" :studied)` into the REPL," George said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

Question: write a Clojure expression for the marker keyword for the type-hint lesson.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"type hints are metadata that guide compilation\" :studied)"}}]}
```

### G11-08 sample 5/N (form: `(let [^String s "abc"] (.toUpperCase s))`, expected: `'ABC'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

A small audience of neighbors had gathered in the cellar to watch
Bob attempt to outguess Helen at reading the
REPL. Helen pointed to a let-binding with a ^String type hint and read out the form
aloud: `(let [^String s "abc"] (.toUpperCase s))`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

What Clojure form computes the uppercased string after a type-hinted binding? Submit it via `eval`.
---asst---
I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

## G11-09: Checked vs unchecked math

**examples (2):**

- ex0: form=`(+ 1 2)` expected=`3`
    concept_phrase: `the form (+ 1 2) under default checked math`
    question_what: `the result of (+ 1 2) under the default math regime`
- ex1: form=`(do "*unchecked-math* turns off overflow checking on prims" :studied)` expected=`':studied'`
    concept_phrase: `the *unchecked-math* dynamic var`
    question_what: `the marker for the checked/unchecked lesson`

### G11-09 sample 1/N (form: `(+ 1 2)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," George said, swaggering through the underbrush.
"Anyone with eyes can see what the form (+ 1 2) under default checked math comes to."
Oliver, who in the village had grown used to such claims, asked
him to actually write the form `(+ 1 2)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the result of (+ 1 2) under the default math regime.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 sample 2/N (form: `(do "*unchecked-math* turns off overflow checking on prims" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, David stopped inside the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do "*unchecked-math* turns off overflow checking on prims" :studied)` evaluated to. David called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit the *unchecked-math* dynamic var to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Question: write a Clojure expression for the marker for the checked/unchecked lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### G11-09 sample 3/N (form: `(+ 1 2)`, expected: `3`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

A small wooden notice nailed to a post at the edge of the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(+ 1 2)`.
George laughed, boasting at every turn, and declared it too easy.
Casey said, untroubled by what others thought, that the only honest way to know
the form (+ 1 2) under default checked math was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the result of (+ 1 2) under the default math regime.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-09 sample 4/N (form: `(do "*unchecked-math* turns off overflow checking on prims" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Charlie had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today inside a cottage, the
next entry was the *unchecked-math* dynamic var. Jordan peered over
his shoulder at the form `(do "*unchecked-math* turns off overflow checking on prims" :studied)` and asked what
it would come out to.

Write a Clojure expression that computes the marker for the checked/unchecked lesson.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"*unchecked-math* turns off overflow checking on prims\" :studied)"}}]}
```

### G11-09 sample 5/N (form: `(+ 1 2)`, expected: `3`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

Beatrice had been trying to teach George how the REPL
works. "Here," she said, pointing to the form (+ 1 2) under default checked math.
"You hand the form `(+ 1 2)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

## G11-10: ClojureScript overview

**examples (2):**

- ex0: form=`(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` expected=`':studied'`
    concept_phrase: `the ClojureScript host overview`
    question_what: `the marker for studying the cljs host`
- ex1: form=`(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` expected=`':cljs'`
    concept_phrase: `where ClojureScript runs and how interop looks`
    question_what: `the marker for the cljs-runtime lesson`

### G11-10 sample 1/N (form: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A merchant's stall deep inside the kitchen sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
the ClojureScript host overview. Alex copied the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` from
the page into their ledger, and Fiona agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

Write a Clojure expression that computes the marker for studying the cljs host.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 sample 2/N (form: `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`, expected: `':cljs'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` evaluated to. Morgan called it
impossible. Bob, walking up at an unhurried pace, simply
said: "Submit where ClojureScript runs and how interop looks to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

What Clojure form computes the marker for the cljs-runtime lesson? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### G11-10 sample 3/N (form: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

A small wooden notice nailed to a post in the orchard carried a puzzle for
the village. The riddle asked the reader to evaluate `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`.
Emily laughed, swaggering through the underbrush, and declared it too easy.
Carol said, saying very little, that the only honest way to know
the ClojureScript host overview was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the marker for studying the cljs host.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-10 sample 4/N (form: `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)`, expected: `':cljs'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"This is not our farmyard," Grace said in the village, her eyes always on the path.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
Robin, calculating in silence, said they could read the
foreign form anyway. Grace sketched `(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)` on a slate beside
the egg-basket; let the runtime, she insisted, declare what
where ClojureScript runs and how interop looks returned.

Write a form whose evaluation gives the marker for the cljs-runtime lesson.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"cljs runs in browsers and Node, with JS interop syntax\" :cljs)"}}]}
```

### G11-10 sample 5/N (form: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Fiona had been trying to teach Frank how the REPL
works. "Here," she said, pointing to the ClojureScript host overview.
"You hand the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the marker for studying the cljs host.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

## G11-11: cljs / JavaScript interop

**examples (2):**

- ex0: form=`(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` expected=`':studied'`
    concept_phrase: `the cljs-to-js interop syntax`
    question_what: `the marker for the cljs-js interop lesson`
- ex1: form=`(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` expected=`':cljs-interop'`
    concept_phrase: `two key cljs-js interop conventions`
    question_what: `the marker keyword for the conventions`

### G11-11 sample 1/N (form: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

A row of three coins sat on the kitchen table in the village, set out as a
wager between Charlie and George. The bet was
simple: predict what `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` would return. Charlie,
imagining all that might be gained, was certain about the answer. George asked
him, with steady, careful steps, to actually write the form into the
REPL — the cljs-to-js interop syntax would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the marker for the cljs-js interop lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 sample 2/N (form: `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`, expected: `':cljs-interop'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Halfway through the morning errand, Morgan stopped in the farm
with a basket of eggs and refused to move on until someone could
prove what the form `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` evaluated to. Morgan called it
impossible. Edward, walking up at an unhurried pace, simply
said: "Submit two key cljs-js interop conventions to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives the marker keyword for the conventions.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### G11-11 sample 3/N (form: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`, expected: `':studied'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
the cljs-to-js interop syntax — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the marker for the cljs-js interop lesson.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-11 sample 4/N (form: `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)`, expected: `':cljs-interop'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place near the village.

Sam offered a small basket of eggs as a wager by the village:
whoever guessed the result of `(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)` first would keep them.
Oliver, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about two key cljs-js interop conventions; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the marker keyword for the conventions.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"js/<name> namespaces JS globals; .- prefix marks field access\" :cljs-interop)"}}]}
```

### G11-11 sample 5/N (form: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"This is not our farmyard," Fiona said deep inside the kitchen, stepping deliberately.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
Sam, eyeing the next morning's gift, said they could read the
foreign form anyway. Fiona sketched `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)` on a slate beside
the egg-basket; let the runtime, she insisted, declare what
the cljs-to-js interop syntax returned.

Write a form whose evaluation gives the marker for the cljs-js interop lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

## G11-12: Basilisp overview (Python host)

**examples (2):**

- ex0: form=`(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` expected=`':studied'`
    concept_phrase: `the basilisp host overview`
    question_what: `the marker for studying basilisp`
- ex1: form=`(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` expected=`':basilisp'`
    concept_phrase: `how basilisp does Python interop`
    question_what: `the marker keyword for basilisp interop`

### G11-12 sample 1/N (form: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

A small audience of neighbors had gathered near the village to watch
Fiona attempt to outguess Helen at reading the
REPL. Helen pointed to the basilisp host overview and read out the form
aloud: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Question: write a Clojure expression for the marker for studying basilisp.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 sample 2/N (form: `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`, expected: `':basilisp'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

A row of three coins sat on the kitchen table in a cottage, set out as a
wager between Robin and Bob. The bet was
simple: predict what `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` would return. Robin,
with a hungry gleam in the eye, was certain about the answer. Bob asked
them, with steady, careful steps, to actually write the form into the
REPL — how basilisp does Python interop would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes the marker keyword for basilisp interop.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### G11-12 sample 3/N (form: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
the basilisp host overview — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the marker for studying basilisp.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-12 sample 4/N (form: `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)`, expected: `':basilisp'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A wooden border-post inside the barn marked the edge of the host runtime's
territory, and beneath it a stall weighed eggs in foreign measures.
The form chalked on the post — `(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)` — captured
how basilisp does Python interop. Sam, wondering how the temptation had risen from a recent bad guess,
agreed for once that crossing into foreign syntax called for actual
evaluation, not greedy assumption.

What Clojure form computes the marker keyword for basilisp interop? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp interops with Python via the same dot-syntax conventions\" :basilisp)"}}]}
```

### G11-12 sample 5/N (form: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A merchant's stall by the meadow sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
the basilisp host overview. Morgan copied the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` from
the page into their ledger, and Oliver agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer.

What Clojure form computes the marker for studying basilisp? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

## G11-13: Cross-platform .cljc and reader-conditionals

**examples (2):**

- ex0: form=`(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` expected=`':studied'`
    concept_phrase: `the reader-conditional #?(...) form`
    question_what: `the marker for the reader-conditional lesson`
- ex1: form=`(do ".cljc files share code across multiple hosts" :cljc)` expected=`':cljc'`
    concept_phrase: `the role of .cljc files`
    question_what: `the marker keyword for the .cljc lesson`

### G11-13 sample 1/N (form: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Sam insisted the foreign-runtime forms were "just like
home." Alice tapped a stone at the edge of the market where someone had
inscribed the reader-conditional #?(...) form above the day's egg-prices. "Then write
`(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` into the REPL," Alice said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

Write a form whose evaluation gives the marker for the reader-conditional lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 sample 2/N (form: `(do ".cljc files share code across multiple hosts" :cljc)`, expected: `':cljc'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

Helen offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do ".cljc files share code across multiple hosts" :cljc)` first would keep them.
Oliver, untroubled by what others thought, said it would be simpler to type the
form into the REPL than to bicker about the role of .cljc files; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Question: write a Clojure expression for the marker keyword for the .cljc lesson.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### G11-13 sample 3/N (form: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`, expected: `':studied'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

A wooden border-post inside a cottage marked the edge of the host runtime's
territory, and beneath it a stall weighed eggs in foreign measures.
The form chalked on the post — `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` — captured
the reader-conditional #?(...) form. Robin, thinking better of the rash impulse from a recent bad guess,
agreed for once that crossing into foreign syntax called for actual
evaluation, not greedy assumption.

What Clojure form computes the marker for the reader-conditional lesson? Submit it via `eval`.
---asst---
I write the interop form using the host's convention.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-13 sample 4/N (form: `(do ".cljc files share code across multiple hosts" :cljc)`, expected: `':cljc'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered in the kitchen to watch
Carol attempt to outguess Grace at reading the
REPL. Grace pointed to the role of .cljc files and read out the form
aloud: `(do ".cljc files share code across multiple hosts" :cljc)`. The crowd waited to see who would correctly
write the form to submit; Quill the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes the marker keyword for the .cljc lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \".cljc files share code across multiple hosts\" :cljc)"}}]}
```

### G11-13 sample 5/N (form: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`, expected: `':studied'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — the reader-conditional #?(...) form would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the marker for the reader-conditional lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

## G11-14: Debugging host leaks

**examples (2):**

- ex0: form=`(do "host stack traces leak through interop; learn to read them" :studied)` expected=`':studied'`
    concept_phrase: `the topic of debugging host-runtime leaks`
    question_what: `the marker for the host-leaks lesson`
- ex1: form=`(try (Math/sqrt 4) (catch Exception _ :err))` expected=`2.0`
    concept_phrase: `wrapping a host call in try/catch in case it leaks`
    question_what: `the result when the host call succeeds`

### G11-14 sample 1/N (form: `(do "host stack traces leak through interop; learn to read them" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

Grace and Diana had carried a basket of eggs by the village
into territory where the REPL spoke to another runtime entirely.
Grace read the market sign and pointed at the topic of debugging host-runtime leaks; the form
to submit, written in the foreign convention, was `(do "host stack traces leak through interop; learn to read them" :studied)`.
Quill the goose had stayed at home, but her ledger came along.

Write a Clojure expression that computes the marker for the host-leaks lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 sample 2/N (form: `(try (Math/sqrt 4) (catch Exception _ :err))`, expected: `2.0`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

George insisted the foreign-runtime forms were "just like
home." Edward tapped a stone in the market where someone had
inscribed wrapping a host call in try/catch in case it leaks above the day's egg-prices. "Then write
`(try (Math/sqrt 4) (catch Exception _ :err))` into the REPL," Edward said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

What Clojure form computes the result when the host call succeeds? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### G11-14 sample 3/N (form: `(do "host stack traces leak through interop; learn to read them" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

Edward and David had carried a basket of eggs in the meadow
into territory where the REPL spoke to another runtime entirely.
Edward read the market sign and pointed at the topic of debugging host-runtime leaks; the form
to submit, written in the foreign convention, was `(do "host stack traces leak through interop; learn to read them" :studied)`.
Plume the goose had stayed at home, but his ledger came along.

Question: write a Clojure expression for the marker for the host-leaks lesson.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

### G11-14 sample 4/N (form: `(try (Math/sqrt 4) (catch Exception _ :err))`, expected: `2.0`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the barn.

Jordan insisted the foreign-runtime forms were "just like
home." Casey tapped a stone in the barn where someone had
inscribed wrapping a host call in try/catch in case it leaks above the day's egg-prices. "Then write
`(try (Math/sqrt 4) (catch Exception _ :err))` into the REPL," Casey said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

Question: write a Clojure expression for the result when the host call succeeds.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(try (Math/sqrt 4) (catch Exception _ :err))"}}]}
```

### G11-14 sample 5/N (form: `(do "host stack traces leak through interop; learn to read them" :studied)`, expected: `':studied'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Bob insisted the foreign-runtime forms were "just like
home." Alice tapped a stone deep inside a cottage where someone had
inscribed the topic of debugging host-runtime leaks above the day's egg-prices. "Then write
`(do "host stack traces leak through interop; learn to read them" :studied)` into the REPL," Alice said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess."

What Clojure form computes the marker for the host-leaks lesson? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

