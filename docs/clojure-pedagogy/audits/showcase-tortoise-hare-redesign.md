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
12-template `_GOAL_SUBPLOTS` (or 8-template `_SHARED_SUBPLOTS`
for atoms) — to show that the same subject renders many ways.
Four of the 12 goal templates carry actual fable beats: Hare
hurries and stumbles; Tortoise writes the form patiently and
the REPL returns the value the steady way. The lesson lands
inside the prompt rather than being a backdrop to it.

---

## G1-01 — Eval as substitution

_L1 atom — a literal evaluates to itself_  •  **atom** — form-display intentional

**form**: `42`  •  **expected**: `42`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

A small audience of forest creatures had gathered at the edge of the meadow to watch
Whisker the hare attempt to outwit Mossback the tortoise at reading the REPL.
Mossback pointed to the value 42 and read out the form aloud:
`42`. The crowd waited to see who would correctly write
the form to submit.

Write a form whose evaluation gives the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-07 — Keywords

_L1 atom — a keyword evaluates to itself_  •  **atom** — form-display intentional

**form**: `:hare`  •  **expected**: `':hare'`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Shelly the tortoise had been trying to teach Bramble the hare how the REPL
works. "Look here," she said, pointing to
the keyword :hare. "You hand the form `:hare` to the runtime, and
the runtime hands you back what it evaluates to." Bramble, weary from the morning's effort,
agreed to try.

Write a Clojure expression that computes the value of :hare.

---

{"tool_calls":[{"name":"eval","args":{"form":":hare"}}]}
````

---

## G1-09 — Symbols vs values

_first non-atom: predicate/equality on quoted symbols_  •  **goal** — no form leak

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"There is no challenge here," Hopper the hare said, with great whoops of laughter.
"Anyone could ask whether a quoted name is a symbol, using the symbol? predicate without thinking." Mossback the tortoise,
who by the orchard had grown used to such claims, asked him to
actually write the symbol-predicate on a quoted name, then submit it to the REPL —
just to be sure.

Question: write a Clojure expression for whether a quoted name is a symbol.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## G1-13 — First arithmetic call

_L2 application — first arithmetic call_  •  **goal** — no form leak

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Shelly the tortoise kept a small leather notebook of every goal
she had translated into a Clojure form. Today near the woods,
the next entry was a goal: add 1 and 2. Shelly sat with pen in
hand, ready to compose the addition, then let the REPL
confirm the value.

Write a form whose evaluation gives the sum of 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## G1-14 — Nested call evaluation

_L2 application — nested evaluation_  •  **goal** — no form leak

**form**: `(+ 1 (* 2 3))`  •  **expected**: `7`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place at the edge of the meadow.

"You always insist on writing it out," Pip the hare complained,
puffed up with pride. "I can see the answer from here." Shelly the tortoise
shook her head slowly. "To add 1 to the product of 2 and 3, the eye is
no help — only the form is. Watch." She wrote
the nested computation in careful strokes, submitted it to the REPL,
and let the returned value speak for itself. Pip, with legs heavy from sprinting,
admitted that this time, again, the patient way had carried the
day.

Write a form whose evaluation gives the sum of 1 with the product of 2 and 3.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 (* 2 3))"}}]}
````

---

## G2-01 — Multi-arg arithmetic

_multi-arg arithmetic_  •  **goal** — no form leak

**form**: `(+ 1 2 3 4)`  •  **expected**: `10`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

"You always insist on writing it out," Whisker the hare complained,
puffed up with pride. "I can see the answer from here." Shelly the tortoise
shook her head slowly. "To add 1, 2, 3, and 4, the eye is
no help — only the form is. Watch." She wrote
the multi-arg sum in careful strokes, submitted it to the REPL,
and let the returned value speak for itself. Whisker, lulled by the gentle wind,
admitted that this time, again, the patient way had carried the
day.

Write a form whose evaluation gives the sum of 1, 2, 3, and 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2 3 4)"}}]}
````

---

## G2-13 — and / or — short circuit, return values

