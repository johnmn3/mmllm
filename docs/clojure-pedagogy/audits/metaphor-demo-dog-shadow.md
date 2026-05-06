# Metaphor demo — dog-shadow curriculum

One canonical subject per metaphor family. Each shows two renders:

- **Story-scaffold render**: the example's authored `scenario` / `need` / `mapping` / `resolution` slots composed into a 5-act grounded story by the `_story()` template (Phase C framework). The metaphor *drives* the action — concrete situation, specific need, explicit mapping, resolution that closes the loop.
- **Family-template render**: one of the family pool's generic templates, for contrast. Same example, no story slots used.

Coverage: 22 metaphor families. Across 216 dog-shadow subjects: 8 atoms (form-display IS the lesson), 185 metaphor-rich subjects (22 families) with 412 story-slotted examples (97% coverage), and 23 abstract subjects on `_GOAL_SUBPLOTS`.

Imagery anchors: bone-in-mouth (let), nose-trail (fn), hollow-log cache (collections), gap-in-a-log (HOFs), tally-stone (atom), counting-bones (numbers), stream-crossing-conditions (boolean), fork-at-the-bank (cond), marker-stone (def), log-bridge-test (try), message-bone (IO), pack-agreement (protocols), kennel-master's-tools (host interop), scout-dog (agent), scent-mark-rewrite (macros), bark-scratch conventions (reader), bone-scratch-vs-bone (quote), sorting-bones (multimethods), kennel-bag (deftype), walking-the-bone-row (reduce), scratch-mark-string (str), pacing-the-bank (recur).

---

## let — local binding — G3-03

_pool_: `_POUCH_SUBPLOTS`

**form**: `(let [x 3] (+ x 1))`  •  **expected**: `4`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound had picked up a small bone near the pond and held it firmly between her jaws. Just for the next stretch of crossing she would need to know the bone's tally — 3 — by a short local name x.

She wanted the running total — what x plus one more would come to — at the moment her paw left the far bank. After that stretch, the mouth would empty and x would mean nothing again.

The closed jaws are the let-binding, x is the name for what's gripped between the teeth, the value held there is 3, and the form's stretch is the crossing. Outside the form, the mouth empties and the binding goes with it.

To bind a value of 3 to a local name x for one stretch, then return that value plus one, She composed the local binding and addition with the binding gripped safely between the teeth and submitted the form. The REPL pulled from the mouth as the form directed:

The REPL pulled from the mouth as the form directed and handed back the running total. Past the crossing, Bell's mouth was empty again — the binding had been in force only for that stretch.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

Rex the dog brushed past the marker stone near the meadow, with a glint of impatience,
and saw his reflection in the water — sure that the
shadow-bone was bigger than the one in his jaws.
He opened his mouth to snap, and the real
bone fell with a splash. Bell the dog, holding firm, intended
to bind a value of 3 to a local name x for one stretch, then return that value plus one: the value was gripped for exactly that stretch.
Bell composed the local binding and addition, submitted the form, and the
REPL — taking the binding from the mouth as the form told it to —
handed back the answer Rex had not even thought to keep.

Question: write a Clojure expression for the running total after binding x to 3 and adding 1.
````

---

## fn — anonymous function — G3-07

_pool_: `_RECIPE_SUBPLOTS`

**form**: `((fn [x] (+ x 1)) 4)`  •  **expected**: `5`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound put her nose to the ground at the bank near the pond and laid out a careful sniffing-trail: take whatever you find, add one bone's worth, carry the result back. She did not name the trail — it would only be walked once.

She had just one input in mind — a starting count — and wanted the answer at the trail's end without ever needing to remember the trail's name afterward.

The trail is the anonymous fn, the single sniff is add-one-bone, the input value is what gets carried into the trail's first step, and what comes back from the last sniff is the trail's value.

To create an anonymous function that adds 1 to its argument and apply it to 4, She laid out the anonymous function call along the nose-trail and submitted the form. The REPL walked the trail end to end:

