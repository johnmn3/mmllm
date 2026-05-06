# Grade 8 goose-eggs — deep spot-check

5 rendered records per subject (16 subjects × 5 = 80 records).

Read each record carefully. Look for paper cuts the audit harness can't catch by structural rules: pronoun mismatches, verb-prep mismatches, subplot/example fit, plan-pool fit, punctuation collisions, cliché repetition, etc.

---

## G8-01: Why polymorphism

**examples (2):**

- ex0: form=`(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))` expected=`None`
    concept_phrase: `a function speak that returns different strings for :hare vs :tortoise`
    question_what: `the form that defines speak via cond`
- ex1: form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k :tortoise) "steady"))] (speak :tortoise))` expected=`'steady'`
    concept_phrase: `speak applied to :tortoise via cond-dispatch`
    question_what: `what speak returns for :tortoise`

### G8-01 sample 1/N (form: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Today near the market, Alice explained to Carol that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))` captured a function speak that returns different strings for :hare vs :tortoise,
and Alice suggested they hand it to the REPL while Plume the goose
waited by the basket.

Write a Clojure expression that computes the form that defines speak via cond.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
```

### G8-01 sample 2/N (form: `(let [speak (fn [k] (cond (= k :hare) "swift" (= k :tortoise) "steady"))] (speak :tortoise))`, expected: `'steady'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A scrap of parchment, pinned to the barn door at the edge of the farm, set out a rule
that all egg-owners in the village would have to abide by. Frank,
calculating in silence, read it aloud: it was speak applied to :tortoise via cond-dispatch. Alice
said only the REPL could confirm what `(let [speak (fn [k] (cond (= k :hare) "swift" (= k :tortoise) "steady"))] (speak :tortoise))` actually decided,
the way only the basket could confirm the morning's true count.

Question: write a Clojure expression for what speak returns for :tortoise.
---asst---
I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\"))] (speak :tortoise))"}}]}
```

### G8-01 sample 3/N (form: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened in the cellar.

Edward had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the cellar, the
next entry was a function speak that returns different strings for :hare vs :tortoise. Casey peered over
his shoulder at the form `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))` and asked what
it would come out to.

What Clojure form computes the form that defines speak via cond? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
```

### G8-01 sample 4/N (form: `(let [speak (fn [k] (cond (= k :hare) "swift" (= k :tortoise) "steady"))] (speak :tortoise))`, expected: `'steady'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened deep inside a cottage.

Carol and Emily stood inside a cottage where someone had
scratched speak applied to :tortoise via cond-dispatch into a smooth slate by the egg-basket.
Emily, with a smug grin, declared the answer was obvious — no need to
evaluate anything. Carol, untroubled by what others thought, suggested they
actually submit the form `(let [speak (fn [k] (cond (= k :hare) "swift" (= k :tortoise) "steady"))] (speak :tortoise))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

Write a form whose evaluation gives what speak returns for :tortoise.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\"))] (speak :tortoise))"}}]}
```

### G8-01 sample 5/N (form: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`, expected: `None`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Bob and Henry. The bet was
simple: predict what `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))` would return. Bob,
with hands itching to count more, was certain about the answer. Henry asked
him, saying very little, to actually write the form into the
REPL — a function speak that returns different strings for :hare vs :tortoise would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the form that defines speak via cond.
---asst---
I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
```

## G8-02: deftype introduction

**examples (2):**

- ex0: form=`(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` expected=`'grey'`
    concept_phrase: `a deftype Pebble with a color field, then read color of an instance`
    question_what: `the color field of a Pebble instance`
- ex1: form=`(do (deftype Stone [weight]) (.-weight (Stone. 7)))` expected=`7`
    concept_phrase: `a deftype Stone with a weight field, then read its weight`
    question_what: `the weight of a Stone constructed with 7`

### G8-02 sample 1/N (form: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`, expected: `'grey'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside the cellar.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today inside the cellar, the
next entry was a deftype Pebble with a color field, then read color of an instance. Oliver peered over
his shoulder at the form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` and asked what
it would come out to.

Write a Clojure expression that computes the color field of a Pebble instance.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

### G8-02 sample 2/N (form: `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`, expected: `7`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A scrap of parchment, pinned to the barn door at the edge of the village, set out a rule
that all egg-owners in the village would have to abide by. Frank,
with a hungry gleam in the eye, read it aloud: it was a deftype Stone with a weight field, then read its weight. Oliver
said only the REPL could confirm what `(do (deftype Stone [weight]) (.-weight (Stone. 7)))` actually decided,
the way only the basket could confirm the morning's true count.

Write a Clojure expression that computes the weight of a Stone constructed with 7.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Stone [weight]) (.-weight (Stone. 7)))"}}]}
```

### G8-02 sample 3/N (form: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`, expected: `'grey'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was at the edge of the farm.

Casey had been trying to teach Helen how the REPL
works. "Here," they said, pointing to a deftype Pebble with a color field, then read color of an instance.
"You hand the form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes the color field of a Pebble instance.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

### G8-02 sample 4/N (form: `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`, expected: `7`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside the kitchen.

Fiona had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the kitchen, the
next entry was a deftype Stone with a weight field, then read its weight. Charlie peered over
her shoulder at the form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))` and asked what
it would come out to.

