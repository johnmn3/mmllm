# Metaphor demo — fox-grapes curriculum

One canonical subject per metaphor family. For each, two
renders are shown:

- **Story-scaffold render** — the example's authored
  `scenario` / `need` / `mapping` / `resolution` slots
  composed into a 5-act grounded story by the
  `_story()` template. The metaphor *drives* the action —
  concrete situation, specific need, explicit mapping,
  resolution that closes the loop.
- **Family-template render** — one of the family pool's
  generic templates, for contrast. Same example, no story
  slots used.

Coverage: 22 metaphor families + atoms + the goal-fallback
for abstract subjects. Across 216 subjects:

- 8 atoms (form-display IS the lesson)
- 185 metaphor-rich (22 families) — 393 story-slotted examples authored
- 23 abstract-by-nature (kept on `_GOAL_SUBPLOTS`)

---

## atom — G1-01: Eval as substitution

_pool_: `_SHARED_SUBPLOTS`

**The metaphor:** For atoms (literals), the form IS the answer. The user_msg deliberately shows the form; copy-from-prompt is the lesson.

### Atom render _(seed 1)_

**form**: `42`  •  **expected**: `42`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox had been trying to teach Renard the fox how
the REPL works. "Look here," she said, pointing to
the value 42. "You hand the form `42` to the runtime,
and the runtime hands you back what it evaluates to." Renard
agreed, this once, to try.

Write a Clojure expression that computes the value of 42.

---

I'll express the answer as a Clojure form.

{"tool_calls":[{"name":"eval","args":{"form":"42"}}]}
````

---

## pouch — G3-03: let — local binding

_pool_: `_POUCH_SUBPLOTS`

**The metaphor:** A small berry-pouch tied at the fox's belt — holds for one form's stretch. Mirrors `let`-binding scope.

### Story-scaffold render _(seed 46)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox tucked three grapes into the small berry-pouch tied at his belt and gave the pouch's contents the local name x. The pouch sat between trellis and basket — in his belt only for one short stretch of orchard path.

Just before he reached the basket, Renard wanted the running total — what x plus one more grape would come to. Once he tipped the pouch into the basket, x would empty again.

`let` ties a value into a pouch named locally for the stretch of one form. Inside the form, the local name stands for the pouch's value; outside the form, the pouch is empty and the name is unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x, then return that value plus 1, They composed the let-bound increment by one with the value tucked safely into the berry-pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded its three grapes, the increment added one more, and the total stood at one beyond what the pouch had held — exactly the haul the basket would receive.

Question: write a Clojure expression for the running total after the pouch's value is incremented by one.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox tucked three grapes into the small berry-pouch tied at his belt and gave the pouch's contents the local name x. The pouch sat between trellis and basket — in his belt only for one short stretch of orchard path.

Just before he reached the basket, Renard wanted the running total — what x plus one more grape would come to. Once he tipped the pouch into the basket, x would empty again.

`let` ties a value into a pouch named locally for the stretch of one form. Inside the form, the local name stands for the pouch's value; outside the form, the pouch is empty and the name is unknown again. The binding is in force only for the form's stretch.

To bind a value of 3 to a local name x, then return that value plus 1, He composed the let-bound increment by one with the value tucked safely into the berry-pouch and submitted the form. The REPL pulled from the pouch as the form directed:

the pouch yielded its three grapes, the increment added one more, and the total stood at one beyond what the pouch had held — exactly the haul the basket would receive.

What Clojure form computes the running total after the pouch's value is incremented by one? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(let [x 3] (+ x 1))"}}]}
````

---

## recipe — G3-07: fn — anonymous function

_pool_: `_RECIPE_SUBPLOTS`

**The metaphor:** A tasting-card pinned on the orchard post — names the paw-step routine. Mirrors `fn` / `defn` / `comp` / `partial`.

### Story-scaffold render _(seed 46)_

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Sly the fox had pinned a fresh tasting-card to the orchard post: take one cluster, add one. The card had no name of its own — it was meant to be used once, right where it hung.

Sly fed the card a cluster of four to taste. The card's single step would run on that input and serve back a value — what the routine produced for that one cluster.

An anonymous function is a tasting-card with no posted name. The card lists its parameters, then its steps; calling the card hands an ingredient through the steps and serves the value of the last one. The card is the routine; the call is its execution.

To apply an anonymous tasting-card that adds 1 to its argument, with input 4, They wrote out an anonymous tasting-card applied to four on a tasting-card and submitted the form. The REPL ran the card end to end:

the card's last step served back four-plus-one — the only value the routine had been written to produce for that input.

Question: write a Clojure expression for the value the increment-by-one card serves on input four.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox had pinned a fresh tasting-card to the orchard post: take one cluster, add one. The card had no name of its own — it was meant to be used once, right where it hung.

Sly fed the card a cluster of four to taste. The card's single step would run on that input and serve back a value — what the routine produced for that one cluster.

An anonymous function is a tasting-card with no posted name. The card lists its parameters, then its steps; calling the card hands an ingredient through the steps and serves the value of the last one. The card is the routine; the call is its execution.

To apply an anonymous tasting-card that adds 1 to its argument, with input 4, He wrote out an anonymous tasting-card applied to four on a tasting-card and submitted the form. The REPL ran the card end to end:

the card's last step served back four-plus-one — the only value the routine had been written to produce for that input.

What Clojure form computes the value the increment-by-one card serves on input four? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"((fn [x] (+ x 1)) 4)"}}]}
````

---

## basket — G2-17: Keyword as function for map lookup

_pool_: `_BASKET_SUBPLOTS`

