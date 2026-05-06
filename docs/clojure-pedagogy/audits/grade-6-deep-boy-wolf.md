# Boy-wolf Grade 6 — deep spot-check

5 generated records per subject (across all examples and a variety of seeds). Read every record carefully. Flag anything that reads odd to a careful reader, including issues the structural audit can't catch (prose flow, contextual fit, cliché repetition, subplot/example mismatch, etc.)

---

## G6-01: Namespace as file

**Examples:** 3 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 3

**form**: `(name 'foo.bar)` • **expected**: `'foo.bar'`

**concept_phrase**: `the symbol foo.bar standing in for a namespace name`

**question_what**: `the string form of the namespace symbol foo.bar`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The reeve of the village kept a small list near the woods of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned the symbol foo.bar standing in for a namespace name. Alice,
without complaint, asked Pat to submit the form
`(name 'foo.bar)` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a Clojure expression that computes the string form of the namespace symbol foo.bar.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### Record 2 — example 2 of 3

**form**: `(name 'clojure.string)` • **expected**: `'clojure.string'`

**concept_phrase**: `the namespace symbol clojure.string`

**question_what**: `the string "clojure.string"`

```
The boy on the hill thought the trick clever the first time he played it.

Lou called down from a stone in the village where someone had
chalked the namespace symbol clojure.string on a flat board. Lou, puffed up with pride,
declared she already knew what would come back. Sam,
untroubled by what others thought, asked her to actually submit the form
`(name 'clojure.string)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string "clojure.string".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

### Record 3 — example 3 of 3

**form**: `(symbol? 'village.flock)` • **expected**: `True`

**concept_phrase**: `whether village.flock is a symbol`

**question_what**: `the value of (symbol? 'village.flock)`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the road.

The elder of the village kept a small slate on the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was whether village.flock is a symbol. George read
out the form `(symbol? 'village.flock)` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

Question: write a Clojure expression for the value of (symbol? 'village.flock).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'village.flock)"}}]}
```

### Record 4 — example 1 of 3

**form**: `(name 'foo.bar)` • **expected**: `'foo.bar'`

**concept_phrase**: `the symbol foo.bar standing in for a namespace name`

**question_what**: `the string form of the namespace symbol foo.bar`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened at the edge of the village.

The reeve of the village kept a small list by the village of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned the symbol foo.bar standing in for a namespace name. Frank,
stepping deliberately, asked Jess to submit the form
`(name 'foo.bar)` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a Clojure expression that computes the string form of the namespace symbol foo.bar.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### Record 5 — example 2 of 3

**form**: `(name 'clojure.string)` • **expected**: `'clojure.string'`

**concept_phrase**: `the namespace symbol clojure.string`

**question_what**: `the string "clojure.string"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The two cottages stood on opposite sides of the village near the hilltop, and
each kept its own copybook of forms. Tom scribbled into
one book; Oliver kept the other. To settle a question that
morning, Oliver pointed to the namespace symbol clojure.string and asked
him to write the form `(name 'clojure.string)` into the REPL so
the answer would carry honestly across both copybooks.

Question: write a Clojure expression for the string "clojure.string".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'clojure.string)"}}]}
```

---

## G6-02: ns form

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(name 'village.shepherd)` • **expected**: `'village.shepherd'`

**concept_phrase**: `the namespace name 'village.shepherd as a string`

**question_what**: `the string "village.shepherd"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will called down from a stone by the orchard where someone had
chalked the namespace name 'village.shepherd as a string on a flat board. Will, with a smug grin,
declared he already knew what would come back. Morgan,
stepping deliberately, asked him to actually submit the form
`(name 'village.shepherd)` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a form whose evaluation gives the string "village.shepherd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'village.shepherd)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(= 'village.shepherd 'village.shepherd)` • **expected**: `True`

**concept_phrase**: `two identical namespace symbols`

**question_what**: `whether the two namespace symbols are equal`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the woods.

Tom had shouted a claim from one side of the village
at the edge of the woods. Grace insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(= 'village.shepherd 'village.shepherd)` would
need to be evaluated under its proper name. Tom, her legs heavy from sprinting,
agreed — two identical namespace symbols was, after all, the line in question.

Write a Clojure expression that computes whether the two namespace symbols are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'village.shepherd 'village.shepherd)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(name 'village.shepherd)` • **expected**: `'village.shepherd'`

**concept_phrase**: `the namespace name 'village.shepherd as a string`

**question_what**: `the string "village.shepherd"`

```
The boy on the hill thought the trick clever the first time he played it. It happened by the woods.

The two cottages stood on opposite sides of the village in the woods, and
each kept its own copybook of forms. Pat scribbled into
one book; Alice kept the other. To settle a question that
morning, Alice pointed to the namespace name 'village.shepherd as a string and asked
them to write the form `(name 'village.shepherd)` into the REPL so
the answer would carry honestly across both copybooks.

Write a form whose evaluation gives the string "village.shepherd".

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'village.shepherd)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(= 'village.shepherd 'village.shepherd)` • **expected**: `True`

**concept_phrase**: `two identical namespace symbols`

**question_what**: `whether the two namespace symbols are equal`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(= 'village.shepherd 'village.shepherd)`, and the page
heading read two identical namespace symbols. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes whether the two namespace symbols are equal.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'village.shepherd 'village.shepherd)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(name 'village.shepherd)` • **expected**: `'village.shepherd'`

**concept_phrase**: `the namespace name 'village.shepherd as a string`

**question_what**: `the string "village.shepherd"`

```
The boy on the hill thought the trick clever the first time he played it. This was by the forest.

A small crowd of villagers had gathered at the edge of the forest to watch
Lou attempt to predict, off the cuff, what the REPL would
return. George pointed to the namespace name 'village.shepherd as a string and read out the
form aloud: `(name 'village.shepherd)`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the string "village.shepherd"? Submit it via `eval`.

---

I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'village.shepherd)"}}]}
```

---

## G6-03: require

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(clojure.string/upper-case "wolf")` • **expected**: `'WOLF'`

**concept_phrase**: `the form using clojure.string/upper-case on "wolf"`

**question_what**: `the upper-cased string "WOLF"`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place at the edge of the village.

Alice had been trying to teach Will how the REPL
works. "Look here," she said, pointing to the form using clojure.string/upper-case on "wolf".
"You hand the form `(clojure.string/upper-case "wolf")` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, drowsy from the warm sun, agreed to try.

Write a Clojure expression that computes the upper-cased string "WOLF".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"wolf\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(clojure.string/lower-case "WOLF")` • **expected**: `'wolf'`

**concept_phrase**: `the form using clojure.string/lower-case`

**question_what**: `the lower-cased string "wolf"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened near the meadow.

A small crowd of villagers had gathered near the meadow to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to the form using clojure.string/lower-case and read out the
form aloud: `(clojure.string/lower-case "WOLF")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the lower-cased string "wolf".

---

I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"WOLF\")"}}]}
```

### Record 3 — example 1 of 2

**form**: `(clojure.string/upper-case "wolf")` • **expected**: `'WOLF'`

**concept_phrase**: `the form using clojure.string/upper-case on "wolf"`

**question_what**: `the upper-cased string "WOLF"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(clojure.string/upper-case "wolf")`, and the line
above it read the form using clojure.string/upper-case on "wolf". Frank handed the page to
Pat, who, yawning at the soft moss, agreed to write it out properly.

Write a Clojure expression that computes the upper-cased string "WOLF".

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"wolf\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(clojure.string/lower-case "WOLF")` • **expected**: `'wolf'`

**concept_phrase**: `the form using clojure.string/lower-case`

**question_what**: `the lower-cased string "wolf"`

```
The boy on the hill thought the trick clever the first time he played it.

The elder of the village kept a small slate near the village, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the form using clojure.string/lower-case. Bob read
out the form `(clojure.string/lower-case "WOLF")` so Will could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the lower-cased string "wolf"? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/lower-case \"WOLF\")"}}]}
```

### Record 5 — example 1 of 2

**form**: `(clojure.string/upper-case "wolf")` • **expected**: `'WOLF'`

**concept_phrase**: `the form using clojure.string/upper-case on "wolf"`

**question_what**: `the upper-cased string "WOLF"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Will had shouted a claim from one side of the village
by the village. Robin insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(clojure.string/upper-case "wolf")` would
need to be evaluated under its proper name. Will, lulled by the gentle wind,
agreed — the form using clojure.string/upper-case on "wolf" was, after all, the line in question.

Write a Clojure expression that computes the upper-cased string "WOLF".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"wolf\")"}}]}
```

---

## G6-04: refer and use

**Examples:** 1 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` • **expected**: `True`

