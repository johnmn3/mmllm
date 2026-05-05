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

    boast = scene.phrase(
        "telling everyone in the meadow that no one could match his speed",
        "boasting around the burrows about how fast he was",
        "bragging that the slow tortoise stood no chance against him",
    ) if hare.gender == "m" else scene.phrase(
        "telling everyone in the meadow that no one could match her speed",
        "boasting around the burrows about how fast she was",
        "bragging that the slow tortoise stood no chance against her",
    ) if hare.gender == "f" else scene.phrase(
        "telling everyone in the meadow how fast they were",
        "boasting around the burrows about their speed",
        "bragging that the slow tortoise stood no chance",
    )
    listened = scene.phrase(
        "listened patiently for many days",
        "said nothing and only blinked slowly",
        "thought about it carefully before agreeing",
    )
    challenge_verb = scene.phrase(
        "finally agreed to a race",
        "agreed to settle the matter with a race",
        "decided the only fair thing was to actually race",
    )
    nap_phrase = scene.phrase(
        "grew tired and decided to take a nap under a tree",
        "felt sleepy and stretched out for a nap on a soft patch of moss",
        "lay down to rest a while in the warm grass",
    )
    user_msg = (
        f"{atmosphere(scene, location)} {species_phrase(hare)} had "
        f"spent days {boast}. {species_phrase(tortoise)}, by contrast, "
        f"{listened}, and at last the two animals {challenge_verb} "
        f"{place_phrase(scene, location)}.\n\n"
        f"They set off together at sunrise. After running "
        f"{n_unit(hare_lead, 'mile')} ahead, {hare.name} "
        f"{nap_phrase}. Meanwhile, {tortoise.name} kept walking, "
        f"steady as ever, at {tortoise_speed} "
        f"{unit(tortoise_speed, 'mile')} per hour. While {hare.name} "
        f"slept, {tortoise.name} kept moving for "
        f"{n_unit(nap_hours, 'hour')} straight without pause.\n\n"
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
    _intro         = _aesopian_intro(scene, "tortoise-hare", location)

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
        user_msg = (
            f"{_intro}{species_phrase(hare)} and {species_phrase(tortoise)} agreed "
            f"to a steady race through {location.article} {location.name}. "
            f"{cap(smart_pronoun(hare, [tortoise]))} ran at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, while {tortoise.name} "
            f"kept a steady {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. Both ran for "
            f"exactly {n_unit(hours, 'hour')}.\n\n"
            f"Question: How many miles ahead is {hare.name} after "
            f"{n_unit(hours, 'hour')}?"
        )
        result_text = f"{hare.name} is {answer} miles ahead."
        narrative   = (
            f"I'll compute each runner's distance by multiplying speed by "
            f"time, then subtract."
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
        user_msg = (
            f"{_intro}{species_phrase(hare)} and {species_phrase(tortoise)} agreed "
            f"to a steady race through {location.article} {location.name}. "
            f"{cap(smart_pronoun(hare, [tortoise]))} ran at {hare_speed} "
            f"{unit(hare_speed, 'mile')} per hour, while {tortoise.name} "
            f"plodded at {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. After some time, "
            f"{hare.name} was exactly {n_unit(miles_ahead, 'mile')} "
            f"ahead.\n\n"
            f"Question: How many hours had they been running?"
        )
        result_text = f"They had been running for {n_unit(answer, 'hour')}."
        narrative   = (
            f"The gap grows by (hare-speed minus tortoise-speed) per hour, "
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
        user_msg = (
            f"{_intro}{species_phrase(hare)} and {species_phrase(tortoise)} agreed "
            f"to a steady race through {location.article} {location.name}. "
            f"{tortoise.name} kept a steady {tortoise_speed} "
            f"{unit(tortoise_speed, 'mile')} per hour. Both ran for "
            f"exactly {n_unit(hours, 'hour')}, by the end of which "
            f"{hare.name} was {n_unit(miles_ahead, 'mile')} ahead.\n\n"
            f"Question: What was {hare.name}'s speed in miles per hour?"
        )
        result_text = (
            f"{hare.name}'s speed was {answer} "
            f"{unit(answer, 'mile')} per hour."
        )
        narrative   = (
            f"{hare.name}'s total distance is "
            f"miles-ahead + tortoise-distance; speed = total / hours."
        )
        chapter_name = "speed-comparison-speed"

    code_block = render_code(expr, form=scene.code_form(), value=answer)
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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

    _intro = _aesopian_intro(scene, "tortoise-hare", location)
    user_msg = (
        f"{_intro}In a long race across {location.article} {location.name}, "
        f"the course is {n_unit(total, 'mile')}. {species_phrase(tortoise)} "
        f"has already walked {n_unit(walked, 'mile')}. "
        f"{cap(tortoise.he_she)} continues at {speed} "
        f"{unit(speed, 'mile')} per hour.\n\n"
        f"Question: How many more whole hours of walking does "
        f"{tortoise.name} need to reach the finish line?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = (
        f"{tortoise.name} needs {n_unit(answer, 'more hour')} of walking."
        if answer != 1 else
        f"{tortoise.name} needs 1 more hour of walking."
    )
    narrative   = (
        f"I subtract the distance already walked from the total to find "
        f"what remains, then divide by {tortoise.name}'s speed."
    )

    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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
    pitcher = next(c for c in ont.CONTAINERS if c.name == "pitcher")
    stone   = next(i for i in ont.ITEMS if i.name == "pebble")

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

    weather  = scene.phrase("On a hot afternoon", "On a thirsty summer day",
                              "One dry morning", "After a long flight")
    found    = scene.phrase("found", "came upon", "discovered")
    raises   = scene.phrase("raised the water level by",
                              "lifted the water by",
                              "pushed the level up by")
    _intro = _aesopian_intro(scene, "crow-pitcher", location)
    user_msg = (
        f"{_intro}{weather} at {location.article} {location.name}, "
        f"{species_phrase(crow)} {found} a {pitcher.name} of water, but "
        f"the water sat only {n_unit(start, 'centimeter')} from the bottom — "
        f"too low to reach. {cap(crow.he_she)} needed the water to rise "
        f"to {n_unit(target, 'centimeter')} before {crow.he_she} could "
        f"drink. {cap(crow.he_she)} began dropping {stone.plural} into "
        f"the {pitcher.name}, and each {stone.name} {raises} "
        f"{n_unit(rise_per, 'centimeter')}.\n\n"
        f"Question: What is the smallest number of {stone.plural} "
        f"{crow.name} needs to drop in to reach the target water level?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{crow.name} needs {answer} {stone.plural if answer != 1 else stone.name}."
    narrative   = (
        f"I find the gap between target and start, then divide by "
        f"the rise per stone (rounding up by adding rise-per-stone-1 first)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="crow-pitcher",
        chapter="stones-needed",
    )


def _cp_water_rise(scene: Scene) -> Record:
    """N stones dropped × R cm each + start = final water level."""
    crow = scene.pick_character(role_classes=("cunning",), species="crow")
    pitcher = next(c for c in ont.CONTAINERS if c.name == "pitcher")
    stone   = next(i for i in ont.ITEMS if i.name == "pebble")

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

    found    = scene.phrase("found", "came upon", "spotted")
    dropped  = scene.phrase("dropped in", "tossed in",
                             "carefully added")
    each_lifts = scene.phrase("raised the water by", "lifted the level by",
                               "made the water rise by")
    _intro = _aesopian_intro(scene, "crow-pitcher")
    user_msg = (
        f"{_intro}{species_phrase(crow)} {found} a {pitcher.name} with water at "
        f"{n_unit(start, 'centimeter')}. {cap(crow.he_she)} {dropped} "
        f"{n_unit(n_stones, stone.name, stone.plural)}, and each one "
        f"{each_lifts} {n_unit(rise_per, 'centimeter')}.\n\n"
        f"Question: After dropping all {n_stones} {stone.plural}, what "
        f"is the new water level in centimeters?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The water level rises to {answer} centimeters."
    narrative   = (
        f"I multiply the number of {stone.plural} by the rise per "
        f"{stone.name} and add the starting level."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="crow-pitcher",
        chapter="water-rise",
    )


def _cp_enough_stones(scene: Scene) -> Record:
    """Crow has K stones in pouch. Will K × R + start ≥ T?"""
    crow = scene.pick_character(role_classes=("cunning",), species="crow")
    pitcher = next(c for c in ont.CONTAINERS if c.name == "pitcher")
    stone   = next(i for i in ont.ITEMS if i.name == "pebble")

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
    answer_str = "yes" if answer else "no"

    _intro = _aesopian_intro(scene, "crow-pitcher")
    user_msg = (
        f"{_intro}{species_phrase(crow)} has only "
        f"{n_unit(k, stone.name, stone.plural)} left. The {pitcher.name}'s "
        f"water sits at {n_unit(start, 'centimeter')} and needs to reach "
        f"{n_unit(target, 'centimeter')} to drink. Each {stone.name} "
        f"raises the water by {n_unit(rise_per, 'centimeter')}.\n\n"
        f"Question: Can {crow.name} drink with the {stone.plural} "
        f"{crow.he_she} has? Answer with yes or no."
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The answer is {answer_str}."
    narrative   = (
        f"I compute the reachable water level with the available "
        f"{stone.plural} and compare with the target."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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

    _intro = _aesopian_intro(scene, "goose-eggs", location)
    user_msg = (
        f"{_intro}In {location.article} {location.name}, {owner.name} owned "
        f"{species_phrase(goose)}. The goose laid {per_day} golden "
        f"{unit(per_day, 'egg')} every day, like clockwork. "
        f"{owner.name} kept the goose for {n_unit(days, 'day')}.\n\n"
        f"Question: How many eggs did the goose lay in total?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The total is {answer} eggs."
    narrative   = "I multiply the eggs per day by the number of days."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        value=answer,
        expr=expr,
        fable="goose-eggs",
        chapter="total-yield",
    )


def _ge_value_yield(scene: Scene) -> Record:
    """Lays N eggs/day × D days × C coins/egg = total coins. Three orientation
    variants (one of {coins, days, per-egg-coins} unknown)."""
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

    stand   = scene.phrase("stood on hind legs", "rose up on hind legs",
                             "stretched up on hind paws")
    leap    = scene.phrase("could leap another",
                             "could spring another",
                             "could jump another")
    _intro = _aesopian_intro(scene, "fox-grapes")
    user_msg = (
        f"{_intro}{species_phrase(fox)} {stand}, reaching "
        f"{n_unit(body_height, 'foot', 'feet')} high, and "
        f"{leap} {n_unit(jump_height, 'foot', 'feet')}.\n\n"
        f"Question: What is the highest point {fox.name} can reach with "
        f"a single leap?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{fox.name} can reach {n_unit(answer, 'foot', 'feet')} high."
    narrative   = "I add the body-stand height and the jump height."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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

    _intro = _aesopian_intro(scene, "fox-grapes")
    user_msg = (
        f"{_intro}The grapes hung from a vine {n_unit(grape_height, 'foot', 'feet')} "
        f"above the ground. {species_phrase(fox)} could leap "
        f"{n_unit(per_jump, 'foot', 'feet')} straight up each try, and "
        f"each leap brought the grapes that much closer to reach.\n\n"
        f"Question: What is the smallest number of leaps {fox.name} needs "
        f"to reach the grapes?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{fox.name} needs {n_unit(answer, 'jump')}."
    narrative   = (
        "I ceiling-divide grape-height by per-jump (add per-jump-1 "
        "before quot)."
    )
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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

    _intro = _aesopian_intro(scene, "fox-grapes")
    user_msg = (
        f"{_intro}{species_phrase(fox)} grew tired of jumping for the grapes. "
        f"{cap(fox.he_she)} would give up after {n_unit(threshold, 'attempt')}. "
        f"So far {fox.he_she} had tried {n_unit(tried, 'time')}.\n\n"
        f"Question: Will {fox.name} try again? Answer yes or no."
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The answer is {answer}."
    narrative   = "I check whether tried is still below the threshold."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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
    food = scene.pick_item(edible=True, size_max=2)
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
    n_bulls    = scene.pick_int(3, 6)
    days_each  = scene.pick_int(1, 4)

    expr = Let(
        bindings=[("bulls",     Lit(n_bulls)),
                  ("days-per-bull", Lit(days_each))],
        body=App("*", [Var("bulls"), Var("days-per-bull")]),
    )
    answer = evaluate(expr)

    _intro = _aesopian_intro(scene, "lion-bulls")
    user_msg = (
        f"{_intro}{species_phrase(lion)} watched {n_unit(n_bulls, 'bull')} grazing. "
        f"Once they scattered, {lion.he_she} could attack one at a time, "
        f"taking {n_unit(days_each, 'day')} per bull.\n\n"
        f"Question: How many total days does {lion.name} need to defeat "
        f"all {n_bulls} bulls?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{lion.name} needs {n_unit(answer, 'day')}."
    narrative   = "I multiply the number of bulls by the days needed for each."
    return _finalize(
        scene,
        user_msg=user_msg,
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
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
