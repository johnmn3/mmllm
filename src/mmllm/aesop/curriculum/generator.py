"""Fable-curriculum generator.

Each (fable, grade, subject) triple defines a body of training records:
- The user_msg embeds the subject's question inside a narrative variant
  drawn from the fable's character pool, location pool, and opener pool.
- The assistant_msg emits an `eval(form)` tool call whose form is the
  Clojure source the subject asks the student to write.
- The eval result, when computed by the runtime, is the answer.

The point: the SAME Clojure subject is taught through hundreds of
different narrative renderings of the same fable, so the model learns
the Clojure concept by seeing it appear in many surface forms — and
learns the fable's narrative dynamics deeply by seeing them constantly
redeployed across different subjects.

Coverage math (per fable, per subject):
   examples × character-pool × location-pool × opener-pool × subplot-pool
   = 5-10 × 4-7 × 8-14 × 4-5 × 6
   ≈ 200-2,000 distinct surface variants per subject

Across all 12 grades × ~18-22 subjects per grade ≈ 216 subjects per
fable. ×10 fables ≈ 2,160 subjects total. With ~500 average variants
each, that's ~1M training records — orders of magnitude more than
the original aesop fable corpus.

Usage:
    from mmllm.aesop.curriculum.generator import generate_subject
    from mmllm.aesop.curriculum.tortoise_hare.grade_1 import SUBJECTS

    records = generate_subject(SUBJECTS["G1-01"], n_per_example=20)
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from typing import Callable, Iterable

from mmllm.aesop import ontology as ont
from mmllm.aesop.fables import (
    FABLE_OPENERS, _aesopian_intro, EMO_PROUD, EMO_PATIENT, EMO_TIRED,
    EMO_HUNGRY, EMO_GREEDY, EMO_CONTENT, EMO_REGRETFUL, EMO_DESPERATE,
    EMO_THIRSTY,
)
from mmllm.aesop.template import (
    ANSWER_AND_EVAL, ANSWER_ONLY, Record, Scene,
    build_tool_calls, render_tool_calls, resolve_preface,
    assemble_assistant_msg, system_prompt, place_phrase,
    species_phrase, smart_pronoun, n_unit, unit, cap,
)


# ─────────────────────── data shapes ───────────────────────


@dataclass
class SubjectExample:
    """One Clojure exercise within a subject.

    `form` is the source the model is being asked to write — what goes
    inside `eval(form: …)`. `expected` is the value evaluating that form
    produces — never appears in the user_msg or any narrative; only used
    for the verifier to confirm correctness.

    `concept_phrase` is a short noun-phrase the subplot template uses
    to refer to what the student is supposed to write — e.g., "the
    value 42", "the form `(+ 1 2)`", "a Clojure expression that
    multiplies 4 by 7". Subplots interpolate this so the narrative
    can flow ("Whisker pointed to {concept_phrase} and asked…").

    `question_what` is the noun-phrase the question wraps around: e.g.,
    "this form evaluates to" or "the result of this expression". The
    subplot ends with "Write a Clojure expression that computes {what}".
    """
    form:           str
    expected:       object
    concept_phrase: str
    question_what:  str
    # tags used for filtering / weighting (optional)
    tags:           tuple[str, ...] = ()


@dataclass
class SubplotTemplate:
    """One narrative scaffold parameterized over (chars, location, form).

    Templates are Python format strings with named placeholders. Each
    template produces a complete user_msg body (the part after the
    aesopian opener and before the question line).

    Standard placeholders (always available):
      {hare}, {tortoise}      — primary characters
      {hare_phrase}           — "Whisker the hare"
      {tortoise_phrase}       — "Shelly the tortoise"
      {hare_he_she}, etc.     — pronouns
      {place}                 — "in the meadow"
      {form_display}          — "`42`", "`(+ 1 2)`", etc. — backtick-wrapped
      {concept_phrase}        — example.concept_phrase
      {emo_proud}, {emo_patient}, …  — single picks from emotion pools

    Templates SHOULD NOT contain the numeric answer — only forms /
    operations / quantities mentioned in the form. The student/model
    is asked to write the form; the answer is what the form computes.
    """
    template:        str
    weight:          float = 1.0
    # Optional tags for selecting which examples this template fits
    fits_tags:       tuple[str, ...] = ()


@dataclass
class SubjectCurriculum:
    """One subject taught through one fable."""
    grade:         int
    subject_id:    str            # e.g., "G1-01"
    subject_title: str            # e.g., "Eval as substitution"
    fable:         str            # e.g., "tortoise-hare"
    examples:      list[SubjectExample]
    subplots:      list[SubplotTemplate]
    plan_pool:     tuple[str, ...] = ()   # plan-only prefaces; never reveal answer


# ─────────────────────── per-fable character / location pools ───────────────────────


def _hares() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "hare")

def _tortoises() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "tortoise")

# Other fables would supply their own pickers; tortoise-hare uses these.
TORTOISE_HARE_LOCATIONS = ("meadow", "forest", "woods", "garden",
                            "orchard", "hilltop", "road")


def _pick_th_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (hare, tortoise) pair for a record."""
    hare = scene.rng.choice(_hares())
    # ensure tortoise is different name (always is — different species — but defensively)
    tortoise = scene.rng.choice(_tortoises())
    return hare, tortoise