**concept_phrase**: `whether two calls to the same fully-qualified function agree`

**question_what**: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

```
The boy on the hill thought the trick clever the first time he played it.

The reeve of the village kept a small list near the farm of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned whether two calls to the same fully-qualified function agree. Bob,
saying very little, asked Pat to submit the form
`(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` • **expected**: `True`

**concept_phrase**: `whether two calls to the same fully-qualified function agree`

**question_what**: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Frank had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to whether two calls to the same fully-qualified function agree.
"You hand the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, yawning at the soft moss, agreed to try.

What Clojure form computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` • **expected**: `True`

**concept_phrase**: `whether two calls to the same fully-qualified function agree`

**question_what**: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A wooden notice nailed to a post near the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`. Tom
laughed, swaggering through the underbrush, and declared it too easy to bother with.
Sam said, patiently, that the only way to be certain of
whether two calls to the same fully-qualified function agree was to put it in the REPL.

Write a Clojure expression that computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` • **expected**: `True`

**concept_phrase**: `whether two calls to the same fully-qualified function agree`

**question_what**: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small crowd of villagers had gathered at the edge of the forest to watch
Jess attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to whether two calls to the same fully-qualified function agree and read out the
form aloud: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` • **expected**: `True`

**concept_phrase**: `whether two calls to the same fully-qualified function agree`

**question_what**: `the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place at the edge of the orchard.

Oliver had been trying to teach Lou how the REPL
works. "Look here," he said, pointing to whether two calls to the same fully-qualified function agree.
"You hand the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Lou, lulled by the gentle wind, agreed to try.

What Clojure form computes the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

---

## G6-05: Fully qualified names

**Examples:** 4 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 4

**form**: `(clojure.string/upper-case "shepherd")` • **expected**: `'SHEPHERD'`

**concept_phrase**: `clojure.string/upper-case applied to "shepherd"`

**question_what**: `the upper-cased string "SHEPHERD"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Halfway through the morning watch, Jess called out
near the hilltop, demanding a verdict on the form `(clojure.string/upper-case "shepherd")` and refusing
to descend until somebody confirmed it. Jess insisted
she already knew the answer. Alice, walking up
at an unhurried pace, simply said: "Submit clojure.string/upper-case applied to "shepherd" to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the upper-cased string "SHEPHERD".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"shepherd\")"}}]}
```

### Record 2 — example 2 of 4

**form**: `(clojure.string/reverse "flock")` • **expected**: `'kcolf'`

**concept_phrase**: `clojure.string/reverse applied to "flock"`

**question_what**: `the reversed string "kcolf"`

```
The boy on the hill thought the trick clever the first time he played it.

The two cottages stood on opposite sides of the village in the forest, and
each kept its own copybook of forms. Tom scribbled into
one book; Alex kept the other. To settle a question that
morning, Alex pointed to clojure.string/reverse applied to "flock" and asked
him to write the form `(clojure.string/reverse "flock")` into the REPL so
the answer would carry honestly across both copybooks.

What Clojure form computes the reversed string "kcolf"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/reverse \"flock\")"}}]}
```

### Record 3 — example 3 of 4

**form**: `(namespace :village/shepherd)` • **expected**: `'village'`

**concept_phrase**: `the namespace portion of the keyword :village/shepherd`

**question_what**: `the string "village"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alex had been trying to teach Tom how the REPL
works. "Look here," they said, pointing to the namespace portion of the keyword :village/shepherd.
"You hand the form `(namespace :village/shepherd)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, her legs heavy from sprinting, agreed to try.

Write a form whose evaluation gives the string "village".

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(namespace :village/shepherd)"}}]}
```

### Record 4 — example 4 of 4

**form**: `(name :village/shepherd)` • **expected**: `'shepherd'`

**concept_phrase**: `the name portion of the keyword :village/shepherd`

**question_what**: `the string "shepherd"`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the village.

Tom had shouted a claim from one side of the village
at the edge of the village. Bob insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(name :village/shepherd)` would
need to be evaluated under its proper name. Tom, her legs heavy from sprinting,
agreed — the name portion of the keyword :village/shepherd was, after all, the line in question.

Write a Clojure expression that computes the string "shepherd".

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(name :village/shepherd)"}}]}
```

### Record 5 — example 1 of 4

**form**: `(clojure.string/upper-case "shepherd")` • **expected**: `'SHEPHERD'`

**concept_phrase**: `clojure.string/upper-case applied to "shepherd"`

**question_what**: `the upper-cased string "SHEPHERD"`

```
The boy on the hill thought the trick clever the first time he played it.

The two cottages stood on opposite sides of the village at the edge of the farm, and
each kept its own copybook of forms. Jess scribbled into
one book; Carol kept the other. To settle a question that
morning, Carol pointed to clojure.string/upper-case applied to "shepherd" and asked
her to write the form `(clojure.string/upper-case "shepherd")` into the REPL so
the answer would carry honestly across both copybooks.

What Clojure form computes the upper-cased string "SHEPHERD"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"shepherd\")"}}]}
```

---

## G6-06: Private defs

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(:private (meta '^:private x))` • **expected**: `True`

