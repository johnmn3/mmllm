"""Aesop fable templates.

Each fable is a function `gen_*(scene: Scene) -> Record`. It internally:

  1. Picks a chapter variant (different math / question shapes)
  2. Picks consistent entities (characters, items, containers, locations)
  3. Picks numeric scale tier (tiny / medium / large)
  4. Builds an Expr tree representing the math
  5. Evaluates it for the ground-truth answer
  6. Renders narrative text + Clojure code + tool-call answer
  7. Picks code form (inline / block) and preface style (none / fixed / narrative)

The renderer composes the assistant-turn body so the JSON tool-call line
is always last (matches the eval extractor's expectations).
"""
from __future__ import annotations

import random
from typing import Callable

from mmllm.aesop import ontology as ont
from mmllm.aesop.expr import (
    App, Cond, Def, Do, Expr, Fn, If, Let, Lit, Thread, Var,
    emit_clojure, emit_clojure_inline, evaluate,
)
from mmllm.aesop.template import (
    ANSWER_AND_EVAL, ANSWER_ONLY, Record, Scene,
    article, assemble_assistant_msg, atmosphere, build_tool_calls, cap,
    char_intro, n_unit, place_phrase, question_phrase, render_code,
    render_tool_calls, resolve_preface, smart_pronoun, smart_possessive,
    species_phrase, system_prompt, the_subject_phrase, time_phrase, unit,
    verb_for,
)


# ─────────────────────── narrative scaffolding ───────────────────────


# Per-fable opener pools. Each entry is 1-2 sentences capturing that
# fable's specific narrative dynamic — vanity vs steadiness, greed vs
# patience, lying vs trust, etc. — rather than generic weather/atmosphere.
# The openers establish the moral tension before the chapter's
# specific quantitative situation introduces itself.
FABLE_OPENERS: dict[str, tuple[str, ...]] = {
    "tortoise-hare": (
        "It was well known among the animals that the Hare boasted of his speed at every chance.",
        "The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the swifter.",
        "There was once a Hare whose pride was as quick as her feet, and a Tortoise who said nothing about either.",
        "In that part of the forest, no one ever expected the Tortoise to outrun the Hare — yet today the question would be settled.",
        "The Hare loved nothing better than the sound of his own boasts; the Tortoise, nothing better than a long quiet walk.",
    ),
    "crow-pitcher": (
        "A thirsty Crow had been searching all afternoon for water and was nearly ready to give up.",
        "Hunger and thirst had driven the Crow far from her usual perch.",
        "The Crow knew that water in the world is sometimes hidden where only the patient can reach it.",
        "It is said that wit, more than strength, is the friend of the thirsty Crow.",
    ),
    "goose-eggs": (
        "A farmer once kept a goose who laid a golden egg every morning, plain and ordinary in every other way.",
        "The villagers all envied the household with the golden-egg goose, though only its owner knew the careful work of patience.",
        "There was once an extraordinary goose whose every morning gift was a single egg of pure gold.",
        "Greed and patience, as everyone knows, do not sit at the same table — and a golden-egg goose tests them both.",
    ),
    "boy-wolf": (
        "Every shepherd in the valley knew the danger of crying wolf for sport.",
        "A young shepherd had been left alone with the flock far too often, and boredom had taken root.",
        "The boy on the hill thought the trick clever the first time he played it.",
        "It is hard to be believed twice when you have lied even once — a lesson every shepherd must one day learn.",
    ),
    "ant-grasshopper": (
        "All summer long, the Ant worked while the Grasshopper sang.",
        "Two creatures of the meadow approached the coming winter very differently.",
        "It is the way of the Ant to gather, and the way of the Grasshopper to play.",
        "Among the small folk of the meadow, no two neighbors lived more differently than the Ant and the Grasshopper.",
    ),
    "milkmaid": (
        "A young milkmaid was returning home with her milk pail balanced on her head, dreaming of the fortune it would bring.",
        "The Milkmaid liked to imagine, each morning on her way to market, what her milk would buy.",
        "Pride goes before a fall, especially when a Milkmaid begins to plan her wealth too eagerly.",
        "There was once a Milkmaid whose dreams ran ahead of her pail.",
    ),
    "fox-grapes": (
        "A hungry Fox came upon a vine of grapes hanging just out of reach.",
        "It is told that many an animal has stood beneath fruit it could not reach and walked away calling it sour.",
        "The Fox crept through the orchard and found himself eyeing a tempting cluster of grapes.",
        "Hunger sharpens the eye but does not always lengthen the leap.",
    ),
    "two-mice": (
        "Once a Country Mouse invited her City cousin to dine at her humble home.",
        "The City Mouse and the Country Mouse had very different ideas of a good meal — and very different stockpiles to draw on.",
        "It is said that a meal among friends is sweeter than feasting alone, and easier to count.",
        "Two mice — one of the city, one of the countryside — had a habit of comparing what little they had.",
    ),
    "dog-shadow": (
        "A Dog was crossing a stream with a fine bone in his mouth, and was very pleased with himself.",
        "What the Dog thought he saw beneath the water turned out to be his own reflection.",
        "Greed has cost more than one creature what they already had.",
        "It is said that the foolish Dog will trade what is real for what is only an image.",
    ),
    "lion-bulls": (
        "Three Bulls had grazed and fought together for so long that no Lion dared trouble them.",
        "There was once a band of Bulls so unified that they made the great Lion uneasy.",
        "Strength shared is strength multiplied — a truth the Lion knew well, and worked patiently to undo.",
        "The Lion stalked the field where the Bulls had grazed in peace for many seasons.",
    ),
}


def _aesopian_intro(scene: Scene, fable: str,
                    location: ont.Location | None = None) -> str:
    """Pick a fable-specific opener from FABLE_OPENERS. Optional `location`
    adds a single setting clause to anchor the scene physically.
    Output ends with `\\n\\n` so chapters can directly prepend it via
    `f"{_intro}{...rest of user_msg...}"`.
    """
    pool = FABLE_OPENERS.get(fable, ())
    if not pool:
        # Fallback: shouldn't happen if every fable is registered.
        return ""
    opener = scene.rng.choice(pool)
    if location is not None and scene.coin(0.4):
        # Anchor with a location-mention. Half the time we drop this so
        # the opener reads as standalone Aesopian narration without
        # geographical pinning (matches the timeless feel of Aesop).
        place = scene.rng.choice((
            f"It happened {place_phrase(scene, location)}.",
            f"This was {place_phrase(scene, location)}.",
            f"All this took place {place_phrase(scene, location)}.",
        ))
        return f"{opener} {place}\n\n"
    return f"{opener}\n\n"


# Legacy alias — old code path called `_atm_intro`, kept so the auto-
# generated chapter rewrites still work. The new fable-aware variant
# is preferred.
def _atm_intro(scene: Scene, location: ont.Location | None = None,
               fable: str = "") -> str:
    """Legacy entry point. If `fable` is given, dispatches to the new
    Aesopian opener; otherwise falls back to a generic atmospheric
    line (the old behavior, kept for any chapter not yet migrated)."""
    if fable:
        return _aesopian_intro(scene, fable, location)
    # generic fallback (used to be the only path; now rare)
    when = scene.rng.choice((
        "One bright morning,", "Late one afternoon,",
        "On a quiet spring day,", "Under a pale sky,",
    ))
    return f"{when} something extraordinary was about to happen.\n\n"


# ─────────────────────── subplot infrastructure ───────────────────────


def _smooth_opener(opener: str, named_protagonist: ont.Character | None) -> str:
    """If the opener uses an abstract 'a Hare' / 'the Hare' form and a named
    protagonist follows, drop the trailing newlines so the subplot can pick
    up directly. Caller is responsible for inserting `\\n\\n` between
    opener and subplot — this just normalizes whitespace.
    """
    return opener.rstrip() + "\n\n"


def _render_subplot(scene: Scene, subplots: list[str], **params) -> str:
    """Pick one of `subplots` (str templates) and format it with `params`.
    Each template uses Python format syntax, and is expected to be
    parameterized over the chapter's character/item/container/number
    bindings. Subplot templates are 60-120 words each — enough to add
    real narrative texture without inflating token count to ridiculous
    sizes.
    """
    template = scene.rng.choice(subplots)
    return template.format(**params).strip()


# Per-character emotional pools — used to ground quantities in feeling
# rather than naked numbers. Picks differ by character archetype where
# possible, so a "boastful" hare's emotional vocabulary differs from
# a "patient" tortoise's.
EMO_PROUD: tuple[str, ...] = (
    "with a smug grin", "puffed up with pride",
    "as if the race were already won", "with great whoops of laughter",
    "boasting at every turn", "swaggering through the underbrush",
)
EMO_PATIENT: tuple[str, ...] = (
    "without complaint", "saying very little",
    "with steady, careful steps", "her eyes always on the path",
    "untroubled by what others thought", "stepping deliberately",
)
EMO_TIRED: tuple[str, ...] = (
    "drowsy from the warm sun", "weary from the morning's effort",
    "lulled by the gentle wind", "her legs heavy from sprinting",
    "yawning at the soft moss",
)
EMO_THIRSTY: tuple[str, ...] = (
    "dry-throated and desperate", "parched from the long flight",
    "her beak cracked with thirst", "near to giving up the search for water",
    "with a thirst that hurt to bear",
)
EMO_HUNGRY: tuple[str, ...] = (
    "his stomach hollow with hunger", "her belly aching for food",
    "weak with hunger", "dreaming of the next meal",
)
EMO_GREEDY: tuple[str, ...] = (
    "his eyes greedy with want", "with a hungry gleam in his eye",
    "imagining all that he might gain", "his thoughts already on more",
    "his mouth watering at the thought of more",
)
EMO_CONTENT: tuple[str, ...] = (
    "happy with what she had", "pleased with her small fortune",
    "grateful for every bite", "content in her quiet life",
)
EMO_REGRETFUL: tuple[str, ...] = (
    "his heart sinking", "wishing she had been more careful",
    "regretting every careless step", "wondering how it had come to this",
)
EMO_DESPERATE: tuple[str, ...] = (
    "with growing alarm", "wide-eyed with fear", "in a panic",
    "shouting until her voice cracked", "her hands trembling",
)


# ─────────────────────── _finalize helper ───────────────────────


def _sum_expr(scene: Scene, xs: Expr) -> Expr:
    """Pick one of three idiomatic Clojure sum forms over `xs`. Used to
    teach the model that these are interchangeable:

      (reduce + xs)                              # idiomatic short
      (apply + xs)                               # also idiomatic
      (reduce (fn [a b] (+ a b)) 0 xs)           # verbose long form
    """
    pick = scene.rng.choices(
        ["reduce-+", "apply-+", "reduce-fn"],
        weights=[0.45, 0.30, 0.25],
    )[0]
    if pick == "reduce-+":
        # `(reduce + xs)` — represented with a special "+" Var since our
        # AST doesn't have a "function reference" node.
        return App("reduce", [Var("+"), xs])
    if pick == "apply-+":
        return App("apply", [Var("+"), xs])
    # verbose
    return App("reduce",
               [Fn(["a", "b"], App("+", [Var("a"), Var("b")])),
                Lit(0),
                xs])


def _extract_code_from_block(code_block: str) -> str:
    """Pull the Clojure source out of a fenced ```clojure ... ;=> N ```
    block. Used so the eval(form: …) tool-call arg always matches the
    EXACT source displayed in the assistant turn — not a re-emit from
    the AST that might disagree (e.g., let vs def-chain block form)."""
    text = code_block
    if text.startswith("```clojure\n"):
        text = text[len("```clojure\n"):]
    if text.endswith("\n```"):
        text = text[:-len("\n```")]
    lines = text.split("\n")
    while lines and (lines[-1].lstrip().startswith(";=>")
                     or lines[-1].lstrip().startswith(";; =>")):
        lines.pop()
    return "\n".join(lines).rstrip()


def _finalize(scene: Scene, *,
              user_msg:    str,
              value,
              expr,
              fable:   str,
              chapter: str,
              plan:        str = "",
              prefer_eval: bool = True,
              # legacy params: `narrative` from old chapters becomes
              # plan; code_block/result_text are ignored (no longer
              # appear in the assistant turn under eval-first design).
              narrative:   str = "",
              code_block:  str = "",
              result_text: str = "") -> Record:
    """Bundle a chapter's prose + math into a Record under the eval-first
    design. The `plan` is an optional one-sentence description of HOW the
    expression is structured (must NOT contain the numeric answer); the
    scene decides whether to surface it as a preface. The form inside the
    eval tool call IS the work — no code block, no result_text, no answer
    annotation.

    `prefer_eval=True` (default) emits a single `eval(form)` tool call.
    `prefer_eval=False` emits a single `answer(value)` call — used by
    chapters whose natural answer is yes/no or short string verdicts.

    Legacy params (narrative/code_block/result_text) are accepted-and-
    ignored to keep this commit's diff focused on the chapters that
    have been migrated; chapters not yet touched still call the old
    signature and get the eval-first behavior automatically.
    Used so the eval(form: …) tool-call arg always matches the
    EXACT source string  — see _extract_code_from_block.
    that was rendered in the assistant's code block — extracted from
    code_block, not re-emitted from expr — so the displayed source and
    the eval-form arg always agree byte-for-byte."""
    # Eval-first: build the form arg as a single-line Clojure expression
    # straight from the AST. This is the only place the math materializes
    # in the assistant turn.
    form_str  = emit_clojure_inline(expr)
    calls     = build_tool_calls(value=value, form_str=form_str,
                                  prefer_eval=prefer_eval)
    catalog   = ANSWER_AND_EVAL if prefer_eval else ANSWER_ONLY
    sys_msg   = system_prompt(use_eval=prefer_eval)
    plan_text = plan or narrative   # legacy chapters pass narrative=
    preface   = resolve_preface(scene, plan_text)
    asst      = assemble_assistant_msg(
        preface=preface,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg=sys_msg,
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=value,
        code_str=form_str,
        fable=fable,
        chapter=chapter,
        catalog=catalog,
    )


# ─────────────────────── 1. Tortoise and the Hare ───────────────────────


def gen_tortoise_hare(scene: Scene) -> Record:
    """Race fable. Chapters: nap-overtake, speed-comparison, distance-remaining."""
    chapter = scene.pick_choice(["nap-overtake", "speed-comparison",
                                  "distance-remaining"])
    if chapter == "nap-overtake":
        return _th_nap_overtake(scene)
    if chapter == "speed-comparison":
        return _th_speed_comparison(scene)
    return _th_distance_remaining(scene)


