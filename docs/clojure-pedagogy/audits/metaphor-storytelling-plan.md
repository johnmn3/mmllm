# Metaphor storytelling plan — round 3

## What the user caught

Three concrete examples from `metaphor-demo-tortoise-hare.md`:

> _RECIPE#5 for G3-09 (defn — named function)_
> "Pip the hare insisted they could just shout the answer rather than
> bother writing a recipe. Slowpoke the tortoise only smiled and reached
> for a fresh card. To define a function dbl that doubles its argument,
> then call it with 5, he composed the function definition and call,
> submitted the form…"

User: *"What does recipe have to do with this story? What answer? Was a
question asked? What is this card slowpoke pulled out? Is it an answer?
Is it a recipe? What does doubling have to do with this situation? …
For a named function, you'd want some metaphor like one character
telling another character to do some procedure, then calling that
procedure a name, and then telling the character to do that by name…"*

> _RECIPE#1 for G3-09 (defn)_
> "Mossback the tortoise kept a small stack of recipe-cards by the road,
> each one a paw-step routine. 'Recipes in Clojure are like these cards,'
> he said: 'the ingredients go at the head, the steps in order, and the
> last step is what gets served.'"

User: *"This one has more narrative context. But here, if we're doubling,
and we're talking about ingredients, then what we would say is that we're
doubling the salt ingredient because we have double the number of folks
eating at the table. Then we'd build a double function for the salt or
ingredients or whatever."*

> _BASKET#1 for G4-08 (assoc — map update)_
> "Shelly the tortoise pointed to a small basket on the path. 'Whatever
> I want to do with what's inside,' she said, 'I read from the basket,
> work the change, and the basket itself stays as it was — what I get
> back is a fresh arrangement.' To associate the key :b with value 2
> onto a map binding :a to 1, she composed the assoc operation…"

User: *"You don't read from a basket. 'Whatever I want to do with what's
inside' is a hypothetical, not related to any particular story. We need
to have a need to affect something inside. … If the basket has
compartments that are named — open area, pouch area 1 and 2, pockets 1
and 2 — you might associate certain foods into certain compartments. One
character might tell another to `assoc` the apple into the pouch area.
Then the code question and answer would reflect those semantics."*

## The failure mode in one sentence

**The metaphor is named but doesn't drive the action.** The Tortoise
becomes a nature documentary narrator giving a definition; the operation
isn't *needed* by anyone in the story. Every record has the same shape:

1. Generic opener (boilerplate Hare/Tortoise pre-roll)
2. Tortoise philosophically introduces the metaphor
3. Tortoise composes `{concept_phrase}` and submits
4. REPL returns

What's missing: **concrete need, narrative tension, element mapping,
resolution that uses the metaphor's verbs.**

## Where this happens

The pattern is across all 22 family pools, on every record. After my
type-neutrality sweep removed false claims, the templates became
honest but empty. Sample evidence (one record per family,
`metaphor-demo-tortoise-hare.md`):

| Family       | Subject     | Has a story? | Has a concrete need? | Maps elements? |
| ------------ | ----------- | ------------ | -------------------- | -------------- |
| pouch        | G3-03 let   | ✗            | ✗                    | ✗              |
| recipe       | G3-09 defn  | ✗            | ✗                    | ✗              |
| basket       | G4-08 assoc | ✗            | ✗                    | ✗              |
| sieve        | G5-10 map   | ✗            | ✗                    | ✗              |
| notebook     | G9-03 atom  | ✗            | ✗                    | ✗              |
| acorn        | G2-04 min   | ✗            | ✗                    | ✗              |
| gate         | G2-13 and   | ✗            | ✗                    | ✗              |
| fork         | G5-04 cond  | ✗            | ✗                    | ✗              |
| roadsign     | G6-03 require | ✗          | ✗                    | ✗              |
| safetynet    | G7-02 try   | ✗            | ✗                    | ✗              |
| scroll       | G7-12 slurp | ✗            | ✗                    | ✗              |
| guild        | G8-04 protocol | ✗         | ✗                    | ✗              |
| sortingtable | G8-08 multi | ✗            | ✗                    | ✗              |
| carryingcase | G8-03 record | ✗           | ✗                    | ✗              |
| toolshed     | G11-02 method | ✗          | ✗                    | ✗              |
| runnerahead  | G9-13 future | ✗           | ✗                    | ✗              |
| rewriterule  | G10-03 macro | ✗           | ✗                    | ✗              |
| scribe       | G1-12 parens | ✗           | ✗                    | ✗              |
| chalkmark    | G1-09 symbol | ✗           | ✗                    | ✗              |
| tallywalk    | G5-12 reduce | ✗           | ✗                    | ✗              |
| beadstring   | G2-11 str    | ✗            | ✗                    | ✗              |
| circuit      | G5-22 recur  | ✗           | ✗                    | ✗              |

Every metaphor-rich subject (172 of 216) has this issue.

## What a grounded story looks like

A real story has five acts:

1. **SETUP** — a specific situation in the meadow that *exists*, not a
   hypothetical.
