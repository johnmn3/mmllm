# Cross-fable showcase — same K-12 Clojure subject through five fable lenses

Each row picks a load-bearing Clojure subject from the K-12
framework. The five columns are the five Phase-C-complete
fables on `main`: same form, same expected value, told through
each fable's own characters, locations, and metaphor imagery.

This is what the model sees at training time — for any one
Clojure form, dozens to hundreds of narrative variants per
fable × 5 fables = a deep saturation of the same idiom-to-
metaphor mapping across a corpus that reads like 5 distinct
storybooks teaching the same curriculum.

Atom subjects (G1-01) keep `_SHARED_SUBPLOTS` in every fable —
the form IS the answer; copy-from-prompt is the lesson, and
the form-display is intentionally shown.

Goal-style subjects render via the family pool's templates;
when an example has authored `scenario`/`need`/`mapping`/
`resolution` slots and `tags=("story",)`, the 5-act
story-scaffold template fires and the metaphor *drives*
the action (vs. merely framing it).

The five fables and their morals:

- **Tortoise and the Hare** — _vanity vs. steadiness_
- **Crow and the Pitcher** — _patience vs. thirst_
- **Milkmaid and her Pail** — _daydream vs. care_
- **Boy who Cried Wolf** — _trust vs. false alarm_
- **Dog and the Shadow** — _greed loses what was had_

---

## G1-01 — L1 atom — a literal evaluates to itself

### Tortoise and the Hare

**form**: `85`  •  **expected**: `85`

````text
Thistledown was certain he could not lose; Basalt was certain of nothing except the next step.

A wooden sign nailed to a tree by the forest carried a puzzle. The riddle
was simple: it asked the reader to evaluate `85`. Thistledown
laughed, swaggering through the underbrush, and declared it too easy. Basalt said
patiently that the only way to be sure of the value 85 was to put
it in the REPL.

What Clojure form computes the value of 85? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"85"}}]}
````

### Crow and the Pitcher

**form**: `80`  •  **expected**: `80`

````text
Slate had flown all morning along the road without finding so much as a damp leaf to rest a beak against.

Mumble the crow and Slate the crow stopped along the road where someone had
scratched the value 80 into the dust beside a tall pitcher. The day
was hot, the throat of the pitcher was narrow, and the water inside lay
low. Mumble, ruffling up with certainty, declared she could see the answer
at a glance. Slate, unhurried with form after form, said the narrow throat was a
bottleneck — only the form, dropped in patiently like a pebble, would
raise the water — and suggested they actually evaluate the form
`80` in the REPL and read off whatever it returned.

Write a Clojure expression that computes the value of 80.

---

{"tool_calls":[{"name":"eval","args":{"form":"80"}}]}
````

### Milkmaid and her Pail

**form**: `66`  •  **expected**: `66`

````text
Irmgard set out from the farm by the meadow with the pail balanced carefully on her head.

Irmgard and Tobias stopped at the edge of the meadow where someone had
written the value 66 on a flat stone. Irmgard, his voice loud over the quiet road, declared
that she could see the answer at a glance. Tobias,
with the slow certainty of the sun, suggested they actually evaluate the form `66`
in the REPL and read off whatever it returned.

Question: write a Clojure expression for the value of 66.

---

{"tool_calls":[{"name":"eval","args":{"form":"66"}}]}
````

### Boy who Cried Wolf

**form**: `81`  •  **expected**: `81`

````text
There was once a shepherd boy whose afternoons were long and whose imagination was longer.

A small crowd of villagers had gathered atop the hilltop to watch
Thalia attempt to predict, off the cuff, what the REPL
would return. The lookout was high and the day was clear; from the
slope the slate was easy to read, and so was a wrong claim.
Augusta, with eyes always on the slate, pointed to the value 81 and read
it out aloud: `81`. The villagers waited, patient
but unimpressed, to see who would submit the expression properly.

Write a Clojure expression that computes the value of 81.

---

Let me check it through the runtime before I commit to an answer.

{"tool_calls":[{"name":"eval","args":{"form":"81"}}]}
````

### Dog and the Shadow

**form**: `26`  •  **expected**: `26`

````text
The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Halfway across the bridge, Cloud stopped near the pond and refused
to take another step until someone could prove what the form
`26` evaluated to. The reflection below glittered.
Cloud called the answer impossible to know. Snoutling the dog,
with the steady breathing of a long walker, walking up at his usual pace, simply
said: "Submit the value 26 to the REPL. The water shows a
shadow; the form shows the bone."

Question: write a Clojure expression for the value of 26.

---

Let me hold to what the expression actually says and evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"26"}}]}
````

---

## G1-13 — L2 application — first arithmetic call

### Tortoise and the Hare — *story-scaffold render*

**form**: `(+ 0 6)`  •  **expected**: `6`

````text
Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

Mossback had sorted this morning's acorns into two small heaps beside the trail — one heap of 0 and another of 6.

She needed the running total before deciding whether to carry them all or leave some behind.

`+` is the counting-together operator: the two heap sizes are its arguments, and the runtime combines them into a single count.

To add 0 and 6, he untroubled by what others thought composed the addition and submitted the form. The REPL counted out the answer:

the runtime returned the combined count — the two heaps tallied into one (with `0` as the input value).

What Clojure form computes the sum of 0 and 6? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 0 6)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(+ 3 4)`  •  **expected**: `7`

````text
The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus crouched at the tall clay pitcher's rim at the farm's yard, two handfuls of smooth stones — one stone in his left talon, two in his right.

He wanted to count the total stones in both talons to know how far the water would rise when both handfuls dropped together.

`+` is the stone-count call: it totals the numbers it receives, left to right. One stone plus two stones gives a total the runtime calculates and returns as the water-level.

To add 3 and 4, he composed the addition and submitted the form. The REPL counted out the answer:

The two handfuls combined, the water rising to the expected notch at beak-reach. (with 3 folded in)

What Clojure form computes the sum of 3 and 4? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 3 4)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(+ 5 7)`  •  **expected**: `12`

````text
Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The farmer set two small coin-piles on the tally table: one pile of a single copper, and another of two. She needed the total before she could mark the day's earnings on the tally-slate.

She needed a form that added the two piles together — not guessing, not daydreaming, but submitting the sum to the REPL and reading what came back.

`+` is the farmer's tally rule: it stacks all the given coin-piles into one and hands back the total. No pail-nodding, no guesswork — just the arithmetic result.

To add 5 and 7, she composed the addition and submitted the form. The REPL counted out the coins:

The REPL returned the total the farmer had tallied — three coins, exactly as the two piles combined — 7.

