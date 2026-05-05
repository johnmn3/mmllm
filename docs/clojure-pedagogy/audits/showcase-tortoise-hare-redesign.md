# Tortoise-Hare — goal-style redesign showcase

This doc shows the post-redesign tortoise-hare curriculum end
to end. Two kinds of subject coexist:

- **Atom subjects** (G1-01..08): the form IS the answer (a
  literal evaluates to itself). The user_msg DOES show the
  form (`{form_display}`); copy-from-prompt is the lesson.
  The model learns 'submit the literal value the prompt shows'.

- **Goal subjects** (everything else): the user_msg shows a
  plain-English `{goal_text}` and an abstract `{concept_phrase}`
  but **never the literal form**. The model must produce the
  form from the goal description alone.

Each row below is one record sampled at a per-subject seed,
so successive rows pick different subplot templates from the
8-template `_GOAL_SUBPLOTS` (or 8-template `_SHARED_SUBPLOTS`
for atoms) — to show that the same subject renders many ways.

---

## G1-01 — Eval as substitution

_L1 atom — a literal evaluates to itself_  •  **atom** — form-display intentional

**form**: `42`  •  **expected**: `42`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Pip the hare chalked a wager on a flat stone at the edge of the forest: whoever
predicted the result of `42` would set the next race's
distance. Shelly the tortoise, without complaint, said it would be simpler
to type the form into the REPL than to bicker about the value 42.

What Clojure form computes the value of 42? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-07 — Keywords

_L1 atom — a keyword evaluates to itself_  •  **atom** — form-display intentional

**form**: `:hare`  •  **expected**: `':hare'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

"There is no need to evaluate that," Bramble the hare said, as if the race were already won.
"Anyone can see what the keyword :hare comes to." Mossback the tortoise, who
atop the hilltop had grown used to such claims, asked her to actually
write the form `:hare` and submit it to the REPL — just to be
sure.

Write a Clojure expression that computes the value of :hare.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
````

---

## G1-09 — Symbols vs values

_first non-atom: predicate/equality on quoted symbols_  •  **goal** — no form leak

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Slowpoke the tortoise had been teaching Whisker the hare how to translate a
goal into a Clojure form. "If you want to ask whether a quoted name is a symbol, using the symbol? predicate," he
said, "you write the symbol-predicate on a quoted name and submit it; the REPL hands you
back the value." Whisker, lulled by the gentle wind, agreed to try writing it.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## G1-13 — First arithmetic call

_L2 application — first arithmetic call_  •  **goal** — no form leak

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Halfway through the race, Bramble the hare stopped by the garden and refused
to continue until someone could write a form to add 1 and 2.
Bramble called the goal impossible. Slowpoke the tortoise, walking up at
his usual pace, simply said: "Write the addition
and submit it. Whatever comes back is the answer."

What Clojure form computes the sum of 1 and 2? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G1-14 — Nested call evaluation

_L2 application — nested evaluation_  •  **goal** — no form leak

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened by the garden.

Pip the hare and Mossback the tortoise stopped near the garden to settle a small
puzzle. Pip wanted to add 1 to the product of 2 and 3. Pip, swaggering through the underbrush, declared
that they could write the form for it without thinking.
Mossback, saying very little, suggested they actually write
the nested computation carefully and let the REPL confirm what it returned.

Question: write a Clojure expression for the sum of 1 with the product of 2 and 3.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
````

---

## G2-01 — Multi-arg arithmetic

_multi-arg arithmetic_  •  **goal** — no form leak

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A small audience of forest creatures had gathered in the orchard to watch
Bramble the hare attempt to outwit Mossback the tortoise at writing the
right form. The challenge: add 1, 2, 3, and 4. Mossback reminded the
crowd that what mattered was the multi-arg sum, written carefully
and submitted to the REPL.

Write a Clojure expression that computes the sum of 1, 2, 3, and 4.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
````

---

## G2-13 — and / or — short circuit, return values

_and/or short-circuit, return values_  •  **goal** — no form leak

**form**: `(and true true)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"There is no challenge here," Hopper the hare said, with great whoops of laughter.
"To test true and true with the and operator is something anyone could write." Mossback the tortoise,
who near the road had grown used to such claims, asked him to
actually write the logical and and submit it to the REPL — just to
be sure.

Write a form whose evaluation gives the result of true and true.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G2-15 — Falsey values: only false and nil

_falsey rule (only false and nil are falsey)_  •  **goal** — no form leak

