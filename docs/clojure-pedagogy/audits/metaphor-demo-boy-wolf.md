# Metaphor demo — boy-wolf curriculum

One canonical subject per metaphor family. For each, two
renders are shown:

- **Story-scaffold render** — the example's authored
  `scenario` / `need` / `mapping` / `resolution` slots
  composed into a 5-act grounded story by the
  `_story()` template (Phase C framework).
- **Family-template render** — one of the family pool's
  generic templates, for contrast. Same example, no story
  slots used.

Polarity flipped from tortoise-hare: SHEPHERD is the
cautionary character (boasts, claims he just *knows*); ELDER
is the corrective voice (writes the form, lets the runtime
decide). Imagery is anchored in the boy-wolf valley setting.

---

## atom — G1-01: Eval as substitution

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For atoms (literals), the form IS the answer. The user_msg deliberately shows the form via `{form_display}`; copy-from-prompt is the lesson — submit the literal as-is.

**form**: `42`  •  **expected**: `42`

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will called down from a stone in the forest where someone had
chalked the value 42 on a flat board. Will, with great whoops of laughter,
declared he already knew what would come back. Robin,
saying very little, asked him to actually submit the form
`42` to the REPL — the village had stopped trusting answers
that weren't checked.

Write a Clojure expression that computes the value of 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** A small leather belt-pouch at the elder's hip. Whatever is tucked inside is held just for one stretch of watch; by the next fence-post the pouch is empty again. Mirrors `let`-binding scope.

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 3 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the local name x for that stretch of watch.