2. **NEED** — something concrete is needed; without the operation,
   something fails.
3. **MAPPING** — the metaphor's elements map directly to the
   operation's parts.
4. **ACTION** — the character composes and submits the form, using the
   metaphor's verbs.
5. **RESOLUTION** — the REPL returns; the value satisfies the need.

### Worked examples

#### G3-09 (defn — named function)

> The kitchen was crowded. Twice as many forest animals had arrived
> for dinner as Mossback had planned for, and every recipe in the
> stack now needed twice the salt. **[setup + need]**
>
> "We can't keep walking back to the cellar," Mossback said. "We need
> a routine — a recipe-card we can call by name when any cook needs
> twice a quantity. We'll write the steps once, give the card a name,
> and any cook in the kitchen can shout the name and have the doubling
> done." **[mapping: defn = recipe-card + name]**
>
> Mossback wrote out a card titled `dbl`: "given any quantity, return
> twice that quantity." Then `dbl` was called: tonight's first reach
> was for 5 pinches of salt. **[action]**
>
> The REPL ran the named recipe with 5 in hand, and 10 came back —
> exactly what the doubled crowd would need. **[resolution]**

The form `(do (defn dbl [x] (* x 2)) (dbl 5))` → 10 *is* the story:
defining the recipe-card with a name, then calling it by name.

#### G4-08 (assoc — map update)

> Mossback's foraging-basket had compartments stitched into its sides.
> The open area at the top was for what she'd already gathered; pouch
> areas and pockets carried particular kinds of finds. **[setup]**
>
> She'd just placed an apple in the open area. Pip arrived with a pear,
> bouncing from the orchard. "Where does the pear go?" he asked.
> "Pouch area B," Mossback said. **[need: pear must end up in a named
> compartment]**
>
> "I'll associate the pear with pouch B," she explained. "The basket
> stays the same shape — open area, pouch A, pouch B — but now pouch B
> holds the pear." **[mapping: assoc = associate value with named
> compartment]**
>
> She composed the form, submitted it, and the REPL handed back the
> basket with both fruits in their compartments — apple in the open
> area, pear in pouch B, exactly where the foraging called for. **[action
> + resolution]**

The form `(assoc {:a 1} :b 2)` → `{:a 1, :b 2}` *is* the story: the
basket originally has the apple in `:a`, and the pear is associated
with `:b`.

#### G9-03 (atom — coordinated mutable state)

> The forest creatures kept a tally of the day's berry-count on a
> notebook open on the tree stump in the middle of the meadow. Anyone
> coming back from foraging walked up, looked at the page to see the
> running total, and added their own count. **[setup]**
>
> Today's tally was zero — no one had foraged yet. The Tortoise's first
> handful was a single berry. **[need: increment the tally by the
> Tortoise's contribution]**
>
> "I'll swap the page atomically," she said. "Read what's there, add
> mine, write back — all in one motion, so if Pip arrives at the same
> moment, neither of us writes over the other." **[mapping: atom =
> notebook on stump; swap! = atomic read-modify-write]**
>
> She composed the form, submitted it, dereferenced the page, and the
> REPL handed back 1 — the new running total, exactly what the meadow
> would expect. **[action + resolution]**

The form `(do (def a (atom 0)) (swap! a inc) @a)` → 1 *is* the story:
the page starts at 0, increments by 1, the Tortoise reads the new value.

### What changed in these stories

- The metaphor is **introduced as a fact of the world**, not as a
  philosophical aside. The basket has compartments because the
  foraging needed compartments. The notebook is on the stump because
  the meadow needs a shared tally.
- There's a **specific need** that the operation satisfies. Without
  the operation, dinner doesn't get its salt; the pear has no place;
  the tally doesn't update.
- The metaphor's elements **map one-to-one** with the operation's
  parts:
  - defn → recipe-card-with-a-name
  - assoc → associate-with-named-compartment
  - swap! → atomic-read-modify-write-on-shared-notebook
- The **form is the story written in Clojure**, not a footnote
  beneath a generic philosophical opener.

## Three architectural paths

### Path A — Richer goal_text only

Rewrite each example's `goal_text` into a one-sentence narrative
backstory:

```python
# Before:
goal="define a function dbl that doubles its argument, then call it with 5"

# After:
goal="give a 'doubling' recipe a name so any cook can call it; with twice the guests, double tonight's 5 pinches of salt"
```

**Pros:** small change, no template authoring needed.
**Cons:** templates still don't *structure* the narrative; the goal_text
gets dropped into a generic philosophical-Tortoise frame, which doesn't
build the setup → need → mapping arc.

### Path B — Per-subject story templates (recommended)

Author 4-6 templates per subject (or small subject-group) that tell
grounded 5-act stories. Templates live in per-subject pools:

```
tortoise_hare/_metaphor_pools/
    __init__.py
    family_pools.py     # generic family-level (current pools, retained
                        #   as fallback for subjects without per-subject
                        #   templates)
    let_subplots.py     # G3-03..06 + G3-11/16/18 — temporary-pouch
                        #   stories
    fn_subplots.py      # G3-07..10 + G3-13/15 — recipe-card stories
    assoc_subplots.py   # G4-07/08/09 — basket-with-compartment stories
    atom_subplots.py    # G9-02..09 — shared-notebook stories
    ...etc
```