The REPL walked the trail end to end and handed back the value at the last sniff. The trail itself, having served Bell for that one walk, faded back into the bank.

Question: write a Clojure expression for the result of applying an anonymous fn that adds 1 to its argument to the value 4.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"On any nose-trail," Bell the dog explained, "the last sniff
is what you carry home." She took the goal — to
create an anonymous function that adds 1 to its argument and apply it to 4 — and laid out the routine's paw-steps in order,
knowing that whatever the final sniff turned up was what would
come back. Bell composed the anonymous function call, submitted the form,
and the REPL — discarding the earlier sniffs — handed back only
the value of the last.

Question: write a Clojure expression for the result of applying an anonymous fn that adds 1 to its argument to the value 4.
````

---

## keyword as map lookup — G2-17

_pool_: `_BASKET_SUBPLOTS`

**form**: `(:hare {:hare 1 :tortoise 2})`  •  **expected**: `1`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound paused at a hollow log near the pond. Inside, two bones rested in named slots — one labeled :hare, one labeled :tortoise.

She wanted the bone in the :hare slot — without disturbing the other. The cache itself would stay as it was for any later dog.

The cache is the map, named slots are the keys, the labels are scratched above each slot, and the bones inside are the values.

To use the keyword :hare to look up a value in the map with keys :hare and :tortoise, She composed the keyword lookup for the bone-cache and submitted the form. The REPL handed back the arrangement:

The REPL reached into the named slot and handed back its bone. The cache stayed exactly as it was, the other slot undisturbed.

Question: write a Clojure expression for the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

A row of bones lay tucked end-to-end inside the log near the meadow, head
at the front, the rest trailing behind. "Many of our caches are
like this row," Bell the dog said. "You can grab the first bone,
you can ask for the rest, you can lay a new bone at the front of
the row." To use the keyword :hare to look up a value in the map with keys :hare and :tortoise, she composed the keyword lookup,
submitted the form, and the REPL ran the row exactly as the form
described.

Question: write a Clojure expression for the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}.
````

---

## into — list to vector — G4-16

_pool_: `_SIEVE_SUBPLOTS`

**form**: `(into [] '(1 2 3))`  •  **expected**: `[1, 2, 3]`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound balanced an empty hollow log under the gap-in-the-log spanning the stream near the pond. A small chain of bones — three of them, in order — rested at the near end, ready to pour through.

She wanted the same three bones to land in the empty receiver, in their original order, but as a row that could be read from either end rather than only from the front.

The gap is the transducer (here, identity since `into` carries no xform), the source is the chain of three bones, the empty receiver below the gap is the vector, and what lands in it is the result.

To convert a list containing 1, 2, and 3 into a vector, She composed building a vector from a list as the gap's rule, ran the input through, and submitted the form. The REPL caught what landed below:

The REPL ran each bone through the gap and packed it into the receiving log. The chain above stayed as it had been; the row below now held the three bones in their original order.

Question: write a Clojure expression for the vector built from a list.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

Bell the dog laid two gapped logs above one another, the bones
that passed the first gap arriving at the second. "What lands at
the bottom," she said, "has been through both rules in
order — applied as a single combined gap." To convert a list containing 1, 2, and 3 into a vector,
She composed building a vector from a list as a stack of gaps,
ran the input through, submitted the form, and the REPL caught
what the stack had let through.

Question: write a Clojure expression for the vector built from a list.
````

---

## atom — counter — G9-02

_pool_: `_NOTEBOOK_SUBPLOTS`

**form**: `(do (def counter (atom 0)) (swap! counter inc) @counter)`  •  **expected**: `1`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

A flat tally-stone sat at the stream's edge near the pack's morning route. Bell the hound chose it as the day's running counter and scratched a fresh zero into it as the starting tally for the season.

When the next dog passed and a bone was added to the cache, the count on the stone would need to step up by one — and any pack member arriving later should see the new tally, not the old.

The stone is the atom, the scratched count is its current value, swap! is the read-apply-write motion in one go, inc is the change applied, and dereferencing is just looking at what the stone now says.

