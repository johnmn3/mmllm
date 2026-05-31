# Deep spot-check: grade 1 ant-grasshopper (5 records per subject)

Manual-review dump for hand-audit. Each subject gets 5 rendered records sampled across different seeds so subplot/character/location variety is visible.

---

## G1-01: Eval as substitution

### G1-01 record 1

**form**: `42`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

Halfway through the morning's work, Skip the grasshopper blocked
Toc the ant's path atop the hilltop and refused to step aside until someone
could prove what the form `42` evaluated to. Skip
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the value 42 to the REPL. Whatever comes
back is the answer."

What Clojure form computes the value of 42? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 record 2

**form**: `42`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the farm.

Bit the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," they said, pointing to the value 42.
"You hand the form `42` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

Write a form whose evaluation gives the value of 42.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 record 3

**form**: `42`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile on the hilltop, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `42`
first would win the right to set the next day's count.
Bit the ant, untroubled by what others thought, said it was simpler to type the form into
the REPL than to argue about the value 42.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 record 4

**form**: `42`  •  **expected**: `42`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Skip the grasshopper said,
as if the race were already won. "Anyone can see what the value 42 comes to."
Bit the ant, who by the orchard had grown used to such claims, asked
her to actually write the form `42` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of 42.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-01 record 5

**form**: `42`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Skip the grasshopper marked out a wager at the edge of the forest: whoever
guessed the result of `42` first would win the right to
choose the next song. Toc the ant, with steady, careful steps, said it was easier
to ask the REPL about the value 42 than to argue.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

## G1-02: Integer numbers

### G1-02 record 1

**form**: `7`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered atop the hilltop to watch
Chirp the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the integer 7 and read out the form aloud:
`7`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 record 2

**form**: `7`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

Chirp the grasshopper chalked a wager on a flat slate atop the hilltop: whoever
predicted the result of `7` first would set the next day's
ration. Bit the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about the integer 7.

What Clojure form computes the value of the integer 7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 record 3

**form**: `7`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

"There is no need to evaluate that," Hum the grasshopper said,
with a smug grin. "Anyone can see what the integer 7 comes to."
Toc the ant, who by the orchard had grown used to such claims, asked
them to actually write the form `7` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 record 4

**form**: `7`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `7` first would set the next day's
ration. Toc the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about the integer 7.

Write a Clojure expression that computes the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

### G1-02 record 5

**form**: `7`  •  **expected**: `7`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk by the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `7`. Skip
laughed, puffed up with pride, and declared it too easy. Tic said patiently
that the only way to be sure of the integer 7 was to put it in the
REPL.

Write a Clojure expression that computes the value of the integer 7.

---

{"tool_calls":[{"name":"eval","args":{"form":"7"}}]}
```

## G1-03: Ratios

### G1-03 record 1

**form**: `1/2`  •  **expected**: `'1/2'`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the garden.

With a twig, Skip the grasshopper marked out a wager near the garden: whoever
guessed the result of `1/2` first would win the right to
choose the next song. Tic the ant, with steady, careful steps, said it was easier
to ask the REPL about the ratio 1/2 than to argue.

Question: write a Clojure expression for the value of the ratio 1/2.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 record 2

**form**: `1/2`  •  **expected**: `'1/2'`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile in the meadow, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `1/2`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the ratio 1/2.

What Clojure form computes the value of the ratio 1/2? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 record 3

**form**: `1/2`  •  **expected**: `'1/2'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

A small audience of meadow creatures had gathered by the garden to watch
Chirp the grasshopper attempt to outwit Bit the ant at reading the
REPL. Bit pointed to the ratio 1/2 and read out the form aloud:
`1/2`. The crowd waited to see who would correctly write the
form to submit.

What Clojure form computes the value of the ratio 1/2? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 record 4

**form**: `1/2`  •  **expected**: `'1/2'`

