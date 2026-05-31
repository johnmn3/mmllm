# Metaphor demo — milkmaid curriculum
One canonical subject per metaphor family. For each, two renders are shown:

- **Story-scaffold render** — the example's authored `scenario` / `need` /
  `mapping` / `resolution` slots composed into a 5-act grounded story by the
  `_story()` template (Phase C framework). The metaphor *drives* the action.
- **Family-template render** — one of the family pool's generic templates, for
  contrast. Same example, no story slots used.

Coverage: 22 metaphor families. 412 of 509 examples across 216 subjects have
story-scaffold slots authored (Phase C complete). The remaining 97 are atom
subjects (form IS the lesson) or abstract-by-nature GOAL subjects.

---
## atom — G1-01 through G1-08: Literals

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For literal atoms, the form IS the answer. The user_msg shows the form as `{form_display}`; copy-from-prompt is the lesson. Story slots are not authored for these — the farmer shows the milkmaid the chalk mark on the pail and asks her to reproduce it.

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** apron-pocket (let-binding).

### Story-scaffold render

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid tucked the number 3 into her apron-pocket at the start of one stretch of the road — a private count, good only for this leg of the journey to market.

She needed to reach into the pocket at the next step and add 1 to the count, then let the pocket empty when the form ended.

`let` is the apron-pocket: it tucks `x = 3` into the pocket for the duration of the body. `(+ x 1)` draws from the pocket and adds 1. When the body ends, the pocket is put away and `x` ceases to exist.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, He composed the local binding and addition with the value tucked into the apron-pocket and submitted the form. The REPL reached into the pocket as the form directed:

the REPL returned 4 — the count from the pocket incremented by one, the pocket now set aside at the road's end.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Family-template render

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

She arrived at the village convinced she could bind a value of 3 to a local name x for one stretch, then return that value plus one
wherever she stood. Rowan did not argue. Instead, they wrote a
form that tucked the local binding and addition into the apron-pocket, used it in three different steps,
and then showed Bess the result. "This is the form's scope," they said.
"Step outside it, and the pocket is sewn shut. The binding exists only where the form breathes."

What Clojure form computes the running total after binding x to 3 and adding 1? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-07: fn — anonymous function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** pail-steps card (fn / defn / comp).

### Story-scaffold render

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid wrote a nameless card with one step: take the count and add one.

The buyer passed a count in and needed the result back.

`fn` is the nameless card: `[x]` is the input slot, `(+ x 1)` is the step. Passing a count runs it.

To create an anonymous function that adds 1 to its argument and apply it to 4, He wrote out the anonymous function call on the pail-steps card and submitted the form. The REPL ran the steps end to end:

The REPL returned the incremented count.

Question: write a Clojure expression for the result of applying an anonymous fn that adds 1 to its argument to the value 4.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

### Family-template render

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One noon, Bess arrived at the dairy with a wild pail-steps card that said: "Do step one.
Then, if the milk is sour, skip to step five. Otherwise, step two." They read it
and said, "Good — this recipe branches. It is still a form; it still the anonymous function call at the end.
But notice: each path through the card leads to a result. The form's logic unfolds as the steps
are read, just as the milkmaid's walk unfolds on the market road."

What Clojure form computes the result of applying an anonymous fn that adds 1 to its argument to the value 4? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

---

## basket — G2-17: Keyword as function for map lookup

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** market-basket (collections).

### Story-scaffold render

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer held a market-basket with two compartments: one labeled :hare held 1 coin, the other labeled :tortoise held 2 coins. She wanted to reach into the :hare compartment and find what was inside.

She needed to look up the value in the :hare compartment of her basket without opening all compartments.

The keyword lookup is the farmer's basket-compartment finder: the keyword :hare acts like a hand reaching into the map to find the labeled compartment and pull out what's inside.

To use the keyword :hare to look up a value in the map with keys :hare and :tortoise, He composed the keyword lookup for the market-basket and submitted the form. The REPL handed back the arrangement:

the REPL returned 1 — the value inside the :hare compartment of the basket.

Question: write a Clojure expression for the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
````

### Family-template render

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One afternoon, Bess arrived pulling two baskets. "This one has my guess," she said,
pointing at one. "This one is the form's result," she said, pointing at the other. The
baskets looked different — the form's basket had the compartments in a new order. They
nodded. "Exactly right. To use the keyword :hare to look up a value in the map with keys :hare and :tortoise, the keyword lookup does not alter the first basket. It builds
a second one, whose arrangement is what the form computed. That is the power of the market-basket —
change is creation, not destruction."