By the next fence-post she would want the running total — what x plus one more lamb came to. Past that post, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 1)`, x means 3; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, She composed the local binding and addition with the binding tucked safely into the belt-pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded 3, the +1 added a fourth lamb, and the running total stood at 4 — exactly what the next fence-post called for.

Write a Clojure expression that computes the running total after binding x to 3 and adding 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will, with great whoops of laughter, claimed he could just
shout the answer without bothering to check. Robin only
shook their head and reached for the belt-pouch. "When I
want to bind a value of 3 to a local name x for one stretch, then return that value plus one," they said, "I tuck the value into
the pouch and carry it just for the stretch where I need it. By the
next milestone the pouch is empty again." They composed
the local binding and addition, the binding tucked away inside the pouch, and
submitted the form to the REPL. The form came back with the answer
the shepherd had not even thought to check.

Write a Clojure expression that computes the running total after binding x to 3 and adding 1.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-07: fn — anonymous function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** A drill-card on the watchhouse wall — a named routine the village can shout for and run. Mirrors `defn`/`fn`: a named, reusable procedure with parameters.

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

On the watchhouse wall, Carol the elder had pinned a small drill-card with no name at the top — just the steps for what to do once an unnamed quantity arrived. Tom waited beside her with 4 strays the south flock had produced that morning.

The strays needed to be added to the running tally, but the village wanted a one-shot routine for it — no name to remember, no card to file, just the steps run this once.

An anonymous `fn` is exactly that: a drill-card with no posted name. It takes the quantity (the parameter), runs the listed step, and serves whatever the last step produces. The 4 strays go in; the routine adds one for the count adjustment.

To create an anonymous function that adds 1 to its argument and apply it to 4, She chalked the anonymous function call onto the drill-card and submitted the form. The REPL ran the routine end to end:

the card ran end-to-end and returned 5 — the adjusted count Carol would carry to the slate, no naming needed.

Write a Clojure expression that computes the result of applying an anonymous fn that adds 1 to its argument to the value 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will, with great whoops of laughter, insisted he could just
shout the answer rather than bother writing a drill-card. Robin
only smiled and reached for chalk and the watchhouse wall. "Recipes
on a drill-card are like the routines we follow," they said:
"the ingredients go at the head, the steps in order, and the last step
is what gets served." To create an anonymous function that adds 1 to its argument and apply it to 4, They chalked out
the anonymous function call on the card, submitted the form, and the REPL followed
the recipe and handed back the value the last step had produced.

Write a Clojure expression that computes the result of applying an anonymous fn that adds 1 to its argument to the value 4.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

---

## basket — G2-17: Keyword as function for map lookup

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** A wool-basket with named pouches inside (e.g., `:wolf`, `:flock`). Original sits untouched; a fresh basket comes back. Mirrors immutable collection updates.

**form**: `(:wolf {:wolf 1 :flock 2})`  •  **expected**: `1`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol's wool-basket sat by the watchhouse. It had two stitched pouches inside: one labeled `:wolf` holding 1 fleece from the south pasture, the other `:flock` holding 2 from the north's morning shearing.

Tom needed the count from the wolf-pouch alone. Reaching in and counting by hand risked spilling the basket; the village wanted a one-step lookup that named the pouch and got back its contents.

A keyword used as a function reaches into the basket and returns whatever is in the pouch labeled with that keyword. `:wolf` names the pouch; the basket gives back the count it holds.

To , She composed the form (:wolf {:wolf 1 :flock 2}) for the wool-basket and submitted the form. The REPL handed back the arrangement:

the lookup returned 1 — the wolf-pouch's fleece count — without disturbing the rest of the basket.

Write a Clojure expression that computes the value (:wolf {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:wolf {:wolf 1 :flock 2})"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin pointed to a wool-basket in the forest. "Whatever I want to
do with what's inside," they said, "I read from the basket,
work the change, and the basket itself stays as it was — what I get
back is a fresh arrangement." To , They
composed the form (:wolf {:wolf 1 :flock 2}), submitted the form, and let the REPL handle
the basket exactly as the operation prescribed.

Write a Clojure expression that computes the value (:wolf {:wolf 1 :flock 2}) returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:wolf {:wolf 1 :flock 2})"}}]}
````

---

## sieve — G4-16: into and conj on collections

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** A fleece-comb / wool-screen. Fleeces poured through; only those passing the rule land in the basket below. Mirrors `map`/`filter`/transducers.

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol set up the fleece-comb at the watchhouse, an empty wool-basket beneath it. Three fleeces arrived from the morning shearing, threaded onto a rough cord ready to be fed through the comb.

The village wanted the fleeces moved into the basket in the order they came in, no rule applied — just a wholesale transfer from one container shape to another.

`into` pours the source through into the destination one item at a time. With an empty vector as the basket below and a list as the cord above, the runtime carries each fleece across, preserving the order.

To convert a list containing 1, 2, and 3 into a vector, She composed building a vector from a list as the fleece-comb's rule, poured the input through, and submitted the form. The REPL caught what passed:

the basket caught all three fleeces in the same order they had arrived — the morning's shearing settled into the day's container.

Write a Clojure expression that computes the vector built from a list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin held up a fleece-comb in the forest — a routine rule attached
at its teeth. "Whatever rule we hang on the comb," they said,
"the wool passes through one lock at a time: some are changed, some kept,
some dropped, depending on the rule." To convert a list containing 1, 2, and 3 into a vector, They
composed building a vector from a list as the comb's rule, poured the fleeces through,
submitted the form, and the REPL returned what the comb had let pass.

Write a Clojure expression that computes the vector built from a list.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

---

## notebook — G9-02: Why state at all

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** The watchhouse slate — the village's single shared running tally. Any shepherd can read or atomically update it. Mirrors `atom`/`swap!`/CAS.

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

The watchhouse slate sat on its stand inside the watchhouse, open for any shepherd to read. Carol had chalked a single tally at the top — 0 honest evaluations for the morning so far — and stepped back to begin the day's count.

Each time a form was honestly evaluated, the slate's tally needed to step up by one — and only one shepherd could be writing at a time, so the village's running count would never be lost or doubled.

An atom is exactly the watchhouse slate: a single shared tally that any shepherd can read or update, with the REPL guaranteeing the read-modify-write step is atomic. `swap!` is `read the page, apply the change, write it back`, all as one motion.

To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, She composed binding an atom to counter, atomically incrementing it, and dereferencing the result for the watchhouse slate and submitted the form. The REPL applied the update on the slate:

the slate now read 1 — the morning's first honest evaluation safely tallied, ready for the next.

Write a Clojure expression that computes the value after atomically swapping counter with inc and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

A watchhouse slate lay on the stone table, open for any shepherd to read.
"Atoms are like this slate," Robin said. "You can read the tally,
or — carefully — update it the atomic way: read the page, apply the change,
write it back, all in one motion that no other writer can step on." To
construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, they composed binding an atom to counter, atomically incrementing it, and dereferencing the result, submitted the form,
and let the REPL work the slate exactly as the form prescribed.

Write a Clojure expression that computes the value after atomically swapping counter with inc and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

---

## acorn — G1-13: First arithmetic call

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** Counting sheep at dawn / weighing fleeces / counting coins paid for wool. Mirrors arithmetic and comparisons.

**form**: `(+ 1 2)`  •  **expected**: `3`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At dawn, Tom had brought lambs back from the south pasture and Carol had brought lambs from the north. They stood at the fold counting together, the village's morning record waiting on them.

The combined morning tally needed to settle correctly before the day's work could begin — the village's records depended on exact arithmetic, no boasting and no fudging.

`+` adds its operands one after another and gives back the running total. The runtime carries the sum exactly — no shouting required.

To , She composed the form (+ 1 2) and submitted the form. The REPL counted out the answer:

the count came back — the morning's flock confirmed by the runtime, not by Tom's memory.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will eyed the grazing flock in the forest, with great whoops of laughter, and called out a
guess about how many sheep were there without bothering to count. Robin
simply began counting — to  required no eyeballing, only the form.
They composed the form (+ 1 2), submitted it to the REPL, and the
runtime returned the number that had been there all along, settling the matter
the patient way.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## gate — G1-15: Equality

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** Fold-gates — a chain of three stone gates from pasture to fold. The first closed gate stops the chain. Mirrors `and`/`or`/falsey rules.

**form**: `(= 1 1)`  •  **expected**: `True`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At the first fold-gate of the morning, Carol had two tally-marks carved into the post: one from yesterday's evening count, one from this morning's. Tom claimed the two had to differ — sheep, after all, never sat still.

Before the flock could pass through the gate and begin the day's grazing, the gate had to confirm whether the two marks agreed. A mistaken pass would corrupt the village ledger.

`=` compares its operands and answers whether they are the same. With both marks reading 1, the gate's predicate carries the comparison and returns the verdict — no opinion required.

To , She composed the equality (= 1 1) and submitted the form. The REPL let the fold-gates decide:

the gate opened — `=` returned true — and the village's count for the morning held without dispute.

Write a Clojure expression that computes the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will sprinted toward the fold-gates in the forest, with great whoops of laughter, certain
they would open for him. Robin slowed and watched: the
only way to know which way the gates would swing was to actually bring the value
to them. To , they composed the equality (= 1 1), submitted the
form, and the REPL — testing the gates properly — settled the matter, the gates
swinging exactly as the rule said, regardless of Will's guess.

Write a Clojure expression that computes the value of (= 1 1).

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

---

## fork — G5-01: if

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** Path-fork at the lookout — three paths fan out. The condition decides which arm the runner takes. Mirrors `if`/`cond`/`case`.

**form**: `(if true :a :b)`  •  **expected**: `':a'`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom stood at the path-fork on the lookout — three paths fanning out below, one to the village, one to the fold, one back to the pasture. Carol had set a small condition-stone at the fork: the day's question for the morning's runner.

The runner needed to take exactly one path. Tom wanted to shout both directions at once; Carol insisted the fork would settle which arm to take based on the condition's verdict.

`if` evaluates the condition and takes one of two arms. With the condition true, the fork's left arm is taken; the right arm's value is never produced. The runtime walks one path; the other simply isn't.

To choose between :a and :b based on a true condition, She composed the conditional and submitted the form. The REPL took the right path from the lookout:

the runner went left — `:a` was the value the fork carried back — and the morning's question settled without the second arm ever being walked.

Write a Clojure expression that computes which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will, with great whoops of laughter, called out which arm of the fork at the lookout
he was sure the runtime would take, without bothering to check
the condition. Robin only smiled: the only way to know is to evaluate
the condition. To choose between :a and :b based on a true condition, they composed the conditional,
submitted the form, and the REPL — checking the condition properly — returned
the value of the arm the form actually took.

Write a Clojure expression that computes which of :a or :b is returned.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

---

## roadsign — G3-01: def — top-level binding

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** The village notice-post at the crossroads. Carol pins named notices for the village to see. Mirrors `def`/namespaces/`require`.

**form**: `(do (def x 42) x)`  •  **expected**: `42`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol the elder stood at the village notice-post at the crossroads. She took her chalk and wrote the name x on the post, posting 42 sheep's worth of head-count beneath it for anyone walking past to see.

Every shepherd on the path needed that name and its count to mean the same thing all morning. Without the posted notice, x would have meant nothing the moment a different voice claimed otherwise.

`def` posts the name x on the notice-post alongside its bound count. The second expression looks the post up and reads back whatever was posted under that name — here, 42.

To bind x to 42 and return it, She composed the top-level binding and lookup and submitted the form. The REPL read the notice-post and replied:

the post returned exactly the count Carol had chalked, and the morning's record stood on village authority.

Write a Clojure expression that computes the value of x after using def to bind x to 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will, with great whoops of laughter, glanced at the notice in the forest and called out
what he thought it said without slowing. Robin stopped
and read carefully. To bind x to 42 and return it, the notice had to be read exactly:
they composed the top-level binding and lookup, submitted the form, and the REPL —
reading literally — returned the right value, while Will's guess
fell short.

Write a Clojure expression that computes the value of x after using def to bind x to 42.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

---

## safetynet — G1-18: Errors are safe in the REPL

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** The practice-pen behind the watchhouse — drills cost nothing here; cried-wolf gets caught, not believed. Mirrors `try`/`catch`/assert.

**form**: `(+ 1 2)`  •  **expected**: `3`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom hesitated at the practice-pen behind the watchhouse. Carol had set out a slate and chalk to demonstrate.

Tom was anxious about errors. Carol explained the pen made careless tries cost nothing — a place to experiment.

The REPL in the practice-pen is safe. A wrong form, a typo, anything tried inside is safely walked back.

To , She composed the form (+ 1 2) and submitted the form. The REPL — practice-pen in place — handed back the value:

Tom wrote the form, the runtime returned its value cleanly, and the pen had served its purpose.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will eyed the narrow path in the forest, with great whoops of laughter, certain he
could run it without a practice-pen or any safety measures. Robin shook
their head and quietly prepared the pen anyway. To  required
no daring, only the safety work: they composed the form (+ 1 2),
submitted the form, and the REPL — catching anything that fell — returned the
answer the careful design had earned.

Write a Clojure expression that computes the result of (+ 1 2).

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## scroll — G6-15: Namespace meta

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** The village log-book — leather-bound, kept by the elder. Watch-roll scrolls written and read; marginalia. Mirrors IO/metadata.

**form**: `(:doc (meta '^{:doc "trust the runtime"} village))`  •  **expected**: `'trust the runtime'`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol kept the village log-book on a stand in the watchhouse—leather-bound, with marginalia in the elder's hand. Today's entry: a symbol `village` with a margin note reading `trust the runtime`.

Tom wanted to read just the marginalia—the note Carol pinned to the symbol—without reading the symbol's value.

`meta` opens the marginalia—the metadata map on the symbol. `:doc` reads the specific `:doc` note from that map, the way you'd read one line from the margin.

To , She composed the :doc metadata attached to the symbol 'village and submitted the form. The REPL — quill in hand — completed the log-book entry:

The log-book returned the marginalia exactly as Carol had pinned it—the elder's note, ready for whoever consulted the entry next.

Write a Clojure expression that computes the docstring "trust the runtime" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"trust the runtime\"} village))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will, with great whoops of laughter, claimed he could guess
what the leather-bound village log-book would say without bothering
to open it. Robin only shook their head and opened
the book in the forest, dipping a quill into ink at the edge. "The world
outside the REPL is scrolls," they said: "you read what
they say, you write what you want to keep, and the runtime carries
the words back and forth." To , They
composed the :doc metadata attached to the symbol 'village, submitted the form, and the REPL handed
back what the log-book actually held.

Write a Clojure expression that computes the docstring "trust the runtime" from the metadata.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"trust the runtime\"} village))"}}]}
````

