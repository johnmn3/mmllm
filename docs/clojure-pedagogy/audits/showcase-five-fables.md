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

**form**: `23`  •  **expected**: `23`

````text
Anyone passing near the meadow that morning would have seen Poppy stretching for show while Rhizome simply began.

At a moss-covered milestone by the meadow, Poppy the hare sketched a small
wager into the path: whoever guessed the result of `23`
first would win the right to set the next race. Rhizome the tortoise,
stepping deliberately, said it was simpler to type the form into the REPL
than to argue about the value 23.

Question: write a Clojure expression for the value of 23.

---

{"tool_calls":[{"name":"eval","args":{"form":"23"}}]}
````

### Crow and the Pitcher

**form**: `66`  •  **expected**: `66`

````text
Smoke the crow was no fool, and on the hilltop the day demanded thinking rather than complaining.

A wooden sign nailed to a tree atop the hilltop carried a puzzle. The riddle
was simple: it asked the reader to evaluate `66`. Crafty
laughed, clicking the beak in self-satisfaction, and declared it too easy. Smoke said
patiently that the only way to be sure of the value 66 was to put
it in the REPL.

Question: write a Clojure expression for the value of 66.

---

{"tool_calls":[{"name":"eval","args":{"form":"66"}}]}
````

### Milkmaid and her Pail

**form**: `23`  •  **expected**: `23`

````text
near the orchard, before the cocks had finished crowing, Cosima had set out with the milk and a head full of plans.

Cosima chalked a wager on a flat stone in the orchard: whoever
predicted the result of `23` would set the next race's
distance. Zacharias, with steady, careful steps, said it would be simpler
to type the form into the REPL than to bicker about the value 23.

What Clojure form computes the value of 23? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"23"}}]}
````

### Boy who Cried Wolf

**form**: `47`  •  **expected**: `47`

````text
near the woods, in the long grass above the village road, Bertrand settled in for another slow afternoon.

Clementine had been trying to teach Bertrand how the REPL
works. "Look here," she said, pointing to the value 47.
"You hand the form `47` to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
Bertrand, worn from too many false starts, agreed to try.

What Clojure form computes the value of 47? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"47"}}]}
````

### Dog and the Shadow

**form**: `42`  •  **expected**: `42`

````text
in the pond, where the path crosses the stream, Trailblazer the dog trotted home with a fine bone in his teeth.

Trailblazer the dog had been keeping a small leather notebook of every
form he had successfully evaluated. Today by the pond, the
next entry was the value 42. Ginger the dog peered over
his shoulder at the form `42` and asked what
it would come out to.

Write a Clojure expression that computes the value of 42.

---

I'll set the form down faithfully and let it run.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## G1-13 — L2 application — first arithmetic call

### Tortoise and the Hare — *story-scaffold render*

**form**: `(+ 1 8)`  •  **expected**: `9`

````text
Ferret the hare liked to talk; Walnut the tortoise liked to listen, and the rivalry between them had grown into a small legend on the hilltop.

Mossback had sorted this morning's acorns into two small heaps beside the trail — one heap of 1 and another of 8.

She needed the running total before deciding whether to carry them all or leave some behind.

`+` is the counting-together operator: the two heap sizes are its arguments, and the runtime combines them into a single count.

To add 1 and 8, He composed the addition and submitted the form. The REPL counted out the answer:

the runtime returned the combined count — the two heaps tallied into one.

Write a form whose evaluation gives the sum of 1 and 8.

---

I'll keep the form honest and let the evaluator finish it.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 8)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(+ 1 9)`  •  **expected**: `10`

````text
at the market, a single pitcher held the last of the water, and Highwing the crow arrived too parched to be picky.

Korvus crouched at the tall clay pitcher's rim at the farm's yard, two handfuls of smooth stones — one stone in his left talon, two in his right.

He wanted to count the total stones in both talons to know how far the water would rise when both handfuls dropped together.

`+` is the stone-count call: it totals the numbers it receives, left to right. One stone plus two stones gives a total the runtime calculates and returns as the water-level.

To add 1 and 9, He composed the addition and submitted the form. The REPL counted out the answer:

The two handfuls combined, the water rising to the expected notch at beak-reach.

Write a form whose evaluation gives the sum of 1 and 9.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 9)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(+ 9 5)`  •  **expected**: `14`

````text
Milk does not forgive a tilted head, but a dreaming mind seldom remembers as much.

The farmer set two small coin-piles on the tally table: one pile of a single copper, and another of two. She needed the total before she could mark the day's earnings on the tally-slate.

She needed a form that added the two piles together — not guessing, not daydreaming, but submitting the sum to the REPL and reading what came back.

`+` is the farmer's tally rule: it stacks all the given coin-piles into one and hands back the total. No pail-nodding, no guesswork — just the arithmetic result.

To add 9 and 5, He composed the addition and submitted the form. The REPL counted out the coins:

the REPL returned the total the farmer had tallied — three coins, exactly as the two piles combined.

Question: write a Clojure expression for the sum of 9 and 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 9 5)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(+ 8 4)`  •  **expected**: `12`

````text
near the village, on a slope above the village, Jelena watched his flock and his shadow grow longer.

At dawn, Tom had brought lambs back from the south pasture and Carol had brought lambs from the north. They stood at the fold counting together, the village's morning record waiting on them.

The combined morning tally needed to settle correctly before the day's work could begin — the village's records depended on exact arithmetic, no boasting and no fudging.

`+` adds its operands one after another and gives back the running total. The runtime carries the sum exactly — no shouting required.

To , She composed the form (+ 8 4) and submitted the form. The REPL counted out the answer:

the count came back — the morning's flock confirmed by the runtime, not by Tom's memory.

Write a form whose evaluation gives the result of (+ 8 4).

---

No premature shouting; I'll evaluate the expression.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 8 4)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(+ 2 5)`  •  **expected**: `7`

````text
The path home wound past a slow brook, and on bright days the brook was full of borrowed shapes.

Bell the hound sat by a flat stone near the pond and laid out two small piles of bones — one of one bone, one of two — careful with the count.

She wanted the precise size of the heap if both piles were nudged together — small or large, the runtime would give the exact number, and that was the count she would carry forward.

The bones are the numbers, the piles are the operands, the act of nudging-together is +, and the count of the combined heap is what the REPL hands back.

To add 2 and 5, She composed the addition and submitted the form. The REPL counted out the answer:

The REPL added the two piles and handed back the precise count. Bell brushed the bones back into a single tidy heap — the answer settled, no eyeballing needed.

Write a form whose evaluation gives the sum of 2 and 5.

---

Let me commit the actual form and let the evaluator decide.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 2 5)"}}]}
````

---

## G2-13 — and/or short-circuit — chain of gates

### Tortoise and the Hare — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
Burrkin announced the race in a voice loud enough to wake the owls, and Walnut accepted with a nod.

Two small wooden gates stood at the start of the meadow trail. Each gate's verdict-stone was carved with the value the runner would carry to it — and today's two stones both read true.

