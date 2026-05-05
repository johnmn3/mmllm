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

def _crows() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "crow")

# Other fables would supply their own pickers; tortoise-hare uses these.
TORTOISE_HARE_LOCATIONS = ("meadow", "forest", "woods", "garden",
                            "orchard", "hilltop", "road")

# Crow-pitcher leans into vessel-friendly settings — places where a
# pitcher could naturally sit and be visited by a thirsty crow. Water
# locations (pond, river bank) are deliberately excluded; the central
# drama is "no easy water nearby," and a pond sitting beside the
# pitcher would defuse the fable's tension.
CROW_PITCHER_LOCATIONS = ("garden", "orchard", "farm", "market",
                           "village", "meadow", "road", "hilltop")


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


def _pick_cp_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (hasty_crow, clever_crow) pair for crow-pitcher.

    The fable in its original form has one crow facing an inanimate
    pitcher; the curriculum stages a dialogue between two crows so the
    moral dynamic — patient form-building vs. give-up impatience — can
    be carried by the characters rather than left implicit. Both
    characters drawn from the same crow pool; roles are assigned per
    record so any of (Korvus, Caw, Sable) plays either side."""
    crows = list(_crows())
    pair = scene.rng.sample(crows, 2)
    return pair[0], pair[1]


def _pick_cp_location(scene: Scene) -> ont.Location:
    """Pick a crow-pitcher-natural outdoor location."""
    cands = [l for l in ont.LOCATIONS
             if l.name in CROW_PITCHER_LOCATIONS]
    return scene.rng.choice(cands)


def _pick_chars(scene: Scene, fable: str) -> tuple[ont.Character, ont.Character]:
    """Dispatch character picking based on fable. Additive — defaults
    to tortoise-hare's picker for any unrecognized fable so existing
    callers keep working unchanged."""
    if fable == "crow-pitcher":
        return _pick_cp_chars(scene)
    return _pick_th_chars(scene)


def _pick_location(scene: Scene, fable: str) -> ont.Location:
    """Dispatch location picking based on fable. Additive — defaults
    to tortoise-hare's picker for any unrecognized fable."""
    if fable == "crow-pitcher":
        return _pick_cp_location(scene)
    return _pick_th_location(scene)


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

    For tortoise-hare (and any unrecognized fable), the canonical
    {hare}/{tortoise} placeholders + their pronoun variants are
    populated. For crow-pitcher, the same two characters (now both
    crows, returned by `_pick_cp_chars`) are ALSO exposed under
    role-aware aliases — `{hasty}`/`{clever}` and their phrase /
    pronoun variants — so subplot templates read naturally for the
    fable's setting. Additions are purely additive: crow-pitcher's
    keys never overwrite tortoise-hare's, and tortoise-hare templates
    keep working unchanged.
    """
    placeholders = {
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

        # emotions (single picks)
        "emo_proud":       scene.rng.choice(EMO_PROUD),
        "emo_patient":     scene.rng.choice(EMO_PATIENT),
        "emo_tired":       scene.rng.choice(EMO_TIRED),
    }
    if fable == "crow-pitcher":
        # `hare` slot holds the role-A (would-give-up / hasty) crow;
        # `tortoise` slot holds the role-B (patient, methodical) crow.
        # Aliases below let crow-pitcher subplots read naturally without
        # forcing them to use tortoise-hare-specific placeholder names.
        placeholders.update({
            "hasty":             hare.name,
            "clever":            tortoise.name,
            "hasty_phrase":      species_phrase(hare),
            "clever_phrase":     species_phrase(tortoise),
            "hasty_he_she":      hare.he_she,
            "clever_he_she":     tortoise.he_she,
            "hasty_he_she_cap":  cap(hare.he_she),
            "clever_he_she_cap": cap(tortoise.he_she),
            "hasty_his_her":     hare.his_her,
            "clever_his_her":    tortoise.his_her,
            "hasty_him_her":     hare.him_her,
            "clever_him_her":    tortoise.him_her,
            # crow-flavored emotions (single picks per record)
            "emo_thirsty":       scene.rng.choice(EMO_THIRSTY),
            "emo_desperate":     scene.rng.choice(EMO_DESPERATE),
        })
    return placeholders


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
       1. Picking a (hare, tortoise, location) for narrative
       2. Picking an aesopian opener
       3. Picking a subplot template
       4. Filling placeholders + rendering question
       5. Building the eval(form) tool call
    """
    hare, tortoise = _pick_chars(scene, sub.fable)
    location = _pick_location(scene, sub.fable)

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

    placeholders = _build_placeholders(scene, hare, tortoise, location,
                                        example, sub.fable)
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