---

## guild — G8-01: Why polymorphism

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** The shepherds' fellowship — sheep-shepherd, goat-shepherd, geese-keeper. Each implements 'raise alarm' its own way. Mirrors protocols.

**form**: `(defn speak [k] (cond (= k :wolf) "howl" (= k :flock) "bleat" :else "silent"))`  •  **expected**: `None`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had called a meeting of the shepherds' fellowship on the village green — sheep-shepherd, goat-shepherd, geese-keeper, all gathered. Each kind of keeper had their own way of raising an alarm: a horn, a bell, a smoke-signal.

The fellowship needed a single named call — `speak` — that any keeper could be asked. Each kind of keeper would answer in their own way, but the call would mean the same thing to all of them.

Polymorphism by `cond` is the fellowship pattern in miniature: one named function, many internal arms — one for each kind of caller. The runtime checks the tag and runs the matching arm; the call site doesn't have to know which keeper showed up.

To , She composed a function speak that returns different strings for :wolf vs :flock and submitted the form. The REPL — checking the fellowship roll — dispatched cleanly:

the function was posted to the fellowship roll — a single name the village could call, with each kind of keeper answering in their own honest voice.

Write a Clojure expression that computes the form that defines speak via cond.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin carved a small wooden sign in the forest: "Shepherds'
Fellowship — any species may join." "A protocol is a fellowship,"
they said. "It lists what every member must be able to
do — the methods. Any animal that can sign the book may claim
membership." To , They composed
a function speak that returns different strings for :wolf vs :flock, submitted the form, and the REPL — fellowship
founded — handed back the fellowship's record.