def _pick_th_location(scene: Scene) -> ont.Location:
    """Pick from the path-like outdoor locations natural for tortoise-hare."""
    cands = [l for l in ont.LOCATIONS
             if l.name in TORTOISE_HARE_LOCATIONS]
    return scene.rng.choice(cands)


# ─── goose-eggs character / location pools ───
#
# Goose-eggs uses two human "trader" characters (an impatient {visitor}
# and a patient {owner}) plus a goose. Locations are the village +
# household places where the fable plays out. Excludes characters whose
# role_classes belong to other fables (shepherd, dreamer, racer, etc.)
# even though they're tagged "trader" by accident.
GOOSE_EGGS_LOCATIONS = ("farm", "village", "market", "barn", "cottage",
                         "kitchen", "cellar", "orchard", "meadow")


def _ge_owners() -> tuple[ont.Character, ...]:
    """Human trader characters suitable for goose-eggs roles."""
    blocked = {"shepherd", "dreamer", "liar", "counter"}
    return tuple(
        c for c in ont.CHARACTERS
        if c.species == "human"
        and "trader" in c.role_classes
        and not (set(c.role_classes) & blocked)
    )


def _ge_geese() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "goose")


def _pick_ge_chars(scene: Scene) -> tuple[ont.Character,
                                          ont.Character,
                                          ont.Character]:
    """Pick (owner, visitor, goose) for a goose-eggs record.

    `owner` is the patient eval-trusting character (tortoise-analog).
    `visitor` is the impatient guesser who wants the answer without
    submitting the form (hare-analog).
    `goose` is the value-yielding bird whose one-egg-per-morning routine
    parallels the REPL's one-form-at-a-time evaluation.
    """
    pool = _ge_owners()
    owner = scene.rng.choice(pool)
    # ensure visitor is a different name than owner
    visitor_pool = [c for c in pool if c.name != owner.name]
    visitor = scene.rng.choice(visitor_pool)
    goose = scene.rng.choice(_ge_geese())
    return owner, visitor, goose


def _pick_ge_location(scene: Scene) -> ont.Location:
    """Pick from village + household locations natural for goose-eggs."""
    cands = [l for l in ont.LOCATIONS if l.name in GOOSE_EGGS_LOCATIONS]
    return scene.rng.choice(cands)


# Pronoun-neutral emotion pools. The fables.py EMO_GREEDY/EMO_CONTENT/
# EMO_REGRETFUL pools hard-code "his/her", which produces ungrammatical
# text when the assigned character has a different gender. These pools
# read naturally regardless of the surrounding character's pronoun.
GE_EMO_GREEDY = (
    "with a hungry gleam in the eye",
    "imagining all that might be gained",
    "thoughts already on more",
    "with hands itching to count more",
    "eyeing the next morning's gift",
    "tempted by the thought of plenty",
    "calculating in silence",
    "with a glint of impatience",
)
GE_EMO_CONTENT = (
    "happy with the day's small gift",
    "pleased with the steady fortune",
    "grateful for every coin",
    "content with the quiet life",
    "settled and unhurried",
    "untroubled by the village gossip",
    "calm in the morning routine",
)
GE_EMO_REGRETFUL = (
    "wishing for more careful counting",
    "regretting the hasty thought",
    "wondering how the temptation had risen",
    "shaking off a careless idea",
    "thinking better of the rash impulse",
)


# ─── boy-wolf character / location pools ───
#
# Boy-wolf cast model: ONE shepherd (the negative moral example — cries
# wolf) + ONE elder/villager (the corrective voice). The shepherd plays
# the Hare-equivalent role (boastful, hasty); the elder/villager plays
# the Tortoise-equivalent role (careful, evaluator-of-record). Unlike
# tortoise-hare where Tortoise is itself a model character, in boy-wolf
# the SHEPHERD is the cautionary one, and the corrective discipline lives
# in the surrounding villagers / elders / a careful neighbouring shepherd.

