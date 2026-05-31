# Metaphor audit — does the narrative illuminate the idiom?

**Status of every subject as of the goal-style redesign + papercut+semantic
round (commit `ec62dcf`).**

The user's framing: a `let`-binding is structurally "putting things in
temporary buckets so we can use them later" — and the *narrative* should
say that, not just frame the idiom in a generic Hare/Tortoise-banter
template.

We currently have:
- **8 `_SHARED_SUBPLOTS`** (atoms G1-01..08): generic "Hare guesses,
  Tortoise reads the REPL" with `{form_display}`. No operation-specific
  metaphor.
- **12 `_GOAL_SUBPLOTS`** (everything else, 198 subjects): generic
  goal-driven banter. No operation-specific metaphor.

So the honest baseline: **almost no subject currently carries an
operation-specific fable metaphor in its narrative**. The fable is a
backdrop; the idiom is in the form. This audit catalogs which idioms
*could* be illuminated by an in-fable metaphor (≈180 of 216 subjects)
and which are abstract-by-nature meta/tooling concepts where adding a
forest-y metaphor would be cargo-cult (≈36 of 216).

Tags:
- 🟢 **HAS** — narrative currently illuminates the idiom (rare; mostly atoms).
- 🟡 **NEEDS** — strong fable-natural metaphor exists; current narrative
  doesn't carry it. Worth retrofitting.
- 🌐 **ABSTRACT** — host/tooling/meta concept. No natural metaphor in the
  fable world. Keep the current generic-banter narrative; it's not
  pretending otherwise.

Proposed metaphors are deliberately compact — 1-2 sentences per
subject — so a human reviewer can quickly approve the mapping, then a
sub-agent can author per-family subplot templates that bake the
metaphor into the narrative.

---

## Metaphor families (the high-leverage groupings)

Many subjects share a metaphor — implementing the metaphor as a *family*
of subplot templates and pointing many subjects at it is much cheaper
than per-subject custom templates. Rough family map:

| Family                          | Subjects covered                             | Metaphor                                                                   |
| ------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------- |
| **acorn-arithmetic**            | G1-13/14, G2-01..10, G2-19, G2-22            | adding/multiplying acorns; baskets that grow                               |
| **the-tally-walk**              | G2-20, G2-21, G4-13, G5-12/13                | walking a row carrying a count; reduce as a tally being carried            |
| **chalk-marks-vs-acorns**       | G1-09, G2-18, G10-01/02/04/05                | symbols are *names*, scratched on bark; values are the things named        |
| **bead-string**                 | G1-04, G2-11, G2-21, G7-12..15               | strings as strings of beads; concat = stringing more beads on              |
| **fork-in-the-path**            | G5-01..06, G5-08                             | if/cond/case/when as forks at a crossroads                                 |
| **gates-on-the-trail**          | G5-07, G2-13/14                              | and/or/not as gates that pass or stop the value                            |
| **temporary-pouch** ⭐           | G3-03..06, G3-11, G3-16, G3-18               | let-binding as a pouch the Tortoise wears for one stretch of road          |
| **road-sign**                   | G3-01/02/12, G3-17, G6-01..03/05/13          | def as a posted sign on the road; namespace as a library of signs         |
| **paw-step-recipe**             | G3-07..10, G3-13/15, G5-09, G5-14..17        | fn as a recipe / sequence of paw-steps                                     |
| **basket-and-label**            | G4-01..20                                    | vector = row of pebbles; map = labeled pouches; set = unique-only basket  |
| **sieve-and-pour**              | G5-10/11, G5-18..21, G12-01..03              | map = treat each the same; filter = sieve; into/transduce = pour through  |
| **circuit-around-the-meadow**   | G5-22                                        | recur as a loop back without growing the trail                             |
| **scroll-and-quill**            | G7-08..17, G6-15                             | IO as scrolls written/read; metadata as marginalia                         |
| **safety-net**                  | G7-01..07, G1-18                             | try/catch as a net under the Hare's leap; preconditions as fitness checks |
| **guild-of-runners**            | G8-01, G8-04..07, G8-11/13/14/16             | protocol as a guild; record-implementing-protocol = labeled guild member  |
| **carrying-case**               | G8-02/03                                     | deftype/defrecord as a custom or labeled carrying-case                     |
| **sorting-table**               | G8-08..10, G8-12, G8-15                      | multimethod as a sorting-table that routes by species                      |
| **shared-notebook-on-a-stump** ⭐| G9-01..09, G9-14/16/17/18                    | atom/ref as a notebook anyone can read; CAS = "only if still …"           |
| **runner-sent-ahead**           | G9-10..13, G9-15                             | future/agent/promise as a runner sent down the road                       |
| **rule-that-rewrites-recipes**  | G10-03/06..10/15/16                          | macro as a rule that rewrites the recipe before the runtime sees it       |
| **scribe-shorthand**            | G10-11..13, G1-10/11/12, G3-14, G2-12/16/17  | reader macros, comments, whitespace, parens as scribe conventions          |
| **tool-from-another-toolshed**  | G11-02/03/04/06..09, G11-14, G6-14           | host interop as borrowing a tool from a different toolshed                 |
| **ABSTRACT (no metaphor)**      | G6-10/11, G11-01/05/10..13, G12-04..18       | tooling, host platforms, library overviews — keep generic narrative        |