Write a Clojure expression that computes the form that defines speak via cond.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))"}}]}
````

---

## toolshed — G6-14: Import for host classes

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** The village smithy / cooper's shed. The shepherd borrows foreign tools using the smithy's specific calls. Mirrors host interop.

**form**: `(symbol? 'java.util.Date)`  •  **expected**: `True`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol led Tom toward the village smithy—a foreign workshop with its own tools and naming conventions. On the lintel was a dotted name in the smith's host language: `java.util.Date`.

Tom wanted to know whether the smithy's marker was a name they could refer to. Borrowing across the boundary required knowing what the foreign label was.

`symbol?` asks whether the dotted-class label is a symbol—a name the runtime can reach across to. Quoted names from the smithy are still names.

To , She composed whether 'java.util.Date is a symbol and submitted the form. The REPL — calling into the foreign smithy — returned:

The predicate confirmed it as a symbol—a borrowable name. Tom understood the boundary could be crossed by name, not by guessing.

Write a Clojure expression that computes the value of (symbol? 'java.util.Date).

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin reached into the foreign toolshed in the forest and pulled
out a tool they hadn't carved themself — a tool
from the host platform. "This isn't ours," they said, "but
we can call its methods directly: dot-prefix on the instance, or
slash for static." To , They composed
whether 'java.util.Date is a symbol, submitted the form, and the REPL — calling into
the foreign tool — handed back what its method had returned.

Write a Clojure expression that computes the value of (symbol? 'java.util.Date).

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
````

---

## runnerahead — G9-10: Agent introduction

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** A dispatched child-runner sent down the path with a message. Come back later for the elder's reply. Mirrors `agent`/`future`/`promise`.

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol called the smallest of the village children to the watchhouse step. She handed the child a folded message with a single instruction: take it to the elder at the far cottage, wait for the reply, and bring back what the elder said.

The instruction couldn't be answered immediately — the child had to run, deliver, and return. The village needed to keep its work going meanwhile, then collect the runner's answer when it was ready.

An agent is the dispatched runner. `send` hands off the message and lets the runner go; `await` waits until the runner is back at the watchhouse step; `@` reads the answer the runner brought.

To construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference, She composed agent, send, await, deref and submitted the form. The REPL coordinated the runner's return:

the runner returned with the elder's reply tallied into the message — 1 step further than the start, honestly delivered.

Write a Clojure expression that computes the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin dispatched a young child-runner down the long path
in the forest, work in pouch. "The runner goes ahead while we keep on
with our own business," they said, "and when we need the
result we ask the runner to hand it back." To construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference,
They composed agent, send, await, deref, submitted the form,
and the REPL — sending the runner, fetching the result later —
returned the value when it was ready.

Write a Clojure expression that computes the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

---

## rewriterule — G10-03: defmacro introduction

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** The elder's drill-card rewrite. Shorthand `alarm-three` is rewritten into the full sequence (horn, beacon, fold) before runtime sees it. Mirrors macros.

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom had taken to writing shorthand drill-cards on the watchhouse wall — one-line abbreviations for routines the village ran every day. Carol watched, holding a fresh card and a stick of chalk.

The shorthand was easy to write but the village's runner needed the full sequence. Carol's job was to rewrite each shorthand card into the spelled-out drill before runtime — the runner only ever saw the full sequence.

`defmacro` registers the elder's rewrite rule. When the shorthand `my-when` appears, Carol — at compile time, before the runtime ever sees the form — rewrites it into the spelled-out `if` plus `do` body. The runtime then evaluates the rewritten form.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, She composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the drill-card rewrite, then evaluating the rewritten form — returned:

the rewrite landed correctly: the shorthand expanded to its full drill, and the runtime returned the value the spelled-out form produced.

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin sat at a small writing desk in the forest, slate and chalk
in hand. "A macro," they said, "is a rule that rewrites
the shorthand before the runtime ever sees it. You write the rule
once, and any form that names it gets rewritten on the way in."
To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, They composed defining a conditional macro and invoking it,
submitted the form, and the REPL — first rewriting, then evaluating —
returned the value the rewritten form had produced.

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-10: Comments

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** Slate-and-chalk conventions: blank line separates entries; dashed line is annotation; brackets group. Mirrors comments / whitespace / reader.

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had chalked an addition on the slate with a dashed line and notes in smaller chalk to the right — annotation only, for the next shepherd's eye.

Tom worried the runtime might mix annotations into the calculation. He needed to know which marks the runtime honored and which it skipped.

A single semicolon `;` is the slate's ignore-from-here mark. Everything to the right is annotation — the reader skips it; the runtime never sees it.

To add 1 and 2, with a single-semicolon trailing comment, She composed the addition with a trailing comment and submitted the form. The REPL read by the slate's conventions and returned:

the value came back as if the dashed annotation weren't there at all — exactly as the slate's conventions promised.

Write a Clojure expression that computes the result, ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

"There are conventions for how the runtime *reads* a form,"
Robin said: "what counts as one token, what's just
spacing, what gets ignored, what gets grouped together. The
scribe and the reader both follow the same conventions." To
add 1 and 2, with a single-semicolon trailing comment, They composed the addition with a trailing comment,
submitted the form, and the REPL — reading exactly by the
conventions — returned the value the form had specified.

Write a Clojure expression that computes the result, ignoring the comment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** Chalk mark on the slate vs the sheep it names. The symbol `bell` is the chalk mark; the bell is the bell. Mirrors `quote`/symbols.

**form**: `(symbol? 'wolf)`  •  **expected**: `True`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Tom had chalked a label on the slate for a flock pen. Carol stood with a carved tag from the live sheep itself.

The village's notes must not mix chalk marks with the things they name. Tom had to tell them apart.

`symbol?` asks whether something is a chalk mark — a name standing in for a value. The quoted form is the mark.

To , She composed the predicate (symbol? 'wolf) and submitted the form. The REPL — distinguishing chalk mark from the sheep it names — returned:

the predicate returned true — it was a chalk mark, a name, not the thing itself. The records stayed straight.

Write a Clojure expression that computes whether 'wolf is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'wolf)"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin pointed at a name chalked onto the slate in the forest,
then at an actual sheep standing in the fold. "The mark on the
slate is the *name*; the sheep is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To , They composed the predicate (symbol? 'wolf),
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer.

Write a Clojure expression that computes whether 'wolf is a symbol.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'wolf)"}}]}
````

---

## sortingtable — G8-08: Multimethod defmulti

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** The brand-sorting gate at the fold. Each sheep wears a brand (`:south`, `:north`); the gate routes by brand. Mirrors multimethods.

**form**: `(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))`  •  **expected**: `':cry'`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At the fold-gate, Carol had set up a brand-sorting gate. Each animal that arrived wore a brand on its ear — `:shepherd` for the village's working sheep, `:lantern-bearer` for the night-watch goats — and the gate routed each to the right pen.

Tom needed a uniform call — `reply` — that worked for any branded animal, with the gate doing the routing. Branding was the dispatch key; the right pen was the method.

`defmulti` posts the dispatch rule (here, look at `:role` on the arriving map) and `defmethod` registers what to do for each brand. The gate reads the brand and routes to the matching method.

To , She composed a defmulti reply that dispatches on :role, called with :shepherd and submitted the form. The REPL routed through the brand-gate:

the gate read the brand, called the right method, and the runtime returned the verdict — `:cry` for the shepherd-branded entry — the routing complete.

Write a Clojure expression that computes what reply returns for {:role :shepherd}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

A wooden gate with three branching paths stood at the fold in the forest.
"Defmulti is a sorting-gate," Robin said. "You decide
what brand on each sheep to look at; the gate reads the brand and
routes each sheep down the matching pen." To ,
They composed a defmulti reply that dispatches on :role, called with :shepherd, submitted the
form, and the REPL — reading the sheep's brand, picking the
gate — returned the value the right pen had produced.

Write a Clojure expression that computes what reply returns for {:role :shepherd}.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti reply :role) (defmethod reply :shepherd [_] :cry) (reply {:role :shepherd}))"}}]}
````

