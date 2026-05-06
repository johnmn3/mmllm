# Metaphor imagery mapping — dog-shadow

**Fable**: A Dog crosses a stream carrying a bone. Seeing his own
reflection, he thinks it's a bigger bone, snaps at the image — and
drops the real bone. Moral: greed loses what you already have.

**Characters**:
- `{hound}` / `{hound_phrase}` — the wise, patient dog (tortoise-analog)
- `{dog}` / `{dog_phrase}` — the hasty, greedy dog (hare-analog)
- Cast: Rex (m), Bell (f), Patch (n) — two picked per record

**World setting**: Streamside / riverbank / pond / forest path near water.

**Core props**: bone in mouth, stream, reflection, bank, flat stones,
hollow-log cache, scratch-marks, gap in bark/log, pack signals.

**Moral tension**: Real bone (what you have) vs. reflected image
(what you think you see). Careful evaluation (hound) vs. hasty
grabbing (dog).

---

## Family imagery table

| Family | Tortoise-hare imagery | Dog-shadow imagery |
|--------|----------------------|-------------------|
| **pouch** (let-binding) | small leather pouch tied at hip | the dog's **mouth**: the bone is carried in the mouth for the length of the crossing; the moment the mouth opens for the shadow the bone drops |
| **recipe** (fn/defn/comp/partial) | paw-step recipe-card on the road | a **nose-trail**: a step-by-step sniffing path the dog follows to find a buried bone — each step is an instruction; the whole trail is the procedure |
| **basket** (collections/immutability) | foraging-basket with labeled compartments | **bone-cache in a hollow log**: a fixed store of bones with named slots; pulling one bone out doesn't disturb the rest; the cache stays as it was |
| **sieve** (map/filter/transducers) | sieve over an empty basket | **gap in a log over the stream**: only bones that fit the gap pass through; others are held back; the rule is the gap size |
| **notebook** (atom/ref/swap!/dosync) | notebook on a tree stump | **tally-scratch on a flat stone** by the stream's edge: the dog's running count of cached bones, scratched fresh each morning; can be updated; holds one value at a time |
| **acorn** (arithmetic / numbers) | counting acorns on the path | **counting bones** at the stream's edge; the dog lays them out on a flat stone and totals them |
| **gate** (and/or/not/falsey) | gates on the trail | **conditions at the stream crossing**: the dog can cross only if water is low AND footing is sound; any closed condition blocks the crossing |
| **fork** (if/cond/case/when) | fork at a crossroads | **fork in the path at the bank**: upstream or downstream — the dog picks a bank based on which condition holds; one path leads to the buried bone |
| **roadsign** (def/namespace/require) | posted road signs | **marker stone by the stream**: a flat stone the dog scratches a name into, marking where a bone is buried; read the scratch, find the bone |
| **safetynet** (try/catch/throw/assert) | safety net stretched across the trail | **log-bridge test before crossing**: the dog tests the log's hold before trusting its full weight; if the log breaks the dog retreats safely to the bank |
| **scroll** (IO/metadata/slurp/spit) | scrolls written and carried | **message-bone**: a bone with scratch-marks that carries a message from one bank to another; slurp = pick it up; spit = set it down at the destination |
| **guild** (protocols) | guild any species can join | **pack agreement**: all dogs in the pack honor the same signal for "bone found" or "danger ahead," regardless of which dog gives it |
| **toolshed** (host interop) | borrowing a tool from another toolshed | **kennel-master's tools**: the dog borrows something from the human's world (leash, bowl, collar) to complete a task that needs human-side equipment |
| **runnerahead** (agent/future/promise) | sending a runner down the road | **scout-dog**: the dog sends another pack member to check if the far bank is clear, then waits at the near bank for the signal before crossing |
| **rewriterule** (macros) | scribe with power to rewrite the recipe | **scent-mark that rewrites itself**: the dog alters a scratch-mark before the pack reads it, changing what path the pack will take |
| **scribe** (comments/whitespace/reader) | scribe's reading conventions | **scratch-marks on bark**: how to read the marks, what blank bark between marks means, how nested paw-prints are counted; the conventions the dog uses to parse what was left |
| **chalkmark** (quote/symbols) | chalk mark on bark vs. the acorn it names | **"bone" scratch vs. real bone**: the scratch that says "bone" is not the bone — just as the reflection in the stream looks like a bone but is only light on water |
| **sortingtable** (multimethods) | sorting-table that routes by tag | **sorting bones by origin**: the dog sorts bones into piles by type — fish, bird, deer — routing each to the correct pile by its shape and smell |
| **carryingcase** (deftype/defrecord) | labeled carrying-case with named slots | **labeled kennel-pouch**: a bag with named compartments — one for the bone's date, one for its size, one for its source — each field pre-declared |
| **tallywalk** (reduce/count) | walking the row carrying a running tally | **walking the bone-row**: the dog paces down a row of cached bones one by one, adding each bone's count to a running total |
| **beadstring** (str concat/subs) | strings as strings of beads | **string of scratch-marks on bark**: each scratch is one character; the dog reads them in order or combines two bark-strips into one longer message |
| **circuit** (recur/loop) | looping back without growing the trail | **pacing the bank**: the dog walks back and forth along the stream bank, making another pass each time the condition holds — without the path growing longer underfoot |

---

## Placeholder names

Dog-shadow templates use `{hound}`, `{dog}` and their pronoun variants:
- `{hound}`, `{hound_phrase}`, `{hound_he_she}`, `{hound_he_she_cap}`, `{hound_his_her}`, `{hound_him_her}`
- `{dog}`, `{dog_phrase}`, `{dog_he_she}`, `{dog_he_she_cap}`, `{dog_his_her}`, `{dog_him_her}`

The generator also provides `{hare}` / `{tortoise}` aliases (mapped to
dog/hound respectively) so that shared subplot templates inherited from
the tortoise-hare grade_1.py render without modification.

Emotion pool keys available: `{emo_proud}`, `{emo_patient}`, `{emo_tired}`,
`{emo_greedy}`, `{emo_content}`, `{emo_regretful}`.

Place key: `{place}` — produces "near the river bank", "by the pond",
"at the stream's edge", etc.

Story-scaffold keys (only for examples with `tags=("story",)`):
`{scenario}`, `{need}`, `{mapping}`, `{resolution}`.

---

## Notes on the fable's moral tension

The central image — real bone vs. reflected bone — maps directly to
**evaluation vs. appearance**: the dog who grabs the shadow loses the
real thing, just as a model who pattern-matches on surface form rather
than evaluating it may produce a wrong answer.

The **hound** (wise dog) always evaluates before acting: checks the log
before crossing, reads the scratch before following it, tests the gap
before trusting it.

The **dog** (greedy dog) grabs before checking: snatches the reflected
bone, crosses the log without testing, follows the first scratch it
sees without reading it carefully.

This maps onto the Clojure lesson: the runtime evaluates the form;
don't guess what it returns — submit the form and let the REPL decide.