⭐ = high-priority families because they directly map a CS abstraction
onto a daily-life image the model + reader can carry forward.

---

## Per-subject classification

### Grade 1 — atoms + first eval

| ID    | Title                                  | Tag      | Family / metaphor                                             |
| ----- | -------------------------------------- | -------- | ------------------------------------------------------------- |
| G1-01 | Eval as substitution                   | 🟢 HAS  | atom — the form IS the answer; current narrative fine         |
| G1-02 | Integer numbers                        | 🟢 HAS  | atom literal                                                  |
| G1-03 | Ratios                                 | 🟡 NEEDS | acorn-arithmetic — "splitting a pie into halves"             |
| G1-04 | Strings                                | 🟡 NEEDS | bead-string — "a string of beads spells a word"              |
| G1-05 | Booleans                               | 🟢 HAS  | atom — "yes-paw or no-paw"; current narrative fine            |
| G1-06 | nil                                    | 🟡 NEEDS | "an empty hollow / a missing acorn — neither full nor false" |
| G1-07 | Keywords                               | 🟢 HAS  | atom — "a stamped tag"; current narrative fine                |
| G1-08 | Characters                             | 🟢 HAS  | atom — "a single letter scratched on bark"                    |
| G1-09 | Symbols vs values                      | 🟡 NEEDS | chalk-marks-vs-acorns — "the *name* of an animal isn't the animal" |
| G1-10 | Comments                               | 🟡 NEEDS | scribe-shorthand — "side-notes the REPL skips, like the Tortoise's marginalia" |
| G1-11 | Whitespace doesn't matter              | 🟡 NEEDS | scribe-shorthand — "the spacing of pebbles doesn't change the count" |
| G1-12 | Parens group; they don't multiply      | 🟡 NEEDS | scribe-shorthand — "fence-posts marking what belongs together; not a multiplication" |
| G1-13 | First arithmetic call                  | 🟡 NEEDS | acorn-arithmetic — "1 acorn + 2 acorns"                       |
| G1-14 | Nested call evaluation                 | 🟡 NEEDS | acorn-arithmetic — "a sub-tally inside the main tally"        |
| G1-15 | Equality                               | 🟡 NEEDS | "two acorns matching shape exactly"                            |
| G1-16 | Numeric predicates                     | 🟡 NEEDS | "is the basket empty? zero acorns?"                            |
| G1-17 | Printing vs returning                  | 🟡 NEEDS | scribe-shorthand — "the print is the *announcement*; the return is what *passes hand to hand*" |
| G1-18 | Errors are safe in the REPL            | 🟡 NEEDS | safety-net — "a stumble in the practice meadow doesn't lose the race" |

### Grade 2 — operators + arithmetic mastery

