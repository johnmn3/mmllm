# Spot-check: 1 sample record per tortoise-hare subject

Manual-review dump. Each subject gets one rendered record.

---

## Grade 1

### G1-01: Eval as substitution

**form**: `42`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today near the hilltop, the
next entry was the value 42. Bramble the hare peered over
his shoulder at the form `42` and asked what
it would come out to.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-02: Integer numbers

**form**: `7`  •  **expected**: `7`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the integer 7 on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `7`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-03: Ratios

**form**: `1/2`  •  **expected**: `'1/2'`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

"There is no need to evaluate that," Hopper the hare said swaggering through the underbrush.
"Anyone can see what the ratio 1/2 comes to." Slowpoke the tortoise, who
at the edge of the garden had grown used to such claims, asked him to actually
write the form `1/2` and submit it to the REPL — just to be
sure.

What Clojure form computes the value of the ratio 1/2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-04: Strings

**form**: `"hello"`  •  **expected**: `'hello'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A wooden sign nailed to a tree across the hilltop carried a puzzle. The riddle
was simple: it asked the reader to evaluate `"hello"`. Bramble
laughed, with a smug grin, and declared it too easy. Shelly said
patiently that the only way to be sure of the string "hello" was to put
it in the REPL.

Question: write a Clojure expression for the value of "hello".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-05: Booleans

**form**: `true`  •  **expected**: `True`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A small audience of forest creatures had gathered by the woods to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the literal true: the form was `true`.
The crowd waited to see who would correctly write the form to submit.

Question: write a Clojure expression for the value of true.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-06: nil

**form**: `nil`  •  **expected**: `None`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A wooden sign nailed to a tree near the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `nil`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Shelly said
patiently that the only way to be sure of the literal nil was to put
it in the REPL.

Question: write a Clojure expression for the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-07: Keywords

**form**: `:hare`  •  **expected**: `':hare'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered across the forest to watch
Whisker the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback read aloud the keyword :hare: the form was `:hare`.
The crowd waited to see who would correctly write the form to submit.

Write a form whose evaluation gives the value of :hare.

---

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
```

### G1-08: Characters

**form**: `\h`  •  **expected**: `'h'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

Whisker the hare and Shelly the tortoise stopped near the hilltop where someone had
written the character \h on a flat stone. Whisker, with a smug grin, declared
that he could see the answer at a glance. Shelly,
without complaint, suggested they actually evaluate the form `\h`
in the REPL and read off whatever it returned.

What Clojure form computes the value of \h? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\h"}}]}
```

### G1-09: Symbols vs values

**form**: `(symbol? 'hare)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

Hopper the hare and Shelly the tortoise stopped by the forest where someone had
written the predicate (symbol? 'hare) on a flat stone. Hopper, boasting at every turn, declared
that he could see the answer at a glance. Shelly,
with steady, careful steps, suggested they actually evaluate the form `(symbol? 'hare)`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for whether 'hare is a symbol.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
```

### G1-10: Comments

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the form (+ 1 2) followed by a comment on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(+ 1 2) ; sum of one and two`
in the REPL and read off whatever it returned.

What Clojure form computes the result of (+ 1 2) ignoring the comment? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-11: Whitespace doesn't matter

**form**: `(+    1    2)`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Halfway through the race, Hopper the hare stopped in the meadow and refused to
continue until someone could prove what the form `(+    1    2)`
evaluated to. He called it impossible.
Shelly the tortoise, walking up at her usual pace, simply said: "Submit
the form (+ 1 2) with extra spaces to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the result of (+    1    2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-12: Parens group; they don't multiply

**form**: `(+ 2 3)`  •  **expected**: `5`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(+ 2 3)` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (+ 2 3).

Question: write a Clojure expression for the result of (+ 2 3) — note the parens are syntax, not multiplication.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-13: First arithmetic call

**form**: `(+ 1 2)`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Bramble the hare and Mossback the tortoise stopped at the edge of the orchard where someone had
written the form (+ 1 2) on a flat stone. Bramble, boasting at every turn, declared
that she could see the answer at a glance. Mossback,
with steady, careful steps, suggested they actually evaluate the form `(+ 1 2)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-14: Nested call evaluation

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the nested form (+ 1 (* 2 3)). "You hand the form `(+ 1 (* 2 3))` to the runtime, and
the runtime hands you back what it evaluates to." Pip, lulled by the gentle wind
from a recent sprint, agreed to try.

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-15: Equality

**form**: `(= 1 1)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Pip the hare said with great whoops of laughter.
"Anyone can see what the equality (= 1 1) comes to." Shelly the tortoise, who
near the hilltop had grown used to such claims, asked them to actually
write the form `(= 1 1)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-16: Numeric predicates

**form**: `(zero? 0)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the predicate (zero? 0) comes to." Mossback the tortoise, who
at the edge of the road had grown used to such claims, asked her to actually
write the form `(zero? 0)` and submit it to the REPL — just to be
sure.

What Clojure form computes whether 0 is zero? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-17: Printing vs returning

**form**: `42`  •  **expected**: `42`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

Slowpoke the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today by the meadow, the
next entry was the value 42 (the REPL returns it; doesn't 'print' it). Hopper the hare peered over
his shoulder at the form `42` and asked what
it would come out to.

Write a Clojure expression that computes what 42 evaluates to (the return value, what the REPL displays).

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-18: Errors are safe in the REPL

**form**: `(+ 1 2)`  •  **expected**: `3`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

A wooden sign nailed to a tree by the road carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(+ 1 2)`. Bramble
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form (+ 1 2) was to put
it in the REPL.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

## Grade 2

### G2-01: Multi-arg arithmetic

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the sum (+ 1 2 3 4) comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(+ 1 2 3 4)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the result of (+ 1 2 3 4).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
```

### G2-02: Comparison chains

**form**: `(< 1 2 3)`  •  **expected**: `True`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the chain (< 1 2 3) on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(< 1 2 3)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives whether 1 < 2 < 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(< 1 2 3)"}}]}
```

### G2-03: not= and = with multiple args

**form**: `(not= 1 2)`  •  **expected**: `True`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(not= 1 2)`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form (not= 1 2) was to put
it in the REPL.

What Clojure form computes whether 1 differs from 2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(not= 1 2)"}}]}
```

### G2-04: min and max

**form**: `(min 1 2 3)`  •  **expected**: `1`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"Whatever `(min 1 2 3)` comes to," Bramble the hare declared with a smug grin
across the hilltop, "I'll wager I know it without typing it." Shelly the tortoise,
saying very little, picked up a stick and drew the form (min 1 2 3) in the
dust. "Then write the form," she said. "The REPL will
have the last word."

Question: write a Clojure expression for the minimum of 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(min 1 2 3)"}}]}
```

### G2-05: quot, rem, mod

**form**: `(quot 17 5)`  •  **expected**: `3`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(quot 17 5)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the integer quotient of 17 and 5 to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the result of (quot 17 5).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(quot 17 5)"}}]}
```

### G2-06: inc and dec

**form**: `(inc 5)`  •  **expected**: `6`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Whatever `(inc 5)` comes to," Hopper the hare declared swaggering through the underbrush
near the woods, "I'll wager I know it without typing it." Shelly the tortoise,
her eyes always on the path, picked up a stick and drew the form (inc 5) in the
dust. "Then write the form," she said. "The REPL will
have the last word."

Question: write a Clojure expression for 5 plus 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(inc 5)"}}]}
```

### G2-07: Absolute value

**form**: `(abs 5)`  •  **expected**: `5`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(abs 5)`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the form (abs 5) to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the absolute value of 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(abs 5)"}}]}
```

### G2-08: Arithmetic on ratios

**form**: `(+ 1/2 1/4)`  •  **expected**: `'3/4'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(+ 1/2 1/4)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the sum 1/2 + 1/4.

What Clojure form computes the value of (+ 1/2 1/4)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1/2 1/4)"}}]}
```

### G2-09: Floats vs ints (the / operator)

**form**: `(/ 10 2)`  •  **expected**: `5`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(/ 10 2)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the integer division 10 ÷ 2.

Question: write a Clojure expression for the value of (/ 10 2).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(/ 10 2)"}}]}
```

### G2-10: Powers via repeated multiplication

**form**: `(* 2 2 2)`  •  **expected**: `8`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written two cubed on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(* 2 2 2)`
in the REPL and read off whatever it returned.

What Clojure form computes 2 to the third power? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(* 2 2 2)"}}]}
```

### G2-11: String concatenation with str

**form**: `(str "tor" "toise")`  •  **expected**: `'tortoise'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was the form (str "tor" "toise"). Hopper the hare peered over
her shoulder at the form `(str "tor" "toise")` and asked what
it would come out to.

Write a Clojure expression that computes the joined string "tortoise".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"tor\" \"toise\")"}}]}
```

### G2-12: print and println — return values

**form**: `(println "hello")`  •  **expected**: `None`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(println "hello")` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (println "hello") (note: it prints, but returns nil).

Question: write a Clojure expression for the return value of (println "hello") (it is nil).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(println \"hello\")"}}]}
```

### G2-13: and / or — short circuit, return values

**form**: `(and true true)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(and true true)` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the form (and true true).

Write a form whose evaluation gives the value of (and true true).

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
```

### G2-14: not — turning truthy to false

**form**: `(not true)`  •  **expected**: `False`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the form (not true): the form was `(not true)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (not true).

---

{"tool_calls":[{"name":"eval","args":{"form":"(not true)"}}]}
```

### G2-15: Falsey values: only false and nil

**form**: `(if 0 :truthy :falsey)`  •  **expected**: `':truthy'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise had been laying out a chain of small computations on
a slate near the hilltop — one operation, then another, all to settle a
question Pip the hare had raised. The current form on the slate was
`(if 0 :truthy :falsey)`, and Shelly explained that the form (if 0 :truthy :falsey) would
be settled the moment the form was evaluated.

Write a form whose evaluation gives which keyword (if 0 :truthy :falsey) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 :truthy :falsey)"}}]}
```

### G2-16: Truthy 0 and empty string

**form**: `(boolean 0)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise had been laying out a chain of small computations on
a slate at the edge of the road — one operation, then another, all to settle a
question Bramble the hare had raised. The current form on the slate was
`(boolean 0)`, and Mossback explained that the form (boolean 0) would
be settled the moment the form was evaluated.

What Clojure form computes the truthiness of 0? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(boolean 0)"}}]}
```

### G2-17: Keyword as function for map lookup

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

"There is no need to evaluate that," Hopper the hare said with a smug grin.
"Anyone can see what the form (:hare {:hare 1 :tortoise 2}) comes to." Slowpoke the tortoise, who
by the meadow had grown used to such claims, asked him to actually
write the form `(:hare {:hare 1 :tortoise 2})` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the value (:hare {:hare 1 :tortoise 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
```

### G2-18: Quoting symbols

**form**: `(quote hare)`  •  **expected**: `'hare'`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"Whatever `(quote hare)` comes to," Bramble the hare declared swaggering through the underbrush
by the road, "I'll wager I know it without typing it." Slowpoke the tortoise,
her eyes always on the path, picked up a stick and drew the quoted symbol (quote hare) in the
dust. "Then write the form," he said. "The REPL will
have the last word."

What Clojure form computes the value of (quote hare)? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(quote hare)"}}]}
```

### G2-19: Auto-promotion to bigint

**form**: `(* 1000000 1000000)`  •  **expected**: `1000000000000`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise had been laying out a chain of small computations on
a slate in the meadow — one operation, then another, all to settle a
question Pip the hare had raised. The current form on the slate was
`(* 1000000 1000000)`, and Slowpoke explained that the form (* 1000000 1000000) would
be settled the moment the form was evaluated.

Question: write a Clojure expression for the result of one million times one million.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(* 1000000 1000000)"}}]}
```

### G2-20: Counting

**form**: `(count [1 2 3])`  •  **expected**: `3`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Shelly the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," she said, pointing to
the count of [1 2 3]. "You hand the form `(count [1 2 3])` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, her legs heavy from sprinting
from a recent sprint, agreed to try.

Write a Clojure expression that computes the count of the vector [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
```

### G2-21: String length and substring

**form**: `(count "tortoise")`  •  **expected**: `8`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened by the hilltop.

Mossback the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," he said, pointing to
the length of "tortoise". "You hand the form `(count "tortoise")` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, yawning at the soft moss
from a recent sprint, agreed to try.

Write a Clojure expression that computes the length of the string "tortoise".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G2-22: Compose pure arithmetic (multi-step calculation)

**form**: `(- (* 5 4) 7)`  •  **expected**: `13`

```
It was well known among the animals that the Hare boasted of his speed at every chance. It happened across the woods.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today at the edge of the woods, the
next entry was the form (- (* 5 4) 7). Pip the hare peered over
her shoulder at the form `(- (* 5 4) 7)` and asked what
it would come out to.

What Clojure form computes 5 mph for 4 hours, minus a 7-mile head start? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(- (* 5 4) 7)"}}]}
```

## Grade 3

### G3-01: def — top-level binding

**form**: `(do (def x 42) x)`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the binding (def x 42) followed by x comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(do (def x 42) x)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value bound to x after (def x 42).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
```

### G3-02: def — redefinition

**form**: `(do (def x 1) (def x 99) x)`  •  **expected**: `99`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the redefined x on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(do (def x 1) (def x 99) x)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value of x after redefinition.

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 1) (def x 99) x)"}}]}
```

### G3-03: let — local binding

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(let [x 3] (+ x 1))`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form (let [x 3] (+ x 1)) was to put
it in the REPL.