Mossback the tortoise wanted to know whether both gates would let the runner through together, or whether the first one would close and stop the chain.

`and` walks the gates left to right: the first false closes the chain and that value comes back; otherwise the value at the last gate is what comes back. With both stones reading true, the chain holds and the last gate's true is the verdict.

To test whether two trues both pass through an and-chain of gates, She composed the logical and and submitted the form. The REPL let the gates decide:

both gates stood open, and the value at the last gate — true — passed back as the chain's verdict.

Question: write a Clojure expression for the result of passing true and true through the and-chain of gates.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
Headwind the crow arrived at the farm with no plan but a sharp eye and a willingness to take small steps.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verdict only if every gate along the chain was open — a single closed gate would block the path.

`and` checks each gate in order; if the first is open it moves to the next. Both true means both gates are open, so `and` returns the last value it checked.

To test whether two trues both pass through an and-chain of gates, He composed the logical and and held it at the dual-gate check. The REPL opened or closed the gates as the logic demanded:

Both gates passed and the expected value arrived at the rim.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
It was the season of new chicks and first cheeses, and every small profit felt like the start of a larger one.

The farmer had two gates on the farmyard path: the first opened when the condition was true, the second also opened when its condition was true. She wondered if both gates would open together.

She needed to check if the first condition was true AND the second condition was also true, without guessing or testing separately.

The logical and is the farmer's gate-chain: both gates must pass (both true) for the journey to continue. If the first gate closes (false), the whole chain fails. If the first passes, check the second.

To test whether two trues both pass through an and-chain of gates, He composed the logical and and submitted the form. The REPL let the gate decide:

the REPL returned true — both gates opened, the and-chain was complete.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

Better to walk carefully than to spill the answer; I'll evaluate.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
It is a serious thing to call for help, and a more serious thing to call for it falsely.

Two fold-gates stood in the shepherd's path: the first open (true), the second open (true). The shepherd wanted to know if both gates allowed passage.

Both gates had to be open for passage. Tom saw the first was open; Carol insisted the form would confirm both were passable.

`and` checks the first gate (true), walks through, checks the second gate (true), and returns true only if all gates pass.

To test whether two trues both pass through an and-chain of gates, He composed the logical and and submitted the form. The REPL let the fold-gates decide:

the form returned true, and the shepherd could walk straight through both gates.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(and true true)`  •  **expected**: `True`

````text
Olive the dog was nearly home on the village when the water below showed him a second bone that did not exist.

Bell the hound stood at the stream bank, facing two test gates placed one after the other. Each gate bore a mark: true, then true.

She wanted to cross if both gates would let her pass. The and would test each one in turn — if either blocked her, the chain would fail.

Each gate is one condition, the and is the chain that checks them in sequence, and the verdict is true only if all pass her through.

To test whether two trues both pass through an and-chain of gates, He composed the logical and and submitted the form. The REPL let the crossing-conditions decide:

The REPL tested true at the first gate — it opened. True at the second gate — it opened too. Both conditions held, and the verdict came back true. She could cross.

Write a Clojure expression that computes the result of passing true and true through the and-chain of gates.

---

{"tool_calls":[{"name":"eval","args":{"form":"(and true true)"}}]}
````

---

## G3-03 — let — local binding (the temporary-pouch metaphor)

### Tortoise and the Hare — *story-scaffold render*

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
Anyone passing along the road that morning would have seen Dart stretching for show while Sienna simply began.

Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth 3 acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x.

Just past the next milestone she'd want the running total — what x plus one more acorn would come to. After the milestone, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 1)`, x means 3; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, He composed the local binding and addition with the binding tucked safely into the pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded 3, the +1 added a fourth acorn, and the running total stood at 4 — exactly what the next milestone needed.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(let [x 8] (+ x 7))`  •  **expected**: `15`

````text
There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and named: x, holding three.

He needed to know how far the water would rise if he added one more stone to whatever was tucked under his wing.

`let` gives a name to a tucked value: x binds 8 for the span of the form. Inside that stretch, `(+ x 7)` reaches under the wing and adds one. When the form ends the wing opens; the binding dissolves.

To bind a value of 8 to a local name x for one stretch, then return that value plus one, He composed the local binding and addition with the binding tucked safely under a wing and submitted the form. The REPL reached under the wing as the form directed:

4 — the tucked count of three, plus the one stone added while the wing held it firm.

Write a Clojure expression that computes the running total after binding x to 8 and adding 7.

---

Let me build the expression slowly, the way water rises by pebbles.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 8] (+ x 7))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(let [x 4] (+ x 5))`  •  **expected**: `9`

````text
The pail sat steady on Danuta's head as she started down the lane along the road.

The milkmaid tucked the number 4 into her apron-pocket at the start of one stretch of the road — a private count, good only for this leg of the journey to market.

She needed to reach into the pocket at the next step and add 5 to the count, then let the pocket empty when the form ended.

`let` is the apron-pocket: it tucks `x = 4` into the pocket for the duration of the body. `(+ x 1)` draws from the pocket and adds 1. When the body ends, the pocket is put away and `x` ceases to exist.

To bind a value of 4 to a local name x for one stretch, then return that value plus one, He composed the local binding and addition with the value tucked into the apron-pocket and submitted the form. The REPL reached into the pocket as the form directed:

the REPL returned 4 — the count from the pocket incremented by one, the pocket now set aside at the road's end.

Question: write a Clojure expression for the running total after binding x to 4 and adding 5.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 4] (+ x 5))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(let [x 2] (+ x 9))`  •  **expected**: `11`

````text
Eduardo was a clever boy, and by the forest cleverness had begun to look very much like trouble.

Carol the elder had been counting along a stretch of fence-line at dawn. She slipped a tally-token worth 2 lambs into the small leather belt-pouch at her hip and gave the pouch's contents the local name x for that stretch of watch.

By the next fence-post she would want the running total — what x plus one more lamb came to. Past that post, the pouch would empty and x would mean nothing again.

`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x 9)`, x means 2; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch.

To bind a value of 2 to a local name x for one stretch, then return that value plus one, She composed the local binding and addition with the binding tucked safely into the belt-pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded 2, the +9 added a fourth lamb, and the running total stood at 4 — exactly what the next fence-post called for.

Question: write a Clojure expression for the running total after binding x to 2 and adding 9.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 2] (+ x 9))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(let [x 4] (+ x 3))`  •  **expected**: `7`

````text
Buster the dog was crossing the stream at the edge of the pond when she caught a glimpse of his own reflection.

Bell the hound had picked up a small bone near the pond and held it firmly between her jaws. Just for the next stretch of crossing she would need to know the bone's tally — 4 — by a short local name x.

She wanted the running total — what x plus one more would come to — at the moment her paw left the far bank. After that stretch, the mouth would empty and x would mean nothing again.

The closed jaws are the let-binding, x is the name for what's gripped between the teeth, the value held there is 4, and the form's stretch is the crossing. Outside the form, the mouth empties and the binding goes with it.