```
Two creatures of the meadow approached the coming winter very differently. It happened by the orchard.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the orchard, the next entry
was the ratio 1/2. Skip the grasshopper peered over
her shoulder at the form `1/2` and asked what it
would come out to.

Write a Clojure expression that computes the value of the ratio 1/2.

---

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

### G1-03 record 5

**form**: `1/2`  •  **expected**: `'1/2'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Tic the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," he said, pointing to the ratio 1/2.
"You hand the form `1/2` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, lulled by the gentle wind, agreed to
try.

What Clojure form computes the value of the ratio 1/2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"1/2"}}]}
```

## G1-04: Strings

### G1-04 record 1

**form**: `"hello"`  •  **expected**: `'hello'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Chirp the grasshopper marked out a wager on the hilltop: whoever
guessed the result of `"hello"` first would win the right to
choose the next song. Toc the ant, saying very little, said it was easier
to ask the REPL about the string "hello" than to argue.

Write a Clojure expression that computes the value of "hello".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 record 2

**form**: `"hello"`  •  **expected**: `'hello'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was on the hilltop.

With a twig, Chirp the grasshopper marked out a wager near the hilltop: whoever
guessed the result of `"hello"` first would win the right to
choose the next song. Tic the ant, stepping deliberately, said it was easier
to ask the REPL about the string "hello" than to argue.

Write a Clojure expression that computes the value of "hello".

---

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 record 3

**form**: `"hello"`  •  **expected**: `'hello'`

```
Two creatures of the meadow approached the coming winter very differently.

Skip the grasshopper chalked a wager on a flat slate in the garden: whoever
predicted the result of `"hello"` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the string "hello".

What Clojure form computes the value of "hello"? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 record 4

**form**: `"hello"`  •  **expected**: `'hello'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," she said, pointing to the string "hello".
"You hand the form `"hello"` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, yawning at the soft moss, agreed to
try.

Write a Clojure expression that computes the value of "hello".

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

### G1-04 record 5

**form**: `"hello"`  •  **expected**: `'hello'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the orchard.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today by the orchard, the next entry
was the string "hello". Skip the grasshopper peered over
her shoulder at the form `"hello"` and asked what it
would come out to.

Write a Clojure expression that computes the value of "hello".

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"\"hello\""}}]}
```

## G1-05: Booleans

### G1-05 record 1

**form**: `true`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

A small audience of meadow creatures had gathered at the edge of the woods to watch
Skip the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the literal true and read out the form aloud:
`true`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives the value of true.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 record 2

**form**: `true`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place atop the hilltop.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path atop the hilltop and refused to step aside until someone
could prove what the form `true` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the literal true to the REPL. Whatever comes
back is the answer."

Question: write a Clojure expression for the value of true.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 record 3

**form**: `true`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. This was near the woods.

Tic the ant and Skip the grasshopper stopped in the woods where someone had
written the literal true on a flat stone. Skip, swaggering through the underbrush,
declared that she could see the answer at a glance.
Tic, her eyes always on the path, suggested they actually evaluate the form
`true` in the REPL and read off whatever it returned.

What Clojure form computes the value of true? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 record 4

**form**: `true`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today at the edge of the farm, the next entry
was the literal true. Hum the grasshopper peered over
his shoulder at the form `true` and asked what it
would come out to.

Write a Clojure expression that computes the value of true.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

### G1-05 record 5

**form**: `true`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Toc the ant and Hum the grasshopper stopped atop the hilltop where someone had
written the literal true on a flat stone. Hum, puffed up with pride,
declared that they could see the answer at a glance.
Toc, her eyes always on the path, suggested they actually evaluate the form
`true` in the REPL and read off whatever it returned.

What Clojure form computes the value of true? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"true"}}]}
```

## G1-06: nil

### G1-06 record 1

**form**: `nil`  •  **expected**: `None`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk near the woods carried a puzzle. The riddle
was simple: it asked the reader to evaluate `nil`. Chirp
laughed, swaggering through the underbrush, and declared it too easy. Tic said patiently
that the only way to be sure of the literal nil was to put it in the
REPL.

Write a form whose evaluation gives the value of nil.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 record 2

**form**: `nil`  •  **expected**: `None`