What Clojure form computes the result of (let [x 3] (+ x 1))? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
```

### G3-04: let — multi-binding

**form**: `(let [a 1 b 2] (+ a b))`  •  **expected**: `3`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"You can call it whatever you like," Shelly said across the hilltop, "but the
form is what matters." She drew the binding for
Bramble the hare: the form `(let [a 1 b 2] (+ a b))` captured the form with two bindings, and
the REPL would do the rest.

Question: write a Clojure expression for the result of (let [a 1 b 2] (+ a b)).

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 1 b 2] (+ a b))"}}]}
```

### G3-05: let — shadowing outer def

**form**: `(do (def x 10) (let [x 99] x))`  •  **expected**: `99`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(do (def x 10) (let [x 99] x))`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
an inner let shadowing the outer def to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the inner-let value of x.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 10) (let [x 99] x))"}}]}
```

### G3-06: let — binding can reference prior

**form**: `(let [a 5 b (* a 2)] b)`  •  **expected**: `10`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"You can call it whatever you like," Shelly said near the woods, "but the
form is what matters." She drew the binding for
Hopper the hare: the form `(let [a 5 b (* a 2)] b)` captured a let where b uses a, and
the REPL would do the rest.

Question: write a Clojure expression for the value of b when a=5 and b is (* a 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 5 b (* a 2)] b)"}}]}
```

### G3-07: fn — anonymous function

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `((fn [x] (+ x 1)) 4)`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
an anonymous function applied to 4 to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the result of applying (fn [x] (+ x 1)) to 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
```

### G3-08: fn — multi-arg

**form**: `((fn [a b c] (+ a b c)) 1 2 3)`  •  **expected**: `6`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `((fn [a b c] (+ a b c)) 1 2 3)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
a three-arg anonymous function.

What Clojure form computes the sum of a, b, c? Submit it via `eval`.

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [a b c] (+ a b c)) 1 2 3)"}}]}
```

### G3-09: defn — shorthand

**form**: `(do (defn dbl [x] (* x 2)) (dbl 5))`  •  **expected**: `10`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(do (defn dbl [x] (* x 2)) (dbl 5))` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
a defn that doubles its argument.

Question: write a Clojure expression for the doubled value (dbl 5).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn dbl [x] (* x 2)) (dbl 5))"}}]}
```

### G3-10: anonymous shorthand #()

**form**: `(#(+ % 1) 5)`  •  **expected**: `6`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the shorthand #(+ % 1) applied to 5 on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(#(+ % 1) 5)`
in the REPL and read off whatever it returned.

What Clojure form computes the result of (#(+ % 1) 5)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(#(+ % 1) 5)"}}]}
```

### G3-11: Substitution rule

**form**: `(let [a 7] (+ a a))`  •  **expected**: `14`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was the let where a is referenced twice. Hopper the hare peered over
her shoulder at the form `(let [a 7] (+ a a))` and asked what
it would come out to.

Write a Clojure expression that computes the result of (+ a a) when a=7.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a 7] (+ a a))"}}]}
```

### G3-12: Scope vs namespace

**form**: `(do (def g 5) (let [g 99] (+ g 1)))`  •  **expected**: `100`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(do (def g 5) (let [g 99] (+ g 1)))` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
an inner let masking the outer def g.

Question: write a Clojure expression for the value computed inside the inner scope.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def g 5) (let [g 99] (+ g 1)))"}}]}
```

### G3-13: fn body returns last form

**form**: `((fn [x] x x x 99) 1)`  •  **expected**: `99`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `((fn [x] x x x 99) 1)` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
a fn whose body has multiple forms; only the last is returned.

Write a form whose evaluation gives the value of a fn body that ends with 99.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] x x x 99) 1)"}}]}
```

### G3-14: do form

**form**: `(do 1 2 3)`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the do form (do 1 2 3) — returns the last form: the form was `(do 1 2 3)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (do 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do 1 2 3)"}}]}
```

### G3-15: Side-effects in body

**form**: `(do (println "hi") 42)`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise kept a small ledger near the hilltop where every meaningful
quantity got its own name. She pointed to today's
entry: the form (do (println "hi") 42). The form `(do (println "hi") 42)` would settle it once
Pip the hare agreed to look at the binding.

Write a form whose evaluation gives the return value of the do (the println side-effects, but the do returns 42).

---

I name the values first and then combine them.

{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

### G3-16: Name collision: namespace vs let

**form**: `(let [+ 99] +)`  •  **expected**: `99`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise kept a small ledger at the edge of the road where every meaningful
quantity got its own name. He pointed to today's
entry: a let that shadows the + function. The form `(let [+ 99] +)` would settle it once
Bramble the hare agreed to look at the binding.

What Clojure form computes the value bound to the (locally shadowed) +? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [+ 99] +)"}}]}
```

### G3-17: Naming conventions (kebab-case)

**form**: `(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))`  •  **expected**: `3`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

"There is no need to evaluate that," Hopper the hare said with a smug grin.
"Anyone can see what a let with kebab-case names comes to." Slowpoke the tortoise, who
by the meadow had grown used to such claims, asked him to actually
write the form `(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the difference of the two speeds.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))"}}]}
```

### G3-18: When to name vs inline

**form**: `(let [n 5] (* n n n))`  •  **expected**: `125`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"You can call it whatever you like," Slowpoke said by the road, "but the
form is what matters." He drew the binding for
Bramble the hare: the form `(let [n 5] (* n n n))` captured naming n once and using it three times, and
the REPL would do the rest.

What Clojure form computes n cubed where n=5? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [n 5] (* n n n))"}}]}
```

## Grade 4

### G4-01: Vector literal

**form**: `[1 2 3]`  •  **expected**: `[1, 2, 3]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the vector [1 2 3] comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `[1 2 3]` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"[1 2 3]"}}]}
```

### G4-02: nth — vector access

**form**: `(nth [10 20 30] 0)`  •  **expected**: `10`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the form (nth [10 20 30] 0) on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(nth [10 20 30] 0)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value at index 0.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(nth [10 20 30] 0)"}}]}
```

### G4-03: conj — append to vector

**form**: `(conj [1 2] 3)`  •  **expected**: `[1, 2, 3]`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(conj [1 2] 3)`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form (conj [1 2] 3) was to put
it in the REPL.

What Clojure form computes [1 2] with 3 conjed? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(conj [1 2] 3)"}}]}
```

### G4-04: List literal

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Bramble the hare, with a smug grin, declared the collection plain. Shelly the tortoise
wrote `'(1 2 3)` on a slate across the hilltop, calmly. "It's not about plain
or fancy," she said. "It's about whether the runtime
agrees with what we think we're describing."

Question: write a Clojure expression for the list of three numbers.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G4-05: cons — prepend to seq

