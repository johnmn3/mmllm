# Grade 1 deep spot-check (tortoise-hare)

5 distinct rendered records per subject. 18 subjects × 5 = 90 records.

---

## G1-01: Eval as substitution

- examples: 8
  - ex0: form=`42` expected=`42`
    concept=`the value 42`
    question_what=`the value of 42`
  - ex1: form=`0` expected=`0`
    concept=`the value 0`
    question_what=`the value of 0`
  - ex2: form=`(+ 1 2)` expected=`3`
    concept=`the form (+ 1 2)`
    question_what=`the result of (+ 1 2)`
  - ex3: form=`(* 4 5)` expected=`20`
    concept=`the form (* 4 5)`
    question_what=`the result of (* 4 5)`
  - ex4: form=`(- 10 (+ 2 3))` expected=`5`
    concept=`the nested form (- 10 (+ 2 3))`
    question_what=`the result of (- 10 (+ 2 3))`
  - ex5: form=`(+ 1 (* 2 3))` expected=`7`
    concept=`the form (+ 1 (* 2 3))`
    question_what=`the result of (+ 1 (* 2 3))`
  - ex6: form=`"hello"` expected=`'hello'`
    concept=`the string "hello"`
    question_what=`the value of "hello"`
  - ex7: form=`nil` expected=`None`
    concept=`the literal nil`
    question_what=`the value of nil`

### Record 1 (form: `42`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the garden.

"There is no need to evaluate that," Hopper the hare said, with great whoops of laughter.
"Anyone can see what the value 42 comes to." Slowpoke the tortoise, who
near the garden had grown used to such claims, asked him to actually
write the form `42` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the value of 42.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 2 (form: `0`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

A wooden sign nailed to a tree by the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `0`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the value 0 was to put
it in the REPL.

Write a Clojure expression that computes the value of 0.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### Record 3 (form: `(+ 1 2)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the forest, the
next entry was the form (+ 1 2). Whisker the hare peered over
his shoulder at the form `(+ 1 2)` and asked what
it would come out to.

Write a Clojure expression that computes the result of (+ 1 2).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 4 (form: `(* 4 5)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened at the edge of the orchard.

"There is no need to evaluate that," Pip the hare said, boasting at every turn.
"Anyone can see what the form (* 4 5) comes to." Mossback the tortoise, who
in the orchard had grown used to such claims, asked them to actually
write the form `(* 4 5)` and submit it to the REPL — just to be
sure.

What Clojure form computes the result of (* 4 5)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### Record 5 (form: `(- 10 (+ 2 3))`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Halfway through the race, Hopper the hare stopped in the forest and refused to
continue until someone could prove what the form `(- 10 (+ 2 3))`
evaluated to. He called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the nested form (- 10 (+ 2 3)) to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the result of (- 10 (+ 2 3)).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(- 10 (+ 2 3))"}}]}
```

## G1-02: Integer numbers

- examples: 6
  - ex0: form=`7` expected=`7`
    concept=`the integer 7`
    question_what=`the value of the integer 7`
  - ex1: form=`-3` expected=`-3`
    concept=`the integer -3`
    question_what=`the value of the integer -3`
  - ex2: form=`0` expected=`0`
    concept=`the integer 0`
    question_what=`the value of zero`
  - ex3: form=`100` expected=`100`
    concept=`the integer 100`
    question_what=`the value of one hundred`
  - ex4: form=`-25` expected=`-25`
    concept=`the integer -25`
    question_what=`the value of negative twenty-five`
  - ex5: form=`12345` expected=`12345`
    concept=`the integer 12345`
    question_what=`the value of 12345`

### Record 1 (form: `7`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place by the woods.

Pip the hare and Mossback the tortoise stopped in the woods where someone had
written the integer 7 on a flat stone. Pip, swaggering through the underbrush, declared
that they could see the answer at a glance. Mossback,
her eyes always on the path, suggested they actually evaluate the form `7`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of the integer 7.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### Record 2 (form: `-3`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened by the orchard.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today by the orchard, the
next entry was the integer -3. Whisker the hare peered over
her shoulder at the form `-3` and asked what
it would come out to.

Question: write a Clojure expression for the value of the integer -3.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"-3"}}]}
```

### Record 3 (form: `0`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

At a moss-covered milestone near the meadow, Whisker the hare drew a wager in the
dust: whoever guessed the result of `0` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the integer 0.

Write a Clojure expression that computes the value of zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"0"}}]}
```

### Record 4 (form: `100`)

```
It was well known among the animals that the Hare boasted of his speed at every chance.

At a moss-covered milestone in the woods, Hopper the hare drew a wager in the
dust: whoever guessed the result of `100` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the integer 100.

Question: write a Clojure expression for the value of one hundred.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"100"}}]}
```

### Record 5 (form: `-25`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place at the edge of the orchard.

Mossback the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the orchard, the
next entry was the integer -25. Whisker the hare peered over
his shoulder at the form `-25` and asked what
it would come out to.

Write a Clojure expression that computes the value of negative twenty-five.

---