| ID    | Title                                                     | Tag      | Family / metaphor                                              |
| ----- | --------------------------------------------------------- | -------- | -------------------------------------------------------------- |
| G2-01 | Multi-arg arithmetic                                      | 🟡 NEEDS | acorn-arithmetic — "summing the day's haul"                   |
| G2-02 | Comparison chains                                         | 🟡 NEEDS | "checking each runner is faster than the next, in line"       |
| G2-03 | not= and = with multiple args                             | 🟡 NEEDS | "checking three pebbles match (or differ)"                    |
| G2-04 | min and max                                               | 🟡 NEEDS | acorn-arithmetic — "smallest / largest acorn in the basket"   |
| G2-05 | quot, rem, mod                                            | 🟡 NEEDS | acorn-arithmetic — "dividing acorns into baskets, with leftovers" |
| G2-06 | inc and dec                                               | 🟡 NEEDS | acorn-arithmetic — "one step forward / one step back"         |
| G2-07 | Absolute value                                            | 🟡 NEEDS | "distance forgets direction — three steps either way is three" |
| G2-08 | Arithmetic on ratios                                      | 🟡 NEEDS | acorn-arithmetic — "adding pie-slices"                         |
| G2-09 | Floats vs ints (the / operator)                           | 🟡 NEEDS | "splitting evenly: when it divides cleanly vs not"            |
| G2-10 | Powers via repeated multiplication                        | 🟡 NEEDS | acorn-arithmetic — "doubling and redoubling the heap"         |
| G2-11 | String concatenation with str                             | 🟡 NEEDS | bead-string — "stringing two strings of beads together"       |
| G2-12 | print and println — return values                         | 🟡 NEEDS | scribe-shorthand — "calling out vs handing back"              |
| G2-13 | and / or — short circuit, return values                   | 🟡 NEEDS | gates-on-the-trail — "the first false stops the chain"        |
| G2-14 | not — turning truthy to false                             | 🟡 NEEDS | gates-on-the-trail — "the opposite-of-paw"                    |
| G2-15 | Falsey values: only false and nil                         | 🟡 NEEDS | gates-on-the-trail — "only nothing-or-no triggers the else-path" |
| G2-16 | Truthy 0 and empty string                                 | 🟡 NEEDS | scribe-shorthand — "even an empty basket is *something*"      |
| G2-17 | Keyword as function for map lookup                        | 🟡 NEEDS | basket-and-label — "the tag walks straight to its tagged item" |
| G2-18 | Quoting symbols                                           | 🟡 NEEDS | chalk-marks-vs-acorns — "labelling the name vs evaluating it" |
| G2-19 | Auto-promotion to bigint                                  | 🟡 NEEDS | acorn-arithmetic — "the heap grows beyond the basket; bigger basket appears" |
| G2-20 | Counting                                                  | 🟡 NEEDS | the-tally-walk — "tallying with toes / pebbles in a row"      |
| G2-21 | String length and substring                               | 🟡 NEEDS | bead-string — "tally of beads in the string"                  |
| G2-22 | Compose pure arithmetic                                   | 🟡 NEEDS | acorn-arithmetic — "step-by-step around the meadow"           |

### Grade 3 — naming and scope

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G3-01 | def — top-level binding            | 🟡 NEEDS | road-sign — "posting a sign by the road that everyone reads"      |
| G3-02 | def — redefinition                 | 🟡 NEEDS | road-sign — "painting over an old sign with new paint"             |
| G3-03 | let — local binding ⭐             | 🟡 NEEDS | temporary-pouch — "putting 3 in a pouch labeled x for one stretch" |
| G3-04 | let — multi-binding                | 🟡 NEEDS | temporary-pouch — "carrying several pouches at once"               |
| G3-05 | let — shadowing outer def          | 🟡 NEEDS | temporary-pouch — "the pouch in your paw beats the road-sign"      |
| G3-06 | let — binding can reference prior  | 🟡 NEEDS | temporary-pouch — "the second pouch can peek into the first"       |
| G3-07 | fn — anonymous function            | 🟡 NEEDS | paw-step-recipe — "an unnamed paw-step routine"                    |
| G3-08 | fn — multi-arg                     | 🟡 NEEDS | paw-step-recipe — "a recipe with several ingredients"              |
| G3-09 | defn — shorthand                   | 🟡 NEEDS | paw-step-recipe — "named recipe posted on the road"                |
| G3-10 | anonymous shorthand #()            | 🟡 NEEDS | paw-step-recipe — "scratched-out shorthand for a one-time recipe"  |
| G3-11 | Substitution rule                  | 🟡 NEEDS | temporary-pouch — "wherever you see the name, paste the value"     |
| G3-12 | Scope vs namespace                 | 🟡 NEEDS | road-sign — "house rules vs road signs; pouch wins indoors"        |
| G3-13 | fn body returns last form          | 🟡 NEEDS | paw-step-recipe — "the last bite is what you remember"             |
| G3-14 | do form                            | 🟡 NEEDS | scribe-shorthand — "doing several things in sequence; last result counts" |
| G3-15 | Side-effects in body               | 🟡 NEEDS | paw-step-recipe — "calling out, then handing back the value"       |
| G3-16 | Name collision: namespace vs let   | 🟡 NEEDS | temporary-pouch — "your pouch overrides what the road says"        |
| G3-17 | Naming conventions (kebab-case)    | 🟡 NEEDS | road-sign — "naming convention; readable signs"                    |
| G3-18 | When to name vs inline             | 🟡 NEEDS | temporary-pouch — "name what you'll reuse; inline what's once"     |

