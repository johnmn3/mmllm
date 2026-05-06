# Boy-wolf Grade 8 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G8-01: Why polymorphism

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))` • **expected**: `None`

**concept_phrase**: `a function speak that returns different strings for :wolf vs :flock`

**question_what**: `the form that defines speak via cond`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Today near the woods, Alice explained to Pat that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))`
captured a function speak that returns different strings for :wolf vs :flock, and Alice suggested they hand it to the
REPL.

Write a Clojure expression that computes the form that defines speak via cond.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "bleat"))] (speak :flock))` • **expected**: `'bleat'`

**concept_phrase**: `speak applied to :flock via cond-dispatch`

**question_what**: `what speak returns for :flock`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked speak applied to :flock via cond-dispatch on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "bleat"))] (speak :flock))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes what speak returns for :flock.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\"))] (speak :flock))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))` • **expected**: `None`

**concept_phrase**: `a function speak that returns different strings for :wolf vs :flock`

**question_what**: `the form that defines speak via cond`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today by the village the next entry was
a function speak that returns different strings for :wolf vs :flock. Pat peered over his shoulder
at the form `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the form that defines speak via cond.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "bleat"))] (speak :flock))` • **expected**: `'bleat'`

**concept_phrase**: `speak applied to :flock via cond-dispatch`

**question_what**: `what speak returns for :flock`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(let [speak (fn [k] (cond (= k :wolf) "howl" (= k :flock) "bleat"))] (speak :flock))`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
speak applied to :flock via cond-dispatch was to put it in the REPL.

What Clojure form computes what speak returns for :flock? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [speak (fn [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\"))] (speak :flock))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))` • **expected**: `None`

**concept_phrase**: `a function speak that returns different strings for :wolf vs :flock`

**question_what**: `the form that defines speak via cond`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone on the road where someone had
chalked a function speak that returns different strings for :wolf vs :flock on a flat board. Lou, with great whoops of laughter,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))` to the REPL — the village had stopped trusting answers
that weren't checked.

What Clojure form computes the form that defines speak via cond? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))"}}]}
```

---

## G8-02: deftype introduction

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))` • **expected**: `'amber'`

**concept_phrase**: `a deftype Lantern with a color field, then read color of an instance`

**question_what**: `the color field of a Lantern instance`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked a deftype Lantern with a color field, then read color of an instance on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(do (deftype Lantern [color]) (.-color (Lantern. "amber")))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the color field of a Lantern instance.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (deftype Crook [length]) (.-length (Crook. 7)))` • **expected**: `7`

**concept_phrase**: `a deftype Crook with a length field, then read its length`

**question_what**: `the length of a Crook constructed with 7`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

A scrap of parchment, pinned to the village board at the edge of the woods, set out a
rule that every honest villager would have to abide by. Tom,
boasting at every turn, read it aloud: it was a deftype Crook with a length field, then read its length. Grace
said only the REPL could confirm what `(do (deftype Crook [length]) (.-length (Crook. 7)))` actually
decided.

Write a Clojure expression that computes the length of a Crook constructed with 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Crook [length]) (.-length (Crook. 7)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))` • **expected**: `'amber'`

**concept_phrase**: `a deftype Lantern with a color field, then read color of an instance`

**question_what**: `the color field of a Lantern instance`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

A wooden notice nailed to a post in the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))`. Pat
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
a deftype Lantern with a color field, then read color of an instance was to put it in the REPL.

Write a form whose evaluation gives the color field of a Lantern instance.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (deftype Crook [length]) (.-length (Crook. 7)))` • **expected**: `7`

**concept_phrase**: `a deftype Crook with a length field, then read its length`

**question_what**: `the length of a Crook constructed with 7`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (deftype Crook [length]) (.-length (Crook. 7)))`, and the page
heading read a deftype Crook with a length field, then read its length. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the length of a Crook constructed with 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Crook [length]) (.-length (Crook. 7)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))` • **expected**: `'amber'`

**concept_phrase**: `a deftype Lantern with a color field, then read color of an instance`

**question_what**: `the color field of a Lantern instance`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to a deftype Lantern with a color field, then read color of an instance and read out the
form aloud: `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the color field of a Lantern instance? Submit it via `eval`.

---

I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))"}}]}
```

---

## G8-03: defrecord introduction

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))` • **expected**: `':hilltop'`

**concept_phrase**: `a defrecord Watcher with name and post fields, get :post`

**question_what**: `the :post value of the Watcher record`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to a defrecord Watcher with name and post fields, get :post.
"You hand the form `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the :post value of the Watcher record.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Watcher [name post]) (:post (->Watcher \"shepherd\" :hilltop)))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defrecord Watcher [name post]) (:name (->Watcher "elder" :village)))` • **expected**: `'elder'`