{"tool_calls":[{"name":"eval","args":{"form":"-25"}}]}
```

## G1-03: Ratios

- examples: 5
  - ex0: form=`1/2` expected=`'1/2'`
    concept=`the ratio 1/2`
    question_what=`the value of the ratio 1/2`
  - ex1: form=`3/4` expected=`'3/4'`
    concept=`the ratio 3/4`
    question_what=`the value of three-quarters`
  - ex2: form=`(+ 1/2 1/4)` expected=`'3/4'`
    concept=`the sum 1/2 + 1/4`
    question_what=`the value of (+ 1/2 1/4)`
  - ex3: form=`(* 2 1/2)` expected=`1`
    concept=`the product of 2 and 1/2`
    question_what=`the value of (* 2 1/2)`
  - ex4: form=`(- 1 1/3)` expected=`'2/3'`
    concept=`1 minus 1/3`
    question_what=`the value of (- 1 1/3)`

### Record 1 (form: `1/2`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place at the edge of the garden.

"There is no need to evaluate that," Whisker the hare said, boasting at every turn.
"Anyone can see what the ratio 1/2 comes to." Slowpoke the tortoise, who
in the garden had grown used to such claims, asked him to actually
write the form `1/2` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the value of the ratio 1/2.

---

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### Record 2 (form: `3/4`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the garden to watch
Bramble the hare attempt to outwit Shelly the tortoise at reading the REPL.
Shelly read aloud the ratio 3/4: the form was `3/4`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of three-quarters.

---

{"tool_calls":[{"name":"eval","args":{"form":"3/4"}}]}
```

### Record 3 (form: `(+ 1/2 1/4)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Hopper the hare stopped on the road and refused to
continue until someone could prove what the form `(+ 1/2 1/4)`
evaluated to. He called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the sum 1/2 + 1/4 to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value of (+ 1/2 1/4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### Record 4 (form: `(* 2 1/2)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened by the woods.

Mossback the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today at the edge of the woods, the
next entry was the product of 2 and 1/2. Bramble the hare peered over
his shoulder at the form `(* 2 1/2)` and asked what
it would come out to.

Question: write a Clojure expression for the value of (* 2 1/2).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 1/2)"}}]}
```

### Record 5 (form: `(- 1 1/3)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. It happened near the road.

Whisker the hare and Mossback the tortoise stopped on the road where someone had
written 1 minus 1/3 on a flat stone. Whisker, with great whoops of laughter, declared
that he could see the answer at a glance. Mossback,
saying very little, suggested they actually evaluate the form `(- 1 1/3)`
in the REPL and read off whatever it returned.

What Clojure form computes the value of (- 1 1/3)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- 1 1/3)"}}]}
```

## G1-04: Strings

- examples: 5
  - ex0: form=`"hello"` expected=`'hello'`
    concept=`the string "hello"`
    question_what=`the value of "hello"`
  - ex1: form=`"race"` expected=`'race'`
    concept=`the string "race"`
    question_what=`the value of "race"`
  - ex2: form=`"slow and steady"` expected=`'slow and steady'`
    concept=`the string "slow and steady"`
    question_what=`the value of "slow and steady"`
  - ex3: form=`""` expected=`''`
    concept=`the empty string`
    question_what=`the value of the empty string`
  - ex4: form=`"42"` expected=`'42'`
    concept=`the string "42"`
    question_what=`the value of the string "42"`

### Record 1 (form: `"hello"`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"There is no need to evaluate that," Pip the hare said, puffed up with pride.
"Anyone can see what the string "hello" comes to." Mossback the tortoise, who
on the road had grown used to such claims, asked them to actually
write the form `"hello"` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value of "hello".

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### Record 2 (form: `"race"`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Halfway through the race, Whisker the hare stopped near the garden and refused to
continue until someone could prove what the form `"race"`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the string "race" to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of "race".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"\"race\""}}]}
```

### Record 3 (form: `"slow and steady"`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

At a moss-covered milestone near the woods, Whisker the hare drew a wager in the
dust: whoever guessed the result of `"slow and steady"` first would win the
right to set the next race. Slowpoke the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the string "slow and steady".

Write a Clojure expression that computes the value of "slow and steady".

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"\"slow and steady\""}}]}
```

### Record 4 (form: `""`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Halfway through the race, Whisker the hare stopped in the woods and refused to
continue until someone could prove what the form `""`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the empty string to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the value of the empty string.

---

{"tool_calls":[{"name":"eval","args":{"form":"\"\""}}]}
```

### Record 5 (form: `"42"`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place by the meadow.

A small audience of forest creatures had gathered in the meadow to watch
Pip the hare attempt to outwit Shelly the tortoise at reading the REPL.
Shelly read aloud the string "42": the form was `"42"`.
The crowd waited to see who would correctly write the form to submit.

