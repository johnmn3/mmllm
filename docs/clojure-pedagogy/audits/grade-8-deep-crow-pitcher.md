# crow-pitcher grade 8 — deep spot-check

5 records per subject for hand-audit.

---

## G8-01: Why polymorphism

### G8-01 record 1  •  form `(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))`  •  expected `None`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow etched a wager along the rim of a chipped pitcher
by the village: whoever predicted the result of `(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
a function speak that returns different strings for :crow vs :stork.

Write a Clojure expression that computes the form that defines speak via cond.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :crow) \"clever\" (= k :stork) \"long-beaked\" :else \"silent\"))"}}]}
```

### G8-01 record 2  •  form `(let [speak (fn [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked"))] (speak :stork))`  •  expected `'long-beaked'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A scrap of parchment, pinned to a tree at the edge of the hilltop, set out a rule that
all the woodland's birds would have to abide by. Korvus, boasting at every turn,
read it aloud: it was speak applied to :stork via cond-dispatch. Sable the crow said only the
REPL could confirm what `(let [speak (fn [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked"))] (speak :stork))` actually decided.

Question: write a Clojure expression for what speak returns for :stork.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :crow) \"clever\" (= k :stork) \"long-beaked\"))] (speak :stork))"}}]}
```

### G8-01 record 3  •  form `(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))`  •  expected `None`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the hilltop, the next entry was
a function speak that returns different strings for :crow vs :stork. Sable the crow peered over his shoulder
at the form `(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))` and asked what it would come out to.

Write a form whose evaluation gives the form that defines speak via cond.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :crow) \"clever\" (= k :stork) \"long-beaked\" :else \"silent\"))"}}]}
```

### G8-01 record 4  •  form `(let [speak (fn [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked"))] (speak :stork))`  •  expected `'long-beaked'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the market.

Sable the crow etched a wager along the rim of a chipped pitcher
at the edge of the market: whoever predicted the result of `(let [speak (fn [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked"))] (speak :stork))` first would set
the next day's foraging route. Korvus the crow, her eyes always on the path, said it
would be simpler to drop the form into the REPL than to bicker about
speak applied to :stork via cond-dispatch.

Write a Clojure expression that computes what speak returns for :stork.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :crow) \"clever\" (= k :stork) \"long-beaked\"))] (speak :stork))"}}]}
```

### G8-01 record 5  •  form `(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))`  •  expected `None`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Halfway through a long thirsty afternoon, Korvus the crow alighted
in the market and refused to fly on until someone could prove what the form
`(defn speak [k] (cond (= k :crow) "clever" (= k :stork) "long-beaked" :else "silent"))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a function speak that returns different strings for :crow vs :stork into the REPL. Whatever rises is the answer."

What Clojure form computes the form that defines speak via cond? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :crow) \"clever\" (= k :stork) \"long-beaked\" :else \"silent\"))"}}]}
```

## G8-02: deftype introduction

### G8-02 record 1  •  form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  expected `'grey'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Today at the edge of the meadow, Caw the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` captured
a deftype Pebble with a color field, then read color of an instance, and Caw suggested they hand it to the
REPL.

Write a form whose evaluation gives the color field of a Pebble instance.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

### G8-02 record 2  •  form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`  •  expected `7`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place near the meadow.

Today at the edge of the meadow, Korvus the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))` captured
a deftype Stone with a weight field, then read its weight, and Korvus suggested they hand it to the
REPL.

Question: write a Clojure expression for the weight of a Stone constructed with 7.

---

I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Stone [weight]) (.-weight (Stone. 7)))"}}]}
```

### G8-02 record 3  •  form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  expected `'grey'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the garden.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to a deftype Pebble with a color field, then read color of an instance.
"You hand the form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the color field of a Pebble instance.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

### G8-02 record 4  •  form `(do (deftype Stone [weight]) (.-weight (Stone. 7)))`  •  expected `7`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A scrap of parchment, pinned to a tree at the edge of the hilltop, set out a rule that
all the woodland's birds would have to abide by. Korvus, with great whoops of laughter,
read it aloud: it was a deftype Stone with a weight field, then read its weight. Sable the crow said only the
REPL could confirm what `(do (deftype Stone [weight]) (.-weight (Stone. 7)))` actually decided.

What Clojure form computes the weight of a Stone constructed with 7? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Stone [weight]) (.-weight (Stone. 7)))"}}]}
```

### G8-02 record 5  •  form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  expected `'grey'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place in the orchard.