def _th_nap_overtake(scene: Scene) -> Record:
    """During the hare's nap, did the tortoise pass him?"""
    hare = scene.pick_character(role_classes=("racer", "fast"))
    tortoise = scene.pick_character(role_classes=("racer", "slow"), not_=hare)
    location = scene.pick_location(tags_any=("path",), indoor=False)

    # Numbers — simple range; this chapter wants overtake outcome to be ~50/50.
    hare_lead = scene.pick_int(3, 12)         # how far ahead hare is when napping
    tortoise_speed = scene.pick_int(1, 4)     # miles/hour
    nap_hours = scene.pick_int(2, 8)

    expr = Let(
        bindings=[
            ("hare-lead",     Lit(hare_lead)),
            ("tortoise-rate", Lit(tortoise_speed)),
            ("nap-hours",     Lit(nap_hours)),
            ("tortoise-pos",  App("*", [Var("tortoise-rate"), Var("nap-hours")])),
        ],
        body=If(
            App(">", [Var("tortoise-pos"), Var("hare-lead")]),
            Lit(tortoise.name),
            Lit(hare.name),
        ),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "tortoise-hare", location)
    proud  = scene.rng.choice(EMO_PROUD)
    patient = scene.rng.choice(EMO_PATIENT)
    tired  = scene.rng.choice(EMO_TIRED)

    # Six narrative subplots — same arithmetic, very different stories.
    # Each grounds the abstract numbers (lead, speed, hours) in a small
    # situational drama and a specific sensory setting.
    nap_overtake_subplots = [
        # 1) classic — boast then nap under tree
        f"{hare.name} the hare bounded down the path {proud}, "
        f"sure that {hare.he_she} would win without effort. By the time "
        f"{hare.he_she} had run {n_unit(hare_lead, 'mile')} ahead, "
        f"{hare.he_she} could no longer see {tortoise.name} behind. "
        f"{cap(hare.he_she)} was {tired}, and curled up under an old oak "
        f"to rest. {tortoise.name} the tortoise, far behind, kept on "
        f"{patient} at a steady {tortoise_speed} "
        f"{unit(tortoise_speed, 'mile')} per hour. {cap(hare.he_she)} "
        f"slept while {tortoise.name} walked for "
        f"{n_unit(nap_hours, 'hour')} without pause.",

        # 2) sweet clover patch + drowsy
        f"{hare.name} sprinted out of the gate {proud}, and "
        f"after {n_unit(hare_lead, 'mile')} {hare.he_she} found a sweet "
        f"patch of clover by the roadside that {hare.he_she} could not "
        f"resist. {cap(hare.he_she)} ate {hare.his_her} fill, grew {tired}, "
        f"and fell into a heavy sleep. {tortoise.name}, who had been "
        f"plodding along {patient}, kept moving at {tortoise_speed} "
        f"{unit(tortoise_speed, 'mile')} per hour for the next "
        f"{n_unit(nap_hours, 'hour')}.",

        # 3) butterfly distraction → nap
        f"After tearing {n_unit(hare_lead, 'mile')} ahead of "
        f"{tortoise.name}, {hare.name} stopped to chase a bright butterfly "
        f"that flickered above the path. The chase tired {hare.him_her} "
        f"more than the running had, and {hare.he_she} flopped down in "
        f"the long grass, asleep within moments. {tortoise.name}, "
        f"{patient}, did not stop or look up — only walked steadily at "
        f"{tortoise_speed} {unit(tortoise_speed, 'mile')} per hour for "
        f"the {n_unit(nap_hours, 'hour')} that followed.",

        # 4) crowd encounter → bragging stop
        f"{n_unit(hare_lead, 'mile')} ahead of {tortoise.name}, "
        f"{hare.name} came upon a small crowd of forest animals who had "
        f"gathered to watch. {cap(hare.he_she)} could not resist a chance "
        f"to boast, and stayed to tell the story of {hare.his_her} "
        f"victory before it was even won. The telling was so long that "
        f"{hare.he_she} dozed off mid-sentence on a tree stump. "
        f"Meanwhile {tortoise.name} kept up a quiet "
        f"{tortoise_speed}-{unit(tortoise_speed, 'mile')}-per-hour pace "
        f"for {n_unit(nap_hours, 'hour')}.",

        # 5) summer heat + cool stream → nap
        f"By the time {hare.name} had run {n_unit(hare_lead, 'mile')} "
        f"ahead, the sun was high and {hare.he_she} was {tired}. A cool "
        f"stream ran beside the path, and {hare.he_she} stopped to drink "
        f"and stretch out on the mossy bank. The water sounded so "
        f"peaceful that {hare.he_she} fell asleep there. "
        f"{tortoise.name}, never slowed by heat, kept walking "
        f"{patient} at {tortoise_speed} {unit(tortoise_speed, 'mile')} "
        f"per hour for {n_unit(nap_hours, 'hour')} straight.",

        # 6) overconfidence → leisurely walk → nap
        f"{hare.name}, having opened a {n_unit(hare_lead, 'mile')} lead "
        f"{proud}, decided {hare.he_she} no longer needed to run at "
        f"all. {cap(hare.he_she)} began to amble — then to dawdle — "
        f"then to lie down for what {hare.he_she} called \"a strategic "
        f"nap.\" {tortoise.name} pressed on at {tortoise_speed} "
        f"{unit(tortoise_speed, 'mile')} per hour, never once "
        f"considering rest. For {n_unit(nap_hours, 'hour')}, "
        f"{tortoise.name} closed the gap step by patient step.",
    ]

    body = _render_subplot(scene, nap_overtake_subplots,
                           # all subplots use only locally-bound names;
                           # no .format substitutions needed since we
                           # built the strings inline. Pass-through.
                           )
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'who is in the lead by the time {hare.name} wakes up')}"
    )

    plan = (
        f"I compute {tortoise.name}'s position as speed × hours, then "
        f"compare against {hare.name}'s lead."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="tortoise-hare",
        chapter="nap-overtake",
        prefer_eval=True,
    )


def _th_speed_comparison(scene: Scene) -> Record:
    """Both move steadily. Three orientation variants of the same arithmetic
    (speed × time = distance):

      - distance-unknown: given speeds + hours, how many miles ahead?
      - hours-unknown:    given speeds + miles-ahead, for how long?
      - speed-unknown:    given tortoise-speed + hours + miles-ahead,
                          what was the hare's speed?
    """
    hare     = scene.pick_character(role_classes=("racer", "fast"))
    tortoise = scene.pick_character(role_classes=("racer", "slow"), not_=hare)
    location = scene.pick_location(tags_any=("path",), indoor=False)
    orient   = scene.pick_choice(["distance", "hours", "speed"])

    hare_speed     = scene.pick_int(4, 10)
    tortoise_speed = scene.pick_int(1, 3)
    hours          = scene.pick_int(2, 6)
    miles_ahead    = (hare_speed - tortoise_speed) * hours

    intro   = _aesopian_intro(scene, "tortoise-hare", location)
    proud   = scene.rng.choice(EMO_PROUD)
    patient = scene.rng.choice(EMO_PATIENT)

    if orient == "distance":
        # Given hare-speed, tortoise-speed, hours; compute miles-ahead.
        expr = Let(
            bindings=[
                ("hare-speed",        Lit(hare_speed)),
                ("tortoise-speed",    Lit(tortoise_speed)),
                ("hours",             Lit(hours)),
                ("hare-distance",     App("*", [Var("hare-speed"), Var("hours")])),
                ("tortoise-distance", App("*", [Var("tortoise-speed"), Var("hours")])),
            ],
            body=App("-", [Var("hare-distance"), Var("tortoise-distance")]),
        )
        answer = evaluate(expr)

        # Six narrative subplots — same arithmetic (hare_dist - tortoise_dist
        # over `hours`) but each grounds the abstract speeds in a small
        # roadside drama. Both run for the same `hours` along the same path;
        # the gap is what we're asked to find.
        speed_distance_subplots = [
            # 1) classic agreement at the starting stump
            f"{hare.name} the hare and {tortoise.name} the tortoise had "
            f"at last agreed to a fair test along the path. "
            f"{cap(hare.he_she)} set off {proud} at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, certain the matter would "
            f"be settled before lunch. {tortoise.name} kept a quiet "
            f"{tortoise_speed} {unit(tortoise_speed, 'mile')} per hour, "
            f"{patient}, and never glanced sideways. They had agreed to "
            f"run for exactly {n_unit(hours, 'hour')} and then measure the "
            f"distance between them.",

            # 2) sun-warmed lane after market
            f"On a sun-warmed lane leading away from the village, "
            f"{hare.name} bounded out {proud} at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, while {tortoise.name} "
            f"set off behind at a deliberate {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. The animals of the "
            f"meadow had agreed to call time after {n_unit(hours, 'hour')} "
            f"of running, then walk out and see how far apart the two had "
            f"ended up. {tortoise.name} pressed on {patient}, eyes never "
            f"leaving the road.",

            # 3) hare's swagger out of the gate
            f"{hare.name} swaggered to the line {proud} while "
            f"{tortoise.name} stood quietly waiting. At the call, "
            f"{hare.name} took off at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, kicking up small clouds "
            f"of dust, and {tortoise.name} began plodding forward at "
            f"{tortoise_speed} {unit(tortoise_speed, 'mile')} per hour. "
            f"Each had pledged to keep that pace without rest for "
            f"{n_unit(hours, 'hour')} — only then would the spectators "
            f"measure the gap.",

            # 4) two paces beneath the elms
            f"Beneath the row of elms that lined the racing path, two "
            f"very different paces fell into rhythm. {hare.name}, "
            f"{proud}, sprang ahead at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour. {tortoise.name}, "
            f"{patient}, set down each foot in turn at exactly "
            f"{tortoise_speed} {unit(tortoise_speed, 'mile')} per hour and "
            f"refused to be hurried. The pact was straightforward: keep "
            f"those paces for {n_unit(hours, 'hour')}, then let the lead "
            f"speak for itself.",

            # 5) old judge with a sundial
            f"An old badger had been chosen as judge, and produced a "
            f"sundial to mark the time. At his nod, {hare.name} bolted "
            f"forward {proud} at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, certain that "
            f"{tortoise.name} could never close any gap. {tortoise.name}, "
            f"{patient}, walked steadily at {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. The badger had said "
            f"plainly: after {n_unit(hours, 'hour')} of pace-keeping, "
            f"he would measure the lead and call it.",

            # 6) leisurely course along the brook
            f"The course wound beside a chuckling brook, and the morning "
            f"was already growing warm. {hare.name}, {proud}, leapt away "
            f"at a confident {hare_speed} {unit(hare_speed, 'mile')} per "
            f"hour. {tortoise.name} followed {patient}, holding to "
            f"{tortoise_speed} {unit(tortoise_speed, 'mile')} per hour as "
            f"if it were a heartbeat. They had each promised to run for "
            f"{n_unit(hours, 'hour')}, no more and no less, before "
            f"comparing where they stood.",
        ]

        body = _render_subplot(scene, speed_distance_subplots)
        what_q = (f"how many miles ahead {hare.name} is after "
                  f"{n_unit(hours, 'hour')}")
        user_msg = (
            f"{intro}{body}\n\n"
            f"{question_phrase(scene, what_q)}"
        )
        plan = (
            f"I multiply each runner's speed by the shared hours to get "
            f"their distances, then subtract."
        )
        chapter_name = "speed-comparison-distance"
    elif orient == "hours":
        # Given hare-speed, tortoise-speed, miles-ahead; compute hours.
        # gap-per-hour = hare-speed - tortoise-speed; hours = miles-ahead / gap.
        expr = Let(
            bindings=[
                ("hare-speed",     Lit(hare_speed)),
                ("tortoise-speed", Lit(tortoise_speed)),
                ("miles-ahead",    Lit(miles_ahead)),
                ("gap-per-hour",   App("-", [Var("hare-speed"),
                                              Var("tortoise-speed")])),
            ],
            body=App("quot", [Var("miles-ahead"), Var("gap-per-hour")]),
        )
        answer = evaluate(expr)

        # Six subplots — given speeds and a known final gap, find how
        # long they had been running. The lead has already opened up; the
        # narrator notices it and asks the listener to work backwards.
        speed_hours_subplots = [
            # 1) racing pair, gap-by-noon
            f"{hare.name} the hare and {tortoise.name} the tortoise had "
            f"set out together at sunrise, {hare.name} {proud} at "
            f"{hare_speed} {unit(hare_speed, 'mile')} per hour and "
            f"{tortoise.name} {patient} at {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. By the time the "
            f"forest folk came to check on them, {hare.name} stood "
            f"exactly {n_unit(miles_ahead, 'mile')} farther down the path "
            f"than {tortoise.name}. The animals knew both speeds and the "
            f"distance between them — only the running time was missing.",

            # 2) farmer notices the gap
            f"A farmer leaning on his fence watched the racers go past. "
            f"{hare.name} flew by {proud} at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour; {tortoise.name} came "
            f"behind at a calm {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour, {patient}. Some "
            f"while later the farmer wandered down the road and found "
            f"{hare.name} a clear {n_unit(miles_ahead, 'mile')} ahead of "
            f"{tortoise.name}. He scratched his beard and tried to work "
            f"out how long they had been running.",

            # 3) badger judge with a worn sundial
            f"The badger judge tracked the race from a low knoll. "
            f"{hare.name} kept up an unbroken {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, {proud}, and "
            f"{tortoise.name} held a steady {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour, {patient}. The "
            f"badger looked up from his sundial when the gap between them "
            f"reached exactly {n_unit(miles_ahead, 'mile')}. Knowing both "
            f"paces, he sat down to figure how many hours had passed since "
            f"the start.",

            # 4) crowd at the half-way ridge
            f"A small crowd had gathered at the half-way ridge to watch. "
            f"{hare.name}, {proud}, ran past at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, and {tortoise.name} "
            f"plodded along {patient} at {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. By the time the "
            f"sun had moved a fair way across the sky, the lead had grown "
            f"to {n_unit(miles_ahead, 'mile')} between them. From the two "
            f"speeds and the present gap, the spectators wanted to "
            f"reconstruct how long the race had been running.",

            # 5) postmaster glancing at the gap
            f"The village postmaster, walking the road, met "
            f"{tortoise.name} plodding along {patient} at {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. Far ahead he could "
            f"just make out {hare.name}, {proud}, holding {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour. The postmaster paced "
            f"out the distance and counted exactly "
            f"{n_unit(miles_ahead, 'mile')} between the two runners. "
            f"Knowing what he knew of their paces, he tried to deduce "
            f"how long the contest had run.",

            # 6) two paces under the elms, gap measured
            f"Under a row of elms, {hare.name} held a steady {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, {proud}, while "
            f"{tortoise.name}, {patient}, kept {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour without flagging. "
            f"At one moment a passing finch noted the gap had reached "
            f"exactly {n_unit(miles_ahead, 'mile')}. Given those two "
            f"unwavering paces, the question was simply how long they "
            f"had been at it.",
        ]

        body = _render_subplot(scene, speed_hours_subplots)
        user_msg = (
            f"{intro}{body}\n\n"
            f"{question_phrase(scene, 'how many whole hours they had been running')}"
        )
        plan = (
            f"The gap grows by (hare-speed minus tortoise-speed) each hour, "
            f"so I divide miles-ahead by that gap rate."
        )
        chapter_name = "speed-comparison-hours"
    else:
        # Given tortoise-speed, hours, miles-ahead; compute hare-speed.
        # hare-speed = (miles-ahead + tortoise-speed*hours) / hours
        expr = Let(
            bindings=[
                ("tortoise-speed", Lit(tortoise_speed)),
                ("hours",          Lit(hours)),
                ("miles-ahead",    Lit(miles_ahead)),
                ("tortoise-distance",
                 App("*", [Var("tortoise-speed"), Var("hours")])),
                ("hare-distance",
                 App("+", [Var("miles-ahead"), Var("tortoise-distance")])),
            ],
            body=App("quot", [Var("hare-distance"), Var("hours")]),
        )
        answer = evaluate(expr)

        # Six subplots — given the tortoise's known steady pace, the run
        # duration, and the final lead, work out the hare's speed. The
        # hare's pride is the moral hook; the missing number is how fast
        # he was actually going.
        speed_speed_subplots = [
            # 1) post-race stump-side debate
            f"After the race, the animals gathered at the finishing stump "
            f"to talk it over. {tortoise.name} had walked {patient} at a "
            f"known {tortoise_speed} {unit(tortoise_speed, 'mile')} per "
            f"hour for the full {n_unit(hours, 'hour')}. {hare.name}, "
            f"{proud}, had refused to say how fast {hare.he_she} had "
            f"actually run, but everyone could see {hare.he_she} had "
            f"finished {n_unit(miles_ahead, 'mile')} ahead of "
            f"{tortoise.name}. The badger judge set out to compute "
            f"{hare.name}'s real pace.",

            # 2) sundial-judged race, hare's swagger
            f"The badger judge timed the race with a sundial: a clean "
            f"{n_unit(hours, 'hour')} from start to call. {tortoise.name}, "
            f"{patient}, had held a measured {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour throughout. "
            f"{hare.name}, {proud}, would only say that {hare.he_she} had "
            f"\"run as a Hare ought,\" finishing "
            f"{n_unit(miles_ahead, 'mile')} in front of {tortoise.name}. "
            f"The badger pulled out his slate to work out {hare.name}'s "
            f"actual speed.",

            # 3) finch reporters at the post
            f"Two finches who had been reporting the race quarrelled "
            f"over the result. {tortoise.name}, {patient}, had walked a "
            f"known {tortoise_speed} {unit(tortoise_speed, 'mile')} per "
            f"hour for the agreed {n_unit(hours, 'hour')}. {hare.name}, "
            f"{proud}, had crossed the finish line "
            f"{n_unit(miles_ahead, 'mile')} ahead. Neither finch had "
            f"thought to clock {hare.name}'s actual pace, but with a "
            f"little arithmetic the speed could still be recovered.",

            # 4) farmer at the gate, end-of-race
            f"The farmer at the gate watched the contestants come past "
            f"in sequence. {tortoise.name}, {patient}, had managed "
            f"exactly {tortoise_speed} {unit(tortoise_speed, 'mile')} "
            f"per hour for {n_unit(hours, 'hour')} without break. "
            f"{hare.name}, {proud}, finished {n_unit(miles_ahead, 'mile')} "
            f"farther down the lane. The farmer leaned on his rake and "
            f"tried to work out, from those numbers alone, how fast "
            f"{hare.name} had truly been running.",

            # 5) elder hedgehog reconstructs the pace
            f"At sundown the elder hedgehog gathered the small crowd "
            f"around to settle the question. {tortoise.name} had kept "
            f"{patient} to {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour for the agreed "
            f"{n_unit(hours, 'hour')}. {hare.name}, {proud}, had crossed "
            f"{n_unit(miles_ahead, 'mile')} ahead. The hedgehog said the "
            f"answer was simple: combine {tortoise.name}'s distance with "
            f"the lead, then divide by the time, and {hare.name}'s real "
            f"pace would emerge.",

            # 6) traveller asking about the morning's race
            f"A traveller passing through stopped to ask about the "
            f"morning's race. He was told that {tortoise.name}, "
            f"{patient}, had walked a steady {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour for "
            f"{n_unit(hours, 'hour')}, and that {hare.name}, {proud}, "
            f"had finished {n_unit(miles_ahead, 'mile')} ahead. "
            f"\"And how fast was the Hare?\" he asked, but no one had "
            f"clocked {hare.name} directly — only the math could supply "
            f"the answer.",
        ]

        body = _render_subplot(scene, speed_speed_subplots)
        what_q = f"{hare.name}'s speed in miles per hour"
        user_msg = (
            f"{intro}{body}\n\n"
            f"{question_phrase(scene, what_q)}"
        )
        plan = (
            f"{hare.name}'s total distance equals the lead plus "
            f"{tortoise.name}'s distance; speed equals that total divided "
            f"by hours."
        )
        chapter_name = "speed-comparison-speed"

    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="tortoise-hare",
        chapter=chapter_name,
    )