What Clojure form computes the weight of a Stone constructed with 7? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Stone [weight]) (.-weight (Stone. 7)))"}}]}
```

### G8-02 sample 5/N (form: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`, expected: `'grey'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. It happened by the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` first would set the asking
price for the morning's eggs. Edward, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
a deftype Pebble with a color field, then read color of an instance — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the color field of a Pebble instance.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

## G8-03: defrecord introduction

**examples (2):**

- ex0: form=`(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))` expected=`':swift'`
    concept_phrase: `a defrecord Runner with name and pace fields, get :pace`
    question_what: `the :pace value of the Runner record`
- ex1: form=`(do (defrecord Runner [name pace]) (:name (->Runner "tortoise" :steady)))` expected=`'tortoise'`
    concept_phrase: `the :name field of a Runner record`
    question_what: `the :name value of the Runner constructed with "tortoise"`

### G8-03 sample 1/N (form: `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))`, expected: `':swift'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place at the edge of the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Beatrice and Henry. The bet was
simple: predict what `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))` would return. Beatrice,
tempted by the thought of plenty, was certain about the answer. Henry asked
her, stepping deliberately, to actually write the form into the
REPL — a defrecord Runner with name and pace fields, get :pace would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the :pace value of the Runner record.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"hare\" :swift)))"}}]}
```

### G8-03 sample 2/N (form: `(do (defrecord Runner [name pace]) (:name (->Runner "tortoise" :steady)))`, expected: `'tortoise'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Robin offered a small basket of eggs as a wager at the edge of the farm:
whoever guessed the result of `(do (defrecord Runner [name pace]) (:name (->Runner "tortoise" :steady)))` first would keep them.
Alex, without complaint, said it would be simpler to type the
form into the REPL than to bicker about the :name field of a Runner record; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for the :name value of the Runner constructed with "tortoise".
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:name (->Runner \"tortoise\" :steady)))"}}]}
```

### G8-03 sample 3/N (form: `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))`, expected: `':swift'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the meadow.

Today by the meadow, Grace explained to Robin that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))` captured a defrecord Runner with name and pace fields, get :pace,
and Grace suggested they hand it to the REPL while Plume the goose
waited by the basket.

Question: write a Clojure expression for the :pace value of the Runner record.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"hare\" :swift)))"}}]}
```

### G8-03 sample 4/N (form: `(do (defrecord Runner [name pace]) (:name (->Runner "tortoise" :steady)))`, expected: `'tortoise'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Alice and Diana stood in the cellar where someone had
scratched the :name field of a Runner record into a smooth slate by the egg-basket.
Diana, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Alice, with steady, careful steps, suggested they
actually submit the form `(do (defrecord Runner [name pace]) (:name (->Runner "tortoise" :steady)))` to the REPL, the way
Quill the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the :name value of the Runner constructed with "tortoise"? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:name (->Runner \"tortoise\" :steady)))"}}]}
```

### G8-03 sample 5/N (form: `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))`, expected: `':swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Carol said, with great whoops of laughter.
"Anyone with eyes can see what a defrecord Runner with name and pace fields, get :pace comes to."
Emily, who at the edge of the market had grown used to such claims, asked
her to actually write the form `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the :pace value of the Runner record.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"hare\" :swift)))"}}]}
```

## G8-04: Protocol definition

**examples (2):**

- ex0: form=`(do (defprotocol Pace (speed [this])) (some? Pace))` expected=`True`
    concept_phrase: `a defprotocol Pace with a single method speed`
    question_what: `whether the Pace protocol was defined (a non-nil truthy value)`
- ex1: form=`(do (defprotocol Greet (hail [this])) (some? Greet))` expected=`True`
    concept_phrase: `a defprotocol Greet with one method hail`
    question_what: `whether Greet has been established`

### G8-04 sample 1/N (form: `(do (defprotocol Pace (speed [this])) (some? Pace))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Alice had been trying to teach Charlie how the REPL
works. "Here," she said, pointing to a defprotocol Pace with a single method speed.
"You hand the form `(do (defprotocol Pace (speed [this])) (some? Pace))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

Write a Clojure expression that computes whether the Pace protocol was defined (a non-nil truthy value).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

### G8-04 sample 2/N (form: `(do (defprotocol Greet (hail [this])) (some? Greet))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was at the edge of the orchard.

Grace had been trying to teach Bob how the REPL
works. "Here," she said, pointing to a defprotocol Greet with one method hail.
"You hand the form `(do (defprotocol Greet (hail [this])) (some? Greet))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives whether Greet has been established.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### G8-04 sample 3/N (form: `(do (defprotocol Pace (speed [this])) (some? Pace))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, Henry stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defprotocol Pace (speed [this])) (some? Pace))` evaluated to. Henry called it
impossible. Robin, walking up at an unhurried pace, simply
said: "Submit a defprotocol Pace with a single method speed to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a form whose evaluation gives whether the Pace protocol was defined (a non-nil truthy value).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

### G8-04 sample 4/N (form: `(do (defprotocol Greet (hail [this])) (some? Greet))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A row of three coins sat on the kitchen table inside a cottage, set out as a
wager between Henry and Charlie. The bet was
simple: predict what `(do (defprotocol Greet (hail [this])) (some? Greet))` would return. Henry,
calculating in silence, was certain about the answer. Charlie asked
him, untroubled by what others thought, to actually write the form into the
REPL — a defprotocol Greet with one method hail would be settled the moment the runtime
answered, not before.