"There is no need to evaluate that," Sable the crow said, puffed up with pride.
"Anyone with a sharp eye can see what a deftype Pebble with a color field, then read color of an instance comes to."
Caw the crow, who at the edge of the orchard had grown used to such claims, asked
them to actually write the form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))` and drop it
into the REPL — just to be sure.

What Clojure form computes the color field of a Pebble instance? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

## G8-03: defrecord introduction

### G8-03 record 1  •  form `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))`  •  expected `':clever'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust by the village: whoever guessed the result of `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))`
first would win the right to claim the next clear water they found.
Korvus the crow, untroubled by what others thought, said it was easier to ask the REPL
about a defrecord Bird with name and style fields, get :style than to argue.

Write a Clojure expression that computes the :style value of the Bird record.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Bird [name style]) (:style (->Bird \"crow\" :clever)))"}}]}
```

### G8-03 record 2  •  form `(do (defrecord Bird [name style]) (:name (->Bird "stork" :long-beaked)))`  •  expected `'stork'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the market.

Halfway through a long thirsty afternoon, Sable the crow alighted
at the edge of the market and refused to fly on until someone could prove what the form
`(do (defrecord Bird [name style]) (:name (->Bird "stork" :long-beaked)))` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the :name field of a Bird record into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the :name value of the Bird constructed with "stork".

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Bird [name style]) (:name (->Bird \"stork\" :long-beaked)))"}}]}
```

### G8-03 record 3  •  form `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))`  •  expected `':clever'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered at the edge of the village to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to a defrecord Bird with name and style fields, get :style and read out the form
aloud: `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a Clojure expression that computes the :style value of the Bird record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Bird [name style]) (:style (->Bird \"crow\" :clever)))"}}]}
```

### G8-03 record 4  •  form `(do (defrecord Bird [name style]) (:name (->Bird "stork" :long-beaked)))`  •  expected `'stork'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place by the farm.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the farm, the next entry was
the :name field of a Bird record. Sable the crow peered over her shoulder
at the form `(do (defrecord Bird [name style]) (:name (->Bird "stork" :long-beaked)))` and asked what it would come out to.

Write a Clojure expression that computes the :name value of the Bird constructed with "stork".

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Bird [name style]) (:name (->Bird \"stork\" :long-beaked)))"}}]}
```

### G8-03 record 5  •  form `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))`  •  expected `':clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the orchard, the next entry was
a defrecord Bird with name and style fields, get :style. Caw the crow peered over their shoulder
at the form `(do (defrecord Bird [name style]) (:style (->Bird "crow" :clever)))` and asked what it would come out to.

Write a form whose evaluation gives the :style value of the Bird record.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Bird [name style]) (:style (->Bird \"crow\" :clever)))"}}]}
```

## G8-04: Protocol definition

### G8-04 record 1  •  form `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the orchard.

A wooden sign nailed to a tree in the orchard carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol Pace (speed [this])) (some? Pace))`. Caw laughed, swaggering through the underbrush, and declared it
too easy. Sable said patiently that the only way to be sure of
a defprotocol Pace with a single method speed was to drop it into the REPL.

Write a form whose evaluation gives whether the Pace protocol was defined (a non-nil truthy value).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

### G8-04 record 2  •  form `(do (defprotocol Greet (hail [this])) (some? Greet))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. This was in the orchard.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Greet (hail [this])) (some? Greet))` first would drink
first when the water rose. Caw the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
a defprotocol Greet with one method hail.

Write a form whose evaluation gives whether Greet has been established.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### G8-04 record 3  •  form `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher in the meadow, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (some? Pace))` first would drink
first when the water rose. Sable the crow, saying very little, said it was
simpler to type the form into the REPL than to argue about
a defprotocol Pace with a single method speed.

Write a Clojure expression that computes whether the Pace protocol was defined (a non-nil truthy value).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

### G8-04 record 4  •  form `(do (defprotocol Greet (hail [this])) (some? Greet))`  •  expected `True`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Korvus the crow etched a wager along the rim of a chipped pitcher
on the hilltop: whoever predicted the result of `(do (defprotocol Greet (hail [this])) (some? Greet))` first would set
the next day's foraging route. Caw the crow, saying very little, said it
would be simpler to drop the form into the REPL than to bicker about
a defprotocol Greet with one method hail.

What Clojure form computes whether Greet has been established? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### G8-04 record 5  •  form `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a defprotocol Pace with a single method speed.
"You hand the form `(do (defprotocol Pace (speed [this])) (some? Pace))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Question: write a Clojure expression for whether the Pace protocol was defined (a non-nil truthy value).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