```
All summer long, the Ant worked while the Grasshopper sang. This was near the orchard.

A small audience of meadow creatures had gathered by the orchard to watch
Hum the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the literal nil and read out the form aloud:
`nil`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 record 3

**form**: `nil`  •  **expected**: `None`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk in the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `nil`. Hum
laughed, boasting at every turn, and declared it too easy. Toc said patiently
that the only way to be sure of the literal nil was to put it in the
REPL.

Write a Clojure expression that computes the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 record 4

**form**: `nil`  •  **expected**: `None`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the forest.

With a twig, Skip the grasshopper marked out a wager in the forest: whoever
guessed the result of `nil` first would win the right to
choose the next song. Toc the ant, her eyes always on the path, said it was easier
to ask the REPL about the literal nil than to argue.

Question: write a Clojure expression for the value of nil.

---

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

### G1-06 record 5

**form**: `nil`  •  **expected**: `None`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was in the meadow.

With a twig, Skip the grasshopper marked out a wager by the meadow: whoever
guessed the result of `nil` first would win the right to
choose the next song. Bit the ant, stepping deliberately, said it was easier
to ask the REPL about the literal nil than to argue.

Question: write a Clojure expression for the value of nil.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"nil"}}]}
```

## G1-07: Keywords

### G1-07 record 1

**form**: `:ant`  •  **expected**: `':ant'`

```
Two creatures of the meadow approached the coming winter very differently.

Tic the ant had been trying to teach Hum the grasshopper how the REPL
works. "Look here," he said, pointing to the keyword :ant.
"You hand the form `:ant` to the runtime, and the runtime hands
you back what it evaluates to." Hum, lulled by the gentle wind, agreed to
try.

Question: write a Clojure expression for the value of :ant.

---

{"tool_calls":[{"name":"eval","args":{"form":":ant"}}]}
```

### G1-07 record 2

**form**: `:ant`  •  **expected**: `':ant'`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place at the edge of the farm.

"There is no need to evaluate that," Hum the grasshopper said,
with great whoops of laughter. "Anyone can see what the keyword :ant comes to."
Toc the ant, who in the farm had grown used to such claims, asked
them to actually write the form `:ant` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the value of :ant.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":":ant"}}]}
```

### G1-07 record 3

**form**: `:ant`  •  **expected**: `':ant'`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager at the edge of the orchard: whoever
guessed the result of `:ant` first would win the right to
choose the next song. Bit the ant, saying very little, said it was easier
to ask the REPL about the keyword :ant than to argue.

Question: write a Clojure expression for the value of :ant.

---

{"tool_calls":[{"name":"eval","args":{"form":":ant"}}]}
```

### G1-07 record 4

**form**: `:ant`  •  **expected**: `':ant'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

A wooden sign nailed to a stalk near the orchard carried a puzzle. The riddle
was simple: it asked the reader to evaluate `:ant`. Hum
laughed, as if the race were already won, and declared it too easy. Toc said patiently
that the only way to be sure of the keyword :ant was to put it in the
REPL.

Write a form whose evaluation gives the value of :ant.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":":ant"}}]}
```

### G1-07 record 5

**form**: `:ant`  •  **expected**: `':ant'`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. This was atop the hilltop.

A wooden sign nailed to a stalk near the hilltop carried a puzzle. The riddle
was simple: it asked the reader to evaluate `:ant`. Chirp
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of the keyword :ant was to put it in the
REPL.

Question: write a Clojure expression for the value of :ant.

---

{"tool_calls":[{"name":"eval","args":{"form":":ant"}}]}
```

## G1-08: Characters

### G1-08 record 1

**form**: `\a`  •  **expected**: `'a'`

```
Two creatures of the meadow approached the coming winter very differently. It happened on the hilltop.

At the edge of a stockpile atop the hilltop, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `\a`
first would win the right to set the next day's count.
Tic the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the character \a.

What Clojure form computes the value of \a? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\a"}}]}
```

### G1-08 record 2

**form**: `\a`  •  **expected**: `'a'`

```
Two creatures of the meadow approached the coming winter very differently. All this took place by the garden.