What Clojure form computes whether Greet has been established? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### G8-04 sample 5/N (form: `(do (defprotocol Pace (speed [this])) (some? Pace))`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small audience of neighbors had gathered near the farm to watch
Helen attempt to outguess Frank at reading the
REPL. Frank pointed to a defprotocol Pace with a single method speed and read out the form
aloud: `(do (defprotocol Pace (speed [this])) (some? Pace))`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes whether the Pace protocol was defined (a non-nil truthy value).
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

## G8-05: Protocol extension

**examples (2):**

- ex0: form=`(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))` expected=`'swift'`
    concept_phrase: `a Pace protocol extended to String, then call speed on a string`
    question_what: `what speed returns when applied to "hare"`
- ex1: form=`(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))` expected=`':number'`
    concept_phrase: `a Greet protocol extended to Long, then call hail on 7`
    question_what: `the keyword hail returns for the number 7`

### G8-05 sample 1/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))`, expected: `'swift'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Halfway through the morning errand, Beatrice stopped deep inside the cellar
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))` evaluated to. Beatrice called it
impossible. Fiona, walking up at an unhurried pace, simply
said: "Submit a Pace protocol extended to String, then call speed on a string to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Question: write a Clojure expression for what speed returns when applied to "hare".
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"swift\")) (speed \"hare\"))"}}]}
```

### G8-05 sample 2/N (form: `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`, expected: `':number'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small wooden notice nailed to a post near the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`.
Beatrice laughed, swaggering through the underbrush, and declared it too easy.
Charlie said, with steady, careful steps, that the only honest way to know
a Greet protocol extended to Long, then call hail on 7 was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the keyword hail returns for the number 7.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### G8-05 sample 3/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))`, expected: `'swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was by the village.

Halfway through the morning errand, Carol stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))` evaluated to. Carol called it
impossible. David, walking up at an unhurried pace, simply
said: "Submit a Pace protocol extended to String, then call speed on a string to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes what speed returns when applied to "hare".
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"swift\")) (speed \"hare\"))"}}]}
```

### G8-05 sample 4/N (form: `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`, expected: `':number'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A scrap of parchment, pinned to the barn door near the meadow, set out a rule
that all egg-owners in the village would have to abide by. Emily,
with a glint of impatience, read it aloud: it was a Greet protocol extended to Long, then call hail on 7. Frank
said only the REPL could confirm what `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))` actually decided,
the way only the basket could confirm the morning's true count.

What Clojure form computes the keyword hail returns for the number 7? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### G8-05 sample 5/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))`, expected: `'swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the kitchen.

Frank offered a small basket of eggs as a wager inside the kitchen:
whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))` first would keep them.
David, without complaint, said it would be simpler to type the
form into the REPL than to bicker about a Pace protocol extended to String, then call speed on a string; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Question: write a Clojure expression for what speed returns when applied to "hare".
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"swift\")) (speed \"hare\"))"}}]}
```

## G8-06: Protocol method dispatch

**examples (2):**

- ex0: form=`(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` expected=`':long-pace'`
    concept_phrase: `Pace dispatched on the class of its argument; called with 42`
    question_what: `the keyword speed returns for the integer 42`
- ex1: form=`(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))` expected=`':string-pace'`
    concept_phrase: `Pace dispatched on a string argument`
    question_what: `the keyword speed returns for the string "x"`

### G8-06 sample 1/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`, expected: `':long-pace'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Henry had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today by the farm, the
next entry was Pace dispatched on the class of its argument; called with 42. Edward peered over
his shoulder at the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` and asked what
it would come out to.

Write a form whose evaluation gives the keyword speed returns for the integer 42.
---asst---
I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

### G8-06 sample 2/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`, expected: `':string-pace'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A scrap of parchment, pinned to the barn door at the edge of the market, set out a rule
that all egg-owners in the village would have to abide by. Fiona,
imagining all that might be gained, read it aloud: it was Pace dispatched on a string argument. Casey
said only the REPL could confirm what `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))` actually decided,
the way only the basket could confirm the morning's true count.

Question: write a Clojure expression for the keyword speed returns for the string "x".
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed \"x\"))"}}]}
```

### G8-06 sample 3/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`, expected: `':long-pace'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the market.

Frank and Helen stood in the market where someone had
scratched Pace dispatched on the class of its argument; called with 42 into a smooth slate by the egg-basket.
Helen, swaggering through the underbrush, declared the answer was obvious — no need to
evaluate anything. Frank, her eyes always on the path, suggested they
actually submit the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` to the REPL, the way
Honk the goose laid one egg at a time: one form, one returned value.

What Clojure form computes the keyword speed returns for the integer 42? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

### G8-06 sample 4/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`, expected: `':string-pace'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Edward said, swaggering through the underbrush.
"Anyone with eyes can see what Pace dispatched on a string argument comes to."
Emily, who deep inside the kitchen had grown used to such claims, asked
him to actually write the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a Clojure expression that computes the keyword speed returns for the string "x".
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed \"x\"))"}}]}
```

### G8-06 sample 5/N (form: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`, expected: `':long-pace'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place inside the barn.