## G8-05: Protocol extension

### G8-05 record 1  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))`  •  expected `'clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today by the farm, the next entry was
a Pace protocol extended to String, then call speed on a string. Caw the crow peered over his shoulder
at the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))` and asked what it would come out to.

Write a Clojure expression that computes what speed returns when applied to "crow".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"clever\")) (speed \"crow\"))"}}]}
```

### G8-05 record 2  •  form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`  •  expected `':number'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A small audience of sparrows had gathered in the village to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to a Greet protocol extended to Long, then call hail on 7 and read out the form
aloud: `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the keyword hail returns for the number 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### G8-05 record 3  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))`  •  expected `'clever'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A scrap of parchment, pinned to a tree in the market, set out a rule that
all the woodland's birds would have to abide by. Caw, with great whoops of laughter,
read it aloud: it was a Pace protocol extended to String, then call speed on a string. Korvus the crow said only the
REPL could confirm what `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))` actually decided.

Write a Clojure expression that computes what speed returns when applied to "crow".

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"clever\")) (speed \"crow\"))"}}]}
```

### G8-05 record 4  •  form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`  •  expected `':number'`

```
Hunger and thirst had driven the Crow far from her usual perch. This was near the road.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to a Greet protocol extended to Long, then call hail on 7.
"You hand the form `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, near to giving up the search for water, agreed to try.

Write a Clojure expression that computes the keyword hail returns for the number 7.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### G8-05 record 5  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))`  •  expected `'clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Today near the market, Caw the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "clever")) (speed "crow"))` captured
a Pace protocol extended to String, then call speed on a string, and Caw suggested they hand it to the
REPL.

Question: write a Clojure expression for what speed returns when applied to "crow".

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"clever\")) (speed \"crow\"))"}}]}
```

## G8-06: Protocol method dispatch

### G8-06 record 1  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`  •  expected `':long-pace'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Korvus the crow said, swaggering through the underbrush.
"Anyone with a sharp eye can see what Pace dispatched on the class of its argument; called with 42 comes to."
Caw the crow, who at the edge of the meadow had grown used to such claims, asked
him to actually write the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the keyword speed returns for the integer 42.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

### G8-06 record 2  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`  •  expected `':string-pace'`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the meadow.

With a careful tap of his beak, Korvus the crow marked out a
wager in the dust by the meadow: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`
first would win the right to claim the next clear water they found.
Caw the crow, her eyes always on the path, said it was easier to ask the REPL
about Pace dispatched on a string argument than to argue.

Question: write a Clojure expression for the keyword speed returns for the string "x".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed \"x\"))"}}]}
```

### G8-06 record 3  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`  •  expected `':long-pace'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Today near the market, Caw the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` captured
Pace dispatched on the class of its argument; called with 42, and Caw suggested they hand it to the
REPL.

What Clojure form computes the keyword speed returns for the integer 42? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

### G8-06 record 4  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`  •  expected `':string-pace'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the hilltop.

With a careful tap of her beak, Caw the crow marked out a
wager in the dust near the hilltop: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed "x"))`
first would win the right to claim the next clear water they found.
Korvus the crow, saying very little, said it was easier to ask the REPL
about Pace dispatched on a string argument than to argue.

What Clojure form computes the keyword speed returns for the string "x"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed \"x\"))"}}]}
```

### G8-06 record 5  •  form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`  •  expected `':long-pace'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A wooden sign nailed to a tree along the road carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`. Korvus laughed, puffed up with pride, and declared it
too easy. Sable said patiently that the only way to be sure of
Pace dispatched on the class of its argument; called with 42 was to drop it into the REPL.

Question: write a Clojure expression for the keyword speed returns for the integer 42.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

## G8-07: Record implementing protocol

### G8-07 record 1  •  form `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))`  •  expected `':clever'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the hilltop.

Sable the crow had been trying to teach Caw the crow how the REPL
works. "Look here," they said, pointing to a defrecord Crow that implements Pace with speed -> :clever.
"You hand the form `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Caw, near to giving up the search for water, agreed to try.

Write a form whose evaluation gives the keyword speed returns for a Crow record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow \"Korvus\")))"}}]}
```

### G8-07 record 2  •  form `(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork "Stilt")))`  •  expected `':long-beaked'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Today at the edge of the orchard, Korvus the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork "Stilt")))` captured
a Stork record implementing Pace with speed -> :long-beaked, and Korvus suggested they hand it to the
REPL.

What Clojure form computes the keyword speed returns for a Stork record? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork \"Stilt\")))"}}]}
```