To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, She composed binding an atom to counter, atomically incrementing it, and dereferencing the result for the tally-stone and submitted the form. The REPL applied the update at the stream's edge:

The REPL applied the update atomically, scratched the new tally into the stone, and handed back what the stone now read. Any later dog at the bank would see the same updated count.

Question: write a Clojure expression for the value after atomically swapping counter with inc and dereferencing.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"The tally stays scratched into the stone," Bell the dog said,
"so any dog who comes by can read what's there right now. The
count changes only when one of us scratches a new one — and only
as the runtime allows." To construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result, She
composed binding an atom to counter, atomically incrementing it, and dereferencing the result, submitted the form, and the REPL —
reading or scratching the tally as the form prescribed — handed
back the value the stone had carried.

Question: write a Clojure expression for the value after atomically swapping counter with inc and dereferencing.
````

---

## first arithmetic call — G1-13

_pool_: `_ACORN_SUBPLOTS`

**form**: `(+ 1 2)`  •  **expected**: `3`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound sat by a flat stone near the pond and laid out two small piles of bones — one of one bone, one of two — careful with the count.

She wanted the precise size of the heap if both piles were nudged together — small or large, the runtime would give the exact number, and that was the count she would carry forward.

The bones are the numbers, the piles are the operands, the act of nudging-together is +, and the count of the combined heap is what the REPL hands back.

To add 1 and 2, She composed the addition and submitted the form. The REPL counted out the answer:

The REPL added the two piles and handed back the precise count. Bell brushed the bones back into a single tidy heap — the answer settled, no eyeballing needed.

Question: write a Clojure expression for the sum of 1 and 2.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

Bell the dog arranged a small heap of bones near the meadow, careful
with the count. "Numbers in Clojure don't fudge,"
she said. "Whatever you do — adding, subtracting,
dividing into piles with leftovers, comparing two heaps — the
runtime gets it exactly right, every time." To add 1 and 2,
She composed the addition, submitted the
form, and the REPL handed back the precise number the operation
called for.

Question: write a Clojure expression for the sum of 1 and 2.
````

---

## equality — G1-15

_pool_: `_GATE_SUBPLOTS`

**form**: `(= 1 1)`  •  **expected**: `True`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound paused at the stream's edge with a pebble in each paw and held them up side by side. The crossing-conditions of the day were simple: either the two pebbles match, or they do not.

She wanted only the verdict — does the runtime see them as equal? — without having to count or compare the pebbles by eye, so the answer would be the runtime's, not hers.

The crossing-condition is =, the two pebbles are the operands, and the verdict — true or false — is what swings the way open or closed for the next step.

To test whether 1 equals 1 with =, She composed the equality check and submitted the form. The REPL let the crossing-conditions decide:

The REPL checked the two values, the conditions ruled, and the verdict came back. Bell trotted on, the matter settled by the runtime exactly as the rule said.

Question: write a Clojure expression for whether 1 equals 1.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"You can't tell whether the crossing will be open by guessing,"
Bell the dog said. "You bring the value to the bank, the
runtime checks it, and the conditions give the only answer that
matters." To test whether 1 equals 1 with =, She composed
the equality check, submitted the form, and the REPL settled the
matter — the conditions had spoken exactly as the rule said.

Question: write a Clojure expression for whether 1 equals 1.
````

---

## if — condition — G5-01

_pool_: `_FORK_SUBPLOTS`

**form**: `(if true :a :b)`  •  **expected**: `':a'`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

The path forked at the bank near the pond. Two arms branched off — upstream and downstream — each marked by a small condition-stone. Bell the hound studied the stone at the fork: it carried a clear verdict that the way was open.

She wanted the answer to which arm of the fork she would actually take — without any wasted sniffing of the unrun arm — so only the chosen arm's value would come back from the runtime.

The fork is the if-form, the condition-stone is the test, the upstream arm is the then-branch and the downstream arm is the else-branch. Only the matching arm's value is what the REPL hands back.