**form**: `(cons 0 '(1 2 3))`  •  **expected**: `[0, 1, 2, 3]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(cons 0 '(1 2 3))`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the form (cons 0 '(1 2 3)) to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the seq with 0 cons'd at the front.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(cons 0 '(1 2 3))"}}]}
```

### G4-06: Map literal

**form**: `{:hare 1 :tortoise 2}`  •  **expected**: `{':hare': 1, ':tortoise': 2}`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Hopper the hare, swaggering through the underbrush, declared the collection plain. Shelly the tortoise
wrote `{:hare 1 :tortoise 2}` on a slate near the woods, calmly. "It's not about plain
or fancy," she said. "It's about whether the runtime
agrees with what we think we're describing."

Question: write a Clojure expression for the map with two entries.

---

{"tool_calls":[{"name":"eval","args":{"form":"{:hare 1 :tortoise 2}"}}]}
```

### G4-07: get — map lookup

**form**: `(get {:a 1 :b 2} :a)`  •  **expected**: `1`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(get {:a 1 :b 2} :a)`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the form (get {:a 1 :b 2} :a) to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value at :a.

---

{"tool_calls":[{"name":"eval","args":{"form":"(get {:a 1 :b 2} :a)"}}]}
```

### G4-08: assoc — map update

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(assoc {:a 1} :b 2)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the form (assoc {:a 1} :b 2).

What Clojure form computes the map after assoc'ing :b 2? Submit it via `eval`.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
```

### G4-09: dissoc — map remove key

**form**: `(dissoc {:a 1 :b 2} :a)`  •  **expected**: `{':b': 2}`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(dissoc {:a 1 :b 2} :a)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the form (dissoc {:a 1 :b 2} :a).

Question: write a Clojure expression for the map without :a.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(dissoc {:a 1 :b 2} :a)"}}]}
```

### G4-10: keys and vals

**form**: `(count (keys {:a 1 :b 2 :c 3}))`  •  **expected**: `3`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the form (count (keys ...)) on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(count (keys {:a 1 :b 2 :c 3}))`
in the REPL and read off whatever it returned.

What Clojure form computes the number of keys in the map? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (keys {:a 1 :b 2 :c 3}))"}}]}
```

### G4-11: Set literal

**form**: `(count #{1 2 3})`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was the count of #{1 2 3}. Hopper the hare peered over
her shoulder at the form `(count #{1 2 3})` and asked what
it would come out to.

Write a Clojure expression that computes the size of the set.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count #{1 2 3})"}}]}
```

### G4-12: Set membership

**form**: `(contains? #{1 2 3} 2)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(contains? #{1 2 3} 2)` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (contains? #{1 2 3} 2).

Question: write a Clojure expression for whether 2 is in the set.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{1 2 3} 2)"}}]}
```

### G4-13: count — universal

**form**: `(count [1 2 3 4 5])`  •  **expected**: `5`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(count [1 2 3 4 5])` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the count of a 5-element vector.

Write a form whose evaluation gives the count.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3 4 5])"}}]}
```

### G4-14: empty?

**form**: `(empty? [])`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the form (empty? []): the form was `(empty? [])`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes whether [] is empty.

---

{"tool_calls":[{"name":"eval","args":{"form":"(empty? [])"}}]}
```

### G4-15: first, rest, last

**form**: `(first [10 20 30])`  •  **expected**: `10`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise had been laying out a small collection near the hilltop —
pebbles, milestones, paw-prints, whatever the day produced. Shelly
wrote `(first [10 20 30])` on a slate and asked Pip the hare to write the
form into the REPL so they could confirm it together.

Write a form whose evaluation gives the first element.

---

I use the appropriate access function on the collection.

{"tool_calls":[{"name":"eval","args":{"form":"(first [10 20 30])"}}]}
```

### G4-16: into and conj on collections

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise had been laying out a small collection at the edge of the road —
pebbles, milestones, paw-prints, whatever the day produced. Mossback
wrote `(into [] '(1 2 3))` on a slate and asked Bramble the hare to write the
form into the REPL so they could confirm it together.

What Clojure form computes the vector built from a list? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
```

### G4-17: Immutability — assoc returns new

**form**: `(let [m {:a 1}] (assoc m :a 99) m)`  •  **expected**: `{':a': 1}`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

"There is no need to evaluate that," Hopper the hare said with a smug grin.
"Anyone can see what the form showing assoc returns a new map comes to." Slowpoke the tortoise, who
by the meadow had grown used to such claims, asked him to actually
write the form `(let [m {:a 1}] (assoc m :a 99) m)` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the original map after assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :a 99) m)"}}]}
```

### G4-18: Equality of vectors and lists

**form**: `(= [1 2 3] '(1 2 3))`  •  **expected**: `True`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

Bramble the hare, swaggering through the underbrush, declared the collection plain. Slowpoke the tortoise
wrote `(= [1 2 3] '(1 2 3))` on a slate by the road, calmly. "It's not about plain
or fancy," he said. "It's about whether the runtime
agrees with what we think we're describing."

What Clojure form computes whether vector and list with same elements are equal? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(= [1 2 3] '(1 2 3))"}}]}
```

### G4-19: range and seq

**form**: `(count (range 5))`  •  **expected**: `5`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise had been laying out a small collection in the meadow —
pebbles, milestones, paw-prints, whatever the day produced. Slowpoke
wrote `(count (range 5))` on a slate and asked Pip the hare to write the
form into the REPL so they could confirm it together.

Question: write a Clojure expression for the count of range 0..4.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(count (range 5))"}}]}
```

### G4-20: Collection vs sequence

**form**: `(count (seq [1 2 3]))`  •  **expected**: `3`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Shelly the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," she said, pointing to
the form (count (seq [1 2 3])). "You hand the form `(count (seq [1 2 3]))` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, her legs heavy from sprinting
from a recent sprint, agreed to try.

Write a Clojure expression that computes the count of seq over a vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (seq [1 2 3]))"}}]}
```

## Grade 5

### G5-01: if

**form**: `(if true :a :b)`  •  **expected**: `':a'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the form (if true :a :b) comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(if true :a :b)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
```

### G5-02: if as expression

**form**: `(+ 1 (if true 10 20))`  •  **expected**: `11`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the form (+ 1 (if true 10 20)) on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(+ 1 (if true 10 20))`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result of adding 1 to the if expression.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (if true 10 20))"}}]}
```

### G5-03: when

**form**: `(when true :yes)`  •  **expected**: `':yes'`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(when true :yes)`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form (when true :yes) was to put
it in the REPL.

What Clojure form computes the value of (when true :yes)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true :yes)"}}]}
```

### G5-04: cond

**form**: `(cond (= 1 2) :a (= 1 1) :b :else :c)`  •  **expected**: `':b'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"Same trick, repeated cleverly," Shelly said across the hilltop, sketching the
form `(cond (= 1 2) :a (= 1 1) :b :else :c)` into the dust. Bramble, with a smug grin, claimed
to know exactly what the cond form would produce — but Shelly
insisted, again, that the REPL was the only honest judge.

Question: write a Clojure expression for which clause of the cond fires.

---

{"tool_calls":[{"name":"eval","args":{"form":"(cond (= 1 2) :a (= 1 1) :b :else :c)"}}]}
```

### G5-05: cond — :else

**form**: `(cond false :a false :b :else :c)`  •  **expected**: `':c'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(cond false :a false :b :else :c)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the cond falling through to :else to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the :else value.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(cond false :a false :b :else :c)"}}]}
```

### G5-06: case

**form**: `(case 2 1 :one 2 :two 3 :three :default)`  •  **expected**: `':two'`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Same trick, repeated cleverly," Shelly said near the woods, sketching the
form `(case 2 1 :one 2 :two 3 :three :default)` into the dust. Hopper, swaggering through the underbrush, claimed
to know exactly what the case form would produce — but Shelly
insisted, again, that the REPL was the only honest judge.

Question: write a Clojure expression for the matched branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(case 2 1 :one 2 :two 3 :three :default)"}}]}
```

### G5-07: and / or as control flow

**form**: `(and 1 2 3)`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(and 1 2 3)`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
the form (and 1 2 3) returns last truthy to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the last truthy value.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and 1 2 3)"}}]}
```

### G5-08: not

**form**: `(not (> 1 2))`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(not (> 1 2))` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
the form (not (> 1 2)).

What Clojure form computes the negated comparison? Submit it via `eval`.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"(not (> 1 2))"}}]}
```

### G5-09: fn as value

**form**: `((fn [f x] (f (f x))) inc 5)`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `((fn [f x] (f (f x))) inc 5)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
applying f twice to x where f is inc.

Question: write a Clojure expression for the result of inc applied twice.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [f x] (f (f x))) inc 5)"}}]}
```

### G5-10: map

**form**: `(map inc [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the form (map inc [1 2 3]) on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(map inc [1 2 3])`
in the REPL and read off whatever it returned.

What Clojure form computes [1 2 3] each incremented? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(map inc [1 2 3])"}}]}
```

### G5-11: filter

**form**: `(filter even? [1 2 3 4])`  •  **expected**: `[2, 4]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was the form (filter even? [1 2 3 4]). Hopper the hare peered over
her shoulder at the form `(filter even? [1 2 3 4])` and asked what
it would come out to.

Write a Clojure expression that computes the even numbers from [1 2 3 4].

---

{"tool_calls":[{"name":"eval","args":{"form":"(filter even? [1 2 3 4])"}}]}
```

### G5-12: reduce

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(reduce + [1 2 3 4])` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the form (reduce + [1 2 3 4]).

Question: write a Clojure expression for the sum.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
```

### G5-13: reduce with init

**form**: `(reduce + 100 [1 2 3])`  •  **expected**: `106`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(reduce + 100 [1 2 3])` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the form (reduce + 100 [1 2 3]).

Write a form whose evaluation gives 100 + sum of [1 2 3].

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + 100 [1 2 3])"}}]}
```

### G5-14: apply

**form**: `(apply + [1 2 3 4])`  •  **expected**: `10`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud the form (apply + [1 2 3 4]): the form was `(apply + [1 2 3 4])`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes + applied to the elements of the vector.

---

{"tool_calls":[{"name":"eval","args":{"form":"(apply + [1 2 3 4])"}}]}
```

### G5-15: comp

**form**: `((comp inc inc) 5)`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise demonstrated near the hilltop how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `((comp inc inc) 5)` captured the form ((comp inc inc) 5), and Pip the hare agreed
to write it for the REPL.

Write a form whose evaluation gives inc twice applied to 5.

---

I write the higher-order form so the REPL can compute.

{"tool_calls":[{"name":"eval","args":{"form":"((comp inc inc) 5)"}}]}
```

### G5-16: partial

**form**: `((partial + 10) 5)`  •  **expected**: `15`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise demonstrated at the edge of the road how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `((partial + 10) 5)` captured the form ((partial + 10) 5), and Bramble the hare agreed
to write it for the REPL.

What Clojure form computes 10 + 5? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"((partial + 10) 5)"}}]}
```

### G5-17: juxt

**form**: `((juxt inc dec) 5)`  •  **expected**: `[6, 4]`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

"There is no need to evaluate that," Hopper the hare said with a smug grin.
"Anyone can see what the form ((juxt inc dec) 5) comes to." Slowpoke the tortoise, who
by the meadow had grown used to such claims, asked him to actually
write the form `((juxt inc dec) 5)` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes inc and dec of 5 in parallel.

---