What Clojure form computes the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(:hare {:hare 1 :tortoise 2})"}}]}
````

---

## sieve — G4-16: into and conj on collections

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** milk-strainer (filter / HOFs).

### Story-scaffold render

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid set the milk-strainer over a fresh pail and poured the contents of a market list — three elements in order — through the strainer's mesh into a fresh vector-shaped container.

She needed to pass the list through the strainer rule into a fresh vector — each element flowing through in sequence, nothing lost, nothing added.

`into` is the milk-strainer over the pail: it pours each element of the source collection through the rule and collects them into the target container in order.

To convert a list containing 1, 2, and 3 into a vector, He composed building a vector from a list as the strainer's rule, poured the input through, and submitted the form. The REPL caught what passed the sieve:

the REPL returned the fresh vector with all three elements — the list had passed through the strainer and arrived in its new shape, intact.

Question: write a Clojure expression for the vector built from a list.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

### Family-template render

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, She poured milk through a strainer with no rule written. The strainer did
nothing — every drop fell away, and the fresh pail was empty. "The strainer is broken!" she
cried. They smiled and said, "No. The strainer requires a rule — a form that
building a vector from a list. Without the rule, the strainer cannot decide. Write the form that says 'pass this,
reject that,' and the fresh pail will fill. But she must write it — the farmer's form, not
the milkmaid's guess."

What Clojure form computes the vector built from a list? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

---

## notebook — G9-02: Why state at all

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** tally-slate by the dairy door (atom/ref).

### Story-scaffold render

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid hung a fresh tally-slate by the dairy door with the number 0 chalked at the top — the starting count for the day's deliveries. The first pail went out; the slate needed updating.

She needed to erase the old mark and chalk a new one — not replace the slate, but update it in place, as if the dairy door itself remembered.

`atom` is the tally-slate; `swap!` is the chalk-update: it reads the current mark, applies `inc` to get the next count, and chalks the new number without replacing the slate. `@` reads what the slate says now.

To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, He composed binding an atom to counter, atomically incrementing it, and dereferencing the result for the tally-slate and submitted the form. The REPL chalked the update on the slate:

the REPL read the slate and returned 1 — one delivery tallied, the slate faithfully updated after the first pail left the door.

Question: write a Clojure expression for the value after atomically swapping counter with inc and dereferencing.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

### Family-template render

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, three farmers arrived at the slate to update the count. Bess panicked — "Will the count
become a mess?" But they said no. "Each farmer submits a form for binding an atom to counter, atomically incrementing it, and dereferencing the result — a form
that reads the current slate, applies the change, and writes the result, atomically. The forms queue up.
One farmer's form completes, then the next, then the next. The count is always clean, always right. That is
the slate's promise: construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result safely, one atom at a time."

What Clojure form computes the value after atomically swapping counter with inc and dereferencing? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

---

## acorn — G1-13: First arithmetic call

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** coin-counting (arithmetic).

### Story-scaffold render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer set two small coin-piles on the tally table: one pile of a single copper, and another of two. She needed the total before she could mark the day's earnings on the tally-slate.

She needed a form that added the two piles together — not guessing, not daydreaming, but submitting the sum to the REPL and reading what came back.

`+` is the farmer's tally rule: it stacks all the given coin-piles into one and hands back the total. No pail-nodding, no guesswork — just the arithmetic result.

To add 1 and 2, He composed the addition and submitted the form. The REPL counted out the coins:

the REPL returned the total the farmer had tallied — three coins, exactly as the two piles combined.

Question: write a Clojure expression for the sum of 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One afternoon, She found a cache of coins hidden in the dairy and tried to guess
the fortune. "Surely I can see the total at a glance!" she cried. they
only shook their head and began sorting the coins into neat piles. "To add 1 and 2,
we must count — truly count. the addition is the form that ticks through each coin, one by one,
and tells the REPL what the total is. Not a dream, not a guess. A form, a count, a truth."

What Clojure form computes the sum of 1 and 2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## gate — G1-15: Equality

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** farmyard gate (boolean / and / or).

### Story-scaffold render

**form**: `(= 1 1)`  •  **expected**: `True`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid stood at the farmyard gate with a penny in each hand, wondering whether both coins were the same denomination. The gate opened only when both sides agreed.