To bind a value of 4 to a local name x for one stretch, then return that value plus one, She composed the local binding and addition with the binding gripped safely between the teeth and submitted the form. The REPL pulled from the mouth as the form directed:

The REPL pulled from the mouth as the form directed and handed back the running total. Past the crossing, Bell's mouth was empty again — the binding had been in force only for that stretch.

Question: write a Clojure expression for the running total after binding x to 4 and adding 3.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 4] (+ x 3))"}}]}
````

---

## G4-08 — assoc — pin a tag on the basket

### Tortoise and the Hare — *story-scaffold render*

**form**: `(assoc {:guava 9, :kiwi 1, :persimmon 9, :lemon 20} :warm 5)`  •  **expected**: `{('__kw__', 'guava'): 9, ('__kw__', 'kiwi'): 1, ('__kw__', 'persimmon'): 9, ('__kw__', 'lemon'): 20, ('__kw__', 'warm'): 5}`

````text
Word went around near the forest that two creatures had agreed to settle an old question with their feet.

Mossback the tortoise's foraging-basket had compartments stitched into its sides — an open area at the top, plus named pouches :a and :b. Pouch :a already held 1 acorn from the morning's gathering.

Pip the hare arrived from the orchard with 5 more acorns. Mossback decided they belonged in pouch :b — and pouch :a's acorn should stay exactly where it was.

`assoc` associates a value with a named compartment of the basket. The basket's shape stays the same — :a still holds its 1, and :b now holds the new 5 — exactly as the foraging called for.

To associate value 5 with the :b compartment of a basket already binding :a to 1, He composed the assoc operation for the basket and submitted the form. The REPL handed back the arrangement:

the basket carried both — 1 in :a, 5 in :b — ready for the rest of the day's gathering.

Write a form whose evaluation gives the basket after associating value 5 with the :b compartment.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:guava 9, :kiwi 1, :persimmon 9, :lemon 20} :warm 5)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(assoc {:nectarine 14, :grape 11} :south 2)`  •  **expected**: `{('__kw__', 'nectarine'): 14, ('__kw__', 'grape'): 11, ('__kw__', 'south'): 2}`

````text
In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Caw held a one-compartment stone-pile at the orchard pitcher — :a with one stone. A second compartment, :b, needed to be scratched in and filled with two stones.

The original pile had to stay as it was; `assoc` should return a new pile that also had the :b compartment filled.

`assoc` scratches a new compartment into a copy of the pile and fills it. The original pile keeps only :a; the returned new pile holds both :a and the fresh :b compartment.

To associate value 2 with the :b compartment of a basket already binding :a to 1, She composed the assoc operation for the stone-pile and submitted the form. The REPL handed back the arrangement:

The REPL returned the extended pile with both compartments present, the original unchanged.

Write a Clojure expression that computes the basket after associating value 2 with the :b compartment.

---

I'll let the REPL raise the answer the way pebbles raise water.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:nectarine 14, :grape 11} :south 2)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(assoc {:blackberry 7, :nectarine 11, :elderberry 2, :lychee 1} :a 3)`  •  **expected**: `{('__kw__', 'blackberry'): 7, ('__kw__', 'nectarine'): 11, ('__kw__', 'elderberry'): 2, ('__kw__', 'lychee'): 1, ('__kw__', 'a'): 3}`

````text
The road from the farm to the town was long, and a daydream could fit comfortably along its length.

The milkmaid held a market-basket with one labeled compartment: :a held the value 1. She stood at the buyer's stall, ready to add a second compartment labeled :b to hold the value 3.

She needed a new basket keeping the original :a binding while adding a fresh :b compartment. The old basket would remain untouched; a new one would carry both bindings.

The `assoc` operation builds a new basket: the assoc form takes the original basket and creates a fresh one with the :a binding intact and a new :b compartment added. The old basket stays as it was.

To associate value 3 with the :b compartment of a basket already binding :a to 1, He composed the assoc operation for the market-basket and submitted the form. The REPL handed back the arrangement:

the REPL handed back a new basket with both bindings — :a still pointing to 1, :b now pointing to 3, the original basket sitting untouched behind.

Write a form whose evaluation gives the basket after associating value 3 with the :b compartment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:blackberry 7, :nectarine 11, :elderberry 2, :lychee 1} :a 3)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(assoc {:guava 14, :pear 2, :mango 14, :fig 4} :near 6)`  •  **expected**: `{('__kw__', 'guava'): 14, ('__kw__', 'pear'): 2, ('__kw__', 'mango'): 14, ('__kw__', 'fig'): 4, ('__kw__', 'near'): 6}`

````text
There was once a shepherd boy whose afternoons were long and whose imagination was longer.

Carol held a wool-basket with one pouch labeled `:a` holding 1 fleece. A fresh delivery brought new fleeces that needed a second pouch labeled `:b` with 6 pieces.

The form had to add the new pouch to the basket and return an updated basket with both pouches, leaving the original unchanged.

`assoc` adds or updates a key-value pair in the map. It takes the old basket, the new key `:b`, and its value 6, returning a fresh basket that holds both the original `:a` and the new `:b`.

To associate value 6 with the :b compartment of a basket already binding :a to 1, He composed the assoc operation for the wool-basket and submitted the form. The REPL handed back the arrangement:

the form returned a new basket showing both `:a` 1 and `:b` 6, while the original single-pouch basket stood untouched.

Write a form whose evaluation gives the basket after associating value 6 with the :b compartment.

---

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:guava 14, :pear 2, :mango 14, :fig 4} :near 6)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(assoc {:quince 17, :persimmon 18, :mandarin 19, :kiwi 16} :first 7)`  •  **expected**: `{('__kw__', 'quince'): 17, ('__kw__', 'persimmon'): 18, ('__kw__', 'mandarin'): 19, ('__kw__', 'kiwi'): 16, ('__kw__', 'first'): 7}`

````text
It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Patch the hound held a hollow log cache with one compartment named :a that held 1 bone. The cache was ready to receive a new compartment. Patch marked out a fresh section and labeled it :b, then placed 7 bones inside.

Patch wanted the REPL to take the existing cache, add the new compartment :b with its 7 bones, and return the extended cache without disturbing what :a held.

The original hollow log is the map {:a 1}, the new compartment name is :b, the new bone-count is 7, and assoc is the operation that adds the slot.

To associate value 7 with the :b compartment of a basket already binding :a to 1, He composed the assoc operation for the bone-cache and submitted the form. The REPL handed back the arrangement:

The REPL extended the cache by one compartment, placing 7 bones in the :b slot while :a kept its 1 bone. The expanded cache came back intact.

Write a Clojure expression that computes the basket after associating value 7 with the :b compartment.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(assoc {:quince 17, :persimmon 18, :mandarin 19, :kiwi 16} :first 7)"}}]}
````

---

## G5-12 — reduce — walk the row carrying a tally

### Tortoise and the Hare — *story-scaffold render*

**form**: `(reduce + [4 9 8 2 13])`  •  **expected**: `36`

````text
A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

A row of four small pebbles lay along the path — counts of 1, 2, 3, and 4 from four foraging trips.