**concept_phrase**: `the :name field of a Watcher record`

**question_what**: `the :name value of the Watcher constructed with "elder"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to the :name field of a Watcher record.
"You hand the form `(do (defrecord Watcher [name post]) (:name (->Watcher "elder" :village)))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the :name value of the Watcher constructed with "elder".

---

I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Watcher [name post]) (:name (->Watcher \"elder\" :village)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))` • **expected**: `':hilltop'`

**concept_phrase**: `a defrecord Watcher with name and post fields, get :post`

**question_what**: `the :post value of the Watcher record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))`, and the line
above it read a defrecord Watcher with name and post fields, get :post. Frank handed the page to
Pat, who, yawning at the soft moss, agreed to write it out properly.

Write a Clojure expression that computes the :post value of the Watcher record.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Watcher [name post]) (:post (->Watcher \"shepherd\" :hilltop)))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defrecord Watcher [name post]) (:name (->Watcher "elder" :village)))` • **expected**: `'elder'`

**concept_phrase**: `the :name field of a Watcher record`

**question_what**: `the :name value of the Watcher constructed with "elder"`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the :name field of a Watcher record. Bob read
out the form `(do (defrecord Watcher [name post]) (:name (->Watcher "elder" :village)))` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the :name value of the Watcher constructed with "elder"? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Watcher [name post]) (:name (->Watcher \"elder\" :village)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))` • **expected**: `':hilltop'`

**concept_phrase**: `a defrecord Watcher with name and post fields, get :post`

**question_what**: `the :post value of the Watcher record`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A scrap of parchment, pinned to the village board by the village, set out a
rule that every honest villager would have to abide by. Will,
boasting at every turn, read it aloud: it was a defrecord Watcher with name and post fields, get :post. Robin
said only the REPL could confirm what `(do (defrecord Watcher [name post]) (:post (->Watcher "shepherd" :hilltop)))` actually
decided.

Write a Clojure expression that computes the :post value of the Watcher record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Watcher [name post]) (:post (->Watcher \"shepherd\" :hilltop)))"}}]}
```

---

## G8-04: Protocol definition

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (some? Alarm))` • **expected**: `True`

**concept_phrase**: `a defprotocol Alarm with a single method sound`

**question_what**: `whether the Alarm protocol was defined (a non-nil truthy value)`

```
The boy on the hill thought the trick clever the first time he played it.

A scrap of parchment, pinned to the village board near the farm, set out a
rule that every honest villager would have to abide by. Pat,
with great whoops of laughter, read it aloud: it was a defprotocol Alarm with a single method sound. Bob
said only the REPL could confirm what `(do (defprotocol Alarm (sound [this])) (some? Alarm))` actually
decided.

Write a Clojure expression that computes whether the Alarm protocol was defined (a non-nil truthy value).

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (some? Alarm))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Greet (hail [this])) (some? Greet))` • **expected**: `True`

**concept_phrase**: `a defprotocol Greet with one method hail`

**question_what**: `whether Greet has been established`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened at the edge of the village.

A scrap of parchment, pinned to the village board near the village, set out a
rule that every honest villager would have to abide by. Jess,
swaggering through the underbrush, read it aloud: it was a defprotocol Greet with one method hail. George
said only the REPL could confirm what `(do (defprotocol Greet (hail [this])) (some? Greet))` actually
decided.

Write a Clojure expression that computes whether Greet has been established.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (some? Alarm))` • **expected**: `True`

**concept_phrase**: `a defprotocol Alarm with a single method sound`

**question_what**: `whether the Alarm protocol was defined (a non-nil truthy value)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what a defprotocol Alarm with a single method sound comes to." Sam, who
near the road had heard such claims many times, asked him to
actually write the form `(do (defprotocol Alarm (sound [this])) (some? Alarm))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes whether the Alarm protocol was defined (a non-nil truthy value).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (some? Alarm))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Greet (hail [this])) (some? Greet))` • **expected**: `True`

**concept_phrase**: `a defprotocol Greet with one method hail`

**question_what**: `whether Greet has been established`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defprotocol Greet (hail [this])) (some? Greet))`, and the line
above it read a defprotocol Greet with one method hail. Bob handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives whether Greet has been established.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (some? Greet))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (some? Alarm))` • **expected**: `True`

**concept_phrase**: `a defprotocol Alarm with a single method sound`