### G8-07 record 3  •  form `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))`  •  expected `':clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

At a moss-flecked pitcher on the hilltop, Caw the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))` first would drink
first when the water rose. Korvus the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
a defrecord Crow that implements Pace with speed -> :clever.

Question: write a Clojure expression for the keyword speed returns for a Crow record.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow \"Korvus\")))"}}]}
```

### G8-07 record 4  •  form `(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork "Stilt")))`  •  expected `':long-beaked'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Caw the crow had been trying to teach Sable the crow how the REPL
works. "Look here," she said, pointing to a Stork record implementing Pace with speed -> :long-beaked.
"You hand the form `(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork "Stilt")))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Sable, her beak cracked with thirst, agreed to try.

Write a Clojure expression that computes the keyword speed returns for a Stork record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Stork [name] Pace (speed [_] :long-beaked)) (speed (->Stork \"Stilt\")))"}}]}
```

### G8-07 record 5  •  form `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))`  •  expected `':clever'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow "Korvus")))` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
a defrecord Crow that implements Pace with speed -> :clever.

Question: write a Clojure expression for the keyword speed returns for a Crow record.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Crow [name] Pace (speed [_] :clever)) (speed (->Crow \"Korvus\")))"}}]}
```

## G8-08: Multimethod defmulti

### G8-08 record 1  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))`  •  expected `':clever'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher near the farm, Caw the crow sketched a small
wager: whoever guessed the result of `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
a defmulti pace that dispatches on :species, called with :crow.

Write a form whose evaluation gives what pace returns for {:species :crow}.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))"}}]}
```

### G8-08 record 2  •  form `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))`  •  expected `':hard'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to a defmulti tag dispatching on :kind.
"You hand the form `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, her beak cracked with thirst, agreed to try.

Write a Clojure expression that computes what tag returns for {:kind :stone}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))"}}]}
```

### G8-08 record 3  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))`  •  expected `':clever'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow and Korvus the crow alighted near the road on the rim of an old
pitcher where someone had scratched a defmulti pace that dispatches on :species, called with :crow. Caw,
with growing alarm, declared the answer beyond reach. Korvus, patient as
ever, suggested they drop the form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes what pace returns for {:species :crow}.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))"}}]}
```

### G8-08 record 4  •  form `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))`  •  expected `':hard'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A scrap of parchment, pinned to a tree at the edge of the hilltop, set out a rule that
all the woodland's birds would have to abide by. Korvus, puffed up with pride,
read it aloud: it was a defmulti tag dispatching on :kind. Caw the crow said only the
REPL could confirm what `(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))` actually decided.

Question: write a Clojure expression for what tag returns for {:kind :stone}.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :stone [_] :hard) (tag {:kind :stone}))"}}]}
```

### G8-08 record 5  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))`  •  expected `':clever'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

At a moss-flecked pitcher on the hilltop, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))` first would drink
first when the water rose. Sable the crow, without complaint, said it was
simpler to type the form into the REPL than to argue about
a defmulti pace that dispatches on :species, called with :crow.

Write a Clojure expression that computes what pace returns for {:species :crow}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (pace {:species :crow}))"}}]}
```

## G8-09: Multimethod defmethod

### G8-09 record 1  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))`  •  expected `':long-beaked'`

```
Hunger and thirst had driven the Crow far from her usual perch. All this took place near the road.

Korvus the crow and Sable the crow alighted near the road on the rim of an old
pitcher where someone had scratched two defmethod entries on pace, called with :stork. Korvus,
shouting until her voice cracked, declared the answer beyond reach. Sable, patient as
ever, suggested they drop the form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes what pace returns for {:species :stork}.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))"}}]}
```

### G8-09 record 2  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))`  •  expected `':unknown'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the orchard.

Korvus the crow and Caw the crow alighted by the orchard on the rim of an old
pitcher where someone had scratched a :default fallback method on pace, called with an unknown species. Korvus,
her hands trembling, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes what pace returns for {:species :robin} when :default falls through.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))"}}]}
```

### G8-09 record 3  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))`  •  expected `':long-beaked'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

Caw the crow had been keeping a small leather notebook of every form
she had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the farm, the next entry was
two defmethod entries on pace, called with :stork. Korvus the crow peered over her shoulder
at the form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))` and asked what it would come out to.

