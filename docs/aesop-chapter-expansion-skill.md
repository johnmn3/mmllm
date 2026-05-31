# Aesop chapter expansion skill

This skill describes how to expand a single chapter function in
`src/mmllm/aesop/fables.py` from a 30-50 word terse setup into a
100-150 word Aesopian narrative with **6 narrative subplots** that
share the same arithmetic but each ground the abstract numbers in a
different small drama.

The skill is applied per chapter. The reference exemplar is
`_th_nap_overtake` in `src/mmllm/aesop/fables.py` (commit `a319792`+).

## Goals

1. **6 subplots per chapter** — same arithmetic, different stories.
   Each subplot is a 60-120 word self-contained narrative beat that
   uses different items / containers / settings / emotional verbs.
2. **Smooth opener-to-subplot flow** — the FABLE_OPENERS line (already
   prepended via `_aesopian_intro`) introduces the moral dynamic in
   the abstract. The subplot picks up with named characters, naturally
   continuing the narrative without redundancy.
3. **Quantities grounded in emotion** — numbers should land with
   feeling. "Bob lost 5 marbles" hits differently than "Bob has 5
   marbles." Use the EMO_* pools in fables.py:
   `EMO_PROUD`, `EMO_PATIENT`, `EMO_TIRED`, `EMO_THIRSTY`,
   `EMO_HUNGRY`, `EMO_GREEDY`, `EMO_CONTENT`, `EMO_REGRETFUL`,
   `EMO_DESPERATE`.
4. **Item / container diversity** — when a chapter naturally has
   countable items, vary them. Don't always use grain. Pull from
   `mmllm.aesop.ontology.ITEMS` (apples, marbles, coins, eggs,
   acorns, biscuits, ribbons, …) and CONTAINERS (pockets, baskets,
   jars, sacks, carts, …). Items must physically fit their container
   (`Container.fits_count(item, n)`).
5. **The math is invariant** — the existing `expr` Tree must still
   evaluate to the existing `answer`. Subplots ONLY change narrative;
   the underlying arithmetic stays exactly the same.
6. **No answer leakage** — the assistant message is built by `_finalize`
   and is just `[optional plan]\n\n{eval(form)}`. The subplot text
   goes into `user_msg`. Never put the numeric `answer` value into
   the user_msg — the question must require the model to compute it
   from the form.

## Procedure (per chapter)

For a chapter `_xx_chapter` in `fables.py`:

1. **Read the chapter** — note the:
   - characters picked (e.g. `hare`, `tortoise`)
   - location picked (or absence)
   - numerical bindings (e.g. `hare_lead`, `tortoise_speed`, `nap_hours`)
   - existing `expr` (do NOT modify the math)
   - existing `answer = evaluate(expr)`
   - the chapter's `fable=` and `chapter=` strings

2. **Identify the chapter's emotional center** — what moral dynamic
   is the math expressing?
     - tortoise-hare: pride vs steadiness → use `EMO_PROUD`,
       `EMO_PATIENT`, `EMO_TIRED`
     - crow-pitcher: thirst + cleverness → `EMO_THIRSTY`
     - goose-eggs: greed vs gratitude → `EMO_GREEDY`, `EMO_CONTENT`
     - boy-wolf: lying + panic → `EMO_DESPERATE`
     - ant-grasshopper: prudence vs idleness → `EMO_CONTENT`,
       `EMO_REGRETFUL`
     - milkmaid: hope + dreams → `EMO_GREEDY` + `EMO_REGRETFUL`
     - fox-grapes: longing + frustration → `EMO_HUNGRY`,
       `EMO_REGRETFUL`
     - two-mice: contentment vs craving → `EMO_CONTENT`, `EMO_GREEDY`
     - dog-shadow: greed losing → `EMO_GREEDY`, `EMO_REGRETFUL`
     - lion-bulls: solidarity vs division → use generic narrative

3. **Replace the existing user_msg construction** with:
   - One call to `_aesopian_intro(scene, "<fable>", location)`
     storing it in `intro` (use `_aesopian_intro(scene, "<fable>")`
     when there's no `location` variable).
   - 1-3 EMO_* picks via `scene.rng.choice(EMO_*)`.
   - A list of **6 subplot strings** (f-strings using the chapter's
     local bindings), each 60-120 words, each grounding the
     arithmetic in a distinct small drama.
   - `body = _render_subplot(scene, subplots_list)`.
   - `user_msg = f"{intro}{body}\n\n{question_phrase(scene, '...')}"`

4. **Update the `_finalize` call** — keep `value=answer`, `expr=expr`,
   `fable=...`, `chapter=...`. Optionally add a plan string (must NOT
   contain the numeric answer; describes only HOW the form works:
   "I multiply A by B and subtract C").

5. **Smoke test** — run
   ```
   python3 -c "from mmllm.aesop import fables; fables.smoke_test(seed=0, n=80)"
   ```
   Should print `fables smoke OK: 80 records across 10 fables`.

6. **Spot-check rendering** — pick a few seeds and print `rec.user_msg`
   to verify the subplots look right and match the expected length
   (80-130 words).

## Subplot writing guidelines

Each subplot:
- Names the characters once (don't repeat awkwardly)
- Uses pronouns smoothly (`smart_pronoun`, `smart_possessive` for
  same-pronoun characters)
- Mentions the chapter's specific quantities (e.g., `n_unit(hare_lead,
  'mile')`, `unit(tortoise_speed, 'mile')`)
- Picks varied items/containers from the ontology where the chapter
  is about counting things (vs simply about distance/time/etc.)
- Has its own sensory hook (a stream, a clover patch, a stump, a
  butterfly, etc.)
- Implies the moral dynamic of the fable through small narrative
  details (the proud Hare's swagger, the patient Tortoise's quiet
  steps)

Aim for each subplot to feel like a slightly different version of
the SAME folk tale told by a different storyteller — same moral, same
arithmetic, different sensory texture.

## Reference exemplar

See `_th_nap_overtake` in `src/mmllm/aesop/fables.py` for a fully
expanded example with 6 subplots covering: classic-oak, sweet-clover,
butterfly-chase, crowd-bragging, cool-stream, leisurely-amble.

## Out of scope (do NOT do)

- Don't change the `expr` AST or `answer` value.
- Don't add new Lit/Var bindings to the expr.
- Don't add result_text or code_block to `_finalize` calls (those are
  legacy params; the eval-first design relies on the form being the
  only place the math materializes).
- Don't put the numeric answer into the user_msg or plan.
- Don't break the existing chapter signature — `def _xx(scene: Scene)
  -> Record:`.