To choose between :a and :b based on a true condition, She composed the conditional and submitted the form. The REPL took the right arm:

The REPL read the condition, took the matching arm, and handed back its value. The other arm remained unrun, the path beneath it untouched.

Question: write a Clojure expression for which of :a or :b is returned.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"What's important about a fork," Bell the dog said, "is that
the arm not taken doesn't run at all. The runtime checks the
condition, walks the right arm, and the unrun arm is just left
behind." To choose between :a and :b based on a true condition, She composed
the conditional, submitted the form, and the REPL — running
only what was needed — handed back the value of the chosen
arm.

Question: write a Clojure expression for which of :a or :b is returned.
````

---

## def — top-level binding — G3-01

_pool_: `_ROADSIGN_SUBPLOTS`

**form**: `(do (def x 42) x)`  •  **expected**: `42`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound chose a flat stone at the bank near the pond and scratched a fresh name into its surface — x — pressing the stone's value beside the marker so any later dog could read it.

She would consult the marker further along and would want the value the stone now bore — without any guessing about what x meant. The runtime, reading the bank, would settle the matter.

The marker stone is the def, the name x is the symbol scratched on the stone, the value is what's pressed beside it, and reading the marker is what the runtime does whenever a later form names x.

To bind x to 42 and return it, She composed the top-level binding and lookup and submitted the form. The REPL read the markers and replied:

The REPL set the marker, then read it back as the form directed, handing back the value the stone had recorded. Any later dog along the bank would see the same name bound to the same value.

Question: write a Clojure expression for the value of x after using def to bind x to 42.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

A small set of marker stones stood in a half-circle near the meadow, each
stone carrying the names for one stretch of riverbank. "Names
live in groups," Bell the dog said: "to use a name from a
stretch you didn't dig, you make sure that stretch's stones are
where the runtime can find them." To bind x to 42 and return it,
She composed the top-level binding and lookup, submitted the form,
and the REPL — finding the right name on the right stone —
returned the value the form had asked for.

Question: write a Clojure expression for the value of x after using def to bind x to 42.
````

---

## errors safe in REPL — G1-18

_pool_: `_SAFETYNET_SUBPLOTS`

**form**: `(+ 1 2)`  •  **expected**: `3`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound stood at the edge of a small log spanning the stream near the pond. She tested the log's hold paw by paw before trusting full weight: a slip would not end the day, only bend it.

She wanted the running total of two small piles — added on the practice bank where a stumble cost nothing — knowing the runtime would catch any error before it crossed.

The log-bridge test is the safety design of the REPL itself, the form is the careful step taken on the practice bank, and what the REPL hands back is the value the careful step earned.

To add 1 and 2, She composed the addition and submitted the form. The REPL — log tested in advance — handed back the value:

The REPL — net in place — handed back the precise count. Bell crossed safely, the arithmetic settled by the patient method, with no daring needed.

Question: write a Clojure expression for the result of adding 1 and 2.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"What matters when something goes wrong," Bell the dog said,
"is that the run can continue — the runtime catches the slip,
takes the recovery path, and the answer comes back even when
something inside the form went off the bank." To add 1 and 2,
She composed the addition, submitted the
form, and the REPL — handling the slip cleanly — returned the
value the recovery path had produced.

Question: write a Clojure expression for the result of adding 1 and 2.
````

---

## metadata extraction — G6-15

_pool_: `_SCROLL_SUBPLOTS`

**form**: `(:doc (meta '\{:doc "steady wins"\} race))`  •  **expected**: `'steady wins'`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound carried a long bone scratched with a name and a small marginal note — a message left by an earlier dog along the bank. The note's tag read :doc, and beside it ran a short instructive phrase.

She wanted only the marginal phrase from the bone — not the symbol it labeled, not the rest of the marks — so the next dog could read what the previous one had set there.

The bone is the form, the marginal scratches are its metadata, :doc is the slot the phrase lives in, and reading-the-tag is what the runtime does when the form asks for that slot.