What Clojure form computes the value of the string "42"? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"\"42\""}}]}
```

## G1-05: Booleans

- examples: 6
  - ex0: form=`true` expected=`True`
    concept=`the literal true`
    question_what=`the value of true`
  - ex1: form=`false` expected=`False`
    concept=`the literal false`
    question_what=`the value of false`
  - ex2: form=`(= 1 1)` expected=`True`
    concept=`the equality (= 1 1)`
    question_what=`the value of (= 1 1)`
  - ex3: form=`(= 1 2)` expected=`False`
    concept=`the equality (= 1 2)`
    question_what=`the value of (= 1 2)`
  - ex4: form=`(< 3 5)` expected=`True`
    concept=`the comparison (< 3 5)`
    question_what=`the value of (< 3 5)`
  - ex5: form=`(> 3 5)` expected=`False`
    concept=`the comparison (> 3 5)`
    question_what=`the value of (> 3 5)`

### Record 1 (form: `true`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a moss-covered milestone on the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `true` first would win the
right to set the next race. Slowpoke the tortoise, her eyes always on the path, said it
was simpler to type the form into the REPL than to argue about
the literal true.

Question: write a Clojure expression for the value of true.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### Record 2 (form: `false`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened near the woods.

Halfway through the race, Hopper the hare stopped at the edge of the woods and refused to
continue until someone could prove what the form `false`
evaluated to. He called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the literal false to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of false.

---

{"tool_calls":[{"name":"eval","args":{"form":"false"}}]}
```

### Record 3 (form: `(= 1 1)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place at the edge of the garden.

Halfway through the race, Hopper the hare stopped in the garden and refused to
continue until someone could prove what the form `(= 1 1)`
evaluated to. He called it impossible.
Shelly the tortoise, walking up at her usual pace, simply said: "Submit
the equality (= 1 1) to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### Record 4 (form: `(= 1 2)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today in the orchard, the
next entry was the equality (= 1 2). Pip the hare peered over
his shoulder at the form `(= 1 2)` and asked what
it would come out to.

What Clojure form computes the value of (= 1 2)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### Record 5 (form: `(< 3 5)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place at the edge of the woods.

Halfway through the race, Pip the hare stopped near the woods and refused to
continue until someone could prove what the form `(< 3 5)`
evaluated to. They called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the comparison (< 3 5) to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of (< 3 5).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(< 3 5)"}}]}
```

## G1-06: nil

- examples: 5
  - ex0: form=`nil` expected=`None`
    concept=`the literal nil`
    question_what=`the value of nil`
  - ex1: form=`(nil? nil)` expected=`True`
    concept=`the predicate (nil? nil)`
    question_what=`whether nil is nil`
  - ex2: form=`(nil? 0)` expected=`False`
    concept=`the predicate (nil? 0)`
    question_what=`whether 0 is nil`
  - ex3: form=`(nil? false)` expected=`False`
    concept=`the predicate (nil? false)`
    question_what=`whether false is nil`
  - ex4: form=`(= nil nil)` expected=`True`
    concept=`the equality (= nil nil)`
    question_what=`the value of (= nil nil)`

### Record 1 (form: `nil`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today atop the hilltop, the
next entry was the literal nil. Bramble the hare peered over
his shoulder at the form `nil` and asked what
it would come out to.

Write a form whose evaluation gives the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### Record 2 (form: `(nil? nil)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"There is no need to evaluate that," Hopper the hare said, as if the race were already won.
"Anyone can see what the predicate (nil? nil) comes to." Mossback the tortoise, who
in the woods had grown used to such claims, asked him to actually
write the form `(nil? nil)` and submit it to the REPL — just to be
sure.

What Clojure form computes whether nil is nil? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(nil? nil)"}}]}
```

### Record 3 (form: `(nil? 0)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Hopper the hare said, swaggering through the underbrush.
"Anyone can see what the predicate (nil? 0) comes to." Slowpoke the tortoise, who
by the woods had grown used to such claims, asked him to actually
write the form `(nil? 0)` and submit it to the REPL — just to be
sure.

What Clojure form computes whether 0 is nil? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(nil? 0)"}}]}
```

### Record 4 (form: `(nil? false)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Mossback the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the orchard, the
next entry was the predicate (nil? false). Pip the hare peered over
his shoulder at the form `(nil? false)` and asked what
it would come out to.

What Clojure form computes whether false is nil? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(nil? false)"}}]}
```

### Record 5 (form: `(= nil nil)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a moss-covered milestone near the forest, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(= nil nil)` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the equality (= nil nil).

Write a form whose evaluation gives the value of (= nil nil).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= nil nil)"}}]}
```

## G1-07: Keywords

- examples: 5
  - ex0: form=`:hare` expected=`':hare'`
    concept=`the keyword :hare`
    question_what=`the value of :hare`
  - ex1: form=`:tortoise` expected=`':tortoise'`
    concept=`the keyword :tortoise`
    question_what=`the value of :tortoise`
  - ex2: form=`:winner` expected=`':winner'`
    concept=`the keyword :winner`
    question_what=`the value of :winner`
  - ex3: form=`(keyword? :hare)` expected=`True`
    concept=`the predicate (keyword? :hare)`
    question_what=`whether :hare is a keyword`
  - ex4: form=`(= :hare :hare)` expected=`True`
    concept=`the equality of two :hare keywords`
    question_what=`whether :hare equals :hare`

### Record 1 (form: `:hare`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise had been trying to teach Whisker the hare how the REPL
works. "Look here," he said, pointing to
the keyword :hare. "You hand the form `:hare` to the runtime, and
the runtime hands you back what it evaluates to." Whisker, drowsy from the warm sun,
agreed to try.