---

## carryingcase — G8-02: deftype introduction

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** A labeled tally-box with named pigeon-holes for sheep records (count, weight, breed). Mirrors `deftype`/`defrecord`.

**form**: `(do (deftype Lantern [color]) (.-color (Lantern. "amber")))`  •  **expected**: `'amber'`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol had ordered a small wooden tally-box from the village cooper — pigeon-holes inside for tallying different kinds of equipment. The first kind to track was lanterns, with one slot per box for the lantern's color.

The village wanted a uniform tally-box shape so any shepherd could lift the lid, find the same labeled slots in the same order, and read off the values without having to learn each box's quirks.

`deftype` is the cooper's plan for a tally-box: a name and a list of labeled slots. `Lantern.` constructs an instance with values in those slots; `.-color` reaches into the slot named `color` and reads it back.

To , She composed a deftype Lantern with a color field, then read color of an instance and submitted the form. The REPL constructed the tally-box:

the tally-box yielded the lantern's color cleanly — the cooper's plan and the village's uniform readout, exactly as designed.

Write a Clojure expression that computes the color field of a Lantern instance.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin held up a small wooden tally-box in the forest, its inside
divided into labeled pigeon-holes — one for count, one for weight,
one for breed. "A defrecord is like this box," they said:
"named compartments holding specific things; a mark on the outside
saying what kind of record it is." To , They
composed a deftype Lantern with a color field, then read color of an instance, submitted the form, and the REPL —
constructing the box, filling its compartments — returned the value
the tally-box held.