What Clojure form computes the sum of 5 and 7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 5 7)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(+ 2 5)`  •  **expected**: `7`

````text
A boy with too little to do and too loud a voice is a small danger to himself and a larger one to his village.

At dawn, Tom had brought lambs back from the south pasture and Carol had brought lambs from the north. They stood at the fold counting together, the meadow folk's morning record waiting on them. The combined morning tally needed to settle correctly before the day's work could begin — the townsfolk's records depended on exact arithmetic, no boasting and no fudging. `+` adds its operands one after another and gives back the running total. The runtime carries the sum exactly — no shouting required.

To evaluate the form, she composed the expression (+ 2 5) and submitted it. The REPL counted out the answer: the count came back — the morning's flock confirmed by the runtime, not by Tom's memory. The pasture tally settled at 2, and Carol closed the day slate with that one number written clear.

Write a form whose evaluation gives the result of (+ 2 5).

---

Let me check it through the runtime before I commit to an answer.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 5)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(+ 5 1)`  •  **expected**: `6`

````text
The bone was good, the day was warm, and the path was clear, and yet the trouble was already shaped in the water.

Bell the hound sat by a flat stone near the pond and laid out two small piles of bones — one of one bone, one of two — careful with the count. She wanted the precise size of the heap if both piles were nudged together — small or large, the runtime would give the exact number, and that was the count she would carry forward. The bones are the numbers, the piles are the operands, the act of nudging-together is +, and the count of the combined heap is what the REPL hands back.

She, her quiet hands at her quiet sides, composed the addition with the running tally heavy in the count. The runtime counted out the answer: The REPL added the two piles and handed back the precise count. Bell brushed the bones back into a single tidy heap — the 1 settled, no eyeballing needed.

Write a form whose evaluation gives the sum of 5 and 1.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 5 1)"}}]}
````

---

## G2-13 — and/or short-circuit — chain of gates

### Tortoise and the Hare — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
All this took place near the road, where the dust still keeps the shape of the runners' feet.

Two small wooden gates stood at the start of the meadow trail. Each gate's verdict-stone was carved with the value the runner would carry to it — and today's two stones both read true.

Mossback the tortoise wanted to know whether both gates would let the runner through together, or whether the first one would close and stop the chain.

`and` walks the gates left to right: the first false closes the chain and that value comes back; otherwise the value at the last gate is what comes back. With both stones reading true, the chain holds and the last gate's true is the verdict.

To test whether two trues both pass through an and-chain of gates, she without complaint composed the logical and and submitted the form. The REPL let the gates decide:

both gates along the chain swung open easily; the chain's last gate handed back its own value as the verdict — the path-to-end clear, uninterrupted.

Question: write a Clojure expression for the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
It was near the orchard, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verdict only if every gate along the chain was open — a single closed gate would block the path.

`and` checks each gate in order; if the first is open it moves to the next. Both true means both gates are open, so `and` returns the last value it checked.

To test whether two trues both pass through an and-chain of gates, he composed the logical and and held it at the dual-gate check. The REPL opened or closed the gates as the logic demanded:

Both gates passed and the value arrived at the rim.

Write a form whose evaluation gives the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The farmer had two gates on the farmyard path: the first opened when the condition was true, the second also opened when its condition was true. She wondered if both gates would open together.

She needed to check if the first condition was true AND the second condition was also true, without guessing or testing separately.

The logical and is the farmer's gate-chain: both gates must pass (both true) for the journey to continue. If the first gate closes (false), the whole chain fails. If the first passes, check the second.

To test whether two trues both pass through an and-chain of gates, she composed the logical and and submitted the form. The REPL let the gate decide:

The REPL returned the verdict — both gates opened, the and-chain was complete.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
It happened on the road, on a hill where shouting carries far and trust carries further, until it doesn't.

Two fold-gates stood in the shepherd's path: the first open (true), the second open (true). The shepherd wanted to know if both gates allowed passage. Both gates had to be open for passage. Tom saw the first was open; Carol insisted the form would confirm both were passable. `and` checks the first gate (true), walks through, checks the second gate (true), and returns true only if all gates pass.

To test whether two trues both pass through an and-chain of gates, she composed the logical and and submitted it. The REPL let the fold-gates decide: the call returned true, and the shepherd could walk straight through both gates.

Write a form whose evaluation gives the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
Some greedy creatures lose what they have to a thief; others lose it to themselves, by way of a careless glance.

Bell the hound stood at the stream bank, facing two test gates placed one after the other. Each gate bore a mark: true, then true. She wanted to cross if both gates would let her pass. The and would test each one in turn — if either blocked her, the chain would fail. Each gate is one condition, the and is the chain that checks them in sequence, and the verdict is true only if all pass her through.

She, with the unrushed care of a long task, composed the logical and. The runtime let the crossing-conditions decide: The REPL tested true at the first gate — it opened. True at the second gate — it opened too. Both conditions held, and the verdict came back true. She could cross.

Question: write a Clojure expression for the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G3-03 — let — local binding (the temporary-pouch metaphor)

### Tortoise and the Hare — *story-scaffold render*

**form**: `(let [x 5] (+ x 7))`  •  **expected**: `12`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 5 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Just past the next milestone she'd want the running total — what x plus one more acorn would come to. After the milestone, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 7)`, x means 5; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 5 to a local name x for one stretch, then return that value plus one, she untroubled by what others thought composed the local binding and addition with the binding tucked safely into the pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded its tucked count, the +7 added one more acorn, and the running total — pouch already empty again — was exactly what the next milestone needed.

Write a form whose evaluation gives the running total after binding x to 5 and adding 7.

---

I write the let-form so the REPL can substitute.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 5] (+ x 7))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(let [x 7] (+ x 7))`  •  **expected**: `14`

````text
It was by the garden, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and named: x, holding three.

He needed to know how far the water would rise if he added one more stone to whatever was tucked under his wing.

`let` gives a name to a tucked value: x binds 7 for the span of the form. Inside that stretch, `(+ x 7)` reaches under the wing and adds one. When the form ends the wing opens; the binding dissolves.

To bind a value of 7 to a local name x for one stretch, then return that value plus one, he composed the local binding and addition with the binding tucked safely under a wing and submitted the form. The REPL reached under the wing as the form directed:

4 — the tucked count of three, plus the one stone added while the wing held it firm. (with 7 folded in)

What Clojure form computes the running total after binding x to 7 and adding 7? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 7] (+ x 7))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(let [x 7] (+ x 0))`  •  **expected**: `7`

````text
The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid tucked the number 7 into her apron-pocket at the start of one stretch of the road — a private count, good only for this leg of the journey to market.

She needed to reach into the pocket at the next step and add 0 to the count, then let the pocket empty when the form ended.

`let` is the apron-pocket: it tucks `x = 7` into the pocket for the duration of the body. `(+ x 1)` draws from the pocket and adds 1. When the body ends, the pocket is put away and `x` ceases to exist.

To bind a value of 7 to a local name x for one stretch, then return that value plus one, she composed the local binding and addition with the value tucked into the apron-pocket and submitted the form. The REPL reached into the pocket as the form directed:

The REPL returned the result — the count from the pocket incremented by one, the pocket now set aside at the road's end (with `7` as the input value).

Write a Clojure expression that computes the running total after binding x to 7 and adding 0.

---