Question: write a Clojure expression for the value of :hare.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
```

### Record 2 (form: `:tortoise`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened at the edge of the forest.

Halfway through the race, Whisker the hare stopped at the edge of the forest and refused to
continue until someone could prove what the form `:tortoise`
evaluated to. He called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the keyword :tortoise to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the value of :tortoise.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":":tortoise"}}]}
```

### Record 3 (form: `:winner`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped in the orchard where someone had
written the keyword :winner on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
untroubled by what others thought, suggested they actually evaluate the form `:winner`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value of :winner.

---

{"tool_calls":[{"name":"eval","args":{"form":":winner"}}]}
```

### Record 4 (form: `(keyword? :hare)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place near the hilltop.

Mossback the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the predicate (keyword? :hare). "You hand the form `(keyword? :hare)` to the runtime, and
the runtime hands you back what it evaluates to." Pip, lulled by the gentle wind,
agreed to try.

Write a Clojure expression that computes whether :hare is a keyword.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(keyword? :hare)"}}]}
```

### Record 5 (form: `(= :hare :hare)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered by the garden to watch
Whisker the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the equality of two :hare keywords: the form was `(= :hare :hare)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes whether :hare equals :hare.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(= :hare :hare)"}}]}
```

## G1-08: Characters

- examples: 4
  - ex0: form=`\h` expected=`'h'`
    concept=`the character \h`
    question_what=`the value of \h`
  - ex1: form=`\space` expected=`' '`
    concept=`the character \space`
    question_what=`the value of \space`
  - ex2: form=`\T` expected=`'T'`
    concept=`the character \T`
    question_what=`the value of \T`
  - ex3: form=`(char? \h)` expected=`True`
    concept=`the predicate (char? \h)`
    question_what=`whether \h is a character`

### Record 1 (form: `\h`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the orchard.

At a moss-covered milestone at the edge of the orchard, Hopper the hare drew a wager in the
dust: whoever guessed the result of `\h` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the character \h.

Question: write a Clojure expression for the value of \h.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"\\h"}}]}
```

### Record 2 (form: `\space`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

At a moss-covered milestone near the road, Hopper the hare drew a wager in the
dust: whoever guessed the result of `\space` first would win the
right to set the next race. Shelly the tortoise, her eyes always on the path, said it
was simpler to type the form into the REPL than to argue about
the character \space.

Question: write a Clojure expression for the value of \space.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"\\space"}}]}
```

### Record 3 (form: `\T`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today by the orchard, the
next entry was the character \T. Bramble the hare peered over
his shoulder at the form `\T` and asked what
it would come out to.

Write a form whose evaluation gives the value of \T.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\T"}}]}
```

### Record 4 (form: `(char? \h)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened in the orchard.

Whisker the hare and Slowpoke the tortoise stopped at the edge of the orchard where someone had
written the predicate (char? \h) on a flat stone. Whisker, with great whoops of laughter, declared
that he could see the answer at a glance. Slowpoke,
untroubled by what others thought, suggested they actually evaluate the form `(char? \h)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives whether \h is a character.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(char? \\h)"}}]}
```

### Record 5 (form: `\h`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a moss-covered milestone in the meadow, Hopper the hare drew a wager in the
dust: whoever guessed the result of `\h` first would win the
right to set the next race. Shelly the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the character \h.

Write a Clojure expression that computes the value of \h.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"\\h"}}]}
```

## G1-09: Symbols vs values

- examples: 4
  - ex0: form=`(symbol? 'hare)` expected=`True`
    concept=`the predicate (symbol? 'hare)`
    question_what=`whether 'hare is a symbol`
  - ex1: form=`(symbol? 42)` expected=`False`
    concept=`the predicate (symbol? 42)`
    question_what=`whether 42 is a symbol`
  - ex2: form=`'hare` expected=`'hare'`
    concept=`the quoted symbol 'hare`
    question_what=`the value of 'hare`
  - ex3: form=`(= 'hare 'hare)` expected=`True`
    concept=`the equality of two 'hare symbols`
    question_what=`whether 'hare equals 'hare`

### Record 1 (form: `(symbol? 'hare)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A small audience of forest creatures had gathered by the garden to watch
Bramble the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the predicate (symbol? 'hare): the form was `(symbol? 'hare)`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives whether 'hare is a symbol.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
```

### Record 2 (form: `(symbol? 42)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened near the forest.

"There is no need to evaluate that," Bramble the hare said, with great whoops of laughter.
"Anyone can see what the predicate (symbol? 42) comes to." Mossback the tortoise, who
in the forest had grown used to such claims, asked her to actually
write the form `(symbol? 42)` and submit it to the REPL — just to be
sure.

What Clojure form computes whether 42 is a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 42)"}}]}
```

### Record 3 (form: `'hare`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place at the edge of the garden.

Bramble the hare and Slowpoke the tortoise stopped in the garden where someone had
written the quoted symbol 'hare on a flat stone. Bramble, with a smug grin, declared
that she could see the answer at a glance. Slowpoke,
untroubled by what others thought, suggested they actually evaluate the form `'hare`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value of 'hare.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"'hare"}}]}
```

### Record 4 (form: `(= 'hare 'hare)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today in the meadow, the
next entry was the equality of two 'hare symbols. Pip the hare peered over
his shoulder at the form `(= 'hare 'hare)` and asked what
it would come out to.