Write a Clojure expression that computes the color field of a Lantern instance.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))"}}]}
````

---

## tallywalk — G2-20: Counting

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** The shepherd walks past each sheep notching a wooden tally-stick once per sheep. Mirrors `reduce`/`count`.

**form**: `(count [1 2 3])`  •  **expected**: `3`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol stood at the fold-gate with her wooden tally-stick in hand, ready for the morning's pass-through. A small row of three lambs waited by the post — the south flock's morning return.

The village's morning record needed the count of the row. Tom offered to estimate; Carol preferred to walk the line with her stick, notching once per lamb so the count would settle exactly.

`count` walks the row and notches the tally-stick once per item. With three lambs in the row, the stick gains three notches — the running total grows knot by knot as the runtime steps through.

To count the elements in the vector containing 1, 2, and 3, She composed the count operation and submitted the form. The REPL walked the row, notch by notch on the tally-stick:

the stick carried 3 notches at the end of the walk — the morning's exact count, ready for the slate.

Write a Clojure expression that computes the result of using count on the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin walked the pasture flock in the forest, one sheep at a time,
notching a wooden tally-stick with the crook's edge. "Reduce is this
walk," they said: "at each sheep, you combine it into the
running tally; at the end, the final count is your answer." To
count the elements in the vector containing 1, 2, and 3, They composed the count operation,
submitted the form, and the REPL — walking the flock, notching the
tally-stick — returned the final number.