To extract the :doc metadata value from a symbol with a docstring, She composed accessing the :doc metadata from a symbol and submitted the form. The REPL — claw to bark — completed the message-bone work:

The REPL read the marginal mark and handed back the phrase the previous dog had set there. The bone itself stayed untouched — the message-carrying scratch was simply read.

Question: write a Clojure expression for the docstring value from a symbol's metadata.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"The world outside the REPL is bigger than the REPL,"
Bell the dog said, "and a message-bone out there has its own
discipline — pick it up carefully, handle it with care, set it
back when you're done." To extract the :doc metadata value from a symbol with a docstring, She
composed accessing the :doc metadata from a symbol, submitted the form, and the REPL —
handling the bone the runtime's careful way — returned the value
the work had produced.

Question: write a Clojure expression for the docstring value from a symbol's metadata.
````

---

## polymorphism via dispatch — G8-01

_pool_: `_GUILD_SUBPLOTS`

**form**: `(defn speak [k] (cond (= k :hare) "swift" (= k :tortoise) "steady" :else "silent"))`  •  **expected**: `None`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound scratched a small set of pack-signals into a flat stone near the pond: every breed in the pack would honor the same call but answer in its own voice. She named the call speak.

When the call went out, the runtime would dispatch by the dog's breed — :hare or :tortoise — and each breed would give back its own characteristic phrase, no two alike.

The pack agreement is the function's shape, the call's name is speak, the dog's breed is the dispatch key, and each breed's voice is the answer associated with its key.

To define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, She composed conditional dispatch on a tag and submitted the form. The REPL — checking the pack ledger — dispatched cleanly:

The REPL set the agreement on the bank and the function value came back. Any later call to speak with a known breed would now produce that breed's characteristic phrase.

Question: write a Clojure expression for the function definition.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

Bell the dog held up the pack ledger — a slab of bark
scratched with breed-by-breed entries. "Membership is in this
record," she said: "the breed, the signals they
honor, and the actual answers each breed gives. The runtime
reads from the ledger whenever the call goes out." To
define a function speak that returns different strings depending on whether its argument is :hare or :tortoise, She composed conditional dispatch on a tag,
submitted the form, and the REPL — checking the ledger as it
ran — returned the right answer.

Question: write a Clojure expression for the function definition.
````

---

## host interop — symbol? — G6-14

_pool_: `_TOOLSHED_SUBPLOTS`

**form**: `(symbol? 'java.util.List)`  •  **expected**: `True`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound stopped beside the kennel-master's shed near the pond. On a peg hung an unfamiliar tool — a host-side label scratched in the kennel-master's hand, written as if it were a path.

She wanted only the runtime's verdict on what kind of mark the label was — a name the dogs could quote, or something else — without trying to use the tool itself.

The label on the peg is the quoted Java class name, the runtime is the kennel-master's bridge, and the symbol-predicate is the question of which kind of mark this is, answered without invoking the host tool.

To test whether a Java class name written as a quoted symbol is a symbol, She composed testing whether a value is a symbol and submitted the form. The REPL — calling into the kennel-master's shed — returned:

The REPL read the mark, applied the predicate, and handed back the verdict. The tool itself stayed on its peg — only its label had been examined.

Question: write a Clojure expression for whether a dotted Java class name is a symbol.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"Kennel-master's tools work, but they need careful handling,"
Bell the dog said. "Their labels are different, their calling
conventions are different, and the runtime has to bridge between
the dogs' world and the human's every time." To test whether a Java class name written as a quoted symbol is a symbol,
She composed testing whether a value is a symbol, submitted the form,
and the REPL — making the bridge cleanly — handed back the value
the foreign tool had produced.

Question: write a Clojure expression for whether a dotted Java class name is a symbol.
````

---

## macros — defmacro — G10-03

_pool_: `_REWRITERULE_SUBPLOTS`

