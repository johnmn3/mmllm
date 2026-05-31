# Crow-pitcher: imagery mapping to 22 metaphor families

**Fable moral:** cleverness in adversity — the crow cannot reach the
water directly, so she drops smooth stones one by one until the
water rises to where her beak can reach. Stone by stone, form by
form, the surface rises.

**Characters:**
- Korvus (m crow) — patient, methodical evaluator (tortoise-analog → `{clever}`)
- Caw (f crow) — impatient guesser who wants the answer without the
  form (hare-analog → `{hasty}`)
- Sable (n crow) — floats between roles; assigned by the generator

**Role assignment:** `{clever}` = primary (patient, stone-dropper);
`{hasty}` = secondary (impatient guesser). Roles are randomly
distributed across the three crows per record, so all three can
be either clever or hasty in different records.

**Locations:** garden, orchard, farm, market, village, meadow, road,
hilltop. No pond/river (proximity to water defuses the thirst tension).

**Core props:**
| Prop | Role |
|------|------|
| Tall clay pitcher | The evaluation vessel — the REPL |
| Smooth stones / pebbles | Forms dropped into the REPL one at a time |
| Water level rising | The answer becoming reachable |
| Crow's beak | The interface that reads the final value |
| Perch / pitcher rim | Where the crow thinks before submitting |
| Talon-scratch | How the crow writes / records |
| Wing-fold / wing-cache | Temporary holding during flight |

---

## Family-to-imagery mapping table