**concept_phrase**: `the :private flag on metadata of '^:private x`

**question_what**: `whether the :private metadata is true`

```
The boy on the hill thought the trick clever the first time he played it.

The reeve of the village kept a small list atop the hilltop of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned the :private flag on metadata of '^:private x. Frank,
her eyes always on the path, asked Will to submit the form
`(:private (meta '^:private x))` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a Clojure expression that computes whether the :private metadata is true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(:private (meta 'x))` • **expected**: `None`

**concept_phrase**: `the :private flag on plain metadata of 'x (none set)`

**question_what**: `the value of (:private (meta 'x)), which is nil`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
near the woods, demanding a verdict on the form `(:private (meta 'x))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Robin, walking up
at an unhurried pace, simply said: "Submit the :private flag on plain metadata of 'x (none set) to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value of (:private (meta 'x)), which is nil? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(:private (meta '^:private x))` • **expected**: `True`

**concept_phrase**: `the :private flag on metadata of '^:private x`

**question_what**: `whether the :private metadata is true`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

A wooden notice nailed to a post atop the hilltop carried a small puzzle. The
riddle simply asked the reader to evaluate `(:private (meta '^:private x))`. Jess
laughed, as if the race were already won, and declared it too easy to bother with.
Morgan said, patiently, that the only way to be certain of
the :private flag on metadata of '^:private x was to put it in the REPL.