A small wooden notice nailed to a post in the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`.
Fiona laughed, puffed up with pride, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
Pace dispatched on the class of its argument; called with 42 was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a Clojure expression that computes the keyword speed returns for the integer 42.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

## G8-07: Record implementing protocol

**examples (2):**

- ex0: form=`(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))` expected=`':swift'`
    concept_phrase: `a defrecord Hare that implements Pace with speed -> :swift`
    question_what: `the keyword speed returns for a Hare record`
- ex1: form=`(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise "Shelly")))` expected=`':steady'`
    concept_phrase: `a Tortoise record implementing Pace with speed -> :steady`
    question_what: `the keyword speed returns for a Tortoise record`

### G8-07 sample 1/N (form: `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`, expected: `':swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Today by the market, David explained to Robin that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))` captured a defrecord Hare that implements Pace with speed -> :swift,
and David suggested they hand it to the REPL while Quill the goose
waited by the basket.

What Clojure form computes the keyword speed returns for a Hare record? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare \"Pip\")))"}}]}
```

### G8-07 sample 2/N (form: `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise "Shelly")))`, expected: `':steady'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. All this took place deep inside the kitchen.

Today deep inside the kitchen, David explained to Edward that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise "Shelly")))` captured a Tortoise record implementing Pace with speed -> :steady,
and David suggested they hand it to the REPL while Plume the goose
waited by the basket.

What Clojure form computes the keyword speed returns for a Tortoise record? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise \"Shelly\")))"}}]}
```

### G8-07 sample 3/N (form: `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`, expected: `':swift'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A scrap of parchment, pinned to the barn door deep inside the cellar, set out a rule
that all egg-owners in the village would have to abide by. Sam,
with a glint of impatience, read it aloud: it was a defrecord Hare that implements Pace with speed -> :swift. Fiona
said only the REPL could confirm what `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))` actually decided,
the way only the basket could confirm the morning's true count.

What Clojure form computes the keyword speed returns for a Hare record? Submit it via `eval`.
---asst---
I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare \"Pip\")))"}}]}
```

### G8-07 sample 4/N (form: `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise "Shelly")))`, expected: `':steady'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

A small audience of neighbors had gathered near the market to watch
George attempt to outguess Casey at reading the
REPL. Casey pointed to a Tortoise record implementing Pace with speed -> :steady and read out the form
aloud: `(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise "Shelly")))`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

What Clojure form computes the keyword speed returns for a Tortoise record? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Tortoise [name] Pace (speed [_] :steady)) (speed (->Tortoise \"Shelly\")))"}}]}
```

### G8-07 sample 5/N (form: `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`, expected: `':swift'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened inside a cottage.

A small wooden notice nailed to a post deep inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`.
Robin laughed, with a smug grin, and declared it too easy.
Helen said, untroubled by what others thought, that the only honest way to know
a defrecord Hare that implements Pace with speed -> :swift was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the keyword speed returns for a Hare record? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare \"Pip\")))"}}]}
```

## G8-08: Multimethod defmulti

**examples (2):**

- ex0: form=`(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))` expected=`':swift'`
    concept_phrase: `a defmulti pace that dispatches on :species, called with :hare`
    question_what: `what pace returns for {:species :hare}`
- ex1: form=`(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))` expected=`':hard'`
    concept_phrase: `a defmulti tag dispatching on :kind`
    question_what: `what tag returns for {:kind :stone}`

### G8-08 sample 1/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`, expected: `':swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened near the village.

Today in the village, Bob explained to Oliver that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))` captured a defmulti pace that dispatches on :species, called with :hare,
and Bob suggested they hand it to the REPL while Plume the goose
waited by the basket.

Write a form whose evaluation gives what pace returns for {:species :hare}.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
```

### G8-08 sample 2/N (form: `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))`, expected: `':hard'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

Halfway through the morning errand, Morgan stopped in the barn
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))` evaluated to. Morgan called it
impossible. George, walking up at an unhurried pace, simply
said: "Submit a defmulti tag dispatching on :kind to the REPL. Whatever comes back is
the answer." Honk the goose watched the basket, calm as ever.

Write a Clojure expression that computes what tag returns for {:kind :stone}.
---asst---
I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))"}}]}
```

### G8-08 sample 3/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`, expected: `':swift'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. This was at the edge of the orchard.

At a small stall near the orchard, someone had chalked a wager: whoever
predicted the result of `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))` first would set the asking
price for the morning's eggs. Jordan, stepping deliberately, said it
was easier to type the form into the REPL than to argue about
a defmulti pace that dispatches on :species, called with :hare — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for what pace returns for {:species :hare}.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
```

### G8-08 sample 4/N (form: `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))`, expected: `':hard'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was deep inside the cellar.

A small wooden notice nailed to a post deep inside the cellar carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))`.
Casey laughed, puffed up with pride, and declared it too easy.
George said, stepping deliberately, that the only honest way to know
a defmulti tag dispatching on :kind was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Question: write a Clojure expression for what tag returns for {:kind :stone}.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))"}}]}
```

### G8-08 sample 5/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`, expected: `':swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. This was inside the cellar.

Helen had been trying to teach Bob how the REPL
works. "Here," she said, pointing to a defmulti pace that dispatches on :species, called with :hare.
"You hand the form `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Plume the goose gives one egg each morning, no more, no less."

What Clojure form computes what pace returns for {:species :hare}? Submit it via `eval`.
---asst---
I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
```

## G8-09: Multimethod defmethod

**examples (2):**

- ex0: form=`(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))` expected=`':steady'`
    concept_phrase: `two defmethod entries on pace, called with :tortoise`
    question_what: `what pace returns for {:species :tortoise}`
- ex1: form=`(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))` expected=`':unknown'`
    concept_phrase: `a :default fallback method on pace, called with an unknown species`
    question_what: `what pace returns for {:species :owl} when :default falls through`

### G8-09 sample 1/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))`, expected: `':steady'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Halfway through the morning errand, George stopped in the village
with a basket of eggs and refused to move on until someone could
prove what the form `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))` evaluated to. George called it
impossible. Oliver, walking up at an unhurried pace, simply
said: "Submit two defmethod entries on pace, called with :tortoise to the REPL. Whatever comes back is
the answer." Quill the goose watched the basket, calm as ever.

Write a Clojure expression that computes what pace returns for {:species :tortoise}.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))"}}]}
```