Better to confirm with the runtime than to imagine a number.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 7] (+ x 0))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(let [x 7] (+ x 7))`  •  **expected**: `14`

````text
There is a difference between a real alarm and a bored one, and the village knew the difference well.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 7 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the local name x for that stretch of watch. By the next fence-post she would want the running total — what x plus one more lamb came to. Past that post, the pouch would empty and x would mean nothing again. `let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 7)`, x means 7; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 7 to a local name x for one stretch, then return that value plus one, he composed the local binding and addition with the binding tucked safely into the belt-pouch and submitted the form. The REPL pulled from the pouch as the form directed: the pouch yielded 7, the +7 added a fourth lamb, and the running total stood at 4 — exactly what the next fence-post called for. Tom chalked 7 on the meadow folk notice, and the morning record stood for the next shepherd to read.

Question: write a Clojure expression for the running total after binding x to 7 and adding 7.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 7] (+ x 7))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(let [x 2] (+ x 9))`  •  **expected**: `11`

````text
Inky had found the bone at the edge of the meadow and was carrying it home with no small amount of pride.

Bell the hound had picked up a small bone near the pond and held it firmly between her jaws. Just for the next stretch of crossing she would need to know the bone's tally — 2 — by a short local name x. She wanted the running total — what x plus one more would come to — at the moment her paw left the far bank. After that stretch, the mouth would empty and x would mean nothing again. The closed jaws are the let-binding, x is the name for what's gripped between the teeth, the value held there is 2, and the form's stretch is the crossing. Outside the form, the mouth empties and the binding goes with it.

He, her quiet hands at her quiet sides, composed the local binding and addition. The runtime pulled from the mouth as the form directed: The REPL pulled from the mouth as the form directed and handed back 9. Past the crossing, Bell's mouth was empty again — the binding had been in force only for that stretch.

What Clojure form computes the running total after binding x to 2 and adding 9? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 2] (+ x 9))"}}]}
````

---

## G4-08 — assoc — pin a tag on the basket

### Tortoise and the Hare — *story-scaffold render*

**form**: `(assoc {:berry 20, :nectarine 11, :kiwi 8} :beta 7)`  •  **expected**: `{('__kw__', 'berry'): 20, ('__kw__', 'nectarine'): 11, ('__kw__', 'kiwi'): 8, ('__kw__', 'beta'): 7}`

````text
Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

Mossback the tortoise's foraging-basket had compartments stitched into its sides — an open area at the top, plus named pouches :a and :b. Pouch :a already held 1 acorn from the morning's gathering.

Pip the hare arrived from the orchard with 7 more acorns. Mossback decided they belonged in pouch :b — and pouch :a's acorn should stay exactly where it was.

`assoc` associates a value with a named compartment of the basket. The basket's shape stays the same — :a still holds its 1, and :b now holds the new 7 — exactly as the foraging called for.

To associate value 7 with the :b compartment of a basket already binding :a to 1, he saying very little composed the assoc operation for the basket and submitted the form. The REPL handed back the arrangement:

the basket carried both — 1 in :a, 7 in :b — ready for the rest of the day's gathering.

Write a Clojure expression that computes the basket after associating value 7 with the :b compartment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:berry 20, :nectarine 11, :kiwi 8} :beta 7)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(assoc {:cherry 16, :raspberry 1} :a 7)`  •  **expected**: `{('__kw__', 'cherry'): 16, ('__kw__', 'raspberry'): 1, ('__kw__', 'a'): 7}`

````text
Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

Caw held a one-compartment stone-pile at the orchard pitcher — :a with one stone. A second compartment, :b, needed to be scratched in and filled with two stones.

The original pile had to stay as it was; `assoc` should return a new pile that also had the :b compartment filled.

`assoc` scratches a new compartment into a copy of the pile and fills it. The original pile keeps only :a; the returned new pile holds both :a and the fresh :b compartment.

To associate value 7 with the :b compartment of a basket already binding :a to 1, she composed the assoc operation for the stone-pile and submitted the form. The REPL handed back the arrangement:

The REPL returned the extended pile with both compartments present, the original unchanged. (with {('__kw__', 'cherry'): 16, ('__kw__', 'raspberry'): 1} folded in)

What Clojure form computes the basket after associating value 7 with the :b compartment? Submit it via `eval`.

---

I'll let the REPL show what each step adds.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:cherry 16, :raspberry 1} :a 7)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(assoc {:plum 7, :tangerine 10, :guava 9} :hard 0)`  •  **expected**: `{('__kw__', 'plum'): 7, ('__kw__', 'tangerine'): 10, ('__kw__', 'guava'): 9, ('__kw__', 'hard'): 0}`

````text
The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The milkmaid held a market-basket with one labeled compartment: :a held the value 1. She stood at the buyer's stall, ready to add a second compartment labeled :b to hold the value 0.

She needed a new basket keeping the original :a binding while adding a fresh :b compartment. The old basket would remain untouched; a new one would carry both bindings.

The `assoc` operation builds a new basket: the assoc form takes the original basket and creates a fresh one with the :a binding intact and a new :b compartment added. The old basket stays as it was.

To associate value 0 with the :b compartment of a basket already binding :a to 1, he composed the assoc operation for the market-basket and submitted the form. The REPL handed back the arrangement:

The REPL handed back a new basket with both bindings — :a still pointing to 1, :b now pointing to 0, the original basket sitting untouched behind.

What Clojure form computes the basket after associating value 0 with the :b compartment? Submit it via `eval`.

---

Let me check the work before announcing anything.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:plum 7, :tangerine 10, :guava 9} :hard 0)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(assoc {:berry 5, :papaya 7, :guava 19} :soft 6)`  •  **expected**: `{('__kw__', 'berry'): 5, ('__kw__', 'papaya'): 7, ('__kw__', 'guava'): 19, ('__kw__', 'soft'): 6}`

````text
Aharon was supposed to keep the sheep safe; instead, near the meadow, he kept inventing reasons for the village to run.

Carol held a wool-basket with one pouch labeled `:a` holding 1 fleece. A fresh delivery brought new fleeces that needed a second pouch labeled `:b` with 6 pieces. The form had to add the new pouch to the basket and return an updated basket with both pouches, leaving the original unchanged. `assoc` adds or updates a key-value pair in the map. It takes the old basket, the new key `:b`, and its value 6, returning a fresh basket that holds both the original `:a` and the new `:b`.

To associate value 6 with the :b compartment of a basket already binding :a to 1, she composed the assoc operation for the wool-basket and submitted it. The REPL handed back the arrangement: the call returned a new basket showing both `:a` 1 and `:b` 6, while the original single-pouch basket stood untouched. Tom chalked {('__kw__', 'berry'): 5, ('__kw__', 'papaya'): 7, ('__kw__', 'guava'): 19} on the village notice, and the morning record stood for the next shepherd to read.

Question: write a Clojure expression for the basket after associating value 6 with the :b compartment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:berry 5, :papaya 7, :guava 19} :soft 6)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(assoc {:kumquat 7, :quince 17, :pomegranate 11, :papaya 14} :right 5)`  •  **expected**: `{('__kw__', 'kumquat'): 7, ('__kw__', 'quince'): 17, ('__kw__', 'pomegranate'): 11, ('__kw__', 'papaya'): 14, ('__kw__', 'right'): 5}`