Skip the grasshopper chalked a wager on a flat slate by the garden: whoever
predicted the result of `\a` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the character \a.

Question: write a Clojure expression for the value of \a.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"\\a"}}]}
```

### G1-08 record 3

**form**: `\a`  •  **expected**: `'a'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. This was at the edge of the forest.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `\a` first would win the right to
choose the next song. Bit the ant, her eyes always on the path, said it was easier
to ask the REPL about the character \a than to argue.

Write a form whose evaluation gives the value of \a.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"\\a"}}]}
```

### G1-08 record 4

**form**: `\a`  •  **expected**: `'a'`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

At the edge of a stockpile near the farm, Chirp the grasshopper sketched a
small wager into the dust: whoever guessed the result of `\a`
first would win the right to set the next day's count.
Tic the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the character \a.

Question: write a Clojure expression for the value of \a.

---

{"tool_calls":[{"name":"eval","args":{"form":"\\a"}}]}
```

### G1-08 record 5

**form**: `\a`  •  **expected**: `'a'`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Chirp the grasshopper said,
with a smug grin. "Anyone can see what the character \a comes to."
Toc the ant, who at the edge of the garden had grown used to such claims, asked
him to actually write the form `\a` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of \a.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"\\a"}}]}
```

## G1-09: Symbols vs values

### G1-09 record 1

**form**: `(symbol? 'ant)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A small audience of meadow creatures had gathered at the edge of the forest to watch
Chirp the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the predicate (symbol? 'ant) and read out the form aloud:
`(symbol? 'ant)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes whether 'ant is a symbol.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'ant)"}}]}
```

### G1-09 record 2

**form**: `(symbol? 'ant)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

Toc the ant and Hum the grasshopper stopped at the edge of the meadow where someone had
written the predicate (symbol? 'ant) on a flat stone. Hum, as if the race were already won,
declared that they could see the answer at a glance.
Toc, without complaint, suggested they actually evaluate the form
`(symbol? 'ant)` in the REPL and read off whatever it returned.

Question: write a Clojure expression for whether 'ant is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'ant)"}}]}
```

### G1-09 record 3

**form**: `(symbol? 'ant)`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang. This was by the farm.

A small audience of meadow creatures had gathered in the farm to watch
Skip the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the predicate (symbol? 'ant) and read out the form aloud:
`(symbol? 'ant)`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives whether 'ant is a symbol.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'ant)"}}]}
```

### G1-09 record 4

**form**: `(symbol? 'ant)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the garden.

"There is no need to evaluate that," Skip the grasshopper said,
as if the race were already won. "Anyone can see what the predicate (symbol? 'ant) comes to."
Tic the ant, who near the garden had grown used to such claims, asked
her to actually write the form `(symbol? 'ant)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives whether 'ant is a symbol.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'ant)"}}]}
```

### G1-09 record 5

**form**: `(symbol? 'ant)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. It happened at the edge of the meadow.

Hum the grasshopper chalked a wager on a flat slate near the meadow: whoever
predicted the result of `(symbol? 'ant)` first would set the next day's
ration. Toc the ant, untroubled by what others thought, said it would be simpler to type
the form into the REPL than to bicker about the predicate (symbol? 'ant).

What Clojure form computes whether 'ant is a symbol? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'ant)"}}]}
```

## G1-10: Comments

### G1-10 record 1

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Bit the ant and Skip the grasshopper stopped near the woods where someone had
written the form (+ 1 2) followed by a comment on a flat stone. Skip, boasting at every turn,
declared that she could see the answer at a glance.
Bit, with steady, careful steps, suggested they actually evaluate the form
`(+ 1 2) ; sum of one and two` in the REPL and read off whatever it returned.

What Clojure form computes the result of (+ 1 2) ignoring the comment? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 2

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the garden: whoever
predicted the result of `(+ 1 2) ; sum of one and two` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the form (+ 1 2) followed by a comment.

Write a form whose evaluation gives the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 3

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today by the garden, the next entry
was the form (+ 1 2) followed by a comment. Chirp the grasshopper peered over
her shoulder at the form `(+ 1 2) ; sum of one and two` and asked what it
would come out to.

Write a form whose evaluation gives the result of (+ 1 2) ignoring the comment.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 4

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the farm.

Bit the ant had been trying to teach Skip the grasshopper how the REPL
works. "Look here," they said, pointing to the form (+ 1 2) followed by a comment.
"You hand the form `(+ 1 2) ; sum of one and two` to the runtime, and the runtime hands
you back what it evaluates to." Skip, her legs heavy from sprinting, agreed to
try.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

### G1-10 record 5

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. It happened at the edge of the farm.

"There is no need to evaluate that," Chirp the grasshopper said,
boasting at every turn. "Anyone can see what the form (+ 1 2) followed by a comment comes to."
Bit the ant, who in the farm had grown used to such claims, asked
him to actually write the form `(+ 1 2) ; sum of one and two` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the result of (+ 1 2) ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
```

## G1-11: Whitespace doesn't matter

### G1-11 record 1

**form**: `(+    1    2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. It happened in the meadow.

A small audience of meadow creatures had gathered in the meadow to watch
Chirp the grasshopper attempt to outwit Tic the ant at reading the
REPL. Tic pointed to the form (+ 1 2) with extra spaces and read out the form aloud:
`(+    1    2)`. The crowd waited to see who would correctly write the
form to submit.

Question: write a Clojure expression for the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 2

**form**: `(+    1    2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. This was near the forest.

Toc the ant and Skip the grasshopper stopped at the edge of the forest where someone had
written the form (+ 1 2) with extra spaces on a flat stone. Skip, as if the race were already won,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(+    1    2)` in the REPL and read off whatever it returned.

Write a form whose evaluation gives the result of the form.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 3

**form**: `(+    1    2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. This was at the edge of the forest.

"There is no need to evaluate that," Skip the grasshopper said,
puffed up with pride. "Anyone can see what the form (+ 1 2) with extra spaces comes to."
Bit the ant, who in the forest had grown used to such claims, asked
her to actually write the form `(+    1    2)` and
submit it to the REPL — just to be sure.

Question: write a Clojure expression for the result of the form.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 4

**form**: `(+    1    2)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Halfway through the morning's work, Hum the grasshopper blocked
Tic the ant's path in the woods and refused to step aside until someone
could prove what the form `(+    1    2)` evaluated to. Hum
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the form (+ 1 2) with extra spaces to the REPL. Whatever comes
back is the answer."

What Clojure form computes the result of the form? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

### G1-11 record 5

**form**: `(+    1    2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

"There is no need to evaluate that," Skip the grasshopper said,
swaggering through the underbrush. "Anyone can see what the form (+ 1 2) with extra spaces comes to."
Bit the ant, who by the garden had grown used to such claims, asked
her to actually write the form `(+    1    2)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the result of the form.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+    1    2)"}}]}
```

## G1-12: Parens group; they don't multiply

### G1-12 record 1

**form**: `(+ 2 3)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile atop the hilltop, Skip the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(+ 2 3)`
first would win the right to set the next day's count.
Toc the ant, stepping deliberately, said it was simpler to type the form into
the REPL than to argue about the form (+ 2 3).

Write a form whose evaluation gives the result of (+ 2 3).

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 2

**form**: `(+ 2 3)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Hum the grasshopper said,
puffed up with pride. "Anyone can see what the form (+ 2 3) comes to."
Bit the ant, who at the edge of the garden had grown used to such claims, asked
them to actually write the form `(+ 2 3)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the result of (+ 2 3).

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 3

**form**: `(+ 2 3)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened at the edge of the woods.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the woods, the next entry
was the form (+ 2 3). Hum the grasshopper peered over
her shoulder at the form `(+ 2 3)` and asked what it
would come out to.

Write a form whose evaluation gives the result of (+ 2 3).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 4

**form**: `(+ 2 3)`  •  **expected**: `5`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Skip the grasshopper said,
with great whoops of laughter. "Anyone can see what the form (+ 2 3) comes to."
Tic the ant, who in the garden had grown used to such claims, asked
her to actually write the form `(+ 2 3)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the result of (+ 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

### G1-12 record 5

**form**: `(+ 2 3)`  •  **expected**: `5`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. It happened near the forest.

A small audience of meadow creatures had gathered at the edge of the forest to watch
Chirp the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (+ 2 3) and read out the form aloud:
`(+ 2 3)`. The crowd waited to see who would correctly write the
form to submit.

Write a Clojure expression that computes the result of (+ 2 3).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 3)"}}]}
```

## G1-13: First arithmetic call

### G1-13 record 1

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile at the edge of the orchard, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(+ 1 2)`
first would win the right to set the next day's count.
Toc the ant, with steady, careful steps, said it was simpler to type the form into
the REPL than to argue about the form (+ 1 2).

Write a form whose evaluation gives the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 record 2

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Chirp the grasshopper said,
swaggering through the underbrush. "Anyone can see what the form (+ 1 2) comes to."
Tic the ant, who by the farm had grown used to such claims, asked
him to actually write the form `(+ 1 2)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 record 3

**form**: `(+ 1 2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. It happened atop the hilltop.

Halfway through the morning's work, Chirp the grasshopper blocked
Tic the ant's path on the hilltop and refused to step aside until someone
could prove what the form `(+ 1 2)` evaluated to. Chirp
called it impossible. Tic the ant, walking up at his usual
pace, simply said: "Submit the form (+ 1 2) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 record 4

**form**: `(+ 1 2)`  •  **expected**: `3`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

Chirp the grasshopper chalked a wager on a flat slate by the farm: whoever
predicted the result of `(+ 1 2)` first would set the next day's
ration. Tic the ant, without complaint, said it would be simpler to type
the form into the REPL than to bicker about the form (+ 1 2).

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-13 record 5

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

Bit the ant had been trying to teach Chirp the grasshopper how the REPL
works. "Look here," they said, pointing to the form (+ 1 2).
"You hand the form `(+ 1 2)` to the runtime, and the runtime hands
you back what it evaluates to." Chirp, her legs heavy from sprinting, agreed to
try.

Question: write a Clojure expression for the result of (+ 1 2).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

## G1-14: Nested call evaluation

### G1-14 record 1

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

With a twig, Skip the grasshopper marked out a wager at the edge of the forest: whoever
guessed the result of `(+ 1 (* 2 3))` first would win the right to
choose the next song. Toc the ant, stepping deliberately, said it was easier
to ask the REPL about the nested form (+ 1 (* 2 3)) than to argue.

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 record 2

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
Two creatures of the meadow approached the coming winter very differently.

At the edge of a stockpile by the woods, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(+ 1 (* 2 3))`
first would win the right to set the next day's count.
Toc the ant, without complaint, said it was simpler to type the form into
the REPL than to argue about the nested form (+ 1 (* 2 3)).

Write a form whose evaluation gives the result of (+ 1 (* 2 3)).

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 record 3

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate at the edge of the hilltop: whoever
predicted the result of `(+ 1 (* 2 3))` first would set the next day's
ration. Bit the ant, stepping deliberately, said it would be simpler to type
the form into the REPL than to bicker about the nested form (+ 1 (* 2 3)).

What Clojure form computes the result of (+ 1 (* 2 3))? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 record 4

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Chirp the grasshopper chalked a wager on a flat slate at the edge of the farm: whoever
predicted the result of `(+ 1 (* 2 3))` first would set the next day's
ration. Tic the ant, saying very little, said it would be simpler to type
the form into the REPL than to bicker about the nested form (+ 1 (* 2 3)).

Write a form whose evaluation gives the result of (+ 1 (* 2 3)).

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

### G1-14 record 5

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Chirp the grasshopper blocked
Toc the ant's path near the hilltop and refused to step aside until someone
could prove what the form `(+ 1 (* 2 3))` evaluated to. Chirp
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the nested form (+ 1 (* 2 3)) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the result of (+ 1 (* 2 3)).

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
```

## G1-15: Equality

### G1-15 record 1

**form**: `(= 1 1)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

"There is no need to evaluate that," Skip the grasshopper said,
with great whoops of laughter. "Anyone can see what the equality (= 1 1) comes to."
Bit the ant, who near the meadow had grown used to such claims, asked
her to actually write the form `(= 1 1)` and
submit it to the REPL — just to be sure.

Write a form whose evaluation gives the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 record 2

**form**: `(= 1 1)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

At the edge of a stockpile by the garden, Hum the grasshopper sketched a
small wager into the dust: whoever guessed the result of `(= 1 1)`
first would win the right to set the next day's count.
Toc the ant, her eyes always on the path, said it was simpler to type the form into
the REPL than to argue about the equality (= 1 1).

Write a form whose evaluation gives the value of (= 1 1).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 record 3

**form**: `(= 1 1)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently.

Hum the grasshopper chalked a wager on a flat slate near the meadow: whoever
predicted the result of `(= 1 1)` first would set the next day's
ration. Bit the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about the equality (= 1 1).

Write a form whose evaluation gives the value of (= 1 1).

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 record 4

**form**: `(= 1 1)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

With a twig, Hum the grasshopper marked out a wager in the forest: whoever
guessed the result of `(= 1 1)` first would win the right to
choose the next song. Tic the ant, with steady, careful steps, said it was easier
to ask the REPL about the equality (= 1 1) than to argue.

Question: write a Clojure expression for the value of (= 1 1).

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

### G1-15 record 5

**form**: `(= 1 1)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the garden.

Toc the ant and Skip the grasshopper stopped in the garden where someone had
written the equality (= 1 1) on a flat stone. Skip, with a smug grin,
declared that she could see the answer at a glance.
Toc, with steady, careful steps, suggested they actually evaluate the form
`(= 1 1)` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
```

## G1-16: Numeric predicates

### G1-16 record 1

**form**: `(zero? 0)`  •  **expected**: `True`

```
Two creatures of the meadow approached the coming winter very differently. All this took place at the edge of the farm.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today by the farm, the next entry
was the predicate (zero? 0). Hum the grasshopper peered over
her shoulder at the form `(zero? 0)` and asked what it
would come out to.

Write a form whose evaluation gives whether 0 is zero.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 record 2

**form**: `(zero? 0)`  •  **expected**: `True`

```
All summer long, the Ant worked while the Grasshopper sang.

Hum the grasshopper chalked a wager on a flat slate in the woods: whoever
predicted the result of `(zero? 0)` first would set the next day's
ration. Tic the ant, her eyes always on the path, said it would be simpler to type
the form into the REPL than to bicker about the predicate (zero? 0).

What Clojure form computes whether 0 is zero? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 record 3

**form**: `(zero? 0)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place by the woods.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today by the woods, the next entry
was the predicate (zero? 0). Chirp the grasshopper peered over
his shoulder at the form `(zero? 0)` and asked what it
would come out to.

Write a form whose evaluation gives whether 0 is zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 record 4

**form**: `(zero? 0)`  •  **expected**: `True`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

"There is no need to evaluate that," Chirp the grasshopper said,
boasting at every turn. "Anyone can see what the predicate (zero? 0) comes to."
Bit the ant, who near the forest had grown used to such claims, asked
him to actually write the form `(zero? 0)` and
submit it to the REPL — just to be sure.

Write a Clojure expression that computes whether 0 is zero.

---

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

### G1-16 record 5

**form**: `(zero? 0)`  •  **expected**: `True`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play. All this took place near the garden.

Halfway through the morning's work, Skip the grasshopper blocked
Bit the ant's path at the edge of the garden and refused to step aside until someone
could prove what the form `(zero? 0)` evaluated to. Skip
called it impossible. Bit the ant, walking up at their usual
pace, simply said: "Submit the predicate (zero? 0) to the REPL. Whatever comes
back is the answer."

Write a form whose evaluation gives whether 0 is zero.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(zero? 0)"}}]}
```

## G1-17: Printing vs returning

### G1-17 record 1

**form**: `42`  •  **expected**: `42`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place by the meadow.

Tic the ant had been keeping a small leather notebook of every form
he had successfully evaluated. Today in the meadow, the next entry
was the value 42. Skip the grasshopper peered over
his shoulder at the form `42` and asked what it
would come out to.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 2

**form**: `42`  •  **expected**: `42`

```
Two creatures of the meadow approached the coming winter very differently. All this took place in the forest.

A wooden sign nailed to a stalk near the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `42`. Hum
laughed, as if the race were already won, and declared it too easy. Bit said patiently
that the only way to be sure of the value 42 was to put it in the
REPL.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 3

**form**: `42`  •  **expected**: `42`

```
All summer long, the Ant worked while the Grasshopper sang. It happened in the orchard.

Toc the ant and Hum the grasshopper stopped in the orchard where someone had
written the value 42 on a flat stone. Hum, with great whoops of laughter,
declared that they could see the answer at a glance.
Toc, saying very little, suggested they actually evaluate the form
`42` in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 4

**form**: `42`  •  **expected**: `42`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Toc the ant had been keeping a small leather notebook of every form
she had successfully evaluated. Today in the garden, the next entry
was the value 42. Chirp the grasshopper peered over
her shoulder at the form `42` and asked what it
would come out to.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

### G1-17 record 5

**form**: `42`  •  **expected**: `42`

```
It is the way of the Ant to gather, and the way of the Grasshopper to play.

"There is no need to evaluate that," Hum the grasshopper said,
boasting at every turn. "Anyone can see what the value 42 comes to."
Toc the ant, who by the farm had grown used to such claims, asked
them to actually write the form `42` and
submit it to the REPL — just to be sure.

What Clojure form computes the value of 42? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
```

## G1-18: Errors are safe in the REPL

### G1-18 record 1

**form**: `(+ 1 2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

A wooden sign nailed to a stalk by the farm carried a puzzle. The riddle
was simple: it asked the reader to evaluate `(+ 1 2)`. Skip
laughed, puffed up with pride, and declared it too easy. Toc said patiently
that the only way to be sure of the form (+ 1 2) was to put it in the
REPL.

What Clojure form computes the result of (+ 1 2)? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 2

**form**: `(+ 1 2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang. All this took place near the farm.

Hum the grasshopper chalked a wager on a flat slate at the edge of the farm: whoever
predicted the result of `(+ 1 2)` first would set the next day's
ration. Bit the ant, with steady, careful steps, said it would be simpler to type
the form into the REPL than to bicker about the form (+ 1 2).

Write a form whose evaluation gives the result of (+ 1 2).

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 3

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.

Halfway through the morning's work, Hum the grasshopper blocked
Toc the ant's path in the farm and refused to step aside until someone
could prove what the form `(+ 1 2)` evaluated to. Hum
called it impossible. Toc the ant, walking up at her usual
pace, simply said: "Submit the form (+ 1 2) to the REPL. Whatever comes
back is the answer."

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 4

**form**: `(+ 1 2)`  •  **expected**: `3`

```
All summer long, the Ant worked while the Grasshopper sang.

With a twig, Skip the grasshopper marked out a wager atop the hilltop: whoever
guessed the result of `(+ 1 2)` first would win the right to
choose the next song. Tic the ant, stepping deliberately, said it was easier
to ask the REPL about the form (+ 1 2) than to argue.

Question: write a Clojure expression for the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```

### G1-18 record 5

**form**: `(+ 1 2)`  •  **expected**: `3`

```
Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper. All this took place in the garden.

A small audience of meadow creatures had gathered near the garden to watch
Hum the grasshopper attempt to outwit Toc the ant at reading the
REPL. Toc pointed to the form (+ 1 2) and read out the form aloud:
`(+ 1 2)`. The crowd waited to see who would correctly write the
form to submit.

Write a form whose evaluation gives the result of (+ 1 2).

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
```


---

**Grade 1 totals: 18 subjects, 90 records.**