### Grade 4 — collections

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G4-01 | Vector literal                     | 🟡 NEEDS | basket-and-label — "a row of pebbles in order"                    |
| G4-02 | nth — vector access                | 🟡 NEEDS | basket-and-label — "the Nth pebble in the row"                    |
| G4-03 | conj — append to vector            | 🟡 NEEDS | basket-and-label — "drop another pebble at the end of the row"     |
| G4-04 | List literal                       | 🟡 NEEDS | basket-and-label — "a procession of animals"                       |
| G4-05 | cons — prepend to seq              | 🟡 NEEDS | basket-and-label — "a new leader at the head of the procession"    |
| G4-06 | Map literal                        | 🟡 NEEDS | basket-and-label — "labeled pouches; tag → thing"                  |
| G4-07 | get — map lookup                   | 🟡 NEEDS | basket-and-label — "fetch the thing under the label"               |
| G4-08 | assoc — map update                 | 🟡 NEEDS | basket-and-label — "pin a new note onto the basket"                |
| G4-09 | dissoc — map remove key            | 🟡 NEEDS | basket-and-label — "unpin a note"                                  |
| G4-10 | keys and vals                      | 🟡 NEEDS | basket-and-label — "the labels alone vs the things alone"          |
| G4-11 | Set literal                        | 🟡 NEEDS | basket-and-label — "a basket where each kind appears once"         |
| G4-12 | Set membership                     | 🟡 NEEDS | basket-and-label — "is this nut in the basket?"                    |
| G4-13 | count — universal                  | 🟡 NEEDS | the-tally-walk — "tally by walking the row"                        |
| G4-14 | empty?                             | 🟡 NEEDS | basket-and-label — "is the basket empty?"                          |
| G4-15 | first, rest, last                  | 🟡 NEEDS | basket-and-label — "the head / tail / final of the procession"     |
| G4-16 | into and conj on collections       | 🟡 NEEDS | sieve-and-pour — "pour one basket into another"                    |
| G4-17 | Immutability — assoc returns new   | 🟡 NEEDS | basket-and-label — "the original basket is untouched; you got a new one" |
| G4-18 | Equality of vectors and lists      | 🟡 NEEDS | basket-and-label — "two arrangements with the same animals in order" |
| G4-19 | range and seq                      | 🟡 NEEDS | basket-and-label — "a numbered path"                                |
| G4-20 | Collection vs sequence             | 🟡 NEEDS | basket-and-label — "the basket vs the line of animals walking out of it" |

### Grade 5 — control flow + HOF

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G5-01 | if                                 | 🟡 NEEDS | fork-in-the-path — "left fork or right; one path taken"           |
| G5-02 | if as expression                   | 🟡 NEEDS | fork-in-the-path — "the chosen branch's value carries forward"     |
| G5-03 | when                               | 🟡 NEEDS | fork-in-the-path — "a one-armed fork; nil down the un-taken side"  |
| G5-04 | cond                               | 🟡 NEEDS | fork-in-the-path — "a multi-fork crossroads"                       |
| G5-05 | cond — :else                       | 🟡 NEEDS | fork-in-the-path — "the catchall path"                             |
| G5-06 | case                               | 🟡 NEEDS | fork-in-the-path — "matching by token at a sorting-stone"          |
| G5-07 | and / or as control flow           | 🟡 NEEDS | gates-on-the-trail — "gates pass the value through, or stop"       |
| G5-08 | not                                | 🟡 NEEDS | gates-on-the-trail — "the opposite-of-paw"                         |
| G5-09 | fn as value                        | 🟡 NEEDS | paw-step-recipe — "passing the recipe itself, not its result"      |
| G5-10 | map                                | 🟡 NEEDS | sieve-and-pour — "treat each animal in line the same way"          |
| G5-11 | filter                             | 🟡 NEEDS | sieve-and-pour — "sieve the basket; keep only the matching ones"   |
| G5-12 | reduce ⭐                          | 🟡 NEEDS | the-tally-walk — "walk the row carrying a tally; combine each into the tally" |
| G5-13 | reduce with init                   | 🟡 NEEDS | the-tally-walk — "start with a partial pile, keep walking"         |
| G5-14 | apply                              | 🟡 NEEDS | paw-step-recipe — "spread the basket as the recipe's ingredients"  |
| G5-15 | comp                               | 🟡 NEEDS | paw-step-recipe — "chain of paw-steps; output of one feeds the next" |
| G5-16 | partial                            | 🟡 NEEDS | paw-step-recipe — "half-loaded recipe waiting for the last ingredient" |
| G5-17 | juxt                               | 🟡 NEEDS | paw-step-recipe — "ask several questions at once; collect each answer" |
| G5-18 | some                               | 🟡 NEEDS | sieve-and-pour — "is there at least one X in the basket?"          |
| G5-19 | every?                             | 🟡 NEEDS | sieve-and-pour — "do they ALL X?"                                  |
| G5-20 | take and drop                      | 🟡 NEEDS | sieve-and-pour — "first three / leave first three"                 |
| G5-21 | distinct and sort                  | 🟡 NEEDS | sieve-and-pour — "deduped / sorted by tortoise-pace"               |
| G5-22 | recur — first taste                | 🟡 NEEDS | circuit-around-the-meadow — "loop back without growing the trail"  |