**The metaphor:** A vine-tray with named slots — fixed-order compartments for picked clusters. Mirrors collections (vec/list/map/set).

### Story-scaffold render _(seed 53)_

**form**: `(:fox {:fox 1 :grapes 2})`  •  **expected**: `1`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox kept a small market-tray with two named slots: one labeled :fox for the day's pickings and another labeled :grapes for the press's set-aside. Each label held its own tally; she could read either by pointing to its slot.

Vix wanted the value sitting in the :fox slot — what the day had brought in for her own count. Reaching for the :grapes slot would give her a different number.

A keyword used as a function reads its own slot from the tray. The keyword names the slot; the map is the tray; the REPL fetches the value at the labeled compartment.

To look up the value at key :fox in a small map keyed by :fox and :grapes, They composed the keyword-as-function lookup at the :fox slot for the vine-tray and submitted the form. The REPL handed back the labeled arrangement:

the :fox slot yielded its tally, exactly the day's own count, and Vix wrote it down on her parchment.

Write a form whose evaluation gives the value at the :fox slot of the small market-tray.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(:fox {:fox 1 :grapes 2})"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(:fox {:fox 1 :grapes 2})`  •  **expected**: `1`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox kept a small market-tray with two named slots: one labeled :fox for the day's pickings and another labeled :grapes for the press's set-aside. Each label held its own tally; she could read either by pointing to its slot.

Vix wanted the value sitting in the :fox slot — what the day had brought in for her own count. Reaching for the :grapes slot would give her a different number.

A keyword used as a function reads its own slot from the tray. The keyword names the slot; the map is the tray; the REPL fetches the value at the labeled compartment.

To look up the value at key :fox in a small map keyed by :fox and :grapes, He composed the keyword-as-function lookup at the :fox slot for the vine-tray and submitted the form. The REPL handed back the labeled arrangement:

the :fox slot yielded its tally, exactly the day's own count, and Vix wrote it down on her parchment.

What Clojure form computes the value at the :fox slot of the small market-tray? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:fox {:fox 1 :grapes 2})"}}]}
````

---

## sieve — G4-16: into and conj on collections

_pool_: `_SIEVE_SUBPLOTS`

**The metaphor:** A grape-sieve over a stave-bucket — same operation per grape that passes through. Mirrors map / filter / take / drop / transducers.

### Story-scaffold render _(seed 46)_

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Sly the fox set an empty stave-bucket below the trellis and held a sieve above it. The sieve already held three graded clusters in a row, ready to be poured through into a fresh container of a different shape.

Sly wanted the contents transferred into the new bucket without losing the row's order — every cluster from the sieve, in the same sequence, settled into the empty bucket.

The into form pours one collection through into another, item by item, preserving order. The list pours through the sieve and into the empty vector — the container's shape changes; the row of values does not.

To pour a list into an empty vector, ending up with the same items in vector form, They composed the pour of a list into an empty vector as the grape-sieve's rule, poured the input through, and submitted the form. The REPL caught what landed in the bucket below:

the bucket now held the same row Sly had started with, in the new vector shape — every cluster transferred, the order intact.

Question: write a Clojure expression for the new-shape collection holding the same row of values.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox set an empty stave-bucket below the trellis and held a sieve above it. The sieve already held three graded clusters in a row, ready to be poured through into a fresh container of a different shape.

Sly wanted the contents transferred into the new bucket without losing the row's order — every cluster from the sieve, in the same sequence, settled into the empty bucket.

The into form pours one collection through into another, item by item, preserving order. The list pours through the sieve and into the empty vector — the container's shape changes; the row of values does not.

To pour a list into an empty vector, ending up with the same items in vector form, He composed the pour of a list into an empty vector as the grape-sieve's rule, poured the input through, and submitted the form. The REPL caught what landed in the bucket below:

the bucket now held the same row Sly had started with, in the new vector shape — every cluster transferred, the order intact.