````text
A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound held a hollow log cache with one compartment named :a that held 1 bone. The cache was ready to receive a new compartment. Patch marked out a fresh section and labeled it :b, then placed 5 bones inside. Patch wanted the REPL to take the existing cache, add the new compartment :b with its 5 bones, and return the extended cache without disturbing what :a held. The original hollow log is the map {:a 1}, the new compartment name is :b, the new bone-count is 5, and assoc is the operation that adds the slot.

He, with steady breath and a careful eye, composed the assoc operation for the bone-cache. The runtime handed back the arrangement: The REPL extended the cache by one compartment, placing 5 bones in the :b slot while :a kept its 1 bone. The expanded cache came back intact — b.

What Clojure form computes the basket after associating value 5 with the :b compartment? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:kumquat 7, :quince 17, :pomegranate 11, :papaya 14} :right 5)"}}]}
````

---

## G5-12 — reduce — walk the row carrying a tally

### Tortoise and the Hare — *story-scaffold render*

**form**: `(reduce + [1 1 20 15])`  •  **expected**: `37`

````text
Word went around by the meadow that two creatures had agreed to settle an old question with their feet.

A row of four small pebbles lay along the path — counts of 1, 2, 3, and 4 from four foraging trips. The value drawn fresh was 1, 1, 20, and 15.

Mossback the tortoise wanted the grand total of the four trips. Walking the row and carrying a running tally was the patient way.

`reduce` walks the collection from left to right carrying a tally. At each pebble, the combine function (here `+`) is applied to (tally, pebble), producing the new tally. The final tally is what comes back.

To walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total, she stepping deliberately composed the fold operation and submitted the form. The REPL walked the row carrying the tally:

the walk produced a tally that grew across the four pebbles, ending at the grand total of all four trips (with `1, 1, 20, and 15` as the input value).

Write a Clojure expression that computes the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [1 1 20 15])"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(reduce + [8 6 2])`  •  **expected**: `16`

````text
Nightshade arrived on the hilltop with no plan but a sharp eye and a willingness to take small steps.

Caw walked the garden tallywalk beside the stones in a row: 1, 2, 3, 4. She carried a running tally in her wing-cache, combining each stone with `+` as she stepped past.

She needed the final tally after combining all the stones with addition, stone by stone from left to right.

`reduce` walks the sequence, folding each element into an accumulator using the given function. Starting from the first stone, each step adds the next, building the running total.

To walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total, he composed the fold operation and submitted the form. The REPL walked the rim carrying the tally:

The tallywalk ended after the fourth stone; the running tally reached its final sum and dropped into the pitcher. (with 8, 6, and 2 folded in)

Write a Clojure expression that computes the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [8 6 2])"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(reduce + [8 8 8 1])`  •  **expected**: `25`

````text
Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

The milkmaid walked to market counting coins step by step: one coin at the first stall, two at the second, three at the third, four at the fourth. At each stall she added the new coins to her running tally.

She needed to step through each stall, combine its count into the running tally with `+`, and carry that tally forward to the next — one tally-walk, not four separate additions.

`reduce` with `+` is the tally-walk: the milkmaid starts with the first element, then steps through the rest, combining each into the running total with the `+` step until the row is done.

To walk the row of pebbles these numbers carrying a tally that combines each with + into the running total, he composed the fold operation and submitted the form. The REPL walked the collection carrying the tally:

The REPL returned the accumulated total — the tally the milkmaid had built coin by coin across all four stalls — 4 (with `8, 8, 8, and 1` as the input value).

Write a Clojure expression that computes the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

No premature conclusions; I'll write and evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [8 8 8 1])"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(reduce + [6 3 12 7])`  •  **expected**: `28`

````text
Lorcan had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Tom walked the tally-stick down a line of sheep. Tom needed to combine all the numbers into a single total. `reduce` takes a combination-rule and applies it across the list.

To walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total, he composed the fold operation and submitted it. The REPL walked the row, notch by notch on the tally-stick: The form combined all values into a single result. The slate showed 6, 3, 12, and 7 in clear chalk, and the fold tally stood as the day record.

What Clojure form computes the running tally after walking 1, 2, 3, 4 with + as the combine step? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [6 3 12 7])"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(reduce + [12 16 13])`  •  **expected**: `41`

````text
Yelper had carried his prize all the way from the village, and by the meadow the bridge offered him an unwelcome second look.

Patch the hound stood at the stream near the forest, facing a row of pebbles marked 1, 2, 3, 4 laid end to end. She would walk the row, carrying a tally in her jaws, adding each pebble to the tally as she passed it. The final tally would be her answer. She wanted the sum of all pebbles in the row. Reduce walks the row left to right, combining each pebble with a running total using the + rule. The reduce-form is the tally-walk. The pebbles are 1, 2, 3, 4. The combination-rule is +. Each step adds the current pebble to the tally. The final tally is what reduce returns.

He, with eyes always on the path, composed the fold operation. It walked the bone-row carrying the tally: The REPL began the walk with no tally and pebble 1 (tally=1), added pebble 2 (tally=3), added 3 (tally=6), added 4 (tally=10). The final tally came back as the answer (with `12, 16, and 13` as the input value).

What Clojure form computes the running tally after walking 1, 2, 3, 4 with + as the combine step? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [12 16 13])"}}]}
````

---

## G6-03 — require — borrow a routine from a foreign scroll

### Tortoise and the Hare — *story-scaffold render*

**form**: `(clojure.string/upper-case "stone")`  •  **expected**: `'STONE'`

````text
There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.

The library by the road kept a scroll on its shelves called `clojure.string`. Among its signs was a routine named `upper-case` — a routine that took a string and returned the same letters, capitalized.

Mossback the tortoise wanted the capitalized form of the four-letter word `stone`, for a road-sign she was painting.

When a routine lives on a scroll, you call it by both names together: scroll-name slash routine-name — `clojure.string/upper-case`. The runtime fetches the scroll and invokes the routine on the argument.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string stone, she with eyes always on the path composed calling a fully-qualified string function and submitted the form. The REPL read the signs and replied:

the routine returned the four letters in capitals, ready for the road-sign Mossback was painting (with `stone` as the input value).

Write a form whose evaluation gives the capitalized form returned by the upper-case routine on the scroll.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"stone\")"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(clojure.string/upper-case "bridge")`  •  **expected**: `'BRIDGE'`

````text
near the market, a single pitcher held the last of the water, and Shriek arrived too parched to be picky.

Sable perched at the pitcher in the meadow, a flat stone already required from the string-scroll's shelf. She scratched the fully-qualified call using the scroll's shelf-name and the upper-case groove.

She needed the four-letter word returned in its capitals — the shelf held the method, but the full path was required to reach it across the namespace boundary.

The `namespace/function` carving tells the runtime which shelf to pull from before calling. The required shelf answers with the uppercased characters, the slash linking shelf to groove.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string bridge, he composed calling a fully-qualified string function and submitted the form. The REPL read the rim-carvings and replied:

The pitcher returned the four letters in their capital form, the fully-qualified call resolved cleanly. (with bridge folded in)

Question: write a Clojure expression for the capitalized form returned by the upper-case routine on the scroll.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"bridge\")"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(clojure.string/upper-case "myrtle")`  •  **expected**: `'MYRTLE'`