### Grade 6 — namespaces + tooling-adjacent

| ID    | Title                              | Tag         | Family / metaphor                                                  |
| ----- | ---------------------------------- | ----------- | ------------------------------------------------------------------ |
| G6-01 | Namespace as file                  | 🟡 NEEDS    | road-sign — "each scroll is a namespace"                           |
| G6-02 | ns form                            | 🟡 NEEDS    | road-sign — "the title page of the scroll"                         |
| G6-03 | require                            | 🟡 NEEDS    | road-sign — "borrowing a scroll from the library"                  |
| G6-04 | refer and use                      | 🟡 NEEDS    | road-sign — "borrowing AND keeping the names handy"                |
| G6-05 | Fully qualified names              | 🟡 NEEDS    | road-sign — "library/section/title path"                           |
| G6-06 | Private defs                       | 🟡 NEEDS    | road-sign — "a sealed back-room of the scroll"                     |
| G6-07 | Public vs private API              | 🟡 NEEDS    | road-sign — "shop window vs back room"                             |
| G6-08 | Circular dependencies              | 🟡 NEEDS    | road-sign — "two scrolls referring to each other"                  |
| G6-09 | Loading order                      | 🟡 NEEDS    | road-sign — "scrolls read in order; can't peek ahead"              |
| G6-10 | Leiningen and deps.edn             | 🌐 ABSTRACT | tooling — keep generic narrative                                   |
| G6-11 | Classpath                          | 🌐 ABSTRACT | tooling — keep generic narrative                                   |
| G6-12 | Multiple files in one project      | 🟡 NEEDS    | road-sign — "many scrolls in one library"                          |
| G6-13 | Aliasing conventions               | 🟡 NEEDS    | road-sign — "shorter name for the borrowed scroll"                 |
| G6-14 | Import for host classes            | 🟡 NEEDS    | tool-from-another-toolshed — "borrowing a tool from another toolshed" |
| G6-15 | Namespace meta                     | 🟡 NEEDS    | scroll-and-quill — "marginalia on the title page"                  |
| G6-16 | Cleaning up requires               | 🟡 NEEDS    | road-sign — "returning scrolls you don't read anymore"             |

### Grade 7 — errors + IO

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G7-01 | throw                              | 🟡 NEEDS | safety-net — "raising the alarm; the runner stops"                 |
| G7-02 | try / catch                        | 🟡 NEEDS | safety-net — "a net beneath the leap"                              |
| G7-03 | try / finally                      | 🟡 NEEDS | safety-net — "always tidy after the run, error or not"             |
| G7-04 | ex-info                            | 🟡 NEEDS | safety-net — "the alarm carries a slip of detail in its pouch"     |
| G7-05 | nil punning                        | 🟡 NEEDS | safety-net — "the empty hollow gracefully behaves; no stumble"     |
| G7-06 | pre and post conditions            | 🟡 NEEDS | safety-net — "checking the runner is fit before the race; checking the carry afterward" |
| G7-07 | assert                             | 🟡 NEEDS | safety-net — "a spot-check that this fact holds before continuing" |
| G7-08 | prn and pprint                     | 🟡 NEEDS | scroll-and-quill — "calling out neatly, in formatted strokes"      |
| G7-09 | tap>                               | 🟡 NEEDS | scroll-and-quill — "a quiet whisper to a listener; doesn't change the run" |
| G7-10 | doc and source                     | 🟡 NEEDS | scroll-and-quill — "the recipe's instruction card"                 |
| G7-11 | Reading stack traces               | 🟡 NEEDS | safety-net — "tracking back the runner's path after a stumble"     |
| G7-12 | slurp and spit                     | 🟡 NEEDS | scroll-and-quill — "drinking from a scroll / writing onto one"     |
| G7-13 | line-seq                           | 🟡 NEEDS | scroll-and-quill — "reading the scroll line by line"               |
| G7-14 | with-open                          | 🟡 NEEDS | scroll-and-quill — "open the scroll, close it after"               |
| G7-15 | *in* and *out*                     | 🟡 NEEDS | scroll-and-quill — "the meadow's loud voice / quiet whisper"       |
| G7-16 | edn read                           | 🟡 NEEDS | scroll-and-quill — "reading what a scroll says, restoring it as data" |
| G7-17 | JSON roundtrip                     | 🟡 NEEDS | scroll-and-quill — "writing the data, reading it back unchanged"   |
| G7-18 | Shell command                      | 🟡 NEEDS | tool-from-another-toolshed — "calling for a runner from outside the meadow" |