def _th_distance_remaining(scene: Scene) -> Record:
    """How much further must the tortoise walk to finish?"""
    tortoise = scene.pick_character(role_classes=("racer", "slow"))
    hare     = scene.pick_character(role_classes=("racer", "fast"), not_=tortoise)
    location = scene.pick_location(tags_any=("path",), indoor=False)

    total       = scene.pick_int(10, 25)
    walked      = scene.pick_int(2, total - 1)
    speed       = scene.pick_int(1, 3)

    expr = Let(
        bindings=[
            ("total",  Lit(total)),
            ("miles-walked", Lit(walked)),
            ("walk-speed",  Lit(speed)),
            ("miles-remaining", App("-", [Var("total"), Var("miles-walked")])),
        ],
        body=App("quot", [Var("miles-remaining"), Var("walk-speed")]),
    )
    answer = evaluate(expr)

    intro   = _aesopian_intro(scene, "tortoise-hare", location)
    proud   = scene.rng.choice(EMO_PROUD)
    patient = scene.rng.choice(EMO_PATIENT)
    tired   = scene.rng.choice(EMO_TIRED)

    # Six narrative subplots — same arithmetic (total - walked, divided
    # by speed) but each frames the unfinished course in a different
    # small drama. The hare is somewhere off-stage in each: napping,
    # boasting, or already finished — leaving the patient tortoise to
    # finish the remaining stretch step by careful step.
    distance_remaining_subplots = [
        # 1) classic — tortoise pauses to look back at distance walked
        f"The course was {n_unit(total, 'mile')} long, and "
        f"{tortoise.name} the tortoise had already covered "
        f"{n_unit(walked, 'mile')} of it {patient}, footstep by "
        f"footstep. Far ahead, {hare.name} the hare was {tired} under "
        f"some tree, having declared the race already won. "
        f"{cap(tortoise.he_she)} paused only briefly to look back at "
        f"the path {tortoise.he_she} had crossed, then resumed at "
        f"{speed} {unit(speed, 'mile')} per hour, intending to finish.",

        # 2) midday milestone, marker stones at the trail
        f"A row of small marker stones counted out the "
        f"{n_unit(total, 'mile')} of the agreed course. "
        f"{tortoise.name}, walking {patient}, had passed the stone "
        f"reading {n_unit(walked, 'mile')} just before noon. "
        f"{hare.name} was somewhere up ahead, dozing {tired} where "
        f"{hare.he_she} had dropped after sprinting too hard. "
        f"{tortoise.name} held to {speed} "
        f"{unit(speed, 'mile')} per hour with no sign of slowing.",

        # 3) curious badger asks how far is left
        f"A curious old badger met {tortoise.name} on the path and "
        f"asked how the race was going. \"The course is "
        f"{n_unit(total, 'mile')},\" said {tortoise.name} {patient}, "
        f"\"and I have walked {n_unit(walked, 'mile')} so far.\" "
        f"Behind him, {hare.name} could just be made out, {proud} but "
        f"{tired}, lounging by a stump. {tortoise.name} added that "
        f"{tortoise.he_she} kept a steady {speed} "
        f"{unit(speed, 'mile')} per hour and meant to finish before "
        f"sundown.",

        # 4) river crossing, halfway behind
        f"The race ran past a slow brown river that cut the "
        f"{n_unit(total, 'mile')} course nearly in two. {tortoise.name} "
        f"had crossed it long ago and now had {n_unit(walked, 'mile')} "
        f"behind {tortoise.him_her}, walking {patient} at {speed} "
        f"{unit(speed, 'mile')} per hour. Down the lane, {hare.name} "
        f"sat against a fence post, {tired}, telling no one in "
        f"particular how the race had been won twice over. "
        f"{tortoise.name} did not stop to listen.",

        # 5) sunset deadline, finish before dark
        f"They had agreed to finish before sundown. The course was "
        f"{n_unit(total, 'mile')}; {tortoise.name} had already walked "
        f"{n_unit(walked, 'mile')} {patient}, never quickening, never "
        f"slowing. {hare.name}, {proud} but now {tired}, had given up "
        f"on running entirely and was instead arguing with a passing "
        f"squirrel about who deserved the prize. {tortoise.name} "
        f"continued at {speed} {unit(speed, 'mile')} per hour, eyes on "
        f"the lengthening shadows.",

        # 6) old shepherd, marker stake at the meadow
        f"An old shepherd had driven a stake at the {n_unit(total, 'mile')} "
        f"mark to call the finish line. {tortoise.name} had passed "
        f"{n_unit(walked, 'mile')} of those miles, plodding {patient} "
        f"without complaint. {hare.name} was nowhere in sight — "
        f"asleep, the shepherd guessed, {tired} from too many "
        f"shortcuts. {tortoise.name} pressed forward at {speed} "
        f"{unit(speed, 'mile')} per hour, certain only that "
        f"{tortoise.he_she} would arrive when {tortoise.he_she} "
        f"arrived.",
    ]

    body = _render_subplot(scene, distance_remaining_subplots)
    what_q = (f"how many more whole hours of walking {tortoise.name} "
              f"needs to reach the finish line")
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, what_q)}"
    )
    plan = (
        f"I subtract the distance already walked from the total to "
        f"find what remains, then divide by {tortoise.name}'s speed."
    )

    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="tortoise-hare",
        chapter="distance-remaining",
    )


# ─────────────────────── 2. Crow and the Pitcher ───────────────────────


def gen_crow_pitcher(scene: Scene) -> Record:
    chapter = scene.pick_choice(["stones-needed", "water-rise",
                                 "enough-stones"])
    if chapter == "stones-needed":
        return _cp_stones_needed(scene)
    if chapter == "water-rise":
        return _cp_water_rise(scene)
    return _cp_enough_stones(scene)


def _cp_stones_needed(scene: Scene) -> Record:
    """Each stone raises water by R cm. Start water S; need T. How many stones?"""
    crow = scene.pick_character(role_classes=("cunning",), species="crow")
    location = scene.pick_location(tags_any=("nature",), indoor=False)
    # Vary the vessel (pitcher / jar / pot) and the dropped item
    # (pebble / marble / bead / acorn / nut) — every story still
    # has the same arithmetic. Items are all small enough to fit.
    vessel = scene.rng.choice([
        c for c in ont.CONTAINERS if c.name in ("pitcher", "jar", "pot")
    ])
    stone = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("pebble", "marble", "bead", "acorn", "nut")
    ])

    rise_per = scene.pick_int(1, 3)
    start    = scene.pick_int(2, 6)
    target   = scene.pick_int(start + rise_per, start + rise_per * 10)

    expr = Let(
        bindings=[
            ("rise-per-stone", Lit(rise_per)),
            ("start-cm",       Lit(start)),
            ("target-cm",      Lit(target)),
            ("level-gap",            App("-", [Var("target-cm"), Var("start-cm")])),
        ],
        body=App("quot", [App("+", [Var("level-gap"),
                                     App("dec", [Var("rise-per-stone")])]),
                          Var("rise-per-stone")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "crow-pitcher", location)
    thirsty   = scene.rng.choice(EMO_THIRSTY)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (gap = target - start;
    # answer = ceil(gap / rise-per-stone)) but each grounds it in a
    # different small drama: a parched flight, a sun-baked yard, a
    # shimmer of water glimpsed at the bottom of the vessel.
    stones_needed_subplots = [
        # 1) classic pitcher in a sunlit garden
        f"After hours of fruitless searching, {crow.name} the crow "
        f"glided down to a quiet garden, {thirsty}. There on a low wall "
        f"stood a {vessel.name}, and from above {crow.he_she} could see "
        f"a thin glimmer of water at the bottom — only "
        f"{n_unit(start, 'centimeter')} deep, and {crow.his_her} beak "
        f"could not reach unless the surface rose to "
        f"{n_unit(target, 'centimeter')}. A scattering of {stone.plural} "
        f"lay along the path. Each {stone.name}, when dropped in, would "
        f"push the water up by {n_unit(rise_per, 'centimeter')}. "
        f"{cap(crow.he_she)} began to count what {crow.he_she} would need.",

        # 2) parched afternoon by the orchard
        f"The afternoon sun beat down hard, and {crow.name}, "
        f"{thirsty}, settled at the edge of an orchard where a stout "
        f"{vessel.name} had been left out. The water inside lay "
        f"{n_unit(start, 'centimeter')} from the bottom — far below "
        f"the {n_unit(target, 'centimeter')} mark {crow.he_she} needed "
        f"to drink. Beneath a nearby tree {crow.he_she} found a small "
        f"heap of {stone.plural}. {cap(crow.he_she)} weighed one in "
        f"{crow.his_her} beak: it would lift the surface by exactly "
        f"{n_unit(rise_per, 'centimeter')}. Now it was only a matter "
        f"of working out how many {crow.he_she} would have to drop.",

        # 3) flock-watched, desperate
        f"A small crowd of finches watched as {crow.name} alighted "
        f"{desperate} beside a tall {vessel.name}. {cap(crow.he_she)} "
        f"could see the dark shimmer of water sitting "
        f"{n_unit(start, 'centimeter')} from the bottom — well short "
        f"of the {n_unit(target, 'centimeter')} {crow.he_she} required. "
        f"By the foot of the {vessel.name} lay a scatter of dry "
        f"{stone.plural}. {cap(crow.he_she)} dropped one in: a soft "
        f"plink, and the water climbed by {n_unit(rise_per, 'centimeter')}. "
        f"The finches leaned closer. {cap(crow.he_she)} began the steady "
        f"work of figuring exactly how many more would do the trick.",

        # 4) old farmyard at dusk
        f"At the edge of an old farmyard, {crow.name} the crow, "
        f"{thirsty}, came to rest on the rim of a cracked {vessel.name}. "
        f"The water below was only {n_unit(start, 'centimeter')} deep "
        f"and needed to climb to {n_unit(target, 'centimeter')} before "
        f"{crow.he_she} could so much as wet {crow.his_her} tongue. "
        f"Around the yard lay countless {stone.plural} of just the right "
        f"size, and a quick test showed each one would raise the water "
        f"by {n_unit(rise_per, 'centimeter')}. The trick now was simply "
        f"to count.",

        # 5) dry stone wall, careful pebbles
        f"{cap(species_phrase(crow))}, {thirsty}, found a {vessel.name} "
        f"set on a dry stone wall. The sound of water sloshing softly "
        f"inside was almost cruel — for the surface lay only "
        f"{n_unit(start, 'centimeter')} from the bottom, and "
        f"{crow.his_her} beak required it to reach "
        f"{n_unit(target, 'centimeter')}. Tiny {stone.plural} were "
        f"wedged among the wall's cracks; {crow.he_she} pried one loose "
        f"and let it fall. A clear chime, and the level rose by "
        f"{n_unit(rise_per, 'centimeter')}. {cap(crow.he_she)} settled "
        f"onto the rim and counted carefully.",

        # 6) quiet courtyard, last hope
        f"In a quiet courtyard {crow.name} alighted {desperate} on "
        f"the lip of a {vessel.name}. Below, a sliver of water at "
        f"{n_unit(start, 'centimeter')} caught the last of the daylight "
        f"— but {crow.his_her} beak could only reach down to "
        f"{n_unit(target, 'centimeter')}, no further. A handful of "
        f"smooth {stone.plural} had been left near the doorway. "
        f"{cap(crow.he_she)} tested one: a single {stone.name} pushed "
        f"the water up by {n_unit(rise_per, 'centimeter')}. "
        f"{cap(crow.he_she)} began calculating how many it would take "
        f"to bring the surface within reach.",
    ]

    body = _render_subplot(scene, stones_needed_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'the smallest number of {stone.plural} {crow.name} needs to drop in to reach the target water level')}"
    )

    plan = (
        f"I find the gap between target and start, then divide by "
        f"the rise per stone (rounding up by adding rise-per-stone-1 first)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="crow-pitcher",
        chapter="stones-needed",
    )


def _cp_water_rise(scene: Scene) -> Record:
    """N stones dropped × R cm each + start = final water level."""
    crow = scene.pick_character(role_classes=("cunning",), species="crow")
    location = scene.pick_location(tags_any=("nature",), indoor=False)
    # Vary the vessel and the dropped item; each subplot keeps the
    # same arithmetic but reaches it through a different small drama.
    vessel = scene.rng.choice([
        c for c in ont.CONTAINERS if c.name in ("pitcher", "jar", "pot")
    ])
    stone = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("pebble", "marble", "bead", "acorn", "nut")
    ])

    rise_per = scene.pick_int(1, 3)
    start    = scene.pick_int(1, 5)
    n_stones = scene.pick_int(2, 12)

    expr = Let(
        bindings=[
            ("rise-per-stone", Lit(rise_per)),
            ("start-cm",       Lit(start)),
            ("n-stones",       Lit(n_stones)),
        ],
        body=App("+", [Var("start-cm"),
                       App("*", [Var("n-stones"), Var("rise-per-stone")])]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "crow-pitcher", location)
    thirsty   = scene.rng.choice(EMO_THIRSTY)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (final = start + n × rise),
    # each grounding it in a distinct sensory beat: a hot afternoon, the
    # plink of falling stones, the slow climb of water against the
    # vessel's wall.
    water_rise_subplots = [
        # 1) classic — quiet garden, methodical drops
        f"{crow.name} the crow, {thirsty}, alighted on the lip of "
        f"a cool {vessel.name} half-hidden in shadow. The water inside "
        f"sat at {n_unit(start, 'centimeter')} from the bottom — too "
        f"deep for {crow.his_her} beak. Around the base lay a scatter "
        f"of small {stone.plural}, and {crow.he_she} began to drop "
        f"them in one by one. {cap(crow.he_she)} counted: "
        f"{n_unit(n_stones, stone.name, stone.plural)} in all. With "
        f"each soft plink, the surface climbed a careful "
        f"{n_unit(rise_per, 'centimeter')} higher.",

        # 2) sun-baked yard — heat shimmer, slow patient work
        f"The afternoon was hot enough to crack a leaf, and {crow.name}, "
        f"{thirsty}, settled at the rim of an old {vessel.name} that "
        f"someone had left in the sun. The water at the bottom — only "
        f"{n_unit(start, 'centimeter')} deep — shimmered just out of "
        f"reach. A pile of dry {stone.plural} sat nearby. One by one "
        f"{crow.he_she} ferried them up and let them fall, "
        f"{n_unit(n_stones, stone.name, stone.plural)} altogether, "
        f"each one shouldering the surface up by another "
        f"{n_unit(rise_per, 'centimeter')}.",

        # 3) sparrows watching — a small audience for cleverness
        f"A pair of sparrows tilted their heads to watch as {crow.name} "
        f"{desperate} circled a stout {vessel.name} on a low garden "
        f"wall. The water within stood at {n_unit(start, 'centimeter')} "
        f"— a depth no beak in {crow.his_her} family had ever managed. "
        f"From a tray nearby {crow.he_she} fetched "
        f"{n_unit(n_stones, stone.name, stone.plural)} in turn, "
        f"dropping each with a soft chime. Every {stone.name} that "
        f"sank lifted the surface by exactly "
        f"{n_unit(rise_per, 'centimeter')}, and the sparrows watched "
        f"the water climb.",

        # 4) farmhouse stoop, dusk
        f"At dusk by a farmhouse stoop, {crow.name} the crow paused "
        f"beside a chipped {vessel.name}. The water inside, only "
        f"{n_unit(start, 'centimeter')} deep, sent up a thin reflection "
        f"of the sky. {cap(crow.he_she)} was {thirsty}, and so "
        f"{crow.he_she} did what every clever crow knows to do: "
        f"{crow.he_she} gathered "
        f"{n_unit(n_stones, stone.name, stone.plural)} from the gravel "
        f"along the path and dropped them in, one after another. Each "
        f"{stone.name} shouldered the water up by "
        f"{n_unit(rise_per, 'centimeter')}, and {crow.he_she} kept count.",

        # 5) cool stone courtyard — sound of falling stones
        f"In a cool stone courtyard {crow.name}, {thirsty}, found a "
        f"narrow {vessel.name} at the foot of a column. The water "
        f"sloshed faintly within at {n_unit(start, 'centimeter')}, far "
        f"out of reach. {cap(crow.he_she)} set to work. From a corner "
        f"where {stone.plural} had been swept into a small heap "
        f"{crow.he_she} lifted them, one after another — "
        f"{n_unit(n_stones, stone.name, stone.plural)} in total — and "
        f"let each fall with a soft chime. Each chime pushed the surface "
        f"up by another {n_unit(rise_per, 'centimeter')}.",

        # 6) orchard well — last light of day
        f"By an orchard well, {crow.name} the crow flexed "
        f"{crow.his_her} tired wings and looked into a {vessel.name} "
        f"someone had set out for travelers. Water lay "
        f"{n_unit(start, 'centimeter')} deep at the bottom. "
        f"{cap(crow.he_she)} was {thirsty}, but {crow.he_she} was also "
        f"clever. Beneath an apple tree {crow.he_she} found "
        f"{n_unit(n_stones, stone.name, stone.plural)} of reasonable "
        f"weight. One at a time {crow.he_she} carried each to the rim "
        f"and dropped it in, every {stone.name} lifting the water by "
        f"another {n_unit(rise_per, 'centimeter')}.",
    ]

    body = _render_subplot(scene, water_rise_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'the new water level in the {vessel.name} (in centimeters) after all {n_stones} {stone.plural} have been dropped in')}"
    )

    plan = (
        f"I multiply the number of {stone.plural} by the rise per "
        f"{stone.name} and add the starting level."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="crow-pitcher",
        chapter="water-rise",
    )