{"tool_calls":[{"name":"eval","args":{"form":"((juxt inc dec) 5)"}}]}
```

### G5-18: some

**form**: `(some even? [1 3 5 8 7])`  •  **expected**: `True`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"Same trick, repeated cleverly," Slowpoke said by the road, sketching the
form `(some even? [1 3 5 8 7])` into the dust. Bramble, swaggering through the underbrush, claimed
to know exactly what the form (some even? [...]) would produce — but Slowpoke
insisted, again, that the REPL was the only honest judge.

What Clojure form computes whether any element is even? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(some even? [1 3 5 8 7])"}}]}
```

### G5-19: every?

**form**: `(every? pos? [1 2 3])`  •  **expected**: `True`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Slowpoke the tortoise demonstrated in the meadow how the same operation, applied
to many things at once, was the heart of every long calculation. The
form `(every? pos? [1 2 3])` captured the form (every? pos? [1 2 3]), and Pip the hare agreed
to write it for the REPL.

Question: write a Clojure expression for whether all are positive.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(every? pos? [1 2 3])"}}]}
```

### G5-20: take and drop

**form**: `(take 3 [10 20 30 40 50])`  •  **expected**: `[10, 20, 30]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Shelly the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," she said, pointing to
the form (take 3 ...). "You hand the form `(take 3 [10 20 30 40 50])` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, her legs heavy from sprinting
from a recent sprint, agreed to try.

Write a Clojure expression that computes the first three elements.

---

{"tool_calls":[{"name":"eval","args":{"form":"(take 3 [10 20 30 40 50])"}}]}
```

### G5-21: distinct and sort

**form**: `(distinct [1 1 2 3 3 4])`  •  **expected**: `[1, 2, 3, 4]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. It happened by the hilltop.

Mossback the tortoise had been trying to teach Hopper the hare how the REPL
works. "Look here," he said, pointing to
the form (distinct [1 1 2 3 3 4]). "You hand the form `(distinct [1 1 2 3 3 4])` to the runtime, and
the runtime hands you back what it evaluates to." Hopper, yawning at the soft moss
from a recent sprint, agreed to try.

Write a Clojure expression that computes the deduplicated seq.

---

{"tool_calls":[{"name":"eval","args":{"form":"(distinct [1 1 2 3 3 4])"}}]}
```

### G5-22: recur — first taste

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

```
It was well known among the animals that the Hare boasted of his speed at every chance. It happened across the woods.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today at the edge of the woods, the
next entry was a loop computing factorial of 5 via recur. Pip the hare peered over
her shoulder at the form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))` and asked what
it would come out to.

What Clojure form computes 5! computed via loop/recur? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
```

## Grade 6

### G6-01: Namespace as file

**form**: `(name 'foo.bar)`  •  **expected**: `'foo.bar'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what the symbol foo.bar standing in for a namespace name comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(name 'foo.bar)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the string form of the namespace symbol foo.bar.

---

{"tool_calls":[{"name":"eval","args":{"form":"(name 'foo.bar)"}}]}
```

### G6-02: ns form

**form**: `(name 'race.tortoise)`  •  **expected**: `'race.tortoise'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the namespace name 'race.tortoise as a string on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(name 'race.tortoise)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the string "race.tortoise".

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(name 'race.tortoise)"}}]}
```

### G6-03: require

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(clojure.string/upper-case "hare")`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of the form using clojure.string/upper-case on "hare" was to put
it in the REPL.

What Clojure form computes the upper-cased string "HARE"? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
```

### G6-04: refer and use

**form**: `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))`  •  **expected**: `True`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

The two of them lived in cottages on opposite sides across the hilltop —
Shelly the tortoise on one side, Bramble the hare on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Shelly read aloud whether two calls to the same fully-qualified function agree and asked, saying very little, what
the form `(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))` would return when the REPL reached across the
shared path.

Question: write a Clojure expression for the value of (= (clojure.string/upper-case "x") (clojure.string/upper-case "x")).

---

I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"}}]}
```

### G6-05: Fully qualified names

**form**: `(clojure.string/upper-case "tortoise")`  •  **expected**: `'TORTOISE'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(clojure.string/upper-case "tortoise")`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
clojure.string/upper-case applied to "tortoise" to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the upper-cased string "TORTOISE".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"tortoise\")"}}]}
```

### G6-06: Private defs

**form**: `(:private (meta '^:private x))`  •  **expected**: `True`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

The two of them lived in cottages on opposite sides near the woods —
Shelly the tortoise on one side, Hopper the hare on the other. Each kept
their own copybook of forms. When the time came to compare notes,
Shelly read aloud the :private flag on metadata of '^:private x and asked, her eyes always on the path, what
the form `(:private (meta '^:private x))` would return when the REPL reached across the
shared path.

Question: write a Clojure expression for whether the :private metadata is true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:private (meta '^:private x))"}}]}
```

### G6-07: Public vs private API

**form**: `(boolean (:private (meta '^:private hidden)))`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(boolean (:private (meta '^:private hidden)))`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
whether the symbol 'hidden carries the :private flag to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the boolean of (:private (meta '^:private hidden)).

---

{"tool_calls":[{"name":"eval","args":{"form":"(boolean (:private (meta '^:private hidden)))"}}]}
```

### G6-08: Circular dependencies

**form**: `(clojure.string/upper-case "a")`  •  **expected**: `'A'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(clojure.string/upper-case "a")` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
a single-direction call from one namespace to clojure.string.

What Clojure form computes the upper-cased string "A"? Submit it via `eval`.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"a\")"}}]}
```

### G6-09: Loading order

**form**: `(do (def step1 1) (def step2 (+ step1 1)) step2)`  •  **expected**: `2`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(do (def step1 1) (def step2 (+ step1 1)) step2)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
two defs evaluated in order, the second using the first.

Question: write a Clojure expression for the final value step2 after sequential loading.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def step1 1) (def step2 (+ step1 1)) step2)"}}]}
```

### G6-10: Leiningen and deps.edn

**form**: `(:deps {:deps {:a 1 :b 2}})`  •  **expected**: `{':a': 1, ':b': 2}`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the :deps key from a small deps-map literal on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(:deps {:deps {:a 1 :b 2}})`
in the REPL and read off whatever it returned.

What Clojure form computes the value at :deps in {:deps {:a 1 :b 2}}? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
```

### G6-11: Classpath

**form**: `(clojure.string/split "src:test" #":")`  •  **expected**: `['src', 'test']`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was splitting a colon-separated classpath-like string. Hopper the hare peered over
her shoulder at the form `(clojure.string/split "src:test" #":")` and asked what
it would come out to.

Write a Clojure expression that computes the vector ["src" "test"].

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/split \"src:test\" #\":\")"}}]}
```

### G6-12: Multiple files in one project

**form**: `(count ['race.tortoise 'race.hare 'race.shared])`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(count ['race.tortoise 'race.hare 'race.shared])` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the number of namespaces in a small project.

Question: write a Clojure expression for the count of namespace symbols in the vector.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count ['race.tortoise 'race.hare 'race.shared])"}}]}
```

### G6-13: Aliasing conventions

**form**: `(let [s clojure.string/upper-case] (s "hare"))`  •  **expected**: `'HARE'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(let [s clojure.string/upper-case] (s "hare"))` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
binding the function clojure.string/upper-case to a local s.

Write a form whose evaluation gives the value (s "hare") where s is upper-case.

---

I keep the namespaces straight and let the REPL resolve the name.

{"tool_calls":[{"name":"eval","args":{"form":"(let [s clojure.string/upper-case] (s \"hare\"))"}}]}
```

### G6-14: Import for host classes

**form**: `(symbol? 'java.util.Date)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud whether 'java.util.Date is a symbol: the form was `(symbol? 'java.util.Date)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of (symbol? 'java.util.Date).

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
```

### G6-15: Namespace meta

**form**: `(:doc (meta '^{:doc "steady wins"} race))`  •  **expected**: `'steady wins'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise kept a small workbench near the hilltop, where every form had
its own labeled drawer. Pip the hare preferred to scribble each
expression in a single notebook. To settle a question that morning,
Shelly pointed to the :doc metadata attached to the symbol 'race and asked Pip to evaluate the
form `(:doc (meta '^{:doc "steady wins"} race))` so they could see what name belonged with what
value.

Write a form whose evaluation gives the docstring "steady wins" from the metadata.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"steady wins\"} race))"}}]}
```

### G6-16: Cleaning up requires

**form**: `(contains? #{'clojure.string} 'clojure.string)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise kept a small workbench at the edge of the road, where every form had
its own labeled drawer. Bramble the hare preferred to scribble each
expression in a single notebook. To settle a question that morning,
Mossback pointed to whether the require list still contains 'clojure.string and asked Bramble to evaluate the
form `(contains? #{'clojure.string} 'clojure.string)` so they could see what name belonged with what
value.

What Clojure form computes the value of (contains? #{'clojure.string} 'clojure.string)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(contains? #{'clojure.string} 'clojure.string)"}}]}
```

## Grade 7

### G7-01: throw

**form**: `(try (throw (Exception. "bad")) (catch Exception e :thrown))`  •  **expected**: `':thrown'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A wooden sign nailed to a tree near the hilltop carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(try (throw (Exception. "bad")) (catch Exception e :thrown))`. Bramble
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of throwing an exception that is then caught was to put
it in the REPL.

Write a form whose evaluation gives the keyword :thrown returned after the throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"bad\")) (catch Exception e :thrown))"}}]}
```

### G7-02: try / catch

**form**: `(try (/ 1 0) (catch Exception e :caught))`  •  **expected**: `':caught'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written a division by zero wrapped in try/catch on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(try (/ 1 0) (catch Exception e :caught))`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
```

### G7-03: try / finally

**form**: `(try 7 (finally :cleanup))`  •  **expected**: `7`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

Slowpoke the tortoise had learned not to trust a form on first reading.
at the edge of the garden, he typed `(try 7 (finally :cleanup))` carefully, ready to
catch whatever the REPL might throw back. Hopper the hare, swaggering through the underbrush,
laughed and said no error would ever come — but Slowpoke insisted
on letting the runtime decide, then reading a try whose finally clause runs but doesn't change the value from
whatever it returned.

What Clojure form computes the value 7 from the body (finally is for side effects)? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(try 7 (finally :cleanup))"}}]}
```

### G7-04: ex-info

**form**: `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))`  •  **expected**: `{':a': 1}`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Beyond the REPL the world had files, streams, and surprises.
Shelly the tortoise opened a small notebook across the hilltop, copying down
throwing an ex-info with attached data, then reading it back. Bramble, weary from the morning's effort, watched as she
wrote the form `(try (throw (ex-info "bad" {:a 1})) (catch Exception e (ex-data e)))` so the runtime could carry the work the
rest of the way.

Question: write a Clojure expression for the data map {:a 1} pulled from the caught ex-info.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))"}}]}
```

### G7-05: nil punning

**form**: `(some? nil)`  •  **expected**: `False`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(some? nil)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the predicate (some? nil) to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for whether nil counts as some? (it does not).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(some? nil)"}}]}
```