She needed the gate rule — a check that compared both sides and opened the gate when they matched, kept it shut when they did not.

`=` is the gate rule: it compares both arguments and swings the gate open (`true`) when they are equal, holds it shut (`false`) when they differ.

To test whether 1 equals 1 with =, He composed the equality check and submitted the form. The REPL let the gate decide:

the REPL swung the gate open — both pennies matched, the condition was met, and `true` came back.

Question: write a Clojure expression for whether 1 equals 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

### Family-template render

**form**: `(= 1 1)`  •  **expected**: `True`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, They walked Bess through a series of gates on the path. The first
gate was open, the second was open, but the third gate's rule said 'closed.' "Here," they
said, pointing. "The form for the equality check must check every gate. The REPL will say 'blocked' —
because one gate stopped us. To test whether 1 equals 1 with =, every gate in the chain must say 'open.' Write the
form and let the REPL walk the chain with you."

What Clojure form computes whether 1 equals 1? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

---

## fork — G5-01: if

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** fork on the road (if / cond / case).

### Story-scaffold render

**form**: `(if true :a :b)`  •  **expected**: `':a'`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

On the road to market, the milkmaid reached a fork: the left lane led to the dairy buyer, the right lane to the grain merchant. The pail could only go one way.

She needed a condition to read the sign and send the pail down the correct lane — only one branch walked, the other left untouched.

`if` is the road fork: the form reads the condition, picks one branch, and the REPL walks only that branch. The other branch is never visited; the pail never splits.

To choose between :a and :b based on a true condition, He composed the conditional and submitted the form. The REPL took the right lane:

the REPL walked the left branch — the condition was true, the pail rolled down the chosen lane, and the other lane was never entered.

Question: write a Clojure expression for which of :a or :b is returned.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

### Family-template render

**form**: `(if true :a :b)`  •  **expected**: `':a'`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

On the way to market, Bess encountered three forks in quick succession. At the first, she
guessed the direction. At the second, she stumbled. At the third, she was lost.
They arrived and said, "For choose between :a and :b based on a true condition, write a form that is the conditional — a
series of forks, each checking a condition, each choosing a path. The form walks the right forks in the
right order. It never wavers, never guesses, never splits. Submit it, and the REPL brings you to market."

What Clojure form computes which of :a or :b is returned? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

---

## roadsign — G3-01: def — top-level binding

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** market-board (def / namespace / require).

### Story-scaffold render

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid had nailed a name-card labelled x to the market-board at the village square, with the price chalked beside it for all buyers to read.

Any buyer who walked up and read x from the board needed to receive the value that had been posted — the board had to hold the name permanently and return it on demand.

`def` is the act of nailing the name-card to the market-board: it posts x in the namespace so every caller can look it up. The second form reads x back off the board.

To bind x to 42 and return it, He composed the top-level binding and lookup and submitted the form. The REPL read the market-board and replied:

The board carried the name, and the REPL returned the posted value when x was looked up — the market-board had done its work.

Question: write a Clojure expression for the value of x after using def to bind x to 42.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

### Family-template render

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, They brought Bess to the market hall and showed her three
boards: one posted the butter price, one posted the cheese price, one posted the cream price. "See? Each
board is the top-level binding and lookup in a different location," they explained. "A buyer who needs butter
walks to that board. A buyer who needs cheese walks to that board. To bind x to 42 and return it, a form the top-level binding and lookup
a name or a reference where all who need it can find it. The market-board is the public shelf."

What Clojure form computes the value of x after using def to bind x to 42? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

---

## safetynet — G1-18: Errors are safe in the REPL

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** careful walk (try / catch / throw).

### Story-scaffold render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid had once stumbled on the road and learned her lesson: a steady, careful walk is the safety net. A spilled pail is a lesson — the journey still continues.

She needed to know that a form submitted to the REPL — even a wrong one — does not end the session. The REPL waits, patient, for the next submission.

The careful walk is the safety net: each form is one step; if the step stumbles, the REPL shows the error and holds steady. The pail may tip, but the milkmaid picks it up and walks on.

To add 1 and 2, He composed the addition and submitted the form. The REPL — pail balanced, walk steady — handed back the value:

the REPL returned the result — the step landed correctly, the pail stayed balanced, and the walk continued to market without crisis.