### G8-09 sample 2/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))`, expected: `':unknown'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Fiona had been trying to teach David how the REPL
works. "Here," she said, pointing to a :default fallback method on pace, called with an unknown species.
"You hand the form `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Question: write a Clojure expression for what pace returns for {:species :owl} when :default falls through.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))"}}]}
```

### G8-09 sample 3/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))`, expected: `':steady'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened in the orchard.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Honk the goose were tallied in another column. Today at the edge of the orchard, the
next entry was two defmethod entries on pace, called with :tortoise. George peered over
their shoulder at the form `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))` and asked what
it would come out to.

Write a form whose evaluation gives what pace returns for {:species :tortoise}.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))"}}]}
```

### G8-09 sample 4/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))`, expected: `':unknown'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A small audience of neighbors had gathered inside a cottage to watch
Jordan attempt to outguess Charlie at reading the
REPL. Charlie pointed to a :default fallback method on pace, called with an unknown species and read out the form
aloud: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))`. The crowd waited to see who would correctly
write the form to submit; Plume the goose watched too, untroubled by
the noise.

Write a Clojure expression that computes what pace returns for {:species :owl} when :default falls through.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (defmethod pace :default [_] :unknown) (pace {:species :owl}))"}}]}
```

### G8-09 sample 5/N (form: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))`, expected: `':steady'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened in the cellar.

George offered a small basket of eggs as a wager in the cellar:
whoever guessed the result of `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))` first would keep them.
Beatrice, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about two defmethod entries on pace, called with :tortoise; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for what pace returns for {:species :tortoise}.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))"}}]}
```

## G8-10: Multimethod vs protocol

**examples (2):**

- ex0: form=`(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))` expected=`'swift'`
    concept_phrase: `a defmulti dispatching on identity, with one method for :hare`
    question_what: `the string show returns for :hare`
- ex1: form=`(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "hare"))` expected=`'str-hare'`
    concept_phrase: `a Show protocol extended to String, called with "hare"`
    question_what: `the string show returns for "hare" via protocol`

### G8-10 sample 1/N (form: `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))`, expected: `'swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. It happened inside the kitchen.

A scrap of parchment, pinned to the barn door deep inside the kitchen, set out a rule
that all egg-owners in the village would have to abide by. Fiona,
with hands itching to count more, read it aloud: it was a defmulti dispatching on identity, with one method for :hare. Alex
said only the REPL could confirm what `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))` actually decided,
the way only the basket could confirm the morning's true count.

Write a Clojure expression that computes the string show returns for :hare.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :hare [_] \"swift\") (show :hare))"}}]}
```

### G8-10 sample 2/N (form: `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "hare"))`, expected: `'str-hare'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Bob had been trying to teach Morgan how the REPL
works. "Here," he said, pointing to a Show protocol extended to String, called with "hare".
"You hand the form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "hare"))` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Honk the goose gives one egg each morning, no more, no less."

What Clojure form computes the string show returns for "hare" via protocol? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"hare\"))"}}]}
```

### G8-10 sample 3/N (form: `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))`, expected: `'swift'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place at the edge of the orchard.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the orchard, the
next entry was a defmulti dispatching on identity, with one method for :hare. Emily peered over
her shoulder at the form `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))` and asked what
it would come out to.

Write a form whose evaluation gives the string show returns for :hare.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :hare [_] \"swift\") (show :hare))"}}]}
```

### G8-10 sample 4/N (form: `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "hare"))`, expected: `'str-hare'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Robin said, swaggering through the underbrush.
"Anyone with eyes can see what a Show protocol extended to String, called with "hare" comes to."
Grace, who in the village had grown used to such claims, asked
them to actually write the form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "hare"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the string show returns for "hare" via protocol.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"hare\"))"}}]}
```

### G8-10 sample 5/N (form: `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))`, expected: `'swift'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Frank offered a small basket of eggs as a wager in the meadow:
whoever guessed the result of `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))` first would keep them.
Fiona, her eyes always on the path, said it would be simpler to type the
form into the REPL than to bicker about a defmulti dispatching on identity, with one method for :hare; the eggs,
after all, would still be there once Honk the goose laid the next
one.