Question: write a Clojure expression for whether 'hare equals 'hare.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= 'hare 'hare)"}}]}
```

### Record 5 (form: `(symbol? 'hare)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the meadow.

At a moss-covered milestone by the meadow, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(symbol? 'hare)` first would win the
right to set the next race. Shelly the tortoise, saying very little, said it
was simpler to type the form into the REPL than to argue about
the predicate (symbol? 'hare).

Question: write a Clojure expression for whether 'hare is a symbol.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
```

## G1-10: Comments

- examples: 2
  - ex0: form=`(+ 1 2) ; sum of one and two` expected=`3`
    concept=`the form (+ 1 2) followed by a comment`
    question_what=`the result of (+ 1 2) ignoring the comment`
  - ex1: form=`42 ;; the answer` expected=`42`
    concept=`the literal 42 with a trailing comment`
    question_what=`the value of 42`

### Record 1 (form: `(+ 1 2) ; sum of one and two`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened at the edge of the woods.

A small audience of forest creatures had gathered by the woods to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the form (+ 1 2) followed by a comment: the form was `(+ 1 2) ; sum of one and two`.
The crowd waited to see who would correctly write the form to submit.

Question: write a Clojure expression for the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### Record 2 (form: `42 ;; the answer`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place near the road.

At a moss-covered milestone near the road, Whisker the hare drew a wager in the
dust: whoever guessed the result of `42 ;; the answer` first would win the
right to set the next race. Shelly the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the literal 42 with a trailing comment.

What Clojure form computes the value of 42? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### Record 3 (form: `(+ 1 2) ; sum of one and two`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone in the forest, Pip the hare drew a wager in the
dust: whoever guessed the result of `(+ 1 2) ; sum of one and two` first would win the
right to set the next race. Mossback the tortoise, saying very little, said it
was simpler to type the form into the REPL than to argue about
the form (+ 1 2) followed by a comment.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### Record 4 (form: `42 ;; the answer`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

A small audience of forest creatures had gathered at the edge of the forest to watch
Whisker the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback read aloud the literal 42 with a trailing comment: the form was `42 ;; the answer`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42 ;; the answer"}}]}
```

### Record 5 (form: `(+ 1 2) ; sum of one and two`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place in the meadow.

At a moss-covered milestone near the meadow, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(+ 1 2) ; sum of one and two` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (+ 1 2) followed by a comment.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

## G1-11: Whitespace doesn't matter

- examples: 2
  - ex0: form=`(+    1    2)` expected=`3`
    concept=`the form (+ 1 2) with extra spaces`
    question_what=`the result of the form`
  - ex1: form=`(+
  1
  2)` expected=`3`
    concept=`the form (+ 1 2) split across lines`
    question_what=`the result of the form`

### Record 1 (form: `(+    1    2)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened atop the hilltop.

A small audience of forest creatures had gathered at the edge of the hilltop to watch
Hopper the hare attempt to outwit Shelly the tortoise at reading the REPL.
Shelly read aloud the form (+ 1 2) with extra spaces: the form was `(+    1    2)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### Record 2 (form: `(+
  1
  2)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened at the edge of the forest.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today at the edge of the forest, the
next entry was the form (+ 1 2) split across lines. Hopper the hare peered over
her shoulder at the form `(+
  1
  2)` and asked what
it would come out to.

Write a form whose evaluation gives the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### Record 3 (form: `(+    1    2)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Pip the hare and Shelly the tortoise stopped at the edge of the forest where someone had
written the form (+ 1 2) with extra spaces on a flat stone. Pip, with a smug grin, declared
that they could see the answer at a glance. Shelly,
with steady, careful steps, suggested they actually evaluate the form `(+    1    2)`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### Record 4 (form: `(+
  1
  2)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Whisker the hare said, puffed up with pride.
"Anyone can see what the form (+ 1 2) split across lines comes to." Mossback the tortoise, who
near the hilltop had grown used to such claims, asked him to actually
write the form `(+
  1
  2)` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+\n  1\n  2)"}}]}
```

### Record 5 (form: `(+    1    2)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

At a moss-covered milestone in the forest, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(+    1    2)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the form (+ 1 2) with extra spaces.

What Clojure form computes the result of the form? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

## G1-12: Parens group; they don't multiply

- examples: 2
  - ex0: form=`(+ 2 3)` expected=`5`
    concept=`the form (+ 2 3)`
    question_what=`the result of (+ 2 3)`
  - ex1: form=`(* (+ 1 2) 3)` expected=`9`
    concept=`the form (* (+ 1 2) 3)`
    question_what=`the result of (* (+ 1 2) 3)`

### Record 1 (form: `(+ 2 3)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the meadow.

Mossback the tortoise had been trying to teach Whisker the hare how the REPL
works. "Look here," he said, pointing to
the form (+ 2 3). "You hand the form `(+ 2 3)` to the runtime, and
the runtime hands you back what it evaluates to." Whisker, lulled by the gentle wind,
agreed to try.

Write a Clojure expression that computes the result of (+ 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### Record 2 (form: `(* (+ 1 2) 3)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A wooden sign nailed to a tree in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(* (+ 1 2) 3)`. Whisker
laughed, boasting at every turn, and declared it too easy. Mossback said
patiently that the only way to be sure of the form (* (+ 1 2) 3) was to put
it in the REPL.

Write a Clojure expression that computes the result of (* (+ 1 2) 3).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### Record 3 (form: `(+ 2 3)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped by the forest where someone had
written the form (+ 2 3) on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(+ 2 3)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result of (+ 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### Record 4 (form: `(* (+ 1 2) 3)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A wooden sign nailed to a tree on the road carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(* (+ 1 2) 3)`. Pip
laughed, swaggering through the underbrush, and declared it too easy. Mossback said
patiently that the only way to be sure of the form (* (+ 1 2) 3) was to put
it in the REPL.

Write a form whose evaluation gives the result of (* (+ 1 2) 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) 3)"}}]}
```

### Record 5 (form: `(+ 2 3)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A wooden sign nailed to a tree near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(+ 2 3)`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Mossback said
patiently that the only way to be sure of the form (+ 2 3) was to put
it in the REPL.

What Clojure form computes the result of (+ 2 3)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

## G1-13: First arithmetic call

- examples: 6
  - ex0: form=`(+ 1 2)` expected=`3`
    concept=`the form (+ 1 2)`
    question_what=`the result of (+ 1 2)`
  - ex1: form=`(- 5 3)` expected=`2`
    concept=`the form (- 5 3)`
    question_what=`the result of (- 5 3)`
  - ex2: form=`(* 4 5)` expected=`20`
    concept=`the form (* 4 5)`
    question_what=`the result of (* 4 5)`
  - ex3: form=`(/ 10 2)` expected=`5`
    concept=`the form (/ 10 2)`
    question_what=`the result of (/ 10 2)`
  - ex4: form=`(+ 7 8)` expected=`15`
    concept=`the form (+ 7 8)`
    question_what=`the result of (+ 7 8)`
  - ex5: form=`(- 20 7)` expected=`13`
    concept=`the form (- 20 7)`
    question_what=`the result of (- 20 7)`

### Record 1 (form: `(+ 1 2)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance.

Halfway through the race, Hopper the hare stopped atop the hilltop and refused to
continue until someone could prove what the form `(+ 1 2)`
evaluated to. He called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the form (+ 1 2) to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the result of (+ 1 2).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 2 (form: `(- 5 3)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened at the edge of the forest.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today by the forest, the
next entry was the form (- 5 3). Pip the hare peered over
his shoulder at the form `(- 5 3)` and asked what
it would come out to.

Write a form whose evaluation gives the result of (- 5 3).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(- 5 3)"}}]}
```

### Record 3 (form: `(* 4 5)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened along the road.

A wooden sign nailed to a tree along the road carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(* 4 5)`. Bramble
laughed, swaggering through the underbrush, and declared it too easy. Mossback said
patiently that the only way to be sure of the form (* 4 5) was to put
it in the REPL.

Write a form whose evaluation gives the result of (* 4 5).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(* 4 5)"}}]}
```

### Record 4 (form: `(/ 10 2)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A small audience of forest creatures had gathered atop the hilltop to watch
Bramble the hare attempt to outwit Shelly the tortoise at reading the REPL.
Shelly read aloud the form (/ 10 2): the form was `(/ 10 2)`.
The crowd waited to see who would correctly write the form to submit.

Question: write a Clojure expression for the result of (/ 10 2).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### Record 5 (form: `(+ 7 8)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. It happened in the garden.

A wooden sign nailed to a tree in the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(+ 7 8)`. Hopper
laughed, with a smug grin, and declared it too easy. Mossback said
patiently that the only way to be sure of the form (+ 7 8) was to put
it in the REPL.

What Clojure form computes the result of (+ 7 8)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 7 8)"}}]}
```

## G1-14: Nested call evaluation

- examples: 4
  - ex0: form=`(+ 1 (* 2 3))` expected=`7`
    concept=`the nested form (+ 1 (* 2 3))`
    question_what=`the result of (+ 1 (* 2 3))`
  - ex1: form=`(* (+ 1 2) (+ 3 4))` expected=`21`
    concept=`the nested form (* (+ 1 2) (+ 3 4))`
    question_what=`the result of (* (+ 1 2) (+ 3 4))`
  - ex2: form=`(- 100 (* 5 5))` expected=`75`
    concept=`the nested form (- 100 (* 5 5))`
    question_what=`the result of (- 100 (* 5 5))`
  - ex3: form=`(+ (* 2 3) (* 4 5))` expected=`26`
    concept=`the sum of two products`
    question_what=`the result of (+ (* 2 3) (* 4 5))`

### Record 1 (form: `(+ 1 (* 2 3))`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

A small audience of forest creatures had gathered atop the hilltop to watch
Hopper the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the nested form (+ 1 (* 2 3)): the form was `(+ 1 (* 2 3))`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives the result of (+ 1 (* 2 3)).

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### Record 2 (form: `(* (+ 1 2) (+ 3 4))`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today along the road, the
next entry was the nested form (* (+ 1 2) (+ 3 4)). Whisker the hare peered over
her shoulder at the form `(* (+ 1 2) (+ 3 4))` and asked what
it would come out to.

Question: write a Clojure expression for the result of (* (+ 1 2) (+ 3 4)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* (+ 1 2) (+ 3 4))"}}]}
```

### Record 3 (form: `(- 100 (* 5 5))`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was in the meadow.

At a moss-covered milestone at the edge of the meadow, Pip the hare drew a wager in the
dust: whoever guessed the result of `(- 100 (* 5 5))` first would win the
right to set the next race. Mossback the tortoise, her eyes always on the path, said it
was simpler to type the form into the REPL than to argue about
the nested form (- 100 (* 5 5)).

Write a form whose evaluation gives the result of (- 100 (* 5 5)).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(- 100 (* 5 5))"}}]}
```

### Record 4 (form: `(+ (* 2 3) (* 4 5))`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Hopper the hare and Shelly the tortoise stopped at the edge of the hilltop where someone had
written the sum of two products on a flat stone. Hopper, boasting at every turn, declared
that he could see the answer at a glance. Shelly,
her eyes always on the path, suggested they actually evaluate the form `(+ (* 2 3) (* 4 5))`
in the REPL and read off whatever it returned.

What Clojure form computes the result of (+ (* 2 3) (* 4 5))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ (* 2 3) (* 4 5))"}}]}
```

### Record 5 (form: `(+ 1 (* 2 3))`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a moss-covered milestone near the forest, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(+ 1 (* 2 3))` first would win the
right to set the next race. Mossback the tortoise, her eyes always on the path, said it
was simpler to type the form into the REPL than to argue about
the nested form (+ 1 (* 2 3)).

Write a form whose evaluation gives the result of (+ 1 (* 2 3)).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

## G1-15: Equality

- examples: 6
  - ex0: form=`(= 1 1)` expected=`True`
    concept=`the equality (= 1 1)`
    question_what=`the value of (= 1 1)`
  - ex1: form=`(= 1 2)` expected=`False`
    concept=`the equality (= 1 2)`
    question_what=`the value of (= 1 2)`
  - ex2: form=`(= "a" "a")` expected=`True`
    concept=`the equality (= "a" "a")`
    question_what=`the value of (= "a" "a")`
  - ex3: form=`(= :hare :hare)` expected=`True`
    concept=`the equality (= :hare :hare)`
    question_what=`the value of (= :hare :hare)`
  - ex4: form=`(= :hare :tortoise)` expected=`False`
    concept=`the equality (= :hare :tortoise)`
    question_what=`the value of (= :hare :tortoise)`
  - ex5: form=`(= 1 1 1 1)` expected=`True`
    concept=`the multi-arg equality (= 1 1 1 1)`
    question_what=`the value of (= 1 1 1 1)`

### Record 1 (form: `(= 1 1)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a moss-covered milestone in the meadow, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(= 1 1)` first would win the
right to set the next race. Shelly the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the equality (= 1 1).

Write a Clojure expression that computes the value of (= 1 1).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### Record 2 (form: `(= 1 2)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped on the hilltop where someone had
written the equality (= 1 2) on a flat stone. Hopper, boasting at every turn, declared
that he could see the answer at a glance. Mossback,
with steady, careful steps, suggested they actually evaluate the form `(= 1 2)`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of (= 1 2).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 2)"}}]}
```

### Record 3 (form: `(= "a" "a")`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place at the edge of the woods.

Halfway through the race, Whisker the hare stopped at the edge of the woods and refused to
continue until someone could prove what the form `(= "a" "a")`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the equality (= "a" "a") to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the value of (= "a" "a").

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(= \"a\" \"a\")"}}]}
```

### Record 4 (form: `(= :hare :hare)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A small audience of forest creatures had gathered near the woods to watch
Bramble the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback read aloud the equality (= :hare :hare): the form was `(= :hare :hare)`.
The crowd waited to see who would correctly write the form to submit.

Question: write a Clojure expression for the value of (= :hare :hare).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= :hare :hare)"}}]}
```

### Record 5 (form: `(= :hare :tortoise)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the orchard.