_and/or short-circuit, return values_  •  **goal** — no form leak

**form**: `(and true true)`  •  **expected**: `True`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.

Halfway through the race, Hopper the hare stopped in the woods and refused
to continue until someone could test true and true with the and operator with a Clojure form.
Hopper called the goal impossible. Shelly the tortoise, walking up at
her usual pace, simply said: "Compose the logical and;
submit it. Whatever comes back is the answer."

Write a Clojure expression that computes the result of using and on true and true.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G2-15 — Falsey values: only false and nil

_falsey rule (only false and nil are falsey)_  •  **goal** — no form leak

**form**: `(if 0 1 0)`  •  **expected**: `1`

````text
It was well known among the animals that the Hare boasted of his speed at every chance. It happened near the hilltop.

A small audience of forest creatures had gathered at the edge of the hilltop to watch
Bramble the hare attempt to outwit Shelly the tortoise at writing the
right form. The challenge: use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch). Shelly reminded the
crowd that what mattered was writing the if conditional with zero as condition carefully,
then submitting it to the REPL — not guessing aloud at the
answer.

What Clojure form computes the result of if with condition 0, then-branch 1, else-branch 0? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(if 0 1 0)"}}]}
````

---

## G2-21 — String length and substring

_string length and substring_  •  **goal** — no form leak

**form**: `(count "tortoise")`  •  **expected**: `8`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Shelly the tortoise had been teaching Pip the hare how to translate a
goal into a Clojure form. "If you want to count the characters in the string tortoise," she
said, "you write the count of characters in a string; submit that to the REPL, and it
hands you back the value." Pip, yawning at the soft moss, agreed to try
writing it.

Write a form whose evaluation gives the result of using count on the string tortoise.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count \"tortoise\")"}}]}
````

---

## G3-03 — let — local binding

_let local binding_  •  **goal** — no form leak

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.

Shelly the tortoise kept a small ledger in the garden where every meaningful
quantity got its own name. She pointed to today's
entry, which required bind x to 3 and add 1 to it. She would write
the local binding and addition and let the REPL confirm.

Write a form whose evaluation gives adding 1 to x after binding x locally to 3 via let.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## G4-08 — assoc — map update

_assoc — map update_  •  **goal** — no form leak

**form**: `(assoc {:a 1} :b 2)`  •  **expected**: `{':a': 1, ':b': 2}`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. All this took place by the woods.

Halfway through the race, Bramble the hare stopped by the woods and refused
to continue until someone could associate the key :b with value 2 onto a map binding :a to 1 with a Clojure form.
Bramble called the goal impossible. Slowpoke the tortoise, walking up at
his usual pace, simply said: "Compose the assoc operation;
submit it. Whatever comes back is the answer."

Question: write a Clojure expression for the map after using assoc to add the key :b with value 2.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:a 1} :b 2)"}}]}
````

---

## G5-12 — reduce

_reduce — fold over a sequence_  •  **goal** — no form leak

**form**: `(reduce + [1 2 3 4])`  •  **expected**: `10`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Mossback the tortoise had been teaching Pip the hare how to translate a
goal into a Clojure form. "If you want to fold + over the vector containing 1, 2, 3, and 4, summing them," he
said, "you write the fold operation; submit that to the REPL, and it
hands you back the value." Pip, with legs heavy from sprinting, agreed to try
writing it.

Write a form whose evaluation gives the sum produced by reducing + over the vector containing 1, 2, 3, and 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 2 3 4])"}}]}
````

---

## G6-03 — require

_require — pulling code in_  •  **goal** — no form leak

**form**: `(clojure.string/upper-case "hare")`  •  **expected**: `'HARE'`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter. This was near the hilltop.

Hopper the hare and Slowpoke the tortoise stopped at the edge of the hilltop to settle a small
puzzle. Hopper wanted to call the uppercasing function from clojure.string on a test string. Hopper, puffed up with pride, declared
that he could write the form for it without thinking.
Slowpoke, with eyes always on the path, suggested he actually write
calling a fully-qualified string function carefully — and then let the REPL confirm what
the value really was.