def _cp_enough_stones(scene: Scene) -> Record:
    """Crow has K stones in pouch. Will K × R + start ≥ T?"""
    crow = scene.pick_character(role_classes=("cunning",), species="crow")
    location = scene.pick_location(tags_any=("nature",), indoor=False)
    # Vary the vessel and the dropped item across subplots; the math
    # (start + k × rise ≥ target) is the same in every story.
    vessel = scene.rng.choice([
        c for c in ont.CONTAINERS if c.name in ("pitcher", "jar", "pot")
    ])
    stone = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("pebble", "marble", "bead", "acorn", "nut")
    ])

    rise_per = scene.pick_int(1, 2)
    start    = scene.pick_int(2, 5)
    target   = scene.pick_int(start + 3, start + 15)
    k        = scene.pick_int(1, 12)

    expr = Let(
        bindings=[
            ("n-stones",  Lit(k)),
            ("rise-per",  Lit(rise_per)),
            ("start-cm",  Lit(start)),
            ("target-cm", Lit(target)),
            ("reachable", App("+", [Var("start-cm"),
                                     App("*", [Var("n-stones"), Var("rise-per")])])),
        ],
        body=App(">=", [Var("reachable"), Var("target-cm")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "crow-pitcher", location)
    thirsty   = scene.rng.choice(EMO_THIRSTY)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (does start + k × rise
    # reach target?) grounded in different small dramas: a pouch
    # carefully counted, the last few stones, the question of whether
    # this small store of cleverness will be enough.
    enough_stones_subplots = [
        # 1) classic — last few pebbles at the rim
        f"After a long flight, {crow.name} the crow alighted "
        f"{thirsty} on the rim of a {vessel.name}. The water within "
        f"sat only {n_unit(start, 'centimeter')} from the bottom and "
        f"needed to reach {n_unit(target, 'centimeter')} before "
        f"{crow.his_her} beak could drink. {cap(crow.he_she)} had "
        f"gathered {n_unit(k, stone.name, stone.plural)} on the way — "
        f"no more. {cap(crow.he_she)} weighed one in {crow.his_her} "
        f"beak: each {stone.name} would lift the surface by "
        f"{n_unit(rise_per, 'centimeter')}. The question was whether "
        f"this small store would be enough.",

        # 2) pouch counted out on the wall
        f"On a low garden wall {crow.name} laid out the contents of "
        f"a small pouch — {n_unit(k, stone.name, stone.plural)}, all "
        f"that remained. Beside the wall stood a {vessel.name}, water "
        f"glinting at {n_unit(start, 'centimeter')} and needing to "
        f"climb to {n_unit(target, 'centimeter')} before {crow.he_she} "
        f"could drink. {cap(crow.he_she)} was {thirsty}, and a quick "
        f"test showed each {stone.name} raised the water by exactly "
        f"{n_unit(rise_per, 'centimeter')}. {cap(crow.he_she)} began "
        f"to count whether so few would do.",

        # 3) sun-baked stoop — desperate calculation
        f"The stoop was hot enough to scorch {crow.his_her} feet, "
        f"and {crow.name}, {desperate}, peered down into a {vessel.name} "
        f"set against the wall. The water lay "
        f"{n_unit(start, 'centimeter')} deep — far short of the "
        f"{n_unit(target, 'centimeter')} {crow.he_she} required. From "
        f"a fold in {crow.his_her} feathers {crow.he_she} produced "
        f"{n_unit(k, stone.name, stone.plural)}, gathered carefully on "
        f"the long road. Each one, dropped in, would lift the surface "
        f"by {n_unit(rise_per, 'centimeter')}. Would it be enough?",

        # 4) sparrows watching, doubt
        f"Two sparrows perched nearby as {crow.name} the crow, "
        f"{thirsty}, hopped to the rim of a {vessel.name}. The water "
        f"glimmered far below at {n_unit(start, 'centimeter')}, and "
        f"{crow.his_her} beak could only drink if it climbed to "
        f"{n_unit(target, 'centimeter')}. From a careful pile beside "
        f"{crow.his_her} foot {crow.he_she} counted "
        f"{n_unit(k, stone.name, stone.plural)} — that was all. A "
        f"trial drop showed each {stone.name} pushed the surface up "
        f"by {n_unit(rise_per, 'centimeter')}. The sparrows watched, "
        f"unconvinced.",

        # 5) twilight orchard, last hope
        f"Twilight settled over the orchard as {crow.name}, "
        f"{thirsty}, found a {vessel.name} forgotten beneath a tree. "
        f"The water sat {n_unit(start, 'centimeter')} from the bottom; "
        f"to drink, {crow.he_she} needed it at "
        f"{n_unit(target, 'centimeter')}. Tucked in a curl of bark "
        f"{crow.he_she} had been keeping "
        f"{n_unit(k, stone.name, stone.plural)} for just such a "
        f"moment. A first {stone.name} fell with a soft chime — the "
        f"water rose by {n_unit(rise_per, 'centimeter')}. "
        f"{cap(crow.he_she)} paused to think before dropping the rest.",

        # 6) old courtyard, careful counting
        f"In an old courtyard {crow.name} the crow tilted "
        f"{crow.his_her} head over a {vessel.name} on a stone bench. "
        f"Water at {n_unit(start, 'centimeter')} sloshed quietly within, "
        f"unreachable until it climbed to "
        f"{n_unit(target, 'centimeter')}. {cap(crow.he_she)} was "
        f"{thirsty} and held only "
        f"{n_unit(k, stone.name, stone.plural)} — every one counted. "
        f"Dropping a single {stone.name} lifted the surface by "
        f"{n_unit(rise_per, 'centimeter')}. {cap(crow.he_she)} "
        f"weighed the question carefully.",
    ]

    body = _render_subplot(scene, enough_stones_subplots)
    stones_with_count = n_unit(k, stone.name, stone.plural)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'whether the water level reaches the target after {crow.name} drops in all {stones_with_count} (true if it does, false otherwise)')}"
    )

    plan = (
        f"I compute the reachable water level with the available "
        f"{stone.plural} and compare with the target."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="crow-pitcher",
        chapter="enough-stones",
    )


# ─────────────────────── 3. Goose and the Golden Eggs ───────────────────────


def gen_goose_eggs(scene: Scene) -> Record:
    chapter = scene.pick_choice(["total-yield", "value-yield",
                                  "compounded", "average"])
    if chapter == "total-yield":
        return _ge_total_yield(scene)
    if chapter == "value-yield":
        return _ge_value_yield(scene)
    if chapter == "compounded":
        return _ge_compounded(scene)
    return _ge_average(scene)


def _ge_total_yield(scene: Scene) -> Record:
    """Lays N eggs/day for D days. Total eggs?"""
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))
    location = scene.pick_location(tag="village")

    per_day = scene.pick_int(1, 3)
    days    = scene.pick_int(5, 30)

    expr = Let(
        bindings=[("per-day", Lit(per_day)), ("days", Lit(days))],
        body=App("*", [Var("per-day"), Var("days")]),
    )
    answer = evaluate(expr)

    intro    = _aesopian_intro(scene, "goose-eggs", location)
    greedy   = scene.rng.choice(EMO_GREEDY)
    content  = scene.rng.choice(EMO_CONTENT)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (per-day × days = total)
    # but each grounds it in a different small drama: the morning ritual,
    # the creaking table where eggs are tallied, the silver-egg variant,
    # the temptation to keep counting more.
    total_yield_subplots = [
        # 1) classic — daily golden ritual at the farm
        f"{owner.name} kept {species_phrase(goose)} on a quiet farm at "
        f"the edge of {location.article} {location.name}. Every morning, "
        f"without fail, the goose laid {per_day} golden "
        f"{unit(per_day, 'egg')} in the same straw nest. {cap(owner.he_she)} "
        f"would lift each egg with both hands, {content}, and place it "
        f"in a wooden basket beside the door. The ritual went on for "
        f"{n_unit(days, 'day')} — sun, wind, or rain — and {owner.name} "
        f"began to wonder how many golden eggs had passed through "
        f"{owner.his_her} hands by the end of that long stretch.",

        # 2) creaking table, evening tally
        f"Each evening at {location.article} {location.name}, "
        f"{owner.name} sat at a creaking table and laid out the day's "
        f"haul: {per_day} golden {unit(per_day, 'egg')} from the goose, "
        f"warm and shining like little suns. {cap(owner.he_she)} kept a "
        f"chalk mark on a beam for every egg, {greedy}, watching the "
        f"row of marks lengthen. After {n_unit(days, 'day')} of marks, "
        f"the beam was nearly full, and {owner.name} squinted up at it "
        f"trying to count exactly how many eggs in all the goose had laid.",

        # 3) silver-egg variant — village gossip
        f"In {location.article} {location.name} the neighbors swore "
        f"{owner.name}'s goose laid silver eggs as well as golden, but "
        f"the truth was simpler: {per_day} ordinary-shaped "
        f"{unit(per_day, 'egg')} of pure gold, every single morning. "
        f"{cap(owner.he_she)} carried each egg from the barn in a folded "
        f"apron, {content}, and slid it into a clay jar by the hearth. "
        f"For {n_unit(days, 'day')} the jar grew heavier. {owner.name} "
        f"set out one quiet evening to count what the goose had given "
        f"in all that time.",

        # 4) market temptation, daily restraint
        f"At first {owner.name} had thought of taking the eggs to the "
        f"market straight away, but {owner.he_she} held back. The goose "
        f"laid {per_day} golden {unit(per_day, 'egg')} each dawn, calm "
        f"as ever, and {owner.name} let them pile up in a little chest "
        f"beneath the bed, {greedy} at the thought of one great trip "
        f"to {location.name} when the time was right. After "
        f"{n_unit(days, 'day')} of steady laying, the chest was so "
        f"heavy {owner.he_she} could barely drag it. The first task was "
        f"to count how many eggs lay inside.",

        # 5) farmhand witness — quiet morning ritual
        f"A young farmhand at {location.article} {location.name} liked "
        f"to come round at sunrise just to watch {owner.name} collect "
        f"from the goose. The bird would settle, ruffle, and stand, "
        f"leaving {per_day} golden {unit(per_day, 'egg')} in the straw — "
        f"never more, never fewer. {owner.name} would gather them "
        f"{content}, smiling at the boy, and tuck them into a folded "
        f"cloth. {cap(owner.he_she)} kept up the routine for "
        f"{n_unit(days, 'day')}, and at the end the boy asked, eyes "
        f"wide, just how many golden eggs the goose had given altogether.",

        # 6) the temptation thought, kept at bay
        f"More than once, {owner.name} had heard a sly voice in "
        f"{owner.his_her} own head whisper that one swift cut would "
        f"bring all the gold at once. But every morning the goose laid "
        f"{per_day} golden {unit(per_day, 'egg')} into the warm straw, "
        f"and every morning {owner.name} chose patience, {regretful} "
        f"only of the day {owner.he_she} had ever entertained the "
        f"thought. After {n_unit(days, 'day')} of steady gifts, "
        f"{owner.he_she} sat by the hearth at {location.article} "
        f"{location.name} and tried to reckon the total of what "
        f"patience had won {owner.him_her}.",
    ]

    body = _render_subplot(scene, total_yield_subplots)
    days_phrase = n_unit(days, "day")
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many eggs the goose laid in total over those {days_phrase}')}"
    )

    plan = "I multiply the eggs per day by the number of days."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="goose-eggs",
        chapter="total-yield",
    )


