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
from mmllm.aesop.curriculum import character_pools as char_pools
from mmllm.aesop.curriculum import opener_pools as opener_pools_mod
from mmllm.aesop.curriculum import emotion_pools as emo_pools
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

    `goal_text` (optional) — a one-sentence imperative describing WHAT
    the form should do, without showing the form itself. Used by
    "goal-style" subplots that describe the goal and ask the model to
    produce the form, rather than showing the form and asking the
    model to copy-evaluate it. Example: form `(+ 1 2)` → goal_text
    `"add 1 and 2"`. When empty, subjects use atom-style subplots
    that show the form (legitimate for L1 atom subjects where the form
    IS the answer; copy-from-prompt is the lesson).

    Story-scaffold slots (optional, all four together) — when an
    example is authored with a grounded fable story, these four
    slots compose a 5-act narrative that templates can render
    directly. Templates that reference these placeholders should be
    tagged with `fits_tags=("story",)` so they only fire for
    examples that include "story" in their tags.

      `scenario`   (act 1 — SETUP)     — a concrete situation in the
                                         meadow that *exists*. Names
                                         characters, place, and the
                                         current state of the world.
                                         1-3 sentences.
      `need`       (act 2 — NEED)      — what's needed; the question
                                         the operation answers.
                                         Without the operation,
                                         something fails. 1-2
                                         sentences.
      `mapping`    (act 3 — MAPPING)   — how the metaphor's elements
                                         map 1:1 to the operation's
                                         parts. The pedagogical core.
                                         1-2 sentences.
      `resolution` (act 5 — RESOLUTION)— what the REPL's value means
                                         in the story; closes the
                                         loop with the need. 1
                                         sentence.

    Act 4 (ACTION) is supplied by the template — the character
    composes `{concept_phrase}` and submits.
    """
    form:           str
    expected:       object
    concept_phrase: str
    question_what:  str
    goal_text:      str = ""
    # Story-scaffold slots (Phase C). All four authored together,
    # with the example's tags including "story" so story-aware
    # subplot templates can match via fits_tags.
    scenario:       str = ""
    need:           str = ""
    mapping:        str = ""
    resolution:     str = ""
    # tags used for filtering / weighting (optional). Examples with
    # all four story slots filled should also include "story" in
    # their tags so story-templates fire.
    tags:           tuple[str, ...] = ()
    # Parametric scalar slots (Phase D — zero-hardcoded-scalars).
    # When `form_template` is set, `slots` defines the typed pools
    # to draw from at render time, and `expected_fn(draws) -> value`
    # computes the ground-truth answer from the draws. The verifier
    # parses the rendered form via form_parser.parse, evaluates via
    # expr.evaluate, and confirms the answer matches expected_fn(draws).
    # Story slots and concept_phrase / question_what / goal_text may
    # reference `{drawn.<slot>}` placeholders to interpolate drawn
    # values into the prose.
    form_template:  str = ""
    slots:          dict = field(default_factory=dict)
    expected_fn:    object = None  # Callable[[dict], Any]
    # Macro / host-interop subjects: `bb_verify=True` routes the form
    # to a Babashka subprocess at curriculum-build time instead of
    # the in-process expr.py evaluator. Requires the form to be valid
    # Clojure source; expected_fn (or hardcoded `expected`) must agree
    # with bb's evaluation.
    bb_verify:      bool = False

    def __post_init__(self):
        """If this is a legacy example (no form_template) and the form
        contains literals we can identify, auto-migrate to parametric.
        Prose fields with literal occurrences also get
        `{drawn.<slot>}` interpolation injected automatically."""
        if self.form_template:
            return  # already parametric
        if not self.form:
            return  # nothing to convert
        # Skip the conversion for forms where the legacy path is the
        # only sensible interpretation (e.g. macros, host interop).
        if self.bb_verify:
            self._maybe_close_resolution_loop()
            return
        from mmllm.aesop.curriculum.auto_parametric import (
            auto_parametric_from_form, replace_literals_in_prose,
        )
        result = auto_parametric_from_form(self.form, expected=self.expected)
        if result is None:
            self._maybe_close_resolution_loop()
            return  # cannot auto-convert; remain legacy
        template, slots, expected_fn, value_to_slot = result
        # Mutate via object.__setattr__ since this is a frozen-style
        # post-init (dataclass field assignment).
        object.__setattr__(self, "form_template", template)
        object.__setattr__(self, "slots",         slots)
        object.__setattr__(self, "expected_fn",   expected_fn)
        # Prose: scan each prose field and replace literal occurrences
        # with {drawn.<slot>} placeholders.
        for fld in ("concept_phrase", "question_what", "goal_text",
                    "scenario", "need", "mapping", "resolution"):
            old = getattr(self, fld)
            new = replace_literals_in_prose(old, value_to_slot)
            if new != old:
                object.__setattr__(self, fld, new)
        # If the example is story-tagged and the resolution still
        # doesn't reference any drawn slot, append a closing
        # parenthetical so the resolution closes the loop with the
        # parametric draw. Audited by the milkmaid wggf fix-set:
        # STORY_RESOLUTION_NO_DRAWN was firing on ~967 milkmaid
        # records because legacy resolutions name a fixed answer
        # ("the REPL answered `false`") without referencing the
        # actual drawn value. The parenthetical adds a {drawn.<first>}
        # so the rendered resolution always contains a literal that
        # matches the form's drawn literal.
        if "story" in (self.tags or ()) and self.resolution and slots:
            res = self.resolution
            if not any(f"{{drawn.{s}}}" in res for s in slots):
                first = next(iter(slots.keys()))
                stripped = res.rstrip(" .;:")
                trail = res[len(stripped):]
                object.__setattr__(
                    self, "resolution",
                    f"{stripped} (with `{{drawn.{first}}}` as the input value){trail}"
                )

    def _maybe_close_resolution_loop(self):
        """For story-tagged legacy/bb_verify examples (no parametric slots),
        append a parenthetical mentioning the form's first literal so the
        resolution closes the loop. Skipped if a literal is already present.
        Mirrors the audit's `_drawn_literals` filtering (skips ints 0/1/2 as
        ambient).
        """
        if "story" not in (self.tags or ()) or not self.resolution:
            return
        import re as _re
        lits = []
        for m in _re.finditer(r"-?\d+", self.form):
            v = m.group(0)
            if v not in ("0", "1", "2"):
                lits.append(v)
        for m in _re.finditer(r":[a-zA-Z][a-zA-Z0-9-]*", self.form):
            lits.append(m.group(0))
        for m in _re.finditer(r'"([^"]{2,})"', self.form):
            lits.append(m.group(1))
        slots_text = " ".join(filter(None, (
            self.scenario, self.need, self.mapping, self.resolution,
        )))
        if lits and not any(lit in slots_text for lit in lits):
            first = lits[0]
            stripped = self.resolution.rstrip(" .;:")
            trail = self.resolution[len(stripped):]
            object.__setattr__(
                self, "resolution",
                f"{stripped} (with `{first}` as the input value){trail}"
            )


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

def _ants() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "ant")

def _grasshoppers() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "grasshopper")

# Other fables would supply their own pickers; tortoise-hare uses these.
TORTOISE_HARE_LOCATIONS = ("meadow", "forest", "woods", "garden",
                            "orchard", "hilltop", "road")

# Ant-grasshopper natural locations: the meadow and adjacent outdoor
# settings where the Ant gathers and the Grasshopper plays. We swap
# the tortoise-hare 'road' for 'farm' (more natural for stockpile
# narratives) and keep the rest.
ANT_GRASSHOPPER_LOCATIONS = ("meadow", "forest", "woods", "garden",
                              "orchard", "hilltop", "farm")


def _make_char(name: str, species: str, gender: str = "n",
               role_classes: tuple = (), archetypes: tuple = ()) -> ont.Character:
    """Build a Character from a name-pool draw. Used by per-fable
    pickers when drawing from the expanded ~200-name pools rather
    than the legacy 2-4-name ontology."""
    return ont.Character(
        name=name, species=species, gender=gender,
        role_classes=role_classes, archetypes=archetypes,
    )


_FABLE_OPENER_POOL = {
    "tortoise-hare": opener_pools_mod.OPENERS_TORTOISE_HARE,
    "crow-pitcher":  opener_pools_mod.OPENERS_CROW_PITCHER,
    "milkmaid":      opener_pools_mod.OPENERS_MILKMAID,
    "boy-wolf":      opener_pools_mod.OPENERS_BOY_WOLF,
    "dog-shadow":    opener_pools_mod.OPENERS_DOG_SHADOW,
}

_FABLE_PLAN_POOL = {
    "tortoise-hare": opener_pools_mod.PLANS_TORTOISE_HARE,
    "crow-pitcher":  opener_pools_mod.PLANS_CROW_PITCHER,
    "milkmaid":      opener_pools_mod.PLANS_MILKMAID,
    "boy-wolf":      opener_pools_mod.PLANS_BOY_WOLF,
    "dog-shadow":    opener_pools_mod.PLANS_DOG_SHADOW,
}


_FABLE_SPECIES_PHRASE = {
    "tortoise-hare": {"hare": "the hare", "tortoise": "the tortoise"},
    "crow-pitcher":  {"crow": "the crow"},
    "milkmaid":      {"human": ""},
    "boy-wolf":      {"human": ""},
    "dog-shadow":    {"dog": "the dog"},
}


def _phrase_for(ch: ont.Character, fable: str) -> str:
    """`Whisker the hare` style. For human roles, just the name."""
    species_phrases = _FABLE_SPECIES_PHRASE.get(fable, {})
    suffix = species_phrases.get(ch.species, "")
    return f"{ch.name} {suffix}".strip()


def _curriculum_intro(scene: Scene, fable: str, location,
                      primary: ont.Character | None,
                      secondary: ont.Character | None) -> str:
    """Pick an opener from the 30-entry expanded opener pool for the
    given fable, substitute placeholders ({place}, {primary},
    {secondary}, {primary_phrase}, {secondary_phrase},
    {primary_he_she}, {secondary_he_she}), and return with the
    "\\n\\n" suffix the caller expects.
    """
    pool = _FABLE_OPENER_POOL.get(fable)
    if not pool:
        # Fallback: legacy path for unknown fables.
        from mmllm.aesop.fables import _aesopian_intro
        return _aesopian_intro(scene, fable, location)
    template = scene.rng.choice(pool)
    if "{" in template and "}" in template:
        place_phrase_str = (place_phrase(scene, location)
                            if location is not None else "in the meadow")
        sub = {
            "place":             place_phrase_str,
            "primary":           primary.name if primary else "",
            "secondary":         secondary.name if secondary else "",
            "primary_phrase":    _phrase_for(primary, fable) if primary else "",
            "secondary_phrase":  _phrase_for(secondary, fable) if secondary else "",
            "primary_he_she":    primary.he_she if primary else "they",
            "secondary_he_she":  secondary.he_she if secondary else "they",
        }
        try:
            opener = template.format(**sub)
        except KeyError:
            # If a template references a placeholder we don't supply,
            # fall back to the unformatted template — better than
            # crashing the whole pipeline.
            opener = template
    else:
        opener = template
    return f"{opener}\n\n"


def _pick_th_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (hare, tortoise) pair from the 200+ expanded
    name pools. Gender alternates so prose pronouns vary."""
    hare_name = scene.rng.choice(char_pools.HARE_NAMES)
    tort_name = scene.rng.choice(char_pools.TORTOISE_NAMES)
    hare_gender = scene.rng.choice(("m", "f"))
    tort_gender = scene.rng.choice(("m", "f"))
    hare = _make_char(hare_name, "hare", hare_gender, ("racer", "fast"))
    tortoise = _make_char(tort_name, "tortoise", tort_gender,
                          ("plodder", "slow"))
    return hare, tortoise