Write a Clojure expression that computes the result of using count on the vector containing 1, 2, and 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

---

## beadstring — G2-11: String concatenation with str

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** A knotted tally-cord — a cord with knots tied at intervals; spliced or counted bead by bead. Mirrors string ops.

**form**: `(str "wa" "tch")`  •  **expected**: `'watch'`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol the elder pulled out her knotted tally-cord — a long cord with knots tied at intervals, each section carrying its own labeled bead. The cord lay on the slate in two pieces: `wa` knotted at one end, `tch` knotted at the other.

The full word the village wanted on the slate was the two pieces spliced together as one cord. Tom guessed at the result; Carol insisted on letting the runtime splice the cord properly.

`str` is the splice — it takes pieces of bead-string and ties them end-to-end into a single cord. Each argument becomes the next stretch of beads; the result is one continuous string.

To , She composed the form (str "wa" "tch") and submitted the form. The REPL spliced or counted along the tally-cord as the form said:

the runtime returned the spliced cord and the village's slate carried the full word, exactly as the two pieces had promised.

Write a Clojure expression that computes the joined string "watch".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"wa\" \"tch\")"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin held up a knotted tally-cord in the forest, a long string
threaded with knots at intervals. "Strings in Clojure are like this,"
they said: "a cord of characters in order. Splice two cords
together, and the threads join; cut a section out, and you get a
shorter cord." To , They composed
the form (str "wa" "tch"), submitted the form, and the REPL — splicing or
cutting as the form said — returned the new tally-cord.