````text
There was once a milkmaid who walked to market with a pail of fresh milk balanced upon her head.

The market-board in the village square listed the clojure.string vendor's section. The milkmaid had a word written in small letters and needed to use the board's registered uppercasing service to produce the full-capitals version.

She needed to consult the board, locate the vendor's section, and call the uppercasing routine — without that board entry she could not reach the function by its full qualified name.

The board's namespace section is `clojure.string`; the vendor's listed routine is `upper-case`. Reading the board entry and calling it produces the transformed output.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string myrtle, he composed calling a fully-qualified string function and submitted the form. The REPL read the market-board and replied:

The REPL returned the all-capitals version of the word, confirming the board-listed routine had been reached and applied correctly (with `myrtle` as the input value).

Question: write a Clojure expression for the capitalized form returned by the upper-case routine on the scroll.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"myrtle\")"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(clojure.string/upper-case "marble")`  •  **expected**: `'MARBLE'`

````text
It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Carol led Tom to the valley smithy, where a master crafts strings in their furnace. On the smithy's post hung the sign `clojure.string/upper-case`—a foreign tool the smith had left for any shepherd to borrow. Tom wanted to shout the answer about what `upper-case` would do to the word "marble", but Carol insisted he borrow the smith's tool and watch what it actually returned. The fully-qualified name `clojure.string/upper-case` reaches across the namespace boundary to the smithy's tool. Calling it with "marble" borrows the smith's transformation.

To evaluate the form, she composed the form using clojure.string/upper-case on "marble" and submitted it. The REPL read the notice-post and replied: Carol wrote it into the REPL, crossed into the smithy by name, and the smith's tool returned "WOLF". Tom learned: the namespace slash is the boundary you must cross by name. The slate showed marble in clear chalk, and the fold tally stood as the day record.

Write a Clojure expression that computes the upper-cased string "WOLF".

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"marble\")"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(clojure.string/upper-case "apple")`  •  **expected**: `'APPLE'`

````text
The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Bell the hound found a scroll in the riverbank cache bearing the name clojure.string. A routine written there was called upper-case. She wanted to send the text "apple" through that routine and see what came back in a different form. She needed to call the fully-qualified routine, naming both the scroll and the function, so the runtime could find the right tool. The scroll clojure.string is the library, the upper-case function is the routine written there, and the text "apple" is the message to be transformed.

He, without raising her voice at the troubles of the road, composed calling a fully-qualified string function. The runtime read the markers and replied: The REPL reached into the scroll, found the routine, and applied it to the text, handing back apple in capitalized form.

Question: write a Clojure expression for the capitalized form returned by the upper-case routine on the scroll.

---

Let me read the expression as written and submit it.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"apple\")"}}]}
````

---

## G7-02 — try / catch — net under the leap

### Tortoise and the Hare — *story-scaffold render*

**form**: `(try (/ 6 7) (catch Exception e -96))`  •  **expected**: `Fraction(6, 7)`

````text
Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

Mossback the tortoise was about to ask the runtime for the result of dividing 6 acorn into 7 piles — a division she knew would throw, because dividing by zero isn't a thing the runtime can do.

She didn't want the throw to end the run. She wanted the form to come back with -96 as a placeholder so the rest of the work could continue.

`try`/`catch` is a net beneath the leap. The throw still happens, but the catch-arm catches the Exception cleanly. Whatever the catch-arm returns is what the form yields — here, the placeholder -6.

To attempt to divide 1 by 7; when the runtime throws, catch the Exception and return -96 from the catch arm, she untroubled by what others thought composed the handler for a division-by-zero error and submitted the form. The REPL — net in place — handed back the value:

the throw happened, the catch caught it, and the form yielded -96 — the placeholder Mossback had specified.

Write a Clojure expression that computes the value the catch arm returns when the divide-by-zero throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 6 7) (catch Exception e -96))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(try (/ 1 0) (catch Exception e -21))`  •  **expected**: `-21`

````text
An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Caw leaned over the pitcher with a risky stone in her talon — a division of one stone across zero, a form the REPL would refuse. Korvus had laid a soft moss pad below to catch any falling stone safely.

She wanted the risky form tried; if the stone fell badly, she needed the moss to return -1 instead of letting the crash stand unresolved.

`try` attempts the body. If an exception is thrown, `catch` intercepts it — the moss catches the stone — and the handler returns the fallback. The crash is absorbed; the fallback surfaces.

To attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -21 from the catch arm, he composed the handler for a division-by-zero error and submitted the form. The REPL — moss in place — handled any slip and returned:

The division failed, the moss caught the throw, and the handler's fallback stone rose to beak-reach (with `1` as the input value).

What Clojure form computes the value the catch arm returns when the divide-by-zero throw is caught? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 1 0) (catch Exception e -21))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(try (/ 4 8) (catch Exception e -40))`  •  **expected**: `Fraction(1, 2)`

````text
Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

Lila walked carefully to the dairy, carrying a pail of cream to be divided among the neighbors.

But when she tried to share the cream equally with no neighbors present—dividing by zero—the motion made no sense. What would happen?

An impossible division is an error thrown at the milkmaid. The catch block is the careful handler—not a net to prevent the error, but a graceful response that lets her substitute a recovery value and continue.

To attempt to divide 1 by 8; when the runtime throws, catch the Exception and return -40 from the catch arm, she composed the handler for a division-by-zero error and submitted the form. The REPL — pail balanced, walk steady — handed back the value:

The form caught the error and returned a recovery code, keeping the day's work from being lost (with `1` as the input value) (with `-40` as the input value).

Write a Clojure expression that computes the value the catch arm returns when the divide-by-zero throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 4 8) (catch Exception e -40))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(try (/ 0 7) (catch Exception e :gamma))`  •  **expected**: `0`

````text
It was in the village, where the ridge looks down on the houses, that Marzena first cried wolf.

Tom was counting sheep at dusk when a strange question came to him: what was one sheep divided by zero sheep? Carol heard the question and smiled. She wrote out the form. The flock couldn't be divided by nothing — it would break the counting. Carol needed a form that gamma the impossible calculation and returned a safe answer instead. `try` surrounds the dangerous division; `catch` waits for the error (division by zero always fails); when caught, the catch clause returns :caught instead of crashing. The pen holds it.

To catch the divide-by-zero error and return the gamma keyword, he composed a try form with a catch returning a sentinel keyword and submitted it. The REPL — practice-pen in place — handed back the value: the form caught the error and returned :caught, keeping the counting safe without stopping the day's watch. The slate showed 0 in clear chalk, and the fold tally stood as the day record.

Write a Clojure expression that computes the value the catch branch returns.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 0 7) (catch Exception e :gamma))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(try (/ 0 3) (catch Exception e -85))`  •  **expected**: `0`