def _pick_th_location(scene: Scene) -> ont.Location:
    """Pick from the path-like outdoor locations natural for tortoise-hare."""
    cands = [l for l in ont.LOCATIONS
             if l.name in TORTOISE_HARE_LOCATIONS]
    return scene.rng.choice(cands)


def _pick_ag_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (ant, grasshopper) pair for a record."""
    ant = scene.rng.choice(_ants())
    grasshopper = scene.rng.choice(_grasshoppers())
    return ant, grasshopper


def _pick_ag_location(scene: Scene) -> ont.Location:
    """Pick from outdoor meadow-adjacent locations natural for ant-grasshopper."""
    cands = [l for l in ont.LOCATIONS
             if l.name in ANT_GRASSHOPPER_LOCATIONS]
    return scene.rng.choice(cands)



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


# Crow-pitcher: the thirsty crow drops smooth stones into the pitcher
# one by one until the water rises to where the beak can reach.
# `{clever}` = patient stone-dropper (tortoise-analog).
# `{hasty}` = impatient guesser who wants the answer without submitting
# (hare-analog). Both roles can be played by any of the three crows.
# Excludes pond/river locations — proximity to open water defuses the
# fable's core tension (the crow would simply drink from the river).
CROW_PITCHER_LOCATIONS = ("garden", "orchard", "farm", "market",
                           "village", "meadow", "road", "hilltop")

# Pronoun-neutral emotion pools for crow-pitcher.
CP_EMO_THIRSTY = (
    "beak parched from the long search",
    "throat dry with the afternoon's search",
    "wings heavy from circling without finding water",
    "eyes darting for any glint of water",
    "tired and parched from the long afternoon",
    "growing more desperate with each empty perch",
)
CP_EMO_PATIENT = (
    "calm and methodical",
    "dropping each stone with careful attention",
    "steady in the stone-by-stone approach",
    "unbothered by the slow progress",
    "trusting the stone-by-stone process",
    "unhurried with form after form",
    "patient as the water rose",
    "letting the count rise on its own",
    "watching the level lift",
    "deliberate and unhurried by the rising sun",
)
CP_EMO_PROUD = (
    "with a triumphant rattle of feathers",
    "head tilted confidently to one side",
    "ruffling up with certainty",
    "with a self-satisfied beak-click",
    "preening at the thought of knowing",
    "with a confident tilt of the head",
)


def _crows() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "crow")


def _pick_cp_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (clever, hasty) crow pair from the 200+ expanded
    crow name pool.

    `clever` is the patient evaluator (tortoise-analog): drops stones
    carefully, lets the REPL decide.
    `hasty` is the impatient guesser (hare-analog): wants the answer
    without submitting the form.
    """
    names = scene.rng.sample(char_pools.CROW_NAMES, 2)
    clever_gender = scene.rng.choice(("m", "f"))
    hasty_gender  = scene.rng.choice(("m", "f"))
    clever = _make_char(names[0], "crow", clever_gender,
                        ("evaluator", "patient"))
    hasty  = _make_char(names[1], "crow", hasty_gender,
                        ("guesser", "impatient"))
    return clever, hasty