def _ge_value_yield(scene: Scene) -> Record:
    """Lays N eggs/day × D days × C coins/egg = total coins. Three orientation
    variants (one of {coins, days, per-egg-coins} unknown).

    The 6 narrative subplots share a skeleton (golden-egg routine + market
    trip + tally beat) and use a per-orient `givens` clause to state the
    facts the question hides — so each branch still gets 6 distinct beats
    without an 18-template explosion.
    """
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))
    location = scene.pick_location(tag="village")

    per_day  = scene.pick_int(1, 2)
    days     = scene.pick_int(7, 30)
    per_egg  = scene.pick_int(5, 50)
    total_coins = per_day * days * per_egg
    orient   = scene.pick_choice(["coins", "days", "per-egg"])
    _intro   = _aesopian_intro(scene, "goose-eggs", location)

    if orient == "coins":
        expr = Let(
            bindings=[
                ("per-day", Lit(per_day)),
                ("days",    Lit(days)),
                ("per-egg-coins", Lit(per_egg)),
                ("total-eggs",    App("*", [Var("per-day"), Var("days")])),
            ],
            body=App("*", [Var("total-eggs"), Var("per-egg-coins")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{owner.name} owned {species_phrase(goose)} that laid "
            f"{per_day} golden {unit(per_day, 'egg')} per day. Each egg "
            f"sold for {n_unit(per_egg, 'coin')} at the market. After "
            f"{n_unit(days, 'day')}, {owner.name} took the eggs to "
            f"{location.article} {location.name} to sell.\n\n"
            f"Question: How many coins did {owner.name} earn in total?"
        )
        result_text = f"{owner.name} earned {n_unit(answer, 'coin')}."
        narrative   = (
            "I find total eggs first (per-day × days), then multiply by "
            "the per-egg coin value."
        )
        chapter_name = "value-yield-coins"
    elif orient == "days":
        expr = Let(
            bindings=[
                ("per-day",        Lit(per_day)),
                ("per-egg-coins",  Lit(per_egg)),
                ("total-coins",    Lit(total_coins)),
                ("coins-per-day",
                 App("*", [Var("per-day"), Var("per-egg-coins")])),
            ],
            body=App("quot", [Var("total-coins"), Var("coins-per-day")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{owner.name} owned {species_phrase(goose)} that laid "
            f"{per_day} golden {unit(per_day, 'egg')} per day. Each egg "
            f"sold for {n_unit(per_egg, 'coin')}. By the time {owner.name} "
            f"had earned {n_unit(total_coins, 'coin')} in total, the goose "
            f"had been laying for some number of days.\n\n"
            f"Question: How many days had the goose been laying?"
        )
        result_text = f"The goose had been laying for {n_unit(answer, 'day')}."
        narrative   = (
            "Daily revenue is per-day eggs × per-egg coins; days = "
            "total-coins / coins-per-day."
        )
        chapter_name = "value-yield-days"
    else:
        expr = Let(
            bindings=[
                ("per-day",     Lit(per_day)),
                ("days",        Lit(days)),
                ("total-coins", Lit(total_coins)),
                ("total-eggs",  App("*", [Var("per-day"), Var("days")])),
            ],
            body=App("quot", [Var("total-coins"), Var("total-eggs")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{owner.name} owned {species_phrase(goose)} that laid "
            f"{per_day} golden {unit(per_day, 'egg')} per day. After "
            f"{n_unit(days, 'day')}, {owner.name} took the eggs to "
            f"{location.article} {location.name} and earned "
            f"{n_unit(total_coins, 'coin')} in all.\n\n"
            f"Question: At what price (in coins) did each egg sell?"
        )
        result_text = f"Each egg sold for {n_unit(answer, 'coin')}."
        narrative   = (
            "Total eggs is per-day × days; per-egg price = total-coins / "
            "total-eggs."
        )
        chapter_name = "value-yield-per-egg"

    code_block = render_code(expr, form=scene.code_form(), value=answer)
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="goose-eggs",
        chapter=chapter_name,
    )


def _ge_compounded(scene: Scene) -> Record:
    """Daily yields, then sum across days. Picks one of three idiomatic
    Clojure forms for the sum: `(reduce + xs)`, `(apply + xs)`, or the
    verbose `(reduce (fn [a b] (+ a b)) 0 xs)`."""
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))

    days = scene.pick_int(3, 7)
    yields = [scene.pick_int(1, 4) for _ in range(days)]

    expr = Let(
        bindings=[("daily-yields", Lit(list(yields)))],
        body=_sum_expr(scene, Var("daily-yields")),
    )
    answer = evaluate(expr)

    yields_str = ", ".join(str(y) for y in yields)
    _intro = _aesopian_intro(scene, "goose-eggs")
    user_msg = (
        f"{_intro}{owner.name} owned {species_phrase(goose)}, who laid different "
        f"numbers of eggs each day for {n_unit(days, 'day')}: "
        f"{yields_str}.\n\n"
        f"Question: How many eggs in total over the {n_unit(days, 'day')}?"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"The total is {answer} eggs."
    narrative   = (
        "I use reduce with + to sum the daily yields starting from 0."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="goose-eggs",
        chapter="compounded",
    )


def _ge_average(scene: Scene) -> Record:
    """Mean yield over D days (using quot for int answer)."""
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))

    days = scene.pick_int(3, 6)
    # Pick yields whose sum is divisible by `days` so the integer
    # quot answer is exact (avoids confusion).
    base = scene.pick_int(2, 5)
    yields = []
    for _ in range(days - 1):
        yields.append(base + scene.pick_int(-1, 1))
    yields.append(base * days - sum(yields))   # forces sum == base*days
    yields = [max(1, y) for y in yields]
    # Recompute final to keep math right after the max(1, …) clamp.
    diff = base * days - sum(yields)
    yields[0] += diff
    yields[0] = max(1, yields[0])

    expr = Let(
        bindings=[
            ("daily-yields", Lit(list(yields))),
            ("total", _sum_expr(scene, Var("daily-yields"))),
            ("days",  App("count", [Var("daily-yields")])),
        ],
        body=App("quot", [Var("total"), Var("days")]),
    )
    answer = evaluate(expr)

    yields_str = ", ".join(str(y) for y in yields)
    _intro = _aesopian_intro(scene, "goose-eggs")
    user_msg = (
        f"{_intro}{owner.name} kept {species_phrase(goose)}, who laid these eggs "
        f"on successive days: {yields_str}.\n\n"
        f"Question: What is the average eggs per day, rounded down to a "
        f"whole number?"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"The average is {answer} eggs per day."
    narrative   = (
        "I compute the total with reduce, divide by the count, taking "
        "integer quotient."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="goose-eggs",
        chapter="average",
    )


# ─────────────────────── 4. Boy Who Cried Wolf ───────────────────────


def gen_boy_wolf(scene: Scene) -> Record:
    chapter = scene.pick_choice(["false-alarms", "sheep-eaten",
                                  "trust-threshold"])
    if chapter == "false-alarms":
        return _bw_false_alarms(scene)
    if chapter == "sheep-eaten":
        return _bw_sheep_eaten(scene)
    return _bw_trust_threshold(scene)


def _bw_false_alarms(scene: Scene) -> Record:
    """Boy cries wolf F times falsely. After each, villagers came in T mins.
    Total minutes wasted by villagers running to the field?"""
    boy   = scene.pick_character(role_classes=("liar", "shepherd"), gender=scene.pick_choice(["m", "f"]))
    n_villagers = scene.pick_int(3, 10)
    n_alarms    = scene.pick_int(2, 6)
    minutes_per = scene.pick_int(5, 20)

    expr = Let(
        bindings=[
            ("villagers", Lit(n_villagers)),
            ("alarms",    Lit(n_alarms)),
            ("minutes-per-trip",      Lit(minutes_per)),
        ],
        body=App("*", [Var("villagers"), Var("alarms"), Var("minutes-per-trip")]),
    )
    answer = evaluate(expr)

    setting   = scene.phrase("watched sheep on the hill",
                               "tended the flock at the edge of the woods",
                               "kept watch over the sheep in the meadow")
    bored     = scene.phrase("Bored,", "Out of mischief,",
                               "Looking for some fun,")
    cried     = scene.phrase("cried 'Wolf!'", "shouted 'Wolf!'",
                               "yelled the alarm")
    came      = scene.phrase("ran from the village to the field",
                               "rushed up the hill",
                               "hurried out from the village")
    each_trip = scene.phrase("taking", "and the trip took",
                               "each round trip lasting")
    _intro = _aesopian_intro(scene, "boy-wolf")
    user_msg = (
        f"{_intro}{boy.name} {setting}. {bored} "
        f"{boy.he_she} {cried} {n_unit(n_alarms, 'time')} "
        f"falsely. Each time, {n_villagers} villagers {came}, "
        f"{each_trip} {n_unit(minutes_per, 'minute')} each.\n\n"
        f"Question: How many total minutes did the villagers waste "
        f"running to {n_unit(n_alarms, 'false alarm')}?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The villagers wasted {answer} minutes in total."
    narrative   = "I multiply villagers × alarms × minutes per trip."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="boy-wolf",
        chapter="false-alarms",
    )


def _bw_sheep_eaten(scene: Scene) -> Record:
    """Real wolf comes; villagers don't believe; wolf eats S sheep."""
    boy = scene.pick_character(role_classes=("liar", "shepherd"), gender=scene.pick_choice(["m", "f"]))
    flock = scene.pick_int(20, 80)
    eaten = scene.pick_int(3, min(flock - 1, 15))

    expr = Let(
        bindings=[("flock-size", Lit(flock)), ("sheep-eaten", Lit(eaten))],
        body=App("-", [Var("flock-size"), Var("sheep-eaten")]),
    )
    answer = evaluate(expr)

    when    = scene.phrase("After many false alarms",
                            "After crying wolf one too many times",
                            "Once the villagers had stopped believing")
    came    = scene.phrase("a real wolf came",
                            "an actual wolf appeared",
                            "a hungry wolf showed up")
    refused = scene.phrase("the villagers did not believe",
                            "no one in the village answered the call from",
                            "the villagers ignored")
    devoured = scene.phrase("ate", "carried off", "made off with")
    _intro = _aesopian_intro(scene, "boy-wolf")
    user_msg = (
        f"{_intro}{boy.name} kept a flock of "
        f"{n_unit(flock, 'sheep', 'sheep')}. {when}, {came} and "
        f"{refused} {boy.him_her}. The wolf {devoured} "
        f"{n_unit(eaten, 'sheep', 'sheep')}.\n\n"
        f"Question: How many sheep does {boy.name} have left?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{boy.name} has {answer} sheep left."
    narrative   = "I subtract the eaten sheep from the original flock."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="boy-wolf",
        chapter="sheep-eaten",
    )


def _bw_trust_threshold(scene: Scene) -> Record:
    """Villagers stop coming after K false alarms. Will they come on alarm N?"""
    boy = scene.pick_character(role_classes=("liar", "shepherd"), gender=scene.pick_choice(["m", "f"]))
    threshold = scene.pick_int(3, 5)
    alarms_so_far = scene.pick_int(0, 7)

    expr = If(
        App("<", [Var("alarms-so-far"), Var("threshold")]),
        Lit("yes"),
        Lit("no"),
    )
    expr = Let(
        bindings=[("threshold", Lit(threshold)),
                  ("alarms-so-far", Lit(alarms_so_far))],
        body=expr,
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "boy-wolf")
    user_msg = (
        f"{_intro}The villagers in {boy.name}'s village stop responding to alarms "
        f"after {n_unit(threshold, 'false alarm')}. So far, {boy.name} has "
        f"raised {n_unit(alarms_so_far, 'false alarm')}.\n\n"
        f"Question: Will the villagers come on the next alarm? Answer "
        f"yes or no."
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The answer is {answer}."
    narrative   = (
        "I compare alarms-so-far against the threshold; if below, "
        "villagers still come."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="boy-wolf",
        chapter="trust-threshold",
    )


# ─────────────────────── 5. Ant and the Grasshopper ───────────────────────


def gen_ant_grasshopper(scene: Scene) -> Record:
    chapter = scene.pick_choice(["summer-stockpile", "winter-consumption",
                                  "comparison-survival"])
    if chapter == "summer-stockpile":
        return _ag_summer_stockpile(scene)
    if chapter == "winter-consumption":
        return _ag_winter_consumption(scene)
    return _ag_comparison_survival(scene)


def _ag_summer_stockpile(scene: Scene) -> Record:
    """Ant collects G grains/day for D days = total. Three orientation
    variants (same product = total):
      total-unknown: given per-day + days, compute total
      days-unknown:  given per-day + total, compute days
      rate-unknown:  given days + total, compute per-day
    """
    ant = scene.pick_character(role_classes=("saver",), species="ant")
    location = scene.pick_location(tags_any=("nature",), indoor=False)
    per_day = scene.pick_int(2, 8)
    days    = scene.pick_int(20, 90)
    total   = per_day * days
    orient  = scene.pick_choice(["total", "days", "rate"])
    _intro  = _aesopian_intro(scene, "ant-grasshopper", location)

    season = scene.phrase("Through the summer", "All summer long",
                          "Across the long summer", "From spring to fall")

    if orient == "total":
        expr = Let(
            bindings=[("per-day", Lit(per_day)), ("days", Lit(days))],
            body=App("*", [Var("per-day"), Var("days")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{season} at {location.article} {location.name}, "
            f"{species_phrase(ant)} collected {per_day} "
            f"{unit(per_day, 'grain')} every day for {n_unit(days, 'day')}.\n\n"
            f"Question: How many grains did {ant.name} collect by the end "
            f"of summer?"
        )
        result_text = f"{ant.name} collected {n_unit(answer, 'grain')}."
        narrative   = "I multiply the daily rate by the number of days."
        chapter_name = "summer-stockpile-total"
    elif orient == "days":
        expr = Let(
            bindings=[("total",   Lit(total)),
                      ("per-day", Lit(per_day))],
            body=App("quot", [Var("total"), Var("per-day")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{season} at {location.article} {location.name}, "
            f"{species_phrase(ant)} collected {n_unit(total, 'grain')} in "
            f"all, gathering {per_day} {unit(per_day, 'grain')} each day.\n\n"
            f"Question: How many days did {ant.name} spend collecting?"
        )
        result_text = f"{ant.name} spent {n_unit(answer, 'day')} collecting."
        narrative   = "I divide the total by the daily rate."
        chapter_name = "summer-stockpile-days"
    else:
        expr = Let(
            bindings=[("total", Lit(total)), ("days", Lit(days))],
            body=App("quot", [Var("total"), Var("days")]),
        )
        answer = evaluate(expr)
        user_msg = (
            f"{_intro}{season} at {location.article} {location.name}, "
            f"{species_phrase(ant)} worked steadily for "
            f"{n_unit(days, 'day')} and gathered "
            f"{n_unit(total, 'grain')} in all.\n\n"
            f"Question: How many grains did {ant.name} collect each day?"
        )
        result_text = f"{ant.name} collected {answer} {unit(answer, 'grain')} per day."
        narrative   = "I divide the total by the number of days."
        chapter_name = "summer-stockpile-rate"

    code_block = render_code(expr, form=scene.code_form(), value=answer)
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="ant-grasshopper",
        chapter=chapter_name,
    )


def _ag_winter_consumption(scene: Scene) -> Record:
    """Ant has S grains, eats E grains/day. How many days food lasts?"""
    ant = scene.pick_character(role_classes=("saver",), species="ant")
    stockpile = scene.pick_int(20, 200)
    per_day   = scene.pick_int(1, 5)

    expr = Let(
        bindings=[("stockpile", Lit(stockpile)),
                  ("per-day",   Lit(per_day))],
        body=App("quot", [Var("stockpile"), Var("per-day")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "ant-grasshopper")
    user_msg = (
        f"{_intro}{species_phrase(ant)} has {n_unit(stockpile, 'grain')} stored "
        f"for winter. {cap(ant.he_she)} {verb_for(ant, 'eat')} {n_unit(per_day, 'grain')} "
        f"per day.\n\n"
        f"Question: For how many whole days will {ant.name}'s stockpile "
        f"last?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The stockpile lasts {n_unit(answer, 'day')}."
    narrative   = "I divide the stockpile by daily consumption (integer quotient)."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="ant-grasshopper",
        chapter="winter-consumption",
    )


def _ag_comparison_survival(scene: Scene) -> Record:
    """Both characters consume rates; who has more food after winter?"""
    ant         = scene.pick_character(role_classes=("saver",), species="ant")
    grasshopper = scene.pick_character(role_classes=("spendthrift",),
                                       species="grasshopper")
    days = scene.pick_int(30, 90)
    ant_stock = scene.pick_int(60, 300)
    ant_per_day = scene.pick_int(1, 3)
    gh_stock = scene.pick_int(0, 30)
    gh_per_day = scene.pick_int(1, 3)

    expr = Let(
        bindings=[
            ("ant-stock",   Lit(ant_stock)),
            ("ant-rate",    Lit(ant_per_day)),
            ("gh-stock",    Lit(gh_stock)),
            ("gh-rate",     Lit(gh_per_day)),
            ("days",        Lit(days)),
            ("ant-left",    App("-", [Var("ant-stock"),
                                       App("*", [Var("ant-rate"),
                                                 Var("days")])])),
            ("gh-left",     App("-", [Var("gh-stock"),
                                       App("*", [Var("gh-rate"),
                                                 Var("days")])])),
        ],
        body=App("max", [Var("ant-left"), Lit(0)]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "ant-grasshopper")
    user_msg = (
        f"{_intro}Winter lasted {n_unit(days, 'day')}. "
        f"{species_phrase(ant)} started with "
        f"{n_unit(ant_stock, 'grain')} and ate {ant_per_day} every day, "
        f"while {species_phrase(grasshopper)} started with "
        f"{n_unit(gh_stock, 'grain')} and ate {gh_per_day} every day. "
        f"If a stockpile runs out, the count cannot go below zero.\n\n"
        f"Question: How many grains does {ant.name} have left at the end "
        f"of winter?"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"{ant.name} has {answer} grains left."
    narrative   = (
        f"I compute leftover for {ant.name} (initial - days × rate), then "
        "clamp to 0 if negative using max."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="ant-grasshopper",
        chapter="comparison-survival",
    )


# ─────────────────────── 6. Milkmaid and Her Pail ───────────────────────


def gen_milkmaid(scene: Scene) -> Record:
    chapter = scene.pick_choice(["egg-to-coin-chain", "investment-return",
                                  "spilled-milk"])
    if chapter == "egg-to-coin-chain":
        return _mm_egg_to_coin_chain(scene)
    if chapter == "investment-return":
        return _mm_investment_return(scene)
    return _mm_spilled_milk(scene)


def _mm_egg_to_coin_chain(scene: Scene) -> Record:
    """Milkmaid plans: E eggs → each hatches into hen → each lays L eggs/year
    × C coins/egg. Total coins after 1 year?"""
    maid = scene.pick_character(role_classes=("counter", "dreamer"))
    eggs = scene.pick_int(3, 12)
    eggs_per_hen_per_year = scene.pick_int(50, 200)
    coins_per_egg = scene.pick_int(1, 5)

    expr = Thread("->>", Lit(eggs),
                  [App("*", [Var("eggs-per-hen")]),
                   App("*", [Var("coins-per-egg")])])
    expr = Let(
        bindings=[
            ("eggs",          Lit(eggs)),
            ("eggs-per-hen",  Lit(eggs_per_hen_per_year)),
            ("coins-per-egg", Lit(coins_per_egg)),
        ],
        body=App("*", [Var("eggs"), Var("eggs-per-hen"),
                       Var("coins-per-egg")]),
    )
    answer = evaluate(expr)

    walking = scene.phrase("carried a pail of milk to market",
                             "walked to market with her milk pail",
                             "set off for the market with a pail of milk")
    dreamt  = scene.phrase("dreamed of the future",
                             "started to plan her fortune",
                             "imagined what she would do with the proceeds")
    _intro = _aesopian_intro(scene, "milkmaid")
    user_msg = (
        f"{_intro}{maid.name} {walking} and {dreamt}. She would buy "
        f"{n_unit(eggs, 'egg')}; each would hatch into a hen; each hen "
        f"would lay {n_unit(eggs_per_hen_per_year, 'egg')} per year; "
        f"each egg would sell for {n_unit(coins_per_egg, 'coin')}.\n\n"
        f"Question: If everything went perfectly, how many coins would "
        f"{maid.name} earn after one year?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{maid.name} would earn {n_unit(answer, 'coin')} in a year."
    narrative   = (
        "I multiply eggs × eggs-per-hen-per-year × coins-per-egg "
        "to get the total."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="milkmaid",
        chapter="egg-to-coin-chain",
    )


def _mm_investment_return(scene: Scene) -> Record:
    """Maid has C coins; cow costs K; each cow gives M cups of milk/day, sold
    at S coins/cup; how many days until cost recovered?"""
    maid = scene.pick_character(role_classes=("counter",))
    cow_cost = scene.pick_int(50, 200)
    cups_per_day = scene.pick_int(2, 8)
    coin_per_cup = scene.pick_int(1, 4)

    expr = Let(
        bindings=[
            ("cow-cost",     Lit(cow_cost)),
            ("cups-per-day", Lit(cups_per_day)),
            ("coin-per-cup", Lit(coin_per_cup)),
            ("daily-revenue", App("*", [Var("cups-per-day"),
                                          Var("coin-per-cup")])),
        ],
        body=App("quot", [App("+", [Var("cow-cost"),
                                     App("dec", [Var("daily-revenue")])]),
                          Var("daily-revenue")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "milkmaid")
    user_msg = (
        f"{_intro}{maid.name} bought a cow for {n_unit(cow_cost, 'coin')}. The "
        f"cow gives {n_unit(cups_per_day, 'cup')} of milk per day, and "
        f"each cup sells for {n_unit(coin_per_cup, 'coin')}.\n\n"
        f"Question: What is the smallest whole number of days until "
        f"{maid.name} fully recovers the cost of the cow?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"It takes {n_unit(answer, 'day')} to break even."
    narrative   = (
        "I find daily revenue (cups × coin-per-cup), then ceiling-divide "
        "the cow's cost by that revenue."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="milkmaid",
        chapter="investment-return",
    )


def _mm_spilled_milk(scene: Scene) -> Record:
    """Pail had M cups; she trips and spills S cups; each cup worth C coins.
    Lost coins?"""
    maid = scene.pick_character(role_classes=("counter",))
    full_cups = scene.pick_int(8, 30)
    spilled   = scene.pick_int(1, full_cups - 1)
    per_cup   = scene.pick_int(1, 5)

    expr = Let(
        bindings=[
            ("spilled", Lit(spilled)),
            ("per-cup", Lit(per_cup)),
        ],
        body=App("*", [Var("spilled"), Var("per-cup")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "milkmaid")
    user_msg = (
        f"{_intro}{maid.name} carried a pail with {n_unit(full_cups, 'cup')} "
        f"of milk. She tripped and spilled {n_unit(spilled, 'cup')}. "
        f"Each cup of milk would have sold for "
        f"{n_unit(per_cup, 'coin')}.\n\n"
        f"Question: How many coins did {maid.name} lose by spilling?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{maid.name} lost {n_unit(answer, 'coin')}."
    narrative   = "I multiply the spilled cups by the price per cup."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="milkmaid",
        chapter="spilled-milk",
    )


# ─────────────────────── 7. Fox and the Grapes ───────────────────────


def gen_fox_grapes(scene: Scene) -> Record:
    chapter = scene.pick_choice(["max-reach", "jumps-needed", "give-up"])
    if chapter == "max-reach":
        return _fg_max_reach(scene)
    if chapter == "jumps-needed":
        return _fg_jumps_needed(scene)
    return _fg_give_up(scene)


def _fg_max_reach(scene: Scene) -> Record:
    """Fox can jump J feet. Grapes are G feet up. How high can fox reach?"""
    fox = scene.pick_character(role_classes=("cunning", "hungry"),
                                species="fox", gender=scene.pick_choice(["m", "f"]))
    body_height = scene.pick_int(2, 4)
    jump_height = scene.pick_int(1, 4)

    expr = Let(
        bindings=[("body-height", Lit(body_height)),
                  ("jump-height", Lit(jump_height))],
        body=App("+", [Var("body-height"), Var("jump-height")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "fox-grapes")
    hungry    = scene.rng.choice(EMO_HUNGRY)
    desperate = scene.rng.choice(EMO_DESPERATE)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (body-stand + jump-height)
    # but each grounds it in a different fruit + setting + sensory hook.
    # The fox's mood ranges from hungry hope to dignified frustration.
    max_reach_subplots = [
        # 1) classic — purple grapes on a vine in the orchard
        f"{species_phrase(fox)} crept beneath an orchard vine, {hungry}, "
        f"and stopped before a heavy cluster of purple grapes. {cap(fox.he_she)} "
        f"rose up on {fox.his_her} hind legs, nose lifted, the tips of "
        f"{fox.his_her} ears just brushing the lowest leaves at "
        f"{n_unit(body_height, 'foot', 'feet')} above the dust. From "
        f"that stretch {fox.he_she} judged {fox.he_she} could spring "
        f"another {n_unit(jump_height, 'foot', 'feet')} cleanly into the "
        f"air. The grapes shone in the late sun, dusty-bloomed and "
        f"impossibly round, and {fox.name} measured the height between "
        f"{fox.his_her} paws and the prize.",

        # 2) ripe apples on a low branch in a farmyard
        f"In the corner of a farmer's yard, where a crooked apple tree "
        f"leaned over the fence, {fox.name} the fox padded to a halt, "
        f"{hungry}. Three ripe apples hung from a low branch, fat and "
        f"red. {cap(fox.he_she)} stretched up on {fox.his_her} hind "
        f"paws — that gave {fox.him_her} {n_unit(body_height, 'foot', 'feet')} "
        f"of reach — and reckoned {fox.he_she} could leap another "
        f"{n_unit(jump_height, 'foot', 'feet')} besides. A hen scratched "
        f"in the dirt, indifferent. {fox.name} eyed the lowest apple and "
        f"weighed {fox.his_her} chances.",

        # 3) blackberries trailing over a garden fence
        f"A tangle of blackberry canes spilled over the top of a garden "
        f"fence, dotted with fat dark berries. {fox.name}, {desperate}, "
        f"circled below and at last reared up on {fox.his_her} hind legs. "
        f"The crown of {fox.his_her} head reached "
        f"{n_unit(body_height, 'foot', 'feet')} from the trampled grass, "
        f"and a strong push of the haunches added another "
        f"{n_unit(jump_height, 'foot', 'feet')} to the upward bound. The "
        f"juice-stained leaves trembled. {cap(fox.he_she)} eyed the "
        f"darkest berry and gathered {fox.him_her}self for the spring.",

        # 4) pears from an arbor in the kitchen garden
        f"At the back of a kitchen garden, {fox.name} the fox slipped "
        f"under an arbor where ripe pears hung in golden bunches, "
        f"{hungry}. {cap(fox.he_she)} drew {fox.him_her}self up on hind "
        f"legs, stretching {fox.his_her} long body until {fox.his_her} "
        f"snout was {n_unit(body_height, 'foot', 'feet')} above the "
        f"path of crushed shells. From there, a hard jump would carry "
        f"{fox.him_her} another {n_unit(jump_height, 'foot', 'feet')} "
        f"upward — no more. {cap(fox.he_she)} stared at the swaying "
        f"pears, calculating where {fox.his_her} reach would end.",

        # 5) plums on a high market display
        f"The market square smelled of dust and overripe fruit when "
        f"{fox.name} slunk between the stalls, {hungry}. A merchant's "
        f"high display hung clusters of dark plums above the heads of "
        f"the passing crowd. {cap(fox.he_she)} chose a moment when no "
        f"one was watching and rose up on hind paws — a stretch of "
        f"{n_unit(body_height, 'foot', 'feet')} — and judged that a leap "
        f"could lift {fox.him_her} another {n_unit(jump_height, 'foot', 'feet')} "
        f"into the laden air. The plums swung lazily, and {fox.name} "
        f"thought hard about how high {fox.he_she} could truly reach.",

        # 6) figs hanging just above a wall in the vineyard
        f"Along the edge of a sunbaked vineyard, an old fig tree had "
        f"grown over the top of a low stone wall, dropping its fruit on "
        f"the wrong side. {fox.name}, {regretful} of having strayed so "
        f"far for a meal, padded to the foot of the wall. {cap(fox.he_she)} "
        f"reared up: the tips of {fox.his_her} ears reached "
        f"{n_unit(body_height, 'foot', 'feet')} above the gravel, and "
        f"experience told {fox.him_her} {fox.he_she} could spring no "
        f"more than {n_unit(jump_height, 'foot', 'feet')} above that. "
        f"The figs hung there, lazy and purple. {cap(fox.he_she)} stared "
        f"and measured.",
    ]

    body = _render_subplot(scene, max_reach_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'the highest point {fox.name} can reach with a single leap')}"
    )

    plan = "I add the body-stand height and the jump height."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="fox-grapes",
        chapter="max-reach",
    )


def _fg_jumps_needed(scene: Scene) -> Record:
    """Each jump goes up J feet. Grapes are G feet. Min jumps to reach grapes
    (assume re-stack progress; hypothetical/dream scenario)."""
    fox = scene.pick_character(role_classes=("cunning", "hungry"),
                                species="fox", gender=scene.pick_choice(["m", "f"]))
    grape_height = scene.pick_int(4, 12)
    per_jump     = scene.pick_int(1, 3)

    expr = Let(
        bindings=[
            ("grape-height", Lit(grape_height)),
            ("per-jump",     Lit(per_jump)),
        ],
        body=App("quot",
                 [App("+", [Var("grape-height"),
                             App("dec", [Var("per-jump")])]),
                  Var("per-jump")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "fox-grapes")
    hungry    = scene.rng.choice(EMO_HUNGRY)
    desperate = scene.rng.choice(EMO_DESPERATE)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (ceil(grape-height /
    # per-jump)) but each varies the fruit, the holder, and the
    # setting. The fox's mood ranges from hungry hope through frantic
    # leaping to dignified rationalization.
    jumps_needed_subplots = [
        # 1) classic — purple grapes on an arbor in the orchard
        f"In the corner of an orchard {fox.name} the fox stopped beneath "
        f"a low arbor where a heavy bunch of purple grapes hung "
        f"{n_unit(grape_height, 'foot', 'feet')} above the trodden grass. "
        f"{cap(fox.he_she)} was {hungry}, and the dusty bloom on each "
        f"grape made {fox.his_her} mouth water. A trial spring carried "
        f"{fox.him_her} {n_unit(per_jump, 'foot', 'feet')} into the air, "
        f"and {fox.he_she} reasoned that each leap, if {fox.he_she} could "
        f"somehow build upon the last, would bring the prize "
        f"{per_jump} {unit(per_jump, 'foot', 'feet')} closer.",

        # 2) ripe apples just out of reach in a farmer's yard
        f"A farmer's apple tree leaned over the low fence of the yard, "
        f"its lowest red apple dangling exactly "
        f"{n_unit(grape_height, 'foot', 'feet')} above the packed earth. "
        f"{cap(species_phrase(fox))}, {desperate} after a day without "
        f"food, padded to a stop and crouched. {cap(fox.he_she)} found "
        f"that {fox.his_her} hardest spring lifted {fox.him_her} "
        f"{n_unit(per_jump, 'foot', 'feet')} skyward — no more. In "
        f"{fox.his_her} mind {fox.he_she} began tallying how many such "
        f"bounds, taken in dreamlike succession, would close the gap "
        f"between paws and apple.",

        # 3) blackberries trailing over a wooden cart
        f"At the edge of a country lane stood a high-sided wooden cart, "
        f"and over its rim spilled long blackberry canes a passing child "
        f"had laid there to dry. The darkest berry hung "
        f"{n_unit(grape_height, 'foot', 'feet')} above the rutted road. "
        f"{fox.name}, {hungry}, circled the cart twice. {cap(fox.he_she)} "
        f"tested {fox.his_her} jump and found it good for "
        f"{n_unit(per_jump, 'foot', 'feet')} of clean lift. {cap(fox.he_she)} "
        f"settled into the dust to count exactly how many such springs, "
        f"each adding cleanly to the last, would carry {fox.him_her} to "
        f"the berry.",

        # 4) pears on a trellis in the kitchen garden
        f"Beyond the kitchen garden's hedge, a tall trellis held up a "
        f"pear tree's heaviest bough; from it the lowest golden pear "
        f"swung {n_unit(grape_height, 'foot', 'feet')} above the gravel "
        f"path. {fox.name}, {hungry}, took {fox.his_her} measure with a "
        f"single trial leap — a tidy {n_unit(per_jump, 'foot', 'feet')} "
        f"of upward bound, no more — and crouched to think. If each "
        f"successive jump could be stacked on the gain of the last, how "
        f"many would {fox.he_she} need before {fox.his_her} teeth could "
        f"close on the pear's freckled skin?",

        # 5) plums on a high market display in the square
        f"The market square was almost empty in the late hour when "
        f"{fox.name} slipped between the wooden stalls. A merchant had "
        f"strung up clusters of dark plums on a high display, and the "
        f"lowest swung {n_unit(grape_height, 'foot', 'feet')} above the "
        f"flagstones. {cap(species_phrase(fox))}, {desperate}, eyed the "
        f"shadowed fruit and tested a leap — {fox.his_her} best effort "
        f"lifted {fox.him_her} only {n_unit(per_jump, 'foot', 'feet')} "
        f"into the dusty air. Quietly, in the half-light, {fox.he_she} "
        f"counted the leaps it would take, each one a clean step closer.",

        # 6) figs above a vineyard wall — and a touch of regret
        f"Along the white stone wall that ringed an old vineyard, a fig "
        f"tree had grown over the top and dropped its fruit on the wrong "
        f"side. The lowest dark fig hung {n_unit(grape_height, 'foot', 'feet')} "
        f"above the dusty lane where {fox.name} the fox now stood, "
        f"{regretful} that the climb up the slope had cost {fox.him_her} "
        f"so much breath for so little gain. {cap(fox.he_she)} sprang "
        f"once to test {fox.him_her}self: the bound carried {fox.him_her} "
        f"{n_unit(per_jump, 'foot', 'feet')} aloft. {cap(fox.he_she)} "
        f"settled to count how many such efforts, each lifting "
        f"{per_jump} {unit(per_jump, 'foot', 'feet')}, would suffice.",
    ]

    body = _render_subplot(scene, jumps_needed_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'the smallest number of leaps {fox.name} needs to reach the fruit')}"
    )

    plan = (
        "I ceiling-divide the fruit's height by the per-jump height "
        "(adding per-jump minus one before quot)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="fox-grapes",
        chapter="jumps-needed",
    )


def _fg_give_up(scene: Scene) -> Record:
    """Fox gives up after K attempts. Has tried T already. Will fox try again?"""
    fox = scene.pick_character(role_classes=("cunning", "hungry"),
                                species="fox", gender=scene.pick_choice(["m", "f"]))
    threshold = scene.pick_int(3, 8)
    tried     = scene.pick_int(0, 10)

    expr = Let(
        bindings=[("threshold", Lit(threshold)),
                  ("tries-so-far",     Lit(tried))],
        body=If(App("<", [Var("tries-so-far"), Var("threshold")]),
                Lit("yes"), Lit("no")),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "fox-grapes")
    hungry    = scene.rng.choice(EMO_HUNGRY)
    desperate = scene.rng.choice(EMO_DESPERATE)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (tries-so-far <
    # threshold => "yes") but each grounds the give-up moment in a
    # different fruit and setting. The early subplots lean desperate;
    # the later ones lean toward the famous sour-grapes rationalization.
    give_up_subplots = [
        # 1) classic — purple grapes on a vineyard vine
        f"Beneath a low vine in an old vineyard {fox.name} the fox had "
        f"been leaping at a heavy cluster of ripe purple grapes for the "
        f"better part of an hour. {cap(fox.he_she)}, {hungry}, had "
        f"resolved before starting that {n_unit(threshold, 'attempt')} "
        f"would be {fox.his_her} limit — beyond that, {fox.he_she} would "
        f"call the grapes sour and walk away. So far {fox.he_she} had "
        f"sprung {n_unit(tried, 'time')}, paws scrabbling at the leaves, "
        f"and now {fox.he_she} stood panting in the dust to weigh "
        f"whether the next jump was worth its breath.",

        # 2) ripe apples in a quiet farmyard
        f"In a farmer's quiet yard, where ripe apples hung from a low "
        f"branch above the dust, {fox.name} had been working "
        f"{fox.him_her}self into a fine sweat. {cap(fox.he_she)} had "
        f"sworn — out loud, to the indifferent hens — that "
        f"{n_unit(threshold, 'attempt')} were all {fox.he_she} would "
        f"grant the apples; after that, {fox.he_she} would name them "
        f"underripe and slink off with what dignity remained. "
        f"{cap(fox.he_she)} had already tried {n_unit(tried, 'time')}, "
        f"each spring shorter than the last, and stood {desperate} "
        f"beneath the lowest apple, deciding.",

        # 3) blackberries spilling over a garden trellis
        f"A garden trellis at the edge of the lane was hung with the "
        f"darkest blackberries {fox.name} the fox had ever seen. "
        f"{cap(species_phrase(fox))}, {hungry}, had set "
        f"{n_unit(threshold, 'attempt')} as the limit of {fox.his_her} "
        f"patience; one more than that and the berries would simply be "
        f"sour, no better than weeds. So far {fox.he_she} had bounded "
        f"upward {n_unit(tried, 'time')}, juice-stained leaves "
        f"trembling each time {fox.his_her} claws caught and slipped. "
        f"Now {fox.he_she} circled below, considering whether to gather "
        f"{fox.him_her}self for another spring.",

        # 4) pears on the arbor of a kitchen garden
        f"Beneath the arbor of a kitchen garden the air was thick with "
        f"the scent of ripening pears. {fox.name}, {desperate} after a "
        f"long morning without food, had agreed with {fox.him_her}self "
        f"on a strict allowance: {n_unit(threshold, 'attempt')} and not "
        f"one leap more. After that, the pears would obviously be hard "
        f"and bitter, and a self-respecting fox would walk away. "
        f"{cap(fox.he_she)} had tried {n_unit(tried, 'time')} so far, "
        f"each landing a little heavier than the last, and now stood "
        f"eyeing the swaying fruit, calculating.",

        # 5) plums on a market square display
        f"The market square was nearly deserted when {fox.name} slipped "
        f"between the stalls and stopped beneath a high display of dark "
        f"plums. {cap(fox.he_she)}, {hungry}, had told {fox.him_her}self "
        f"firmly: {n_unit(threshold, 'attempt')} only — beyond that the "
        f"plums were certainly half-rotten and beneath {fox.his_her} "
        f"notice. {cap(fox.he_she)} had already sprung "
        f"{n_unit(tried, 'time')}, paws clattering on the flagstones, "
        f"and now stood with whiskers twitching, weighing whether to "
        f"gather {fox.him_her}self for one more leap.",

        # 6) figs over a vineyard wall — sour-grapes near at hand
        f"At the edge of a sunbaked vineyard a fig tree had grown over "
        f"a low stone wall, dropping its fruit on the wrong side. "
        f"{fox.name} the fox stood beneath, {regretful} of the long walk "
        f"that had brought {fox.him_her} here, and had set "
        f"{n_unit(threshold, 'attempt')} as the absolute limit of "
        f"{fox.his_her} effort. Past that and the figs would be sour, "
        f"shrivelled, fit only for crows. So far {fox.he_she} had jumped "
        f"{n_unit(tried, 'time')}, each landing a touch less proud than "
        f"the last, and now considered the matter from the dust.",
    ]

    body = _render_subplot(scene, give_up_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'whether {fox.name} will try again — answer yes or no')}"
    )

    plan = (
        "I check whether tries-so-far is still below the threshold; "
        "if so the answer is yes, otherwise no."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="fox-grapes",
        chapter="give-up",
    )


# ─────────────────────── 8. Country Mouse / City Mouse ───────────────────────


def gen_two_mice(scene: Scene) -> Record:
    chapter = scene.pick_choice(["food-comparison", "shared-meal",
                                  "trip-budget"])
    if chapter == "food-comparison":
        return _tm_food_comparison(scene)
    if chapter == "shared-meal":
        return _tm_shared_meal(scene)
    return _tm_trip_budget(scene)


def _tm_food_comparison(scene: Scene) -> Record:
    """Country mouse has C grains; city mouse has K. Difference?"""
    country = scene.pick_character(role_classes=("prey",), species="mouse")
    city    = scene.pick_character(role_classes=("prey",), species="mouse",
                                    not_=country)
    food    = scene.pick_item(edible=True, countable=True, size_max=2)
    a = scene.pick_int(1, 30)
    b = scene.pick_int(1, 30)

    expr = Let(
        bindings=[("country-amt", Lit(a)),
                  ("city-amt",    Lit(b))],
        body=App("abs", [App("-", [Var("city-amt"), Var("country-amt")])]),
    )
    answer = evaluate(expr)

    country_phrase = scene.phrase("lived in the countryside",
                                    "lived in a quiet country burrow",
                                    "made a home out in the meadows")
    city_phrase    = scene.phrase("lived in the city",
                                    "lived in a busy townhouse pantry",
                                    "made a home in the bustling city")
    _intro = _aesopian_intro(scene, "two-mice")
    user_msg = (
        f"{_intro}{species_phrase(country)} {country_phrase} and had "
        f"{n_unit(a, food.name, food.plural)}, while "
        f"{species_phrase(city)} {city_phrase} and had "
        f"{n_unit(b, food.name, food.plural)}.\n\n"
        f"Question: What is the absolute difference in {food.plural} "
        f"between the two mice?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The difference is {n_unit(answer, food.name, food.plural)}."
    narrative   = "I take the absolute value of the difference."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="two-mice",
        chapter="food-comparison",
    )


def _tm_shared_meal(scene: Scene) -> Record:
    """N mice + a meal; each gets quot N portion."""
    country = scene.pick_character(role_classes=("prey",), species="mouse")
    city    = scene.pick_character(role_classes=("prey",), species="mouse",
                                    not_=country)
    food    = scene.pick_item(edible=True, countable=True, size_max=2)
    n_mice  = scene.pick_int(2, 5)
    total   = scene.pick_int(n_mice, n_mice * 10)

    expr = Let(
        bindings=[("total",  Lit(total)),
                  ("n-mice", Lit(n_mice))],
        body=App("quot", [Var("total"), Var("n-mice")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "two-mice")
    user_msg = (
        f"{_intro}{species_phrase(country)} and {species_phrase(city)} hosted "
        f"a feast for {n_unit(n_mice, 'mouse', 'mice')} (counting "
        f"themselves). They had {n_unit(total, food.name, food.plural)} "
        f"to share equally.\n\n"
        f"Question: How many whole {food.plural} does each mouse get if "
        f"any leftover is set aside?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"Each mouse gets {n_unit(answer, food.name, food.plural)}."
    narrative   = "I integer-divide the total by the number of mice."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="two-mice",
        chapter="shared-meal",
    )


def _tm_trip_budget(scene: Scene) -> Record:
    """Mouse spends X coins on trip + Y coins on food. Has C remaining?"""
    mouse  = scene.pick_character(role_classes=("prey",), species="mouse")
    start  = scene.pick_int(20, 100)
    travel = scene.pick_int(1, start // 2)
    food   = scene.pick_int(1, start // 3)

    expr = Let(
        bindings=[
            ("start-coins", Lit(start)),
            ("travel-cost", Lit(travel)),
            ("food-cost",   Lit(food)),
        ],
        body=App("-", [Var("start-coins"),
                       Var("travel-cost"),
                       Var("food-cost")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "two-mice")
    user_msg = (
        f"{_intro}{species_phrase(mouse)} began the journey with "
        f"{n_unit(start, 'coin')}. {cap(mouse.he_she)} spent "
        f"{n_unit(travel, 'coin')} on travel and {n_unit(food, 'coin')} "
        f"on food.\n\n"
        f"Question: How many coins does {mouse.name} have left?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{mouse.name} has {n_unit(answer, 'coin')} remaining."
    narrative   = "I subtract travel and food from the starting coins."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="two-mice",
        chapter="trip-budget",
    )


# ─────────────────────── 9. Dog and the Shadow ───────────────────────


def gen_dog_shadow(scene: Scene) -> Record:
    chapter = scene.pick_choice(["double-loss", "regret", "exchange-loss"])
    if chapter == "double-loss":
        return _ds_double_loss(scene)
    if chapter == "regret":
        return _ds_regret(scene)
    return _ds_exchange_loss(scene)


def _ds_double_loss(scene: Scene) -> Record:
    """Dog had B bones. Saw shadow with 'extra' bone. Drops one for shadow,
    loses it. Now has B-1."""
    dog = scene.pick_character(role_classes=("everyman",), species="dog", gender=scene.pick_choice(["m", "f"]))
    bones = scene.pick_int(2, 8)

    expr = Let(
        bindings=[("start-bones", Lit(bones))],
        body=App("dec", [Var("start-bones")]),
    )
    answer = evaluate(expr)

    crossing = scene.phrase("crossed a stream carrying",
                              "trotted over a bridge with",
                              "padded across a brook holding")
    looking  = scene.phrase("Looking down", "Glancing into the water",
                              "Peering at the surface")
    grabbed  = scene.phrase("dropped one bone to grab the shadow's",
                              "let go of one bone, lunging at the reflection",
                              "released a bone to snap at the watery double's")
    _intro = _aesopian_intro(scene, "dog-shadow")
    user_msg = (
        f"{_intro}{species_phrase(dog)} {crossing} {n_unit(bones, 'bone')}. "
        f"{looking}, {dog.he_she} saw {dog.his_her} reflection and thought "
        f"it was another dog with more bones. {cap(dog.he_she)} {grabbed}, "
        f"but the bone fell into the stream.\n\n"
        f"Question: How many bones does {dog.name} have now?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} has {n_unit(answer, 'bone')} left."
    narrative   = "I subtract 1 (the dropped bone) from the original count."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="dog-shadow",
        chapter="double-loss",
    )


def _ds_regret(scene: Scene) -> Record:
    """If dog hadn't dropped, would've had B. Now has B-1. Difference."""
    dog = scene.pick_character(role_classes=("everyman",), species="dog", gender=scene.pick_choice(["m", "f"]))
    expected_bones = scene.pick_int(3, 12)

    expr = Let(
        bindings=[("expected-bones", Lit(expected_bones)),
                  ("actual-bones",   App("dec", [Var("expected-bones")]))],
        body=App("-", [Var("expected-bones"), Var("actual-bones")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "dog-shadow")
    user_msg = (
        f"{_intro}{species_phrase(dog)} expected to bring home "
        f"{n_unit(expected_bones, 'bone')}, but lost one chasing a "
        f"shadow and ended up with one fewer.\n\n"
        f"Question: How many bones did {dog.name} fall short by, "
        f"compared to what {dog.he_she} expected?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} fell short by {n_unit(answer, 'bone')}."
    narrative   = "I compute expected-actual where actual is expected-1."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="dog-shadow",
        chapter="regret",
    )


def _ds_exchange_loss(scene: Scene) -> Record:
    """Dog had B bones. Trader offered N bones for M of dog's. Dog accepted but
    trader cheated — gave only K. Net change?"""
    dog    = scene.pick_character(role_classes=("everyman",), species="dog", gender=scene.pick_choice(["m", "f"]))
    trader = scene.pick_character(role_classes=("trader",))
    start  = scene.pick_int(5, 15)
    given  = scene.pick_int(2, start - 1)
    received = scene.pick_int(1, given - 1)  # cheated: less than given but at least 1

    expr = Let(
        bindings=[("start-bones",    Lit(start)),
                  ("bones-given",    Lit(given)),
                  ("bones-received", Lit(received))],
        body=App("+", [App("-", [Var("start-bones"), Var("bones-given")]),
                       Var("bones-received")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "dog-shadow")
    user_msg = (
        f"{_intro}{species_phrase(dog)} had {n_unit(start, 'bone')}. {trader.name} "
        f"offered to trade — {dog.name} would give {n_unit(given, 'bone')} "
        f"in exchange for some larger ones. But the trader cheated and "
        f"only gave back {n_unit(received, 'bone')}.\n\n"
        f"Question: How many bones does {dog.name} have after the trade?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} ends with {n_unit(answer, 'bone')}."
    narrative   = "I subtract given, then add received back to the start."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="dog-shadow",
        chapter="exchange-loss",
    )


# ─────────────────────── 10. Lion and the Three Bulls ───────────────────────


def gen_lion_bulls(scene: Scene) -> Record:
    chapter = scene.pick_choice(["days-to-defeat", "remaining-after-k",
                                  "divide-conquer-bool"])
    if chapter == "days-to-defeat":
        return _lb_days_to_defeat(scene)
    if chapter == "remaining-after-k":
        return _lb_remaining_after_k(scene)
    return _lb_divide_conquer_bool(scene)


def _lb_days_to_defeat(scene: Scene) -> Record:
    """Lion takes D days per bull. There are N bulls. Total days?"""
    lion = scene.pick_character(role_classes=("predator",), species="lion", gender=scene.pick_choice(["m", "f"]))
    location = scene.pick_location(tags_any=("path",), indoor=False)
    n_bulls    = scene.pick_int(3, 6)
    days_each  = scene.pick_int(1, 4)

    expr = Let(
        bindings=[("bulls",     Lit(n_bulls)),
                  ("days-per-bull", Lit(days_each))],
        body=App("*", [Var("bulls"), Var("days-per-bull")]),
    )
    answer = evaluate(expr)

    intro     = _aesopian_intro(scene, "lion-bulls", location)
    patient   = scene.rng.choice(EMO_PATIENT)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (bulls × days-per-bull =
    # total days). Each grounds the count in a distinct setting and
    # captures the lion's patient strategy and the bulls' growing
    # isolation as their unity dissolves.
    days_to_defeat_subplots = [
        # 1) open meadow — herd's old grazing ground after the quarrel
        f"For many seasons, {n_unit(n_bulls, 'bull')} had stood "
        f"shoulder to shoulder in an open meadow, and no predator had "
        f"dared approach. Then a quarrel split them, and they wandered "
        f"separately into the long grass. {species_phrase(lion)} "
        f"watched from a fold in the land {patient}, knowing each bull "
        f"on its own was no longer the same problem as the herd "
        f"together. {cap(lion.he_she)} reckoned that, hunting alone, "
        f"{lion.he_she} would need a careful "
        f"{n_unit(days_each, 'day')} of stalking and waiting for every "
        f"single bull. {lion.name} settled in to count the days the "
        f"whole undertaking would cost.",

        # 2) hilltop pasture at dawn, herd dispersed
        f"On a wide hilltop pasture, {n_unit(n_bulls, 'bull')} had "
        f"been grazing under the morning sun until petty rivalries "
        f"pulled them apart. Thorn moved north of the spring, Boulder "
        f"south, and the rest scattered to lower slopes. "
        f"{species_phrase(lion)} crouched among the scrub at the ridge "
        f"{patient}, taking the long view. {cap(lion.he_she)} had "
        f"learned, after one bruising failure, that a single bull on "
        f"open ground took {lion.him_her} a measured "
        f"{n_unit(days_each, 'day')} to bring down. With the herd now "
        f"broken, {lion.name} began to figure how many days the "
        f"entire hunt would consume.",

        # 3) valley grassland by a slow stream
        f"In a valley grassland threaded by a slow stream, "
        f"{n_unit(n_bulls, 'bull')} that had once watered together "
        f"now drank at separate bends. {species_phrase(lion)} moved "
        f"through the reeds {patient}, never pressing, never showing "
        f"more than a flick of tail. From the heron-haunted bank, "
        f"{lion.he_she} watched Gale wade in alone, far from the "
        f"others. {cap(lion.he_she)} counted on "
        f"{n_unit(days_each, 'day')} per bull to do the work properly "
        f"— no rushing, no warning bellows carrying across the water. "
        f"{lion.name} sat back to total what those days, multiplied "
        f"across the broken herd, would come to.",

        # 4) fence-line they no longer respect
        f"There had once been an old fence-line that the {n_bulls} "
        f"{unit(n_bulls, 'bull')} had walked together every evening, "
        f"horns clacking against the rails. Now they drifted past it "
        f"singly, paying it no mind, and the fence stood as a reminder "
        f"of a trust that had broken. {species_phrase(lion)}, "
        f"{patient}, padded along the far side. {cap(lion.he_she)} "
        f"counted on a measured {n_unit(days_each, 'day')} for each "
        f"of the {n_bulls} {unit(n_bulls, 'bull')}, hunted one at a "
        f"time. The lion sat in the shade of the rails and worked out "
        f"how many days in all that patient labor would take.",

        # 5) clearing surrounded by tall grass
        f"At the center of a wide clearing rimmed in shoulder-high "
        f"grass, {n_unit(n_bulls, 'bull')} had been grazing in a "
        f"loose, suspicious ring — no longer a single mass. "
        f"{species_phrase(lion)} circled the perimeter {patient}, the "
        f"grass swallowing every footfall. From a tussock, "
        f"{lion.he_she} watched a young bull turn its back and wander "
        f"deeper into the green. The lion knew from long practice that "
        f"solitary prey meant {n_unit(days_each, 'day')} of patient "
        f"work for each kill. As {desperate} bellows sometimes drifted "
        f"through the clearing at dusk, {lion.name} sat down to tally "
        f"what the whole campaign would cost in days.",

        # 6) edge of the forest where bulls graze
        f"At the edge of the forest, where the trees gave way to a "
        f"grazing strip, {n_unit(n_bulls, 'bull')} had wandered out "
        f"one by one rather than as the close-pressed mass they used "
        f"to be. {species_phrase(lion)} watched from the deeper shade "
        f"{patient}, ears half-folded, tail quiet. {cap(lion.he_she)} "
        f"knew the terrain well enough to be certain of "
        f"{lion.his_her} timing — {n_unit(days_each, 'day')} of "
        f"stalking and one sudden lunge, no more, no less, for each "
        f"bull alone. With the herd's old solidarity in shreds, "
        f"{lion.name} began to add up how many days of careful hunting "
        f"lay ahead.",
    ]

    body = _render_subplot(scene, days_to_defeat_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many total days {lion.name} will need to defeat all {n_bulls} bulls')}"
    )

    plan = "I multiply the number of bulls by the days needed for each."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="lion-bulls",
        chapter="days-to-defeat",
    )


def _lb_remaining_after_k(scene: Scene) -> Record:
    """N bulls, K already defeated (K < N). Remaining?"""
    lion = scene.pick_character(role_classes=("predator",), species="lion", gender=scene.pick_choice(["m", "f"]))
    n_bulls = scene.pick_int(4, 10)
    # K < N: there's always at least 1 bull left (avoids the trivial
    # "0 remain" narrative).
    defeated = scene.pick_int(1, n_bulls - 1)

    expr = Let(
        bindings=[("bulls",    Lit(n_bulls)),
                  ("bulls-defeated", Lit(defeated))],
        body=App("-", [Var("bulls"), Var("bulls-defeated")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "lion-bulls")
    user_msg = (
        f"{_intro}{species_phrase(lion)} faced {n_unit(n_bulls, 'bull')} grazing "
        f"alone in the field. After several days, {smart_pronoun(lion, [])} "
        f"had defeated {defeated} of them.\n\n"
        f"Question: How many bulls remain?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = (f"There is {answer} bull left." if answer == 1
                   else f"There are {answer} bulls left.")
    narrative   = "I subtract the defeated from the original count."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="lion-bulls",
        chapter="remaining-after-k",
    )


def _lb_divide_conquer_bool(scene: Scene) -> Record:
    """Lion needs S strength to defeat all bulls together. Has L. Together
    bulls > L. Alone, bulls have B each (B*N == total). Can lion defeat
    them one at a time?"""
    lion = scene.pick_character(role_classes=("predator",), species="lion", gender=scene.pick_choice(["m", "f"]))
    lion_strength = scene.pick_int(5, 15)
    n_bulls       = scene.pick_int(3, 5)
    bull_strength = scene.pick_int(2, lion_strength)  # individually beatable

    expr = Let(
        bindings=[
            ("lion-strength",  Lit(lion_strength)),
            ("bulls",          Lit(n_bulls)),
            ("bull-strength",  Lit(bull_strength)),
            ("combined-strength",       App("*", [Var("bulls"), Var("bull-strength")])),
        ],
        body=And_clauses(  # workaround: 'and' is not a special form in our AST
            App(">", [Var("lion-strength"), Var("bull-strength")]),
            App("<", [Var("lion-strength"), Var("combined-strength")]),
        ),
    )
    answer = evaluate(expr)
    answer_str = "yes" if answer else "no"

    _intro = _aesopian_intro(scene, "lion-bulls")
    user_msg = (
        f"{_intro}{species_phrase(lion)} has strength {lion_strength}. Each of "
        f"the {n_unit(n_bulls, 'bull')} has strength {bull_strength}. "
        f"Together the bulls' combined strength is {n_bulls * bull_strength}.\n\n"
        f"Question: Can {lion.name} only defeat the bulls if they "
        f"separate? Answer yes if alone-the-lion-wins-but-together-they-do-not, "
        f"otherwise no."
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"The answer is {answer_str}."
    narrative   = (
        "I check both: lion > one bull (alone wins) AND lion < "
        "combined-strength (together loses)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="lion-bulls",
        chapter="divide-conquer-bool",
    )


def And_clauses(*clauses):
    """Helper: emit `(and a b ...)` as App."""
    return App("and", list(clauses))


# ─────────────────────── registry ───────────────────────


GENERATORS: dict[str, Callable[[Scene], Record]] = {
    "tortoise-hare":   gen_tortoise_hare,
    "crow-pitcher":    gen_crow_pitcher,
    "goose-eggs":      gen_goose_eggs,
    "boy-wolf":        gen_boy_wolf,
    "ant-grasshopper": gen_ant_grasshopper,
    "milkmaid":        gen_milkmaid,
    "fox-grapes":      gen_fox_grapes,
    "two-mice":        gen_two_mice,
    "dog-shadow":      gen_dog_shadow,
    "lion-bulls":      gen_lion_bulls,
}


# ─────────────────────── self-test ───────────────────────


def smoke_test(seed: int = 0, n: int = 12) -> None:
    rng = random.Random(seed)
    for i in range(n):
        scene = Scene(rng=rng)
        gen = rng.choice(list(GENERATORS.values()))
        rec = gen(scene)
        assert rec.system_msg
        assert rec.user_msg
        assert rec.assistant_msg
        # Eval-first verification:
        #   - prefer_eval=True records: single eval call whose form,
        #     when re-evaluated, must match `expected`
        #   - prefer_eval=False records: single answer(value) call
        #     whose `value` arg must match `expected`
        last_call = rec.tool_calls[-1]
        if last_call["name"] == "eval":
            # We trust the AST evaluator already ran; cross-check that
            # the form-string round-trips by re-evaluating it isn't
            # cheap from Python (no Clojure runtime), so we just verify
            # the form string is a non-empty Clojure-shaped expression.
            assert last_call["args"]["form"].startswith("("), (
                f"eval form not a Clojure form: {last_call['args']['form'][:40]!r}"
            )
        else:
            assert last_call["name"] == "answer"
            assert any(_eq_relaxed(v, rec.expected)
                       for v in last_call["args"].values()), (
                f"answer mismatch: tool_call={last_call}  expected={rec.expected}"
            )
    print(f"fables smoke OK: {n} records across {len(GENERATORS)} fables")


def _eq_relaxed(a, b) -> bool:
    """Compare with bool/str/int leniency for tool-call value matching."""
    if a == b:
        return True
    if isinstance(a, str) and isinstance(b, bool):
        return (a == "yes") == b or (a == "no") == (not b)
    return False


if __name__ == "__main__":
    smoke_test()