**form**: `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-when true 1 2 3))`  •  **expected**: `3`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound crouched at a fresh patch of bark near the pond, paw poised. She would set a rule that any later mark of a certain shape would be rewritten — before the runtime ever followed it — into a different mark with the same intent.

When any later form named my-when was scratched, the runtime should first rewrite it into an equivalent if-form, then evaluate that. The rule would do the work once; every use would benefit.

The rule is the macro, the source shape is the my-when form, the rewritten shape is the equivalent if-form, and the runtime applies the rewrite before evaluation begins.

To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, She composed defining a conditional macro and invoking it and submitted the form. The REPL — applying the rewrite, then evaluating the rewritten form — returned:

The REPL set the rule on the bark, walked through the use, rewriting first and evaluating second. The rewritten form yielded the value the original had asked for.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"The order matters," Bell the dog said. "When a rule is
involved, the runtime first walks through the form and applies
the rule wherever it sees one — and only then does it evaluate
the result." To define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body, She composed
defining a conditional macro and invoking it, submitted the form, and the REPL — rewriting
first, evaluating second — returned the final value.

Question: write a Clojure expression for the value the rewritten if-do form returns when the test is true and the body has three expressions.
````

---

## comments — semicolon — G1-10

_pool_: `_SCRIBE_SUBPLOTS`

**form**: `(+ 1 2) ;; sum of one and two`  •  **expected**: `3`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound wrote a form on a clean strip of bark near the pond, then added a double-semicolon mark followed by a note in plain words. "The note is only for other dogs to read," she said. "The REPL will stop at the semicolon."

She wanted the runtime to ignore the trailing prose and hand back the value before the comment-sign. The note was pack knowledge, not code.

The arithmetic form is what the runtime evaluates. The double-semicolon marks where the comment begins. What comes after is skipped entirely by the reader — kept on the bark for later dogs only.

To add 1 and 2, with a double-semicolon trailing comment, She composed the addition with a trailing comment and submitted the form. The REPL read by the conventions and returned:

The REPL read the marks up to the comment-sign, evaluated the form, and handed back its value. The note stayed on the bark, untouched, waiting for the pack.

Question: write a Clojure expression for the result, ignoring the comment.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

Bell the dog smoothed a fresh strip of bark near the meadow and
scratched slowly, paying attention to every mark. "The form has
to be written so the reader can read it cleanly,"
she said. "If the marks are right, the runtime gets
the right form; if not, not." To add 1 and 2, with a double-semicolon trailing comment,
She composed the addition with a trailing comment, submitted the
form, and the REPL — reading exactly as scratched — returned
the value cleanly.

Question: write a Clojure expression for the result, ignoring the comment.
````

---

## symbols vs values — G1-09

_pool_: `_CHALKMARK_SUBPLOTS`

**form**: `(symbol? 'hare)`  •  **expected**: `True`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound pointed at a name scratched into a piece of bark — the mark, not what it pointed to. The reflection in the stream had looked like a bone, but the scratch that says bone is not the bone either; the same kind of distinction was at work here.

She wanted only the runtime's verdict on what the scratch is — a name the dogs can quote and pass around — without resolving the scratch to whatever it might point to.

The scratch on the bark is the symbol, the actual bone (or whatever the name might point to) would be the value, and the predicate is the question of which kind of thing the form is talking about.

To ask whether a quoted name is a symbol, using the symbol? predicate, She composed the symbol-predicate on a quoted name and submitted the form. The REPL — distinguishing scratch from bone — returned:

The REPL read the form, distinguishing scratch from bone, and handed back the verdict. The mark and the bone stayed two distinct things, exactly as the scratch had said.

Question: write a Clojure expression for whether a quoted name is a symbol.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"There's a difference between *labeling* the form and
*evaluating* it," Bell the dog said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say otherwise." To ask whether a quoted name is a symbol, using the symbol? predicate,
She composed the symbol-predicate on a quoted name, submitted the
form, and the REPL — labeling exactly what the form asked for —
returned the form-as-data, exactly as the marks had directed.

Question: write a Clojure expression for whether a quoted name is a symbol.
````