Write a form whose evaluation gives the string show returns for :hare.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :hare [_] \"swift\") (show :hare))"}}]}
```

## G8-11: Protocol vs Java interface

**examples (1):**

- ex0: form=`(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` expected=`':ran'`
    concept_phrase: `an IPace protocol (Clojure analogue of a Java interface) extended to String`
    question_what: `the keyword run returns for "hare" via the protocol`

### G8-11 sample 1/N (form: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`, expected: `':ran'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the village.

At a small stall in the village, someone had chalked a wager: whoever
predicted the result of `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` first would set the asking
price for the morning's eggs. George, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
an IPace protocol (Clojure analogue of a Java interface) extended to String — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the keyword run returns for "hare" via the protocol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

### G8-11 sample 2/N (form: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`, expected: `':ran'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

At a small stall by the orchard, someone had chalked a wager: whoever
predicted the result of `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` first would set the asking
price for the morning's eggs. Grace, untroubled by what others thought, said it
was easier to type the form into the REPL than to argue about
an IPace protocol (Clojure analogue of a Java interface) extended to String — Honk the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a form whose evaluation gives the keyword run returns for "hare" via the protocol.
---asst---
I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

### G8-11 sample 3/N (form: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`, expected: `':ran'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

"There is no need to evaluate that," Sam said, swaggering through the underbrush.
"Anyone with eyes can see what an IPace protocol (Clojure analogue of a Java interface) extended to String comes to."
Fiona, who deep inside the kitchen had grown used to such claims, asked
them to actually write the form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Write a form whose evaluation gives the keyword run returns for "hare" via the protocol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

### G8-11 sample 4/N (form: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`, expected: `':ran'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

A row of three coins sat on the kitchen table deep inside a cottage, set out as a
wager between George and Frank. The bet was
simple: predict what `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` would return. George,
calculating in silence, was certain about the answer. Frank asked
him, with steady, careful steps, to actually write the form into the
REPL — an IPace protocol (Clojure analogue of a Java interface) extended to String would be settled the moment the runtime
answered, not before.

What Clojure form computes the keyword run returns for "hare" via the protocol? Submit it via `eval`.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

### G8-11 sample 5/N (form: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`, expected: `':ran'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Morgan and Robin. The bet was
simple: predict what `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` would return. Morgan,
imagining all that might be gained, was certain about the answer. Robin asked
them, her eyes always on the path, to actually write the form into the
REPL — an IPace protocol (Clojure analogue of a Java interface) extended to String would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes the keyword run returns for "hare" via the protocol.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

## G8-12: extend-type on built-in types

**examples (2):**

- ex0: form=`(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` expected=`':number-pace'`
    concept_phrase: `extend-type used to attach Pace to Long, called with 5`
    question_what: `the keyword speed returns for 5`
- ex1: form=`(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "hare"))` expected=`':string-pace'`
    concept_phrase: `extend-type attaching Pace to String`
    question_what: `the keyword speed returns for "hare" via extend-type`

### G8-12 sample 1/N (form: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`, expected: `':number-pace'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. This was near the village.

Fiona offered a small basket of eggs as a wager near the village:
whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` first would keep them.
Helen, saying very little, said it would be simpler to type the
form into the REPL than to bicker about extend-type used to attach Pace to Long, called with 5; the eggs,
after all, would still be there once Plume the goose laid the next
one.

Question: write a Clojure expression for the keyword speed returns for 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

### G8-12 sample 2/N (form: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "hare"))`, expected: `':string-pace'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. All this took place deep inside a cottage.

At a small stall in a cottage, someone had chalked a wager: whoever
predicted the result of `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "hare"))` first would set the asking
price for the morning's eggs. Bob, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
extend-type attaching Pace to String — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the keyword speed returns for "hare" via extend-type.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed \"hare\"))"}}]}
```

### G8-12 sample 3/N (form: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`, expected: `':number-pace'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened at the edge of the market.

At a small stall near the market, someone had chalked a wager: whoever
predicted the result of `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` first would set the asking
price for the morning's eggs. Robin, without complaint, said it
was easier to type the form into the REPL than to argue about
extend-type used to attach Pace to Long, called with 5 — Quill the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Question: write a Clojure expression for the keyword speed returns for 5.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

### G8-12 sample 4/N (form: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "hare"))`, expected: `':string-pace'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A small wooden notice nailed to a post inside the barn carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "hare"))`.
Sam laughed, swaggering through the underbrush, and declared it too easy.
Morgan said, stepping deliberately, that the only honest way to know
extend-type attaching Pace to String was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the keyword speed returns for "hare" via extend-type? Submit it via `eval`.
---asst---
Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed \"hare\"))"}}]}
```

### G8-12 sample 5/N (form: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`, expected: `':number-pace'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A scrap of parchment, pinned to the barn door by the meadow, set out a rule
that all egg-owners in the village would have to abide by. Oliver,
imagining all that might be gained, read it aloud: it was extend-type used to attach Pace to Long, called with 5. Morgan
said only the REPL could confirm what `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` actually decided,
the way only the basket could confirm the morning's true count.

What Clojure form computes the keyword speed returns for 5? Submit it via `eval`.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

## G8-13: this-style vs fn-style

**examples (2):**

- ex0: form=`(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))` expected=`'Pip'`
    concept_phrase: `a protocol method using this to read a field`
    question_what: `the name returned by name-of for a Hare record`
- ex1: form=`(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))` expected=`':grey'`
    concept_phrase: `a Tagged protocol method that pulls :t off this`
    question_what: `the :t value via tag-of for a Stone`

### G8-13 sample 1/N (form: `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`, expected: `'Pip'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A small wooden notice nailed to a post at the edge of the market carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`.
Sam laughed, with great whoops of laughter, and declared it too easy.
Alice said, untroubled by what others thought, that the only honest way to know
a protocol method using this to read a field was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

Write a form whose evaluation gives the name returned by name-of for a Hare record.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare \"Pip\")))"}}]}
```

### G8-13 sample 2/N (form: `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))`, expected: `':grey'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place near the meadow.