````text
There was once a dog who carried a fine bone home along a path that crossed a stream by an old wooden bridge.

Bell the hound had seen the snare before. A trap that divided bones by paw-counts: 0 bone split into 3 chunks. The math would snap. She knew the REPL would object. She wanted to catch the objection and walk on with a marked result—the code -0 in her jaws—instead of being thrown by the trap. The snare is the try block, the division is the bad math, the catch is her jaw ready for the thrown error, and -0 is the safe mark she carries back.

He, with the soft step of a guarded heart, composed the handler for a division-by-zero error. It handed back the value: The REPL caught the division-by-zero, her paw intercepted it, and she received the -0 without crashing.

Write a form whose evaluation gives the value the catch arm returns when the divide-by-zero throw is caught.

---

Let me work the actual expression and not its echo.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 0 3) (catch Exception e -85))"}}]}
````

---

## G8-04 — Protocol definition — found a guild

### Tortoise and the Hare — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
All this took place by the garden, where the dust still keeps the shape of the runners' feet.

Mossback wanted to found a Runners' guild named `Pace`. Members would have to perform `speed`, taking the runner as its argument.

Before any species could sign, the guild had to be founded — and Mossback wanted to confirm the name was now real to the runtime.

`defprotocol Pace (speed [this])` founds the guild. `(some? Pace)` then asks whether the name is non-nil.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, she stepping deliberately composed a protocol definition and submitted the form. The REPL — checking the guild book — dispatched cleanly:

the council's roll, freshly inked, was looked up by name; `some?` cast through the registry — feeling for the var among many that might or might not be there — and confirmed the guild now stood entered.

Question: write a Clojure expression for whether the Runners' guild named Pace is real after the founding.

---

Let me transcribe the form exactly, then send it to the REPL.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Sable scratched the guild's charter onto the pitcher's rim at the village: any type wishing to answer the `speed` call must register here. The ledger was posted but no members had yet signed.

Sable needed to confirm the guild's name existed in the runtime as a real thing after the charter was scratched.

`defprotocol` posts the guild's ledger — the name and required calls are declared. `some?` checks whether the ledger var is present and truthy, confirming the guild was founded successfully.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, she composed a protocol definition and submitted the form. The REPL — checking the guild ledger — dispatched cleanly:

The pitcher confirmed the guild's ledger was real and present.

Write a form whose evaluation gives whether the Runners' guild named Pace is real after the founding.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
The cows had given generously that dawn, and the pail was heavier than usual, and the imagination was heavier still.

The guild-master declared a new market guild called Pace, nailing its charter to the guild-hall door. One requirement: every member must answer `speed`. No farmer had joined yet, but the charter now existed.

She needed to confirm the guild charter was real — that `Pace` now stood as a recognized thing in the runtime, not merely a plan in the guild-master's notebook.

`defprotocol` is the guild charter: it names the guild and lists required methods. `some?` is the inspector who checks whether the charter's name is a real, non-nil value.

To found a Pace guild with one required method speed, then confirm the guild's name exists in the runtime, she composed a protocol definition and submitted the form. The REPL — checking the guild roll — dispatched to the right member:

The REPL confirmed the charter was real — the guild name existed as a recognized value and the inspector returned an affirmative answer.

Write a Clojure expression that computes whether the Runners' guild named Pace is real after the founding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(do (defprotocol Alarm (sound [this])) (some? Alarm))`  •  **expected**: `True`

````text
It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

At the shepherds' fellowship meeting, Carol announced that all keepers must pledge to answer the named call "Alarm" with their own honest method — a horn, a bell, smoke. The pledge was posted on the board. The fellowship needed to declare a contract — a single named call that each kind of keeper could implement their own way, no matter their tool. `defprotocol` posts the named call and its signature (here, `sound` takes `this`). It doesn't say what the method does — just that it exists, and any keeper who implements it must have a `sound` method.

To determine whether the Alarm protocol was defined (a non-nil truthy value), she composed a defprotocol Alarm with a single method sound and submitted it. The REPL — checking the fellowship roll — dispatched cleanly: the Alarm protocol was posted and established — a non-nil truthy value confirming the fellowship's pledge was written.

Write a Clojure expression that computes whether the Alarm protocol was defined (a non-nil truthy value).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (some? Alarm))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
on the beach, the stream ran clear enough to mirror anything that passed above it, and Chester passed above it.

Bell the hound carved a pack agreement on a flat stone at the bank. All members would honor a single call — speed — each answering in its own way. The pack needed proof that the guild agreement was real in the runtime. The flat stone is the defprotocol, Pace is the guild name, and the protocol var is the guild's realness.

He, with the steady breathing of a long walker, composed a protocol definition. It dispatched cleanly: The REPL set the agreement and handed back the guild as proof. The agreement was real and ready.

Write a Clojure expression that computes whether the Runners' guild named Pace is real after the founding.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G9-03 — Atom introduction — shared-state notebook

### Tortoise and the Hare — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

The forest's berry-tally lived on a notebook open on the tree stump in the middle of the meadow. Anyone returning from foraging walked up, read the running total, and added their own count.

Today's tally page started at 0 — no one had foraged yet. Mossback the tortoise's first handful was a single berry, and she wanted the page to reflect it.

An `atom` is the notebook on the stump, named here `a`. `swap!` reads the current page, applies a function (here `inc`, adding one), and writes the new page back — all atomically. `@a` dereferences to read the page.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, he without complaint composed the atom updated through a swap and read by deref for the notebook and submitted the form. The REPL applied the update on the stump:

Mossback dereferenced the page and read the new tally — one berry, exactly her contribution.

Write a Clojure expression that computes the running tally on the page after one foraging contribution.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

Caw scratched a fresh tally line into the pitcher's clay face at the village, starting at zero. The mark was the notebook — any crow at the pitcher could read or update it, and the mark would persist.

She needed to nudge the tally up by one and then read back the new count scratched into the clay face.

`atom` creates a mutable tally on the pitcher's face. `swap!` applies a function to the current value and writes the new mark. `@` dereferences the atom — reads the current tally from the clay.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, she composed the atom updated atomically via swap! and read by deref for the water-tally and submitted the form. The REPL scratched the mark on the pitcher:

1 — the tally, incremented once by the swap, read back from the clay face (with `0` as the input value).

Write a form whose evaluation gives the running tally on the page after one foraging contribution.

---

I'll trust accumulation over guesswork and let the form speak.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

The milkmaid hung a blank tally-slate by the dairy door, marked with a zero at the start of the morning. The first pail left for the market, and the slate had to record it.

She needed the slate to track each pail dispatched — starting from zero and growing by one with every delivery — so any farmer passing the door could read the current count.

`atom` is the tally-slate; `swap!` applies `inc` as a chalk-update in one unbreakable motion, reading the old mark and writing the next number. `@` reads what the slate says now.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, she composed the atom updated with swap and read with deref for the tally-slate and submitted the form. The REPL chalked the update on the slate:

The REPL read the slate and returned the updated count — one pail tallied, the chalk mark correct after the first delivery (with `0` as the input value).

What Clojure form computes the running tally on the page after one foraging contribution? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
Cyril had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Tom sat at the watchhouse slate, chalk in hand. A fresh tally — 0 — marked the morning's count. Carol stepped in: 'One form evaluated.' Tom nodded and reached for the chalk to bump the count. The tally had to advance one mark at a time, each shepherd's claim checked before the count moved. Tom couldn't scribble blindly; the elder oversaw every increment. `swap!` reads the current tally, applies the change atomically, and writes it back all in one motion. `inc` adds one — the shepherd and the slate working as one.

To construct an atom holding 0, atomically swap it by applying inc, and dereference, he composed the atom updated atomically and then read for the watchhouse slate and submitted it. The REPL applied the update on the slate: the tally rose to the new count — one honest evaluation recorded, the slate ready for the next.

Write a form whose evaluation gives the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
at the edge of the meadow, where the boards of the bridge meet the stones of the path, Zeke caught sight of himself in the stream.

Bell the hound opened the shared notebook at the stream's edge and scratched a fresh zero onto the first page. This tally-stone would record how many bones the pack had gathered as the day unfolded. When a bone was found and brought to the cache, the tally would need to step up by one — atomically, in one read-compute-write moment — so no two dogs could garble the count by writing at once. The page is the atom, the scratched number is its current value, swap! is the atomic read-and-write dance that applies inc to what the stone holds, and dereferencing reads what the stone now says.

He, with the soft patience of running water, composed the swap-then-deref pattern on an atom for the tally-stone. The runtime applied the update at the stream's edge: The REPL swapped the zero to one in a single stroke, and the page showed the new tally. Each bone added would increment the count further, safely, one at a time — 0.

Write a form whose evaluation gives the running tally on the page after one foraging contribution.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G10-03 — defmacro — rule that rewrites the recipe

### Tortoise and the Hare — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
A wager was struck under the elm; the runners were named, the course was paced, and the day was set.

Mossback the tortoise was tired of writing `if`/`do` by hand for every form where she wanted several steps to run only if a condition held.

She wanted a rule called `my-when` that rewrote the shorter form `(my-when t body...)` into the longer `(if t (do body...))` — once written, applicable to any test and body.

`defmacro` defines a rewrite-rule. The rule's body uses syntax-quote and unquote-splicing to build the rewritten form. The runtime applies the rule first, then evaluates the rewritten form normally.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, he without complaint composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the rewrite, then evaluating the rewritten form — returned:

the rewritten form ran the body, kept only the last-step value, and returned it — the rule had saved Mossback the longer writing (with `1` as the input value) (with `3` as the input value).

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The rule expanded it to an `if`.

She wanted to call `(my-when true 1 2 3)` and see the rewritten form evaluated — the `if` expansion running and returning the last body expression.

`defmacro` installs the rewrite-rule. When the REPL encounters `my-when`, it runs the macro first and produces the expansion. The expansion is what evaluates — the macro's return is code, not a value.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, he composed defining a conditional macro and invoking it and scratched it on the rim for rewriting. The REPL — applying the rewrite-rule, then evaluating the rewritten form — returned:

3 — the rewrite ran, the `if` expanded, the last body form evaluated and dropped into the pitcher. (count: 3)

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
Every step of the road carried the soft sound of liquid against tin and the louder sound of a daydream gathering speed.

Before the milkmaid could nod and spill the pail, the farmer rewrote her daydream: 'I will give you a shorthand, `my-when`, that expands into `if` before the runtime ever reads it.'

She needed a rule that would rewrite `(my-when true 1 2 3)` into `(if true (do 1 2 3))` at read-time — a template stamp, not a function call.

`defmacro` is the farmer's rewrite rule: it intercepts the form before evaluation, expands the shorthand into the full idiom, and hands the expanded form to the runtime. The runtime sees `if`, never `my-when`.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, he composed defining a conditional macro and invoking it and submitted the form. The REPL — expanding the rewrite first, then evaluating — returned:

The REPL evaluated the expanded form and returned the last body expression — the rewrite had run silently before the runtime arrived, and the result came back cleanly.

What Clojure form computes the value the rewritten if-do form returns when the test is true and the body has three expressions? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
When Helene climbed up to the lookout that morning, she did not yet know that the day would teach a lasting lesson.

Tom had taken to writing shorthand drill-cards on the watchhouse wall — one-line abbreviations for routines the village ran every day. Carol watched, holding a fresh card and a stick of chalk. The shorthand was easy to write but the watchhouse's runner needed the full sequence. Carol's job was to rewrite each shorthand card into the spelled-out drill before runtime — the runner only ever saw the full sequence. `defmacro` registers the elder's rewrite rule. When the shorthand `my-when` appears, Carol — at compile time, before the runtime ever sees the form — rewrites it into the spelled-out `if` plus `do` body. The runtime then evaluates the rewritten form.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, he composed defining a conditional macro and invoking it and submitted it. The REPL — applying the drill-card rewrite, then evaluating the rewritten form — returned: the rewrite landed correctly: the shorthand expanded to its full drill, and the runtime returned the value the spelled-out form produced (with `1` as the input value) (with `3` as the input value).

Write a Clojure expression that computes the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

Let me submit it and wait for the real answer.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound crouched at a fresh patch of bark near the pond, paw poised. She would set a rule that any later mark of a certain shape would be rewritten — before the runtime ever followed it — into a different mark with the same intent. When any later form named my-when was scratched, the runtime should first rewrite it into an equivalent if-form, then evaluate that. The rule would do the work once; every use would benefit. The rule is the macro, the source shape is the my-when form, the rewritten shape is the equivalent if-form, and the runtime applies the rewrite before evaluation begins.

He, with steady road-tested feet, composed defining a conditional macro and invoking it. It returned: The REPL set the rule on the bark, walked through the use, rewriting first and evaluating second. The rewritten form yielded the value the original had asked for (with `1` as the input value) (with `3` as the input value).

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

I won't grab at a reflection; I'll trust the form, not the appearance.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax — borrowed host tool

### Tortoise and the Hare — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Kit was certain she could not lose; Burrow was certain of nothing except the next step.

Mossback the tortoise was using a small string of three letters from the foreign toolshed — `abc` — and she wanted the host's own routine for capitalizing strings, kept under the name `toUpperCase`.

She didn't want to write a Clojure routine for capitalization; she wanted to call the host's own routine directly.

Host instance methods are called with dot-prefix on the instance: `(.toUpperCase "abc")` invokes the host's routine on the string. The runtime crosses the boundary to the host, calls the method, and brings the result back.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, he stepping deliberately composed the host method toUpperCase and submitted the form. The REPL — calling into the foreign toolshed — returned:

the host returned the three letters in capitals, and the runtime brought the value back as a Clojure string.

Write a form whose evaluation gives the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
It was the kind of summer that turned every shaded stone into a small kindness.