Mossback the tortoise wanted the grand total of the four trips. Walking the row and carrying a running tally was the patient way.

`reduce` walks the collection from left to right carrying a tally. At each pebble, the combine function (here `+`) is applied to (tally, pebble), producing the new tally. The final tally is what comes back.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, He composed the fold operation and submitted the form. The REPL walked the row carrying the tally:

the walk produced a tally that grew across the four pebbles, ending at the grand total of all four trips.

Write a form whose evaluation gives the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

I let the REPL do the evaluation.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [4 9 8 2 13])"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(reduce + [8 9 3 14])`  •  **expected**: `34`

````text
When Ebon landed by the garden wall, she saw the water and saw the distance, and stood very still.

Caw walked the garden tallywalk beside four stones in a row: 1, 2, 3, 4. She carried a running tally in her wing-cache, combining each stone with `+` as she stepped past.

She needed the final tally after combining all four stones with addition, stone by stone from left to right.

`reduce` walks the sequence, folding each element into an accumulator using the given function. Starting from the first stone, each step adds the next, building the running total.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, She composed the fold operation and submitted the form. The REPL walked the rim carrying the tally:

The tallywalk ended after the fourth stone; the running tally reached its final sum and dropped into the pitcher.

Write a Clojure expression that computes the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [8 9 3 14])"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(reduce + [3 6 17 14 17])`  •  **expected**: `57`

````text
The sun had only just cleared the hedgerows when the day's first tally of imagined coins began.

The milkmaid walked to market counting coins step by step: one coin at the first stall, two at the second, three at the third, four at the fourth. At each stall she added the new coins to her running tally.

She needed to step through each stall, combine its count into the running tally with `+`, and carry that tally forward to the next — one tally-walk, not four separate additions.

`reduce` with `+` is the tally-walk: the milkmaid starts with the first element, then steps through the rest, combining each into the running total with the `+` step until the row is done.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, He composed the fold operation and submitted the form. The REPL walked the collection carrying the tally:

the REPL returned the accumulated total — the tally the milkmaid had built coin by coin across all four stalls.

Write a form whose evaluation gives the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [3 6 17 14 17])"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(reduce + [3 10 5])`  •  **expected**: `18`

````text
The pasture lay below a rocky lookout, and the sheep were easier to count than the hours.

Tom walked the tally-stick down a line of sheep.

Tom needed to combine all the numbers into a single total.

`reduce` takes a combination-rule and applies it across the list.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, She composed the fold operation and submitted the form. The REPL walked the row, notch by notch on the tally-stick:

The form combined all values into a single result.

Write a form whose evaluation gives the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

Let me submit the form and wait for the verdict.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [3 10 5])"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(reduce + [4 14 19 15 11])`  •  **expected**: `63`

````text
A dog with a bone in his jaws is a happy creature; a dog who looks too hard at the water may not be.

Patch the hound stood at the stream near the forest, facing a row of pebbles marked 1, 2, 3, 4 laid end to end. She would walk the row, carrying a tally in her jaws, adding each pebble to the tally as she passed it. The final tally would be her answer.

She wanted the sum of all pebbles in the row. Reduce walks the row left to right, combining each pebble with a running total using the + rule.

The reduce-form is the tally-walk. The pebbles are 1, 2, 3, 4. The combination-rule is +. Each step adds the current pebble to the tally. The final tally is what reduce returns.

To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total, She composed the fold operation and submitted the form. The REPL walked the bone-row carrying the tally:

The REPL began the walk with no tally and pebble 1 (tally=1), added pebble 2 (tally=3), added 3 (tally=6), added 4 (tally=10). The final tally came back as the answer.

Question: write a Clojure expression for the running tally after walking 1, 2, 3, 4 with + as the combine step.

---

Let me write what is there, not what it seems to promise.

{"tool_calls":[{"name":"eval","args":{"form":"(reduce + [4 14 19 15 11])"}}]}
````

---

## G6-03 — require — borrow a routine from a foreign scroll

### Tortoise and the Hare — *story-scaffold render*

**form**: `(clojure.string/upper-case "amber")`  •  **expected**: `'AMBER'`

````text
Two creatures of very different gait once agreed that the ground between two stones would settle a long argument.

The library by the road kept a scroll on its shelves called `clojure.string`. Among its signs was a routine named `upper-case` — a routine that took a string and returned the same letters, capitalized.

Mossback the tortoise wanted the capitalized form of the four-letter word `amber`, for a road-sign she was painting.

When a routine lives on a scroll, you call it by both names together: scroll-name slash routine-name — `clojure.string/upper-case`. The runtime fetches the scroll and invokes the routine on the argument.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string amber, He composed calling a fully-qualified string function and submitted the form. The REPL read the signs and replied:

the routine returned the four letters in capitals, ready for the road-sign Mossback was painting.

What Clojure form computes the capitalized form returned by the upper-case routine on the scroll? Submit it via `eval`.

---

I'll let the REPL settle this, no point arguing about arithmetic.

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"amber\")"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(clojure.string/upper-case "alder")`  •  **expected**: `'ALDER'`

````text
at the edge of the garden, where the heat shimmered above the stones, Chrysocolla the crow began the slow business of solving thirst.

Sable perched at the pitcher in the meadow, a flat stone already required from the string-scroll's shelf. She scratched the fully-qualified call using the scroll's shelf-name and the upper-case groove.

She needed the four-letter word returned in its capitals — the shelf held the method, but the full path was required to reach it across the namespace boundary.

The `namespace/function` carving tells the runtime which shelf to pull from before calling. The required shelf answers with the uppercased characters, the slash linking shelf to groove.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string alder, He composed calling a fully-qualified string function and submitted the form. The REPL read the rim-carvings and replied:

The pitcher returned the four letters in their capital form, the fully-qualified call resolved cleanly.

What Clojure form computes the capitalized form returned by the upper-case routine on the scroll? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"alder\")"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(clojure.string/upper-case "raven")`  •  **expected**: `'RAVEN'`

````text
On market mornings, the dairy yard smelled of damp grass and warm tin, and the future seemed safely arrangeable.

The market-board in the village square listed the clojure.string vendor's section. The milkmaid had a word written in small letters and needed to use the board's registered uppercasing service to produce the full-capitals version.

She needed to consult the board, locate the vendor's section, and call the uppercasing routine — without that board entry she could not reach the function by its full qualified name.

The board's namespace section is `clojure.string`; the vendor's listed routine is `upper-case`. Reading the board entry and calling it produces the transformed output.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string raven, She composed calling a fully-qualified string function and submitted the form. The REPL read the market-board and replied:

the REPL returned the all-capitals version of the word, confirming the board-listed routine had been reached and applied correctly.