**question_what**: `whether the Alarm protocol was defined (a non-nil truthy value)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
a defprotocol Alarm with a single method sound. Lou peered over his shoulder
at the form `(do (defprotocol Alarm (sound [this])) (some? Alarm))` and was asked, gently, to be the one to
submit it.

What Clojure form computes whether the Alarm protocol was defined (a non-nil truthy value)? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (some? Alarm))"}}]}
```

---

## G8-05: Protocol extension

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))` • **expected**: `'howl'`

**concept_phrase**: `an Alarm protocol extended to String, then call sound on a string`

**question_what**: `what sound returns when applied to "wolf"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit an Alarm protocol extended to String, then call sound on a string to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for what sound returns when applied to "wolf".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] \"howl\")) (sound \"wolf\"))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))` • **expected**: `':number'`

**concept_phrase**: `a Greet protocol extended to Long, then call hail on 7`

**question_what**: `the keyword hail returns for the number 7`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post in the forest carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`. Tom
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
a Greet protocol extended to Long, then call hail on 7 was to put it in the REPL.

What Clojure form computes the keyword hail returns for the number 7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))` • **expected**: `'howl'`

**concept_phrase**: `an Alarm protocol extended to String, then call sound on a string`

**question_what**: `what sound returns when applied to "wolf"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place at the edge of the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to an Alarm protocol extended to String, then call sound on a string.
"You hand the form `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a form whose evaluation gives what sound returns when applied to "wolf".

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] \"howl\")) (sound \"wolf\"))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))` • **expected**: `':number'`

**concept_phrase**: `a Greet protocol extended to Long, then call hail on 7`

**question_what**: `the keyword hail returns for the number 7`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
a Greet protocol extended to Long, then call hail on 7 was to put it in the REPL.

Question: write a Clojure expression for the keyword hail returns for the number 7.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Greet (hail [this])) (extend-protocol Greet java.lang.Long (hail [_] :number)) (hail 7))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))` • **expected**: `'howl'`

**concept_phrase**: `an Alarm protocol extended to String, then call sound on a string`

**question_what**: `what sound returns when applied to "wolf"`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] "howl")) (sound "wolf"))`. Jess
laughed, boasting at every turn, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
an Alarm protocol extended to String, then call sound on a string was to put it in the REPL.

What Clojure form computes what sound returns when applied to "wolf"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm java.lang.String (sound [_] \"howl\")) (sound \"wolf\"))"}}]}
```

---

## G8-06: Protocol method dispatch

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))` • **expected**: `':long-alarm'`

**concept_phrase**: `Alarm dispatched on the class of its argument; called with 42`

**question_what**: `the keyword sound returns for the integer 42`

```
The boy on the hill thought the trick clever the first time he played it.

Today atop the hilltop, Frank explained to Will that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))`
captured Alarm dispatched on the class of its argument; called with 42, and Frank suggested they hand it to the
REPL.

Write a Clojure expression that computes the keyword sound returns for the integer 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound "x"))` • **expected**: `':string-alarm'`

**concept_phrase**: `Alarm dispatched on a string argument`

**question_what**: `the keyword sound returns for the string "x"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound "x"))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit Alarm dispatched on a string argument to the
REPL. Whatever comes back is the answer."

What Clojure form computes the keyword sound returns for the string "x"? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound \"x\"))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))` • **expected**: `':long-alarm'`

**concept_phrase**: `Alarm dispatched on the class of its argument; called with 42`

**question_what**: `the keyword sound returns for the integer 42`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
Alarm dispatched on the class of its argument; called with 42 was to put it in the REPL.

Question: write a Clojure expression for the keyword sound returns for the integer 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound "x"))` • **expected**: `':string-alarm'`

**concept_phrase**: `Alarm dispatched on a string argument`

**question_what**: `the keyword sound returns for the string "x"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound "x"))`, and the line
above it read Alarm dispatched on a string argument. Robin handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the keyword sound returns for the string "x".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound \"x\"))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))` • **expected**: `':long-alarm'`

**concept_phrase**: `Alarm dispatched on the class of its argument; called with 42`

**question_what**: `the keyword sound returns for the integer 42`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))`, and the page
heading read Alarm dispatched on the class of its argument; called with 42. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the keyword sound returns for the integer 42? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-protocol Alarm   java.lang.String (sound [_] :string-alarm)   java.lang.Long   (sound [_] :long-alarm)) (sound 42))"}}]}
```

---

## G8-07: Record implementing protocol

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))` • **expected**: `':cry'`

**concept_phrase**: `a defrecord Shepherd that implements Alarm with sound -> :cry`

**question_what**: `the keyword sound returns for a Shepherd record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to a defrecord Shepherd that implements Alarm with sound -> :cry and read out the
form aloud: `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the keyword sound returns for a Shepherd record? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd \"Pip\")))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder "Mira")))` • **expected**: `':measured'`