| Family | Crow-pitcher prop | Imagery |
|--------|-------------------|---------|
| `_POUCH_SUBPLOTS` | wing-cache | The clever crow tucks the intermediate value under one wing — held only for the stretch where the form needs it. After the drop, the wing opens again: the value existed only inside the form's reach. |
| `_RECIPE_SUBPLOTS` | talon-scratched drop-order | The clever crow scratches a step-by-step sequence into the pitcher's clay rim — a drop-order any crow can follow to raise the water to beak-reach. Same recipe, different stones each time. |
| `_BASKET_SUBPLOTS` | stone-pile on the rim | The crow's gathered stone-pile sits beside the pitcher, each stone in place. Dropping a new stone into the pitcher doesn't move the ones already piled on the rim — the pile is the original, untouched arrangement. |
| `_SIEVE_SUBPLOTS` | sorting-perch | The crow holds each stone over the pitcher's mouth and decides: smooth round ones go in, jagged or flat ones are set aside. The rule filters the whole pile — only the qualifying stones reach the water. |
| `_NOTEBOOK_SUBPLOTS` | water-tally scratch | The crow scratches a tally mark into the pitcher's clay face each time the water level rises — the mark persists, updated stone by stone, visible to any crow who perches there later. |
| `_ACORN_SUBPLOTS` | stone-count | The clever crow counts smooth stones from the meadow floor, adding, dividing, or subtracting to calculate exactly how many more drops will raise the water to beak-reach. |
| `_GATE_SUBPLOTS` | dual-gate check | The crow can only drink if two gates clear in sequence — the pitcher must be deep enough AND the water must have risen past the threshold mark. One gate closed, no drink. |
| `_FORK_SUBPLOTS` | branch-choice above the pitcher | Perched above the pitcher's mouth, the crow decides: if the water already clears the mark, lower the beak; else drop another stone. The branch in the form is the branch on the perch. |
| `_ROADSIGN_SUBPLOTS` | rim-carving | The crow carves a name into the pitcher's clay rim — a marker any crow who perches there can read to know which calculation is stored at this spot. Named once; recalled whenever needed. |
| `_SAFETYNET_SUBPLOTS` | soft-moss test-drop | The crow tests each stone over a soft patch of moss before committing — if the form fails, the moss catches the stone safely and the crow can try a different one without losing the water level. |
| `_SCROLL_SUBPLOTS` | talon-inscribed flat stone | The crow scratches an inscription into a smooth flat stone with the tip of her talon — written once in the moment, readable whenever another crow alights on the same stone later. |
| `_GUILD_SUBPLOTS` | any-crow-can-drop | Any crow at the pitcher — Korvus, Caw, Sable — answers the same stone-drop call. Each raises the water the same amount per stone, each in their own rhythm, but the result is uniform. |
| `_SORTINGTABLE_SUBPLOTS` | shape-sorting rim | The pitcher's mouth has a sorting lip: stones marked with one groove go straight in; stones with two grooves are deflected to the pile. The mark on the stone decides the path, not the crow's choice at the moment. |
| `_CARRYINGCASE_SUBPLOTS` | custom-stitched stone-pouch | The clever crow weaves a carrying-pouch from bark strips and vine — a bespoke case with named slots for each kind of stone (round, flat, jagged). The case's shape defines what fits inside. |
| `_TOOLSHED_SUBPLOTS` | borrowed earthenware vessel | The crow borrows an earthenware pitcher made by a human potter — a different maker's vessel, different clay, but the stone-drop sequence works the same. The crow's beak doesn't care who fired the clay. |
| `_RUNNERAHEAD_SUBPLOTS` | scout-crow | The clever crow sends a second crow ahead to count the stones at the far orchard — come back with the tally when done; meanwhile, keep dropping here. The scout's count arrives when the form resolves. |
| `_REWRITERULE_SUBPLOTS` | rewrite-before-drop | The crow's talon rewrites the drop-order scratched on the rim before a single stone falls — a master revision that changes what the form will do before the REPL sees it. |
| `_SCRIBE_SUBPLOTS` | pitcher-notations | The talon-scratched notes on the clay: spacing between tally marks, parenthetical asides in the margin, shorthand that tells the REPL how to read the form before it evaluates. |
| `_CHALKMARK_SUBPLOTS` | chalk-scratch vs the stone | The chalk mark scratched on a smooth stone names the stone — it is not the stone itself. The mark can be carried, quoted, passed around; only when the form runs does the mark become the stone's weight. |
| `_TALLYWALK_SUBPLOTS` | stone-by-stone running tally | The crow walks the rim of the pitcher, dropping each stone in turn, carrying the running count in one talon — the tally grows with every drop until the last stone goes in. |
| `_BEADSTRING_SUBPLOTS` | pebble-string on a vine | The crow threads smooth pebbles on a vine in a row — each pebble a character in the sequence, the whole vine a pebble-string. Joining two vines end-to-end extends the string; snipping a stretch takes a slice. |
| `_CIRCUIT_SUBPLOTS` | looping-drop without leaving the rim | The crow loops back to the stone-pile after each drop without lifting off the rim — stone after stone in a tight circuit, each iteration calling back to the start without growing the flight path. |

---

## Character-placeholder scheme

In templates, use:
- `{clever}` / `{clever_phrase}` / `{clever_he_she}` / `{clever_he_she_cap}` / `{clever_his_her}` / `{clever_him_her}` — patient stone-dropper
- `{hasty}` / `{hasty_phrase}` / `{hasty_he_she}` / `{hasty_he_she_cap}` / `{hasty_his_her}` / `{hasty_him_her}` — impatient guesser

`{clever}` maps to the tortoise-analog (writes the form, drops the stone).
`{hasty}` maps to the hare-analog (wants the answer without submitting).

Crow-pitched emotion pools (`{emo_thirsty}`, `{emo_patient}`, `{emo_proud}`)
are all pronoun-neutral (no hardcoded "her").

---

## Tone notes for template authors

- Every template should feel **bird-physical**: perching, beaking,
  taloning, wingfolding, dropping stones, watching water rise.
- The REPL is always the pitcher. Submitting the form = dropping
  the stone. The value = the water-level when the stone settles.
- `{hasty}` wants to guess (put the beak in before the water is
  up) or gives up ("the water is too low — we should move on").
  `{clever}` keeps dropping, form by form, until the water rises.
- Vary the location (garden, orchard, farm, hilltop, meadow) to
  give each record its own setting. The pitcher can sit anywhere.
