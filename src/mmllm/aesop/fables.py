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
        "The Hare and the Tortoise had argued for as long as anyone could remember about who was truly the faster.",
        "There was once a Hare whose pride matched her feet in speed, and a Tortoise who said nothing about either.",
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
    "with steady, careful steps", "with eyes always on the path",
    "untroubled by what others thought", "stepping deliberately",
)
EMO_TIRED: tuple[str, ...] = (
    "drowsy from the warm sun", "weary from the morning's effort",
    "lulled by the gentle wind", "with legs heavy from sprinting",
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
    market   = next(l for l in ont.LOCATIONS if l.name == "market")

    per_day  = scene.pick_int(1, 2)
    days     = scene.pick_int(7, 30)
    per_egg  = scene.pick_int(5, 50)
    total_coins = per_day * days * per_egg
    orient   = scene.pick_choice(["coins", "days", "per-egg"])
    intro    = _aesopian_intro(scene, "goose-eggs", location)
    greedy   = scene.rng.choice(EMO_GREEDY)
    content  = scene.rng.choice(EMO_CONTENT)

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
        givens = (
            f"The goose laid {per_day} golden {unit(per_day, 'egg')} a "
            f"day, and at the {market.name} each egg fetched "
            f"{n_unit(per_egg, 'coin')}. After {n_unit(days, 'day')} of "
            f"steady laying, "
        )
        question = (
            f"how many coins {owner.name} had earned in all from the "
            f"goose's eggs"
        )
        chapter_name = "value-yield-coins"
        plan = (
            "I find total eggs first (per-day × days), then multiply by "
            "the per-egg coin value."
        )
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
        givens = (
            f"The goose laid {per_day} golden {unit(per_day, 'egg')} a "
            f"day, and at the {market.name} each egg fetched "
            f"{n_unit(per_egg, 'coin')}. By the time the small chest of "
            f"coins beside the hearth held {n_unit(total_coins, 'coin')} "
            f"in all, "
        )
        question = "for how many days the goose had been laying"
        chapter_name = "value-yield-days"
        plan = (
            "Daily revenue is per-day eggs × per-egg coins; days = "
            "total-coins / coins-per-day."
        )
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
        givens = (
            f"The goose laid {per_day} golden {unit(per_day, 'egg')} a "
            f"day for {n_unit(days, 'day')}, and when the eggs were "
            f"finally carried in their basket to the {market.name} they "
            f"fetched {n_unit(total_coins, 'coin')} in all — "
        )
        question = "the price in coins at which each single egg had sold"
        chapter_name = "value-yield-per-egg"
        plan = (
            "Total eggs is per-day × days; per-egg price = total-coins / "
            "total-eggs."
        )

    # Six narrative subplots — same arithmetic skeleton (a daily golden-
    # egg routine that culminates in a market trip), each grounded in a
    # different small drama. The orient-specific `givens` clause carries
    # the numbers the question hides, so the 6 templates serve all three
    # branches.
    value_yield_subplots = [
        # 1) classic — willow basket, dawn at the market
        f"{owner.name} kept {species_phrase(goose)} on a small holding "
        f"at the edge of {location.article} {location.name}, where the "
        f"goose had a habit of settling on the same patch of straw each "
        f"morning. {givens}{owner.he_she} had grown into a quiet ritual "
        f"of carrying the eggs to the {market.name} in a willow basket, "
        f"{content}, where bread and cheese smelled thick in the dawn "
        f"air and traders haggled over each shining egg.",

        # 2) creaking table, evening tally with the chest
        f"There was a creaking table by the window of {owner.name}'s "
        f"cottage where {owner.he_she} liked to count out the day's "
        f"earnings each evening. {givens}{owner.he_she} would tip the "
        f"coins from the leather purse and let them clink across the "
        f"wood, {greedy} at the steady glint, then pour them into a "
        f"small iron-bound chest beneath the bed.",

        # 3) the regular customer at the stall
        f"At the {market.name} stall, a thin merchant in a green coat "
        f"had taken to buying every one of {owner.name}'s eggs, paying "
        f"in clean stamped coins each time. {givens}the merchant always "
        f"weighed the gold against a tiny brass scale before handing "
        f"it over. {owner.name} watched the routine, {content}, while "
        f"the smell of warm bread drifted from the next stall.",

        # 4) farmhand witness — chalk marks on the barn beam
        f"A young farmhand at {location.article} {location.name} kept "
        f"a chalk tally on a beam in the barn — one mark for each egg "
        f"the goose laid, one cross for each coin paid at the "
        f"{market.name}. {givens}the boy stood and stared up at the "
        f"marks, while {owner.name} sat by the door of the barn, "
        f"{content}, listening to the goose ruffle her feathers.",

        # 5) silver-egg rumor in the village
        f"In {location.article} {location.name} the rumor went that "
        f"{owner.name}'s goose laid silver as well as golden eggs, but "
        f"{owner.he_she} only smiled and said nothing of the kind. "
        f"{givens}every morning {owner.he_she} would carry the eggs to "
        f"the {market.name} folded inside a cloth, {greedy} at the "
        f"soft weight against {owner.his_her} hip, listening to the "
        f"coins jingle home each evening.",

        # 6) the temptation kept at bay
        f"More than once {owner.name} had heard a sly voice whisper "
        f"that the goose was wasted on slow daily laying. But "
        f"{owner.he_she} swallowed the thought each time, fed the bird, "
        f"and let the gold come at its own pace. {givens}{owner.he_she} "
        f"sat by the hearth, {content}, and looked at the worn ledger "
        f"where every egg, every coin, every trip to the {market.name} "
        f"had been written down in a careful hand.",
    ]

    body = _render_subplot(scene, value_yield_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, question)}"
    )

    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    intro    = _aesopian_intro(scene, "goose-eggs")
    greedy   = scene.rng.choice(EMO_GREEDY)
    content  = scene.rng.choice(EMO_CONTENT)

    # Six narrative subplots — same arithmetic (sum of daily yields), but
    # each grounds the day-by-day list in a different small drama: a
    # diary, a barn ledger, a string of ribbons, a kitchen-window tally.
    # The yields_str carries the actual numbers so the model still must
    # reduce them.
    compounded_subplots = [
        # 1) classic — diary kept by lamplight
        f"{owner.name} kept a leather-bound diary by the lamp on the "
        f"kitchen table, and each evening would write down the day's "
        f"yield from {species_phrase(goose)} in {owner.his_her} careful "
        f"hand. Over {n_unit(days, 'day')}, the count came out — day "
        f"after day — as {yields_str}. Some mornings the goose laid "
        f"more than {owner.he_she} expected, and {owner.name} would "
        f"linger in the barn, {greedy} at the warm gold; other days "
        f"only one or two, and {owner.he_she} simply nodded and closed "
        f"the door.",

        # 2) barn ledger, chalk on a beam
        f"On a beam in the barn {owner.name} kept a chalk ledger, one "
        f"row per day, one mark per egg. After {n_unit(days, 'day')} "
        f"the row read in order: {yields_str}. {cap(owner.he_she)} would "
        f"stand at the foot of the ladder and look up at the marks in "
        f"the lamplight, {content}, listening to {species_phrase(goose)} "
        f"settle for the night in her straw, never the same number of "
        f"eggs twice in a row but always something.",

        # 3) ribbon-on-a-string daily count
        f"The children of {owner.name}'s household had taken to threading "
        f"colored ribbons onto a string by the hearth — one ribbon for "
        f"each egg {species_phrase(goose)} laid that morning. Over "
        f"{n_unit(days, 'day')} the ribbons formed a record of the daily "
        f"yields: {yields_str}. {owner.name} watched the string lengthen, "
        f"{content}, never quite ready to count the whole until the "
        f"week was through.",

        # 4) market trader noting yields in a tally book
        f"A trader from the next village had asked {owner.name} to "
        f"keep a careful record of {species_phrase(goose)}'s daily yield, "
        f"hoping to buy eggs in bulk. So {owner.name} jotted each "
        f"morning's count into a tally book by the window. The "
        f"{n_unit(days, 'day')}' worth came to: {yields_str}. The trader "
        f"would arrive at week's end, and {owner.name} sat by the "
        f"hearth, {greedy} at the thought of the coin, totaling each "
        f"line.",

        # 5) farmhand witness — pebbles in a jar
        f"A young farmhand at {owner.name}'s farm kept a small clay "
        f"jar in the kitchen, and each morning dropped in one pebble "
        f"for every egg {species_phrase(goose)} had laid. After "
        f"{n_unit(days, 'day')}, the daily counts had come out as "
        f"{yields_str}. The boy would bring the jar to {owner.name} "
        f"each evening and they would peer into it together, "
        f"{content}, while the bird ruffled in her straw outside.",

        # 6) the long week of varied days
        f"It had been a strange week at the farm: some mornings the "
        f"goose laid generously, others almost grudgingly. Over the "
        f"course of {n_unit(days, 'day')}, {owner.name} had carefully "
        f"noted each day's tally — {yields_str} — onto a strip of paper "
        f"pinned to the kitchen door. {cap(owner.he_she)} stood looking "
        f"at the paper now, {content}, working out what the goose had "
        f"given altogether across all those days.",
    ]

    body = _render_subplot(scene, compounded_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, 'how many eggs in total were laid over those days')}"
    )

    plan = "I sum the daily yields with reduce."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    intro     = _aesopian_intro(scene, "goose-eggs")
    greedy    = scene.rng.choice(EMO_GREEDY)
    content   = scene.rng.choice(EMO_CONTENT)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (sum / count quot), but
    # each frames the average-eggs-per-day question through a different
    # small drama: a buyer wanting a typical-day estimate, a tax man,
    # a child's curiosity, the farmer's own bookkeeping. The yields_str
    # carries the actual numbers so the model still sums and divides.
    average_subplots = [
        # 1) classic — village bookkeeper sets a typical-day baseline
        f"At the end of {n_unit(days, 'day')}, {owner.name} sat at the "
        f"kitchen table and laid the week's tally before {owner.him_her}: "
        f"{yields_str}. The village bookkeeper had asked for a single "
        f"\"typical-day\" figure for the goose's yield, rounded down to "
        f"a whole number, and {owner.name} began to work it out, "
        f"{content}, while {species_phrase(goose)} settled outside in "
        f"the warm dusk.",

        # 2) buyer wants a daily estimate before agreeing on a price
        f"A grain merchant from the next valley had offered to buy "
        f"{owner.name}'s eggs in advance, but only at a price tied to "
        f"the goose's typical daily yield. {owner.name} pulled out the "
        f"week's notes — {yields_str} over {n_unit(days, 'day')} — and "
        f"set about computing the rounded-down average, {greedy} at the "
        f"thought of what a fair number would be worth.",

        # 3) child's curiosity at the kitchen window
        f"A small child had taken to standing at the kitchen window each "
        f"morning to count the eggs as {species_phrase(goose)} laid them. "
        f"After {n_unit(days, 'day')} the child had recorded {yields_str} "
        f"and now tugged at {owner.name}'s sleeve, asking how many the "
        f"bird laid \"on a usual day.\" {cap(owner.he_she)} smiled, "
        f"{content}, and sat down with the child to figure out the "
        f"whole-number average.",

        # 4) tax collector demanding a typical day
        f"The village tax collector wanted to know the goose's typical "
        f"yield, and would not be put off by talk of varying days. "
        f"{owner.name} laid out the {n_unit(days, 'day')}' counts on a "
        f"slate — {yields_str} — and set to working out the rounded-down "
        f"average, {regretful} of the day {owner.he_she} had ever "
        f"mentioned the bird in the village square.",

        # 5) the farmer's own ledger, pondering at sundown
        f"In the lull after sundown, {owner.name} liked to pull out the "
        f"farm ledger and look at how the week had gone for "
        f"{species_phrase(goose)}. The {n_unit(days, 'day')}' counts read "
        f"{yields_str}. {cap(owner.he_she)} stared at the column, "
        f"{content}, working out a single steady-day figure — rounded "
        f"down to a whole egg — for the bird's average yield.",

        # 6) the temptation kept at bay — what is she really worth?
        f"{owner.name} had heard a sly voice whisper that perhaps the "
        f"goose was no longer earning her keep, that one bad week proved "
        f"it. So {owner.he_she} laid out the {n_unit(days, 'day')}' "
        f"yields — {yields_str} — and set to compute the typical, "
        f"rounded-down daily count, {regretful} of having entertained "
        f"the doubt at all.",
    ]

    body = _render_subplot(scene, average_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, 'the average eggs per day, rounded down to a whole number')}"
    )

    plan = (
        "I sum the yields, divide by the count of days, and take the "
        "integer quotient."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    """Boy raises F false alarms. Villagers run T minutes each time. Total
    minutes wasted = villagers × alarms × minutes-per-trip."""
    boy   = scene.pick_character(role_classes=("liar", "shepherd"),
                                  gender=scene.pick_choice(["m", "f"]))
    n_villagers = scene.pick_int(3, 10)
    n_alarms    = scene.pick_int(2, 6)
    minutes_per = scene.pick_int(5, 20)

    expr = Let(
        bindings=[
            ("villagers",        Lit(n_villagers)),
            ("alarms",           Lit(n_alarms)),
            ("minutes-per-trip", Lit(minutes_per)),
        ],
        body=App("*", [Var("villagers"), Var("alarms"),
                       Var("minutes-per-trip")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "boy-wolf")
    desperate = scene.rng.choice(EMO_DESPERATE)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (villagers × alarms ×
    # minutes), grounded in different small dramas about the cost of
    # crying-out-without-cause.
    false_alarms_subplots = [
        # 1) classic — boy on the hill at midday
        f"On the slope above the village, {boy.name} kept watch over a "
        f"small flock and grew restless in the long noon. Just to see "
        f"what would happen, {boy.he_she} sang out the alarm — and "
        f"{n_villagers} villagers dropped their tools and hurried up "
        f"the path. {boy.name} did this {n_unit(n_alarms, 'time')} "
        f"in all, each rush taking {n_unit(minutes_per, 'minute')} of "
        f"climbing and walking back down. The villagers, "
        f"{regretful}, returned to their work each time without a word.",

        # 2) market interruption
        f"On market days the villagers gathered to trade, and "
        f"{boy.name}, watching the flock from a high stone, learned "
        f"that a single shout would empty the market square. So "
        f"{boy.he_she} shouted — falsely — {n_unit(n_alarms, 'time')}. "
        f"On each occasion, {n_villagers} of the busiest villagers ran "
        f"out from their stalls to help, {desperate}, and the round "
        f"trip back cost each of them "
        f"{n_unit(minutes_per, 'minute')}.",

        # 3) hot afternoon — villagers irritable
        f"The afternoon was hot, and the villagers had been working in "
        f"the fields all day. {boy.name}, on the hill alone with the "
        f"sheep, raised the alarm without reason "
        f"{n_unit(n_alarms, 'time')}. Each time, {n_villagers} villagers "
        f"left their work and made the long walk up to the meadow and "
        f"back, a trip that took {n_unit(minutes_per, 'minute')} from "
        f"start to finish. They returned each time hotter and more "
        f"weary than before.",

        # 4) winter — villagers in coats
        f"In the cold months, even a short run took its toll. "
        f"{boy.name} watched the flock at the edge of the snow-frosted "
        f"meadow and, perhaps to fight off boredom, called for help "
        f"when there was none — {n_unit(n_alarms, 'time')} in all. On "
        f"every alarm, {n_villagers} villagers pulled on their coats "
        f"and hurried out, the round trip to the meadow taking "
        f"{n_unit(minutes_per, 'minute')} apiece.",

        # 5) elder counts the time
        f"An old village elder, who kept careful track of how the "
        f"hours of the village were spent, watched {boy.name} raise "
        f"the alarm {n_unit(n_alarms, 'time')} without cause. On each "
        f"occasion, {n_villagers} villagers made the climb to the "
        f"meadow, and the round trip took every one of them "
        f"{n_unit(minutes_per, 'minute')}. The elder kept tallying "
        f"the time on a slate, {regretful}, and waited for a lesson "
        f"to settle in.",

        # 6) season's end — pattern recognized
        f"By the end of the season, the village had a saying about "
        f"{boy.name} on the hill. The young shepherd had given the "
        f"alarm without cause {n_unit(n_alarms, 'time')}, and on each "
        f"of those days {n_villagers} villagers had hurried out to "
        f"help — a round trip that took {n_unit(minutes_per, 'minute')} "
        f"each. They counted the cost of trust, slowly, and "
        f"determined the time had not been spent well.",
    ]

    body = _render_subplot(scene, false_alarms_subplots)
    alarms_str = n_unit(n_alarms, "false alarm")
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many total minutes the villagers spent answering the {alarms_str}')}"
    )

    plan = "I multiply villagers × alarms × minutes-per-trip."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="boy-wolf",
        chapter="false-alarms",
    )


def _bw_sheep_eaten(scene: Scene) -> Record:
    """A wolf appears; villagers no longer believe the boy; the wolf
    chases off S sheep before help arrives. Remaining sheep = flock − S."""
    boy = scene.pick_character(role_classes=("liar", "shepherd"),
                                gender=scene.pick_choice(["m", "f"]))
    flock = scene.pick_int(20, 80)
    eaten = scene.pick_int(3, min(flock - 1, 15))

    expr = Let(
        bindings=[("flock-size",  Lit(flock)),
                  ("sheep-eaten", Lit(eaten))],
        body=App("-", [Var("flock-size"), Var("sheep-eaten")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "boy-wolf")
    desperate = scene.rng.choice(EMO_DESPERATE)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (flock − missing-sheep),
    # grounded in different small dramas about a flock that scattered
    # while help did not come.
    sheep_eaten_subplots = [
        # 1) wolf at the meadow's edge — villagers don't come
        f"The shepherd's flock numbered {n_unit(flock, 'sheep', 'sheep')} "
        f"at sundown when a thin grey wolf slipped from the trees and "
        f"set the meadow into a panic. {boy.name} cried out for help, "
        f"{desperate}, but the villagers — long since out of trust for "
        f"that voice — did not stir from the village. By the time the "
        f"wolf gave up and returned to the woods, "
        f"{n_unit(eaten, 'sheep', 'sheep')} had run off into the dusk "
        f"and were not seen again that night.",

        # 2) misty morning — wolf comes through fog
        f"On a misty morning {boy.name} stood at the head of a flock "
        f"of {n_unit(flock, 'sheep', 'sheep')}, watching the white "
        f"shapes shift among the trees. A wolf moved through the fog, "
        f"and the boy shouted for the village. No one came. By the "
        f"time the mist lifted and a worried neighbour finally walked "
        f"up the path, {n_unit(eaten, 'sheep', 'sheep')} had bolted "
        f"in fright and could not be recovered. {boy.name} sat on the "
        f"stone, {regretful}.",

        # 3) old shepherd arrives too late
        f"The flock that morning held {n_unit(flock, 'sheep', 'sheep')}. "
        f"When a wolf came down from the ridge, {boy.name} ran to the "
        f"village edge calling for help, {desperate}, but the doors "
        f"stayed shut. By the time the old shepherd at the far end of "
        f"the village heard the noise and walked up, the wolf was "
        f"gone and {n_unit(eaten, 'sheep', 'sheep')} had vanished into "
        f"the gullies — too far now to gather back.",

        # 4) winter snow — wolf tracks left behind
        f"It was a hard winter morning, and {boy.name} had counted "
        f"{n_unit(flock, 'sheep', 'sheep')} into the meadow at dawn. "
        f"A grey wolf appeared by the snow-line, and the boy shouted "
        f"for help. The villagers, weary of such cries, did not come. "
        f"After the wolf had retreated into the trees and the flock "
        f"settled, the boy walked the perimeter and found "
        f"{n_unit(eaten, 'sheep', 'sheep')} missing — gone with the "
        f"tracks that led off into the snow.",

        # 5) festival day — village preoccupied
        f"It was festival day in the village, and the streets were "
        f"full of music and bunting. {boy.name} watched a flock of "
        f"{n_unit(flock, 'sheep', 'sheep')} on the hill alone. When a "
        f"wolf slipped from the brush, the boy raised the alarm — but "
        f"the village, long since deaf to those cries and busy with "
        f"the festival besides, did not come. By the time the music "
        f"stopped and a few villagers wandered up, "
        f"{n_unit(eaten, 'sheep', 'sheep')} had been lost to the "
        f"chase.",

        # 6) old grandfather counts the loss at dusk
        f"At dusk, the boy's grandfather walked up to the meadow and "
        f"helped count the flock. There had been "
        f"{n_unit(flock, 'sheep', 'sheep')} that morning. A wolf had "
        f"come at midday, and {boy.name} had shouted for help — "
        f"{desperate}, but no help came. The grandfather, "
        f"{regretful}, walked the line of the flock and found "
        f"{n_unit(eaten, 'sheep', 'sheep')} were missing, scattered "
        f"to the gullies and the woods.",
    ]

    body = _render_subplot(scene, sheep_eaten_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many sheep {boy.name} has left in the flock')}"
    )

    plan = "I subtract the missing sheep from the original flock size."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
        value=answer,
        expr=expr,
        fable="boy-wolf",
        chapter="sheep-eaten",
    )


def _bw_trust_threshold(scene: Scene) -> Record:
    """Villagers stop responding after K false alarms. Given how many
    false alarms the shepherd has raised so far, will the villagers
    answer the next call? Returns 'yes' or 'no'."""
    boy = scene.pick_character(role_classes=("liar", "shepherd"),
                                gender=scene.pick_choice(["m", "f"]))
    threshold = scene.pick_int(3, 5)
    alarms_so_far = scene.pick_int(0, 7)

    expr = If(
        App("<", [Var("alarms-so-far"), Var("threshold")]),
        Lit("yes"),
        Lit("no"),
    )
    expr = Let(
        bindings=[("threshold",     Lit(threshold)),
                  ("alarms-so-far", Lit(alarms_so_far))],
        body=expr,
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "boy-wolf")
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same boolean arithmetic (alarms-so-far
    # < threshold ?), grounded in different small dramas about
    # village patience nearing its limit.
    trust_threshold_subplots = [
        # 1) elder sets the rule
        f"After many seasons of false cries from the hill, an old "
        f"village elder set a rule that the people held to: the "
        f"villagers would answer no more than {n_unit(threshold, 'false alarm')} "
        f"from a single shepherd. {boy.name} had so far raised "
        f"{n_unit(alarms_so_far, 'false alarm')}. Whether they would "
        f"come the next time depended on a simple comparison.",

        # 2) tally on the village hall door
        f"On the door of the village hall hung a small slate where the "
        f"reeve marked false alarms with a chalked stroke. The rule "
        f"was plain: more than {n_unit(threshold, 'mark')} on the slate "
        f"and the village no longer turned out. {boy.name}'s slate "
        f"showed {n_unit(alarms_so_far, 'mark')} so far, and the "
        f"shepherd, {regretful}, looked at it on the way home each "
        f"evening.",

        # 3) gentle reminder from the boy's mother
        f"At supper, the boy's mother quietly explained the village's "
        f"patience: the neighbours would come for any alarm, but only "
        f"up to {n_unit(threshold, 'false call')}. After that, the "
        f"village considered the well dry. {boy.name} had so far "
        f"raised {n_unit(alarms_so_far, 'false alarm')}, and could "
        f"work out, simply by counting, whether the next call would "
        f"draw any answer at all.",

        # 4) the new shepherd asks the rule
        f"A new shepherd, recently come to the village, asked aloud "
        f"how many warnings the neighbours would tolerate before they "
        f"stopped answering at all. The reeve answered honestly: the "
        f"limit was {n_unit(threshold, 'false alarm')}. {boy.name}'s "
        f"recent record stood at {n_unit(alarms_so_far, 'false alarm')}, "
        f"and the new shepherd worked out, by simple comparison, "
        f"whether help would come the next time.",

        # 5) end-of-week reckoning
        f"Each Saturday the village reeve walked up to the meadow and "
        f"reviewed the week's alarms. The custom long ago set the "
        f"limit at {n_unit(threshold, 'false alarm')}; beyond that, "
        f"the village considered itself excused from coming. "
        f"{boy.name}'s tally for the week stood at "
        f"{n_unit(alarms_so_far, 'false alarm')} when the reeve "
        f"opened {boy.his_her} ledger.",

        # 6) the boy himself counting on his fingers
        f"That evening, sitting on a stone above the meadow, "
        f"{boy.name} counted on {boy.his_her} fingers what the village "
        f"would tolerate: at most {n_unit(threshold, 'false alarm')}. "
        f"So far, {boy.he_she} had cried out without cause "
        f"{n_unit(alarms_so_far, 'time')}. The boy worked out, with "
        f"some unease, whether tomorrow's call would still bring help.",
    ]

    body = _render_subplot(scene, trust_threshold_subplots)
    q = ("whether the villagers will come on the next alarm "
         '(return the string "yes" or "no")')
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, q)}"
    )

    plan = (
        "I compare alarms-so-far against the threshold and return "
        "'yes' if below, 'no' otherwise."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    # Item / container diversity — the ant doesn't only ever hoard grain.
    # Pick a small edible item the ant might gather and a small storage
    # container or burrow space. Subplots reference (item, container)
    # directly so each retelling feels like a different harvest season.
    item = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("grain", "seed", "crumb", "nut", "acorn", "biscuit")
    ])
    container = scene.rng.choice([
        c for c in ont.CONTAINERS
        if c.name in ("pouch", "jar", "bag", "basket", "hole")
    ])

    if orient == "total":
        expr = Let(
            bindings=[("per-day", Lit(per_day)), ("days", Lit(days))],
            body=App("*", [Var("per-day"), Var("days")]),
        )
        answer = evaluate(expr)
        # facts: per_day + days exposed; total is the answer (don't reveal)
        facts = (
            f"every day {ant.name} carried {n_unit(per_day, item.name, item.plural)} "
            f"home, and the work went on for {n_unit(days, 'day')} without pause"
        )
        question_what = (
            f"how many {item.plural} {ant.name} has gathered by summer's end"
        )
        plan = "I multiply the daily rate by the number of days."
        chapter_name = "summer-stockpile-total"
    elif orient == "days":
        expr = Let(
            bindings=[("total",   Lit(total)),
                      ("per-day", Lit(per_day))],
            body=App("quot", [Var("total"), Var("per-day")]),
        )
        answer = evaluate(expr)
        # facts: per_day + total exposed; days is the answer
        facts = (
            f"by the close of summer {ant.name} had gathered "
            f"{n_unit(total, item.name, item.plural)} in all, carrying "
            f"{n_unit(per_day, item.name, item.plural)} home each day"
        )
        question_what = (
            f"how many days {ant.name} spent at the gathering"
        )
        plan = "I divide the total by the daily rate."
        chapter_name = "summer-stockpile-days"
    else:
        expr = Let(
            bindings=[("total", Lit(total)), ("days", Lit(days))],
            body=App("quot", [Var("total"), Var("days")]),
        )
        answer = evaluate(expr)
        # facts: days + total exposed; per_day is the answer
        facts = (
            f"{ant.name} worked the whole {n_unit(days, 'day')} of summer "
            f"and finished with {n_unit(total, item.name, item.plural)} stored away"
        )
        question_what = (
            f"how many {item.plural} {ant.name} carried home each day"
        )
        plan = "I divide the total by the number of days."
        chapter_name = "summer-stockpile-rate"

    intro    = _aesopian_intro(scene, "ant-grasshopper", location)
    content  = scene.rng.choice(EMO_CONTENT)
    proud    = scene.rng.choice(EMO_PROUD)
    regret   = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — each grounds the same arithmetic in a
    # distinct small drama with a distinct (item, container) pairing.
    # `facts` carries the orientation-specific quantitative beat; the
    # surrounding prose varies with each retelling.
    summer_subplots = [
        # 1) classic — ant at the meadow's edge, container by container
        f"At {location.article} {location.name}, {species_phrase(ant)} bent low "
        f"over the warm earth, collecting one {item.name} at a time and lining "
        f"the {container.name} that sat half-buried by the burrow's mouth. "
        f"While the Grasshopper fiddled in the long grass nearby, {ant.name} "
        f"worked {content}, knowing the cold months would come whether or not "
        f"anyone sang for them. So {facts}.",

        # 2) midsummer haul — pride in the larder
        f"Halfway through summer, {ant.name} stood {proud} beside a "
        f"{container.name} that was already heavier than {ant.he_she} could "
        f"easily drag. Each {item.name} had been chosen, weighed in two "
        f"feelers, and tucked carefully in. The Grasshopper passed by humming "
        f"a tune and laughed at the trouble {ant.name} took over so small "
        f"a thing. {cap(ant.he_she)} only kept on; {facts}.",

        # 3) dawn-and-dusk routine — patient repetition
        f"At {location.article} {location.name}, the days began with "
        f"{ant.name} setting out before the sun and ended with {ant.him_her} "
        f"hauling another load of {item.plural} into the {container.name} "
        f"hidden under the roots. The Grasshopper watched lazily from a stalk "
        f"of grass, certain summer would last forever. But {ant.name} kept a "
        f"quieter count: {facts}. The {container.name} grew fuller by the day.",

        # 4) thunderstorm interlude — work even in rain
        f"A storm rolled across {location.article} {location.name} one "
        f"afternoon, and the Grasshopper darted under a leaf to wait it out. "
        f"{ant.name}, however, only paused long enough to shake the rain from "
        f"{ant.his_her} back before trundling another {item.name} into the "
        f"{container.name} {ant.he_she} kept beside the back wall of the "
        f"burrow. The work did not stop for weather; {facts}.",

        # 5) Grasshopper's idle visit — the ant explains
        f"\"Why bother?\" sang the Grasshopper one bright noon, lounging at "
        f"the lip of {ant.name}'s burrow. {ant.name} did not stop, only "
        f"set another {item.name} into the {container.name} with the small "
        f"satisfaction of one {content}. \"Because winter,\" {ant.he_she} said "
        f"simply. And so it was that {facts} — even as the Grasshopper "
        f"laughed and chirped the long afternoons away.",

        # 6) the grasshopper begins to suspect — too late hint
        f"By late summer the Grasshopper had begun to glance, {regret}, "
        f"at {ant.name}'s steady marching to and from the {container.name} "
        f"by the burrow's mouth. Each trip brought another {item.name} to "
        f"the store. The fields of {location.article} {location.name} were "
        f"already turning gold; soon the wind would change. Inside that "
        f"quiet {container.name}, the count was honest: {facts}.",
    ]

    body = _render_subplot(scene, summer_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, question_what)}"
    )

    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    # Item / container diversity — vary what the ant has hoarded against
    # the long winter, and where it is stored.
    item = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("grain", "seed", "crumb", "nut", "acorn", "biscuit")
    ])
    container = scene.rng.choice([
        c for c in ont.CONTAINERS
        if c.name in ("pouch", "jar", "bag", "basket", "hole")
    ])

    intro    = _aesopian_intro(scene, "ant-grasshopper")
    content  = scene.rng.choice(EMO_CONTENT)
    proud    = scene.rng.choice(EMO_PROUD)

    # Six narrative subplots — same arithmetic (stockpile quot per_day =
    # whole days the food lasts). Each grounds the count in a different
    # winter scene with a distinct (item, container) pairing. The Ant is
    # mostly content / proud here — winter is the season of vindication.
    winter_subplots = [
        # 1) classic snow-covered burrow, careful tally at dawn
        f"Snow had drifted high over the meadow grass, and inside the warm "
        f"burrow {species_phrase(ant)} sat beside a {container.name} of "
        f"{item.plural} that {ant.he_she} had hauled in all summer. "
        f"{cap(ant.he_she)} counted them out: {n_unit(stockpile, item.name, item.plural)} "
        f"in all. By {ant.his_her} careful rule {ant.he_she} would eat just "
        f"{n_unit(per_day, item.name, item.plural)} each day, no more, no less. "
        f"The wind howled outside and {ant.name} sat {content}, working out "
        f"how long the {container.name} would carry {ant.him_her}.",

        # 2) the grasshopper at the door, half a sentence away
        f"There came a thin scratching at the burrow's mouth — the Grasshopper, "
        f"thinner now and shivering, asking for shelter. {ant.name} did not yet "
        f"answer; {ant.he_she} was busy counting the {item.plural} in the "
        f"{container.name} by the wall. {n_unit(stockpile, item.name, item.plural)} "
        f"sat in their orderly rows, and {ant.name}'s rule for the cold months "
        f"was steady: only {n_unit(per_day, item.name, item.plural)} per day, "
        f"taken at evening, no matter what.",

        # 3) silent winter afternoon, lamp light, careful arithmetic
        f"In the long blue hour after noon, with snow piled to the rafters, "
        f"{ant.name} sat by a small lamp and went over the inventory once "
        f"again. The {container.name} that held the winter's food contained "
        f"exactly {n_unit(stockpile, item.name, item.plural)}. "
        f"{cap(ant.he_she)} measured out {n_unit(per_day, item.name, item.plural)} "
        f"as a single day's portion — that was the rule {ant.he_she} had set "
        f"for {ant.himself_herself} when summer was bright. Now {ant.he_she} "
        f"only had to work out how many days the supply would carry {ant.him_her}.",

        # 4) winter solstice — short days, smaller portions
        f"On the shortest day of the year, {ant.name} sat {proud} by the "
        f"{container.name} of stored food and took stock. "
        f"{n_unit(stockpile, item.name, item.plural)} remained — gathered, sorted, "
        f"and laid in during the long bright weeks. {cap(ant.he_she)} ate "
        f"sparely now: only {n_unit(per_day, item.name, item.plural)} a day, "
        f"and never went over. The Grasshopper, somewhere outside, was no "
        f"longer singing.",

        # 5) the cellar by candlelight, ledger-style
        f"Inside the burrow, candlelight fell on {ant.name}'s little ledger. "
        f"In the cellar beyond, a {container.name} stood crammed with "
        f"{n_unit(stockpile, item.name, item.plural)} — every one carried home "
        f"on {ant.his_her} own back across the long summer. "
        f"{cap(ant.he_she)} would take only {n_unit(per_day, item.name, item.plural)} "
        f"each morning, and the ledger would tally them off one by one. "
        f"How many entries the ledger would hold before the {container.name} "
        f"ran empty, that was the question.",

        # 6) blizzard outside, calm planning inside
        f"A blizzard rattled the dry stalks of the meadow, and far below, "
        f"in the close warmth of the burrow, {ant.name} ran a feeler over "
        f"the smooth side of the {container.name} where the winter's stores "
        f"sat. {n_unit(stockpile, item.name, item.plural)} in all. The plan, "
        f"settled long before the first snow, was unbroken: "
        f"{n_unit(per_day, item.name, item.plural)} per day, eaten at the "
        f"same hour, with the same {content} care. {cap(ant.he_she)} began "
        f"to figure how long the {container.name} could carry {ant.him_her}.",
    ]

    body = _render_subplot(scene, winter_subplots)
    question_what = f"how many whole days {ant.name}'s stockpile will last"
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, question_what)}"
    )

    plan = "I divide the stockpile by daily consumption (integer quotient)."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    # Item / container diversity — share a single food kind across both
    # characters (the meadow's harvest), but pair the diligent Ant with a
    # proper storage container and the late-realizing Grasshopper with a
    # smaller one (or with empty pockets). The contrast in containers is
    # part of the moral.
    item = scene.rng.choice([
        i for i in ont.ITEMS
        if i.name in ("grain", "seed", "crumb", "nut", "acorn", "biscuit")
    ])
    ant_container = scene.rng.choice([
        c for c in ont.CONTAINERS
        if c.name in ("jar", "basket", "bag", "hole")
    ])
    gh_container = scene.rng.choice([
        c for c in ont.CONTAINERS
        if c.name in ("pouch", "jar", "bag", "basket")
    ])

    intro     = _aesopian_intro(scene, "ant-grasshopper")
    content   = scene.rng.choice(EMO_CONTENT)
    proud     = scene.rng.choice(EMO_PROUD)
    regret    = scene.rng.choice(EMO_REGRETFUL)
    hungry    = scene.rng.choice(EMO_HUNGRY)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (ant-left clamped to 0).
    # Each grounds the contrast between provident Ant and improvident
    # Grasshopper in a different small drama. Both have a stash and a
    # daily-eating rule; the question targets the Ant's leftover after
    # `days` days of winter. The clamp-at-0 hint stays explicit so the
    # model knows to use max with 0.
    survival_subplots = [
        # 1) classic side-by-side larders
        f"Winter had come at last to the meadow, and lasted "
        f"{n_unit(days, 'day')} from first frost to first thaw. In {ant.name} "
        f"the ant's neat {ant_container.name} sat "
        f"{n_unit(ant_stock, item.name, item.plural)}, gathered in the bright "
        f"weeks of summer; {ant.name} ate {n_unit(ant_per_day, item.name, item.plural)} "
        f"each day, no more, {content}. In {grasshopper.name} the grasshopper's "
        f"thin {gh_container.name} sat only {n_unit(gh_stock, item.name, item.plural)}, "
        f"and {grasshopper.he_she} too ate "
        f"{n_unit(gh_per_day, item.name, item.plural)} a day, {regret}. "
        f"If a stockpile runs out, the count cannot go below zero.",

        # 2) the grasshopper at the door, contrasting tallies
        f"On the first hard morning of winter — a season that would last "
        f"{n_unit(days, 'day')} in all — {grasshopper.name} the grasshopper "
        f"came scratching at {ant.name}'s burrow, {hungry}. Inside the "
        f"burrow, {ant.name} sat beside a {ant_container.name} of "
        f"{n_unit(ant_stock, item.name, item.plural)} and ate "
        f"{n_unit(ant_per_day, item.name, item.plural)} each day. The "
        f"Grasshopper had only {n_unit(gh_stock, item.name, item.plural)} "
        f"in {article(gh_container.name)} {gh_container.name}, and ate "
        f"{n_unit(gh_per_day, item.name, item.plural)} "
        f"a day. (No stockpile can drop below zero.)",

        # 3) a long winter, two diaries
        f"That year the cold months stretched {n_unit(days, 'day')} from "
        f"first snow to last frost. {ant.name} kept a careful tally: "
        f"{n_unit(ant_stock, item.name, item.plural)} in the {ant_container.name} "
        f"by the wall at the start, and {ant.he_she} drew "
        f"{n_unit(ant_per_day, item.name, item.plural)} from it every morning, "
        f"{proud} of {ant.his_her} planning. {grasshopper.name}, hidden in "
        f"the dry stalks, had begun the winter with only "
        f"{n_unit(gh_stock, item.name, item.plural)} in "
        f"{grasshopper.his_her} {gh_container.name}, and chewed through "
        f"{n_unit(gh_per_day, item.name, item.plural)} a day. The count, "
        f"of course, cannot go below zero for either of them.",

        # 4) the meadow at midwinter — short ledgers
        f"Midway through a winter that ran {n_unit(days, 'day')} from end to "
        f"end, two ledgers told two stories. {species_phrase(ant)} had "
        f"begun with {n_unit(ant_stock, item.name, item.plural)} stored "
        f"snugly in the {ant_container.name} at the back of the burrow, "
        f"and ate exactly {n_unit(ant_per_day, item.name, item.plural)} "
        f"per day. {species_phrase(grasshopper)} had begun with only "
        f"{n_unit(gh_stock, item.name, item.plural)} in {grasshopper.his_her} "
        f"thin {gh_container.name}, and {grasshopper.he_she} too went through "
        f"{n_unit(gh_per_day, item.name, item.plural)} per day, {desperate}. "
        f"Whichever stockpile emptied first, the count would simply rest at zero.",

        # 5) the village of small folk weighs in
        f"The small folk of the meadow whispered, on the longest night, "
        f"about how the two neighbors were faring. Winter, all said, would "
        f"last {n_unit(days, 'day')} in all. {ant.name} the ant, "
        f"{content}, had laid in {n_unit(ant_stock, item.name, item.plural)} "
        f"in the {ant_container.name} at the back of the burrow and ate "
        f"only {n_unit(ant_per_day, item.name, item.plural)} a day. "
        f"{grasshopper.name} the grasshopper had managed only "
        f"{n_unit(gh_stock, item.name, item.plural)} in "
        f"{grasshopper.his_her} {gh_container.name}, and ate "
        f"{n_unit(gh_per_day, item.name, item.plural)} a day, {regret}. "
        f"Neither stockpile could carry a count below zero.",

        # 6) cold spring's eve — final accounting
        f"On the eve of the first spring thaw — at the end of "
        f"{n_unit(days, 'day')} of winter — the two neighbors sat very "
        f"differently. In a {ant_container.name} at the heart of the "
        f"burrow, {ant.name} had begun winter with "
        f"{n_unit(ant_stock, item.name, item.plural)}, and across the cold "
        f"weeks {ant.he_she} had taken only "
        f"{n_unit(ant_per_day, item.name, item.plural)} a day. "
        f"{grasshopper.name}, in {grasshopper.his_her} thin "
        f"{gh_container.name}, had begun with only "
        f"{n_unit(gh_stock, item.name, item.plural)}, and ate "
        f"{n_unit(gh_per_day, item.name, item.plural)} per day, {hungry}. "
        f"A stockpile, once it runs out, cannot go below zero.",
    ]

    body = _render_subplot(scene, survival_subplots)
    question_what = (
        f"how many {item.plural} {ant.name} has left at the end of winter"
    )
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, question_what)}"
    )

    plan = (
        f"I compute leftover for {ant.name} as initial minus days times rate, "
        f"then clamp to 0 if negative using max."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro = _aesopian_intro(scene, "milkmaid")
    greedy    = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (eggs × eggs-per-hen ×
    # coins-per-egg) but each grounds the daydream in a different
    # container, item, and sensory setting. The Milkmaid's mood swings
    # between hopeful imagining and the small flickers of regret that
    # warn she may be counting too far ahead.
    egg_chain_subplots = [
        # 1) classic — wooden pail of milk balanced on her head
        f"{maid.name} walked the long road to market with her wooden "
        f"pail balanced upon her head, the milk inside slopping gently "
        f"with every step. {cap(greedy)}, she began to count out her "
        f"coming fortune. The milk would buy {n_unit(eggs, 'egg')} from "
        f"the poultry stall; each would hatch into a fine hen; each hen "
        f"would lay {n_unit(eggs_per_hen_per_year, 'egg')} in the course "
        f"of a year; and every one of those eggs would fetch "
        f"{n_unit(coins_per_egg, 'coin')} at market. She walked faster, "
        f"smiling to herself.",

        # 2) duck eggs in a willow basket, returning from the henhouse
        f"Carrying a willow basket of duck eggs from the henhouse to the "
        f"kitchen door, {maid.name} let her thoughts run further than "
        f"her feet. {cap(greedy)}, she traced out the chain on her "
        f"fingers. The coins from the morning's eggs would buy "
        f"{n_unit(eggs, 'egg')} more; each would warm and hatch under a "
        f"good broody hen; each grown hen would give "
        f"{n_unit(eggs_per_hen_per_year, 'egg')} a year; and at market "
        f"each of those would sell for {n_unit(coins_per_egg, 'coin')}. "
        f"The basket creaked. She did not feel its weight at all.",

        # 3) butter pats in a pot beside the kitchen fire, planning
        f"Beside the kitchen fire one cool evening, {maid.name} stirred "
        f"butter into pats in a clay pot and let her mind wander. "
        f"{cap(greedy)}, she planned the future of her small earnings. "
        f"From the butter sales she would buy {n_unit(eggs, 'egg')}; "
        f"each would hatch; each hen, once grown, would lay "
        f"{n_unit(eggs_per_hen_per_year, 'egg')} across a year; and at "
        f"the village market each egg would bring "
        f"{n_unit(coins_per_egg, 'coin')}. She stirred more slowly, "
        f"already imagining the coins clinking in her apron pouch.",

        # 4) ribbons she would buy with the proceeds — pure daydream
        f"All the way to the village fair, {maid.name} planned which "
        f"ribbons she would buy when her fortune came in. {cap(greedy)}, "
        f"she did the sums under her breath. First she would purchase "
        f"{n_unit(eggs, 'egg')} from the poultry-woman; each egg would "
        f"hatch; each hen would lay {n_unit(eggs_per_hen_per_year, 'egg')} "
        f"in a year; every egg would sell for "
        f"{n_unit(coins_per_egg, 'coin')}. She could already see herself "
        f"in a new hair-ribbon the colour of plums, the envy of every "
        f"girl in the parish.",

        # 5) cheese rounds at market, half-distracted by the daydream
        f"At the market stall where she sold her small cheese rounds, "
        f"{maid.name} stood between a cart of turnips and a knot of "
        f"buyers and let herself dream. {cap(greedy)}, she worked the "
        f"plan through. With the cheese-money she would buy "
        f"{n_unit(eggs, 'egg')}; each would hatch into a hen; each hen "
        f"would lay {n_unit(eggs_per_hen_per_year, 'egg')} in a year; "
        f"and every egg, in turn, would sell here for "
        f"{n_unit(coins_per_egg, 'coin')}. A buyer asked her price "
        f"twice before she heard him.",

        # 6) cream in a jar — jar nearly tipped, dream wavering
        f"{maid.name} carried a heavy jar of cream home from the dairy, "
        f"and the morning light made the future seem easy. {cap(greedy)}, "
        f"she counted her wealth before she had it. The cream would sell "
        f"for enough to buy {n_unit(eggs, 'egg')}; each would hatch into "
        f"a hen; each hen would give "
        f"{n_unit(eggs_per_hen_per_year, 'egg')} in a year; and every "
        f"egg would fetch {n_unit(coins_per_egg, 'coin')} at market. The "
        f"jar tilted in her hands. For an instant she paused, "
        f"{regretful}, then steadied it and walked on.",
    ]

    body = _render_subplot(scene, egg_chain_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many coins {maid.name} would earn after one year if everything went perfectly')}"
    )

    plan = (
        "I multiply eggs × eggs-per-hen-per-year × coins-per-egg "
        "to chain the daydream into a single total."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro = _aesopian_intro(scene, "milkmaid")
    greedy    = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (cow-cost ceiling-divided
    # by cups-per-day × coin-per-cup) but each grounds it in a different
    # container, item, or market setting. The Milkmaid's mood ranges
    # from eager investment to nervous arithmetic and a flicker of
    # second-guessing as she stakes her savings on the cow.
    investment_subplots = [
        # 1) classic — cow bought, milk pail counted day after day
        f"{maid.name} had spent {n_unit(cow_cost, 'coin')} on a fine "
        f"brown cow, and {greedy}, she sat down to plan the days ahead. "
        f"Each morning her wooden pail would fill with "
        f"{n_unit(cups_per_day, 'cup')} of warm milk; each cup, taken to "
        f"market, would fetch {n_unit(coin_per_cup, 'coin')}. She marked "
        f"a tally on the inside of her cottage door, telling herself she "
        f"would make a notch every evening until the cow had paid for "
        f"itself.",

        # 2) cart trips with milk to market, calculating the climb back
        f"{maid.name} loaded her small cart with the day's milk and set "
        f"off down the lane to market, the cow's price of "
        f"{n_unit(cow_cost, 'coin')} still heavy on her mind. The cow "
        f"gave {n_unit(cups_per_day, 'cup')} a day; at the village "
        f"square each cup sold steadily for {n_unit(coin_per_cup, 'coin')}. "
        f"{cap(greedy)}, she did the sum on her fingers as the cart "
        f"creaked, working out how many such trips she would need before "
        f"the debt was clear.",

        # 3) coins in a leather pouch by the kitchen fire
        f"By the kitchen fire each evening, {maid.name} emptied her "
        f"day's earnings from a leather pouch and counted them out on "
        f"the hearthstone. The cow had cost her {n_unit(cow_cost, 'coin')} "
        f"— a sum that had emptied her savings. Now the cow gave "
        f"{n_unit(cups_per_day, 'cup')} a day; each cup brought home "
        f"{n_unit(coin_per_cup, 'coin')}. {cap(greedy)}, she stacked the "
        f"coins into little piles and watched the pouch grow no faster "
        f"than the days went by.",

        # 4) jars of milk lined up at the market stall, cautious mood
        f"At her market stall, {maid.name} arranged her milk-jars in a "
        f"neat row and tried not to think too hard about the "
        f"{n_unit(cow_cost, 'coin')} she had handed to the cattle-trader. "
        f"The new cow gave {n_unit(cups_per_day, 'cup')} a day; each cup "
        f"sold for {n_unit(coin_per_cup, 'coin')} to whichever neighbour "
        f"came first. {cap(regretful)}, she wondered for a moment "
        f"whether she had been too quick to spend; then she squared her "
        f"shoulders and waited for buyers.",

        # 5) cream pail tipped — sober calculation despite the mishap
        f"{maid.name} sat on the milking-stool with her pail steaming "
        f"between her knees, weighing the bargain she had struck. The "
        f"cow had cost {n_unit(cow_cost, 'coin')}, every spare bit she "
        f"owned. From the pail came {n_unit(cups_per_day, 'cup')} of "
        f"good milk a day; at market each cup brought "
        f"{n_unit(coin_per_cup, 'coin')}. A breath of wind tipped a "
        f"little cream over the rim, and {regretful}, she remembered "
        f"how thin her margin was.",

        # 6) ribbons window in the village — the dream beyond break-even
        f"Walking past the ribbon-seller's window in the village, "
        f"{maid.name} touched a soft length of yellow silk and tried to "
        f"read the price. The cow had cost her {n_unit(cow_cost, 'coin')}, "
        f"and she could not buy a thread of ribbon until that sum had "
        f"come back. The cow gave {n_unit(cups_per_day, 'cup')} a day; "
        f"each cup sold for {n_unit(coin_per_cup, 'coin')}. {cap(greedy)}, "
        f"she counted the days under her breath, eyes still on the "
        f"yellow silk in the glass.",
    ]

    body = _render_subplot(scene, investment_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'the smallest whole number of days until {maid.name} fully recovers the cost of the cow')}"
    )

    plan = (
        "I find daily revenue (cups × coin-per-cup), then ceiling-divide "
        "the cow's cost by that revenue."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro = _aesopian_intro(scene, "milkmaid")
    greedy    = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (spilled × per-cup) but
    # each grounds the loss in a different container, setting, and
    # small disaster. The Milkmaid's mood begins greedy or hopeful and
    # falls hard into regret as the milk hits the ground.
    spilled_subplots = [
        # 1) classic — pail on the head, dream broken on the road to market
        f"{maid.name} balanced her wooden pail on her head and walked "
        f"the road to market with {n_unit(full_cups, 'cup')} of fresh "
        f"milk swaying gently above her. {cap(greedy)}, she was halfway "
        f"through her daydream when her foot caught a stone and the "
        f"pail tipped. {n_unit(spilled, 'cup')} splashed down into the "
        f"dust. Each of those cups would have sold for "
        f"{n_unit(per_cup, 'coin')} at the stalls. {cap(regretful)}, "
        f"she stared at the pale pool darkening the road.",

        # 2) jar of cream knocked from the kitchen table
        f"In her kitchen, {maid.name} set a tall jar holding "
        f"{n_unit(full_cups, 'cup')} of cream on the table while she "
        f"swept the hearth. {cap(greedy)}, she was already counting the "
        f"profit when her elbow caught the jar's lip. It tilted, "
        f"steadied, and then went over. {n_unit(spilled, 'cup')} ran "
        f"across the boards and dripped through the cracks. Each spilled "
        f"cup of cream would have fetched {n_unit(per_cup, 'coin')} at "
        f"market. {cap(regretful)}, she watched the white pool widen.",

        # 3) basket of milk-flasks tipping off the cart
        f"{maid.name} drove her cart to the village fair with a basket "
        f"of milk-flasks holding {n_unit(full_cups, 'cup')} between her "
        f"feet. The wheel struck a rut; the basket pitched; and "
        f"{n_unit(spilled, 'cup')} of milk soaked into the straw before "
        f"she could right it. Each of those cups would have brought "
        f"{n_unit(per_cup, 'coin')} from the townspeople queueing at her "
        f"stall. {cap(regretful)}, she pulled the cart to a halt and "
        f"sat very still for a moment in the road.",

        # 4) pot at the market — bumped by a passing customer
        f"At the market, {maid.name} ladled milk from a clay pot of "
        f"{n_unit(full_cups, 'cup')} into the jugs of customers, "
        f"{greedy}. A man with a heavy basket pushed past her stall and "
        f"the pot rocked off its trivet. {n_unit(spilled, 'cup')} ran "
        f"across the boards and over the edge into the gutter. Each "
        f"lost cup had been promised at {n_unit(per_cup, 'coin')}. "
        f"{cap(regretful)}, she set the pot upright with hands that "
        f"would not quite stop trembling.",

        # 5) pouch of curds in a leather flask, dropped on the path
        f"Returning from the dairy with a leather flask of "
        f"{n_unit(full_cups, 'cup')} of buttermilk, {maid.name} stepped "
        f"over a fallen branch and the flask slipped from her arm. The "
        f"stopper popped free and {n_unit(spilled, 'cup')} poured into "
        f"the bracken before she could right it. Each of those cups "
        f"would have sold for {n_unit(per_cup, 'coin')} to the inn at "
        f"the crossroads. {cap(regretful)}, she stood on the path and "
        f"counted the loss in her head.",

        # 6) pail at the milking stool, kicked over by a restless cow
        f"{maid.name} sat on her milking-stool with her pail brimming "
        f"to {n_unit(full_cups, 'cup')}, her eyes already on the wealth "
        f"the morning would bring. {cap(greedy)}, she did not see the "
        f"cow shift its weight. A hoof clipped the rim and the pail "
        f"toppled; {n_unit(spilled, 'cup')} pulsed across the byre "
        f"floor. Each cup, sold at market, would have brought "
        f"{n_unit(per_cup, 'coin')}. {cap(regretful)}, she pressed her "
        f"forehead against the cow's warm flank and said nothing.",
    ]

    body = _render_subplot(scene, spilled_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many coins {maid.name} lost by spilling')}"
    )

    plan = "I multiply the spilled cups by the price per cup."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
        f"In the corner of an orchard {species_phrase(fox)} stopped beneath "
        f"a low arbor where a heavy bunch of purple grapes hung "
        f"{n_unit(grape_height, 'foot', 'feet')} above the trodden grass. "
        f"{fox.name}, {hungry}, paused there with "
        f"{fox.his_her} mouth watering at the dusty bloom on each grape. "
        f"A trial spring carried {fox.him_her} "
        f"{n_unit(per_jump, 'foot', 'feet')} into the air, and "
        f"{fox.he_she} reasoned that each leap, if {fox.he_she} could "
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
    a = scene.pick_int(1, 30)
    b = scene.pick_int(1, 30)

    expr = Let(
        bindings=[("country-amt", Lit(a)),
                  ("city-amt",    Lit(b))],
        body=App("abs", [App("-", [Var("city-amt"), Var("country-amt")])]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "two-mice")
    content   = scene.rng.choice(EMO_CONTENT)
    greedy    = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (|city - country|), each
    # grounding the count in a different item / container / setting.
    # The country mouse's modest store contrasts with the city mouse's
    # uneasy hoard; the difference is what the question asks about.
    food_comparison_subplots = [
        # 1) cheese rinds in a country pouch vs cake crumbs in a city drawer
        f"{country.name} the country mouse opened {country.his_her} "
        f"little leather pouch by the hearth of a hollow stump, "
        f"{content}: inside lay {n_unit(a, 'cheese rind', 'cheese rinds')} "
        f"saved from a farmer's table. Far away, in a wallpapered "
        f"drawer behind a townhouse skirting board, {city.name} the "
        f"city mouse counted {n_unit(b, 'cake crumb', 'cake crumbs')} "
        f"swept from a kitchen tray, {greedy}. Each mouse looked at "
        f"the other's tally and wondered, in {country.his_her} own way, "
        f"who had truly more.",

        # 2) hazelnuts in a burrow vs raisins in a kitchen jar
        f"Beneath a tangle of hedge roots, {country.name} kept "
        f"{n_unit(a, 'hazelnut')} tucked into a small acorn-cup, "
        f"{content} with {country.his_her} quiet hoard. In a porcelain "
        f"jar high on a city pantry shelf, {city.name} hunched over "
        f"{n_unit(b, 'raisin')} pinched from a baker's mixing bowl, "
        f"{greedy} and listening for footsteps. They had argued before "
        f"about whose home was richer; tonight the question was simply "
        f"how far apart their two counts ran.",

        # 3) acorns under the floor vs butter pats in a city cellar
        f"{country.name} stored {n_unit(a, 'acorn')} under a loose "
        f"floorboard of {country.his_her} burrow, {content} that the "
        f"oak above would drop more in autumn. Down in a cool city "
        f"cellar, {city.name} brooded over "
        f"{n_unit(b, 'butter pat', 'butter pats')} stolen one by one "
        f"from a dairy crock, {greedy} and watchful of the cat. Neither "
        f"could quite agree on whose larder was larger, only that the "
        f"gap between them mattered.",

        # 4) berries in a basket vs gouda wedges in a sideboard
        f"On the lip of a meadow, {country.name} carried home a small "
        f"woven basket holding {n_unit(a, 'berry', 'berries')}, "
        f"{content} after a morning's foraging. In a velvet-lined "
        f"sideboard drawer in the city, {city.name} guarded "
        f"{n_unit(b, 'gouda wedge', 'gouda wedges')} pilfered from a "
        f"merchant's plate, {greedy} and unable to sleep for fear of "
        f"thieves. The two mice met to compare, as they often did, "
        f"and the difference between their stocks was the talking point.",

        # 5) walnuts in a pouch vs swiss-cheese chunks in a hole pantry
        f"By a moss-cushioned fireplace in the country, {country.name} "
        f"poured {n_unit(a, 'walnut')} from {country.his_her} "
        f"mouse-sized pouch onto the hearth-stone, {content}. Across "
        f"the long road, in a hole-in-the-wall pantry tucked behind a "
        f"city kitchen, {city.name} stacked "
        f"{n_unit(b, 'swiss-cheese chunk', 'swiss-cheese chunks')} into "
        f"a precarious pile, {greedy} and forever rearranging. Whichever "
        f"of them had more, the gap was real and worth measuring.",

        # 6) breadcrumbs in a thimble vs cheddar slices in a city sack
        f"{country.name} sat on a flat stone outside {country.his_her} "
        f"burrow with {n_unit(a, 'breadcrumb')} gathered in a thimble, "
        f"{content} with the meal that lay ahead. Meanwhile, {city.name} "
        f"hunched in a damp city sack behind a tavern door, counting "
        f"{n_unit(b, 'cheddar slice', 'cheddar slices')} again and "
        f"again, {regretful} of having strayed so far from the quiet "
        f"fields. Yet still the city mouse could not stop tallying — "
        f"and the difference between the two stores was plain.",
    ]

    body = _render_subplot(scene, food_comparison_subplots)
    diff_target = (
        f"the absolute difference between {country.name} "
        f"and {city.name}'s food counts"
    )
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, diff_target)}"
    )

    plan = (
        "I subtract the country mouse's count from the city mouse's "
        "count and take the absolute value."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    n_mice  = scene.pick_int(2, 5)
    total   = scene.pick_int(n_mice, n_mice * 10)

    expr = Let(
        bindings=[("total",  Lit(total)),
                  ("n-mice", Lit(n_mice))],
        body=App("quot", [Var("total"), Var("n-mice")]),
    )
    answer = evaluate(expr)

    intro = _aesopian_intro(scene, "two-mice")
    content = scene.rng.choice(EMO_CONTENT)
    greedy  = scene.rng.choice(EMO_GREEDY)

    # Six narrative subplots — same arithmetic (total // n-mice). Each
    # frames the shared feast around a different country/city food and
    # a different vessel: the country mouse hosts plainly, the city
    # mouse hosts grandly, but the meal is divided the same way.
    shared_meal_subplots = [
        # 1) cheese rinds in the country burrow's central pouch
        f"In the warm hollow of an old oak, {country.name} the country "
        f"mouse spread a worn pouch open on the moss floor. Inside lay "
        f"{n_unit(total, 'cheese rind', 'cheese rinds')}, "
        f"saved scrap by scrap from a farmer's broken plate. "
        f"{n_unit(n_mice, 'mouse', 'mice')} had gathered for the meal "
        f"— including {country.name} and {city.name}, the city visitor "
        f"— and they sat in a careful ring, {content}. The host counted "
        f"out portions slowly, leaving any remainder for the next day's "
        f"breakfast.",

        # 2) hazelnuts in a basket in the meadow clearing
        f"On a flat stone in a meadow clearing, {country.name} placed a "
        f"woven basket holding {n_unit(total, 'hazelnut')}, gathered "
        f"under the autumn trees. {n_unit(n_mice, 'mouse', 'mice')} had "
        f"come for the feast — {city.name} among them, eyeing the "
        f"basket {greedy} and remembering richer fare. Yet the country "
        f"mouse insisted the meal be divided fairly, whole nuts only, "
        f"with whatever leftover was set aside for the squirrels. The "
        f"share each mouse received was the same.",

        # 3) cake crumbs spread on a velvet napkin in the city pantry
        f"In a city pantry, beneath a tall sideboard, {city.name} laid "
        f"out a velvet napkin and tipped onto it "
        f"{n_unit(total, 'cake crumb', 'cake crumbs')} pinched from a "
        f"baker's window-tray. {n_unit(n_mice, 'mouse', 'mice')} sat "
        f"around the napkin — including the visiting {country.name}, "
        f"who watched the city mouse heap and rearrange the crumbs "
        f"{greedy}. Still, the meal must be split equally, whole crumbs "
        f"each, the remainder swept aside for tomorrow.",

        # 4) raisins in a tiny clay pot under the kitchen step
        f"{city.name} the city mouse had carried home a tiny clay pot "
        f"holding {n_unit(total, 'raisin')} stolen from a kitchen "
        f"counter, and tonight {country.name} and the others were "
        f"invited to share. {n_unit(n_mice, 'mouse', 'mice')} clustered "
        f"around the pot beneath the kitchen step. {city.name} sorted "
        f"with hungry, fussy paws, {greedy}; {country.name} sat "
        f"{content} and waited. Each mouse would get the same whole "
        f"share, no more.",

        # 5) acorns under the floorboard in the country burrow
        f"{country.name} pried up a loose floorboard in {country.his_her} "
        f"burrow to reveal {n_unit(total, 'acorn')} stored against the "
        f"frost. {n_unit(n_mice, 'mouse', 'mice')} were dining tonight, "
        f"counting {country.name}, the visiting {city.name}, and the "
        f"neighbors from down the lane. The country mouse, {content}, "
        f"announced that the acorns would be split evenly — whole nuts "
        f"only — and any uneven leftover set carefully back beneath "
        f"the board.",

        # 6) butter pats on a saucer in the city cellar
        f"On a chipped saucer in the corner of a damp city cellar, "
        f"{city.name} arranged "
        f"{n_unit(total, 'butter pat', 'butter pats')} freshly stolen "
        f"from a dairy. {n_unit(n_mice, 'mouse', 'mice')} sat around "
        f"the saucer in flickering candlelight, including the country "
        f"guest. {city.name}, {greedy}, fretted over the arrangement; "
        f"{country.name} simply waited, {content}, ready to accept "
        f"whichever share fell out of an honest split. Whole pats each, "
        f"leftover set aside.",
    ]

    body = _render_subplot(scene, shared_meal_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, 'how many whole pieces of food each mouse receives if any leftover is set aside')}"
    )

    plan = (
        "I integer-divide the total food by the number of mice and "
        "ignore the remainder."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro = _aesopian_intro(scene, "two-mice")
    content   = scene.rng.choice(EMO_CONTENT)
    greedy    = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (start - travel - food).
    # The items here are coins; what varies is the container the mouse
    # carries them in (pouch, purse, rolled-up leaf, thimble, etc.) and
    # the road or city errand that drains them.
    trip_budget_subplots = [
        # 1) tiny leather pouch on the country road
        f"{species_phrase(mouse)} set out for the city before dawn with "
        f"{n_unit(start, 'coin')} jingling in a tiny leather pouch tied "
        f"at {mouse.his_her} belt, {content} that {mouse.he_she} had "
        f"saved enough at last. Along the road {mouse.he_she} paid "
        f"{n_unit(travel, 'coin')} for a ride on the back of a passing "
        f"cart, and at a roadside inn {mouse.he_she} laid out "
        f"{n_unit(food, 'coin')} for a crust of bread and a thimble of "
        f"milk. After both transactions the pouch felt much lighter "
        f"against {mouse.his_her} side.",

        # 2) small embroidered purse to a city festival
        f"{cap(species_phrase(mouse))} buttoned a small embroidered "
        f"purse holding {n_unit(start, 'coin')} into a hidden inner "
        f"pocket, {greedy} at the thought of a festival in the city. "
        f"The carriage fare came to {n_unit(travel, 'coin')}, paid "
        f"reluctantly to a tall driver who bowed to no one. At a "
        f"market stall, {mouse.name} parted with another "
        f"{n_unit(food, 'coin')} for a wedge of cheese and a slice of "
        f"plum cake. The purse, once heavy, was much thinner now.",

        # 3) coins folded into a rolled-up leaf
        f"With {n_unit(start, 'coin')} carefully folded into a rolled-up "
        f"oak leaf and tucked beneath {mouse.his_her} cloak, {mouse.name} "
        f"left the meadow at first light. {cap(mouse.he_she)} paid "
        f"{n_unit(travel, 'coin')} to a kindly hedgehog driver who "
        f"carried {mouse.him_her} most of the way, and {n_unit(food, 'coin')} "
        f"at a noisy bakery stall for two warm rolls. By the time "
        f"{mouse.he_she} reached the city gate, the leaf-bundle felt "
        f"thin between {mouse.his_her} paws — yet the journey was real, "
        f"and so was the spending.",

        # 4) a thimble carried inside a knapsack
        f"{cap(species_phrase(mouse))} packed {n_unit(start, 'coin')} "
        f"into a battered tin thimble and slid the thimble deep into "
        f"{mouse.his_her} knapsack. The road tolls along the river "
        f"path swallowed {n_unit(travel, 'coin')} between the country "
        f"crossing and the gates of the city. Hunger drove {mouse.him_her} "
        f"to a corner stall where a city baker took {n_unit(food, 'coin')} "
        f"for hot biscuits. {cap(mouse.he_she)} sat on a curb to count "
        f"what remained in the thimble, {regretful} of how quickly it "
        f"had drained.",

        # 5) coins in a hollow walnut shell
        f"For travel-money, {mouse.name} the mouse used a trick of the "
        f"old burrow folk: {mouse.he_she} hid {n_unit(start, 'coin')} "
        f"inside a hollow walnut shell, sealed with a smear of beeswax. "
        f"On the way to the market town, {n_unit(travel, 'coin')} was "
        f"spent on stage-fares and a copper for the bridge-toll. At a "
        f"vendor's cart {mouse.he_she} traded another "
        f"{n_unit(food, 'coin')} for fresh raisins and a sliver of "
        f"butter. The walnut shell, when {mouse.he_she} pried it open "
        f"again, sounded much quieter than before.",

        # 6) a small drawstring sack into the bustle of the city
        f"A small drawstring sack of {n_unit(start, 'coin')} swung at "
        f"{mouse.name}'s side as {mouse.he_she} stepped onto the city's "
        f"crowded paving stones, {greedy} for the wonders {mouse.he_she} "
        f"had heard described. The trolley-mouse charged "
        f"{n_unit(travel, 'coin')} for the long ride from the country "
        f"gate to the central square; a vendor of cheese-rinds took "
        f"another {n_unit(food, 'coin')} for a paper twist of "
        f"crumbles. {cap(mouse.he_she)} paused at a fountain, untied "
        f"the sack, and weighed what remained against the long road "
        f"home.",
    ]

    body = _render_subplot(scene, trip_budget_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many coins {mouse.name} has left after the trip')}"
    )

    plan = (
        "I subtract the travel cost and the food cost from the "
        "starting coins."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro    = _aesopian_intro(scene, "dog-shadow")
    greedy   = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (start-bones decremented by 1)
    # but each grounds it in a different load + crossing + sensory hook.
    # Item per subplot is varied: bones, biscuits, sticks, scraps of meat,
    # marrow-bones, soft bread chunks. The narrative item changes; the
    # underlying expression keeps the `start-bones` name (math invariant).
    # Each entry is (subplot_text, item_singular, item_plural).
    double_loss_subplots = [
        # 1) classic — bones across a stream
        (f"{species_phrase(dog)} trotted across a low stone footbridge with "
         f"{n_unit(bones, 'bone')} clamped firmly between {dog.his_her} jaws, "
         f"feeling very pleased with the morning's prize. Halfway over, "
         f"{dog.he_she} glanced down at the slow brown water and saw — "
         f"{greedy} — what looked like another dog below, with the very "
         f"same load. {cap(dog.he_she)} opened {dog.his_her} mouth to "
         f"snatch at that other dog's bone, but of course the moment "
         f"{dog.his_her} jaws parted a single bone tumbled away into the "
         f"stream and was gone. {cap(dog.he_she)} stood blinking, "
         f"{regretful}.",
         "bone", "bones"),

        # 2) biscuits in a soft cloth bundle
        (f"{species_phrase(dog)} had been given {n_unit(bones, 'biscuit')} "
         f"by the baker's wife, who tied them into a soft little cloth "
         f"bundle that {dog.he_she} carried gently in {dog.his_her} mouth. "
         f"On the plank bridge over the brook the bundle dipped down "
         f"toward the water, and there in the ripples {dog.he_she} saw a "
         f"second dog with what looked like a fatter bundle. {cap(greedy)}, "
         f"{dog.he_she} lunged — and one biscuit slipped out of the "
         f"loose corner of the cloth and dropped, lost in the current.",
         "biscuit", "biscuits"),

        # 3) sticks for fetch — by a pond
        (f"{species_phrase(dog)} had been collecting {n_unit(bones, 'stick')} "
         f"all afternoon along the path that ran beside the pond, holding "
         f"the bundle proudly in a wide grip across {dog.his_her} jaws. "
         f"As {dog.he_she} skirted the bank, the still water caught a "
         f"clear picture of {dog.him_her} below. {cap(dog.he_she)} saw, or "
         f"thought {dog.he_she} saw, another dog with a thicker bunch of "
         f"sticks, and {greedy}, {dog.he_she} barked at the rival. The "
         f"bark let one stick fall, plop, into the pond.",
         "stick", "sticks"),

        # 4) scraps of meat from a butcher — over a stream
        (f"{species_phrase(dog)} was carrying home {n_unit(bones, 'scrap')} "
         f"of meat from the butcher, soft and savory and twisted in a bit "
         f"of brown paper held lightly between {dog.his_her} teeth. At "
         f"the shallow stream {dog.he_she} stepped out onto the stepping-"
         f"stones, and the water below showed a phantom dog with what "
         f"seemed a richer parcel. {cap(dog.he_she)} could not help "
         f"{dog.him_her}self — {greedy}, {dog.he_she} snapped — and a "
         f"single scrap fluttered free, swept off downstream before "
         f"{dog.he_she} could lift a paw.",
         "scrap of meat", "scraps of meat"),

        # 5) marrow-bones over a footbridge
        (f"It was a fine cold day, and {species_phrase(dog)} had "
         f"{n_unit(bones, 'marrow-bone')} from the kitchen, big and pale "
         f"and worth a long quiet afternoon's chewing. The footbridge "
         f"over the river was old and creaky. As {dog.he_she} crossed, "
         f"{dog.he_she} caught sight of {dog.his_her} reflection in the "
         f"deep water and mistook it for a stranger with even better "
         f"marrow-bones. {cap(dog.he_she)} growled, {greedy}, and the "
         f"growl shook one marrow-bone loose from {dog.his_her} jaws. "
         f"It plunged in with a heavy splash, and {dog.he_she} stood "
         f"there {regretful}.",
         "marrow-bone", "marrow-bones"),

        # 6) soft bread chunks from the kitchen — over a brook
        (f"{species_phrase(dog)} had stolen {n_unit(bones, 'bread chunk')} "
         f"from the kitchen table while no one was looking and was now "
         f"trotting back to {dog.his_her} hiding place across the brook. "
         f"On the slick wet stones in the middle of the crossing, "
         f"{dog.he_she} looked down and saw, beneath the moving water, "
         f"another dog whose mouth seemed somehow fuller. {cap(greedy)}, "
         f"{dog.he_she} dipped {dog.his_her} head to challenge the "
         f"creature — and one soft bread chunk fell straight from "
         f"{dog.his_her} mouth into the brook, where it dissolved at "
         f"once into mush.",
         "bread chunk", "bread chunks"),
    ]

    idx = scene.rng.randrange(len(double_loss_subplots))
    body, _item_s, item_p = double_loss_subplots[idx]
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many {item_p} {dog.name} has now')}"
    )

    plan = "I decrement the starting count by one (the dropped piece)."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro    = _aesopian_intro(scene, "dog-shadow")
    greedy   = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (expected-bones minus
    # actual-bones, where actual = expected - 1, giving a regret of 1).
    # Each subplot uses a different item the dog set out to bring home,
    # frames the loss as a concrete moment, and ends on the dog wishing
    # things had gone differently. The math is invariant; the items vary.
    # Each entry is (subplot_text, item_singular, item_plural).
    regret_subplots = [
        # 1) classic — bones meant for a buried hoard
        (f"{species_phrase(dog)} had set out that morning meaning to bring "
         f"home {n_unit(expected_bones, 'bone')} for {dog.his_her} secret "
         f"corner under the rose bush. Crossing the stream on the way back, "
         f"{dog.he_she} saw {dog.his_her} reflection — {greedy} — and "
         f"snatched at the shadow's bone. One bone spun away into the "
         f"current, and {dog.he_she} arrived home with one fewer than "
         f"the count {dog.he_she} had been so proud of. {cap(dog.he_she)} "
         f"sat by the rose bush, {regretful}, comparing what {dog.he_she} "
         f"meant to have brought against what was actually in the pile.",
         "bone", "bones"),

        # 2) biscuits the kitchen-girl had counted out
        (f"The kitchen-girl had counted out {n_unit(expected_bones, 'biscuit')} "
         f"into a cloth and sent {species_phrase(dog)} off with them, "
         f"saying not to lose a single one. On the bridge over the brook "
         f"{dog.he_she} caught sight of another dog in the water with "
         f"what seemed an even fuller cloth, and {greedy}, snapped at "
         f"the rival. One biscuit slipped free and was swallowed by the "
         f"brown water. When {dog.he_she} came back to the kitchen, "
         f"{regretful}, the count was short by exactly the difference "
         f"between what had been promised and what actually arrived.",
         "biscuit", "biscuits"),

        # 3) sticks gathered for the master's fire
        (f"The master had asked {dog.name} to fetch {n_unit(expected_bones, 'stick')} "
         f"for the evening fire, and {dog.name} had gathered them all "
         f"along the path beside the pond. Halfway home, the still water "
         f"showed a dog with what looked like a thicker bunch, and "
         f"{dog.he_she} lunged at it, {greedy}. One stick clattered "
         f"down to the bank and rolled into the pond. {cap(dog.he_she)} "
         f"reached the cottage with one fewer than the master had "
         f"requested, and the gap between expected and delivered "
         f"sticks lay plainly between {dog.him_her} and the hearth.",
         "stick", "sticks"),

        # 4) scraps of meat tallied by the butcher
        (f"The butcher had tied up {n_unit(expected_bones, 'scrap')} of "
         f"meat in a paper for {species_phrase(dog)} to carry home, and "
         f"the count had been said aloud, both of them nodding. On the "
         f"footbridge over the river the paper sagged near the water; "
         f"{dog.he_she} saw a phantom dog with a richer parcel and, "
         f"{greedy}, snapped — losing one scrap to the river. By "
         f"evening, when the cook checked the parcel against the "
         f"butcher's tally, the actual count fell short of the expected "
         f"by exactly that single greedy moment.",
         "scrap of meat", "scraps of meat"),

        # 5) marrow-bones for a long winter afternoon
        (f"{species_phrase(dog)} had hoped to chew through "
         f"{n_unit(expected_bones, 'marrow-bone')} all afternoon, the way "
         f"{dog.he_she} had planned it that morning, lined up neatly in "
         f"a row by the fire. But on the way back across the stream "
         f"{dog.he_she} growled at {dog.his_her} own reflection — "
         f"{greedy} — and a single marrow-bone tumbled in. By dusk, "
         f"as {dog.he_she} laid out the row, {regretful}, the line "
         f"was shorter than it should have been. The difference between "
         f"the imagined row and the real one was the day's small lesson.",
         "marrow-bone", "marrow-bones"),

        # 6) soft bread chunks from a careful loaf
        (f"{cap(species_phrase(dog))} had been allowed exactly "
         f"{n_unit(expected_bones, 'bread chunk')} from the morning loaf "
         f"by the baker's wife, who had arranged them carefully on a low "
         f"plank for {dog.him_her} to carry home. On the brook crossing "
         f"the water mirrored {dog.him_her}, and {greedy}, {dog.he_she} "
         f"lunged at the seeming rival's mouthful. One soft chunk fell "
         f"into the brook and dissolved at once. {cap(dog.he_she)} "
         f"reached the doorstep, {regretful}, and the loaf-keeper saw "
         f"plainly the gap between the careful count and the count that "
         f"actually arrived.",
         "bread chunk", "bread chunks"),
    ]

    idx = scene.rng.randrange(len(regret_subplots))
    body, _item_s, item_p = regret_subplots[idx]
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many {item_p} {dog.name} fell short by, compared to what {dog.he_she} expected to bring home')}"
    )

    plan = "I subtract the actual count (one fewer) from the expected count to find the gap."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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

    intro    = _aesopian_intro(scene, "dog-shadow")
    greedy   = scene.rng.choice(EMO_GREEDY)
    regretful = scene.rng.choice(EMO_REGRETFUL)

    # Six narrative subplots — same arithmetic (start - given + received)
    # but each grounds the bad trade in a different item + setting.
    # The dog's greedy hope at the trade ("bigger ones!") is undone by the
    # trader's cheat. Math invariant; items and tone vary.
    # Each entry is (subplot_text, item_singular, item_plural).
    exchange_loss_subplots = [
        # 1) classic — bones traded for "bigger" bones
        (f"{species_phrase(dog)} arrived at {trader.name}'s back gate with "
         f"{n_unit(start, 'bone')} stacked carefully in a small basket. "
         f"{trader.name} eyed the pile and offered a deal: hand over "
         f"{n_unit(given, 'bone')} of those plain bones, and "
         f"{trader.he_she} would give back the same number of much "
         f"bigger ones from a sack in the shed. {cap(dog.he_she)} agreed, "
         f"{greedy}. But when {trader.name} returned, only "
         f"{n_unit(received, 'bone')} dropped from the sack into the "
         f"basket — fewer than promised, and {trader.name} shrugged as "
         f"if {dog.he_she} ought to be grateful.",
         "bone", "bones"),

        # 2) biscuits traded for "bakery seconds"
        (f"By the side of the road {trader.name} had set up a little "
         f"folding stall, and {species_phrase(dog)} stopped there with "
         f"{n_unit(start, 'biscuit')} that the kitchen-girl had spared "
         f"{dog.him_her}. {trader.name} promised that if {dog.he_she} "
         f"handed over {n_unit(given, 'biscuit')}, {trader.he_she} "
         f"would put back the same count of finer bakery seconds, butter-"
         f"glazed and twice the size. {cap(dog.he_she)} pushed the "
         f"biscuits across, {greedy}. {trader.name} returned only "
         f"{n_unit(received, 'biscuit')}, claiming the rest had broken "
         f"in the box.",
         "biscuit", "biscuits"),

        # 3) sticks for "seasoned hardwood"
        (f"{species_phrase(dog)} had collected {n_unit(start, 'stick')} "
         f"by the riverbank when {trader.name} came along leading a "
         f"small handcart. {cap(trader.he_she)} offered {dog.him_her} a "
         f"trade: {n_unit(given, 'stick')} of those green sticks for "
         f"the same number of seasoned hardwood pieces from the cart, "
         f"which (so {trader.he_she} swore) burned twice as long. "
         f"{cap(dog.he_she)} pushed the sticks over, {greedy}. From "
         f"the cart {trader.name} drew only {n_unit(received, 'stick')} "
         f"and rolled the cart away whistling.",
         "stick", "sticks"),

        # 4) scraps of meat for "fresher butchery"
        (f"At the corner of the market square {species_phrase(dog)} met "
         f"{trader.name}, who looked over the {n_unit(start, 'scrap')} "
         f"of meat in {dog.his_her} cloth and made a generous-sounding "
         f"offer: hand over {n_unit(given, 'scrap')}, and {trader.he_she} "
         f"would give back the same count of fresh trimmings from "
         f"{trader.his_her} own butcher's cousin in the village. "
         f"{cap(dog.he_she)} agreed, {greedy}. The bag {trader.name} "
         f"opened in return held only {n_unit(received, 'scrap')}, and "
         f"{dog.he_she} stood blinking at it, {regretful}.",
         "scrap of meat", "scraps of meat"),

        # 5) marrow-bones for "kitchen-grade"
        (f"{species_phrase(dog)} had {n_unit(start, 'marrow-bone')} "
         f"saved up in a corner of the barn when {trader.name} stopped "
         f"by, sniffing at the heap with practiced interest. "
         f"{cap(trader.he_she)} proposed a swap: "
         f"{n_unit(given, 'marrow-bone')} for the same number of "
         f"kitchen-grade ones — pale, fat, twice the chewing. "
         f"{cap(dog.he_she)} parted with the lot, {greedy}, and watched "
         f"{trader.name} reach into a sack and produce only "
         f"{n_unit(received, 'marrow-bone')}, smiling as though "
         f"this were how every honest deal ended.",
         "marrow-bone", "marrow-bones"),

        # 6) bread chunks for "soft loaf-ends"
        (f"{cap(trader.name)} stopped {species_phrase(dog)} at the gate "
         f"of the cottage and admired the {n_unit(start, 'bread chunk')} "
         f"that {dog.he_she} carried. {cap(trader.he_she)} proposed a "
         f"trade — {n_unit(given, 'bread chunk')} for the same number of "
         f"soft loaf-ends from the bakery, the sort that went quickest "
         f"down the throat. {cap(dog.he_she)} pushed the chunks across, "
         f"{greedy}. From {trader.his_her} bag came back only "
         f"{n_unit(received, 'bread chunk')}, and {trader.name} was "
         f"already walking briskly off down the lane.",
         "bread chunk", "bread chunks"),
    ]

    idx = scene.rng.randrange(len(exchange_loss_subplots))
    body, _item_s, item_p = exchange_loss_subplots[idx]
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'how many {item_p} {dog.name} has after the trade')}"
    )

    plan = "I subtract what was given away from the start, then add back what was received."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    location = scene.pick_location(tags_any=("path",), indoor=False)
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

    intro     = _aesopian_intro(scene, "lion-bulls", location)
    patient   = scene.rng.choice(EMO_PATIENT)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same arithmetic (n-bulls minus
    # bulls-defeated = remaining). Each subplot grounds the loss
    # in a distinct setting, and the bulls' shrinking number
    # makes the survivors' isolation increasingly desperate.
    remaining_after_k_subplots = [
        # 1) open meadow — counting heads at sunrise
        f"At sunrise, {species_phrase(lion)} surveyed the open meadow "
        f"where {n_unit(n_bulls, 'bull')} had once grazed in a tight "
        f"crescent. Many seasons of patient hunting had passed since "
        f"the herd first quarreled. {cap(lion.he_she)} counted the "
        f"still shapes hidden in the long grass — {defeated} of the "
        f"bulls had already fallen, one at a time, on separate days. "
        f"The survivors stood scattered, {desperate}, each alone in a "
        f"pocket of dew-soaked clover. The lion sat back on "
        f"{lion.his_her} haunches {patient} and tried to count how "
        f"many of the original {n_bulls} bulls were still upright in "
        f"the meadow.",

        # 2) hilltop pasture — wind carrying news of losses
        f"On a high hilltop pasture, where the wind carried the "
        f"smell of broken grass for miles, the {n_bulls} "
        f"{unit(n_bulls, 'bull')} had once been impossible to "
        f"approach. Now {species_phrase(lion)} crossed the bald slope "
        f"openly. Over the long, slow campaign, {lion.he_she} had "
        f"brought down {defeated} of them, never two on the same "
        f"week. The remaining bulls watched from far ridges, "
        f"{desperate}, no longer trusting the wind. {cap(lion.he_she)} "
        f"paused {patient} on a flat stone and reckoned how many of "
        f"the herd were still standing.",

        # 3) valley grassland — survivors near the stream
        f"In the valley grassland by the slow stream, where "
        f"{n_unit(n_bulls, 'bull')} had once drunk together at the "
        f"same bend, only a few survivors now picked their way "
        f"between the reeds. {species_phrase(lion)} had taken "
        f"{defeated} of the herd already over many quiet weeks, and "
        f"the bulls left alive {desperate} would not even stand near "
        f"each other to drink. From a willow shadow, the lion "
        f"watched {patient}. {cap(lion.he_she)} began to count, on "
        f"the soft pads of {lion.his_her} paws, how many bulls of "
        f"the original number remained.",

        # 4) fence-line they no longer respect
        f"Along the broken fence-line that the herd had once walked "
        f"together at evening, {species_phrase(lion)} stalked at a "
        f"slow trot. The {n_bulls} {unit(n_bulls, 'bull')} had been "
        f"a tight shoulder-to-shoulder column then; now the fence "
        f"divided them, and they no longer minded. The lion had "
        f"taken {defeated} bulls from this stretch alone, picking "
        f"off whichever wandered to the rails by itself. The few "
        f"survivors paced {desperate} in the far field. The lion "
        f"sat against a fence-post {patient} and worked out how many "
        f"of the original herd were still alive.",

        # 5) clearing surrounded by tall grass
        f"In a wide clearing rimmed by tall, bristling grass, what "
        f"had once been {n_unit(n_bulls, 'bull')} grazing in a loose "
        f"ring was now a scattered remnant. {species_phrase(lion)} "
        f"had taken {defeated} of them through the long campaign — "
        f"each one alone, each one on a different day. The bulls "
        f"that remained stood {desperate} at separate corners of the "
        f"clearing, refusing to look at one another. "
        f"{cap(lion.he_she)} crouched in the shadow of a stump "
        f"{patient} and totaled how many bulls were still standing.",

        # 6) flat plain at dusk — silhouettes of the survivors
        f"At dusk on a flat plain, the silhouettes of the surviving "
        f"bulls were spread far across the grass. There had been "
        f"{n_unit(n_bulls, 'bull')} at the start of the long season, "
        f"and {species_phrase(lion)} had taken {defeated} since then, "
        f"one by one. The remaining shapes stood {desperate}, each "
        f"in its own patch of fading light. {cap(lion.he_she)} "
        f"watched the long shadows lean across the plain {patient} "
        f"and counted how many bulls of the original herd were still "
        f"left to take.",
    ]

    body = _render_subplot(scene, remaining_after_k_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, 'how many bulls remain')}"
    )

    plan = "I subtract the defeated count from the original number of bulls."
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
    location = scene.pick_location(tags_any=("path",), indoor=False)
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
    combined = n_bulls * bull_strength

    intro     = _aesopian_intro(scene, "lion-bulls", location)
    patient   = scene.rng.choice(EMO_PATIENT)
    desperate = scene.rng.choice(EMO_DESPERATE)

    # Six narrative subplots — same boolean (lion > one-bull AND lion <
    # combined). Each subplot makes the math feel like a real measuring
    # contest: the lion's confident-against-one strength on one side, the
    # bulls' fragile-but-formidable union on the other. Settings vary;
    # the boolean asks whether divide-and-conquer is the lion's only
    # winning path.
    divide_conquer_subplots = [
        # 1) open meadow — old herd-test
        f"In the heart of an open meadow stood {n_unit(n_bulls, 'bull')}, "
        f"each tested at the spring tournament to be of strength "
        f"{bull_strength}. {species_phrase(lion)} watched from the long "
        f"grass {patient}, {lion.his_her} own measured strength known to "
        f"be {lion_strength}. Bull by bull, {lion.he_she} could outmatch "
        f"any one of them one-on-one. But when the bulls had stood "
        f"shoulder to shoulder, their unified strength came to "
        f"{combined} — too great for any single lion. The question now "
        f"was simply whether the lion's only winning path lay through "
        f"dividing the herd.",

        # 2) hilltop pasture — measured in spring tests
        f"On a hilltop pasture, each of the {n_unit(n_bulls, 'bull')} "
        f"had been weighed and trial-tested by the elder bulls in "
        f"younger years, and each carried strength {bull_strength}. "
        f"{species_phrase(lion)}, with strength {lion_strength}, paced "
        f"the ridge {patient}. Alone, a bull would not stand against "
        f"{lion.him_her}; but pressed together, the herd's combined "
        f"strength rose to {combined}, beyond anything one cat could "
        f"meet. The bulls already paced apart, {desperate}, no longer "
        f"sure of one another. Whether the lion needed them divided to "
        f"win was the only remaining question.",

        # 3) valley grassland — by the slow stream
        f"In the valley grassland, {species_phrase(lion)} crouched at "
        f"the reed-line {patient}, watching {n_unit(n_bulls, 'bull')} "
        f"drink at separate bends of the slow stream. Each bull had "
        f"strength {bull_strength}; the lion's own strength was "
        f"{lion_strength}. Solo, no bull at the water could withstand "
        f"{lion.him_her}; together at the bend they had once held "
        f"{combined} between them, more than enough to chase a lion off. "
        f"The math of the situation was clear, and the only thing left "
        f"to settle was the boolean: did the lion's chance depend on "
        f"keeping the bulls divided?",

        # 4) fence-line they no longer respect
        f"Along an old fence-line that the herd had once walked together "
        f"each evening, {n_unit(n_bulls, 'bull')} now drifted past the "
        f"rails singly. Every bull had a measured strength of "
        f"{bull_strength}, and {species_phrase(lion)}, at "
        f"{lion_strength}, padded the far side {patient}. One bull at "
        f"the fence was no contest for {lion.him_her}; the herd at full "
        f"muster, however, mounted a combined strength of {combined}, "
        f"which would have flung the lion clean off the rails. The "
        f"bulls' unease left them {desperate}, drifting further apart "
        f"each night. The remaining question was a yes-or-no.",

        # 5) clearing surrounded by tall grass
        f"In a wide clearing rimmed by tall grass, {n_unit(n_bulls, 'bull')} "
        f"stood at suspicious distances, each of strength "
        f"{bull_strength}. {species_phrase(lion)} crossed the clearing "
        f"{patient}, knowing {lion.his_her} own strength to be "
        f"{lion_strength}. Single-handedly against a single bull, the "
        f"lion held the upper paw; but if the herd closed ranks the "
        f"combined strength of {combined} would have made short work of "
        f"{lion.him_her}. The lion sat in the long shadow at the edge "
        f"and considered: did victory depend strictly on keeping them "
        f"apart?",

        # 6) flat plain at dusk — final reckoning
        f"At dusk on a flat plain, the silhouettes of "
        f"{n_unit(n_bulls, 'bull')} stood widely scattered, each carrying "
        f"the same well-known strength {bull_strength}. "
        f"{species_phrase(lion)}, of strength {lion_strength}, watched "
        f"the long shadows lean across the grass {patient}. The lion "
        f"could meet any one of those silhouettes alone; the herd's "
        f"combined strength of {combined}, however, would simply "
        f"trample {lion.him_her}. The bulls themselves shifted "
        f"{desperate} at every distant snap of grass. All that remained "
        f"was the boolean: did the lion truly need them divided to win?",
    ]

    body = _render_subplot(scene, divide_conquer_subplots)
    user_msg = (
        f"{intro}{body}\n\n"
        f"{question_phrase(scene, f'whether {lion.name} can defeat each bull alone (lion-strength > bull-strength) yet would lose against the herd combined (lion-strength < combined-strength)')}"
    )

    plan = (
        "I check both: lion-strength > one bull's strength (alone wins) "
        "AND lion-strength < combined-strength (together the herd wins)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        plan=plan,
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