"There is no need to evaluate that," Pip the hare said, puffed up with pride.
"Anyone can see what the equality (= :hare :tortoise) comes to." Mossback the tortoise, who
in the orchard had grown used to such claims, asked them to actually
write the form `(= :hare :tortoise)` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the value of (= :hare :tortoise).

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= :hare :tortoise)"}}]}
```

## G1-16: Numeric predicates

- examples: 6
  - ex0: form=`(zero? 0)` expected=`True`
    concept=`the predicate (zero? 0)`
    question_what=`whether 0 is zero`
  - ex1: form=`(zero? 5)` expected=`False`
    concept=`the predicate (zero? 5)`
    question_what=`whether 5 is zero`
  - ex2: form=`(pos? 7)` expected=`True`
    concept=`the predicate (pos? 7)`
    question_what=`whether 7 is positive`
  - ex3: form=`(pos? -2)` expected=`False`
    concept=`the predicate (pos? -2)`
    question_what=`whether -2 is positive`
  - ex4: form=`(neg? -3)` expected=`True`
    concept=`the predicate (neg? -3)`
    question_what=`whether -3 is negative`
  - ex5: form=`(neg? 4)` expected=`False`
    concept=`the predicate (neg? 4)`
    question_what=`whether 4 is negative`

### Record 1 (form: `(zero? 0)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place near the meadow.