**concept_phrase**: `an Elder record implementing Alarm with sound -> :measured`

**question_what**: `the keyword sound returns for an Elder record`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder "Mira")))`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
an Elder record implementing Alarm with sound -> :measured was to put it in the REPL.

Write a Clojure expression that computes the keyword sound returns for an Elder record.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder \"Mira\")))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))` • **expected**: `':cry'`

**concept_phrase**: `a defrecord Shepherd that implements Alarm with sound -> :cry`

**question_what**: `the keyword sound returns for a Shepherd record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))`, and the line
above it read a defrecord Shepherd that implements Alarm with sound -> :cry. Oliver handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

What Clojure form computes the keyword sound returns for a Shepherd record? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd \"Pip\")))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder "Mira")))` • **expected**: `':measured'`

**concept_phrase**: `an Elder record implementing Alarm with sound -> :measured`

**question_what**: `the keyword sound returns for an Elder record`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
in the orchard, demanding a verdict on the form `(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder "Mira")))` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit an Elder record implementing Alarm with sound -> :measured to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the keyword sound returns for an Elder record.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (defrecord Elder [name] Alarm (sound [_] :measured)) (sound (->Elder \"Mira\")))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))` • **expected**: `':cry'`

**concept_phrase**: `a defrecord Shepherd that implements Alarm with sound -> :cry`

**question_what**: `the keyword sound returns for a Shepherd record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd "Pip")))`, and the page
heading read a defrecord Shepherd that implements Alarm with sound -> :cry. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the keyword sound returns for a Shepherd record? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (defrecord Shepherd [name] Alarm (sound [_] :cry)) (sound (->Shepherd \"Pip\")))"}}]}
```

---

## G8-08: Multimethod defmulti

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))` • **expected**: `':cry'`

**concept_phrase**: `a defmulti reply that dispatches on :role, called with :shepherd`

**question_what**: `what reply returns for {:role :shepherd}`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

Today in the orchard, Oliver explained to Tom that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))`
captured a defmulti reply that dispatches on :role, called with :shepherd, and Oliver suggested they hand it to the
REPL.

Write a form whose evaluation gives what reply returns for {:role :shepherd}.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))` • **expected**: `':bright'`

**concept_phrase**: `a defmulti tag dispatching on :kind`

**question_what**: `what tag returns for {:kind :lantern}`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))`, and the line
above it read a defmulti tag dispatching on :kind. Alex handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes what tag returns for {:kind :lantern}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))` • **expected**: `':cry'`

**concept_phrase**: `a defmulti reply that dispatches on :role, called with :shepherd`

**question_what**: `what reply returns for {:role :shepherd}`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

A wooden notice nailed to a post near the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))`. Will
laughed, as if the race were already won, and declared it too easy to bother with.
Grace said, patiently, that the only way to be certain of
a defmulti reply that dispatches on :role, called with :shepherd was to put it in the REPL.

Write a Clojure expression that computes what reply returns for {:role :shepherd}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))` • **expected**: `':bright'`

**concept_phrase**: `a defmulti tag dispatching on :kind`

**question_what**: `what tag returns for {:kind :lantern}`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))`, and the line
above it read a defmulti tag dispatching on :kind. Sam handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes what tag returns for {:kind :lantern}.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti tag :kind) (defmethod tag :lantern [_] :bright) (tag {:kind :lantern}))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))` • **expected**: `':cry'`

**concept_phrase**: `a defmulti reply that dispatches on :role, called with :shepherd`

**question_what**: `what reply returns for {:role :shepherd}`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, with great whoops of laughter.
"Anyone can see what a defmulti reply that dispatches on :role, called with :shepherd comes to." Oliver, who
by the orchard had heard such claims many times, asked them to
actually write the form `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes what reply returns for {:role :shepherd}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))"}}]}
```

---

## G8-09: Multimethod defmethod

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))` • **expected**: `':measured'`

**concept_phrase**: `two defmethod entries on reply, called with :elder`

**question_what**: `what reply returns for {:role :elder}`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit two defmethod entries on reply, called with :elder to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for what reply returns for {:role :elder}.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))` • **expected**: `':unknown'`

**concept_phrase**: `a :default fallback method on reply, called with an unknown role`

**question_what**: `what reply returns for {:role :stranger} when :default falls through`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what a :default fallback method on reply, called with an unknown role comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives what reply returns for {:role :stranger} when :default falls through.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))` • **expected**: `':measured'`

**concept_phrase**: `two defmethod entries on reply, called with :elder`

**question_what**: `what reply returns for {:role :elder}`

```
The boy on the hill thought the trick clever the first time he played it.