A row of three coins sat on the kitchen table in the meadow, set out as a
wager between Helen and Oliver. The bet was
simple: predict what `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))` would return. Helen,
tempted by the thought of plenty, was certain about the answer. Oliver asked
her, untroubled by what others thought, to actually write the form into the
REPL — a Tagged protocol method that pulls :t off this would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the :t value via tag-of for a Stone.
---asst---
I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))"}}]}
```

### G8-13 sample 3/N (form: `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`, expected: `'Pip'`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way. It happened in a cottage.

A small wooden notice nailed to a post inside a cottage carried a puzzle for
the village. The riddle asked the reader to evaluate `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`.
Robin laughed, with great whoops of laughter, and declared it too easy.
Diana said, untroubled by what others thought, that the only honest way to know
a protocol method using this to read a field was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing.

What Clojure form computes the name returned by name-of for a Hare record? Submit it via `eval`.
---asst---
I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare \"Pip\")))"}}]}
```

### G8-13 sample 4/N (form: `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))`, expected: `':grey'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol offered a small basket of eggs as a wager in the kitchen:
whoever guessed the result of `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))` first would keep them.
Grace, without complaint, said it would be simpler to type the
form into the REPL than to bicker about a Tagged protocol method that pulls :t off this; the eggs,
after all, would still be there once Quill the goose laid the next
one.

Write a Clojure expression that computes the :t value via tag-of for a Stone.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))"}}]}
```

### G8-13 sample 5/N (form: `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`, expected: `'Pip'`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

A row of three coins sat on the kitchen table at the edge of the orchard, set out as a
wager between Emily and Sam. The bet was
simple: predict what `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))` would return. Emily,
thoughts already on more, was certain about the answer. Sam asked
her, saying very little, to actually write the form into the
REPL — a protocol method using this to read a field would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the name returned by name-of for a Hare record.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare \"Pip\")))"}}]}
```

## G8-14: Protocols don't inherit

**examples (1):**

- ex0: form=`(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` expected=`[':a-impl', ':b-impl']`
    concept_phrase: `two independent protocols A and B both extended to String`
    question_what: `the pair [a-op b-op] when each protocol is used independently`

### G8-14 sample 1/N (form: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`, expected: `[':a-impl', ':b-impl']`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened at the edge of the village.

Grace had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today by the village, the
next entry was two independent protocols A and B both extended to String. Diana peered over
her shoulder at the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` and asked what
it would come out to.

Write a Clojure expression that computes the pair [a-op b-op] when each protocol is used independently.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 sample 2/N (form: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`, expected: `[':a-impl', ':b-impl']`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened near the meadow.

Edward had been keeping a small leather ledger of every form
he had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today in the meadow, the
next entry was two independent protocols A and B both extended to String. David peered over
his shoulder at the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` and asked what
it would come out to.

Question: write a Clojure expression for the pair [a-op b-op] when each protocol is used independently.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 sample 3/N (form: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`, expected: `[':a-impl', ':b-impl']`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold. It happened deep inside a cottage.

Today deep inside a cottage, Alice explained to Bob that one named
operation could mean different things for different kinds of birds — a
goose's morning yield was not a hen's yield, yet both could be asked
the same question. The form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` captured two independent protocols A and B both extended to String,
and Alice suggested they hand it to the REPL while Quill the goose
waited by the basket.

What Clojure form computes the pair [a-op b-op] when each protocol is used independently? Submit it via `eval`.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 sample 4/N (form: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`, expected: `[':a-impl', ':b-impl']`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

Edward had been trying to teach George how the REPL
works. "Here," he said, pointing to two independent protocols A and B both extended to String.
"You hand the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way Quill the goose gives one egg each morning, no more, no less."

Write a form whose evaluation gives the pair [a-op b-op] when each protocol is used independently.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 sample 5/N (form: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`, expected: `[':a-impl', ':b-impl']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

At a small stall inside the kitchen, someone had chalked a wager: whoever
predicted the result of `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` first would set the asking
price for the morning's eggs. Carol, with steady, careful steps, said it
was easier to type the form into the REPL than to argue about
two independent protocols A and B both extended to String — Plume the goose was about to lay another egg
anyway, and the morning would not wait for guessing.

Write a Clojure expression that computes the pair [a-op b-op] when each protocol is used independently.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

## G8-15: derive and isa? — multimethod hierarchy

**examples (3):**

- ex0: form=`(do (derive ::hare ::runner) (isa? ::hare ::runner))` expected=`True`
    concept_phrase: `deriving ::hare from ::runner and asking isa?`
    question_what: `whether ::hare isa? ::runner after derive`
- ex1: form=`(isa? java.lang.Long java.lang.Number)` expected=`True`
    concept_phrase: `the predicate (isa? Long Number)`
    question_what: `whether Long isa? Number`
- ex2: form=`(isa? java.lang.String java.lang.Number)` expected=`False`
    concept_phrase: `the predicate (isa? String Number)`
    question_what: `whether String isa? Number`

### G8-15 sample 1/N (form: `(do (derive ::hare ::runner) (isa? ::hare ::runner))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. This was near the village.

A row of three coins sat on the kitchen table by the village, set out as a
wager between Emily and Robin. The bet was
simple: predict what `(do (derive ::hare ::runner) (isa? ::hare ::runner))` would return. Emily,
with hands itching to count more, was certain about the answer. Robin asked
her, saying very little, to actually write the form into the
REPL — deriving ::hare from ::runner and asking isa? would be settled the moment the runtime
answered, not before.

Write a Clojure expression that computes whether ::hare isa? ::runner after derive.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::hare ::runner) (isa? ::hare ::runner))"}}]}
```

### G8-15 sample 2/N (form: `(isa? java.lang.Long java.lang.Number)`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience. All this took place in the cellar.

"There is no need to evaluate that," David said, with a smug grin.
"Anyone with eyes can see what the predicate (isa? Long Number) comes to."
Charlie, who deep inside the cellar had grown used to such claims, asked
him to actually write the form `(isa? java.lang.Long java.lang.Number)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for whether Long isa? Number.
---asst---
Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