---

## agent / async — G9-10

_pool_: `_RUNNERAHEAD_SUBPLOTS`

**form**: `(do (def ag (agent 0)) (send ag inc) (await ag) @ag)`  •  **expected**: `1`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound dispatched a young scout-dog along the bank near the pond — an instruction in jaws to step the scout's tally up by one — while she stayed back arranging the next bit of work.

She would not look at the scout's satchel until the scout had returned — patience first — and only then ask for the value carried back.

The scout is the agent, the instruction is the function sent, the await is synchronization, and the dereference asks for the scout's final value.

To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference, She composed agent, send, await, deref and submitted the form. The REPL coordinated the scout's return:

The REPL coordinated the scout, awaited its completion, and handed back the value the scout had delivered. Bell read it without snatching too early.

Question: write a Clojure expression for the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"The hard part isn't sending the scout," Bell the dog said.
"The hard part is being patient enough to wait for the answer
when it comes — not snatching too early, not giving up too soon.
The runtime makes that easier than it sounds." To construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference,
She composed agent, send, await, deref, submitted the
form, and the REPL — coordinating the wait properly — returned
the scout's answer when the scout had it ready.

Question: write a Clojure expression for the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing.
````

---

## multimethods — defmulti — G8-08

_pool_: `_SORTINGTABLE_SUBPLOTS`

**form**: `(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))`  •  **expected**: `':swift'`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

A flat stone sat at the bank near the pond. Bell the hound chose the species stamp as the dispatch key and added one pile for the hare breed with its own pace-word.

When a runner of a known breed arrived, the stone would route the runner to the matching pile and that pile's pace-word would come back.

The sorting-stone is the multimethod, the species stamp is the dispatch key, each breed's pile is a defmethod, and the pace-word is what the runtime returns.

To declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, She composed the multimethod and its first arm and submitted the form. The REPL routed through the piles:

The REPL read the species, picked the matching pile, and handed back its pace-word. The stone stood ready for any later breed.

Question: write a Clojure expression for the pace returned for a runner stamped :hare after the table routes to its arm.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"What the stone sorts by is up to you," Bell the dog said.
"You decide what to look at on each bone — a kind, a smell, a
size, anything. The runtime reads it, finds the matching pile,
and runs that one." To declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table, She composed
the multimethod and its first arm, submitted the form, and the REPL — reading
what the dispatch function produced — returned the value the
right pile had given.

Question: write a Clojure expression for the pace returned for a runner stamped :hare after the table routes to its arm.
````

---

## deftype — labeled bag — G8-02

_pool_: `_CARRYINGCASE_SUBPLOTS`

**form**: `(do (deftype Pebble [color]) (.-color (Pebble. "grey")))`  •  **expected**: `'grey'`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound carved a small kennel-bag with a single labeled compartment — one slot, marked color — and slipped a stone of a particular shade into the slot. The bag's outside bore the kind-stamp Pebble.

She wanted to read the slot's contents back — exactly the shade the stone bore — by the slot's name, with the runtime fetching the field cleanly from the bag she had just constructed.

The bag is the deftype, its labeled compartment is the field, the kind-stamp is the type name, and field-access is asking the bag for the slot by name.

To define a type Pebble with a color field and then read the color field from an instance, She composed reading the color field of a Pebble instance and submitted the form. The REPL constructed the kennel-bag:

The REPL constructed the bag, fetched the named compartment, and handed back the shade the stone had borne. The bag itself kept its kind-stamp on the outside for any later read.

Question: write a Clojure expression for the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"A deftype is a barer bag," Bell the dog said. "Compartments,
a stamp — no map-like behavior unless you ask for it. Faster,
more focused, less convenient." To define a type Pebble with a color field and then read the color field from an instance,
She composed reading the color field of a Pebble instance, submitted the
form, and the REPL — constructing the bare bag as specified —
returned the value inside.

Question: write a Clojure expression for the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field.
````

---

## count — vector size — G2-20