Write a Clojure expression that computes what pace returns for {:species :stork}.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))"}}]}
```

### G8-09 record 4  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))`  •  expected `':unknown'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place at the edge of the village.

A small audience of sparrows had gathered by the village to watch
Korvus the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to a :default fallback method on pace, called with an unknown species and read out the form
aloud: `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes what pace returns for {:species :robin} when :default falls through? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (defmethod pace :default [_] :unknown) (pace {:species :robin}))"}}]}
```

### G8-09 record 5  •  form `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))`  •  expected `':long-beaked'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened at the edge of the hilltop.

A wooden sign nailed to a tree at the edge of the hilltop carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))`. Caw laughed, puffed up with pride, and declared it
too easy. Korvus said patiently that the only way to be sure of
two defmethod entries on pace, called with :stork was to drop it into the REPL.

Write a form whose evaluation gives what pace returns for {:species :stork}.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :crow [_] :clever) (defmethod pace :stork [_] :long-beaked) (pace {:species :stork}))"}}]}
```

## G8-10: Multimethod vs protocol

### G8-10 record 1  •  form `(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))`  •  expected `'clever'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened at the edge of the farm.

A wooden sign nailed to a tree near the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))`. Korvus laughed, as if the race were already won, and declared it
too easy. Caw said patiently that the only way to be sure of
a defmulti dispatching on identity, with one method for :crow was to drop it into the REPL.

Write a Clojure expression that computes the string show returns for :crow.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :crow [_] \"clever\") (show :crow))"}}]}
```

### G8-10 record 2  •  form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "crow"))`  •  expected `'str-crow'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

Korvus the crow and Caw the crow alighted at the edge of the meadow on the rim of an old
pitcher where someone had scratched a Show protocol extended to String, called with "crow". Korvus,
shouting until her voice cracked, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "crow"))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

Write a Clojure expression that computes the string show returns for "crow" via protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"crow\"))"}}]}
```

### G8-10 record 3  •  form `(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))`  •  expected `'clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered near the village to watch
Caw the crow attempt to outwit Sable the crow at the rim of an old
pitcher. Sable pointed to a defmulti dispatching on identity, with one method for :crow and read out the form
aloud: `(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Write a form whose evaluation gives the string show returns for :crow.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :crow [_] \"clever\") (show :crow))"}}]}
```

### G8-10 record 4  •  form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "crow"))`  •  expected `'str-crow'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A small audience of sparrows had gathered by the garden to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to a Show protocol extended to String, called with "crow" and read out the form
aloud: `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "crow"))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for the string show returns for "crow" via protocol.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"crow\"))"}}]}
```

### G8-10 record 5  •  form `(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))`  •  expected `'clever'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the orchard and refused to fly on until someone could prove what the form
`(do (defmulti show identity) (defmethod show :crow [_] "clever") (show :crow))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
a defmulti dispatching on identity, with one method for :crow into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the string show returns for :crow.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :crow [_] \"clever\") (show :crow))"}}]}
```

## G8-11: Protocol vs Java interface

### G8-11 record 1  •  form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`  •  expected `':ran'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A scrap of parchment, pinned to a tree on the hilltop, set out a rule that
all the woodland's birds would have to abide by. Sable, with great whoops of laughter,
read it aloud: it was an IPace protocol (Clojure analogue of a Java interface) extended to String. Caw the crow said only the
REPL could confirm what `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))` actually decided.

Write a Clojure expression that computes the keyword run returns for "crow" via the protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"crow\"))"}}]}
```

### G8-11 record 2  •  form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`  •  expected `':ran'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow etched a wager along the rim of a chipped pitcher
along the road: whoever predicted the result of `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))` first would set
the next day's foraging route. Sable the crow, stepping deliberately, said it
would be simpler to drop the form into the REPL than to bicker about
an IPace protocol (Clojure analogue of a Java interface) extended to String.

Question: write a Clojure expression for the keyword run returns for "crow" via the protocol.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"crow\"))"}}]}
```

### G8-11 record 3  •  form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`  •  expected `':ran'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was by the market.

A small audience of sparrows had gathered by the market to watch
Sable the crow attempt to outwit Korvus the crow at the rim of an old
pitcher. Korvus pointed to an IPace protocol (Clojure analogue of a Java interface) extended to String and read out the form
aloud: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

What Clojure form computes the keyword run returns for "crow" via the protocol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"crow\"))"}}]}
```

### G8-11 record 4  •  form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`  •  expected `':ran'`