**form**: `(if 0 1 0)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Halfway through the race, Pip the hare stopped at the edge of the orchard and refused
to continue until someone could write a form to write an if where the condition is 0, the then-branch is 1, and the else-branch is 0.
Pip called the goal impossible. Slowpoke the tortoise, walking up at
his usual pace, simply said: "Write the if conditional with zero as condition
and submit it. Whatever comes back is the answer."

Write a form whose evaluation gives which branch the if takes when the condition is 0.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 1 0)"}}]}
````

---

## G2-21 — String length and substring

_string length and substring_  •  **goal** — no form leak

**form**: `(count "tortoise")`  •  **expected**: `8`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Bramble the hare stopped atop the hilltop and refused
to continue until someone could write a form to count the characters in the string tortoise.
Bramble called the goal impossible. Slowpoke the tortoise, walking up at
his usual pace, simply said: "Write the count of characters in a string
and submit it. Whatever comes back is the answer."

Write a Clojure expression that computes the length of an eight-letter string.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
````

---

## G3-03 — let — local binding

_let local binding_  •  **goal** — no form leak

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
It was well known among the animals that the Hare boasted of his speed at every chance.

A small audience of forest creatures had gathered at the edge of the orchard to watch
Pip the hare attempt to outwit Shelly the tortoise at writing the
right form. The challenge: bind x to 3 and add 1 to it. Shelly reminded the
crowd that what mattered was the local binding and addition, written carefully
and submitted to the REPL.

What Clojure form computes the result of adding 1 to the bound x? Submit it via `eval`.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## G4-08 — assoc — map update

_assoc — map update_  •  **goal** — no form leak

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Halfway through the race, Pip the hare stopped by the forest and refused
to continue until someone could write a form to associate the key :b with value 2 onto a map binding :a to 1.
Pip called the goal impossible. Mossback the tortoise, walking up at
his usual pace, simply said: "Write the assoc operation
and submit it. Whatever comes back is the answer."

Write a form whose evaluation gives the map after update.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## G5-12 — reduce

_reduce — fold over a sequence_  •  **goal** — no form leak

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. All this took place in the forest.

A wooden sign nailed to a tree in the forest carried a small puzzle. The
challenge was simple: fold + over the vector containing 1, 2, 3, and 4, summing them. Whisker laughed, with a smug grin, and
declared it too easy. Mossback said patiently that the only way to
be sure of the fold operation was to write the form and put it in the
REPL.

What Clojure form computes the sum? Submit it via `eval`.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## G6-03 — require

_require — pulling code in_  •  **goal** — no form leak

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was by the garden.

Mossback the tortoise kept a small leather notebook of every goal
he had translated into a Clojure form. Today at the edge of the garden,
the next entry was a goal: call the uppercasing function from clojure.string on a test string. Mossback sat with pen in
hand, ready to write calling a fully-qualified string function and let the REPL confirm.

Question: write a Clojure expression for the result of calling a string transformation function.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## G7-02 — try / catch

_try / catch_  •  **goal** — no form leak

**form**: `(try (/ 1 0) (catch Exception e :caught))`  •  **expected**: `':caught'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Hopper the hare stopped by the forest and refused
to continue until someone could write a form to divide 1 by 0 and catch the resulting exception, returning a keyword.
Hopper called the goal impossible. Shelly the tortoise, walking up at
her usual pace, simply said: "Write the handler for a division-by-zero error
and submit it. Whatever comes back is the answer."

Write a Clojure expression that computes what the handler returns when division by zero occurs.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e :caught))"}}]}
````

---

## G8-04 — Protocol definition

_Protocol definition_  •  **goal** — no form leak

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled. It happened at the edge of the forest.

Hopper the hare and Mossback the tortoise stopped near the forest to settle a small
puzzle. Hopper wanted to define a protocol named Pace with one method speed that takes a single argument this. Hopper, swaggering through the underbrush, declared
that he could write the form for it without thinking.
Mossback, without complaint, suggested he actually write
a protocol definition carefully and let the REPL confirm what it returned.

Question: write a Clojure expression for whether it was established.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G9-03 — Atom introduction

_Atom — coordinated mutable state_  •  **goal** — no form leak

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

A wooden sign nailed to a tree in the orchard carried a small puzzle. The
challenge was simple: construct an atom holding 0, atomically swap it by applying inc, and dereference the result. Bramble laughed, swaggering through the underbrush, and
declared it too easy. Mossback said patiently that the only way to
be sure of constructing an atom holding 0, atomically swapping by applying inc, and dereferencing was to write the form and put it in the
REPL.

Question: write a Clojure expression for the value after atomically swapping a by applying inc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G10-03 — defmacro introduction

_defmacro introduction_  •  **goal** — no form leak

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Shelly the tortoise had been teaching Whisker the hare how to translate a
goal into a Clojure form. "If you want to define a macro named my-when that takes a test and body expressions, then invoke it," she
said, "you write defining a conditional macro and invoking it and submit it; the REPL hands you
back the value." Whisker, drowsy from the warm sun, agreed to try writing it.

Write a form whose evaluation gives the value produced by calling the macro.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax

_Method call syntax_  •  **goal** — no form leak

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Mossback the tortoise had been teaching Whisker the hare how to translate a
goal into a Clojure form. "If you want to call the host method toUpperCase on the string abc," he
said, "you write the host method toUpperCase and submit it; the REPL hands you
back the value." Whisker, drowsy from the warm sun, agreed to try writing it.

Write a form whose evaluation gives the uppercased result.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G12-01 — Transducers introduction

_Transducers introduction_  •  **goal** — no form leak

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was near the hilltop.

Halfway through the race, Whisker the hare stopped at the edge of the hilltop and refused
to continue until someone could write a form to use the map-inc transducer with into to increment the vector containing 1, 2, 3.
Whisker called the goal impossible. Mossback the tortoise, walking up at
his usual pace, simply said: "Write the map-inc transducer applied via into
and submit it. Whatever comes back is the answer."

Write a form whose evaluation gives the result of incrementing elements from the vector.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