### Grade 8 — polymorphism

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G8-01 | Why polymorphism                   | 🟡 NEEDS | guild-of-runners — "different species, same call (run!)"           |
| G8-02 | deftype introduction               | 🟡 NEEDS | carrying-case — "a custom-made carrying-case with named compartments" |
| G8-03 | defrecord introduction             | 🟡 NEEDS | carrying-case — "a labeled carrying-case (acts like a map too)"    |
| G8-04 | Protocol definition                | 🟡 NEEDS | guild-of-runners — "founding a guild — anyone may join later"      |
| G8-05 | Protocol extension                 | 🟡 NEEDS | guild-of-runners — "an animal signs the guild book and gets the call" |
| G8-06 | Protocol method dispatch           | 🟡 NEEDS | guild-of-runners — "the same call dispatches to species-specific behavior" |
| G8-07 | Record implementing protocol       | 🟡 NEEDS | guild-of-runners — "a labeled case that's also a guild member"     |
| G8-08 | Multimethod defmulti               | 🟡 NEEDS | sorting-table — "a sorting-table; route by what's stamped on the runner" |
| G8-09 | Multimethod defmethod              | 🟡 NEEDS | sorting-table — "the table's branches: hare here, tortoise there"  |
| G8-10 | Multimethod vs protocol            | 🟡 NEEDS | sorting-table — "tables (open dispatch) vs guilds (open extension)" |
| G8-11 | Protocol vs Java interface         | 🟡 NEEDS | guild-of-runners — "Clojure-side guild vs host-side ledger"        |
| G8-12 | extend-type on built-in types      | 🟡 NEEDS | sorting-table — "teaching an existing animal a new call"           |
| G8-13 | this-style vs fn-style             | 🟡 NEEDS | guild-of-runners — "the carrying-case can introspect itself"       |
| G8-14 | Protocols don't inherit            | 🟡 NEEDS | guild-of-runners — "joining one guild doesn't auto-join another"   |
| G8-15 | derive and isa? — multimethod hierarchy | 🟡 NEEDS | sorting-table — "a hierarchy: hare is-a runner is-a animal"       |
| G8-16 | Abstract design with protocols     | 🟡 NEEDS | guild-of-runners — "many runners, one race-call"                   |

### Grade 9 — concurrency

| ID    | Title                              | Tag      | Family / metaphor                                                  |
| ----- | ---------------------------------- | -------- | ------------------------------------------------------------------ |
| G9-01 | Immutability as default — review   | 🟡 NEEDS | basket-and-label — "the basket on the road can't be changed"       |
| G9-02 | Why state at all                   | 🟡 NEEDS | shared-notebook-on-a-stump — "a shared scoreboard, updated together" |
| G9-03 | Atom introduction ⭐               | 🟡 NEEDS | shared-notebook-on-a-stump — "a notebook on a stump that any animal can update atomically" |
| G9-04 | Atom CAS semantics                 | 🟡 NEEDS | shared-notebook-on-a-stump — "I'll only write if the value's still 0" |
| G9-05 | Watch on atom                      | 🟡 NEEDS | shared-notebook-on-a-stump — "a listener who logs each update"     |
| G9-06 | Validator on atom                  | 🟡 NEEDS | shared-notebook-on-a-stump — "a referee who only allows valid updates" |
| G9-07 | Ref introduction                   | 🟡 NEEDS | shared-notebook-on-a-stump — "a notebook used in a coordinated transaction" |
| G9-08 | dosync and alter                   | 🟡 NEEDS | shared-notebook-on-a-stump — "the bookkeeping ritual: all updates land together or none do" |
| G9-09 | Ref vs atom                        | 🟡 NEEDS | shared-notebook-on-a-stump — "team-bookkeeping vs single-counter"  |
| G9-10 | Agent introduction                 | 🟡 NEEDS | runner-sent-ahead — "a messenger you send updates to"              |
| G9-11 | send and send-off                  | 🟡 NEEDS | runner-sent-ahead — "delivering the message in the right way"      |
| G9-12 | await — synchronizing on agents    | 🟡 NEEDS | runner-sent-ahead — "wait for the messenger to finish"             |
| G9-13 | future introduction                | 🟡 NEEDS | runner-sent-ahead — "a runner sent down the road; come back for the result" |
| G9-14 | deref @ shorthand                  | 🟡 NEEDS | shared-notebook-on-a-stump — "looking inside the notebook"         |
| G9-15 | promise — deliver and deref        | 🟡 NEEDS | runner-sent-ahead — "a sealed scroll; opens when delivered"        |
| G9-16 | volatile — when STM is too heavy   | 🟡 NEEDS | shared-notebook-on-a-stump — "a quick-and-dirty notebook (no transaction safety)" |
| G9-17 | binding — thread-local             | 🟡 NEEDS | shared-notebook-on-a-stump — "a personal handbook, only this runner sees it" |
| G9-18 | locking — last resort              | 🟡 NEEDS | shared-notebook-on-a-stump — "a fence around the notebook; one writer at a time" |