A scrap of parchment, pinned to the village board in the orchard, set out a
rule that every honest villager would have to abide by. Jess,
with great whoops of laughter, read it aloud: it was two defmethod entries on reply, called with :elder. Morgan
said only the REPL could confirm what `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))` actually
decided.

Write a Clojure expression that computes what reply returns for {:role :elder}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))` • **expected**: `':unknown'`

**concept_phrase**: `a :default fallback method on reply, called with an unknown role`

**question_what**: `what reply returns for {:role :stranger} when :default falls through`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
at the edge of the woods, demanding a verdict on the form `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Carol, walking up
at an unhurried pace, simply said: "Submit a :default fallback method on reply, called with an unknown role to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives what reply returns for {:role :stranger} when :default falls through.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (defmethod reply :default  [_] :unknown) (reply {:role :stranger}))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))` • **expected**: `':measured'`

**concept_phrase**: `two defmethod entries on reply, called with :elder`

**question_what**: `what reply returns for {:role :elder}`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. George pointed to two defmethod entries on reply, called with :elder and read out the
form aloud: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for what reply returns for {:role :elder}.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (defmethod reply :elder    [_] :measured) (reply {:role :elder}))"}}]}
```

---

## G8-10: Multimethod vs protocol

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` • **expected**: `'howl'`

**concept_phrase**: `a defmulti dispatching on identity, with one method for :wolf`

**question_what**: `the string show returns for :wolf`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked a defmulti dispatching on identity, with one method for :wolf on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string show returns for :wolf.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :wolf [_] \"howl\") (show :wolf))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "wolf"))` • **expected**: `'str-wolf'`

**concept_phrase**: `a Show protocol extended to String, called with "wolf"`

**question_what**: `the string show returns for "wolf" via protocol`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

"There is no need to evaluate that," Pat said, with a smug grin.
"Anyone can see what a Show protocol extended to String, called with "wolf" comes to." Carol, who
near the orchard had heard such claims many times, asked them to
actually write the form `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "wolf"))` and submit it to the REPL —
just to be sure.

Question: write a Clojure expression for the string show returns for "wolf" via protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"wolf\"))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` • **expected**: `'howl'`

**concept_phrase**: `a defmulti dispatching on identity, with one method for :wolf`

**question_what**: `the string show returns for :wolf`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to a defmulti dispatching on identity, with one method for :wolf.
"You hand the form `(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the string show returns for :wolf? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :wolf [_] \"howl\") (show :wolf))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "wolf"))` • **expected**: `'str-wolf'`

**concept_phrase**: `a Show protocol extended to String, called with "wolf"`

**question_what**: `the string show returns for "wolf" via protocol`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A scrap of parchment, pinned to the village board along the road, set out a
rule that every honest villager would have to abide by. Tom,
puffed up with pride, read it aloud: it was a Show protocol extended to String, called with "wolf". Alice
said only the REPL could confirm what `(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str "str-" s))) (show "wolf"))` actually
decided.

Question: write a Clojure expression for the string show returns for "wolf" via protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Show (show [this])) (extend-protocol Show java.lang.String (show [s] (str \"str-\" s))) (show \"wolf\"))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` • **expected**: `'howl'`

**concept_phrase**: `a defmulti dispatching on identity, with one method for :wolf`

**question_what**: `the string show returns for :wolf`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A scrap of parchment, pinned to the village board by the farm, set out a
rule that every honest villager would have to abide by. Tom,
with a smug grin, read it aloud: it was a defmulti dispatching on identity, with one method for :wolf. Robin
said only the REPL could confirm what `(do (defmulti show identity) (defmethod show :wolf [_] "howl") (show :wolf))` actually
decided.

Write a form whose evaluation gives the string show returns for :wolf.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :wolf [_] \"howl\") (show :wolf))"}}]}
```

---

## G8-11: Protocol vs Java interface

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` • **expected**: `':raised'`

**concept_phrase**: `an IAlarm protocol (Clojure analogue of a Java interface) extended to String`

**question_what**: `the keyword raise returns for "wolf" via the protocol`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Halfway through the morning watch, Will called out
in the meadow, demanding a verdict on the form `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. Bob, walking up
at an unhurried pace, simply said: "Submit an IAlarm protocol (Clojure analogue of a Java interface) extended to String to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the keyword raise returns for "wolf" via the protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise \"wolf\"))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` • **expected**: `':raised'`

**concept_phrase**: `an IAlarm protocol (Clojure analogue of a Java interface) extended to String`