Write a Clojure expression that computes the capitalized form returned by the upper-case routine on the scroll.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"raven\")"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(clojure.string/upper-case "feather")`  •  **expected**: `'FEATHER'`

````text
Eitan had been told the rules plainly: cry only when the wolf is real, and never when he is bored.

Carol led Tom to the village smithy, where a master crafts strings in their furnace. On the smithy's post hung the sign `clojure.string/upper-case`—a foreign tool the smith had left for any shepherd to borrow.

Tom wanted to shout the answer about what `upper-case` would do to the word "feather", but Carol insisted he borrow the smith's tool and watch what it actually returned.

The fully-qualified name `clojure.string/upper-case` reaches across the namespace boundary to the smithy's tool. Calling it with "feather" borrows the smith's transformation.

To , He composed the form using clojure.string/upper-case on "feather" and submitted the form. The REPL read the notice-post and replied:

Carol wrote the form into the REPL, crossed into the smithy by name, and the smith's tool returned "WOLF". Tom learned: the namespace slash is the boundary you must cross by name.

Write a form whose evaluation gives the upper-cased string "WOLF".

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"feather\")"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(clojure.string/upper-case "thistle")`  •  **expected**: `'THISTLE'`

````text
at the edge of the forest, the path bends down to meet the water, and Milo the dog stopped at exactly the wrong moment.

Bell the hound found a scroll in the riverbank cache bearing the name clojure.string. A routine written there was called upper-case. She wanted to send the text "thistle" through that routine and see what came back in a different form.

She needed to call the fully-qualified routine, naming both the scroll and the function, so the runtime could find the right tool.

The scroll clojure.string is the library, the upper-case function is the routine written there, and the text "thistle" is the message to be transformed.

To call the upper-case routine on the clojure.string scroll, applied to the four-letter string thistle, He composed calling a fully-qualified string function and submitted the form. The REPL read the markers and replied:

The REPL reached into the scroll, found the routine, and applied it to the text, handing back the result in capitalized form.

What Clojure form computes the capitalized form returned by the upper-case routine on the scroll? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(clojure.string/upper-case \"thistle\")"}}]}
````

---

## G7-02 — try / catch — net under the leap

### Tortoise and the Hare — *story-scaffold render*

**form**: `(try (/ 3 3) (catch Exception e -53))`  •  **expected**: `1`

````text
A path ran from the old oak to the river stone, and on it many a boast had been measured against many a steady step.

Mossback the tortoise was about to ask the runtime for the result of dividing 3 acorn into 3 piles — a division she knew would throw, because dividing by zero isn't a thing the runtime can do.

She didn't want the throw to end the run. She wanted the form to come back with -3 as a placeholder so the rest of the work could continue.

`try`/`catch` is a net beneath the leap. The throw still happens, but the catch-arm catches the Exception cleanly. Whatever the catch-arm returns is what the form yields — here, the placeholder -3.

To attempt to divide 1 by 3; when the runtime throws, catch the Exception and return -53 from the catch arm, She composed the handler for a division-by-zero error and submitted the form. The REPL — net in place — handed back the value:

the throw happened, the catch caught it, and the form yielded -3 — the placeholder Mossback had specified.

Write a Clojure expression that computes the value the catch arm returns when the divide-by-zero throw is caught.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 3 3) (catch Exception e -53))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(try (/ 7 8) (catch Exception e -85))`  •  **expected**: `Fraction(7, 8)`

````text
On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw leaned over the pitcher with a risky stone in her talon — a division of one stone across zero, a form the REPL would refuse. Korvus had laid a soft moss pad below to catch any falling stone safely.

She wanted the risky form tried; if the stone fell badly, she needed the moss to return -7 instead of letting the crash stand unresolved.

`try` attempts the body. If an exception is thrown, `catch` intercepts it — the moss catches the stone — and the handler returns the fallback. The crash is absorbed; the fallback surfaces.

To attempt to divide 1 by 8; when the runtime throws, catch the Exception and return -85 from the catch arm, She composed the handler for a division-by-zero error and submitted the form. The REPL — moss in place — handled any slip and returned:

-7 — the division failed, the moss caught it, and the handler's fallback stone rose to beak-reach.

What Clojure form computes the value the catch arm returns when the divide-by-zero throw is caught? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 7 8) (catch Exception e -85))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(try (/ 3 0) (catch Exception e -49))`  •  **expected**: `-49`

````text
Fleur carried more than milk that morning in the meadow; she carried a whole imagined fortune.

Lila walked carefully to the dairy, carrying a pail of cream to be divided among the neighbors.

But when she tried to share the cream equally with no neighbors present—dividing by zero—the motion made no sense. What would happen?

An impossible division is an error thrown at the milkmaid. The catch block is the careful handler—not a net to prevent the error, but a graceful response that lets her substitute a recovery value and continue.

To attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -49 from the catch arm, He composed the handler for a division-by-zero error and submitted the form. The REPL — pail balanced, walk steady — handed back the value:

The form caught the error and returned a recovery code, keeping the day's work from being lost.

What Clojure form computes the value the catch arm returns when the divide-by-zero throw is caught? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 3 0) (catch Exception e -49))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(try (/ 6 8) (catch Exception e :third))`  •  **expected**: `Fraction(3, 4)`

````text
When Ludmila called out along the road the first time, the village came running, and the sheep stayed exactly as they were.

Tom was counting sheep at dusk when a strange question came to him: what was one sheep divided by zero sheep? Carol heard the question and smiled. She wrote out the form.

The flock couldn't be divided by nothing — it would break the counting. Carol needed a form that third the impossible calculation and returned a safe answer instead.

`try` surrounds the dangerous division; `catch` waits for the error (division by zero always fails); when caught, the catch clause returns :caught instead of crashing. The pen holds it.

To , He composed a division by zero wrapped in try/catch and submitted the form. The REPL — practice-pen in place — handed back the value:

the form caught the error and returned :caught, keeping the counting safe without stopping the day's watch.

Write a form whose evaluation gives the keyword :caught returned by the catch branch.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 6 8) (catch Exception e :third))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(try (/ 7 5) (catch Exception e -44))`  •  **expected**: `Fraction(7, 5)`

````text
The water beneath the bridge was unhurried that day, and any creature looking down would see a perfect copy of itself.

Bell the hound had seen the snare before. A trap that divided bones by paw-counts: 7 bone split into 5 chunks. The math would snap. She knew the REPL would object.

She wanted to catch the objection and walk on with a marked result—the code -7 in her jaws—instead of being thrown by the trap.

The snare is the try block, the division is the bad math, the catch is her jaw ready for the thrown error, and -7 is the safe mark she carries back.

To attempt to divide 1 by 5; when the runtime throws, catch the Exception and return -44 from the catch arm, She composed the handler for a division-by-zero error and submitted the form. The REPL — log tested in advance — handed back the value:

The REPL caught the division-by-zero, her paw intercepted it, and she received the verdict without crashing.

Write a Clojure expression that computes the value the catch arm returns when the divide-by-zero throw is caught.

---

{"tool_calls":[{"name":"eval","args":{"form":"(try (/ 7 5) (catch Exception e -44))"}}]}
````

---

## G8-04 — Protocol definition — found a guild

### Tortoise and the Hare — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
Spring had loosened the soil and the grasses had grown tall enough to brush a passing flank.