_pool_: `_TALLYWALK_SUBPLOTS`

**form**: `(count [1 2 3])`  •  **expected**: `3`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound paced down a small row of cached bones near the pond — three of them lying end to end on a flat stone — adding one to her running tally at each bone, no other operation needed.

She wanted only the size of the row — how many bones lay in it — without examining what kind each one was. The runtime would do the counting for her, exact every time.

The row is the vector, each bone is one element, the running tally is the count, and the runtime's walk-and-add-one at each step is what count does for any collection.

To count the elements in the vector containing 1, 2, and 3, She composed the count operation and submitted the form. The REPL walked the bone-row carrying the tally:

The REPL walked the row, adding one at each bone, and handed back the size. The bones themselves stayed where they had been — the answer was the count, not the contents.

Question: write a Clojure expression for the result of using count on the vector containing 1, 2, and 3.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"You don't have to start the tally at zero," Bell the dog
said, holding up a stone already scratched with a number. "If
you start with a different value, the walk begins from there —
the combine-step folds each bone in from that starting point."
To count the elements in the vector containing 1, 2, and 3, She composed the count operation,
submitted the form, and the REPL — starting from the given
tally, walking the row — returned the final value.

Question: write a Clojure expression for the result of using count on the vector containing 1, 2, and 3.
````

---

## str — splice strings — G2-11

_pool_: `_BEADSTRING_SUBPLOTS`

**form**: `(str "ab" "cd")`  •  **expected**: `'abcd'`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound held up two short bark-strips at the bank near the pond, each scratched with a pair of marks.

She wanted the strips spliced into one longer strip — every mark in its place — without altering either original.

Each strip is a string, each scratch is one character, str is the splicing operation, and the result is the longer strip with both sets of marks in order.

To use str to splice the two-letter strings "ab" and "cd" into a single thread, She composed the string concatenation and submitted the form. The REPL spliced or counted as the form said:

The REPL spliced the strips and handed back the longer one. The two originals stayed as they had been.

Question: write a Clojure expression for the result of using str to splice "ab" and "cd".
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"To count the marks, walk the strip," Bell the dog said.
"Want a section of marks? Cut from one position to another and
you get a smaller strip, the original untouched." To
use str to splice the two-letter strings "ab" and "cd" into a single thread, She composed the string concatenation,
submitted the form, and the REPL — counting or cutting —
returned the answer the strip had given up.

Question: write a Clojure expression for the result of using str to splice "ab" and "cd".
````

---

## loop / recur — G5-22

_pool_: `_CIRCUIT_SUBPLOTS`

**form**: `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))`  •  **expected**: `120`

### Story-scaffold render

````text
What the Dog thought he saw beneath the water turned out to be his own reflection. All this took place by the beach.

Bell the hound paced back and forth along a stretch of stream bank near the pond, carrying a small running tally in her jaws. Each pass returned to the same starting point, with the tally a little different and the count of remaining passes one fewer.

She would loop until the count of remaining passes reached zero — the base case — and the final tally on that pass would be her answer, with no extra trail laid down behind her.

The pacing-without-growing-the-trail is recur, the binding pair is loop's initial state, the base case is the if-zero check, and the new bindings on each pass are what recur supplies.

To walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, She composed a factorial computation via loop and recur and submitted the form. The REPL paced without growing the trail:

The REPL paced the bank the right number of times, then stopped at the base case, and handed back the final tally. The trail beneath the pacing had not grown — the call-stack was exactly as it began.

Question: write a Clojure expression for the factorial of 5 computed by walking a circuit.
````

### Family-template render (for contrast)

````text
Greed has cost more than one creature what they already had.

"Every pacing has a stopping condition," Bell the dog said.
"Without one, the dog walks forever. With one, the dog knows
when the passes are done and the tally is the answer." To
walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero, She composed a factorial computation via loop and recur,
submitted the form, and the REPL — looping until the base case —
returned the value the final pass produced.

Question: write a Clojure expression for the factorial of 5 computed by walking a circuit.
````

---