Write a Clojure expression that computes the joined string "watch".

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"wa\" \"tch\")"}}]}
````

---

## circuit — G5-22: recur — first taste

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** Dawn fence-walk — the shepherd walks the same fence circuit each dawn; no growing trail behind. Mirrors `recur`/`loop`.

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

At dawn, Tom set out to walk the fence-line that ringed the south pasture — the same circuit he walked every morning. Carol watched from the lookout, ready to read the count when he came back round.

The walk had to cover the whole circuit and return to the start carrying the running count, without leaving a growing trail of footprints behind. The village wanted the morning's tally, no matter how long the loop was.

`recur` takes a step forward on the same fence-walk without growing the trail behind it — each step replaces the last. The base case ends the walk; everywhere else, the loop steps and continues.

To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, She composed a factorial computation via loop and recur and submitted the form. The REPL walked the fence-line without growing the trail:

the walk completed the circuit and the loop returned the running tally — 120 — without leaving a single extra footprint along the fence-line.

Write a Clojure expression that computes the factorial of 5 computed by walking a circuit.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Robin walked the fence-line at dawn in the forest, each lap
returning to the same starting stone with fresh tallies in hand.
"Recur is this circuit," they said: "back to the top with
new bindings, no extra trail laid down behind us." To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero,
They composed a factorial computation via loop and recur, submitted the form,
and the REPL — looping without growing the call-stack — returned
the final value.

Write a Clojure expression that computes the factorial of 5 computed by walking a circuit.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

## goal — G6-10: Leiningen and deps.edn

_pool_: `_GOAL_SUBPLOTS`

**The metaphor:** Generic shepherd-vs-elder banter; no specific imagery. Used as the honest fallback for abstract subjects (host platforms, library design, build tools) where forcing a pastoral metaphor would be cargo-cult.

**form**: `(:deps {:deps {:a 1 :b 2}})`  •  **expected**: `{':a': 1, ':b': 2}`

### Story-scaffold render

````text
A young shepherd had been left alone with the flock far too often, and boredom had taken root.

Carol kept a small ledger entry describing the project setup in a nested map: which dependencies the project needed, which paths to search. Tom asked how to read just the dependencies portion from the map.

Before the village would approve a new project, Tom had to show he could extract the correct section from the ledger—the dependencies list.

A map with a `:deps` key holds the dependencies. Querying the key `:deps` on the map returns the nested structure—the dependencies the project declared it would need.

To extract the value at the :deps key from a nested map, She composed accessing a key from a nested map structure and submitted the form. The REPL — the village's only honest judge — returned:

Carol wrote the form, and the REPL returned the dependencies map. Tom had read the ledger correctly; the village approved the project setup.

Write a Clojure expression that computes the value at the :deps key in a deps-style map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
````

### Family-template render _(seed 1)_

````text
The boy on the hill thought the trick clever the first time he played it. It happened by the forest.

Will and Robin stopped in the forest to settle a small
question. Will, with great whoops of laughter, declared he could
write the form for it without thinking. Robin, saying very little, asked
him to actually write accessing a key from a nested map structure carefully — and
then let the REPL confirm what the value really was. To extract the value at the :deps key from a nested map,
they composed the form and submitted it.

Write a Clojure expression that computes the value at the :deps key in a deps-style map.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:deps {:deps {:a 1 :b 2}})"}}]}
````

---
