# milkmaid semantic coverage — gap report

**Snapshot after Phase C framework lands.**

## Where we are

| Slice | Subjects | Examples | Story slots authored |
| --- | ---: | ---: | ---: |
| All milkmaid subjects | 216 | 509 | 412 |
| **Metaphor-rich (need stories)** | 185 | 422 | 412 |
| Atoms (`_SHARED_SUBPLOTS`; form-display IS the lesson) | 8 | 40 | — |
| Abstract (`_GOAL_SUBPLOTS`; goal-fallback) | 23 | 47 | — |

**Story-slot coverage of the metaphor-rich pool: 412 of 422 examples = 97.6%.**

The framework is wired in end-to-end. The long tail is **authoring slot content for the remaining metaphor-rich examples.** Each remaining slot-set is roughly 100-150 words of grounded story.

## Gap by metaphor family

| Family | Subjects | Examples | Stories | TODO |
| --- | ---: | ---: | ---: | ---: |
| `_POUCH_SUBPLOTS` | 7 | 15 | 15 | 0 ✅ |
| `_RECIPE_SUBPLOTS` | 12 | 20 | 20 | 0 ✅ |
| `_BASKET_SUBPLOTS` | 21 | 42 | 42 | 0 ✅ |
| `_SIEVE_SUBPLOTS` | 10 | 20 | 20 | 0 ✅ |
| `_NOTEBOOK_SUBPLOTS` | 12 | 23 | 23 | 0 ✅ |
| `_ACORN_SUBPLOTS` | 16 | 69 | 63 | 6 |
| `_GATE_SUBPLOTS` | 7 | 28 | 28 | 0 ✅ |
| `_FORK_SUBPLOTS` | 6 | 10 | 10 | 0 ✅ |
| `_ROADSIGN_SUBPLOTS` | 16 | 30 | 28 | 2 |
| `_SAFETYNET_SUBPLOTS` | 9 | 19 | 19 | 0 ✅ |
| `_SCROLL_SUBPLOTS` | 10 | 19 | 19 | 0 ✅ |
| `_GUILD_SUBPLOTS` | 9 | 16 | 16 | 0 ✅ |
| `_SORTINGTABLE_SUBPLOTS` | 5 | 11 | 11 | 0 ✅ |
| `_CARRYINGCASE_SUBPLOTS` | 2 | 4 | 4 | 0 ✅ |
| `_TOOLSHED_SUBPLOTS` | 9 | 19 | 19 | 0 ✅ |
| `_RUNNERAHEAD_SUBPLOTS` | 5 | 9 | 9 | 0 ✅ |
| `_REWRITERULE_SUBPLOTS` | 10 | 21 | 21 | 0 ✅ |
| `_SCRIBE_SUBPLOTS` | 9 | 19 | 17 | 2 |
| `_CHALKMARK_SUBPLOTS` | 4 | 12 | 12 | 0 ✅ |
| `_TALLYWALK_SUBPLOTS` | 3 | 8 | 8 | 0 ✅ |
| `_BEADSTRING_SUBPLOTS` | 2 | 7 | 7 | 0 ✅ |
| `_CIRCUIT_SUBPLOTS` | 1 | 1 | 1 | 0 ✅ |
| **TOTAL (metaphor-rich)** | **185** | **422** | **412** | **10** |

**19 of 22** families are fully covered (every example carries an authored story-scaffold slot-set).

## What stays on `_GOAL_SUBPLOTS` by design

The 23 subjects (47 examples) on `_GOAL_SUBPLOTS` are abstract overview / cargo-cult topics — sequences of named-concept introductions where the lesson is the goal phrasing itself, not a concrete fable scenario. Forcing a metaphor onto these would either (a) trivialise the concept or (b) introduce an analogy mismatch that confuses more than it teaches. Examples include grade-11/12 type-system overviews, transducer composition, core.async survey, and host-class introductions where the form display + goal text together form the complete pedagogical unit.

## What stays on `_SHARED_SUBPLOTS` by design

The 8 atom subjects (40 examples) use `_SHARED_SUBPLOTS` because the form **is** the lesson: each user_msg shows the literal form (`{form_display}`) and the model copies it into the eval tool call. There is no metaphor to map to because the operation is identity — read the literal, submit it.

## Bottom line

The milkmaid framework is wired and the canonicals are in. The remaining work is mechanical slot-authoring for the long tail.