Question: write a Clojure expression for the result of adding 1 and 2.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One afternoon, Bess hurried down the path and tripped. The pail crashed, and the milk was lost.
She wept. But they gathered the pieces of the pail and showed her
the REPL: "Here is the practice meadow. Here, the addition — write the form carefully and submit it.
If it stumbles, the safety net catches it, and you know what went wrong. You try again. In the real meadow,
one stumble ends the day. In the REPL, a hundred stumbles are practice. Walk carefully. Let the REPL teach you."

What Clojure form computes the result of adding 1 and 2? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## scroll — G6-15: Namespace meta

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** market order slip (IO / metadata).

### Story-scaffold render

**form**: `(:doc (meta '\{:doc "steady wins"\} race))`  •  **expected**: `'steady wins'`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer had annotated a symbol called `race` with a slip of paper tucked into its metadata: a docstring recording the dairy's guiding principle. She needed to read that annotation back from the slip.

She needed to unwrap the market order — reach into the symbol's metadata, find the `:doc` key, and return the value written on the slip.

`meta` opens the order-slip envelope tied to the symbol; the `:doc` keyword reads the line on the slip labeled doc. The form retrieves the annotation, not the symbol itself.

To extract the :doc metadata value from a symbol with a docstring, He composed accessing the :doc metadata from a symbol and submitted the form. The REPL — slip in hand — completed the market order:

the REPL returned the docstring the farmer had tucked into the slip — the principle she had recorded for the day's dairy run.

Question: write a Clojure expression for the docstring value from a symbol's metadata.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '\\{:doc \"steady wins\"\\} race))"}}]}
````

### Family-template render

**form**: `(:doc (meta '\{:doc "steady wins"\} race))`  •  **expected**: `'steady wins'`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

She found an old market order slip in the barn, yellowed and creased. "Can this
still tell us what to do?" she asked. they took it and read the marks.
"Yes. This slip holds a record — even old records tell us what the buyer once wanted. To extract the :doc metadata value from a symbol with a docstring
with such a slip, we accessing the :doc metadata from a symbol the document itself. The scroll is a store of information that
outlasts the moment. We read it, and the past speaks."

What Clojure form computes the docstring value from a symbol's metadata? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '\\{:doc \"steady wins\"\\} race))"}}]}
````

---

## guild — G8-01: Why polymorphism

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** market guild (protocols / dispatch).

### Story-scaffold render

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The guild-master had posted a dispatch window at the dairy hall. Every farmer carried a guild-card stamped with her kind. One function name, `speak`, would read the card and send each farmer to the correct answer.

She needed to define the dispatch window — a `defn` named `speak` whose `cond` arms read each caller's stamp and return the matching reply without the guild-master deciding case-by-case.

`defn` names the window; `cond` is the roll-call board, one row per stamp. Each `=` test reads the stamp and returns the paired response on a match. `:else` is the catch-all placard for any card not listed.

To define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, He composed conditional dispatch on a tag and submitted the form. The REPL — checking the guild roll — dispatched to the right member:

the REPL registered the function without complaint — the dispatch window was installed and ready to route any caller who arrived with a guild-card.

Question: write a Clojure expression for the function definition.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

### Family-template render

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

They brought together five new farmers at the market square. "All of you will join the guild,"
they announced. "Your first rule: conditional dispatch on a tag when I call 'Deliver!' But each of you will
write your own form for conditional dispatch on a tag. The guild says what you promise; your form says how you keep it.
To define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, you must join the guild by showing conditional dispatch on a tag — your farm's unique answer to the
guild's universal call."

What Clojure form computes the function definition? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

---

## toolshed — G6-14: Import for host classes

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** neighbor's milking stool (host interop).

### Story-scaffold render

**form**: `(symbol? 'java.util.List)`  •  **expected**: `True`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The neighbor's toolshed held a milking stool labeled with a dotted Java class name — a borrowed tool from the adjacent farm. The milkmaid needed to confirm the label on the stool was a proper symbol before she could carry it to her dairy.

She needed to verify that the borrowed tool's dotted class name was recognized as a symbol — the dairy door would only accept tools whose labels passed the symbol check.

`symbol?` examines the borrowed tool's label — a quoted dotted class name — and confirms it is a symbol, just as it would be for any other qualified name on the neighbor's rack.

To test whether a Java class name written as a quoted symbol is a symbol, He composed testing whether a value is a symbol and submitted the form. The REPL — borrowing the neighbor's stool — returned:

the REPL confirmed the dotted class name was indeed a symbol, clearing the borrowed tool for use at the dairy.