Question: write a Clojure expression for whether the :private metadata is true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(:private (meta 'x))` • **expected**: `None`

**concept_phrase**: `the :private flag on plain metadata of 'x (none set)`

**question_what**: `the value of (:private (meta 'x)), which is nil`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(:private (meta 'x))`, and the line
above it read the :private flag on plain metadata of 'x (none set). Robin handed the page to
Pat, who, lulled by the gentle wind, agreed to write it out properly.

Write a Clojure expression that computes the value of (:private (meta 'x)), which is nil.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta 'x))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(:private (meta '^:private x))` • **expected**: `True`

**concept_phrase**: `the :private flag on metadata of '^:private x`

**question_what**: `whether the :private metadata is true`

```
Every shepherd in the valley knew the danger of crying wolf for sport. It happened along the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(:private (meta '^:private x))`, and the page
heading read the :private flag on metadata of '^:private x. George nodded at Will to
write the form properly so the slate would carry an honest entry.

What Clojure form computes whether the :private metadata is true? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

---

## G6-07: Public vs private API

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(boolean (:private (meta '^:private hidden)))` • **expected**: `True`

**concept_phrase**: `whether the symbol 'hidden carries the :private flag`

**question_what**: `the boolean of (:private (meta '^:private hidden))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small crowd of villagers had gathered by the woods to watch
Tom attempt to predict, off the cuff, what the REPL would
return. Robin pointed to whether the symbol 'hidden carries the :private flag and read out the
form aloud: `(boolean (:private (meta '^:private hidden)))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(boolean (:private (meta 'public)))` • **expected**: `False`

**concept_phrase**: `whether 'public carries the :private flag`

**question_what**: `the boolean of (:private (meta 'public))`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the meadow.

A wooden notice nailed to a post by the meadow carried a small puzzle. The
riddle simply asked the reader to evaluate `(boolean (:private (meta 'public)))`. Jess
laughed, puffed up with pride, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
whether 'public carries the :private flag was to put it in the REPL.

Write a Clojure expression that computes the boolean of (:private (meta 'public)).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(boolean (:private (meta '^:private hidden)))` • **expected**: `True`

**concept_phrase**: `whether the symbol 'hidden carries the :private flag`

**question_what**: `the boolean of (:private (meta '^:private hidden))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place on the hilltop.

"There is no need to evaluate that," Will said, boasting at every turn.
"Anyone can see what whether the symbol 'hidden carries the :private flag comes to." Oliver, who
at the edge of the hilltop had heard such claims many times, asked him to
actually write the form `(boolean (:private (meta '^:private hidden)))` and submit it to the REPL —
just to be sure.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(boolean (:private (meta 'public)))` • **expected**: `False`

**concept_phrase**: `whether 'public carries the :private flag`

**question_what**: `the boolean of (:private (meta 'public))`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Halfway through the morning watch, Tom called out
in the orchard, demanding a verdict on the form `(boolean (:private (meta 'public)))` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. Alex, walking up
at an unhurried pace, simply said: "Submit whether 'public carries the :private flag to the
REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the boolean of (:private (meta 'public)).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta 'public)))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(boolean (:private (meta '^:private hidden)))` • **expected**: `True`

**concept_phrase**: `whether the symbol 'hidden carries the :private flag`

**question_what**: `the boolean of (:private (meta '^:private hidden))`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A small slate sat on a flat stone near the farm; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(boolean (:private (meta '^:private hidden)))`, and the page
heading read whether the symbol 'hidden carries the :private flag. George nodded at Jess to
write the form properly so the slate would carry an honest entry.

What Clojure form computes the boolean of (:private (meta '^:private hidden))? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

---

## G6-08: Circular dependencies

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(clojure.string/upper-case "a")` • **expected**: `'A'`

**concept_phrase**: `a single-direction call from one namespace to clojure.string`

**question_what**: `the upper-cased string "A"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. It happened near the orchard.

The reeve of the village kept a small list in the orchard of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned a single-direction call from one namespace to clojure.string. Oliver,
stepping deliberately, asked Tom to submit the form
`(clojure.string/upper-case "a")` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a form whose evaluation gives the upper-cased string "A".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(= 'a.b 'a.b)` • **expected**: `True`

**concept_phrase**: `whether two references to the same namespace symbol agree`

**question_what**: `the value of (= 'a.b 'a.b)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened by the orchard.

"There is no need to evaluate that," Pat said, puffed up with pride.
"Anyone can see what whether two references to the same namespace symbol agree comes to." Alex, who
by the orchard had heard such claims many times, asked them to
actually write the form `(= 'a.b 'a.b)` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the value of (= 'a.b 'a.b).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(clojure.string/upper-case "a")` • **expected**: `'A'`

**concept_phrase**: `a single-direction call from one namespace to clojure.string`

**question_what**: `the upper-cased string "A"`

```
The boy on the hill thought the trick clever the first time he played it. It happened at the edge of the farm.

The two cottages stood on opposite sides of the village near the farm, and
each kept its own copybook of forms. Will scribbled into
one book; Grace kept the other. To settle a question that
morning, Grace pointed to a single-direction call from one namespace to clojure.string and asked
him to write the form `(clojure.string/upper-case "a")` into the REPL so
the answer would carry honestly across both copybooks.

Write a Clojure expression that computes the upper-cased string "A".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(= 'a.b 'a.b)` • **expected**: `True`

**concept_phrase**: `whether two references to the same namespace symbol agree`

**question_what**: `the value of (= 'a.b 'a.b)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(= 'a.b 'a.b)`, and the line
above it read whether two references to the same namespace symbol agree. Sam handed the page to
Tom, who, her legs heavy from sprinting, agreed to write it out properly.

Write a Clojure expression that computes the value of (= 'a.b 'a.b).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'a.b 'a.b)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(clojure.string/upper-case "a")` • **expected**: `'A'`

**concept_phrase**: `a single-direction call from one namespace to clojure.string`

**question_what**: `the upper-cased string "A"`

```
The boy on the hill thought the trick clever the first time he played it.

A wooden notice nailed to a post by the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(clojure.string/upper-case "a")`. Pat
laughed, with great whoops of laughter, and declared it too easy to bother with.
Oliver said, patiently, that the only way to be certain of
a single-direction call from one namespace to clojure.string was to put it in the REPL.

Write a Clojure expression that computes the upper-cased string "A".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

---

## G6-09: Loading order

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(do (def step1 1) (def step2 (+ step1 1)) step2)` • **expected**: `2`

**concept_phrase**: `two defs evaluated in order, the second using the first`

**question_what**: `the final value step2 after sequential loading`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. All this took place in the woods.

Halfway through the morning watch, Will called out
at the edge of the woods, demanding a verdict on the form `(do (def step1 1) (def step2 (+ step1 1)) step2)` and refusing
to descend until somebody confirmed it. Will insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit two defs evaluated in order, the second using the first to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the final value step2 after sequential loading.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(let [a 1 b (+ a 1)] (+ a b))` • **expected**: `3`

**concept_phrase**: `an in-expression analogue of file-loading order via let`

**question_what**: `the value of (+ a b) given a=1 b=(+ a 1)`

```
The boy on the hill thought the trick clever the first time he played it.

"There is no need to evaluate that," Pat said, swaggering through the underbrush.
"Anyone can see what an in-expression analogue of file-loading order via let comes to." Alice, who
by the forest had heard such claims many times, asked them to
actually write the form `(let [a 1 b (+ a 1)] (+ a b))` and submit it to the REPL —
just to be sure.

Write a form whose evaluation gives the value of (+ a b) given a=1 b=(+ a 1).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(do (def step1 1) (def step2 (+ step1 1)) step2)` • **expected**: `2`

**concept_phrase**: `two defs evaluated in order, the second using the first`

**question_what**: `the final value step2 after sequential loading`

```
The boy on the hill thought the trick clever the first time he played it.

The reeve of the village kept a small list in the orchard of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned two defs evaluated in order, the second using the first. Morgan,
her eyes always on the path, asked Jess to submit the form
`(do (def step1 1) (def step2 (+ step1 1)) step2)` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

Write a Clojure expression that computes the final value step2 after sequential loading.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(let [a 1 b (+ a 1)] (+ a b))` • **expected**: `3`

**concept_phrase**: `an in-expression analogue of file-loading order via let`

**question_what**: `the value of (+ a b) given a=1 b=(+ a 1)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(let [a 1 b (+ a 1)] (+ a b))`, and the line
above it read an in-expression analogue of file-loading order via let. Carol handed the page to
Pat, who, drowsy from the warm sun, agreed to write it out properly.

Write a form whose evaluation gives the value of (+ a b) given a=1 b=(+ a 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b (+ a 1)] (+ a b))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(do (def step1 1) (def step2 (+ step1 1)) step2)` • **expected**: `2`

**concept_phrase**: `two defs evaluated in order, the second using the first`

**question_what**: `the final value step2 after sequential loading`

```
The boy on the hill thought the trick clever the first time he played it.

Halfway through the morning watch, Tom called out
by the woods, demanding a verdict on the form `(do (def step1 1) (def step2 (+ step1 1)) step2)` and refusing
to descend until somebody confirmed it. Tom insisted
he already knew the answer. George, walking up
at an unhurried pace, simply said: "Submit two defs evaluated in order, the second using the first to the
REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the final value step2 after sequential loading.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

---

## G6-10: Leiningen and deps.edn

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(:deps {:deps {:a 1 :b 2}})` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the :deps key from a small deps-map literal`

**question_what**: `the value at :deps in {:deps {:a 1 :b 2}}`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Lou called down from a stone atop the hilltop where someone had
chalked the :deps key from a small deps-map literal on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Grace,
with steady, careful steps, asked her to actually submit the form
`(:deps {:deps {:a 1 :b 2}})` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value at :deps in {:deps {:a 1 :b 2}}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### Record 2 — example 2 of 2

**form**: `(get-in {:paths ["src"]} [:paths 0])` • **expected**: `'src'`

**concept_phrase**: `the first :paths entry from a tiny deps-style map`

**question_what**: `the string "src" at [:paths 0]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. This was near the orchard.

A wooden notice nailed to a post near the orchard carried a small puzzle. The
riddle simply asked the reader to evaluate `(get-in {:paths ["src"]} [:paths 0])`. Pat
laughed, with a smug grin, and declared it too easy to bother with.
Carol said, patiently, that the only way to be certain of
the first :paths entry from a tiny deps-style map was to put it in the REPL.

Question: write a Clojure expression for the string "src" at [:paths 0].

---

{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(:deps {:deps {:a 1 :b 2}})` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the :deps key from a small deps-map literal`

**question_what**: `the value at :deps in {:deps {:a 1 :b 2}}`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Alice had been trying to teach Tom how the REPL
works. "Look here," she said, pointing to the :deps key from a small deps-map literal.
"You hand the form `(:deps {:deps {:a 1 :b 2}})` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the value at :deps in {:deps {:a 1 :b 2}}? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### Record 4 — example 2 of 2

**form**: `(get-in {:paths ["src"]} [:paths 0])` • **expected**: `'src'`

**concept_phrase**: `the first :paths entry from a tiny deps-style map`

**question_what**: `the string "src" at [:paths 0]`

```
The boy on the hill thought the trick clever the first time he played it. This was along the road.

Tom had shouted a claim from one side of the village
along the road. Alice insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(get-in {:paths ["src"]} [:paths 0])` would
need to be evaluated under its proper name. Tom, her legs heavy from sprinting,
agreed — the first :paths entry from a tiny deps-style map was, after all, the line in question.

Question: write a Clojure expression for the string "src" at [:paths 0].

---

{"tool_calls":[{"name":"eval","args":{"form":"(get-in {:paths [\"src\"]} [:paths 0])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(:deps {:deps {:a 1 :b 2}})` • **expected**: `{':a': 1, ':b': 2}`

**concept_phrase**: `the :deps key from a small deps-map literal`

**question_what**: `the value at :deps in {:deps {:a 1 :b 2}}`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Tom had shouted a claim from one side of the village
by the farm. Robin insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(:deps {:deps {:a 1 :b 2}})` would
need to be evaluated under its proper name. Tom, lulled by the gentle wind,
agreed — the :deps key from a small deps-map literal was, after all, the line in question.

Write a form whose evaluation gives the value at :deps in {:deps {:a 1 :b 2}}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

---

## G6-11: Classpath

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(clojure.string/split "src:test" #":")` • **expected**: `['src', 'test']`

**concept_phrase**: `splitting a colon-separated classpath-like string`

**question_what**: `the vector ["src" "test"]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened in the meadow.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(clojure.string/split "src:test" #":")`, and the line
above it read splitting a colon-separated classpath-like string. Bob handed the page to
Will, who, her legs heavy from sprinting, agreed to write it out properly.

Question: write a Clojure expression for the vector ["src" "test"].

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### Record 2 — example 2 of 2

**form**: `(count ["src" "test" "resources"])` • **expected**: `3`

**concept_phrase**: `the number of entries in a classpath-like vector`

**question_what**: `the count of three classpath entries`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. All this took place near the road.

A small slate sat on a flat stone near the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(count ["src" "test" "resources"])`, and the page
heading read the number of entries in a classpath-like vector. Sam nodded at Jess to
write the form properly so the slate would carry an honest entry.

Write a Clojure expression that computes the count of three classpath entries.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(clojure.string/split "src:test" #":")` • **expected**: `['src', 'test']`

**concept_phrase**: `splitting a colon-separated classpath-like string`

**question_what**: `the vector ["src" "test"]`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The two cottages stood on opposite sides of the village in the village, and
each kept its own copybook of forms. Will scribbled into
one book; Alex kept the other. To settle a question that
morning, Alex pointed to splitting a colon-separated classpath-like string and asked
him to write the form `(clojure.string/split "src:test" #":")` into the REPL so
the answer would carry honestly across both copybooks.

Write a Clojure expression that computes the vector ["src" "test"].

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### Record 4 — example 2 of 2

**form**: `(count ["src" "test" "resources"])` • **expected**: `3`

**concept_phrase**: `the number of entries in a classpath-like vector`

**question_what**: `the count of three classpath entries`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was on the road.

A wooden notice nailed to a post on the road carried a small puzzle. The
riddle simply asked the reader to evaluate `(count ["src" "test" "resources"])`. Lou
laughed, with great whoops of laughter, and declared it too easy to bother with.
George said, patiently, that the only way to be certain of
the number of entries in a classpath-like vector was to put it in the REPL.

What Clojure form computes the count of three classpath entries? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [\"src\" \"test\" \"resources\"])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(clojure.string/split "src:test" #":")` • **expected**: `['src', 'test']`

**concept_phrase**: `splitting a colon-separated classpath-like string`

**question_what**: `the vector ["src" "test"]`

```
Every shepherd in the valley knew the danger of crying wolf for sport. All this took place by the orchard.

A small crowd of villagers had gathered near the orchard to watch
Lou attempt to predict, off the cuff, what the REPL would
return. Carol pointed to splitting a colon-separated classpath-like string and read out the
form aloud: `(clojure.string/split "src:test" #":")`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Write a form whose evaluation gives the vector ["src" "test"].

---

I require the namespace and call the function.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

---

## G6-12: Multiple files in one project

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(count ['village.shepherd 'village.elder 'village.shared])` • **expected**: `3`

**concept_phrase**: `the number of namespaces in a small project`

**question_what**: `the count of namespace symbols in the vector`

```
The boy on the hill thought the trick clever the first time he played it. This was near the orchard.

Grace had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to the number of namespaces in a small project.
"You hand the form `(count ['village.shepherd 'village.elder 'village.shared])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, weary from the morning's effort, agreed to try.

Write a Clojure expression that computes the count of namespace symbols in the vector.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(count ['village.shepherd 'village.elder 'village.shared])"}}]}
```

### Record 2 — example 2 of 2

**form**: `(map name ['village.shepherd 'village.elder])` • **expected**: `['village.shepherd', 'village.elder']`

**concept_phrase**: `the names of two namespaces as strings`

**question_what**: `the vector of namespace name strings`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Robin had been trying to teach Tom how the REPL
works. "Look here," they said, pointing to the names of two namespaces as strings.
"You hand the form `(map name ['village.shepherd 'village.elder])` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the vector of namespace name strings.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map name ['village.shepherd 'village.elder])"}}]}
```

### Record 3 — example 1 of 2

**form**: `(count ['village.shepherd 'village.elder 'village.shared])` • **expected**: `3`

**concept_phrase**: `the number of namespaces in a small project`

**question_what**: `the count of namespace symbols in the vector`

```
The boy on the hill thought the trick clever the first time he played it. It happened along the road.

The elder of the village kept a small slate near the road, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was the number of namespaces in a small project. George read
out the form `(count ['village.shepherd 'village.elder 'village.shared])` so Tom could write it
properly into the REPL and earn an honest mark on the slate.

What Clojure form computes the count of namespace symbols in the vector? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(count ['village.shepherd 'village.elder 'village.shared])"}}]}
```

### Record 4 — example 2 of 2

**form**: `(map name ['village.shepherd 'village.elder])` • **expected**: `['village.shepherd', 'village.elder']`

**concept_phrase**: `the names of two namespaces as strings`

**question_what**: `the vector of namespace name strings`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

A small slate sat on a flat stone on the road; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was `(map name ['village.shepherd 'village.elder])`, and the page
heading read the names of two namespaces as strings. Frank nodded at Will to
write the form properly so the slate would carry an honest entry.

Question: write a Clojure expression for the vector of namespace name strings.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(map name ['village.shepherd 'village.elder])"}}]}
```

### Record 5 — example 1 of 2

**form**: `(count ['village.shepherd 'village.elder 'village.shared])` • **expected**: `3`

**concept_phrase**: `the number of namespaces in a small project`

**question_what**: `the count of namespace symbols in the vector`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Tom had shouted a claim from one side of the village
in the farm. Oliver insisted that, before the answer could be
relied on by anyone in the other cottage, the form `(count ['village.shepherd 'village.elder 'village.shared])` would
need to be evaluated under its proper name. Tom, yawning at the soft moss,
agreed — the number of namespaces in a small project was, after all, the line in question.

What Clojure form computes the count of namespace symbols in the vector? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count ['village.shepherd 'village.elder 'village.shared])"}}]}
```

---

## G6-13: Aliasing conventions

**Examples:** 1 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 1

**form**: `(let [s clojure.string/upper-case] (s "wolf"))` • **expected**: `'WOLF'`

**concept_phrase**: `binding the function clojure.string/upper-case to a local s`

**question_what**: `the value (s "wolf") where s is upper-case`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

The two cottages stood on opposite sides of the village at the edge of the woods, and
each kept its own copybook of forms. Pat scribbled into
one book; Sam kept the other. To settle a question that
morning, Sam pointed to binding the function clojure.string/upper-case to a local s and asked
them to write the form `(let [s clojure.string/upper-case] (s "wolf"))` into the REPL so
the answer would carry honestly across both copybooks.

Write a Clojure expression that computes the value (s "wolf") where s is upper-case.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"wolf\"))"}}]}
```

### Record 2 — example 1 of 1

**form**: `(let [s clojure.string/upper-case] (s "wolf"))` • **expected**: `'WOLF'`

**concept_phrase**: `binding the function clojure.string/upper-case to a local s`

**question_what**: `the value (s "wolf") where s is upper-case`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Halfway through the morning watch, Pat called out
in the village, demanding a verdict on the form `(let [s clojure.string/upper-case] (s "wolf"))` and refusing
to descend until somebody confirmed it. Pat insisted
they already knew the answer. Morgan, walking up
at an unhurried pace, simply said: "Submit binding the function clojure.string/upper-case to a local s to the
REPL. Whatever comes back is the answer."

What Clojure form computes the value (s "wolf") where s is upper-case? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"wolf\"))"}}]}
```

### Record 3 — example 1 of 1

**form**: `(let [s clojure.string/upper-case] (s "wolf"))` • **expected**: `'WOLF'`

**concept_phrase**: `binding the function clojure.string/upper-case to a local s`

**question_what**: `the value (s "wolf") where s is upper-case`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root. It happened at the edge of the farm.

Bob had been trying to teach Tom how the REPL
works. "Look here," he said, pointing to binding the function clojure.string/upper-case to a local s.
"You hand the form `(let [s clojure.string/upper-case] (s "wolf"))` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Tom, drowsy from the warm sun, agreed to try.

What Clojure form computes the value (s "wolf") where s is upper-case? Submit it via `eval`.

---

I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"wolf\"))"}}]}
```

### Record 4 — example 1 of 1

**form**: `(let [s clojure.string/upper-case] (s "wolf"))` • **expected**: `'WOLF'`

**concept_phrase**: `binding the function clojure.string/upper-case to a local s`

**question_what**: `the value (s "wolf") where s is upper-case`

```
The boy on the hill thought the trick clever the first time he played it.

A small crowd of villagers had gathered near the farm to watch
Will attempt to predict, off the cuff, what the REPL would
return. Oliver pointed to binding the function clojure.string/upper-case to a local s and read out the
form aloud: `(let [s clojure.string/upper-case] (s "wolf"))`. The villagers waited, patient but
unimpressed, to see who would submit the form properly.

Question: write a Clojure expression for the value (s "wolf") where s is upper-case.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"wolf\"))"}}]}
```

### Record 5 — example 1 of 1

**form**: `(let [s clojure.string/upper-case] (s "wolf"))` • **expected**: `'WOLF'`

**concept_phrase**: `binding the function clojure.string/upper-case to a local s`

**question_what**: `the value (s "wolf") where s is upper-case`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Lou called down from a stone near the woods where someone had
chalked binding the function clojure.string/upper-case to a local s on a flat board. Lou, boasting at every turn,
declared she already knew what would come back. Alex,
stepping deliberately, asked her to actually submit the form
`(let [s clojure.string/upper-case] (s "wolf"))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value (s "wolf") where s is upper-case.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"wolf\"))"}}]}
```

---

## G6-14: Import for host classes

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(symbol? 'java.util.Date)` • **expected**: `True`

**concept_phrase**: `whether 'java.util.Date is a symbol`

**question_what**: `the value of (symbol? 'java.util.Date)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had been trying to teach Jess how the REPL
works. "Look here," she said, pointing to whether 'java.util.Date is a symbol.
"You hand the form `(symbol? 'java.util.Date)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Jess, lulled by the gentle wind, agreed to try.

Question: write a Clojure expression for the value of (symbol? 'java.util.Date).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(name 'java.util.Date)` • **expected**: `'java.util.Date'`

**concept_phrase**: `the dotted-class symbol's name`

**question_what**: `the string "java.util.Date"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn. This was along the road.

The two cottages stood on opposite sides of the village along the road, and
each kept its own copybook of forms. Pat scribbled into
one book; Grace kept the other. To settle a question that
morning, Grace pointed to the dotted-class symbol's name and asked
them to write the form `(name 'java.util.Date)` into the REPL so
the answer would carry honestly across both copybooks.

Question: write a Clojure expression for the string "java.util.Date".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(symbol? 'java.util.Date)` • **expected**: `True`

**concept_phrase**: `whether 'java.util.Date is a symbol`

**question_what**: `the value of (symbol? 'java.util.Date)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

Morgan had been trying to teach Will how the REPL
works. "Look here," they said, pointing to whether 'java.util.Date is a symbol.
"You hand the form `(symbol? 'java.util.Date)` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Will, yawning at the soft moss, agreed to try.

Question: write a Clojure expression for the value of (symbol? 'java.util.Date).

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(name 'java.util.Date)` • **expected**: `'java.util.Date'`

**concept_phrase**: `the dotted-class symbol's name`

**question_what**: `the string "java.util.Date"`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

A wooden notice nailed to a post at the edge of the farm carried a small puzzle. The
riddle simply asked the reader to evaluate `(name 'java.util.Date)`. Tom
laughed, with a smug grin, and declared it too easy to bother with.
Alice said, patiently, that the only way to be certain of
the dotted-class symbol's name was to put it in the REPL.

Write a Clojure expression that computes the string "java.util.Date".

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'java.util.Date)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(symbol? 'java.util.Date)` • **expected**: `True`

**concept_phrase**: `whether 'java.util.Date is a symbol`

**question_what**: `the value of (symbol? 'java.util.Date)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(symbol? 'java.util.Date)`, and the line
above it read whether 'java.util.Date is a symbol. Grace handed the page to
Jess, who, lulled by the gentle wind, agreed to write it out properly.

What Clojure form computes the value of (symbol? 'java.util.Date)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

---

## G6-15: Namespace meta

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(:doc (meta '^{:doc "trust the runtime"} village))` • **expected**: `'trust the runtime'`

**concept_phrase**: `the :doc metadata attached to the symbol 'village`

**question_what**: `the docstring "trust the runtime" from the metadata`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The reeve of the village kept a small list near the meadow of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned the :doc metadata attached to the symbol 'village. Grace,
without complaint, asked Lou to submit the form
`(:doc (meta '^{:doc "trust the runtime"} village))` so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village.

What Clojure form computes the docstring "trust the runtime" from the metadata? Submit it via `eval`.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"trust the runtime\"} village))"}}]}
```

### Record 2 — example 2 of 2

**form**: `(:author (meta '^{:author "Aesop"} village))` • **expected**: `'Aesop'`

**concept_phrase**: `the :author metadata on 'village`

**question_what**: `the string "Aesop"`

```
Every shepherd in the valley knew the danger of crying wolf for sport. This was near the hilltop.

Tom called down from a stone atop the hilltop where someone had
chalked the :author metadata on 'village on a flat board. Tom, as if the race were already won,
declared he already knew what would come back. Alex,
untroubled by what others thought, asked him to actually submit the form
`(:author (meta '^{:author "Aesop"} village))` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the string "Aesop".

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} village))"}}]}
```

### Record 3 — example 1 of 2

**form**: `(:doc (meta '^{:doc "trust the runtime"} village))` • **expected**: `'trust the runtime'`

**concept_phrase**: `the :doc metadata attached to the symbol 'village`

**question_what**: `the docstring "trust the runtime" from the metadata`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The two cottages stood on opposite sides of the village near the orchard, and
each kept its own copybook of forms. Lou scribbled into
one book; George kept the other. To settle a question that
morning, George pointed to the :doc metadata attached to the symbol 'village and asked
her to write the form `(:doc (meta '^{:doc "trust the runtime"} village))` into the REPL so
the answer would carry honestly across both copybooks.

Write a Clojure expression that computes the docstring "trust the runtime" from the metadata.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"trust the runtime\"} village))"}}]}
```

### Record 4 — example 2 of 2

**form**: `(:author (meta '^{:author "Aesop"} village))` • **expected**: `'Aesop'`

**concept_phrase**: `the :author metadata on 'village`

**question_what**: `the string "Aesop"`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The two cottages stood on opposite sides of the village near the meadow, and
each kept its own copybook of forms. Will scribbled into
one book; Frank kept the other. To settle a question that
morning, Frank pointed to the :author metadata on 'village and asked
him to write the form `(:author (meta '^{:author "Aesop"} village))` into the REPL so
the answer would carry honestly across both copybooks.

Question: write a Clojure expression for the string "Aesop".

---

{"tool_calls":[{"name":"eval","args":{"form":"(:author (meta '^{:author \"Aesop\"} village))"}}]}
```

### Record 5 — example 1 of 2

**form**: `(:doc (meta '^{:doc "trust the runtime"} village))` • **expected**: `'trust the runtime'`

**concept_phrase**: `the :doc metadata attached to the symbol 'village`

**question_what**: `the docstring "trust the runtime" from the metadata`

```
The boy on the hill thought the trick clever the first time he played it. All this took place in the village.

"There is no need to evaluate that," Jess said, boasting at every turn.
"Anyone can see what the :doc metadata attached to the symbol 'village comes to." Carol, who
at the edge of the village had heard such claims many times, asked her to
actually write the form `(:doc (meta '^{:doc "trust the runtime"} village))` and submit it to the REPL —
just to be sure.

Write a Clojure expression that computes the docstring "trust the runtime" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"trust the runtime\"} village))"}}]}
```

---

## G6-16: Cleaning up requires

**Examples:** 2 | **Subplots:** 13 | **Plan-pool size:** 10

### Record 1 — example 1 of 2

**form**: `(contains? #{'clojure.string} 'clojure.string)` • **expected**: `True`

**concept_phrase**: `whether the require list still contains 'clojure.string`

**question_what**: `the value of (contains? #{'clojure.string} 'clojure.string)`

```
Every shepherd in the valley knew the danger of crying wolf for sport.

Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was `(contains? #{'clojure.string} 'clojure.string)`, and the line
above it read whether the require list still contains 'clojure.string. Sam handed the page to
Pat, who, her legs heavy from sprinting, agreed to write it out properly.

Write a form whose evaluation gives the value of (contains? #{'clojure.string} 'clojure.string).

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### Record 2 — example 2 of 2

**form**: `(contains? #{'clojure.string} 'clojure.set)` • **expected**: `False`

**concept_phrase**: `whether the require list contains an unused 'clojure.set`

**question_what**: `the value of (contains? #{'clojure.string} 'clojure.set)`

```
The boy on the hill thought the trick clever the first time he played it. All this took place near the village.

"There is no need to evaluate that," Tom said, swaggering through the underbrush.
"Anyone can see what whether the require list contains an unused 'clojure.set comes to." Alice, who
at the edge of the village had heard such claims many times, asked him to
actually write the form `(contains? #{'clojure.string} 'clojure.set)` and submit it to the REPL —
just to be sure.

What Clojure form computes the value of (contains? #{'clojure.string} 'clojure.set)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### Record 3 — example 1 of 2

**form**: `(contains? #{'clojure.string} 'clojure.string)` • **expected**: `True`

**concept_phrase**: `whether the require list still contains 'clojure.string`

**question_what**: `the value of (contains? #{'clojure.string} 'clojure.string)`

```
It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.

The two cottages stood on opposite sides of the village in the farm, and
each kept its own copybook of forms. Pat scribbled into
one book; Bob kept the other. To settle a question that
morning, Bob pointed to whether the require list still contains 'clojure.string and asked
them to write the form `(contains? #{'clojure.string} 'clojure.string)` into the REPL so
the answer would carry honestly across both copybooks.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.string).

---

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

### Record 4 — example 2 of 2

**form**: `(contains? #{'clojure.string} 'clojure.set)` • **expected**: `False`

**concept_phrase**: `whether the require list contains an unused 'clojure.set`

**question_what**: `the value of (contains? #{'clojure.string} 'clojure.set)`

```
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today near the farm the next entry was
whether the require list contains an unused 'clojure.set. Will peered over his shoulder
at the form `(contains? #{'clojure.string} 'clojure.set)` and was asked, gently, to be the one to
submit it.

Question: write a Clojure expression for the value of (contains? #{'clojure.string} 'clojure.set).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.set)"}}]}
```

### Record 5 — example 1 of 2

**form**: `(contains? #{'clojure.string} 'clojure.string)` • **expected**: `True`

**concept_phrase**: `whether the require list still contains 'clojure.string`

**question_what**: `the value of (contains? #{'clojure.string} 'clojure.string)`

```
The boy on the hill thought the trick clever the first time he played it. This was by the orchard.

Frank kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today at the edge of the orchard the next entry was
whether the require list still contains 'clojure.string. Pat peered over his shoulder
at the form `(contains? #{'clojure.string} 'clojure.string)` and was asked, gently, to be the one to
submit it.

Write a form whose evaluation gives the value of (contains? #{'clojure.string} 'clojure.string).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

---