### Grade 10 — macros

| ID     | Title                                | Tag         | Family / metaphor                                                  |
| ------ | ------------------------------------ | ----------- | ------------------------------------------------------------------ |
| G10-01 | quote, unquote, unquote-splice       | 🟡 NEEDS    | chalk-marks-vs-acorns — "chalk-mark a list to label it instead of cooking it" |
| G10-02 | syntax-quote                         | 🟡 NEEDS    | chalk-marks-vs-acorns — "a labeled recipe-template with placeholders" |
| G10-03 | defmacro introduction                | 🟡 NEEDS    | rule-that-rewrites-recipes — "a rule that rewrites the recipe before the runtime sees it" |
| G10-04 | Macro expansion rule                 | 🟡 NEEDS    | rule-that-rewrites-recipes — "showing the rewritten recipe step"   |
| G10-05 | macroexpand                          | 🟡 NEEDS    | rule-that-rewrites-recipes — "fully expanded recipe"               |
| G10-06 | when and when-not as macros          | 🟡 NEEDS    | rule-that-rewrites-recipes — "the trail-shorthand expanded into the full fork" |
| G10-07 | Threading macros revisited           | 🟡 NEEDS    | paw-step-recipe — "passing the value through a relay of paws"      |
| G10-08 | Macro vs fn                          | 🟡 NEEDS    | rule-that-rewrites-recipes — "macros rewrite forms; fns evaluate args" |
| G10-09 | Hygiene and gensym                   | 🟡 NEEDS    | rule-that-rewrites-recipes — "use a one-off scratch-name to avoid collision" |
| G10-10 | Anaphoric macros are confusing       | 🟡 NEEDS    | rule-that-rewrites-recipes — "binding implicit names — confusing"  |
| G10-11 | Reader macros overview               | 🟡 NEEDS    | scribe-shorthand — "the scribe's shorthand for reading"            |
| G10-12 | Tagged literals                      | 🟡 NEEDS    | scribe-shorthand — "marked literals like #inst"                    |
| G10-13 | Data readers and EDN extension       | 🟡 NEEDS    | scribe-shorthand — "custom shorthand for reading"                  |
| G10-14 | eval (the function)                  | 🟡 NEEDS    | rule-that-rewrites-recipes — "asking the REPL to evaluate this form right now" |
| G10-15 | When not to write a macro            | 🟡 NEEDS    | rule-that-rewrites-recipes — "if a function suffices, don't"       |
| G10-16 | Macro pattern library                | 🟡 NEEDS    | rule-that-rewrites-recipes — "a stash of useful recipe-rewriters"  |

### Grade 11 — host interop (mostly abstract by nature)

| ID     | Title                                            | Tag         | Family / metaphor                                                  |
| ------ | ------------------------------------------------ | ----------- | ------------------------------------------------------------------ |
| G11-01 | JVM vs CLR vs JS vs Python (host overview)       | 🌐 ABSTRACT | tooling/host overview                                              |
| G11-02 | Method call syntax                               | 🟡 NEEDS    | tool-from-another-toolshed — "calling a foreign tool's hand-method" |
| G11-03 | Static method call                               | 🟡 NEEDS    | tool-from-another-toolshed — "a tool's standard-issue function"    |
| G11-04 | Field access                                     | 🟡 NEEDS    | tool-from-another-toolshed — "reading a label off the foreign tool" |
| G11-05 | Import form                                      | 🌐 ABSTRACT | tooling                                                             |
| G11-06 | new and dot-construct                            | 🟡 NEEDS    | tool-from-another-toolshed — "constructing a foreign tool from raw materials" |
| G11-07 | Arrays                                           | 🟡 NEEDS    | tool-from-another-toolshed — "the host's primitive row-of-things"  |
| G11-08 | Type hints                                       | 🟡 NEEDS    | tool-from-another-toolshed — "telling the host what kind of tool"  |
| G11-09 | Checked vs unchecked math                        | 🟡 NEEDS    | acorn-arithmetic — "two ways to count: with overflow check or without" |
| G11-10 | ClojureScript overview                           | 🌐 ABSTRACT | tooling                                                             |
| G11-11 | cljs / JavaScript interop                        | 🌐 ABSTRACT | tooling                                                             |
| G11-12 | Basilisp overview (Python host)                  | 🌐 ABSTRACT | tooling                                                             |
| G11-13 | Cross-platform .cljc and reader-conditionals     | 🌐 ABSTRACT | tooling                                                             |
| G11-14 | Debugging host leaks                             | 🟡 NEEDS    | tool-from-another-toolshed — "host stack traces leak through; learn to read them" |