Question: write a Clojure expression for whether a dotted Java class name is a symbol.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.List)"}}]}
````

### Family-template render

**form**: `(symbol? 'java.util.List)`  •  **expected**: `True`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

When Bess borrowed the neighbor's milking stool, They asked, "Do you know how the
stool was made?" she said no. "Then you cannot use it?" they asked. She
laughed. "Of course I can! I sit on it." they nodded. "Exactly. To test whether a Java class name written as a quoted symbol is a symbol, you testing whether a value is a symbol
— you use the neighbor's tool by name, and it works. You do not need to understand its timber or nails.
You need only know: this tool, called this way, does that thing."

What Clojure form computes whether a dotted Java class name is a symbol? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.List)"}}]}
````

---

## runnerahead — G9-10: Agent introduction

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** runner sent ahead (agent / future).

### Story-scaffold render

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer sent a swift runner ahead to the buyer's stall with a message: 'increment the day's count when you arrive.' She didn't wait for the runner to return — she kept milking while the runner moved.

She needed the runner to carry `inc` to the agent ahead; she needed to carry on with her chores; and then, when the sun reached its peak, she needed to read the runner's final answer.

`agent` is the runner; `send` dispatches the runner with the `inc` message; `await` waits at the gate for the runner to return; `@` reads the answer the runner brought back.

To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference, He composed agent, send, await, deref and submitted the form. The REPL waited at the gate for the runner to return:

the REPL read the agent's final tally — the runner had arrived, applied `inc`, and the count was waiting when the milkmaid came to collect it.

Question: write a Clojure expression for the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

### Family-template render

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

They sent three runners — one to the grain merchant, one to the cheese master, one to the
village council. "Each of you is agent, send, await, deref with a different message," they said.
"To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference, I will have three answers, not one. But I do not wait for all three at once. I check
each one when she is ready. If she checks too early, the runner has not
returned, and there is no answer yet. But the runners are working. Eventually, each will arrive."

What Clojure form computes the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

---

## rewriterule — G10-03: defmacro introduction

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** farmer rewrites the plan (macros).

### Story-scaffold render

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

Before the milkmaid could nod and spill the pail, the farmer rewrote her daydream: 'I will give you a shorthand, `my-when`, that expands into `if` before the runtime ever reads it.'

She needed a rule that would rewrite `(my-when true 1 2 3)` into `(if true (do 1 2 3))` at read-time — a template stamp, not a function call.

`defmacro` is the farmer's rewrite rule: it intercepts the form before evaluation, expands the shorthand into the full idiom, and hands the expanded form to the runtime. The runtime sees `if`, never `my-when`.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, He composed defining a conditional macro and invoking it and submitted the form. The REPL — expanding the rewrite first, then evaluating — returned:

the REPL evaluated the expanded form and returned the last body expression — the rewrite had run silently before the runtime arrived, and the result came back cleanly.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Family-template render

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

Three farmers arrived with three different ways to define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body. Each wrote a daydream form on a slip. But
They took all three slips and defining a conditional macro and invoking it — rewrote them all into the same efficient
steps before the work began. "Why?" the farmers asked. they replied, "Each of you dreamed differently,
but the dairy does not see dreams. It sees the rewritten form. Before anything runs, I rewrite all daydreams
into what actually happens. That is the farmer's power — the rewrite is the truth."

What Clojure form computes the value the rewritten if-do form returns when the test is true and the body has three expressions? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-10: Comments

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** chalk marks on dairy wall (comments).

### Story-scaffold render

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

Beside the dairy tally, the milkmaid had chalked a note: '; sum of one and two.' The note was for her own reference — the dairy buyer at market would never see the chalk wall.

She needed a way to leave a human-readable reminder beside the form without it affecting what the REPL computed or returned.

The semicolon `;` is the chalk mark: everything after it on the same line is scribe's shorthand, visible to the milkmaid but invisible to the runtime. The runtime reads only the form before the mark.

To add 1 and 2, with a single-semicolon trailing comment, He composed the addition with a trailing comment and submitted the form. The REPL read past the chalk marks and returned:

the REPL computed the form and returned the sum — the chalk note on the wall never crossed the dairy door, and the runtime never read it.

Question: write a Clojure expression for the result, ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