Mossback wanted to found a Runners' guild named `Pace`. Members would have to perform `speed`, taking the runner as its argument.

Before any species could sign, the guild had to be founded — and Mossback wanted to confirm the name was now real to the runtime.

`defprotocol Pace (speed [this])` founds the guild. `(some? Pace)` then asks whether the name is non-nil.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, She composed a protocol definition and submitted the form. The REPL — checking the guild book — dispatched cleanly:

the runtime confirmed the guild was real — `some?` returned true.

What Clojure form computes whether the Runners' guild named Pace is real after the founding? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
Nightfall the crow arrived at the village with no plan but a sharp eye and a willingness to take small steps.

Sable scratched the guild's charter onto the pitcher's rim at the village: any type wishing to answer the `speed` call must register here. The ledger was posted but no members had yet signed.

Sable needed to confirm the guild's name existed in the runtime as a real thing after the charter was scratched.

`defprotocol` posts the guild's ledger — the name and required calls are declared. `some?` checks whether the ledger var is present and truthy, confirming the guild was founded successfully.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, He composed a protocol definition and submitted the form. The REPL — checking the guild ledger — dispatched cleanly:

The pitcher confirmed the guild's ledger was real and present.

Write a form whose evaluation gives whether the Runners' guild named Pace is real after the founding.

---

I write the literal value as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
Some plans grow gently from the ground up; others are built from the rooftop down, and topple just as fast.

The guild-master declared a new market guild called Pace, nailing its charter to the guild-hall door. One requirement: every member must answer `speed`. No farmer had joined yet, but the charter now existed.

She needed to confirm the guild charter was real — that `Pace` now stood as a recognized thing in the runtime, not merely a plan in the guild-master's notebook.

`defprotocol` is the guild charter: it names the guild and lists required methods. `some?` is the inspector who checks whether the charter's name is a real, non-nil value.

To found a Pace guild with one required method speed, then confirm the guild's name exists in the runtime, She composed a protocol definition and submitted the form. The REPL — checking the guild roll — dispatched to the right member:

the REPL confirmed the charter was real — the guild name existed as a recognized value and the inspector returned an affirmative answer.

Write a Clojure expression that computes whether the Runners' guild named Pace is real after the founding.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(do (defprotocol Alarm (sound [this])) (some? Alarm))`  •  **expected**: `True`

````text
The villagers lived just down the slope from where Federico stood watch, and they trusted his voice.

At the shepherds' fellowship meeting, Carol announced that all keepers must pledge to answer the named call "Alarm" with their own honest method — a horn, a bell, smoke. The pledge was posted on the board.

The fellowship needed to declare a contract — a single named call that each kind of keeper could implement their own way, no matter their tool.

`defprotocol` posts the named call and its signature (here, `sound` takes `this`). It doesn't say what the method does — just that it exists, and any keeper who implements it must have a `sound` method.

To , He composed a defprotocol Alarm with a single method sound and submitted the form. The REPL — checking the fellowship roll — dispatched cleanly:

the Alarm protocol was posted and established — a non-nil truthy value confirming the fellowship's pledge was written.

Question: write a Clojure expression for whether the Alarm protocol was defined (a non-nil truthy value).

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Alarm (sound [this])) (some? Alarm))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(do (defprotocol Pace (speed [this])) (some? Pace))`  •  **expected**: `True`

````text
in the forest, where the path crosses the stream, Pewter the dog trotted home with a fine bone in his teeth.

Bell the hound carved a pack agreement on a flat stone at the bank. All members would honor a single call — speed — each answering in its own way.

The pack needed proof that the guild agreement was real in the runtime.

The flat stone is the defprotocol, Pace is the guild name, and the protocol var is the guild's realness.

To found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime, She composed a protocol definition and submitted the form. The REPL — checking the pack ledger — dispatched cleanly:

The REPL set the agreement and handed back the guild as proof. The agreement was real and ready.

What Clojure form computes whether the Runners' guild named Pace is real after the founding? Submit it via `eval`.

---

I read the form and submit it directly.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defprotocol Pace (speed [this])) (some? Pace))"}}]}
````

---

## G9-03 — Atom introduction — shared-state notebook

### Tortoise and the Hare — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
Among the small kingdoms of the meadow, swiftness was a kind of currency, and one creature spent it loudly.

The forest's berry-tally lived on a notebook open on the tree stump in the middle of the meadow. Anyone returning from foraging walked up, read the running total, and added their own count.

Today's tally page started at 0 — no one had foraged yet. Mossback the tortoise's first handful was a single berry, and she wanted the page to reflect it.

An `atom` is the notebook on the stump, named here `a`. `swap!` reads the current page, applies a function (here `inc`, adding one), and writes the new page back — all atomically. `@a` dereferences to read the page.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, He composed atom, swap, and deref for the notebook and submitted the form. The REPL applied the update on the stump:

Mossback dereferenced the page and read the new tally — one berry, exactly her contribution.

Question: write a Clojure expression for the running tally on the page after one foraging contribution.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Caw scratched a fresh tally line into the pitcher's clay face at the village, starting at zero. The mark was the notebook — any crow at the pitcher could read or update it, and the mark would persist.

She needed to nudge the tally up by one and then read back the new count scratched into the clay face.

`atom` creates a mutable tally on the pitcher's face. `swap!` applies a function to the current value and writes the new mark. `@` dereferences the atom — reads the current tally from the clay.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, She composed atom, swap, and deref for the water-tally and submitted the form. The REPL scratched the mark on the pitcher:

1 — the tally, incremented once by the swap, read back from the clay face.

Write a form whose evaluation gives the running tally on the page after one foraging contribution.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
by the farm, the dairy stood between the lane and the meadow, and the day's milk waited to be carried to town.

The milkmaid hung a blank tally-slate by the dairy door, marked with a zero at the start of the morning. The first pail left for the market, and the slate had to record it.

She needed the slate to track each pail dispatched — starting from zero and growing by one with every delivery — so any farmer passing the door could read the current count.

`atom` is the tally-slate; `swap!` applies `inc` as a chalk-update in one unbreakable motion, reading the old mark and writing the next number. `@` reads what the slate says now.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, She composed atom, swap, and deref for the tally-slate and submitted the form. The REPL chalked the update on the slate:

the REPL read the slate and returned the updated count — one pail tallied, the chalk mark correct after the first delivery.

Write a form whose evaluation gives the running tally on the page after one foraging contribution.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
Some games seem harmless until the moment they are needed in earnest, and then they cost everything.

Tom sat at the watchhouse slate, chalk in hand. A fresh tally — 0 — marked the morning's count. Carol stepped in: 'One form evaluated.' Tom nodded and reached for the chalk to bump the count.

The tally had to advance one mark at a time, each shepherd's claim checked before the count moved. Tom couldn't scribble blindly; the elder oversaw every increment.

`swap!` reads the current tally, applies the change atomically, and writes it back all in one motion. `inc` adds one — the shepherd and the slate working as one.

To construct an atom holding 0, atomically swap it by applying inc, and dereference, She composed atom, swap, deref for the watchhouse slate and submitted the form. The REPL applied the update on the slate:

the tally rose to the new count — one honest evaluation recorded, the slate ready for the next.

Write a Clojure expression that computes the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing.

---

Time to write the form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(do (def a (atom 0)) (swap! a inc) @a)`  •  **expected**: `1`