Write a Clojure expression that computes the uppercase form of the string hare produced by clojure.string/upper-case.

---

I use the fully-qualified name to reach the var.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"hare\")"}}]}
````

---

## G7-02 — try / catch

_try / catch_  •  **goal** — no form leak

**form**: `(try (/ 1 0) (catch Exception e -1))`  •  **expected**: `-1`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.

Hopper the hare and Shelly the tortoise stopped by the woods to settle a small
puzzle. Hopper wanted to divide 1 by 0, catch the resulting ArithmeticException, return a numeric code. Hopper, with great whoops of laughter, declared
that he could write the form for it without thinking.
Shelly, with eyes always on the path, suggested he actually write
the handler for a division-by-zero error carefully — and then let the REPL confirm what
the value really was.

What Clojure form computes what the catch clause returns when ArithmeticException is caught? Submit it via `eval`.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -1))"}}]}
````

---

## G8-04 — Protocol definition

_Protocol definition_  •  **goal** — no form leak

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Slowpoke the tortoise kept a small leather notebook of every goal
he had translated into a Clojure form. Today on the hilltop,
the next entry was a goal: define a protocol named Pace with one method speed that takes a single argument this. Slowpoke sat with pen in
hand, ready to compose a protocol definition, then let the REPL
confirm the value.

Write a Clojure expression that computes whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G9-03 — Atom introduction

_Atom — coordinated mutable state_  •  **goal** — no form leak

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.

Halfway through the race, Whisker the hare stopped along the road and refused
to continue until someone could construct an atom holding 0, atomically swap it by applying inc, and dereference the result with a Clojure form.
Whisker called the goal impossible. Mossback the tortoise, walking up at
his usual pace, simply said: "Compose atom, swap, and deref;
submit it. Whatever comes back is the answer."

What Clojure form computes the value returned by dereferencing a after defining a as an atom holding 0 and swapping it via inc? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G10-03 — defmacro introduction

_defmacro introduction_  •  **goal** — no form leak

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. All this took place by the forest.

Bramble the hare insisted at the edge of the forest that macros were the same as functions.
Shelly the tortoise, untroubled by what others thought, sketched defining a conditional macro and invoking it on a
strip of bark. "The difference," she said, "is in what
we're trying to accomplish: define a macro named my-when that takes a test and body expressions, then invoke it. Write the form and let the
runtime tell us exactly what it does."

What Clojure form computes the value returned when my-when expands to an if-do block that runs the body with test true? Submit it via `eval`.

---

I write the macro form and let the runtime evaluate or expand it.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax

_Method call syntax_  •  **goal** — no form leak

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk. This was near the woods.

A wooden sign nailed to a tree by the woods carried a small puzzle. The
challenge was simple: call the host method toUpperCase on the string abc. Bramble laughed, puffed up with pride, and
declared it too easy. Mossback said patiently that the only way
to be sure of the host method toUpperCase was to write the form and put it
in the REPL — not to guess at the value from the goal alone.

What Clojure form computes the uppercase form of the string abc produced by the host method toUpperCase via dot-prefix syntax? Submit it via `eval`.

---

I use the dot or slash form for the host method, then submit.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G12-01 — Transducers introduction

_Transducers introduction_  •  **goal** — no form leak

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either. This was along the road.

"This is nothing," Pip the hare scoffed, swaggering through the underbrush. "I can
use the map-inc transducer with into to increment the vector containing 1, 2, 3 in my sleep." Pip grabbed a stick and dashed off a
few characters in the dust — but a paren went missing, an operand
fell out of place, and the form did not even read as Clojure.
Slowpoke the tortoise, with eyes always on the path, had already written
the map-inc transducer applied via into on a flat stone, neat and unhurried, and
submitted it to the REPL. The value came back as quietly as
he had written. The hares of the meadow looked
between the two slates: only his had run.

What Clojure form computes the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3? Submit it via `eval`.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