### Family-template render

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, Bess arrived to find a form with no chalk marks at all — just steps written in a jumble.
"Is this form broken?" she asked. They said, "The form works. It the addition with a trailing comment
correctly. But without chalk marks to guide the reader, no one knows why each step is there. To add 1 and 2, with a single-semicolon trailing comment,
we write the addition with a trailing comment to make the form's intention clear. The form itself will not change — only the reader's
understanding will. A good dairy wall has both milk and marks; a good form has both code and clarity."

What Clojure form computes the result, ignoring the comment? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** chalk mark vs milk inside (quote/symbol).

### Story-scaffold render

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid had chalked the word 'hare' on the outside of a pail — a name, not the milk inside. The farmer asked: is that chalk mark a symbol, a name-thing, or something else?

She needed a predicate that would read the chalk mark and say plainly whether it was a name or a value.

`symbol?` is the farmer's chalk-inspector: it reads the quoted name and answers `true` if the mark is a symbol — a written label — rather than a computed value.

To ask whether a quoted name is a symbol, using the symbol? predicate, He composed the symbol-predicate on a quoted name and submitted the form. The REPL — reading the pail, not the chalk — returned:

the REPL answered `true` — the chalk mark was a name, not the milk inside the pail, and the inspector confirmed it.

Question: write a Clojure expression for whether a quoted name is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

### Family-template render

**form**: `(symbol? 'hare)`  •  **expected**: `True`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One day, Bess arrived with a stack of pails, each chalked with a different name: "cream," "skim," "butter,"
"curds." she pointed at one and guessed, "This pail contains butter." They asked,
"Did you open it?" she said no. they said, "Then you know only the chalk mark. To
ask whether a quoted name is a symbol, using the symbol? predicate, the symbol-predicate on a quoted name lets you work with the marks — the names on the pails. The form you write
decides whether to return the chalk mark itself or to open the pail and take out the milk inside. Choose carefully:
are you reading the label or the contents?"

What Clojure form computes whether a quoted name is a symbol? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'hare)"}}]}
````

---

## sortingtable — G8-08: Multimethod defmulti

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** dairy sorting table (multimethods).

### Story-scaffold render

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The dairy had a sorting table: each pail arrived stamped with a species-tag. The table-master nailed a placard for `:hare` to one shelf and set the routing rule: read the `:species` stamp.

She needed to define the dispatch rule (`defmulti` reading `:species`) and one arm (`defmethod` for `:hare`), then route a pail and read where it landed.

`defmulti` carves the table with `pace` as the router and `:species` as the stamp key. `defmethod` pins the `:hare` placard. Calling `pace` with a stamped map routes the pail to the matching arm.

To build a sorting-table named pace that reads the :species stamp, add a :hare arm, then route a pail stamped :hare, He composed the multimethod and its first arm and submitted the form. The REPL routed the pail through the sorting table:

the REPL returned the value the `:hare` arm had posted — the sort had routed correctly and the pail landed exactly where the placard said.

Question: write a Clojure expression for the pace returned for a runner stamped :hare after the table routes to its arm.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Family-template render

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One morning, three batches arrived at the sorting table at once: cream, skim, and butter. Each had a different
stamp. They showed Bess the form that the multimethod and its first arm. She watched
as the form read the first batch's stamp, sent it to the cream shelf. Then it read the second batch's stamp, sent
it to the skim shelf. Then the third — to butter. "The table sorted all three, and each one went to the right
place," she said in wonder. they replied, "the multimethod and its first arm does not care how many
batches arrive. Each one is routed by its stamp. That is the power of the table — many stamps, same rules."

What Clojure form computes the pace returned for a runner stamped :hare after the table routes to its arm? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-02: deftype introduction

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** the pail itself (deftype / defrecord).

### Story-scaffold render

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer designed a custom pail called Pebble — a single-slot container meant to carry one attribute, color, to market. She then hammered a Pebble pail into shape and filled the color slot.

She needed to define the pail's shape (`deftype Pebble [color]`), build a concrete pail, then read back what was in the color slot — not guess what she put in.

`deftype` is the pail mold: it names the container and its labeled slot. `Pebble.` stamps the mold into a real pail. `.-color` is the slot-reader that reaches in and retrieves the value.

To define a type Pebble with a color field and then read the color field from an instance, He composed reading the color field of a Pebble instance and submitted the form. The REPL stamped the pail into shape:

the REPL handed back the contents of the color slot — exactly what the farmer had placed there when she hammered the pail.

Question: write a Clojure expression for the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

### Family-template render

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