```
Hunger and thirst had driven the Crow far from her usual perch.

Korvus the crow and Caw the crow alighted in the village on the rim of an old
pitcher where someone had scratched an IPace protocol (Clojure analogue of a Java interface) extended to String. Korvus,
her hands trembling, declared the answer beyond reach. Caw, patient as
ever, suggested they drop the form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))` into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface.

What Clojure form computes the keyword run returns for "crow" via the protocol? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"crow\"))"}}]}
```

### G8-11 record 5  •  form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))`  •  expected `':ran'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Korvus the crow had been keeping a small leather notebook of every form
he had successfully dropped into the REPL — one entry per
stone, one rise per form. Today in the garden, the next entry was
an IPace protocol (Clojure analogue of a Java interface) extended to String. Sable the crow peered over his shoulder
at the form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "crow"))` and asked what it would come out to.

Write a Clojure expression that computes the keyword run returns for "crow" via the protocol.

---

I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"crow\"))"}}]}
```

## G8-12: extend-type on built-in types

### G8-12 record 1  •  form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`  •  expected `':number-pace'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Caw the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," she said, pointing to extend-type used to attach Pace to Long, called with 5.
"You hand the form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, with a thirst that hurt to bear, agreed to try.

Write a form whose evaluation gives the keyword speed returns for 5.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

### G8-12 record 2  •  form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "crow"))`  •  expected `':string-pace'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

A wooden sign nailed to a tree in the garden carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "crow"))`. Caw laughed, as if the race were already won, and declared it
too easy. Korvus said patiently that the only way to be sure of
extend-type attaching Pace to String was to drop it into the REPL.

Write a form whose evaluation gives the keyword speed returns for "crow" via extend-type.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed \"crow\"))"}}]}
```

### G8-12 record 3  •  form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`  •  expected `':number-pace'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened near the orchard.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today at the edge of the orchard, the next entry was
extend-type used to attach Pace to Long, called with 5. Korvus the crow peered over their shoulder
at the form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` and asked what it would come out to.

Question: write a Clojure expression for the keyword speed returns for 5.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

### G8-12 record 4  •  form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "crow"))`  •  expected `':string-pace'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. All this took place on the road.

A scrap of parchment, pinned to a tree along the road, set out a rule that
all the woodland's birds would have to abide by. Sable, with a smug grin,
read it aloud: it was extend-type attaching Pace to String. Korvus the crow said only the
REPL could confirm what `(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed "crow"))` actually decided.

Write a Clojure expression that computes the keyword speed returns for "crow" via extend-type.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.String Pace (speed [_] :string-pace)) (speed \"crow\"))"}}]}
```

### G8-12 record 5  •  form `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`  •  expected `':number-pace'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened in the orchard.

At a moss-flecked pitcher near the orchard, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` first would drink
first when the water rose. Caw the crow, stepping deliberately, said it was
simpler to type the form into the REPL than to argue about
extend-type used to attach Pace to Long, called with 5.

Write a form whose evaluation gives the keyword speed returns for 5.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

## G8-13: this-style vs fn-style

### G8-13 record 1  •  form `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))`  •  expected `'Korvus'`

```
Hunger and thirst had driven the Crow far from her usual perch.

A wooden sign nailed to a tree in the village carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))`. Korvus laughed, with great whoops of laughter, and declared it
too easy. Caw said patiently that the only way to be sure of
a protocol method using this to read a field was to drop it into the REPL.

Write a Clojure expression that computes the name returned by name-of for a Crow record.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow \"Korvus\")))"}}]}
```

### G8-13 record 2  •  form `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))`  •  expected `':grey'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

A scrap of parchment, pinned to a tree in the farm, set out a rule that
all the woodland's birds would have to abide by. Caw, boasting at every turn,
read it aloud: it was a Tagged protocol method that pulls :t off this. Sable the crow said only the
REPL could confirm what `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))` actually decided.

Write a Clojure expression that computes the :t value via tag-of for a Stone.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))"}}]}
```

### G8-13 record 3  •  form `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))`  •  expected `'Korvus'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.

"There is no need to evaluate that," Caw the crow said, puffed up with pride.
"Anyone with a sharp eye can see what a protocol method using this to read a field comes to."
Sable the crow, who by the farm had grown used to such claims, asked
her to actually write the form `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))` and drop it
into the REPL — just to be sure.