Each subject (or subject-group) imports its own pool. Templates within
each pool tell *concrete stories* parameterized by goal_text and
example values.

**Pros:** stories actually land. The metaphor *drives* the operation.
The model trains on the structural mapping between fable elements and
operation parts.

**Cons:** ~700 templates to author across ~30-50 subject groups.
Heavy authoring lift. Cross-fable consistency is harder (each fable
needs parallel subject pools, not just family pools).

### Path C — Story-scaffold framework

Extend `SubjectExample` with narrative slots:

```python
@dataclass
class SubjectExample:
    form: str
    expected: object
    concept_phrase: str
    question_what: str
    goal_text: str = ""
    # NEW story slots:
    scenario: str = ""        # "The kitchen was crowded with twice the guests."
    need:     str = ""        # "Every recipe needed twice the salt."
    mapping:  str = ""        # "A named recipe any cook can call: dbl."
    resolution: str = ""      # "Tonight's 5 pinches doubled to 10."
    tags:     tuple[str, ...] = ()
```

Templates compose these slots in standard 5-act shape. Pools become
thin — they specify the metaphor's vocabulary and how slots are woven
in.

**Pros:** maximally flexible. Story material lives in the example,
where it belongs (the example's *meaning* is the story). Cross-fable
consistency is automatic — same scenario, fable-specific characters.

**Cons:** framework change. ~500 examples need scenario/need/mapping
authoring (currently they have goal_text only). Templates need
rewriting around the new slots.

## Recommendation

**Phase 1 (this commit cycle):**
- Path A as a quick win for the 12 highest-leverage subjects:
  G3-03 let, G3-09 defn, G4-08 assoc, G4-07 get, G5-10 map, G5-11
  filter, G5-12 reduce, G9-03 atom, G9-08 dosync, G7-02 try, G5-01
  if, G8-04 protocol. Rich goal_texts that *describe* a need.
- Templates updated in those subjects' pools to **stage** the goal_text
  as a concrete situation, not an aside.

**Phase 2 (next cycle):**
- Migrate to Path C: extend `SubjectExample` with `scenario` / `need` /
  `mapping` / `resolution` slots.
- Author per-subject story scaffolds for the highest-value 30 subjects.
- Keep family pools as fallback for the remaining subjects.

**Phase 3 (future):**
- Roll out the scaffold across all 172 metaphor-rich subjects.
- Cross-fable: parallel scaffolds for goose-eggs and ant-grasshopper
  (same need-structure, different fable imagery).

The atom subjects (G1-01..08) and abstract subjects (~36) keep their
current setup — atoms are intentionally form-display, abstract
subjects are intentionally generic.

## Worked Phase-1 inventory

For the 12 phase-1 subjects, here's the story shape each needs:

| Subject | Scenario | Need | Mapping |
| ------- | -------- | ---- | ------- |
| G3-03 let | a one-stretch-of-road carry | bind a pebble to the pouch for that stretch | pouch = local binding |
| G3-09 defn | kitchen with double the guests | name the doubling recipe so any cook can call it | recipe-card-with-name = defn |
| G4-07 get | foraging basket with named compartments | reach into a specific compartment | named compartment = map key |
| G4-08 assoc | basket with compartments, new fruit arrives | place fruit in a named compartment | assoc = associate value with key |
| G5-10 map | row of acorns, each needs the same trim | apply the trim recipe to each acorn | sieve-with-recipe = map |
| G5-11 filter | mixed basket, only the ripe ones go to market | keep only the matching ones | sieve-as-predicate = filter |
| G5-12 reduce | row of acorns, total weight needed | walk the row carrying a running tally | tally-walk = reduce |
| G9-03 atom | meadow keeping a shared berry tally | one foragers's count adds atomically | notebook-on-stump = atom |
| G9-08 dosync | hare and tortoise both count, both must land or neither | coordinated update of two notebooks | dosync = transaction over refs |
| G7-02 try | high-jump where the runner can fall | catch the fall, continue the run | net = catch clause |
| G5-01 if | trail forks at the orchard | take the orchard arm if hungry, else the meadow arm | fork = if/then/else |
| G8-04 protocol | runners' guild any species may join | found the guild, define what members must do | guild = defprotocol |

## Decision needed

Which path?

- **A:** quickest, ~1 commit, modest improvement in 12 subjects.
- **B:** medium, ~3-5 commits, full grounding for ~30 subjects.
- **C:** biggest lift, ~6-10 commits, full grounding for all 172 +
  framework that scales to other fables.

My recommendation: **start with A as a working prototype on one or two
subjects to validate the story-shape approach lands, then commit to C
as the architectural answer.**

Once we have one subject (say G4-08 assoc) working end-to-end with a
grounded story, the template for the rest is clear and the
implementation pace is much faster.