### Grade 12 — real-world (mostly tooling)

| ID     | Title                                  | Tag         | Family / metaphor                                              |
| ------ | -------------------------------------- | ----------- | -------------------------------------------------------------- |
| G12-01 | Transducers introduction               | 🟡 NEEDS    | sieve-and-pour — "a recipe-shaped sieve, reusable"            |
| G12-02 | Transducer composition                 | 🟡 NEEDS    | sieve-and-pour — "stacked sieves; output of one feeds the next" |
| G12-03 | into with a transducer (xform)         | 🟡 NEEDS    | sieve-and-pour — "pour through the sieve into a new basket"   |
| G12-04 | core.async introduction                | 🌐 ABSTRACT | tooling                                                         |
| G12-05 | Channels and pipelines                 | 🌐 ABSTRACT | tooling (could fit "messengers and routes" loosely)            |
| G12-06 | clojure.spec                           | 🌐 ABSTRACT | tooling                                                         |
| G12-07 | Spec generators                        | 🌐 ABSTRACT | tooling                                                         |
| G12-08 | clojure.test                           | 🌐 ABSTRACT | tooling                                                         |
| G12-09 | Test fixtures                          | 🌐 ABSTRACT | tooling                                                         |
| G12-10 | Property-based testing                 | 🌐 ABSTRACT | tooling                                                         |
| G12-11 | Leiningen project.clj                  | 🌐 ABSTRACT | tooling                                                         |
| G12-12 | deps.edn projects                      | 🌐 ABSTRACT | tooling                                                         |
| G12-13 | Aliases and tools                      | 🌐 ABSTRACT | tooling                                                         |
| G12-14 | Pedestal / Ring (web stack brief)      | 🌐 ABSTRACT | tooling                                                         |
| G12-15 | Datomic / XTDB (datalog db brief)      | 🌐 ABSTRACT | tooling                                                         |
| G12-16 | Reagent (cljs UI brief)                | 🌐 ABSTRACT | tooling                                                         |
| G12-17 | Library design patterns                | 🌐 ABSTRACT | meta                                                             |
| G12-18 | Clojure style guide                    | 🌐 ABSTRACT | meta                                                             |

---

## Summary counts

| Tag         | Count  | Share |
| ----------- | ------ | ----- |
| 🟢 HAS       | 6      | 3%    |
| 🟡 NEEDS     | 174    | 81%   |
| 🌐 ABSTRACT  | 36     | 17%   |
| **TOTAL**    | **216** | 100% |

The 174 NEEDS subjects fall into ~21 metaphor families. Implementing
metaphors at the **family level** (not per-subject) means we'd need
~21 new subplot template-pools, each with 4-6 templates. Subjects pick
the appropriate family pool the way grade_2-12 currently pick
`_GOAL_SUBPLOTS` — by import. Estimated effort: 2-3 days of authorship
work, then re-fan-out per grade to retag each subject's `subplots=`
field.

## What I'd recommend

1. Author the **5 highest-leverage metaphor families first** —
   `temporary-pouch`, `paw-step-recipe`, `basket-and-label`,
   `shared-notebook-on-a-stump`, `sieve-and-pour`. These cover roughly
   100 of the 174 NEEDS subjects and are the most pedagogically
   load-bearing (let, fn, collections, atoms, HOFs).
2. Audit the showcase doc against the family templates to verify the
   metaphor lands.
3. Then author the remaining ~16 families.
4. Tooling/abstract subjects (36) keep current generic narrative;
   that's honest, not contrived.

The atom subjects (G1-01..08) currently use form-display narrative
which is a reasonable "show, don't tell" approach. Optional later: add
flavor — "a stamped tag", "an empty hollow" — but the form-display
mechanism is already pedagogically correct.