Question: write a Clojure expression for the name returned by name-of for a Crow record.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow \"Korvus\")))"}}]}
```

### G8-13 record 4  •  form `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))`  •  expected `':grey'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. It happened at the edge of the meadow.

Today near the meadow, Caw the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))` captured
a Tagged protocol method that pulls :t off this, and Caw suggested they hand it to the
REPL.

What Clojure form computes the :t value via tag-of for a Stone? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Stone [t] Tagged (tag-of [this] (:t this))) (tag-of (->Stone :grey)))"}}]}
```

### G8-13 record 5  •  form `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))`  •  expected `'Korvus'`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the market.

At a moss-flecked pitcher in the market, Sable the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow "Korvus")))` first would drink
first when the water rose. Caw the crow, with steady, careful steps, said it was
simpler to type the form into the REPL than to argue about
a protocol method using this to read a field.

Write a form whose evaluation gives the name returned by name-of for a Crow record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Crow [n] Named (name-of [this] (:n this))) (name-of (->Crow \"Korvus\")))"}}]}
```

## G8-14: Protocols don't inherit

### G8-14 record 1  •  form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  expected `[':a-impl', ':b-impl']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. It happened by the market.

At a moss-flecked pitcher in the market, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` first would drink
first when the water rose. Sable the crow, untroubled by what others thought, said it was
simpler to type the form into the REPL than to argue about
two independent protocols A and B both extended to String.

What Clojure form computes the pair [a-op b-op] when each protocol is used independently? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 record 2  •  form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  expected `[':a-impl', ':b-impl']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree at the edge of the meadow carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`. Caw laughed, with great whoops of laughter, and declared it
too easy. Korvus said patiently that the only way to be sure of
two independent protocols A and B both extended to String was to drop it into the REPL.

Question: write a Clojure expression for the pair [a-op b-op] when each protocol is used independently.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 record 3  •  form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  expected `[':a-impl', ':b-impl']`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. This was by the market.

Halfway through a long thirsty afternoon, Caw the crow alighted
at the edge of the market and refused to fly on until someone could prove what the form
`(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` evaluated to. Caw called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
two independent protocols A and B both extended to String into the REPL. Whatever rises is the answer."

Question: write a Clojure expression for the pair [a-op b-op] when each protocol is used independently.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 record 4  •  form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  expected `[':a-impl', ':b-impl']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. All this took place at the edge of the market.

"There is no need to evaluate that," Sable the crow said, with great whoops of laughter.
"Anyone with a sharp eye can see what two independent protocols A and B both extended to String comes to."
Caw the crow, who near the market had grown used to such claims, asked
them to actually write the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` and drop it
into the REPL — just to be sure.

Write a form whose evaluation gives the pair [a-op b-op] when each protocol is used independently.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-14 record 5  •  form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  expected `[':a-impl', ':b-impl']`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the village.

Sable the crow had been keeping a small leather notebook of every form
they had successfully dropped into the REPL — one entry per
stone, one rise per form. Today near the village, the next entry was
two independent protocols A and B both extended to String. Caw the crow peered over their shoulder
at the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` and asked what it would come out to.

Write a form whose evaluation gives the pair [a-op b-op] when each protocol is used independently.

---

I drop the form into the REPL like a stone into the pitcher.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

## G8-15: derive and isa? — multimethod hierarchy

### G8-15 record 1  •  form `(do (derive ::crow ::bird) (isa? ::crow ::bird))`  •  expected `True`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened at the edge of the farm.

Sable the crow had been trying to teach Korvus the crow how the REPL
works. "Look here," they said, pointing to deriving ::crow from ::bird and asking isa?.
"You hand the form `(do (derive ::crow ::bird) (isa? ::crow ::bird))` to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." Korvus, dry-throated and desperate, agreed to try.

What Clojure form computes whether ::crow isa? ::bird after derive? Submit it via `eval`.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::crow ::bird) (isa? ::crow ::bird))"}}]}
```

### G8-15 record 2  •  form `(isa? java.lang.Long java.lang.Number)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A small audience of sparrows had gathered by the garden to watch
Korvus the crow attempt to outwit Caw the crow at the rim of an old
pitcher. Caw pointed to the predicate (isa? Long Number) and read out the form
aloud: `(isa? java.lang.Long java.lang.Number)`. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit.

Question: write a Clojure expression for whether Long isa? Number.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

### G8-15 record 3  •  form `(isa? java.lang.String java.lang.Number)`  •  expected `False`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it.