**question_what**: `the keyword raise returns for "wolf" via the protocol`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small crowd of villagers had gathered on the road to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Sam pointed to an IAlarm protocol (Clojure analogue of a Java interface) extended to String and read out the
form aloud: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the keyword raise returns for "wolf" via the protocol.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise \"wolf\"))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` • **expected**: `':raised'`

**concept_phrase**: `an IAlarm protocol (Clojure analogue of a Java interface) extended to String`

**question_what**: `the keyword raise returns for "wolf" via the protocol`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post in the village carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))`. Will
laughed, with great whoops of laughter, and declared it too easy to bother with.
Alex said, patiently, that the only way to be certain of
an IAlarm protocol (Clojure analogue of a Java interface) extended to String was to put it in the REPL.

Write a Clojure expression that computes the keyword raise returns for "wolf" via the protocol.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise \"wolf\"))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` • **expected**: `':raised'`

**concept_phrase**: `an IAlarm protocol (Clojure analogue of a Java interface) extended to String`

**question_what**: `the keyword raise returns for "wolf" via the protocol`

```
The boy on the hill thought the trick clever the first time he played it. All this took place by the woods.

A small crowd of villagers had gathered by the woods to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Frank pointed to an IAlarm protocol (Clojure analogue of a Java interface) extended to String and read out the
form aloud: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a Clojure expression that computes the keyword raise returns for "wolf" via the protocol.

---

I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise \"wolf\"))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))` • **expected**: `':raised'`

**concept_phrase**: `an IAlarm protocol (Clojure analogue of a Java interface) extended to String`

**question_what**: `the keyword raise returns for "wolf" via the protocol`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to an IAlarm protocol (Clojure analogue of a Java interface) extended to String and read out the
form aloud: `(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise "wolf"))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the keyword raise returns for "wolf" via the protocol.

---

I define the protocol or type, then exercise it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IAlarm (raise [this])) (extend-protocol IAlarm java.lang.String (raise [_] :raised)) (raise \"wolf\"))"}}]}
```

---

## G8-12: extend-type on built-in types

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` • **expected**: `':number-alarm'`

**concept_phrase**: `extend-type used to attach Alarm to Long, called with 5`

**question_what**: `the keyword sound returns for 5`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the orchard the next entry was
extend-type used to attach Alarm to Long, called with 5. Jess peered over her shoulder
at the form `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the keyword sound returns for 5.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound "wolf"))` • **expected**: `':string-alarm'`

**concept_phrase**: `extend-type attaching Alarm to String`

**question_what**: `the keyword sound returns for "wolf" via extend-type`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Robin kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the meadow the next entry was
extend-type attaching Alarm to String. Tom peered over their shoulder
at the form `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound "wolf"))` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the keyword sound returns for "wolf" via extend-type.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound \"wolf\"))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` • **expected**: `':number-alarm'`

**concept_phrase**: `extend-type used to attach Alarm to Long, called with 5`

**question_what**: `the keyword sound returns for 5`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was extend-type used to attach Alarm to Long, called with 5. George read
out the form `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the keyword sound returns for 5? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound "wolf"))` • **expected**: `':string-alarm'`

**concept_phrase**: `extend-type attaching Alarm to String`

**question_what**: `the keyword sound returns for "wolf" via extend-type`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound "wolf"))`, and the page
heading read extend-type attaching Alarm to String. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the keyword sound returns for "wolf" via extend-type.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-type java.lang.String Alarm (sound [_] :string-alarm)) (sound \"wolf\"))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` • **expected**: `':number-alarm'`

**concept_phrase**: `extend-type used to attach Alarm to Long, called with 5`

**question_what**: `the keyword sound returns for 5`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A scrap of parchment, pinned to the village board in the farm, set out a
rule that every honest villager would have to abide by. Tom,
with great whoops of laughter, read it aloud: it was extend-type used to attach Alarm to Long, called with 5. Oliver
said only the REPL could confirm what `(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))` actually
decided.

What Clojure form computes the keyword sound returns for 5? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (extend-type java.lang.Long Alarm (sound [_] :number-alarm)) (sound 5))"}}]}
```

---

## G8-13: this-style vs fn-style

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))` • **expected**: `'Pip'`

**concept_phrase**: `a protocol method using this to read a field`

**question_what**: `the name returned by name-of for a Shepherd record`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post at the edge of the woods carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
a protocol method using this to read a field was to put it in the REPL.

Write a Clojure expression that computes the name returned by name-of for a Shepherd record.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd \"Pip\")))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))` • **expected**: `':amber'`