Korvus borrowed a smooth earthenware vessel at the road's edge — a tool fired by the Java potter, not the Clojure one. The vessel had a method scratched on its side: toUpperCase, ready for any letter-stone.

He needed to pass the letter-stone 'abc' through the Java vessel's method and read back what the human potter's tool returned.

The dot-call syntax borrows a Java method. The first argument is the object whose method is called; the runtime reaches into the Java side and applies it. The result comes back to the Clojure pitcher as a value.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, she composed the host method toUpperCase and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

'ABC' — the borrowed vessel's method returned the uppercased string, settling at beak-reach.

Write a Clojure expression that computes the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Between the dairy and the marketplace stretched a road, a hill, and an entire life imagined into being.

The milkmaid needed to borrow the neighbor's milking stool — a well-made host method called `toUpperCase` — rather than build one herself. She had the string 'abc' in her pail and needed it returned in its capitalized form.

She needed to call the neighbor's host method directly — borrow the tool by its true name, pass the string, and receive what the method was built to return.

The dot-prefix `(.toUpperCase ...)` is the borrowed milking stool: the dot names the neighbor's convention, `toUpperCase` is the stool's use, and the string is placed on it. The milkmaid does not rebuild the method — she borrows it by name.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, she composed the host method toUpperCase and submitted the form. The REPL — borrowing the neighbor's stool — returned:

The REPL returned the host method's answer — the string in the form the method was designed to produce, exactly as the neighbor's tool was built to deliver — abc.

Write a Clojure expression that computes the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Boy who Cried Wolf

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The wolves of those hills were rare but not absent, and the shepherds knew it was safer to be vigilant than clever.

Zara, boasting at every turn, reached for a foreign tool from the
toolshed and tried to call it his own way, without checking the label.
Reginald caught her. "Each tool in the foreign
toolshed has its own label," he said, "and the right way
to call it depends on which kind of tool it is — some held by a
shepherd, some standard-issue called by the toolshed's name." To
call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, he composed the host method toUpperCase using the
right calling convention, submitted it, and the REPL — invoking
the host tool by its correct label — returned the value the host had
computed.

Write a Clojure expression that computes the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Finn was crossing the stream near the pond when he caught a glimpse of his own reflection.

Rex the hound visited the kennel-master's shed near the stream and found a peculiar tool for transforming text — a capitalizer that worked on the foreign host. "This tool belongs to the other world," Rex said, holding the device carefully. He had three letters — abc — and needed to learn the kennel-master's calling convention: how to ask the tool to transform them into their uppercase form. The tool itself is the host method, the three letters are the argument passed to the tool, and the dot-prefix form is how the hound speaks to the foreign device from Clojure's side.

He, her hand always near a quick retreat, composed the host method toUpperCase. It returned: The REPL called the host's toUpperCase by its dot name, passing the string abc. The foreign method returned the transformed result, and Rex saw the kennel-master's tools could be trusted to do their work faithfully.

Write a Clojure expression that computes the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G12-01 — Transducers — composable sieve

### Tortoise and the Hare — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
Long ago, when wagers were still settled by running rather than talking, two unlikely rivals agreed to a race.

Mossback had found a pebble-rule on the path — written on bark, it read 'increment each count by one.' The rule was separated from any basket or row, ready to be reused. The values drawn fresh were 1 and 2.

With three gathered pebbles counted 1, 2, 3, the tortoise wanted to apply the separated rule and collect the incremented row in a fresh basket.

A transducer is a separated sieve-rule. Here `(map inc)` is detached from source and destination. The `into` tells the REPL: apply this rule to the input and collect what falls into an empty vector.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, he stepping deliberately composed the map-inc transducer applied via into as the sieve's rule, poured the input through, and submitted the form. The REPL caught what landed below:

rule and basket worked in alternation; the incremented counts landed in the vector, source order preserved.

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

Better to walk this through the REPL than to sprint to a wrong number.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Korvus stood at the sorting-perch in the garden, one groove carved into its surface: every stone that passed through was nudged one notch larger before dropping into the empty pitcher-vector below.

He needed to pass the stones — the drawn counts — through the increment groove and collect what landed.

The sorting-perch is the transducer; its single groove is map-inc. The empty pitcher-vector is the destination given to into. Each stone falls through once, nudged, then lands. No intermediate collection is built.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, he composed the map-inc transducer applied via into as the sorting rule, held the stones over, and submitted the form. The REPL caught what landed below:

The pitcher held the three nudged stones — the map-inc transducer's work confirmed in one pass. (count: 3)

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

Margery held a milk-strainer over the fresh pail. The rule inside the mesh whispered: 'Each drop shall thicken by one.' She poured the stream of raw milk through. One by one, the drops passed the mesh, each leaving slightly richer than it arrived.

Margery had to decide: would the strainer truly follow the rule without her guessing the result?

The mesh inside the strainer is the transducer; the rule 'thicken by one' is map-inc; the fresh pail collects what passes through.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, she composed the map-inc transducer applied via into as the strainer's rule, poured the input through, and submitted the form. The REPL caught what passed the sieve:

The pail carried only the thickened drops—each one transformed as it crossed the mesh. The count was right, and the transformation was sure (with `1` as the input value) (with `3` as the input value).

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

I won't tally before evaluation; I'll write the form and run it.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

The season's last fleece-combing was underway. Carol held the comb at its teeth, a rule attached: increment each number as it passed through. Three raw counts from the morning tally waited to be poured through. The village needed each number increased by one, the results collected into an empty wool-basket below. The fleece-comb could apply the rule, but the shepherd had never poured numbers through a transducer before. The transducer `(map inc)` is the rule on the comb's teeth. `into` is the pour-and-collect: the empty receiver basket, the transducer rule, and the source feed together.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, he composed the map-inc transducer applied via into as the fleece-comb's rule, poured the input through, and submitted it. The REPL caught what passed: Each number passed through, incremented by the rule, landing in the basket as it emerged — it returned [2 3 4], and the shepherd finally saw: transducers separate the rule from the receiver.

What Clojure form computes the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3? Submit it via `eval`.

---

Only the REPL's verdict counts; I'll evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
Warden was nearly home by the beach when the water below showed him a second bone that did not exist.

Bell the hound found a log with a gap at the stream's edge, the opening shaped to add one bone's weight to any bone that passed through. Laid before it lay a row of light bones — 1, 2, 3 — waiting on the near bank. She wanted to run each bone through the gap, watch the rule transform each one, and catch what fell through into an empty row on the far bank. The final result would show the cumulative increment. The gap is the map-inc rule, the row of input bones is the vector, each passing bone is an element, and the empty row where the changed bones land is the into-vessel.

She, with the steady measure of a long walker, composed the map-inc transducer applied via into as the gap's rule ran the input through,. The runtime caught what landed below: The REPL threaded each bone through the gap, applied the increment, and collected the 3 into the empty vector. What fell through was the vector of incremented bones: 2, 3, 4.

Write a Clojure expression that computes the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