def _pick_cp_location(scene: Scene) -> ont.Location:
    """Pick from outdoor locations natural for crow-pitcher."""
    cands = [l for l in ont.LOCATIONS if l.name in CROW_PITCHER_LOCATIONS]
    return scene.rng.choice(cands)


def _build_cp_placeholders(scene: Scene,
                           clever: ont.Character,
                           hasty: ont.Character,
                           location: ont.Location,
                           example: SubjectExample) -> dict:
    """Crow-pitcher placeholder dict.

    Exposes `{clever}` / `{hasty}` (and their suffix families) for
    crow-specific metaphor-pool templates, PLUS `{hare}` / `{tortoise}`
    aliases so the inherited `_GOAL_SUBPLOTS` and other shared templates
    from tortoise-hare render naturally. The mapping is:
      hasty  → hare-analog   (impatient guesser)
      clever → tortoise-analog (patient evaluator)
    """
    base = {
        "place":          place_phrase(scene, location),
        "location":       location.name,
        "form_display":   _format_form_display(example.form),
        "concept_phrase": example.concept_phrase,
        "what":           example.question_what,
        "goal_text":      example.goal_text,
        "scenario":       example.scenario,
        "need":           example.need,
        "mapping":        example.mapping,
        "resolution":     example.resolution,
        "emo_proud":      scene.rng.choice(CP_EMO_PROUD),
        "emo_patient":    scene.rng.choice(CP_EMO_PATIENT),
        "emo_tired":      scene.rng.choice(CP_EMO_THIRSTY),
        "emo_thirsty":    scene.rng.choice(CP_EMO_THIRSTY),
        "emo_content":    scene.rng.choice(CP_EMO_PATIENT),
        "emo_regretful":  scene.rng.choice(CP_EMO_THIRSTY),
        "emo_hungry":     scene.rng.choice(CP_EMO_THIRSTY),
    }
    for role, char in (("clever", clever), ("hasty", hasty)):
        base[role]                  = char.name
        base[f"{role}_phrase"]      = species_phrase(char)
        base[f"{role}_he_she"]      = char.he_she
        base[f"{role}_he_she_cap"]  = cap(char.he_she)
        base[f"{role}_his_her"]     = char.his_her
        base[f"{role}_him_her"]     = char.him_her
    # hare/tortoise aliases for compatibility with shared subplot templates
    base["hare"]                = hasty.name
    base["hare_phrase"]         = species_phrase(hasty)
    base["hare_he_she"]         = hasty.he_she
    base["hare_he_she_cap"]     = cap(hasty.he_she)
    base["hare_his_her"]        = hasty.his_her
    base["hare_him_her"]        = hasty.him_her
    base["tortoise"]            = clever.name
    base["tortoise_phrase"]     = species_phrase(clever)
    base["tortoise_he_she"]     = clever.he_she
    base["tortoise_he_she_cap"] = cap(clever.he_she)
    base["tortoise_his_her"]    = clever.his_her
    base["tortoise_him_her"]    = clever.him_her
    return base