### G7-06: pre and post conditions

**form**: `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`  •  **expected**: `10`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A small slip of paper near the woods carried the form `((fn [x] {:pre [(pos? x)]} (* x 2)) 5)`. Hopper
glanced at it and dashed on, certain there was no trouble.
Shelly the tortoise sat down, her eyes always on the path, and worked through
a fn with a :pre condition that is satisfied step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again.

Question: write a Clojure expression for the value returned when the precondition holds and 5 is doubled.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] {:pre [(pos? x)]} (* x 2)) 5)"}}]}
```

### G7-07: assert

**form**: `(do (assert (= 1 1)) :ok)`  •  **expected**: `':ok'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Mossback the tortoise had been keeping a small leather notebook of every
form he had successfully evaluated. Today across the forest, the
next entry was an assert that passes, followed by a return value. Whisker the hare peered over
his shoulder at the form `(do (assert (= 1 1)) :ok)` and asked what
it would come out to.

Write a form whose evaluation gives the keyword :ok returned after the assert succeeds.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (assert (= 1 1)) :ok)"}}]}
```

### G7-08: prn and pprint

**form**: `(with-out-str (prn 42))`  •  **expected**: `'42\n'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(with-out-str (prn 42))` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
capturing the output of (prn 42).

What Clojure form computes the string "42\n" produced by prn? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (prn 42))"}}]}
```

### G7-09: tap>

**form**: `(tap> :hello)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(tap> :hello)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
tapping a value into the tap pool.

Question: write a Clojure expression for the boolean true returned by tap>.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(tap> :hello)"}}]}
```

### G7-10: doc and source

**form**: `(:doc (meta '^{:doc "adds two"} plus))`  •  **expected**: `'adds two'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the :doc metadata on a symbol — what doc would print on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(:doc (meta '^{:doc "adds two"} plus))`
in the REPL and read off whatever it returned.

What Clojure form computes the string "adds two" from the metadata? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"adds two\"} plus))"}}]}
```

### G7-11: Reading stack traces

**form**: `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))`  •  **expected**: `'oops'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

"There is no need to evaluate that," Hopper the hare said boasting at every turn.
"Anyone can see what extracting the message from a caught exception comes to." Shelly the tortoise, who
in the meadow had grown used to such claims, asked him to actually
write the form `(try (throw (Exception. "oops")) (catch Exception e (.getMessage e)))` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the string "oops" from the caught Exception.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))"}}]}
```

### G7-12: slurp and spit

**form**: `(count "hare\ntortoise\n")`  •  **expected**: `14`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(count "hare\ntortoise\n")` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
the length of a multi-line string (as if read by slurp).

Question: write a Clojure expression for the count of characters in "hare\ntortoise\n".

---

I let the REPL read the file or stream for me.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"hare\\ntortoise\\n\")"}}]}
```

### G7-13: line-seq

**form**: `(count (clojure.string/split-lines "a\nb\nc"))`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(count (clojure.string/split-lines "a\nb\nc"))` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the number of lines in a small text.

Write a form whose evaluation gives the count of lines in "a\nb\nc".

---

{"tool_calls":[{"name":"eval","args":{"form":"(count (clojure.string/split-lines \"a\\nb\\nc\"))"}}]}
```

### G7-14: with-open

**form**: `(with-out-str (println "hare"))`  •  **expected**: `'hare\n'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud a resource-scoped capture of println output: the form was `(with-out-str (println "hare"))`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the string "hare\n" from the scoped block.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (println \"hare\"))"}}]}
```

### G7-15: *in* and *out*

**form**: `(with-out-str (print "x"))`  •  **expected**: `'x'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small slip of paper near the hilltop carried the form `(with-out-str (print "x"))`. Pip
glanced at it and dashed on, certain there was no trouble.
Shelly the tortoise sat down, without complaint, and worked through
redirecting *out* via with-out-str and printing step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again.

Write a form whose evaluation gives the string "x" captured from *out*.

---

{"tool_calls":[{"name":"eval","args":{"form":"(with-out-str (print \"x\"))"}}]}
```

### G7-16: edn read

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

A small slip of paper at the edge of the road carried the form `(clojure.edn/read-string "42")`. Bramble
glanced at it and dashed on, certain there was no trouble.
Mossback the tortoise sat down, stepping deliberately, and worked through
reading an edn integer from a string step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again.

What Clojure form computes the integer 42 read from "42"? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G7-17: JSON roundtrip

**form**: `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`  •  **expected**: `{':a': 1, ':b': 2}`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

A wooden sign nailed to a tree by the meadow carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(clojure.edn/read-string (pr-str {:a 1 :b 2}))`. Hopper
laughed, with a smug grin, and declared it too easy. Slowpoke said
patiently that the only way to be sure of writing then reading back a small map (edn-shaped roundtrip) was to put
it in the REPL.

Write a Clojure expression that computes the map {:a 1 :b 2} after the roundtrip.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string (pr-str {:a 1 :b 2}))"}}]}
```

### G7-18: Shell command

**form**: `(:cmd {:cmd "ls" :args ["-l"]})`  •  **expected**: `'ls'`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

Beyond the REPL the world had files, streams, and surprises.
Slowpoke the tortoise opened a small notebook by the road, copying down
the :cmd portion of a shell-call descriptor map. Bramble, weary from the morning's effort, watched as he
wrote the form `(:cmd {:cmd "ls" :args ["-l"]})` so the runtime could carry the work the
rest of the way.

What Clojure form computes the string "ls"? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(:cmd {:cmd \"ls\" :args [\"-l\"]})"}}]}
```

## Grade 8

### G8-01: Why polymorphism

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what a function speak that returns different strings for :hare vs :tortoise comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the form that defines speak via cond.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
```

### G8-02: deftype introduction

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written a deftype Pebble with a color field, then read color of an instance on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the color field of a Pebble instance.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
```

### G8-03: defrecord introduction

**form**: `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))`  •  **expected**: `':swift'`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (defrecord Runner [name pace]) (:pace (->Runner "hare" :swift)))`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of a defrecord Runner with name and pace fields, get :pace was to put
it in the REPL.

What Clojure form computes the :pace value of the Runner record? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defrecord Runner [name pace]) (:pace (->Runner \"hare\" :swift)))"}}]}
```

### G8-04: Protocol definition

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A scrap of parchment, pinned to a tree across the hilltop, set out a rule that all
creatures of the woodland would have to abide by. Bramble, with a smug grin,
read it aloud: it was a defprotocol Pace with a single method speed. Shelly the tortoise said only the
REPL could confirm what `(do (defprotocol Pace (speed [this])) (some? Pace))` actually decided.

Question: write a Clojure expression for whether the Pace protocol was defined (a non-nil truthy value).

---

I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
```

### G8-05: Protocol extension

**form**: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))`  •  **expected**: `'swift'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] "swift")) (speed "hare"))`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
a Pace protocol extended to String, then call speed on a string to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for what speed returns when applied to "hare".

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace java.lang.String (speed [_] \"swift\")) (speed \"hare\"))"}}]}
```

### G8-06: Protocol method dispatch

**form**: `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))`  •  **expected**: `':long-pace'`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A scrap of parchment, pinned to a tree near the woods, set out a rule that all
creatures of the woodland would have to abide by. Hopper, swaggering through the underbrush,
read it aloud: it was Pace dispatched on the class of its argument; called with 42. Shelly the tortoise said only the
REPL could confirm what `(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))` actually decided.

Question: write a Clojure expression for the keyword speed returns for the integer 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-protocol Pace   java.lang.String (speed [_] :string-pace)   java.lang.Long   (speed [_] :long-pace)) (speed 42))"}}]}
```

### G8-07: Record implementing protocol

**form**: `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`  •  **expected**: `':swift'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare "Pip")))`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
a defrecord Hare that implements Pace with speed -> :swift to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the keyword speed returns for a Hare record.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (defrecord Hare [name] Pace (speed [_] :swift)) (speed (->Hare \"Pip\")))"}}]}
```

### G8-08: Multimethod defmulti

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
a defmulti pace that dispatches on :species, called with :hare.

What Clojure form computes what pace returns for {:species :hare}? Submit it via `eval`.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
```

### G8-09: Multimethod defmethod

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))`  •  **expected**: `':steady'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
two defmethod entries on pace, called with :tortoise.

Question: write a Clojure expression for what pace returns for {:species :tortoise}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (defmethod pace :tortoise [_] :steady) (pace {:species :tortoise}))"}}]}
```

### G8-10: Multimethod vs protocol

**form**: `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))`  •  **expected**: `'swift'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written a defmulti dispatching on identity, with one method for :hare on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(do (defmulti show identity) (defmethod show :hare [_] "swift") (show :hare))`
in the REPL and read off whatever it returned.

What Clojure form computes the string show returns for :hare? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti show identity) (defmethod show :hare [_] \"swift\") (show :hare))"}}]}
```

### G8-11: Protocol vs Java interface

**form**: `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))`  •  **expected**: `':ran'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was an IPace protocol (Clojure analogue of a Java interface) extended to String. Hopper the hare peered over
her shoulder at the form `(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run "hare"))` and asked what
it would come out to.

Write a Clojure expression that computes the keyword run returns for "hare" via the protocol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol IPace (run [this])) (extend-protocol IPace java.lang.String (run [_] :ran)) (run \"hare\"))"}}]}
```

### G8-12: extend-type on built-in types

**form**: `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))`  •  **expected**: `':number-pace'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
extend-type used to attach Pace to Long, called with 5.

Question: write a Clojure expression for the keyword speed returns for 5.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (extend-type java.lang.Long Pace (speed [_] :number-pace)) (speed 5))"}}]}
```

### G8-13: this-style vs fn-style

**form**: `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))`  •  **expected**: `'Pip'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare "Pip")))` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
a protocol method using this to read a field.

Write a form whose evaluation gives the name returned by name-of for a Hare record.

---

I let the polymorphic dispatch pick the right implementation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Named (name-of [this])) (defrecord Hare [n] Named (name-of [this] (:n this))) (name-of (->Hare \"Pip\")))"}}]}
```

### G8-14: Protocols don't inherit

**form**: `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`  •  **expected**: `[':a-impl', ':b-impl']`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud two independent protocols A and B both extended to String: the form was `(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op "x") (b-op "x")])`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the pair [a-op b-op] when each protocol is used independently.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol A (a-op [this])) (defprotocol B (b-op [this])) (extend-protocol A java.lang.String (a-op [_] :a-impl)) (extend-protocol B java.lang.String (b-op [_] :b-impl)) [(a-op \"x\") (b-op \"x\")])"}}]}
```