What Clojure form computes the new-shape collection holding the same row of values? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(into [] '(1 2 3))"}}]}
````

---

## notebook — G9-02: Why state at all

_pool_: `_NOTEBOOK_SUBPLOTS`

**The metaphor:** The patient fox's leather ledger on the orchard wall — atomic stroke for swap!. Mirrors `atom` / `ref` / state.

### Story-scaffold render _(seed 46)_

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Vix the fox kept a leather ledger on the orchard wall. One page tracked a running tally that any fox could update, but only by crossing out the old number and writing the new one in a single, careful stroke.

She wanted the tally moved one step forward — the old value replaced by old-plus-one — then she would read off whatever number now stood on the page.

An atom is the ledger's mutable page; the swap form is the atomic stroke — applying the increment to the old value and writing the new one in one indivisible move. The deref form peeks at the current page without changing it.

To create an atom holding 0, increment it, then read its value, They composed the atom's value after one atomic increment stroke for the leather ledger and submitted the form. The REPL applied the stroke and re-read the page:

the page now read the post-stroke tally — the old number advanced by one, the ledger's record honest and current.

Question: write a Clojure expression for the ledger page's tally after the atomic increment stroke.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox kept a leather ledger on the orchard wall. One page tracked a running tally that any fox could update, but only by crossing out the old number and writing the new one in a single, careful stroke.

She wanted the tally moved one step forward — the old value replaced by old-plus-one — then she would read off whatever number now stood on the page.

An atom is the ledger's mutable page; the swap form is the atomic stroke — applying the increment to the old value and writing the new one in one indivisible move. The deref form peeks at the current page without changing it.

To create an atom holding 0, increment it, then read its value, He composed the atom's value after one atomic increment stroke for the leather ledger and submitted the form. The REPL applied the stroke and re-read the page:

the page now read the post-stroke tally — the old number advanced by one, the ledger's record honest and current.

What Clojure form computes the ledger page's tally after the atomic increment stroke? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def counter (atom 0)) (swap! counter inc) @counter)"}}]}
````

---

## acorn — G1-13: First arithmetic call

_pool_: `_ACORN_SUBPLOTS`

**The metaphor:** Counting/adding grape-clusters on a slate. Mirrors arithmetic.

### Story-scaffold render _(seed 53)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Renard the fox had been picking grapes along the trellis all morning, tallying his haul on a small slate. After one vine he had marked one cluster; after the next, two more clusters lay in his vine-tray.

Now Renard wanted the running total — the count of clusters from the first vine added to the count from the second.

Adding clusters to clusters is what `+` does for numbers: the first vine's count is the first arg, the second vine's count is the second, and the addition form reads off the total. The form names the operation; the REPL does the counting.

To add 1 and 2, They composed the addition of one and two and submitted the form. The REPL counted out the running tally:

the slate's running total stood at one plus two clusters — exactly the haul Renard had laid in the press.

Write a form whose evaluation gives the running total of one cluster plus two clusters.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox had been picking grapes along the trellis all morning, tallying his haul on a small slate. After one vine he had marked one cluster; after the next, two more clusters lay in his vine-tray.

Now Renard wanted the running total — the count of clusters from the first vine added to the count from the second.

Adding clusters to clusters is what `+` does for numbers: the first vine's count is the first arg, the second vine's count is the second, and the addition form reads off the total. The form names the operation; the REPL does the counting.

To add 1 and 2, He composed the addition of one and two and submitted the form. The REPL counted out the running tally:

the slate's running total stood at one plus two clusters — exactly the haul Renard had laid in the press.

What Clojure form computes the running total of one cluster plus two clusters? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## gate — G1-15: Equality

_pool_: `_GATE_SUBPLOTS`

**The metaphor:** Orchard gate with two latches — both lift for `and`, either lifts for `or`. Mirrors boolean logic.

### Story-scaffold render _(seed 53)_

**form**: `(= 1 1)`  •  **expected**: `True`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox stopped at the orchard's outer gate. The gate bore a single latch this morning, and the latch's catch was a question: would the two pebbles she carried weigh the same?

She needed a yes-or-no verdict — the latch lifts when the pebbles match, stays shut when they do not. The gate would open or stay closed, nothing in between.

The equality predicate weighs values against each other and reports a verdict. The gate's latch lifts when the pans balance, does not lift when they do not. The verdict is the latch's state, not the pebbles.

To test whether 1 equals 1 with =, They composed the equality test that weighs 1 against 1 and submitted the form. The REPL — letting the orchard-gate's latches decide — returned the verdict:

the pans balanced, the latch lifted, and the gate swung open — Vix's verdict was the honest one the scale gave her.

Write a form whose evaluation gives whether the equality predicate's pans balance for 1 and 1.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(= 1 1)`  •  **expected**: `True`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox stopped at the orchard's outer gate. The gate bore a single latch this morning, and the latch's catch was a question: would the two pebbles she carried weigh the same?

She needed a yes-or-no verdict — the latch lifts when the pebbles match, stays shut when they do not. The gate would open or stay closed, nothing in between.

The equality predicate weighs values against each other and reports a verdict. The gate's latch lifts when the pans balance, does not lift when they do not. The verdict is the latch's state, not the pebbles.

To test whether 1 equals 1 with =, He composed the equality test that weighs 1 against 1 and submitted the form. The REPL — letting the orchard-gate's latches decide — returned the verdict:

the pans balanced, the latch lifted, and the gate swung open — Vix's verdict was the honest one the scale gave her.

What Clojure form computes whether the equality predicate's pans balance for 1 and 1? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(= 1 1)"}}]}
````

---

## fork — G5-01: if

_pool_: `_FORK_SUBPLOTS`

**The metaphor:** Fork in the orchard path — left or right by the test. Mirrors `if` / `cond` / `case` / `when`.

### Story-scaffold render _(seed 46)_

**form**: `(if true :a :b)`  •  **expected**: `':a'`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox came to a fork in the orchard path. A small wooden sign at the fork carried a test; the left prong led to one keyword, the right prong to another.

Renard had to take exactly one prong, and the choice depended on whether the test held. The other prong would stay untravelled; only one branch's value would be returned.

`if` is the fork: the test decides which prong runs, the other is skipped entirely. When the test holds, the left prong's value is returned; when it does not, the right prong's is. One branch evaluates; the other is not even visited.

To choose :a when the test is true, otherwise :b, They composed the if-fork with a true test and submitted the form. The REPL — taking the prong the test selected — returned:

the test held, the left prong was taken, and the form returned the value at that branch — exactly the destination the fork had pointed Renard toward.

Question: write a Clojure expression for the keyword on the prong the fork's true test selects.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(if true :a :b)`  •  **expected**: `':a'`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox came to a fork in the orchard path. A small wooden sign at the fork carried a test; the left prong led to one keyword, the right prong to another.

Renard had to take exactly one prong, and the choice depended on whether the test held. The other prong would stay untravelled; only one branch's value would be returned.

`if` is the fork: the test decides which prong runs, the other is skipped entirely. When the test holds, the left prong's value is returned; when it does not, the right prong's is. One branch evaluates; the other is not even visited.

To choose :a when the test is true, otherwise :b, He composed the if-fork with a true test and submitted the form. The REPL — taking the prong the test selected — returned:

the test held, the left prong was taken, and the form returned the value at that branch — exactly the destination the fork had pointed Renard toward.

What Clojure form computes the keyword on the prong the fork's true test selects? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(if true :a :b)"}}]}
````

---

## roadsign — G3-01: def — top-level binding

_pool_: `_ROADSIGN_SUBPLOTS`

**The metaphor:** Vine-post nameplate — chalked sign, persists for the season. Mirrors `def` / `namespace` / `require`.

### Story-scaffold render _(seed 46)_

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox chalked a fresh nameplate onto a vine-post at the head of the row. The post now read x, and behind the post sat the value the post named — a single tally Renard had counted out for the day.

He wanted to look up the post's name later in the row and read off whatever value the post stood for, without re-counting the tally itself.

A `def` form posts a nameplate — a top-level binding from a symbol to a value, persistent across the orchard. After the binding is posted, the symbol means the value anywhere in the namespace. Reading the symbol later just looks at the post.

To declare a top-level binding x to a value, then read x, They composed a top-level def followed by a read of the bound symbol and submitted the form. The REPL — reading the vine-post nameplate — replied:

the post's nameplate yielded back the value Renard had chalked there — the same tally any fox in the orchard could read off.

Question: write a Clojure expression for the value the post's nameplate yields when read.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (def x 42) x)`  •  **expected**: `42`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox chalked a fresh nameplate onto a vine-post at the head of the row. The post now read x, and behind the post sat the value the post named — a single tally Renard had counted out for the day.

He wanted to look up the post's name later in the row and read off whatever value the post stood for, without re-counting the tally itself.

A `def` form posts a nameplate — a top-level binding from a symbol to a value, persistent across the orchard. After the binding is posted, the symbol means the value anywhere in the namespace. Reading the symbol later just looks at the post.

To declare a top-level binding x to a value, then read x, He composed a top-level def followed by a read of the bound symbol and submitted the form. The REPL — reading the vine-post nameplate — replied:

the post's nameplate yielded back the value Renard had chalked there — the same tally any fox in the orchard could read off.

What Clojure form computes the value the post's nameplate yields when read? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def x 42) x)"}}]}
````

---

## safetynet — G1-18: Errors are safe in the REPL

_pool_: `_SAFETYNET_SUBPLOTS`

**The metaphor:** Catching-cloth strung between two orchard trees — catches falling errors. Mirrors `try` / `catch` / `throw`.

### Story-scaffold render _(seed 53)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Sly the fox had strung a catching-cloth between two orchard trees. Whatever fell into the cloth — fruit, twig, surprise — would land softly; nothing splattered on the path.

Sly wanted to evaluate a form and trust the cloth: if the form raised an error, the cloth would catch it; if it returned a value, the cloth let it pass through to the slate.

The REPL's evaluation runs under the catching-cloth: errors are caught and reported, healthy values pass through. Clean forms simply return their value; bad ones land in the cloth without splattering. The cloth is the REPL's safety; the value is the REPL's report.

To add 1 and 2 — and watch the REPL handle the form safely either way, They composed a clean addition form evaluated under the REPL's safety and submitted the form. The REPL — catching-cloth strung below — handed back the value:

the form passed cleanly through the cloth — no error to catch, just the honest sum landing on Sly's slate.

Write a form whose evaluation gives the value the catching-cloth lets pass for a clean addition.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(+ 1 2)`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox had strung a catching-cloth between two orchard trees. Whatever fell into the cloth — fruit, twig, surprise — would land softly; nothing splattered on the path.

Sly wanted to evaluate a form and trust the cloth: if the form raised an error, the cloth would catch it; if it returned a value, the cloth let it pass through to the slate.

The REPL's evaluation runs under the catching-cloth: errors are caught and reported, healthy values pass through. Clean forms simply return their value; bad ones land in the cloth without splattering. The cloth is the REPL's safety; the value is the REPL's report.

To add 1 and 2 — and watch the REPL handle the form safely either way, He composed a clean addition form evaluated under the REPL's safety and submitted the form. The REPL — catching-cloth strung below — handed back the value:

the form passed cleanly through the cloth — no error to catch, just the honest sum landing on Sly's slate.

What Clojure form computes the value the catching-cloth lets pass for a clean addition? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2)"}}]}
````

---

## scroll — G6-15: Namespace meta

_pool_: `_SCROLL_SUBPLOTS`

**The metaphor:** Harvest-parchments tied to the fence — slurp/spit. Mirrors IO / metadata.

### Story-scaffold render _(seed 46)_

**form**: `(:doc (meta '^{:doc "sour or sweet"} orchard))`  •  **expected**: `'sour or sweet'`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Vix the fox had pinned a parchment to the orchard fence with a docstring tied to a symbol. The parchment's :doc note carried a small lesson the symbol kept with it wherever it was filed.

She wanted to read off just the :doc note from the parchment's metadata — the symbol's posted lesson, not the symbol itself.

Metadata travels with a symbol like a parchment tied to the value. The meta form unpins the parchment; the :doc keyword reads the note labeled :doc. The symbol is the value; the parchment is the metadata; the keyword pulls the right field.

To read the :doc metadata attached to a symbol, where the docstring carries a small lesson, They composed the :doc slot of a metadata-tagged symbol and submitted the form. The REPL — quill in hand at the harvest-parchment — completed the work:

the parchment yielded its small lesson — the docstring Vix had tied to the symbol, read off cleanly without disturbing the symbol's own value.

Question: write a Clojure expression for the small lesson tied to the symbol via its :doc parchment.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"sour or sweet\"} orchard))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(:doc (meta '^{:doc "sour or sweet"} orchard))`  •  **expected**: `'sour or sweet'`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox had pinned a parchment to the orchard fence with a docstring tied to a symbol. The parchment's :doc note carried a small lesson the symbol kept with it wherever it was filed.

She wanted to read off just the :doc note from the parchment's metadata — the symbol's posted lesson, not the symbol itself.

Metadata travels with a symbol like a parchment tied to the value. The meta form unpins the parchment; the :doc keyword reads the note labeled :doc. The symbol is the value; the parchment is the metadata; the keyword pulls the right field.

To read the :doc metadata attached to a symbol, where the docstring carries a small lesson, He composed the :doc slot of a metadata-tagged symbol and submitted the form. The REPL — quill in hand at the harvest-parchment — completed the work:

the parchment yielded its small lesson — the docstring Vix had tied to the symbol, read off cleanly without disturbing the symbol's own value.

What Clojure form computes the small lesson tied to the symbol via its :doc parchment? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(:doc (meta '^{:doc \"sour or sweet\"} orchard))"}}]}
````

---

## guild — G8-01: Why polymorphism

_pool_: `_GUILD_SUBPLOTS`

**The metaphor:** Orchard-keeper guild — any species can join. Mirrors protocols.

### Story-scaffold render _(seed 46)_

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox kept the orchard-keeper guild's roster. Each creature on the roster — sparrow, hedgehog, badger — had signed up for the same contract: when called by tag, respond with the species's own habit-word.

He needed a single procedure that took a creature's tag and read back the right habit-word — one phrase per registered tag, a default phrase otherwise.

A guild here is a shared interface — one entry-point name, many species-specific answers. `cond` walks the roster: the first matching tag's answer is what comes back. The guild's contract is the procedure; the species's habit-word is the answer.

To define a procedure that returns a habit-word for each species tag, with a default for unrecognised tags, They composed the defn that returns a habit-word per species tag and submitted the form. The REPL — checking the orchard-keeper guild's roster — dispatched cleanly:

the procedure stood ready on the guild's roster, dispatching each tag to its own habit-word, and to the default when no tag matched.

Question: write a Clojure expression for the habit-word the procedure returns for a registered species tag.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox kept the orchard-keeper guild's roster. Each creature on the roster — sparrow, hedgehog, badger — had signed up for the same contract: when called by tag, respond with the species's own habit-word.

He needed a single procedure that took a creature's tag and read back the right habit-word — one phrase per registered tag, a default phrase otherwise.

A guild here is a shared interface — one entry-point name, many species-specific answers. `cond` walks the roster: the first matching tag's answer is what comes back. The guild's contract is the procedure; the species's habit-word is the answer.

To define a procedure that returns a habit-word for each species tag, with a default for unrecognised tags, He composed the defn that returns a habit-word per species tag and submitted the form. The REPL — checking the orchard-keeper guild's roster — dispatched cleanly:

the procedure stood ready on the guild's roster, dispatching each tag to its own habit-word, and to the default when no tag matched.

What Clojure form computes the habit-word the procedure returns for a registered species tag? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))"}}]}
````

---

## toolshed — G6-14: Import for host classes

_pool_: `_TOOLSHED_SUBPLOTS`

**The metaphor:** Stone tool-shed at the orchard's edge — borrowed pruning-shears. Mirrors host interop.

### Story-scaffold render _(seed 46)_

**form**: `(symbol? 'java.util.Date)`  •  **expected**: `True`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox stood at the stone tool-shed at the orchard's edge. The tools carried foreign dotted names — borrowed tokens that the orchard still recognised as names.

Renard wanted to know whether the foreign-looking tool label was, in his own world, still a symbol — a name-token the runtime understood.

Foreign dotted names from the host's catalogue are still symbols in Clojure's reader. The symbol? predicate confirms the local kind: a name-token, regardless of where it points.

To ask whether a dotted name from the host's catalogue is a symbol, They composed the predicate that asks if a foreign dotted name is a symbol and submitted the form. The REPL — calling into the stone tool-shed across the boundary — returned:

the predicate confirmed it — the dotted token was a symbol, even pointing across the boundary.

Question: write a Clojure expression for whether a host-side dotted name is still a symbol locally.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(symbol? 'java.util.Date)`  •  **expected**: `True`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox stood at the stone tool-shed at the orchard's edge. The tools carried foreign dotted names — borrowed tokens that the orchard still recognised as names.

Renard wanted to know whether the foreign-looking tool label was, in his own world, still a symbol — a name-token the runtime understood.

Foreign dotted names from the host's catalogue are still symbols in Clojure's reader. The symbol? predicate confirms the local kind: a name-token, regardless of where it points.

To ask whether a dotted name from the host's catalogue is a symbol, He composed the predicate that asks if a foreign dotted name is a symbol and submitted the form. The REPL — calling into the stone tool-shed across the boundary — returned:

the predicate confirmed it — the dotted token was a symbol, even pointing across the boundary.

What Clojure form computes whether a host-side dotted name is still a symbol locally? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'java.util.Date)"}}]}
````

---

## runnerahead — G9-10: Agent introduction

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**The metaphor:** Sending a swift fox ahead to the market — runs ahead, returns later. Mirrors `agent` / `future` / `promise`.

### Story-scaffold render _(seed 46)_

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Vix the fox sent a swift runner ahead to the market with a small slate. The runner would advance the slate's tally by one and return.

She needed the slate updated by the runner's pace, with a guarantee that by the time she read it, the runner had finished.

An agent is the slate the runner carries; the send form dispatches the work; the await form waits for return; the deref reads the slate's value.

To create an agent at 0, send an increment, wait for completion, read the value, They composed the agent's value after a send-and-await increment and submitted the form. The REPL coordinated the swift fox's return:

by the time Vix arrived, the runner had returned, and the slate showed one more than it had started with.

Question: write a Clojure expression for the slate's tally after the runner has returned with the new value.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox sent a swift runner ahead to the market with a small slate. The runner would advance the slate's tally by one and return.

She needed the slate updated by the runner's pace, with a guarantee that by the time she read it, the runner had finished.

An agent is the slate the runner carries; the send form dispatches the work; the await form waits for return; the deref reads the slate's value.

To create an agent at 0, send an increment, wait for completion, read the value, He composed the agent's value after a send-and-await increment and submitted the form. The REPL coordinated the swift fox's return:

by the time Vix arrived, the runner had returned, and the slate showed one more than it had started with.

What Clojure form computes the slate's tally after the runner has returned with the new value? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (def ag (agent 0)) (send ag inc) (await ag) @ag)"}}]}
````

---

## rewriterule — G10-03: defmacro introduction

_pool_: `_REWRITERULE_SUBPLOTS`

**The metaphor:** The patient fox's rewriting-quill — rewrites the tasting-card before reading. Mirrors macros.

### Story-scaffold render _(seed 48)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox kept a rewriting-quill at the orchard's posting wall. Whenever a shorthand tasting-card came in, she rewrote it into a longer card before any fox followed it — the new card had explicit checks and an in-order block the runtime would actually run.

She wanted the shorthand card to expand into a guarded block: the test up front, then all the body steps in order. Once expanded, the rewritten card would behave as if she had written the long form by hand.

A macro is a quill that rewrites the card before reading. `defmacro` registers the rewriting rule; the syntax-quote and unquote-splice splice the body into the new card's block. The expansion happens before runtime; only the rewritten form runs.

To define a macro that wraps body in a guarded do-block, and call it with three steps, They composed the value the rewritten guarded-block returns from its last step and submitted the form. The REPL — applying the rewriting-quill first, then evaluating the rewritten card — returned:

the rewritten card ran in order; the body's last step's value was what came back, just as if she had written the long form herself.

What Clojure form computes the value of the last step in the macro's expanded guarded block? Submit it via `eval`.

---

I let the runtime decide what the form evaluates to.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox kept a rewriting-quill at the orchard's posting wall. Whenever a shorthand tasting-card came in, she rewrote it into a longer card before any fox followed it — the new card had explicit checks and an in-order block the runtime would actually run.

She wanted the shorthand card to expand into a guarded block: the test up front, then all the body steps in order. Once expanded, the rewritten card would behave as if she had written the long form by hand.

A macro is a quill that rewrites the card before reading. `defmacro` registers the rewriting rule; the syntax-quote and unquote-splice splice the body into the new card's block. The expansion happens before runtime; only the rewritten form runs.

To define a macro that wraps body in a guarded do-block, and call it with three steps, He composed the value the rewritten guarded-block returns from its last step and submitted the form. The REPL — applying the rewriting-quill first, then evaluating the rewritten card — returned:

the rewritten card ran in order; the body's last step's value was what came back, just as if she had written the long form herself.

What Clojure form computes the value of the last step in the macro's expanded guarded block? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))"}}]}
````

---

## scribe — G1-10: Comments

_pool_: `_SCRIBE_SUBPLOTS`

**The metaphor:** Marginalia in the leather ledger — runtime ignores. Mirrors comments / whitespace / `do` / reader.

### Story-scaffold render _(seed 53)_

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Renard the fox wrote a fresh entry in the leather ledger: the day's first tally form, with a thin marginalia note spelling out what the form did.

Renard wanted the form's value but also wanted the marginalia preserved. The note must not change what the form evaluates to.

A single-semicolon comment is a scribe's marginalia: text the runtime ignores. The semicolon and what follows are dropped before evaluation.

To add 1 and 2, with a single-semicolon trailing comment, They composed an addition form followed by a single-semicolon margin comment and submitted the form. The REPL read by the scribe's conventions and returned:

the form returned its honest sum, and the marginalia stayed in the margin — visible to the reader, invisible to the runtime.

Write a form whose evaluation gives the value of an addition form whose right-margin comment is dropped.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(+ 1 2) ; sum of one and two`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox wrote a fresh entry in the leather ledger: the day's first tally form, with a thin marginalia note spelling out what the form did.

Renard wanted the form's value but also wanted the marginalia preserved. The note must not change what the form evaluates to.

A single-semicolon comment is a scribe's marginalia: text the runtime ignores. The semicolon and what follows are dropped before evaluation.

To add 1 and 2, with a single-semicolon trailing comment, He composed an addition form followed by a single-semicolon margin comment and submitted the form. The REPL read by the scribe's conventions and returned:

the form returned its honest sum, and the marginalia stayed in the margin — visible to the reader, invisible to the runtime.

What Clojure form computes the value of an addition form whose right-margin comment is dropped? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(+ 1 2) ; sum of one and two"}}]}
````

---

## chalkmark — G1-09: Symbols vs values

_pool_: `_CHALKMARK_SUBPLOTS`

**The metaphor:** Chalk tag on vine-post vs the grape-cluster it names. Mirrors `quote` / symbols / syntax-quote.

### Story-scaffold render _(seed 53)_

**form**: `(symbol? 'fox)`  •  **expected**: `True`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox had been chalking name-tags onto the vine-posts all morning: each tag a quoted token, each post a real cluster the tag stood for. The chalked tag at the head of the row was a name, written but not yet read by anyone.

Vix wanted to know whether the chalked tag was the *kind of thing* a name is — a symbol — rather than a number or a string. The predicate would say so.

A quoted token is a symbol — a name standing for something, not the thing itself. The symbol? predicate asks of any value: is this one of those name-tokens? The chalk tag is the symbol; the cluster behind it is what the tag names.

To ask whether a quoted name is a symbol, using the symbol? predicate, They composed the predicate that asks if a quoted name is a symbol and submitted the form. The REPL — distinguishing the chalk tag from the cluster it names — returned:

the predicate confirmed what the chalk had drawn — a name, not a value — and Vix moved on to tag the next vine.

Write a form whose evaluation gives whether a quoted name is a symbol.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'fox)"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(symbol? 'fox)`  •  **expected**: `True`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox had been chalking name-tags onto the vine-posts all morning: each tag a quoted token, each post a real cluster the tag stood for. The chalked tag at the head of the row was a name, written but not yet read by anyone.

Vix wanted to know whether the chalked tag was the *kind of thing* a name is — a symbol — rather than a number or a string. The predicate would say so.

A quoted token is a symbol — a name standing for something, not the thing itself. The symbol? predicate asks of any value: is this one of those name-tokens? The chalk tag is the symbol; the cluster behind it is what the tag names.

To ask whether a quoted name is a symbol, using the symbol? predicate, He composed the predicate that asks if a quoted name is a symbol and submitted the form. The REPL — distinguishing the chalk tag from the cluster it names — returned:

the predicate confirmed what the chalk had drawn — a name, not a value — and Vix moved on to tag the next vine.

What Clojure form computes whether a quoted name is a symbol? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(symbol? 'fox)"}}]}
````

---

## sortingtable — G8-08: Multimethod defmulti

_pool_: `_SORTINGTABLE_SUBPLOTS`

**The metaphor:** Market sorting-tray — routes by tag. Mirrors multimethods.

### Story-scaffold render _(seed 46)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox set up a sorting-tray at the market. The tray dispatched each basket by the :species tag stamped on it — one channel per species, more added by anyone.

He needed to register a handler for one species, then drop a basket bearing that tag onto the tray.

A defmulti posts the tray and the dispatch rule. A defmethod registers a channel for one tag. Calling the multimethod reads the tag and routes through the matching channel.

To define a multimethod that dispatches on a :species tag, register a method for one species, then call it, They composed the multimethod call routed through a registered species channel and submitted the form. The REPL routed the basket through the market sorting-tray:

the basket's tag routed it through the registered channel, and the tray returned that channel's habit-word.

Question: write a Clojure expression for the channel's habit-word for a basket bearing a registered species tag.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox set up a sorting-tray at the market. The tray dispatched each basket by the :species tag stamped on it — one channel per species, more added by anyone.

He needed to register a handler for one species, then drop a basket bearing that tag onto the tray.

A defmulti posts the tray and the dispatch rule. A defmethod registers a channel for one tag. Calling the multimethod reads the tag and routes through the matching channel.

To define a multimethod that dispatches on a :species tag, register a method for one species, then call it, He composed the multimethod call routed through a registered species channel and submitted the form. The REPL routed the basket through the market sorting-tray:

the basket's tag routed it through the registered channel, and the tray returned that channel's habit-word.

What Clojure form computes the channel's habit-word for a basket bearing a registered species tag? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))"}}]}
````

---

## carryingcase — G8-02: deftype introduction

_pool_: `_CARRYINGCASE_SUBPLOTS`

**The metaphor:** Labeled fruit-crate with named compartments. Mirrors `deftype` / `defrecord`.

### Story-scaffold render _(seed 46)_

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Renard the fox had built a labeled fruit-crate at the press with one named compartment. Each crate of his own type carried just that single field, fixed at the time of construction.

He had just packed a fresh crate, marking its slot, and now wanted to read back what was written on its label without unpacking the rest of the crate.

`deftype` declares a crate's shape — its named compartments. Constructing the type fills those slots; the field-access form reads the value at the named compartment directly. The shape is fixed; the slot's value is stamped at build time.

To define a Pebble type with a color field, build one, and read its color, They composed the field-access on a deftype-instance and submitted the form. The REPL constructed the labeled fruit-crate:

the label slot read back the value Renard had stamped at the press — the crate's own field, fetched in one step.

Question: write a Clojure expression for the value at the named compartment of the labeled crate.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Renard the fox had built a labeled fruit-crate at the press with one named compartment. Each crate of his own type carried just that single field, fixed at the time of construction.

He had just packed a fresh crate, marking its slot, and now wanted to read back what was written on its label without unpacking the rest of the crate.

`deftype` declares a crate's shape — its named compartments. Constructing the type fills those slots; the field-access form reads the value at the named compartment directly. The shape is fixed; the slot's value is stamped at build time.

To define a Pebble type with a color field, build one, and read its color, He composed the field-access on a deftype-instance and submitted the form. The REPL constructed the labeled fruit-crate:

the label slot read back the value Renard had stamped at the press — the crate's own field, fetched in one step.

What Clojure form computes the value at the named compartment of the labeled crate? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))"}}]}
````

---

## tallywalk — G2-20: Counting

_pool_: `_TALLYWALK_SUBPLOTS`

**The metaphor:** Walking the vine-row tallying clusters. Mirrors `reduce` / `count`.

### Story-scaffold render _(seed 53)_

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Vix the fox walked the vine-row with a slate, ticking off each cluster as she passed it. The row carried three clusters this morning — she would walk it once and report the tally at the end.

She wanted the row's length — not which clusters were there, just how many — landing on the slate as a single honest number.

The count form is the tally-walk: it visits each item in the collection once, ticking the slate, and returns the tick-total. The walk is the operation; the slate's final number is the return value.

To count the items in a small vector, They composed the length of a small vector and submitted the form. The REPL walked the vine-row carrying the running tally:

the slate at the row's end held the row's length — Vix's honest tick-count, ready to be posted to the day's harvest log.

Write a form whose evaluation gives the row's tick-total after the tally-walk.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(count [1 2 3])`  •  **expected**: `3`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Vix the fox walked the vine-row with a slate, ticking off each cluster as she passed it. The row carried three clusters this morning — she would walk it once and report the tally at the end.

She wanted the row's length — not which clusters were there, just how many — landing on the slate as a single honest number.

The count form is the tally-walk: it visits each item in the collection once, ticking the slate, and returns the tick-total. The walk is the operation; the slate's final number is the return value.

To count the items in a small vector, He composed the length of a small vector and submitted the form. The REPL walked the vine-row carrying the running tally:

the slate at the row's end held the row's length — Vix's honest tick-count, ready to be posted to the day's harvest log.

What Clojure form computes the row's tick-total after the tally-walk? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(count [1 2 3])"}}]}
````

---

## beadstring — G2-11: String concatenation with str

_pool_: `_BEADSTRING_SUBPLOTS`

**The metaphor:** Beads on the market-fox's counting-cord. Mirrors string ops.

### Story-scaffold render _(seed 53)_

**form**: `(str "x" "y" "z")`  •  **expected**: `'xyz'`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach.

Sly the fox had three short cords of lettered beads on the market-fox's counting-table, each cord just one letter long. The cords sat side by side, ready to be tied head-to-tail in order.

Sly wanted one continuous cord — the three cords' beads in the order they were laid out, threaded into a single string.

The str form ties cords end-to-end: each argument is a cord of beads, and the result is one long cord. The first arg's beads come first; the next arg's are knotted to its tail; the third's to that tail in turn.

To concatenate three single-character strings into one, They composed the three-arg concatenation of single-character strings and submitted the form. The REPL spliced or counted the cord of beads as the form said:

the joined cord carried all three letters in their original order, head-to-tail in one piece, and Sly hung it from the stall.

Write a form whose evaluation gives the joined cord the three single-letter strings produce.

---

I express the form as Clojure source.

{"tool_calls":[{"name":"eval","args":{"form":"(str \"x\" \"y\" \"z\")"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(str "x" "y" "z")`  •  **expected**: `'xyz'`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox had three short cords of lettered beads on the market-fox's counting-table, each cord just one letter long. The cords sat side by side, ready to be tied head-to-tail in order.

Sly wanted one continuous cord — the three cords' beads in the order they were laid out, threaded into a single string.

The str form ties cords end-to-end: each argument is a cord of beads, and the result is one long cord. The first arg's beads come first; the next arg's are knotted to its tail; the third's to that tail in turn.

To concatenate three single-character strings into one, He composed the three-arg concatenation of single-character strings and submitted the form. The REPL spliced or counted the cord of beads as the form said:

the joined cord carried all three letters in their original order, head-to-tail in one piece, and Sly hung it from the stall.

What Clojure form computes the joined cord the three single-letter strings produce? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(str \"x\" \"y\" \"z\")"}}]}
````

---

## circuit — G5-22: recur — first taste

_pool_: `_CIRCUIT_SUBPLOTS`

**The metaphor:** Walking back to the head of the row each lap — no growing trail. Mirrors `recur` / `loop`.

### Story-scaffold render _(seed 46)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
A hungry Fox came upon a vine of grapes hanging just out of reach. This was near the woods.

Sly the fox stood at the head of a five-vine row, slate in paw. On each lap he would multiply the running tally by the current vine's number, then walk back to the head of the row with the new tally and the next vine to count.

Sly wanted the running product of all five vine-numbers — five times four times three and so on down — landing as the row-end tally on the slate.

`loop` sets the head of the row with starting bindings; `recur` is walking back to that head with new values, not stacking new walks on the old. The base case `zero?` is the row's end — no more vines to multiply, return the tally.

To compute the factorial of 5 by looping a counter down to 0 with a running product, They composed the loop-recur factorial of five and submitted the form. The REPL — walking each lap back to the head of the row without growing the trail — returned:

after the fifth lap the row's end was reached, and the slate held the running product of every vine — exactly the factorial Sly had set out to count.

Question: write a Clojure expression for the row-end product after walking the five-vine row.

---

Here's the calculation.

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

### Family-template render _(seed 12345)_

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

````text
The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.

Sly the fox stood at the head of a five-vine row, slate in paw. On each lap he would multiply the running tally by the current vine's number, then walk back to the head of the row with the new tally and the next vine to count.

Sly wanted the running product of all five vine-numbers — five times four times three and so on down — landing as the row-end tally on the slate.

`loop` sets the head of the row with starting bindings; `recur` is walking back to that head with new values, not stacking new walks on the old. The base case `zero?` is the row's end — no more vines to multiply, return the tally.

To compute the factorial of 5 by looping a counter down to 0 with a running product, He composed the loop-recur factorial of five and submitted the form. The REPL — walking each lap back to the head of the row without growing the trail — returned:

after the fifth lap the row's end was reached, and the slate held the running product of every vine — exactly the factorial Sly had set out to count.

What Clojure form computes the row-end product after walking the five-vine row? Submit it via `eval`.

---

{"tool_calls":[{"name":"eval","args":{"form":"(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))"}}]}
````

---