# ── Milkmaid fable ─────────────────────────────────────────────────────
# The milkmaid carries her pail to market while dreaming of the wealth
# it will bring. The {milkmaid} is the dreamer/guesser (hare-analog);
# the {farmer} is the patient evaluator who insists on submitting the
# form first (tortoise-analog).
MILKMAID_LOCATIONS = ("road", "meadow", "hilltop",
                      "farm", "market", "orchard", "village")


def _mm_milkmaids() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS
                 if c.species == "human" and "dreamer" in c.role_classes)


def _mm_farmers() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS
                 if c.species == "human" and "farmer" in c.role_classes)


def _pick_mm_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick a fresh (milkmaid, farmer) pair from the 200+ expanded
    human pools.

    `milkmaid` is the dreamer/guesser (hare-analog) — young woman.
    `farmer`   is the patient evaluator (tortoise-analog) — older,
               m or f.
    """
    milkmaid_name = scene.rng.choice(char_pools.HUMAN_F)
    farmer_pool = (char_pools.HUMAN_ELDER_M if scene.rng.random() < 0.6
                   else char_pools.HUMAN_ELDER_F)
    farmer_gender = "m" if farmer_pool is char_pools.HUMAN_ELDER_M else "f"
    farmer_name = scene.rng.choice(farmer_pool)
    milkmaid = _make_char(milkmaid_name, "human", "f",
                          ("milkmaid", "dreamer"))
    farmer   = _make_char(farmer_name, "human", farmer_gender,
                          ("farmer", "evaluator"))
    return milkmaid, farmer


def _pick_mm_location(scene: Scene) -> ont.Location:
    """Pick from road / market / countryside locations natural for milkmaid."""
    cands = [l for l in ont.LOCATIONS if l.name in MILKMAID_LOCATIONS]
    return scene.rng.choice(cands)


def _build_mm_placeholders(scene: Scene,
                           milkmaid: ont.Character,
                           farmer:   ont.Character,
                           location: ont.Location,
                           example:  SubjectExample) -> dict:
    """Milkmaid placeholder dict.

    Provides both milkmaid-specific keys ({milkmaid}, {farmer} + variants)
    AND tortoise-hare aliases ({hare}, {tortoise} + variants) so shared
    subplot templates still render. Mapping: milkmaid → hare-analog
    (dreamer/guesser), farmer → tortoise-analog (patient evaluator).
    """
    return {
        # tortoise-hare aliases
        "hare":                 milkmaid.name,
        "tortoise":             farmer.name,
        "hare_phrase":          species_phrase(milkmaid),
        "tortoise_phrase":      species_phrase(farmer),
        "hare_he_she":          milkmaid.he_she,
        "tortoise_he_she":      farmer.he_she,
        "hare_he_she_cap":      cap(milkmaid.he_she),
        "tortoise_he_she_cap":  cap(farmer.he_she),
        "hare_his_her":         milkmaid.his_her,
        "tortoise_his_her":     farmer.his_her,
        "hare_him_her":         milkmaid.him_her,
        "tortoise_him_her":     farmer.him_her,

        # milkmaid-specific role names
        "milkmaid":             milkmaid.name,
        "milkmaid_phrase":      species_phrase(milkmaid),
        "milkmaid_he_she":      milkmaid.he_she,
        "milkmaid_he_she_cap":  cap(milkmaid.he_she),
        "milkmaid_his_her":     milkmaid.his_her,
        "milkmaid_him_her":     milkmaid.him_her,
        "farmer":               farmer.name,
        "farmer_phrase":        species_phrase(farmer),
        "farmer_he_she":        farmer.he_she,
        "farmer_he_she_cap":    cap(farmer.he_she),
        "farmer_his_her":       farmer.his_her,
        "farmer_him_her":       farmer.him_her,

        # place
        "place":                place_phrase(scene, location),
        "location":             location.name,

        # the example
        "form_display":         _format_form_display(example.form),
        "concept_phrase":       example.concept_phrase,
        "what":                 example.question_what,
        "goal_text":            example.goal_text,
        "scenario":             example.scenario,
        "need":                 example.need,
        "mapping":              example.mapping,
        "resolution":           example.resolution,

        # Emotions — milkmaid Cat-J lift draws from the integration
        # branch's emotion_pools (≥30 entries each, environment-anchored)
        # rather than the legacy 6-entry fables pools. This gives the
        # subplot prose access to phrases like "with eyes always on the
        # path" / "checking the path before setting her foot" that map
        # the milkmaid's emotional state to the algorithmic situation.
        # Polarity-aware: milkmaid is the daydreamer/guesser (boastful
        # / regretful when the pail tips); farmer is the patient
        # evaluator (patient / cautious).
        "emo_proud":            scene.rng.choice(emo_pools.EMO_PROUD),
        "emo_patient":          scene.rng.choice(emo_pools.EMO_PATIENT),
        "emo_tired":            scene.rng.choice(emo_pools.EMO_TIRED),
        "emo_content":          scene.rng.choice(emo_pools.EMO_CONTENT),
        "emo_regretful":        scene.rng.choice(emo_pools.EMO_REGRETFUL),
        "emo_hungry":           scene.rng.choice(emo_pools.EMO_HUNGRY),
        "emo_greedy":           scene.rng.choice(GE_EMO_GREEDY),
        "emo_boastful":         scene.rng.choice(emo_pools.EMO_BOASTFUL),
        "emo_cautious":         scene.rng.choice(emo_pools.EMO_CAUTIOUS),
        "emo_desperate":        scene.rng.choice(emo_pools.EMO_DESPERATE),
    }


# Dog-shadow uses two dogs: a wise hound (tortoise-analog) and a greedy
# dog (hare-analog, the protagonist who drops the real bone for its
# reflection). Locations are streamside / waterside settings where the
# reflection metaphor plays out.
DOG_SHADOW_LOCATIONS = ("river bank", "pond", "beach", "meadow",
                         "forest", "village", "road")


def _dogs() -> tuple[ont.Character, ...]:
    return tuple(c for c in ont.CHARACTERS if c.species == "dog")


def _pick_ds_chars(scene: Scene) -> tuple[ont.Character, ont.Character]:
    """Pick (hound, dog) — wise evaluator + greedy grabber — for dog-shadow.

    `hound` is the patient, wise character (tortoise-analog). `dog` is the
    hasty, greedy one who drops the real bone chasing a reflection
    (hare-analog).
    """
    names = scene.rng.sample(char_pools.DOG_NAMES, 2)
    hound_gender = scene.rng.choice(("m", "f"))
    dog_gender   = scene.rng.choice(("m", "f"))
    hound = _make_char(names[0], "dog", hound_gender,
                       ("evaluator", "patient"))
    dog   = _make_char(names[1], "dog", dog_gender,
                       ("greedy", "hasty"))
    return hound, dog


def _pick_ds_location(scene: Scene) -> ont.Location:
    """Pick from streamside + outdoor locations natural for dog-shadow."""
    cands = [l for l in ont.LOCATIONS if l.name in DOG_SHADOW_LOCATIONS]
    return scene.rng.choice(cands)


def _build_ds_placeholders(scene: Scene,
                            hound:    ont.Character,
                            dog:      ont.Character,
                            location: ont.Location,
                            example:  SubjectExample) -> dict:
    """Dog-shadow placeholder dict.

    Exposes `{dog}` / `{hound}` and pronoun variants, plus `{hare}` /
    `{tortoise}` aliases so shared subplot templates from
    `_SHARED_SUBPLOTS` (which still use the tortoise-hare names) render
    without modification. Mapping: greedy dog → hare-analog; wise hound →
    tortoise-analog.
    """
    return {
        # tortoise-hare aliases for shared subplot template compatibility
        "hare":              dog.name,
        "tortoise":          hound.name,
        "hare_phrase":       species_phrase(dog),
        "tortoise_phrase":   species_phrase(hound),
        "hare_he_she":       dog.he_she,
        "tortoise_he_she":   hound.he_she,
        "hare_he_she_cap":   cap(dog.he_she),
        "tortoise_he_she_cap": cap(hound.he_she),
        "hare_his_her":      dog.his_her,
        "tortoise_his_her":  hound.his_her,
        "hare_him_her":      dog.him_her,
        "tortoise_him_her":  hound.him_her,

        # dog-shadow cast
        "dog":               dog.name,
        "dog_phrase":        species_phrase(dog),
        "dog_he_she":        dog.he_she,
        "dog_he_she_cap":    cap(dog.he_she),
        "dog_his_her":       dog.his_her,
        "dog_him_her":       dog.him_her,
        "hound":             hound.name,
        "hound_phrase":      species_phrase(hound),
        "hound_he_she":      hound.he_she,
        "hound_he_she_cap":  cap(hound.he_she),
        "hound_his_her":     hound.his_her,
        "hound_him_her":     hound.him_her,

        # place
        "place":             place_phrase(scene, location),
        "location":          location.name,

        # example
        "form_display":      _format_form_display(example.form),
        "concept_phrase":    example.concept_phrase,
        "what":              example.question_what,
        "goal_text":         example.goal_text,
        "scenario":          example.scenario,
        "need":              example.need,
        "mapping":           example.mapping,
        "resolution":        example.resolution,

        # Emotions — dog-shadow Cat-J lift (slice QVez) draws from the
        # integration branch's emotion_pools (≥30 entries each,
        # environment-anchored) rather than the 6-entry legacy
        # fables pools. This widens LOW_GROUNDING coverage across
        # all dog-shadow records and adds the polarity-aligned
        # placeholders the templates need: hound (patient evaluator)
        # → emo_patient/emo_cautious/emo_content; dog (greedy/hasty)
        # → emo_greedy/emo_boastful/emo_desperate.
        "emo_proud":         scene.rng.choice(emo_pools.EMO_PROUD),
        "emo_patient":       scene.rng.choice(emo_pools.EMO_PATIENT),
        "emo_tired":         scene.rng.choice(emo_pools.EMO_TIRED),
        "emo_greedy":        scene.rng.choice(emo_pools.EMO_GREEDY),
        "emo_content":       scene.rng.choice(emo_pools.EMO_CONTENT),
        "emo_regretful":     scene.rng.choice(emo_pools.EMO_REGRETFUL),
        "emo_boastful":      scene.rng.choice(emo_pools.EMO_BOASTFUL),
        "emo_cautious":      scene.rng.choice(emo_pools.EMO_CAUTIOUS),
        "emo_desperate":     scene.rng.choice(emo_pools.EMO_DESPERATE),
        "emo_hungry":        scene.rng.choice(emo_pools.EMO_HUNGRY),
        "emo_suspicious":    scene.rng.choice(emo_pools.EMO_SUSPICIOUS),
    }


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
    """Pick a fresh (shepherd, elder) pair from the 200+ expanded
    human pools.

    `shepherd` is the boy/young-shepherd (hare-analog dreamer).
    `elder`    is the village elder (tortoise-analog evaluator).
    """
    shepherd_gender = scene.rng.choice(("m", "f"))
    shepherd_pool = (char_pools.HUMAN_M if shepherd_gender == "m"
                     else char_pools.HUMAN_F)
    shepherd_name = scene.rng.choice(shepherd_pool)
    elder_gender = scene.rng.choice(("m", "f"))
    elder_pool = (char_pools.HUMAN_ELDER_M if elder_gender == "m"
                  else char_pools.HUMAN_ELDER_F)
    elder_name = scene.rng.choice(elder_pool)
    while elder_name == shepherd_name:
        elder_name = scene.rng.choice(elder_pool)
    shepherd = _make_char(shepherd_name, "human", shepherd_gender,
                          ("shepherd", "dreamer"))
    elder    = _make_char(elder_name, "human", elder_gender,
                          ("elder", "evaluator"))
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
                        primary: ont.Character,
                        secondary: ont.Character,
                        location: ont.Location,
                        example: SubjectExample,
                        fable: str = "tortoise-hare") -> dict:
    """Assemble the {placeholder: value} dict that subplot templates use.

    The two characters are exposed under fable-specific role names so
    the same placeholder builder serves every fable additively. For
    tortoise-hare the role names are `hare` / `tortoise`; for
    ant-grasshopper they are `ant` / `grasshopper`. Each role exposes
    the standard suffix family: `_phrase`, `_he_she`, `_he_she_cap`,
    `_his_her`, `_him_her`.
    """
    # Pick fable-specific role labels for the two characters.
    if fable == "ant-grasshopper":
        primary_role, secondary_role = "ant", "grasshopper"
    else:
        # tortoise-hare default — preserves the existing call shape.
        primary_role, secondary_role = "hare", "tortoise"

    base: dict = {
        # place
        "place":           place_phrase(scene, location),
        "location":        location.name,

        # the example
        "form_display":    _format_form_display(example.form),
        "concept_phrase":  example.concept_phrase,
        "what":            example.question_what,
        "goal_text":       example.goal_text,
        # story-scaffold slots (Phase C). Empty when the example
        # has no story authored; templates that use them should
        # be tagged fits_tags=("story",).
        "scenario":        example.scenario,
        "need":            example.need,
        "mapping":         example.mapping,
        "resolution":      example.resolution,

        # emotions — single picks. The pool covers ant-grasshopper's
        # natural emotional palette (content/proud/regretful/tired/hungry)
        # plus tortoise-hare's (proud/patient/tired). Adding extra keys
        # is harmless — Python format() ignores unused keys.
        "emo_proud":       scene.rng.choice(EMO_PROUD),
        "emo_patient":     scene.rng.choice(EMO_PATIENT),
        "emo_tired":       scene.rng.choice(EMO_TIRED),
        "emo_content":     scene.rng.choice(EMO_CONTENT),
        "emo_regretful":   scene.rng.choice(EMO_REGRETFUL),
        "emo_hungry":      scene.rng.choice(EMO_HUNGRY),
    }

    # Expose each character under its fable-specific role name with the
    # standard suffix family. `primary` is conventionally the
    # protagonist of the fable's moral (the one who gets it right —
    # tortoise / ant); `secondary` is the foil (hare / grasshopper).
    # NOTE: tortoise-hare passed (hare, tortoise) historically, so the
    # primary/secondary naming is generic but the roles map correctly:
    # for tortoise-hare, primary=hare and secondary=tortoise; this is
    # preserved exactly to keep all existing tortoise-hare templates
    # rendering identically.
    for role, char in ((primary_role, primary), (secondary_role, secondary)):
        base[role]                  = char.name
        base[f"{role}_phrase"]      = species_phrase(char)
        base[f"{role}_he_she"]      = char.he_she
        base[f"{role}_he_she_cap"]  = cap(char.he_she)
        base[f"{role}_his_her"]     = char.his_her
        base[f"{role}_him_her"]     = char.him_her

    if fable == "boy-wolf":
        # Slot A (primary) → the SHEPHERD (the boy who cries wolf — the
        # cautionary character). Slot B (secondary) → the ELDER /
        # VILLAGER (the corrective voice).
        #
        # Boy-wolf overrides the EMO pools with gender-neutral
        # fable-flavored variants (BW_EMO_*) to avoid race imagery and
        # gendered phrases from the shared pool that don't fit the
        # boy-wolf valley setting.
        from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
            BW_EMO_PROUD, BW_EMO_PATIENT, BW_EMO_TIRED,
            BW_EMO_REGRETFUL, BW_EMO_DESPERATE,
        )
        base.update({
            "shepherd":             primary.name,
            "shepherd_phrase":      species_phrase(primary),
            "shepherd_he_she":      primary.he_she,
            "shepherd_he_she_cap":  cap(primary.he_she),
            "shepherd_his_her":     primary.his_her,
            "shepherd_him_her":     primary.him_her,

            "elder":                secondary.name,
            "elder_phrase":         species_phrase(secondary),
            "elder_he_she":         secondary.he_she,
            "elder_he_she_cap":     cap(secondary.he_she),
            "elder_his_her":        secondary.his_her,
            "elder_him_her":        secondary.him_her,

            "villager":             secondary.name,
            "villager_phrase":      species_phrase(secondary),
            "villager_he_she":      secondary.he_she,
            "villager_he_she_cap":  cap(secondary.he_she),
            "villager_his_her":     secondary.his_her,
            "villager_him_her":     secondary.him_her,

            # Override the shared EMO_* picks with gender-neutral
            # boy-wolf-specific pools.
            "emo_proud":       scene.rng.choice(BW_EMO_PROUD),
            "emo_patient":     scene.rng.choice(BW_EMO_PATIENT),
            "emo_tired":       scene.rng.choice(BW_EMO_TIRED),
            "emo_regretful":   scene.rng.choice(BW_EMO_REGRETFUL),
            "emo_desperate":   scene.rng.choice(BW_EMO_DESPERATE),
        })
        # Fix-set 2 (ju2R): when goal_text is empty (atom subjects),
        # avoid the EMPTY_GOAL_RENDERED bug where templates like
        # "To {goal_text}, X composed Y" render as "To , X composed Y".
        # Substitute a type-generic fallback that keeps the prefix
        # well-formed without leaking the form's literals (FORM_LEAK).
        if not (example.goal_text or "").strip():
            f = (example.form or "").strip()
            if not f.startswith("("):
                base["goal_text"] = "evaluate the literal"
            else:
                head = f[1:].split(None, 1)[0] if len(f) > 1 else ""
                if head in {"=", "not=", "<", ">", "<=", ">=",
                             "zero?", "pos?", "neg?", "nil?", "true?",
                             "false?", "symbol?", "keyword?", "string?",
                             "number?", "boolean?", "vector?", "list?",
                             "map?", "set?", "seq?", "coll?",
                             "even?", "odd?", "empty?", "some?", "any?",
                             "every?", "contains?", "instance?"}:
                    base["goal_text"] = "evaluate the predicate"
                elif head in {"and", "or", "not"}:
                    base["goal_text"] = "evaluate the boolean form"
                elif head in {"if", "when", "cond", "case"}:
                    base["goal_text"] = "evaluate the conditional form"
                else:
                    base["goal_text"] = "evaluate the form"

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
        "goal_text":       example.goal_text,
        # story-scaffold slots (Phase C); see the same block in
        # the tortoise-hare branch above.
        "scenario":        example.scenario,
        "need":            example.need,
        "mapping":         example.mapping,
        "resolution":      example.resolution,

        # emotions (pronoun-neutral pools so any character gender works)
        "emo_proud":       scene.rng.choice(EMO_PROUD),
        "emo_patient":     scene.rng.choice(EMO_PATIENT),
        "emo_tired":       scene.rng.choice(EMO_TIRED),
        "emo_greedy":      scene.rng.choice(GE_EMO_GREEDY),
        "emo_content":     scene.rng.choice(GE_EMO_CONTENT),
        "emo_regretful":   scene.rng.choice(GE_EMO_REGRETFUL),
    }


def _render_question(scene: Scene, example: SubjectExample,
                     question_what: str | None = None) -> str:
    """The closing line of the user_msg. Always asks the student to
    write a Clojure expression that produces the answer.

    If question_what already ends with ``?`` (often because the author
    references a predicate by name — ``contains?`` / ``empty?`` /
    ``zero?``), strip the trailing ``?`` before appending framing
    punctuation. Otherwise the rendered text reads ``... using
    contains?? Submit ...`` (PREDICATE_QUESTION_COLLISION).
    """
    qw = question_what if question_what is not None else example.question_what
    # Strip trailing ``?`` so the framing's own ``?`` or ``.`` doesn't
    # collide with the predicate-name suffix.
    qw = qw.rstrip().rstrip('?').rstrip()
    framings = (
        f"Write a Clojure expression that computes {qw}.",
        f"Write a form whose evaluation gives {qw}.",
        f"What Clojure form computes {qw}? Submit it via `eval`.",
        f"Question: write a Clojure expression for {qw}.",
    )
    return scene.rng.choice(framings)


# ─────────────────────── parametric draw + verify ───────────────────────


class VerifierMismatch(Exception):
    """Raised when a parametric draw's evaluator answer doesn't match
    the schema's expected_fn(draws). Indicates either a buggy
    expected_fn or a form_template / pool combination that the
    evaluator can't handle."""