def _shepherds() -> tuple[ont.Character, ...]:
    """Tom (m), Will (m), Pat (n), Jess (f), Lou (f) — all role
    ('liar', 'shepherd'). These are the boy-who-cried-wolf cast."""
    return tuple(c for c in ont.CHARACTERS if "shepherd" in c.role_classes)


def _bw_villagers() -> tuple[ont.Character, ...]:
    """Pool of village-folk who play the corrective voice in boy-wolf
    subplots. Drawn from the human characters with role 'everyman' —
    Bob, Frank, George, Oliver, Carol, Grace, Alex, Sam, Robin, Morgan
    (and Alice, who carries 'everyman' as a third role). Mixed-gender
    so the same shepherd can be paired with same- or different-gender
    villager across runs for variety."""
    return tuple(c for c in ont.CHARACTERS
                 if c.species == "human" and "everyman" in c.role_classes)


# Pastoral / village locations natural for boy-wolf. We exclude indoor
# spaces and water-anchored ones; the action happens between hill,
# meadow, and village square.
BOY_WOLF_LOCATIONS = ("meadow", "forest", "hilltop", "village", "farm",
                      "road", "woods", "orchard")


def _pick_bw_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (shepherd, elder) pair for a boy-wolf record."""
    shepherd = scene.rng.choice(_shepherds())
    # Avoid name collision (different name pools, but defensive guard
    # in case the ontology grows).
    cands = [c for c in _bw_villagers() if c.name != shepherd.name]
    elder = scene.rng.choice(cands)
    return shepherd, elder


def _pick_bw_location(scene: Scene) -> ont.Location:
    """Pick a pastoral / village location natural for boy-wolf."""
    cands = [l for l in ont.LOCATIONS
             if l.name in BOY_WOLF_LOCATIONS]
    return scene.rng.choice(cands)



# ─────────────────────── render helpers ───────────────────────


def _format_form_display(form: str) -> str:
    """Wrap a Clojure form for display inside narrative prose. Use
    backticks so the form is visually distinct."""
    return f"`{form}`"


def _build_placeholders(scene: Scene,
                        hare: ont.Character,
                        tortoise: ont.Character,
                        location: ont.Location,
                        example: SubjectExample,
                        fable: str = "tortoise-hare") -> dict:
    """Assemble the {placeholder: value} dict that subplot templates use.

    The two character slots are named `hare` / `tortoise` for historical
    reasons — they were introduced for the tortoise-hare reference
    curriculum. Other fables receive *aliases* under the names natural
    to their cast (e.g. `shepherd` / `elder` for boy-wolf), so a fable's
    subplot templates can use idiomatic placeholder names while the
    underlying character objects live in the same two slots.

    `fable` controls which alias set gets emitted. Default tortoise-hare.
    """
    base = {
        # characters
        "hare":            hare.name,
        "tortoise":        tortoise.name,
        "hare_phrase":     species_phrase(hare),
        "tortoise_phrase": species_phrase(tortoise),
        "hare_he_she":     hare.he_she,
        "tortoise_he_she": tortoise.he_she,
        "hare_he_she_cap": cap(hare.he_she),
        "tortoise_he_she_cap": cap(tortoise.he_she),
        "hare_his_her":    hare.his_her,
        "tortoise_his_her": tortoise.his_her,
        # Object-case pronouns (for "asked X to ...", "told X that ...")
        "hare_him_her":     hare.him_her,
        "tortoise_him_her": tortoise.him_her,

        # place
        "place":           place_phrase(scene, location),
        "location":        location.name,

        # the example
        "form_display":    _format_form_display(example.form),
        "concept_phrase":  example.concept_phrase,
        "what":            example.question_what,

        # emotions (single picks). Fables that need other emotion pools
        # (regretful, desperate, content, ...) can extend this dict in
        # their per-fable alias section below.
        "emo_proud":       scene.rng.choice(EMO_PROUD),
        "emo_patient":     scene.rng.choice(EMO_PATIENT),
        "emo_tired":       scene.rng.choice(EMO_TIRED),
    }

    # ─── Per-fable additive aliases ───
    #
    # These are pure aliases pointing at the SAME two character objects
    # already exposed under hare/tortoise. They let each fable's subplot
    # templates use placeholder names natural to the fable's cast without
    # the templates having to talk about hares and tortoises.

    if fable == "boy-wolf":
        # Slot A (hare) → the SHEPHERD (the boy who cries wolf — the
        # cautionary character). Slot B (tortoise) → the ELDER /
        # VILLAGER (the corrective voice).
        base.update({
            "shepherd":             hare.name,
            "shepherd_phrase":      species_phrase(hare),
            "shepherd_he_she":      hare.he_she,
            "shepherd_he_she_cap":  cap(hare.he_she),
            "shepherd_his_her":     hare.his_her,
            "shepherd_him_her":     hare.him_her,

            "elder":                tortoise.name,
            "elder_phrase":         species_phrase(tortoise),
            "elder_he_she":         tortoise.he_she,
            "elder_he_she_cap":     cap(tortoise.he_she),
            "elder_his_her":        tortoise.his_her,
            "elder_him_her":        tortoise.him_her,

            # 'villager' is an alias for elder used in some templates
            # where 'elder' would feel too age-specific.
            "villager":             tortoise.name,
            "villager_phrase":      species_phrase(tortoise),
            "villager_he_she":      tortoise.he_she,
            "villager_he_she_cap":  cap(tortoise.he_she),
            "villager_his_her":     tortoise.his_her,
            "villager_him_her":     tortoise.him_her,

            # Boy-wolf-specific emotion picks. The fable's own narrative
            # uses regretful (the village counting the cost) and
            # desperate (the shepherd shouting in earnest) heavily.
            "emo_regretful":   scene.rng.choice(EMO_REGRETFUL),
            "emo_desperate":   scene.rng.choice(EMO_DESPERATE),
        })

    return base


def _build_ge_placeholders(scene: Scene,
                           owner:    ont.Character,
                           visitor:  ont.Character,
                           goose:    ont.Character,
                           location: ont.Location,
                           example:  SubjectExample) -> dict:
    """Goose-eggs placeholder dict.

    Provides BOTH the goose-eggs-specific keys (`{owner}`, `{visitor}`,
    `{goose}` and their phrase / pronoun variants) AND the tortoise-hare
    `{hare}` / `{tortoise}` aliases so the shared subplot templates from
    `tortoise_hare/grade_1.py:_SHARED_SUBPLOTS` still render. The mapping
    is: visitor → hare-analog (impatient guesser), owner → tortoise-analog
    (patient evaluator). This is the additive part of the SKILL doc's
    "extend `_build_placeholders`" recipe.
    """
    return {
        # tortoise-hare-style aliases (so shared subplots from
        # tortoise_hare/grade_1.py render naturally without rewrites)
        "hare":            visitor.name,
        "tortoise":        owner.name,
        "hare_phrase":     species_phrase(visitor),
        "tortoise_phrase": species_phrase(owner),
        "hare_he_she":     visitor.he_she,
        "tortoise_he_she": owner.he_she,
        "hare_he_she_cap": cap(visitor.he_she),
        "tortoise_he_she_cap": cap(owner.he_she),
        "hare_his_her":    visitor.his_her,
        "tortoise_his_her": owner.his_her,
        "hare_him_her":    visitor.him_her,
        "tortoise_him_her": owner.him_her,

        # Goose-eggs cast
        "owner":           owner.name,
        "owner_phrase":    species_phrase(owner),
        "owner_he_she":    owner.he_she,
        "owner_he_she_cap": cap(owner.he_she),
        "owner_his_her":   owner.his_her,
        "owner_him_her":   owner.him_her,
        "visitor":         visitor.name,
        "visitor_phrase":  species_phrase(visitor),
        "visitor_he_she":  visitor.he_she,
        "visitor_he_she_cap": cap(visitor.he_she),
        "visitor_his_her": visitor.his_her,
        "visitor_him_her": visitor.him_her,
        "goose":           goose.name,
        "goose_phrase":    species_phrase(goose),
        "goose_he_she":    goose.he_she,
        "goose_he_she_cap": cap(goose.he_she),
        "goose_his_her":   goose.his_her,
        "goose_him_her":   goose.him_her,

        # place
        "place":           place_phrase(scene, location),
        "location":        location.name,

        # the example
        "form_display":    _format_form_display(example.form),
        "concept_phrase":  example.concept_phrase,
        "what":            example.question_what,

        # emotions (pronoun-neutral pools so any character gender works)
        "emo_proud":       scene.rng.choice(EMO_PROUD),
        "emo_patient":     scene.rng.choice(EMO_PATIENT),
        "emo_tired":       scene.rng.choice(EMO_TIRED),
        "emo_greedy":      scene.rng.choice(GE_EMO_GREEDY),
        "emo_content":     scene.rng.choice(GE_EMO_CONTENT),
        "emo_regretful":   scene.rng.choice(GE_EMO_REGRETFUL),
    }


def _render_question(scene: Scene, example: SubjectExample) -> str:
    """The closing line of the user_msg. Always asks the student to
    write a Clojure expression that produces the answer."""
    framings = (
        f"Write a Clojure expression that computes {example.question_what}.",
        f"Write a form whose evaluation gives {example.question_what}.",
        f"What Clojure form computes {example.question_what}? Submit it via `eval`.",
        f"Question: write a Clojure expression for {example.question_what}.",
    )
    return scene.rng.choice(framings)


# ─────────────────────── generator ───────────────────────


def generate_one_record(scene: Scene,
                        sub: SubjectCurriculum,
                        example: SubjectExample) -> Record:
    """Produce a single Record by:
       1. Picking characters + a location appropriate to the fable
       2. Picking an aesopian opener
       3. Picking a subplot template
       4. Filling placeholders + rendering question
       5. Building the eval(form) tool call
    """
    # Per-fable character / location picker dispatch. Each fable that
    # diverges from the default tortoise-hare cast has its own picker
    # branch and supplies a `placeholders_fn` that builds the placeholder
    # dict for its templates. The default branch (tortoise-hare and any
    # fable that maps cleanly onto a two-character cast) uses the
    # standard `_build_placeholders` with a `fable=` parameter.
    if sub.fable == "goose-eggs":
        owner, visitor, goose = _pick_ge_chars(scene)
        location = _pick_ge_location(scene)
        placeholders_fn = lambda ex: _build_ge_placeholders(
            scene, owner, visitor, goose, location, ex)
    elif sub.fable == "boy-wolf":
        slot_a, slot_b = _pick_bw_chars(scene)
        location = _pick_bw_location(scene)
        placeholders_fn = lambda ex: _build_placeholders(
            scene, slot_a, slot_b, location, ex, fable=sub.fable)
    else:
        slot_a, slot_b = _pick_th_chars(scene)
        location = _pick_th_location(scene)
        placeholders_fn = lambda ex: _build_placeholders(
            scene, slot_a, slot_b, location, ex, fable=sub.fable)

    intro = _aesopian_intro(scene, sub.fable, location)

    # Filter subplots by tags if example has tags
    candidate_subplots = sub.subplots
    if example.tags:
        tagged = [s for s in sub.subplots
                  if not s.fits_tags
                  or set(s.fits_tags) & set(example.tags)]
        if tagged:
            candidate_subplots = tagged
    weights = [s.weight for s in candidate_subplots]
    subplot = scene.rng.choices(candidate_subplots, weights=weights)[0]

    placeholders = placeholders_fn(example)
    body = subplot.template.format(**placeholders).strip()
    question = _render_question(scene, example)

    user_msg = f"{intro}{body}\n\n{question}"

    # Eval-first tool call: form is the Clojure source the model produces.
    calls    = build_tool_calls(value=example.expected,
                                form_str=example.form,
                                prefer_eval=True)
    sys_msg  = system_prompt(use_eval=True)
    plan     = scene.rng.choice(sub.plan_pool) if sub.plan_pool else ""
    preface  = resolve_preface(scene, plan)
    asst     = assemble_assistant_msg(
        preface=preface,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg=sys_msg,
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=example.expected,
        code_str=example.form,
        fable=sub.fable,
        chapter=sub.subject_id,
        catalog=ANSWER_AND_EVAL,
    )


def generate_subject(sub: SubjectCurriculum,
                     n_per_example: int = 222,
                     seed: int = 0) -> list[Record]:
    """Generate `n_per_example` records for each example in the subject.

    Total records returned = len(examples) × n_per_example.
    """
    rng = random.Random(seed)
    out = []
    for example in sub.examples:
        for _ in range(n_per_example):
            scene = Scene(rng=rng)
            out.append(generate_one_record(scene, sub, example))
    return out


def generate_grade(subjects: Iterable[SubjectCurriculum],
                   n_per_example: int = 222,
                   seed: int = 0) -> list[Record]:
    out = []
    for sub in subjects:
        out.extend(generate_subject(sub, n_per_example=n_per_example,
                                     seed=seed))
        seed += 1   # different RNG per subject
    return out