**concept_phrase**: `a Tagged protocol method that pulls :t off this`

**question_what**: `the :t value via tag-of for a Lantern`

```
The boy on the hill thought the trick clever the first time he played it.

George kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today in the forest the next entry was
a Tagged protocol method that pulls :t off this. Jess peered over his shoulder
at the form `(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))` and was asked, gently, to be the one to
submit it.

Write a Clojure expression that computes the :t value via tag-of for a Lantern.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))` • **expected**: `'Pip'`

**concept_phrase**: `a protocol method using this to read a field`

**question_what**: `the name returned by name-of for a Shepherd record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to a protocol method using this to read a field.
"You hand the form `(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the name returned by name-of for a Shepherd record? Submit it via `eval`.

---

I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd \"Pip\")))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))` • **expected**: `':amber'`

**concept_phrase**: `a Tagged protocol method that pulls :t off this`

**question_what**: `the :t value via tag-of for a Lantern`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was at the edge of the forest.

Lou called down from a stone near the forest where someone had
chalked a Tagged protocol method that pulls :t off this on a flat board. Lou, with a smug grin,
declared she already knew what would come back. Morgan,
stepping deliberately, asked her to actually submit the form
`(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the :t value via tag-of for a Lantern.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Tagged (tag-of [this])) (defrecord Lantern [t] Tagged (tag-of [this] (:t this))) (tag-of (->Lantern :amber)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))` • **expected**: `'Pip'`

**concept_phrase**: `a protocol method using this to read a field`

**question_what**: `the name returned by name-of for a Shepherd record`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked a protocol method using this to read a field on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd "Pip")))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the name returned by name-of for a Shepherd record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Shepherd [n] Named (name-of [this] (:n this))) (name-of (->Shepherd \"Pip\")))"}}]}
```

---

## G8-14: Protocols don't inherit

**Examples:** 1 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` • **expected**: `[':a-impl', ':b-impl']`

**concept_phrase**: `two independent protocols A and B both extended to String`

**question_what**: `the pair [a-op b-op] when each protocol is used independently`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to two independent protocols A and B both extended to String.
"You hand the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the pair [a-op b-op] when each protocol is used independently.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### Record 2 — example 1 of 1

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` • **expected**: `[':a-impl', ':b-impl']`

**concept_phrase**: `two independent protocols A and B both extended to String`

**question_what**: `the pair [a-op b-op] when each protocol is used independently`

```
The boy on the hill thought the trick clever the first time he played it. All this took place atop the hilltop.

Grace had been trying to teach Pat how the REPL
works. "Look here," she said, pointing to two independent protocols A and B both extended to String.
"You hand the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Pat, yawning at the soft moss, agreed to try.

Write a form whose evaluation gives the pair [a-op b-op] when each protocol is used independently.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### Record 3 — example 1 of 1

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` • **expected**: `[':a-impl', ':b-impl']`

**concept_phrase**: `two independent protocols A and B both extended to String`

**question_what**: `the pair [a-op b-op] when each protocol is used independently`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to two independent protocols A and B both extended to String.
"You hand the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for the pair [a-op b-op] when each protocol is used independently.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### Record 4 — example 1 of 1

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` • **expected**: `[':a-impl', ':b-impl']`

**concept_phrase**: `two independent protocols A and B both extended to String`

**question_what**: `the pair [a-op b-op] when each protocol is used independently`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone in the orchard where someone had
chalked two independent protocols A and B both extended to String on a flat board. Will, as if the race were already won,
declared he already knew what would come back. Sam,
saying very little, asked him to actually submit the form
`(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the pair [a-op b-op] when each protocol is used independently.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### Record 5 — example 1 of 1

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` • **expected**: `[':a-impl', ':b-impl']`

**concept_phrase**: `two independent protocols A and B both extended to String`

**question_what**: `the pair [a-op b-op] when each protocol is used independently`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Jess called out
near the woods, demanding a verdict on the form `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Grace, walking up
at an unhurried pace, simply said: "Submit two independent protocols A and B both extended to String to the
REPL. Whatever comes back is the answer."

What Clojure form computes the pair [a-op b-op] when each protocol is used independently? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

---

## G8-15: derive and isa? — multimethod hierarchy

**Examples:** 3 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))` • **expected**: `True`

**concept_phrase**: `deriving ::shepherd from ::villager and asking isa?`

**question_what**: `whether ::shepherd isa? ::villager after derive`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Today near the meadow, Grace explained to Lou that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form `(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))`
captured deriving ::shepherd from ::villager and asking isa?, and Grace suggested they hand it to the
REPL.