### G8-15: derive and isa? — multimethod hierarchy

**form**: `(do (derive ::hare ::runner) (isa? ::hare ::runner))`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Today near the hilltop, Shelly the tortoise explained to Pip the hare that one named
operation could mean different things for different kinds of creatures
— a hare's pace was not a tortoise's pace, yet both could be asked the
same question. The form `(do (derive ::hare ::runner) (isa? ::hare ::runner))` captured deriving ::hare from ::runner and asking isa?, and
Shelly suggested they hand it to the REPL.

Write a form whose evaluation gives whether ::hare isa? ::runner after derive.

---

I wrap the definition and the call together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (derive ::hare ::runner) (isa? ::hare ::runner))"}}]}
```

### G8-16: Abstract design with protocols

**form**: `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))`  •  **expected**: `[':leap', ':plod']`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Today at the edge of the road, Mossback the tortoise explained to Bramble the hare that one named
operation could mean different things for different kinds of creatures
— a hare's pace was not a tortoise's pace, yet both could be asked the
same question. The form `(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))` captured a Move protocol with two record implementations, mapped over instances, and
Mossback suggested they hand it to the REPL.

What Clojure form computes the pair of step results for a Hare and a Tortoise? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Move (step [this])) (defrecord Hare [] Move (step [_] :leap)) (defrecord Tortoise [] Move (step [_] :plod)) (mapv step [(->Hare) (->Tortoise)]))"}}]}
```

## Grade 9

### G9-01: Immutability as default — review

**form**: `(let [m {:a 1}] (assoc m :b 2) m)`  •  **expected**: `{':a': 1}`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said swaggering through the underbrush.
"Anyone can see what binding m, calling (assoc m :b 2), then returning m unchanged comes to." Slowpoke the tortoise, who
near the hilltop had grown used to such claims, asked her to actually
write the form `(let [m {:a 1}] (assoc m :b 2) m)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the original map after a non-mutating assoc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [m {:a 1}] (assoc m :b 2) m)"}}]}
```

### G9-02: Why state at all

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written an atom counter, incremented once, then read on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(do (def counter (atom 0)) (swap! counter inc) @counter)`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the value of counter after one swap! inc.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
```

### G9-03: Atom introduction

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

A wooden sign nailed to a tree at the edge of the garden carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(do (def a (atom 0)) (swap! a inc) @a)`. Hopper
laughed, swaggering through the underbrush, and declared it too easy. Slowpoke said
patiently that the only way to be sure of an atom starting at 0, incremented once via swap! was to put
it in the REPL.

What Clojure form computes the value of the atom after one swap! inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-04: Atom CAS semantics

**form**: `(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`  •  **expected**: `1`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"Why bother with all this?" Bramble the hare demanded across the hilltop.
"She could just write the new value!" Shelly the tortoise,
saying very little, sketched out compare-and-set! on an atom: expected 0, set to 1 instead and showed the form
`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the atom after a successful CAS.

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (compare-and-set! a 0 1) @a)"}}]}
```

### G9-05: Watch on atom

**form**: `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`  •  **expected**: `[1]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Pip the hare stopped by the woods and refused to
continue until someone could prove what the form `(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
an atom with a watch that appends each new value to a log to the REPL. Whatever comes back is the answer."

Question: write a Clojure expression for the contents of the log after one swap.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (def log (atom [])) (add-watch a :w (fn [_ _ _ n] (swap! log conj n))) (swap! a inc) @log)"}}]}
```

### G9-06: Validator on atom

**form**: `(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`  •  **expected**: `1`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

"Why bother with all this?" Hopper the hare demanded near the woods.
"He could just write the new value!" Shelly the tortoise,
her eyes always on the path, sketched out an atom with a number? validator, incremented once instead and showed the form
`(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

Question: write a Clojure expression for the value of the atom after a valid update.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (set-validator! a number?) (swap! a inc) @a)"}}]}
```

### G9-07: Ref introduction

**form**: `(do (def r (ref 0)) (dosync (alter r inc)) @r)`  •  **expected**: `1`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Whisker the hare stopped across the forest and refused to
continue until someone could prove what the form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`
evaluated to. He called it impossible.
Mossback the tortoise, walking up at her usual pace, simply said: "Submit
a ref incremented inside a dosync transaction to the REPL. Whatever comes back is the answer."

Write a form whose evaluation gives the value of the ref after dosync alter inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def r (ref 0)) (dosync (alter r inc)) @r)"}}]}
```

### G9-08: dosync and alter

**form**: `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])`  •  **expected**: `[2, 3]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
two refs each incremented inside a single dosync.

What Clojure form computes the pair [a b] after the coordinated transaction? Submit it via `eval`.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (ref 1)) (def b (ref 2)) (dosync (alter a inc) (alter b inc)) [@a @b])"}}]}
```

### G9-09: Ref vs atom

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(do (def a (atom 0)) (swap! a inc) @a)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
an atom updated via swap!.

Question: write a Clojure expression for the value of the atom after one swap! inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
```

### G9-10: Agent introduction

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written an agent sent inc and awaited on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`
in the REPL and read off whatever it returned.

What Clojure form computes the value of the agent after send inc and await? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-11: send and send-off

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had been keeping a small leather notebook of every
form she had successfully evaluated. Today in the meadow, the
next entry was send used on an agent, then awaited. Hopper the hare peered over
her shoulder at the form `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)` and asked what
it would come out to.

Write a Clojure expression that computes the agent's value after send inc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
```

### G9-12: await — synchronizing on agents

**form**: `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)`  •  **expected**: `2`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone near the hilltop, Pip the hare drew a wager in the
dust: whoever guessed the result of `(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)` first would win the
right to set the next race. Slowpoke the tortoise, stepping deliberately, said it
was simpler to type the form into the REPL than to argue about
two send inc calls then await before deref.

Question: write a Clojure expression for the agent's value after two sends and await.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)"}}]}
```

### G9-13: future introduction

**form**: `@(future (+ 1 2))`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `@(future (+ 1 2))` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
a future computing (+ 1 2), dereferenced.

Write a form whose evaluation gives the value of the future for (+ 1 2).

---

I let the runtime mediate the change before reading the final value.

{"tool_calls":[{"name":"eval","args":{"form":"@(future (+ 1 2))"}}]}
```

### G9-14: deref @ shorthand

**form**: `(do (def a (atom 7)) @a)`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

A small audience of forest creatures had gathered at the edge of the forest to watch
Pip the hare attempt to outwit Slowpoke the tortoise at reading the REPL.
Slowpoke read aloud deref via @ on an atom holding 7: the form was `(do (def a (atom 7)) @a)`.
The crowd waited to see who would correctly write the form to submit.

Write a Clojure expression that computes the value of the atom via @.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 7)) @a)"}}]}
```

### G9-15: promise — deliver and deref

**form**: `(do (def p (promise)) (deliver p :done) @p)`  •  **expected**: `':done'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise kept a small ledger of state near the hilltop — a value that
might change as the race went on. She explained that
the form `(do (def p (promise)) (deliver p :done) @p)` captured a promise delivered with :done, then dereffed: a careful, ordered
update. Pip the hare, with great whoops of laughter, asked the REPL to confirm the final
value.

Write a form whose evaluation gives the value of the promise after deliver.

---

I wrap the def, the update, and the deref together in a do block.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def p (promise)) (deliver p :done) @p)"}}]}
```

### G9-16: volatile — when STM is too heavy

**form**: `(do (def v (volatile! 0)) (vswap! v inc) @v)`  •  **expected**: `1`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Mossback the tortoise kept a small ledger of state at the edge of the road — a value that
might change as the race went on. He explained that
the form `(do (def v (volatile! 0)) (vswap! v inc) @v)` captured a volatile! incremented via vswap!: a careful, ordered
update. Bramble the hare, swaggering through the underbrush, asked the REPL to confirm the final
value.

What Clojure form computes the value of the volatile after one vswap! inc? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def v (volatile! 0)) (vswap! v inc) @v)"}}]}
```

### G9-17: binding — thread-local

**form**: `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))`  •  **expected**: `99`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

"There is no need to evaluate that," Hopper the hare said with a smug grin.
"Anyone can see what a dynamic var *p* rebound to 99 inside binding comes to." Slowpoke the tortoise, who
by the meadow had grown used to such claims, asked him to actually
write the form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the value of *p* inside the binding form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))"}}]}
```

### G9-18: locking — last resort

**form**: `(do (def lock (Object.)) (locking lock (+ 1 2)))`  •  **expected**: `3`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

"Why bother with all this?" Bramble the hare demanded by the road.
"She could just write the new value!" Slowpoke the tortoise,
her eyes always on the path, sketched out a locking form around (+ 1 2) using a fresh Object as monitor instead and showed the form
`(do (def lock (Object.)) (locking lock (+ 1 2)))`: the proper way for the runtime to manage change. They
agreed to submit it to the REPL.

What Clojure form computes the result of the body inside locking? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def lock (Object.)) (locking lock (+ 1 2)))"}}]}
```

## Grade 10

### G10-01: quote, unquote, unquote-splice

**form**: `(quote (+ 1 2))`  •  **expected**: `['+', 1, 2]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"A macro is just a function that runs at compile time," Slowpoke
explained near the hilltop, stepping deliberately. Bramble, swaggering through the underbrush, said
she could already see what the quoted form (quote (+ 1 2)) meant.
Slowpoke the tortoise insisted they actually evaluate `(quote (+ 1 2))` and
read what the runtime reported, expansion or value.