A wooden sign nailed to a tree at the edge of the farm carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(isa? java.lang.String java.lang.Number)`. Caw laughed, with a smug grin, and declared it
too easy. Korvus said patiently that the only way to be sure of
the predicate (isa? String Number) was to drop it into the REPL.

Write a Clojure expression that computes whether String isa? Number.

---

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.String java.lang.Number)"}}]}
```

### G8-15 record 4  •  form `(do (derive ::crow ::bird) (isa? ::crow ::bird))`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was at the edge of the orchard.

Halfway through a long thirsty afternoon, Korvus the crow alighted
near the orchard and refused to fly on until someone could prove what the form
`(do (derive ::crow ::bird) (isa? ::crow ::bird))` evaluated to. Korvus called it impossible.
Caw the crow, gliding down at an unhurried pace, simply said: "Drop
deriving ::crow from ::bird and asking isa? into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives whether ::crow isa? ::bird after derive.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::crow ::bird) (isa? ::crow ::bird))"}}]}
```

### G8-15 record 5  •  form `(isa? java.lang.Long java.lang.Number)`  •  expected `True`

```
The Crow knew that water in the world is sometimes hidden where only the patient can reach it. This was near the garden.

Halfway through a long thirsty afternoon, Sable the crow alighted
at the edge of the garden and refused to fly on until someone could prove what the form
`(isa? java.lang.Long java.lang.Number)` evaluated to. Sable called it impossible.
Korvus the crow, gliding down at an unhurried pace, simply said: "Drop
the predicate (isa? Long Number) into the REPL. Whatever rises is the answer."

What Clojure form computes whether Long isa? Number? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

## G8-16: Abstract design with protocols

### G8-16 record 1  •  form `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))`  •  expected `[':hop', ':stride']`

```
It is said that wit, more than strength, is the friend of the thirsty Crow. This was in the farm.

Today by the farm, Sable the crow explained to Korvus the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))` captured
a Move protocol with two record implementations, mapped over instances, and Sable suggested they hand it to the
REPL.

Write a form whose evaluation gives the pair of step results for a Crow and a Stork.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))"}}]}
```

### G8-16 record 2  •  form `(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))`  •  expected `':clatter'`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

Halfway through a long thirsty afternoon, Korvus the crow alighted
by the meadow and refused to fly on until someone could prove what the form
`(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))` evaluated to. Korvus called it impossible.
Sable the crow, gliding down at an unhurried pace, simply said: "Drop
a Sound protocol with two implementations, called on a Stork into the REPL. Whatever rises is the answer."

Write a form whose evaluation gives the keyword cry returns for a Stork.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))"}}]}
```

### G8-16 record 3  •  form `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))`  •  expected `[':hop', ':stride']`

```
Hunger and thirst had driven the Crow far from her usual perch. It happened in the meadow.

Today by the meadow, Korvus the crow explained to Sable the crow that one
named operation could mean different things for different kinds of
creatures — a stork's beak was not a crow's beak, yet both could be
asked the same question. The form `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))` captured
a Move protocol with two record implementations, mapped over instances, and Korvus suggested they hand it to the
REPL.

What Clojure form computes the pair of step results for a Crow and a Stork? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))"}}]}
```

### G8-16 record 4  •  form `(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))`  •  expected `':clatter'`

```
A thirsty Crow had been searching all afternoon for water and was nearly ready to give up. It happened by the market.

A wooden sign nailed to a tree near the market carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate `(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))`. Caw laughed, boasting at every turn, and declared it
too easy. Sable said patiently that the only way to be sure of
a Sound protocol with two implementations, called on a Stork was to drop it into the REPL.

What Clojure form computes the keyword cry returns for a Stork? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Crow [] Sound (cry [_] :caw)) (defrecord Stork [] Sound (cry [_] :clatter)) (cry (->Stork)))"}}]}
```

### G8-16 record 5  •  form `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))`  •  expected `[':hop', ':stride']`

```
It is said that wit, more than strength, is the friend of the thirsty Crow.

At a moss-flecked pitcher atop the hilltop, Korvus the crow sketched a small
wager: whoever guessed the result of `(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))` first would drink
first when the water rose. Sable the crow, her eyes always on the path, said it was
simpler to type the form into the REPL than to argue about
a Move protocol with two record implementations, mapped over instances.

Write a Clojure expression that computes the pair of step results for a Crow and a Stork.

---

I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Crow [] Move (step [_] :hop)) (defrecord Stork [] Move (step [_] :stride)) (mapv step [(->Crow) (->Stork)]))"}}]}
```