What Clojure form computes whether ::shepherd isa? ::villager after derive? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))"}}]}
```

### Record 2 — example 2 of 3

**form**: `(isa? java.lang.Long java.lang.Number)` • **expected**: `True`

**concept_phrase**: `the predicate (isa? Long Number)`

**question_what**: `whether Long isa? Number`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the predicate (isa? Long Number) on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(isa? java.lang.Long java.lang.Number)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes whether Long isa? Number.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(isa? java.lang.String java.lang.Number)` • **expected**: `False`

**concept_phrase**: `the predicate (isa? String Number)`

**question_what**: `whether String isa? Number`

```
The boy on the hill thought the trick clever the first time he played it.

A small slate sat on a flat stone at the edge of the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(isa? java.lang.String java.lang.Number)`, and the page
heading read the predicate (isa? String Number). Frank nodded at Lou to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for whether String isa? Number.

---

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.String java.lang.Number)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))` • **expected**: `True`

**concept_phrase**: `deriving ::shepherd from ::villager and asking isa?`

**question_what**: `whether ::shepherd isa? ::villager after derive`

```
The boy on the hill thought the trick clever the first time he played it. This was near the village.

A scrap of parchment, pinned to the village board in the village, set out a
rule that every honest villager would have to abide by. Tom,
swaggering through the underbrush, read it aloud: it was deriving ::shepherd from ::villager and asking isa?. Sam
said only the REPL could confirm what `(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))` actually
decided.

Write a form whose evaluation gives whether ::shepherd isa? ::villager after derive.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))"}}]}
```

### Record 5 — example 2 of 3

**form**: `(isa? java.lang.Long java.lang.Number)` • **expected**: `True`

**concept_phrase**: `the predicate (isa? Long Number)`

**question_what**: `whether Long isa? Number`

```
The boy on the hill thought the trick clever the first time he played it.

Today near the orchard, George explained to Will that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form `(isa? java.lang.Long java.lang.Number)`
captured the predicate (isa? Long Number), and George suggested they hand it to the
REPL.

Write a form whose evaluation gives whether Long isa? Number.

---

{"tool_calls":[{"name":"eval","args":{"form":"(isa? java.lang.Long java.lang.Number)"}}]}
```

---

## G8-16: Abstract design with protocols

**Examples:** 2 | **Subplots:** 12 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))` • **expected**: `[':scan', ':verify']`

**concept_phrase**: `a Watch protocol with two record implementations, mapped over instances`

**question_what**: `the pair of look results for a Shepherd and an Elder`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Pat called out
by the orchard, demanding a verdict on the form `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Sam, walking up
at an unhurried pace, simply said: "Submit a Watch protocol with two record implementations, mapped over instances to the
REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the pair of look results for a Shepherd and an Elder.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))` • **expected**: `':calm'`

**concept_phrase**: `a Sound protocol with two implementations, called on an Elder`

**question_what**: `the keyword cry returns for an Elder`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what a Sound protocol with two implementations, called on an Elder comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))` and submit it to the REPL —
just to be sure.

What Clojure form computes the keyword cry returns for an Elder? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))` • **expected**: `[':scan', ':verify']`

**concept_phrase**: `a Watch protocol with two record implementations, mapped over instances`

**question_what**: `the pair of look results for a Shepherd and an Elder`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post in the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))`. Pat
laughed, puffed up with pride, and declared it too easy to bother with.
Bob said, patiently, that the only way to be certain of
a Watch protocol with two record implementations, mapped over instances was to put it in the REPL.

Question: write a Clojure expression for the pair of look results for a Shepherd and an Elder.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))` • **expected**: `':calm'`

**concept_phrase**: `a Sound protocol with two implementations, called on an Elder`

**question_what**: `the keyword cry returns for an Elder`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
a Sound protocol with two implementations, called on an Elder. Will peered over his shoulder
at the form `(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the keyword cry returns for an Elder.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Sound (cry [this])) (defrecord Shepherd [] Sound (cry [_] :alarm)) (defrecord Elder [] Sound (cry [_] :calm)) (cry (->Elder)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))` • **expected**: `[':scan', ':verify']`

**concept_phrase**: `a Watch protocol with two record implementations, mapped over instances`

**question_what**: `the pair of look results for a Shepherd and an Elder`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
a Watch protocol with two record implementations, mapped over instances. Pat peered over his shoulder
at the form `(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the pair of look results for a Shepherd and an Elder.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Watch (look [this])) (defrecord Shepherd [] Watch (look [_] :scan)) (defrecord Elder [] Watch (look [_] :verify)) (mapv look [(->Shepherd) (->Elder)]))"}}]}
```

---