At a moss-covered milestone by the meadow, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(zero? 0)` first would win the
right to set the next race. Shelly the tortoise, saying very little, said it
was simpler to type the form into the REPL than to argue about
the predicate (zero? 0).

Question: write a Clojure expression for whether 0 is zero.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### Record 2 (form: `(zero? 5)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place in the orchard.

Shelly the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," she said, pointing to
the predicate (zero? 5). "You hand the form `(zero? 5)` to the runtime, and
the runtime hands you back what it evaluates to." Pip, lulled by the gentle wind,
agreed to try.

What Clojure form computes whether 5 is zero? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 5)"}}]}
```

### Record 3 (form: `(pos? 7)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened by the meadow.

"There is no need to evaluate that," Bramble the hare said, swaggering through the underbrush.
"Anyone can see what the predicate (pos? 7) comes to." Mossback the tortoise, who
at the edge of the meadow had grown used to such claims, asked her to actually
write the form `(pos? 7)` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes whether 7 is positive.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? 7)"}}]}
```

### Record 4 (form: `(pos? -2)`)

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was at the edge of the woods.

Halfway through the race, Bramble the hare stopped at the edge of the woods and refused to
continue until someone could prove what the form `(pos? -2)`
evaluated to. She called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the predicate (pos? -2) to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes whether -2 is positive.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(pos? -2)"}}]}
```