### G8-15 sample 3/N (form: `(isa? java.lang.String java.lang.Number)`, expected: `False`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both. All this took place in the farm.

George and Morgan stood near the farm where someone had
scratched the predicate (isa? String Number) into a smooth slate by the egg-basket.
Morgan, boasting at every turn, declared the answer was obvious — no need to
evaluate anything. George, without complaint, suggested they
actually submit the form `(isa? java.lang.String java.lang.Number)` to the REPL, the way
Plume the goose laid one egg at a time: one form, one returned value.

What Clojure form computes whether String isa? Number? Submit it via `eval`.
---asst---
Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.String java.lang.Number)"}}]}
```

### G8-15 sample 4/N (form: `(do (derive ::hare ::runner) (isa? ::hare ::runner))`, expected: `True`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Casey had been keeping a small leather ledger of every form
they had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today at the edge of the meadow, the
next entry was deriving ::hare from ::runner and asking isa?. Alex peered over
their shoulder at the form `(do (derive ::hare ::runner) (isa? ::hare ::runner))` and asked what
it would come out to.

Write a form whose evaluation gives whether ::hare isa? ::runner after derive.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::hare ::runner) (isa? ::hare ::runner))"}}]}
```

### G8-15 sample 5/N (form: `(isa? java.lang.Long java.lang.Number)`, expected: `True`)

```
Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.

"There is no need to evaluate that," Robin said, with a smug grin.
"Anyone with eyes can see what the predicate (isa? Long Number) comes to."
Diana, who near the orchard had grown used to such claims, asked
them to actually write the form `(isa? java.lang.Long java.lang.Number)` and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance.

Question: write a Clojure expression for whether Long isa? Number.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

## G8-16: Abstract design with protocols

**examples (2):**

- ex0: form=`(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))` expected=`[':leap', ':plod']`
    concept_phrase: `a Move protocol with two record implementations, mapped over instances`
    question_what: `the pair of step results for a Hare and a Tortoise`
- ex1: form=`(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))` expected=`':hiss'`
    concept_phrase: `a Sound protocol with two implementations, called on a Tortoise`
    question_what: `the keyword cry returns for a Tortoise`

### G8-16 sample 1/N (form: `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))`, expected: `[':leap', ':plod']`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

Alice had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today by the meadow, the
next entry was a Move protocol with two record implementations, mapped over instances. Sam peered over
her shoulder at the form `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))` and asked what
it would come out to.

Write a form whose evaluation gives the pair of step results for a Hare and a Tortoise.
---asst---
Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))"}}]}
```

### G8-16 sample 2/N (form: `(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))`, expected: `':hiss'`)

```
There was once an extraordinary goose whose every morning gift was a single egg of pure gold.

A row of three coins sat on the kitchen table deep inside the barn, set out as a
wager between Fiona and Frank. The bet was
simple: predict what `(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))` would return. Fiona,
with hands itching to count more, was certain about the answer. Frank asked
her, untroubled by what others thought, to actually write the form into the
REPL — a Sound protocol with two implementations, called on a Tortoise would be settled the moment the runtime
answered, not before.

Question: write a Clojure expression for the keyword cry returns for a Tortoise.
---asst---
{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))"}}]}
```

### G8-16 sample 3/N (form: `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))`, expected: `[':leap', ':plod']`)

```
A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.

A row of three coins sat on the kitchen table at the edge of the farm, set out as a
wager between Bob and Sam. The bet was
simple: predict what `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))` would return. Bob,
calculating in silence, was certain about the answer. Sam asked
him, stepping deliberately, to actually write the form into the
REPL — a Move protocol with two record implementations, mapped over instances would be settled the moment the runtime
answered, not before.

Write a form whose evaluation gives the pair of step results for a Hare and a Tortoise.
---asst---
I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))"}}]}
```

### G8-16 sample 4/N (form: `(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))`, expected: `':hiss'`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Carol had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Quill the goose were tallied in another column. Today in the market, the
next entry was a Sound protocol with two implementations, called on a Tortoise. David peered over
her shoulder at the form `(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))` and asked what
it would come out to.

Write a Clojure expression that computes the keyword cry returns for a Tortoise.
---asst---
I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Hare [] Sound (cry [_] :thump)) (defrecord Tortoise [] Sound (cry [_] :hiss)) (cry (->Tortoise)))"}}]}
```

### G8-16 sample 5/N (form: `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))`, expected: `[':leap', ':plod']`)

```
The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.

Emily had been keeping a small leather ledger of every form
she had successfully evaluated, the same way the eggs from
Plume the goose were tallied in another column. Today inside the barn, the
next entry was a Move protocol with two record implementations, mapped over instances. Bob peered over
her shoulder at the form `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))` and asked what
it would come out to.

Write a Clojure expression that computes the pair of step results for a Hare and a Tortoise.
---asst---
I submit the form patiently and read whatever comes back.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))"}}]}
```