Write a form whose evaluation gives the value of (quote (+ 1 2)) — the unevaluated list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(quote (+ 1 2))"}}]}
```

### G10-02: syntax-quote

**form**: `(let [x 10] `(+ ~x ~x))`  •  **expected**: `['+', 10, 10]`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written a syntax-quoted addition with x unquoted twice on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(let [x 10] `(+ ~x ~x))`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the form produced by `(+ ~x ~x) when x is 10.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 10] `(+ ~x ~x))"}}]}
```

### G10-03: defmacro introduction

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

Hopper the hare insisted at the edge of the garden that macros were the same as functions.
Slowpoke the tortoise, saying very little, drew the form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))` on a
strip of bark. "The difference," he said, "is in
a tiny when-style macro and a call to it. Submit the form and let the runtime tell us
exactly what it does."

What Clojure form computes what (my-when true 1 2 3) returns? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
```

### G10-04: Macro expansion rule

**form**: `(macroexpand-1 '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

At a stone tablet across the hilltop, Shelly the tortoise was teaching
Bramble the hare the discipline of expansion: never trust your eyes, only
the macroexpander. The day's example was the one-step expansion of (when true 1). The form
`(macroexpand-1 '(when true 1))` had to be submitted; nothing else would do.

Question: write a Clojure expression for what macroexpand-1 returns for (when true 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand-1 '(when true 1))"}}]}
```

### G10-05: macroexpand

**form**: `(macroexpand '(when true 1))`  •  **expected**: `['if', True, ['do', 1]]`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"There is no need to evaluate that," Pip the hare said with great whoops of laughter.
"Anyone can see what the full expansion of (when true 1) comes to." Slowpoke the tortoise, who
by the woods had grown used to such claims, asked them to actually
write the form `(macroexpand '(when true 1))` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for what macroexpand returns for (when true 1).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(macroexpand '(when true 1))"}}]}
```

### G10-06: when and when-not as macros

**form**: `(when true 1 2 3)`  •  **expected**: `3`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A small notebook lay open near the woods where the Tortoise had been studying
syntax-quote. The page showed the form (when true 1 2 3), with the form
`(when true 1 2 3)` circled in pencil. Hopper the hare, weary from the morning's effort of
the lecture, agreed to write the form to settle once and for all
what it produced.

Question: write a Clojure expression for what (when true 1 2 3) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(when true 1 2 3)"}}]}
```

### G10-07: Threading macros revisited

**form**: `(-> 5 inc inc inc)`  •  **expected**: `8`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Whisker the hare said with great whoops of laughter.
"Anyone can see what the thread-first form (-> 5 inc inc inc) comes to." Mossback the tortoise, who
across the forest had grown used to such claims, asked him to actually
write the form `(-> 5 inc inc inc)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives what (-> 5 inc inc inc) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(-> 5 inc inc inc)"}}]}
```

### G10-08: Macro vs fn

**form**: `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
a plain function adding two numbers.

What Clojure form computes the result of calling a function (args evaluated)? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))"}}]}
```

### G10-09: Hygiene and gensym

**form**: `(symbol? (gensym))`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(symbol? (gensym))` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the predicate (symbol? (gensym)).

Question: write a Clojure expression for whether (gensym) returns a symbol.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? (gensym))"}}]}
```

### G10-10: Anaphoric macros are confusing

**form**: `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`  •  **expected**: `10`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written a hygienic if-let style macro avoiding anaphoric injection on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))`
in the REPL and read off whatever it returned.

What Clojure form computes what the hygienic if-let macro returns? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro safe-if-let [bind then else] `(if-let ~bind ~then ~else)) (safe-if-let [x 5] (* x 2) 0))"}}]}
```

### G10-11: Reader macros overview

**form**: `'(1 2 3)`  •  **expected**: `[1, 2, 3]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise had spent the morning in the meadow sketching a tiny
language of her own — a notebook of macros that wrote
other forms. The next entry was the quote reader macro 'foo, and the form
`'(1 2 3)` was what Shelly wanted Hopper the hare to submit so
the REPL could show what code it produced or what value it returned.

Write a Clojure expression that computes what '(1 2 3) reads as.

---

{"tool_calls":[{"name":"eval","args":{"form":"'(1 2 3)"}}]}
```

### G10-12: Tagged literals

**form**: `(inst? #inst "2024-01-01")`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the predicate (inst? #inst "2024-01-01"). "You hand the form `(inst? #inst "2024-01-01")` to the runtime, and
the runtime hands you back what it evaluates to." Pip, yawning at the soft moss
from a recent sprint, agreed to try.

Question: write a Clojure expression for whether the #inst tagged literal reads to an inst.

---

I submit the syntax-quoted or quoted form to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(inst? #inst \"2024-01-01\")"}}]}
```

### G10-13: Data readers and EDN extension

**form**: `(clojure.edn/read-string "42")`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(clojure.edn/read-string "42")` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
edn read-string of "42".

Write a form whose evaluation gives what edn/read-string returns for the source "42".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.edn/read-string \"42\")"}}]}
```

### G10-14: eval (the function)

**form**: `(eval '(+ 1 2 3))`  •  **expected**: `6`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Pip the hare stopped at the edge of the forest and refused to
continue until someone could prove what the form `(eval '(+ 1 2 3))`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the form (eval '(+ 1 2 3)) to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes what eval returns for the quoted (+ 1 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(eval '(+ 1 2 3))"}}]}
```

### G10-15: When not to write a macro

**form**: `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))`  •  **expected**: `7`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Pip the hare insisted near the hilltop that macros were the same as functions.
Shelly the tortoise, without complaint, drew the form `(do "a function suffices when no syntax shaping is needed" ((fn [x y] (+ x y)) 3 4))` on a
strip of bark. "The difference," she said, "is in
a function call where no macro is justified. Submit the form and let the runtime tell us
exactly what it does."

Write a form whose evaluation gives what the plain function call returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"a function suffices when no syntax shaping is needed\" ((fn [x y] (+ x y)) 3 4))"}}]}
```

### G10-16: Macro pattern library

**form**: `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))`  •  **expected**: `42`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

Bramble the hare insisted at the edge of the road that macros were the same as functions.
Mossback the tortoise, stepping deliberately, drew the form `(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))` on a
strip of bark. "The difference," he said, "is in
a with-X macro pattern that binds a local and runs body. Submit the form and let the runtime tell us
exactly what it does."

What Clojure form computes what the with- macro yields? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro with-tortoise-pace [& body] `(let [pace# :slow-and-steady] ~@body)) (with-tortoise-pace 42))"}}]}
```

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

**form**: `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"This is not your meadow," Slowpoke the tortoise said near the hilltop, stepping deliberately.
"Here, the methods belong to objects, and the dot has a particular
meaning." Bramble the hare, swaggering through the underbrush, said she could read
the foreign form anyway. Slowpoke sketched `(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)` on the
ground; let the runtime, he insisted, declare what
the idea that Clojure has multiple host runtimes returned.

Write a form whose evaluation gives the marker value when the host overview has been studied.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Clojure runs on multiple hosts: JVM, CLR, JS, Python\" :studied)"}}]}
```

### G11-02: Method call syntax

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the method call (.toUpperCase "abc") on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(.toUpperCase "abc")`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the uppercased string returned by the method.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
```

### G11-03: Static method call

**form**: `(Math/abs -7)`  •  **expected**: `7`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

Hopper the hare insisted the foreign-runtime forms were "just like home."
Slowpoke the tortoise tapped a stone at the edge of the garden where someone had inscribed
the static call (Math/abs -7). "Then write `(Math/abs -7)` into the REPL," Slowpoke
said, "and we'll see if your familiarity holds."

What Clojure form computes the absolute value of -7 via the static method? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(Math/abs -7)"}}]}
```

### G11-04: Field access

**form**: `(count "tortoise")`  •  **expected**: `8`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A merchant's stall across the hilltop sold translated phrasebooks for the host
language; today's lesson was the count of "tortoise" — host-portable length. Shelly the tortoise
copied the form `(count "tortoise")` from the page, and Bramble the hare
agreed (for once) that one should always check the REPL before
trusting a translation.

Question: write a Clojure expression for the length of "tortoise".

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
```

### G11-05: Import form

**form**: `(do "(:import (java.util Date)) imports a host class" :imported)`  •  **expected**: `':imported'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"There is no need to evaluate that," Pip the hare said with great whoops of laughter.
"Anyone can see what the (:import ...) ns clause for host classes comes to." Slowpoke the tortoise, who
by the woods had grown used to such claims, asked them to actually
write the form `(do "(:import (java.util Date)) imports a host class" :imported)` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the marker for the import-form lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(:import (java.util Date)) imports a host class\" :imported)"}}]}
```

### G11-06: new and dot-construct

**form**: `(String. "hello")`  •  **expected**: `'hello'`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

At a wayside shrine near the woods dedicated to interop, the day's offering
was the constructor call (String. "hello"). Shelly the tortoise knelt and placed the form
`(String. "hello")` on the stone. Hopper, watching, agreed to be the one
to submit it to the runtime.

Question: write a Clojure expression for the string built by the dot-construct.

---

{"tool_calls":[{"name":"eval","args":{"form":"(String. \"hello\")"}}]}
```

### G11-07: Arrays

**form**: `(let [a (int-array [10 20 30])] (aget a 1))`  •  **expected**: `20`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Whisker the hare said with great whoops of laughter.
"Anyone can see what indexing into an int-array via aget comes to." Mossback the tortoise, who
across the forest had grown used to such claims, asked him to actually
write the form `(let [a (int-array [10 20 30])] (aget a 1))` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the value at index 1 of the array.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [a (int-array [10 20 30])] (aget a 1))"}}]}
```

### G11-08: Type hints

**form**: `(let [^String s "abc"] (.toUpperCase s))`  •  **expected**: `'ABC'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(let [^String s "abc"] (.toUpperCase s))` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
a let-binding with a ^String type hint.

What Clojure form computes the uppercased string after a type-hinted binding? Submit it via `eval`.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(let [^String s \"abc\"] (.toUpperCase s))"}}]}
```

### G11-09: Checked vs unchecked math

**form**: `(+ 1 2)`  •  **expected**: `3`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(+ 1 2)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the form (+ 1 2) under default checked math.

Question: write a Clojure expression for the result of (+ 1 2) under the default math regime.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G11-10: ClojureScript overview

**form**: `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`  •  **expected**: `':studied'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the ClojureScript host overview on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)`
in the REPL and read off whatever it returned.

What Clojure form computes the marker for studying the cljs host? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"ClojureScript compiles to JavaScript via the Closure compiler\" :studied)"}}]}
```

### G11-11: cljs / JavaScript interop

**form**: `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

Shelly the tortoise and Hopper the hare had wandered in the meadow into territory
where the REPL spoke to another runtime entirely. Shelly read the
sign and pointed at the cljs-to-js interop syntax; the form to submit, written in
the foreign convention, was `(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)`.

Write a Clojure expression that computes the marker for the cljs-js interop lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(js/console.log x) calls a JS global; (.-foo o) reads a JS field\" :studied)"}}]}
```

### G11-12: Basilisp overview (Python host)

**form**: `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the basilisp host overview. "You hand the form `(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)` to the runtime, and
the runtime hands you back what it evaluates to." Pip, yawning at the soft moss
from a recent sprint, agreed to try.

Question: write a Clojure expression for the marker for studying basilisp.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"basilisp is a Clojure-like Lisp implemented on Python\" :studied)"}}]}
```

### G11-13: Cross-platform .cljc and reader-conditionals

**form**: `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the reader-conditional #?(...) form.

Write a form whose evaluation gives the marker for the reader-conditional lesson.

---

I express the host call as a Clojure form for the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"#?(:clj … :cljs …) selects a form per host at read time\" :studied)"}}]}
```