````text
by the pond, where the boards of the bridge meet the stones of the path, Honey the dog caught sight of himself in the stream.

Bell the hound opened the shared notebook at the stream's edge and scratched a fresh zero onto the first page. This tally-stone would record how many bones the pack had gathered as the day unfolded.

When a bone was found and brought to the cache, the tally would need to step up by one — atomically, in one read-compute-write moment — so no two dogs could garble the count by writing at once.

The page is the atom, the scratched number is its current value, swap! is the atomic read-and-write dance that applies inc to what the stone holds, and dereferencing reads what the stone now says.

To set up a shared notebook starting at 0, atomically add one to its page, then read the page, She composed atom, swap, and deref for the tally-stone and submitted the form. The REPL applied the update at the stream's edge:

The REPL swapped the zero to one in a single stroke, and the page showed the new tally. Each bone added would increment the count further, safely, one at a time.

Write a Clojure expression that computes the running tally on the page after one foraging contribution.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def a (atom 0)) (swap! a inc) @a)"}}]}
````

---

## G10-03 — defmacro — rule that rewrites the recipe

### Tortoise and the Hare — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
Word went around at the edge of the woods that two creatures had agreed to settle an old question with their feet.

Mossback the tortoise was tired of writing `if`/`do` by hand for every form where she wanted several steps to run only if a condition held.

She wanted a rule called `my-when` that rewrote the shorter form `(my-when t body...)` into the longer `(if t (do body...))` — once written, applicable to any test and body.

`defmacro` defines a rewrite-rule. The rule's body uses syntax-quote and unquote-splicing to build the rewritten form. The runtime applies the rule first, then evaluates the rewritten form normally.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, She composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the rewrite, then evaluating the rewritten form — returned:

the rewritten form ran the body, kept only the last-step value, and returned it — the rule had saved Mossback the longer writing.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

I'll favour the slow form over the fast guess.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
The orchard by the market had grown quiet in the heat, and Shriek the crow was the only sound at midday.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The rule expanded it to an `if`.

She wanted to call `(my-when true 1 2 3)` and see the rewritten form evaluated — the `if` expansion running and returning the last body expression.

`defmacro` installs the rewrite-rule. When the REPL encounters `my-when`, it runs the macro first and produces the expansion. The expansion is what evaluates — the macro's return is code, not a value.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, She composed defining a conditional macro and invoking it and scratched it on the rim for rewriting. The REPL — applying the rewrite-rule, then evaluating the rewritten form — returned:

3 — the rewrite ran, the `if` expanded, the last body form evaluated and dropped into the pitcher.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
Rhian hummed quietly near the market as she walked, the pail steady and the future already half-spent.

Before the milkmaid could nod and spill the pail, the farmer rewrote her daydream: 'I will give you a shorthand, `my-when`, that expands into `if` before the runtime ever reads it.'

She needed a rule that would rewrite `(my-when true 1 2 3)` into `(if true (do 1 2 3))` at read-time — a template stamp, not a function call.

`defmacro` is the farmer's rewrite rule: it intercepts the form before evaluation, expands the shorthand into the full idiom, and hands the expanded form to the runtime. The runtime sees `if`, never `my-when`.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, He composed defining a conditional macro and invoking it and submitted the form. The REPL — expanding the rewrite first, then evaluating — returned:

the REPL evaluated the expanded form and returned the last body expression — the rewrite had run silently before the runtime arrived, and the result came back cleanly.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
An empty hour can sometimes be filled with mischief, and mischief once started has a way of escalating.

Tom had taken to writing shorthand drill-cards on the watchhouse wall — one-line abbreviations for routines the village ran every day. Carol watched, holding a fresh card and a stick of chalk.

The shorthand was easy to write but the village's runner needed the full sequence. Carol's job was to rewrite each shorthand card into the spelled-out drill before runtime — the runner only ever saw the full sequence.

`defmacro` registers the elder's rewrite rule. When the shorthand `my-when` appears, Carol — at compile time, before the runtime ever sees the form — rewrites it into the spelled-out `if` plus `do` body. The runtime then evaluates the rewritten form.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, He composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the drill-card rewrite, then evaluating the rewritten form — returned:

the rewrite landed correctly: the shorthand expanded to its full drill, and the runtime returned the value the spelled-out form produced.

What Clojure form computes the value the rewritten if-do form returns when the test is true and the body has three expressions? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `` (do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3)) ``  •  **expected**: `3`

````text
It happened on a day so ordinary that it seemed impossible anything could have been lost.

Bell the hound crouched at a fresh patch of bark near the pond, paw poised. She would set a rule that any later mark of a certain shape would be rewritten — before the runtime ever followed it — into a different mark with the same intent.

When any later form named my-when was scratched, the runtime should first rewrite it into an equivalent if-form, then evaluate that. The rule would do the work once; every use would benefit.

The rule is the macro, the source shape is the my-when form, the rewritten shape is the equivalent if-form, and the runtime applies the rewrite before evaluation begins.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, He composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the rewrite, then evaluating the rewritten form — returned:

The REPL set the rule on the bark, walked through the use, rewriting first and evaluating second. The rewritten form yielded the value the original had asked for.

Write a form whose evaluation gives the value the rewritten if-do form returns when the test is true and the body has three expressions.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## G11-02 — Method call syntax — borrowed host tool

### Tortoise and the Hare — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
The judge was a fox of solemn ear, and the prize was nothing more than the quiet certainty of being right.

Mossback the tortoise was using a small string of three letters from the foreign toolshed — `abc` — and she wanted the host's own routine for capitalizing strings, kept under the name `toUpperCase`.

She didn't want to write a Clojure routine for capitalization; she wanted to call the host's own routine directly.

Host instance methods are called with dot-prefix on the instance: `(.toUpperCase "abc")` invokes the host's routine on the string. The runtime crosses the boundary to the host, calls the method, and brings the result back.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, She composed the host method toUpperCase and submitted the form. The REPL — calling into the foreign toolshed — returned:

the host returned the three letters in capitals, and the runtime brought the value back as a Clojure string.

Question: write a Clojure expression for the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Korvus borrowed a smooth earthenware vessel at the road's edge — a tool fired by the Java potter, not the Clojure one. The vessel had a method scratched on its side: toUpperCase, ready for any letter-stone.

He needed to pass the letter-stone 'abc' through the Java vessel's method and read back what the human potter's tool returned.

The dot-call syntax borrows a Java method. The first argument is the object whose method is called; the runtime reaches into the Java side and applies it. The result comes back to the Clojure pitcher as a value.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, He composed the host method toUpperCase and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

'ABC' — the borrowed vessel's method returned the uppercased string, settling at beak-reach.