def _draw_and_verify(example: SubjectExample,
                     scene: Scene,
                     max_rerolls: int = 8) -> tuple[str, object, dict]:
    """Render the parametric form, evaluate it, and confirm the answer
    matches expected_fn(draws). Returns (form_str, expected, draws).

    Re-rolls up to `max_rerolls` times on transient ConstraintFailure
    (predicate couldn't fire); raises VerifierMismatch on a true
    answer mismatch.
    """
    from mmllm.aesop.curriculum.scalar_pools import (
        render_form, ConstraintFailure,
    )
    from mmllm.aesop.curriculum.form_parser import parse
    from mmllm.aesop.expr import evaluate

    last_err = None
    for attempt in range(max_rerolls):
        try:
            form_str, draws = render_form(
                example.form_template, example.slots, scene.rng)
        except ConstraintFailure as e:
            last_err = e
            continue
        try:
            ast = parse(form_str)
            got = evaluate(ast)
        except Exception as e:
            raise VerifierMismatch(
                f"parse/eval failure on {form_str!r}: {e}") from e
        want = example.expected_fn(draws)
        if got != want:
            # Try a tolerant compare for keyword/list normalization.
            from mmllm.aesop.expr import _eval_v  # noqa: F401
            if _values_equal(got, want):
                return form_str, want, draws
            raise VerifierMismatch(
                f"answer mismatch on {form_str!r}: "
                f"got {got!r}, want {want!r} (draws={draws!r})")
        return form_str, want, draws
    raise VerifierMismatch(
        f"could not satisfy slot constraints in {max_rerolls} re-rolls: "
        f"last_err={last_err!r}")