One afternoon, They created two different kinds of pails. One reading the color field of a Pebble instance held milk,
date, and cow-name. The other held milk, volume, and destination. She looked at both and
asked, "Are these the same pail?" they said, "No. Each form reading the color field of a Pebble instance creates pails with
a different structure. The first pail remembers the cow. The second pail tracks the destination. Both are
pails, but they are defined by different forms. The form is the blueprint; the pails are the houses built
from that blueprint."

What Clojure form computes the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

---

## tallywalk — G2-20: Counting

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** walk to market counting coins (reduce).

### Story-scaffold render

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The farmer walked to market counting pails: one step per pail, one coin per step. She held a vector of three pails in her basket and needed the total count before she could enter the market gate.

She needed a tally that walked through the basket, counting one element per step, and returned the final number when the walk was done.

`count` is the tally-walk: it steps through every element in the collection exactly once, tallying one per step, and returns the total at the end of the path.

To count the elements in the vector containing 1, 2, and 3, He composed the count operation and submitted the form. The REPL walked the collection carrying the tally:

the REPL returned the final tally — one count per element, the walk complete, the total ready to show at the market gate.

Question: write a Clojure expression for the result of using count on the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

### Family-template render

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

She arrived at the market breathless. "How many coins do I have?" they asked.
she counted on her fingers, looking back at each milestone. "I picked up bags at
five milestones. I counted them all together..." Finally, she arrived at a number. they
smiled. "That is count the elements in the vector containing 1, 2, and 3 — you walked the path, tallied the coins, and produced a number. the count operation
does this form in code. The form walks the coin-bags and returns the final tally."

What Clojure form computes the result of using count on the vector containing 1, 2, and 3? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

---

## beadstring — G2-11: String concatenation with str

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** braiding cheesecloth (string ops).

### Story-scaffold render

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid had two short lengths of cheesecloth: one labeled "ab" and one labeled "cd." She needed to stitch them together end-to-end into one unbroken cloth for straining the morning milk.

She needed a braiding operation — join both lengths in order, left to right, with no gap or overlap between the two pieces.

`str` is the braiding peg: it takes the cloth-lengths in order and weaves them into one continuous thread. The first length leads; the second follows without pause.

To use str to splice the two-letter strings "ab" and "cd" into a single thread, He composed the string concatenation and submitted the form. The REPL braided the cheesecloth as the form said:

the REPL returned the joined cloth — four characters woven together in the order given, the seam invisible.

Question: write a Clojure expression for the result of using str to splice "ab" and "cd".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

### Family-template render

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

They held a long braided cheesecloth and measured it with their hands. "This braid
is twelve hands long," they said. She asked, "How do you know?" they
replied, "I counted each hand-span. the string concatenation — the form that tells us the braid's length. The form
examines the cloth from end to end and returns the number. The braid itself does not change. We only measure it."

What Clojure form computes the result of using str to splice "ab" and "cd"? Submit it via `eval`.

---

I write the form and let the REPL evaluate it.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"ab\" \"cd\")"}}]}
````

---

## circuit — G5-22: recur — first taste

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** the daily milking round (loop/recur).

### Story-scaffold render

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.

The milkmaid walked the daily milking circuit: five stations along the same path, starting with a tally of 1. At each station she multiplied the running tally by the station count, then moved one step closer to done.

She needed to walk the circuit without adding new ground — the same loop, five laps, each time stepping the tally forward and the counter down, until the counter reached zero.

`loop/recur` is the daily milking round: `n` is the station-counter that shrinks each lap, `acc` is the running product, and `recur` sends her back to the circuit's start without growing the path.

To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, He composed a factorial computation via loop and recur and submitted the form. The REPL looped the round without growing the trail:

the REPL returned the accumulated product of all five laps — the tally the milkmaid had built one station at a time.

Question: write a Clojure expression for the factorial of 5 computed by walking a circuit.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Family-template render

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly. All this took place on the road.

They showed Bess a form that a factorial computation via loop and recur — a loop that milked each cow in turn, then
looped back to the first cow to milk it again. "The form does not climb a hill of calls," they said.
"It walks the circuit: milk cow one, milk cow two, milk cow three, back to cow one. Each lap is like the milkmaid's
morning round — the same steps, no height gained. To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, use a factorial computation via loop and recur and the form will loop
without growing the call stack."

What Clojure form computes the factorial of 5 computed by walking a circuit? Submit it via `eval`.

---

I submit the form to the REPL via the eval tool.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