### Record 5 (form: `(neg? -3)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Whisker the hare and Slowpoke the tortoise stopped by the forest where someone had
written the predicate (neg? -3) on a flat stone. Whisker, with great whoops of laughter, declared
that he could see the answer at a glance. Slowpoke,
without complaint, suggested they actually evaluate the form `(neg? -3)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives whether -3 is negative.

---

{"tool_calls":[{"name":"eval","args":{"form":"(neg? -3)"}}]}
```

## G1-17: Printing vs returning

- examples: 2
  - ex0: form=`42` expected=`42`
    concept=`the value 42`
    question_what=`the value of 42`
  - ex1: form=`(+ 1 2)` expected=`3`
    concept=`the form (+ 1 2)`
    question_what=`the result of (+ 1 2)`

### Record 1 (form: `42`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone in the forest, Pip the hare drew a wager in the
dust: whoever guessed the result of `42` first would win the
right to set the next race. Mossback the tortoise, saying very little, said it
was simpler to type the form into the REPL than to argue about
the value 42.

Write a Clojure expression that computes the value of 42.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 2 (form: `(+ 1 2)`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

A small audience of forest creatures had gathered at the edge of the forest to watch
Whisker the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback read aloud the form (+ 1 2): the form was `(+ 1 2)`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 3 (form: `42`)

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. All this took place in the meadow.

At a moss-covered milestone near the meadow, Whisker the hare drew a wager in the
dust: whoever guessed the result of `42` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the value 42.

Write a Clojure expression that computes the value of 42.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### Record 4 (form: `(+ 1 2)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. It happened by the orchard.

Shelly the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," she said, pointing to
the form (+ 1 2). "You hand the form `(+ 1 2)` to the runtime, and
the runtime hands you back what it evaluates to." Pip, weary from the morning's effort,
agreed to try.

Write a form whose evaluation gives the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 5 (form: `42`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. It happened near the road.

Halfway through the race, Pip the hare stopped on the road and refused to
continue until someone could prove what the form `42`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the value 42 to the REPL. Whatever comes back is the answer."

What Clojure form computes the value of 42? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

## G1-18: Errors are safe in the REPL

- examples: 2
  - ex0: form=`(+ 1 2)` expected=`3`
    concept=`the form (+ 1 2)`
    question_what=`the result of (+ 1 2)`
  - ex1: form=`(* 7 6)` expected=`42`
    concept=`the form (* 7 6)`
    question_what=`the result of (* 7 6)`

### Record 1 (form: `(+ 1 2)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Pip the hare and Shelly the tortoise stopped at the edge of the forest where someone had
written the form (+ 1 2) on a flat stone. Pip, with a smug grin, declared
that they could see the answer at a glance. Shelly,
with steady, careful steps, suggested they actually evaluate the form `(+ 1 2)`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 2 (form: `(* 7 6)`)

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Whisker the hare said, puffed up with pride.
"Anyone can see what the form (* 7 6) comes to." Mossback the tortoise, who
near the hilltop had grown used to such claims, asked him to actually
write the form `(* 7 6)` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the result of (* 7 6).

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### Record 3 (form: `(+ 1 2)`)

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

At a moss-covered milestone in the forest, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(+ 1 2)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the form (+ 1 2).

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### Record 4 (form: `(* 7 6)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"There is no need to evaluate that," Pip the hare said, with great whoops of laughter.
"Anyone can see what the form (* 7 6) comes to." Slowpoke the tortoise, who
in the orchard had grown used to such claims, asked them to actually
write the form `(* 7 6)` and submit it to the REPL — just to be
sure.

What Clojure form computes the result of (* 7 6)? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(* 7 6)"}}]}
```

### Record 5 (form: `(+ 1 2)`)

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place at the edge of the garden.

Slowpoke the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," he said, pointing to
the form (+ 1 2). "You hand the form `(+ 1 2)` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, drowsy from the warm sun,
agreed to try.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