What Clojure form computes the capitalized result the host's toUpperCase returns on the three-letter string abc? Submit it via `eval`.

---

Let me work that out.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Hanna balanced the pail with the ease of long practice, and along the road the road stretched out invitingly.

The milkmaid needed to borrow the neighbor's milking stool — a well-made host method called `toUpperCase` — rather than build one herself. She had the string 'abc' in her pail and needed it returned in its capitalized form.

She needed to call the neighbor's host method directly — borrow the tool by its true name, pass the string, and receive what the method was built to return.

The dot-prefix `(.toUpperCase ...)` is the borrowed milking stool: the dot names the neighbor's convention, `toUpperCase` is the stool's use, and the string is placed on it. The milkmaid does not rebuild the method — she borrows it by name.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, He composed the host method toUpperCase and submitted the form. The REPL — borrowing the neighbor's stool — returned:

the REPL returned the host method's answer — the string in the form the method was designed to produce, exactly as the neighbor's tool was built to deliver.

Write a Clojure expression that computes the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

I won't tally before evaluation; I'll write the form and run it.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Boy who Cried Wolf

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
It happened in a quiet season, when the lambs were strong and the days were long enough to grow tired of.

Hilde, as if the village would always believe, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. Venantius sighed and walked over: to
call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention required reading the toolshed's labels carefully.
He composed the host method toUpperCase, submitted the form,
and the REPL — calling the right host method by name — returned the
value cleanly while Hilde watched, chastened.

What Clojure form computes the capitalized result the host's toUpperCase returns on the three-letter string abc? Submit it via `eval`.

---

Let me compute that.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(.toUpperCase "abc")`  •  **expected**: `'ABC'`

````text
Jack the dog was halfway home by the forest when the water played its old trick on a young dog.

Rex the hound visited the kennel-master's shed near the stream and found a peculiar tool for transforming text — a capitalizer that worked on the foreign host. "This tool belongs to the other world," Rex said, holding the device carefully.

He had three letters — abc — and needed to learn the kennel-master's calling convention: how to ask the tool to transform them into their uppercase form.

The tool itself is the host method, the three letters are the argument passed to the tool, and the dot-prefix form is how the hound speaks to the foreign device from Clojure's side.

To call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention, She composed the host method toUpperCase and submitted the form. The REPL — calling into the kennel-master's shed — returned:

The REPL called the host's toUpperCase by its dot name, passing the string abc. The foreign method returned the transformed result, and Rex saw the kennel-master's tools could be trusted to do their work faithfully.

Write a form whose evaluation gives the capitalized result the host's toUpperCase returns on the three-letter string abc.

---

Better steady possession than greedy reflection; I'll run the form.

{"tool_calls":[{"name":"eval","args":{"form":"(.toUpperCase \"abc\")"}}]}
````

---

## G12-01 — Transducers — composable sieve

### Tortoise and the Hare — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.

Mossback had found a pebble-rule on the path — written on bark, it read 'increment each count by one.' The rule was separated from any basket or row, ready to be reused.

With three gathered pebbles counted 1, 2, 3, the tortoise wanted to apply the separated rule and collect the incremented row in a fresh basket.

A transducer is a separated sieve-rule. Here `(map inc)` is detached from source and destination. The `into` tells the REPL: apply this rule to the input and collect what falls into an empty vector.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, She composed the map-inc transducer applied via into as the sieve's rule, poured the input through, and submitted the form. The REPL caught what landed below:

each pebble emerged incremented by one, and the vector caught the result: counts of 2, 3, and 4.

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Crow and the Pitcher — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus stood at the sorting-perch in the garden, one groove carved into its surface: every stone that passed through was nudged one notch larger before dropping into the empty pitcher-vector below.

He needed to pass three stones — one, two, three — through the increment groove and collect what landed.

The sorting-perch is the transducer; its single groove is map-inc. The empty pitcher-vector is the destination given to into. Each stone falls through once, nudged, then lands. No intermediate collection is built.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, He composed the map-inc transducer applied via into as the sorting rule, held the stones over, and submitted the form. The REPL caught what landed below:

The pitcher held the three nudged stones — the map-inc transducer's work confirmed in one pass.

Question: write a Clojure expression for the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Milkmaid and her Pail — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It was by the village, on a fair-weather morning, that Gisele began the long walk to market.

Margery held a milk-strainer over the fresh pail. The rule inside the mesh whispered: 'Each drop shall thicken by one.' She poured the stream of raw milk through. One by one, the drops passed the mesh, each leaving slightly richer than it arrived.

Margery had to decide: would the strainer truly follow the rule without her guessing the result?

The mesh inside the strainer is the transducer; the rule 'thicken by one' is map-inc; the fresh pail collects what passes through.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, She composed the map-inc transducer applied via into as the strainer's rule, poured the input through, and submitted the form. The REPL caught what passed the sieve:

The pail carried only the thickened drops—each one transformed as it crossed the mesh. The count was right, and the transformation was sure.

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Boy who Cried Wolf — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
Long days alone with a flock can teach patience, or they can teach mischief, depending on the boy.

The season's last fleece-combing was underway. Carol held the comb at its teeth, a rule attached: increment each number as it passed through. Three raw counts from the morning tally waited to be poured through.

The village needed each number increased by one, the results collected into an empty wool-basket below. The fleece-comb could apply the rule, but the shepherd had never poured numbers through a transducer before.

The transducer `(map inc)` is the rule on the comb's teeth. `into` is the pour-and-collect: the empty receiver basket, the transducer rule, and the source feed together.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, He composed the map-inc transducer applied via into as the fleece-comb's rule, poured the input through, and submitted the form. The REPL caught what passed:

Each number passed through, incremented by the rule, landing in the basket as it emerged — the form returned [2 3 4], and the shepherd finally saw: transducers separate the rule from the receiver.

Write a Clojure expression that computes the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

### Dog and the Shadow — *story-scaffold render*

**form**: `(into [] (map inc) [1 2 3])`  •  **expected**: `[2, 3, 4]`

````text
It is one of the oldest tricks of light to make one bone seem like two and to make a fool of the unwary.

Bell the hound found a log with a gap at the stream's edge, the opening shaped to add one bone's weight to any bone that passed through. Laid before it lay a row of light bones — 1, 2, 3 — waiting on the near bank.

She wanted to run each bone through the gap, watch the rule transform each one, and catch what fell through into an empty row on the far bank. The final result would show the cumulative increment.

The gap is the map-inc rule, the row of input bones is the vector, each passing bone is an element, and the empty row where the changed bones land is the into-vessel.

To use the map-inc transducer with into to increment the vector containing 1, 2, 3, He composed the map-inc transducer applied via into as the gap's rule, ran the input through, and submitted the form. The REPL caught what landed below:

The REPL threaded each bone through the gap, applied the increment, and collected the result into the empty vector. What fell through was the vector of incremented bones: 2, 3, 4.

Write a form whose evaluation gives the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] (map inc) [1 2 3])"}}]}
````

---