### G11-14: Debugging host leaks

**form**: `(do "host stack traces leak through interop; learn to read them" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Pip the hare stopped at the edge of the forest and refused to
continue until someone could prove what the form `(do "host stack traces leak through interop; learn to read them" :studied)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the topic of debugging host-runtime leaks to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the marker for the host-leaks lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"host stack traces leak through interop; learn to read them\" :studied)"}}]}
```

## Grade 12

### G12-01: Transducers introduction

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had filled an entire notebook over the long race
with tools and patterns: transducers, channels, specs, tests.
near the hilltop, the next entry was the transducer (map inc) used via into, and the form was
`(into [] (map inc) [1 2 3])`. Bramble the hare, swaggering through the underbrush but more reflective than
usual, agreed to write the form into the REPL.

Write a form whose evaluation gives [1 2 3] each incremented through a transducer.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
```

### G12-02: Transducer composition

**form**: `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`  •  **expected**: `[2, 4]`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Hopper the hare and Mossback the tortoise stopped across the forest where someone had
written the composed transducer (comp (map inc) (filter even?)) on a flat stone. Hopper, with a smug grin, declared
that he could see the answer at a glance. Mossback,
stepping deliberately, suggested they actually evaluate the form `(into [] (comp (map inc) (filter even?)) [1 2 3 4])`
in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result of inc-then-keep-evens via a composed transducer.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (comp (map inc) (filter even?)) [1 2 3 4])"}}]}
```

### G12-03: into with a transducer (xform)

**form**: `(into #{} (map inc) [1 2 3])`  •  **expected**: `{2, 3, 4}`

```
It was well known among the animals that the Hare boasted of his speed at every chance. All this took place in the garden.

At the finish line at the edge of the garden, a row of small monuments commemorated
the libraries the racers had learned along the way. The newest one
honoured into a set with the (map inc) transducer. Slowpoke the tortoise touched it with a paw
and said the form to remember was `(into #{} (map inc) [1 2 3])`; Hopper the hare
agreed to submit it.

What Clojure form computes the set produced by mapping inc into an empty set? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into #{} (map inc) [1 2 3])"}}]}
```

### G12-04: core.async introduction

**form**: `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)`  •  **expected**: `':studied'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A banquet at the end of the road across the hilltop brought together every
animal who'd ever raced. The day's discussion was the core.async primitives chan/go/<!/>!.
Shelly wrote the form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)` on a square of parchment
and passed it across the table; Bramble, weary from the morning's effort but pleased,
agreed to read it into the REPL.

Question: write a Clojure expression for the marker for the core.async lesson.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(chan), (go ...), (<! ...), (>! ...) form the core.async core\" :studied)"}}]}
```

### G12-05: Channels and pipelines

**form**: `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)`  •  **expected**: `':studied'`

```
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

"There is no need to evaluate that," Pip the hare said with great whoops of laughter.
"Anyone can see what the pipeline operators in core.async comes to." Slowpoke the tortoise, who
by the woods had grown used to such claims, asked them to actually
write the form `(do "pipe, mult, mix, pipeline-async route values across channels" :studied)` and submit it to the REPL — just to be
sure.

Question: write a Clojure expression for the marker for the channel-pipeline lesson.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"pipe, mult, mix, pipeline-async route values across channels\" :studied)"}}]}
```

### G12-06: clojure.spec

**form**: `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))`  •  **expected**: `True`

```
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Hopper the hare, weary from the morning's effort from a season of races, was finally willing
to study patterns. Shelly the tortoise pointed near the woods at
(s/valid? int? 42) — a basic spec check. The form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))` was the canonical example;
the REPL would confirm what it produced.

Question: write a Clojure expression for whether 42 conforms to the int? spec.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42))"}}]}
```

### G12-07: Spec generators

**form**: `(do "s/exercise produces sample inputs for a spec" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Whisker the hare said with great whoops of laughter.
"Anyone can see what what s/exercise does comes to." Mossback the tortoise, who
across the forest had grown used to such claims, asked him to actually
write the form `(do "s/exercise produces sample inputs for a spec" :studied)` and submit it to the REPL — just to be
sure.

Write a form whose evaluation gives the marker for the spec-generators lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"s/exercise produces sample inputs for a spec\" :studied)"}}]}
```

### G12-08: clojure.test

**form**: `(= (+ 1 2) 3)`  •  **expected**: `True`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the hilltop.

At a moss-covered milestone near the hilltop, Whisker the hare drew a wager in the
dust: whoever guessed the result of `(= (+ 1 2) 3)` first would win the
right to set the next race. Shelly the tortoise, without complaint, said it
was simpler to type the form into the REPL than to argue about
(= (+ 1 2) 3) — what an `is` would test.

What Clojure form computes the truth value an `is` assertion would record? Submit it via `eval`.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(= (+ 1 2) 3)"}}]}
```

### G12-09: Test fixtures

**form**: `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place across the forest.

At a moss-covered milestone by the forest, Hopper the hare drew a wager in the
dust: whoever guessed the result of `(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)` first would win the
right to set the next race. Shelly the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
use-fixtures and the fixture pattern.

Question: write a Clojure expression for the marker for the fixtures lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"(use-fixtures :each f) wraps every deftest in setup/teardown\" :studied)"}}]}
```

### G12-10: Property-based testing

**form**: `(= (reverse (reverse [1 2 3])) [1 2 3])`  •  **expected**: `True`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare and Slowpoke the tortoise stopped near the road where someone had
written the property that double-reverse is identity on a flat stone. Pip, boasting at every turn, declared
that they could see the answer at a glance. Slowpoke,
with steady, careful steps, suggested they actually evaluate the form `(= (reverse (reverse [1 2 3])) [1 2 3])`
in the REPL and read off whatever it returned.

What Clojure form computes the truth value of the double-reverse property on [1 2 3]? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= (reverse (reverse [1 2 3])) [1 2 3])"}}]}
```

### G12-11: Leiningen project.clj

**form**: `(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. It happened in the meadow.

The race had ended in the meadow and the two were sitting beneath an old
tree, comparing notes. Shelly the tortoise drew the project.clj manifest for Leiningen into
the dust. "We've come a long way," she said. "The form
`(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)` is the kind of thing we'd reach for now." Hopper
nodded — for once her legs heavy from sprinting enough to listen.

Write a Clojure expression that computes the marker for the project.clj lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"project.clj declares :dependencies, :main, :profiles for Leiningen\" :studied)"}}]}
```

### G12-12: deps.edn projects

**form**: `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been trying to teach Pip the hare how the REPL
works. "Look here," he said, pointing to
the deps.edn manifest for the Clojure CLI. "You hand the form `(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)` to the runtime, and
the runtime hands you back what it evaluates to." Pip, yawning at the soft moss
from a recent sprint, agreed to try.

Question: write a Clojure expression for the marker for the deps.edn lesson.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"deps.edn declares :deps and :aliases for the Clojure CLI\" :studied)"}}]}
```

### G12-13: Aliases and tools

**form**: `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At a moss-covered milestone at the edge of the orchard, Bramble the hare drew a wager in the
dust: whoever guessed the result of `(do "`clj -M:test` runs the :test alias from deps.edn" :studied)` first would win the
right to set the next race. Mossback the tortoise, with steady, careful steps, said it
was simpler to type the form into the REPL than to argue about
the alias-execution pattern with the Clojure CLI.

Write a form whose evaluation gives the marker for the aliases lesson.

---

I let the REPL exercise the library form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"`clj -M:test` runs the :test alias from deps.edn\" :studied)"}}]}
```

### G12-14: Pedestal / Ring (web stack brief)

**form**: `(do "Ring models HTTP as request-map -> response-map" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Pip the hare stopped at the edge of the forest and refused to
continue until someone could prove what the form `(do "Ring models HTTP as request-map -> response-map" :studied)`
evaluated to. They called it impossible.
Slowpoke the tortoise, walking up at her usual pace, simply said: "Submit
the Ring HTTP-as-data abstraction to the REPL. Whatever comes back is the answer."

Write a Clojure expression that computes the marker for the Ring lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Ring models HTTP as request-map -> response-map\" :studied)"}}]}
```

### G12-15: Datomic / XTDB (datalog db brief)

**form**: `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

At the finish line near the hilltop, a row of small monuments commemorated
the libraries the racers had learned along the way. The newest one
honoured the Datomic / XTDB family. Shelly the tortoise touched it with a paw
and said the form to remember was `(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)`; Pip the hare
agreed to submit it.

Write a form whose evaluation gives the marker for the datalog-DB lesson.

---

I express the pipeline / spec / test as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Datomic and XTDB are immutable, time-aware datalog DBs\" :studied)"}}]}
```

### G12-16: Reagent (cljs UI brief)

**form**: `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`  •  **expected**: `':studied'`

```
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the road.

At the finish line at the edge of the road, a row of small monuments commemorated
the libraries the racers had learned along the way. The newest one
honoured the Reagent wrapper around React. Mossback the tortoise touched it with a paw
and said the form to remember was `(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)`; Bramble the hare
agreed to submit it.

What Clojure form computes the marker for the Reagent lesson? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"Reagent wraps React with Hiccup-shaped Clojure data\" :studied)"}}]}
```

### G12-17: Library design patterns

**form**: `(do "good libraries expose data, then functions, then macros sparingly" :studied)`  •  **expected**: `':studied'`

```
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. This was at the edge of the meadow.

The race had ended by the meadow and the two were sitting beneath an old
tree, comparing notes. Slowpoke the tortoise drew the Clojure library-design hierarchy into
the dust. "We've come a long way," he said. "The form
`(do "good libraries expose data, then functions, then macros sparingly" :studied)` is the kind of thing we'd reach for now." Hopper
nodded — for once lulled by the gentle wind enough to listen.

Write a Clojure expression that computes the marker for the library-design lesson.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do \"good libraries expose data, then functions, then macros sparingly\" :studied)"}}]}
```

### G12-18: Clojure style guide

**form**: `(do "kebab-case names, two-space indent, threading for deep nests" :studied)`  •  **expected**: `':studied'`

```
It was well known among the animals that the Hare boasted of his speed at every chance.

Bramble the hare, weary from the morning's effort from a season of races, was finally willing
to study patterns. Slowpoke the tortoise pointed by the road at
the community-style basics. The form `(do "kebab-case names, two-space indent, threading for deep nests" :studied)` was the canonical example;
the REPL would confirm what it produced.

What Clojure form computes the marker for the style-guide lesson? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(do \"kebab-case names, two-space indent, threading for deep nests\" :studied)"}}]}
```