def _values_equal(a, b) -> bool:
    """Tolerant equality for evaluator outputs vs author intent.
    Normalizes keyword sentinels and dict key types."""
    if isinstance(a, str) and a.startswith(":"):
        a = ("__kw__", a[1:])
    if isinstance(b, str) and b.startswith(":"):
        b = ("__kw__", b[1:])
    if isinstance(a, list) and isinstance(b, list):
        return (len(a) == len(b)
                and all(_values_equal(x, y) for x, y in zip(a, b)))
    if isinstance(a, dict) and isinstance(b, dict):
        if set(_norm_key(k) for k in a) != set(_norm_key(k) for k in b):
            return False
        an = {_norm_key(k): v for k, v in a.items()}
        bn = {_norm_key(k): v for k, v in b.items()}
        return all(_values_equal(an[k], bn[k]) for k in an)
    return a == b


def _norm_key(k):
    if isinstance(k, str) and k.startswith(":"):
        return ("__kw__", k[1:])
    return k


def _interpolate_drawn(text: str, draws: dict) -> str:
    """Substitute `{drawn.<slot>}` tokens in narrative text with prose
    renderings of drawn values. Other `{...}` placeholders are left
    intact for the subplot template's own format pass."""
    if not text or "{drawn." not in text:
        return text
    from mmllm.aesop.curriculum.scalar_pools import POOLS, Slot
    out = text
    for sname, value in draws.items():
        token = "{drawn." + sname + "}"
        if token not in out:
            continue
        # Use prose rendering. Pool name resolution: we don't have the
        # slot here directly, so fall back to str() if value is a
        # primitive. For collections, render English.
        if isinstance(value, list):
            if len(value) == 0:    s = "an empty list"
            elif len(value) == 1:  s = str(value[0])
            elif len(value) == 2:  s = f"{value[0]} and {value[1]}"
            else:
                s = ", ".join(str(v) for v in value[:-1]) + f", and {value[-1]}"
        elif isinstance(value, str) and value.startswith(":"):
            s = value[1:]
        elif isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
            s = value[1]
        elif isinstance(value, tuple) and len(value) == 2 and value[1] != 0:
            # Ratio
            s = f"{value[0]}/{value[1]}"
        else:
            s = str(value)
        out = out.replace(token, s)
    return out


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
    primary = secondary = None
    if sub.fable == "goose-eggs":
        owner, visitor, goose = _pick_ge_chars(scene)
        location = _pick_ge_location(scene)
        primary, secondary = owner, visitor
        placeholders_fn = lambda ex: _build_ge_placeholders(
            scene, owner, visitor, goose, location, ex)
    elif sub.fable == "ant-grasshopper":
        primary, secondary = _pick_ag_chars(scene)
        location = _pick_ag_location(scene)
        placeholders_fn = lambda ex: _build_placeholders(
            scene, primary, secondary, location, ex, sub.fable)
    elif sub.fable == "crow-pitcher":
        clever, hasty = _pick_cp_chars(scene)
        location = _pick_cp_location(scene)
        primary, secondary = clever, hasty
        placeholders_fn = lambda ex: _build_cp_placeholders(
            scene, clever, hasty, location, ex)
    elif sub.fable == "milkmaid":
        milkmaid, farmer = _pick_mm_chars(scene)
        location = _pick_mm_location(scene)
        primary, secondary = milkmaid, farmer
        placeholders_fn = lambda ex: _build_mm_placeholders(
            scene, milkmaid, farmer, location, ex)
    elif sub.fable == "boy-wolf":
        primary, secondary = _pick_bw_chars(scene)
        location = _pick_bw_location(scene)
        placeholders_fn = lambda ex: _build_placeholders(
            scene, primary, secondary, location, ex, fable=sub.fable)
    elif sub.fable == "dog-shadow":
        hound, dog = _pick_ds_chars(scene)
        location = _pick_ds_location(scene)
        primary, secondary = hound, dog
        placeholders_fn = lambda ex: _build_ds_placeholders(
            scene, hound, dog, location, ex)
    else:
        # tortoise-hare default
        hare, tortoise = _pick_th_chars(scene)
        location = _pick_th_location(scene)
        primary, secondary = hare, tortoise
        placeholders_fn = lambda ex: _build_placeholders(
            scene, hare, tortoise, location, ex)

    intro = _curriculum_intro(scene, sub.fable, location, primary, secondary)

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

    # Parametric draw + verify (when example has form_template).
    # This produces a fresh (form, expected, draws) triple per record;
    # legacy examples without a template fall through to static
    # form/expected from authoring time.
    if example.form_template:
        rendered_form, rendered_expected, draws = _draw_and_verify(
            example, scene)
    else:
        rendered_form     = example.form
        rendered_expected = example.expected
        draws             = {}

    # Build placeholders. We pass a "slot-aware" example so subplot
    # templates that reference {form_display}, {concept_phrase},
    # {goal_text}, scenario/need/mapping/resolution see the
    # drawn-value-interpolated versions.
    if draws:
        slot_example = _example_with_draws(example, rendered_form,
                                           rendered_expected, draws)
    else:
        slot_example = example
    placeholders = placeholders_fn(slot_example)
    body = subplot.template.format(**placeholders).strip()
    question_what = _interpolate_drawn(slot_example.question_what, draws)
    question = _render_question(scene, slot_example, question_what)

    user_msg = f"{intro}{body}\n\n{question}"

    # Eval-first tool call: form is the Clojure source the model produces.
    calls    = build_tool_calls(value=rendered_expected,
                                form_str=rendered_form,
                                prefer_eval=True)
    sys_msg  = system_prompt(use_eval=True)
    # Plan pool: prefer the expanded 30-entry per-fable pool over the
    # subject's own plan_pool (which is 4-6 entries). The subject's
    # plan_pool, if set, gets folded in as additional candidates.
    expanded_plans = _FABLE_PLAN_POOL.get(sub.fable, ())
    plan_candidates = list(expanded_plans) + list(sub.plan_pool or ())
    plan = scene.rng.choice(plan_candidates) if plan_candidates else ""
    if "{primary}" in plan or "{secondary}" in plan:
        try:
            plan = plan.format(
                primary=primary.name if primary else "",
                secondary=secondary.name if secondary else "")
        except (KeyError, AttributeError):
            pass
    plan = _interpolate_drawn(plan, draws) if draws else plan
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
        expected=rendered_expected,
        code_str=rendered_form,
        fable=sub.fable,
        chapter=sub.subject_id,
        catalog=ANSWER_AND_EVAL,
    )


def _example_with_draws(ex: SubjectExample,
                        form_str: str,
                        expected: object,
                        draws: dict) -> SubjectExample:
    """Return a shallow copy of `ex` with form/expected replaced by
    the rendered values, and concept_phrase / question_what /
    goal_text / scenario / need / mapping / resolution all
    drawn-value-interpolated."""
    return SubjectExample(
        form           = form_str,
        expected       = expected,
        concept_phrase = _interpolate_drawn(ex.concept_phrase, draws),
        question_what  = _interpolate_drawn(ex.question_what,  draws),
        goal_text      = _interpolate_drawn(ex.goal_text,      draws),
        scenario       = _interpolate_drawn(ex.scenario,       draws),
        need           = _interpolate_drawn(ex.need,           draws),
        mapping        = _interpolate_drawn(ex.mapping,        draws),
        resolution     = _interpolate_drawn(ex.resolution,     draws),
        tags           = ex.tags,
        # Keep template fields in case the rest of the pipeline
        # introspects them, but they're not used post-draw.
        form_template  = ex.form_template,
        slots          = ex.slots,
        expected_fn    = ex.expected_fn,
        bb_verify      = ex.bb_verify,
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
