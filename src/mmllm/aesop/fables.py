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
    emit_clojure, evaluate,
)
from mmllm.aesop.template import (
    Record, Scene,
    article, assemble_assistant_msg, cap, n_unit, render_code,
    render_tool_calls, species_phrase, the_subject_phrase, unit,
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
    location = scene.pick_location(tags_any=("nature",), indoor=False)

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

    user_msg = (
        f"Once upon a time, {species_phrase(hare)} challenged "
        f"{species_phrase(tortoise)} to a race through "
        f"{location.article} {location.name}. "
        f"{cap(hare.he_she)} bragged about being the fastest, "
        f"while {tortoise.he_she} just kept a steady pace.\n\n"
        f"After running {n_unit(hare_lead, 'mile')} ahead, {hare.name} "
        f"grew tired and decided to take a nap. Meanwhile, {tortoise.name} "
        f"kept walking at {tortoise_speed} {unit(tortoise_speed, 'mile')} "
        f"per hour. While {hare.name} slept, {tortoise.name} walked for "
        f"{n_unit(nap_hours, 'hour')} straight.\n\n"
        f"Question: After {tortoise.name}'s walk, who is in the lead?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"So {answer} is now in the lead."
    narrative   = (
        f"Let me figure out where {tortoise.name} is by multiplying "
        f"{tortoise.name}'s speed by the time spent walking, then comparing "
        f"with {hare.name}'s lead."
    )

    calls = _build_tool_calls(scene, primary={"winner": answer},
                              secondary_lookups=[("compare-positions",
                                                  {"a": hare_lead,
                                                   "b": tortoise_speed * nap_hours})])
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )

    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="tortoise-hare",
        chapter="nap-overtake",
    )


def _th_speed_comparison(scene: Scene) -> Record:
    """Both move steadily; over T hours, who's ahead?"""
    hare     = scene.pick_character(role_classes=("racer", "fast"))
    tortoise = scene.pick_character(role_classes=("racer", "slow"), not_=hare)
    location = scene.pick_location(tags_any=("nature",), indoor=False)

    hare_speed     = scene.pick_int(4, 10)
    tortoise_speed = scene.pick_int(1, 3)
    hours          = scene.pick_int(2, 6)

    expr = Let(
        bindings=[
            ("hare-speed",     Lit(hare_speed)),
            ("tortoise-speed", Lit(tortoise_speed)),
            ("hours",          Lit(hours)),
            ("hare-distance",     App("*", [Var("hare-speed"), Var("hours")])),
            ("tortoise-distance", App("*", [Var("tortoise-speed"), Var("hours")])),
        ],
        body=App("-", [Var("hare-distance"), Var("tortoise-distance")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(hare)} and {species_phrase(tortoise)} agreed to a "
        f"steady race across {location.article} {location.name}. "
        f"{cap(hare.he_she)} ran at {hare_speed} "
        f"{unit(hare_speed, 'mile')} per hour, while {tortoise.name} "
        f"plodded at {tortoise_speed} {unit(tortoise_speed, 'mile')} "
        f"per hour. They both ran for exactly {n_unit(hours, 'hour')}.\n\n"
        f"Question: How many miles ahead is {hare.name} after "
        f"{n_unit(hours, 'hour')}?"
    )

    code_block = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{hare.name} is {answer} miles ahead."
    narrative   = (
        f"I'll compute each runner's distance by multiplying speed by time, "
        f"then subtract."
    )
    calls = _build_tool_calls(scene, primary={"miles_ahead": answer})

    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="tortoise-hare",
        chapter="speed-comparison",
    )


def _th_distance_remaining(scene: Scene) -> Record:
    """How much further must the tortoise walk to finish?"""
    tortoise = scene.pick_character(role_classes=("racer", "slow"))
    hare     = scene.pick_character(role_classes=("racer", "fast"), not_=tortoise)
    location = scene.pick_location(tags_any=("nature",), indoor=False)

    total       = scene.pick_int(10, 25)
    walked      = scene.pick_int(2, total - 1)
    speed       = scene.pick_int(1, 3)

    expr = Let(
        bindings=[
            ("total",  Lit(total)),
            ("walked", Lit(walked)),
            ("speed",  Lit(speed)),
            ("remaining", App("-", [Var("total"), Var("walked")])),
        ],
        body=App("quot", [Var("remaining"), Var("speed")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"In a long race across {location.article} {location.name}, "
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

    calls = _build_tool_calls(scene, primary={"hours_remaining": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
            ("gap",            App("-", [Var("target-cm"), Var("start-cm")])),
        ],
        body=App("quot", [App("+", [Var("gap"),
                                     App("dec", [Var("rise-per-stone")])]),
                          Var("rise-per-stone")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"On a hot afternoon at {location.article} {location.name}, "
        f"{species_phrase(crow)} found a {pitcher.name} of water but the "
        f"water sat only {n_unit(start, 'centimeter')} from the bottom — "
        f"too low to reach. {cap(crow.he_she)} needed the water to rise "
        f"to {n_unit(target, 'centimeter')} before {crow.he_she} could "
        f"drink. {cap(crow.he_she)} started dropping {stone.plural} into "
        f"the {pitcher.name}, and each {stone.name} raised the water level "
        f"by {n_unit(rise_per, 'centimeter')}.\n\n"
        f"Question: What is the smallest number of {stone.plural} "
        f"{crow.name} needs to drop in to reach the target water level?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{crow.name} needs {answer} {stone.plural if answer != 1 else stone.name}."
    narrative   = (
        f"I find the gap between target and start, then divide by "
        f"the rise per stone (rounding up by adding rise-per-stone-1 first)."
    )
    calls = _build_tool_calls(scene, primary={"stones": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{species_phrase(crow)} found a {pitcher.name} with water at "
        f"{n_unit(start, 'centimeter')}. {cap(crow.he_she)} dropped in "
        f"{n_unit(n_stones, stone.name, stone.plural)}, and each one "
        f"raised the water by {n_unit(rise_per, 'centimeter')}.\n\n"
        f"Question: After dropping all {n_stones} {stone.plural}, what "
        f"is the new water level in centimeters?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The water level rises to {answer} centimeters."
    narrative   = (
        f"I multiply the number of {stone.plural} by the rise per "
        f"{stone.name} and add the starting level."
    )
    calls = _build_tool_calls(scene, primary={"water_level_cm": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
            ("k",         Lit(k)),
            ("rise-per",  Lit(rise_per)),
            ("start-cm",  Lit(start)),
            ("target-cm", Lit(target)),
            ("reachable", App("+", [Var("start-cm"),
                                     App("*", [Var("k"), Var("rise-per")])])),
        ],
        body=App(">=", [Var("reachable"), Var("target-cm")]),
    )
    answer = evaluate(expr)
    answer_str = "yes" if answer else "no"

    user_msg = (
        f"{species_phrase(crow)} has only "
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
    calls = _build_tool_calls(scene, primary={"can_drink": answer_str})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"In {location.article} {location.name}, {owner.name} owned "
        f"{species_phrase(goose)}. The goose laid {per_day} golden "
        f"{unit(per_day, 'egg')} every day, like clockwork. "
        f"{owner.name} kept the goose for {n_unit(days, 'day')}.\n\n"
        f"Question: How many eggs did the goose lay in total?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The total is {answer} eggs."
    narrative   = "I multiply the eggs per day by the number of days."
    calls = _build_tool_calls(scene, primary={"total_eggs": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="goose-eggs",
        chapter="total-yield",
    )


def _ge_value_yield(scene: Scene) -> Record:
    """Lays N eggs/day for D days, each worth C coins. Total coins?"""
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))
    location = scene.pick_location(tag="village")

    per_day  = scene.pick_int(1, 2)
    days     = scene.pick_int(7, 30)
    per_egg  = scene.pick_int(5, 50)

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
        f"{owner.name} owned {species_phrase(goose)} that laid {per_day} "
        f"golden {unit(per_day, 'egg')} per day. Each egg sold for "
        f"{n_unit(per_egg, 'coin')} at the market. After "
        f"{n_unit(days, 'day')}, {owner.name} took the eggs to "
        f"{location.article} {location.name} to sell.\n\n"
        f"Question: How many coins did {owner.name} earn in total?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{owner.name} earned {answer} coins."
    narrative   = (
        "I find total eggs first (per-day × days), then multiply by the "
        "per-egg coin value."
    )
    calls = _build_tool_calls(scene, primary={"total_coins": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="goose-eggs",
        chapter="value-yield",
    )


def _ge_compounded(scene: Scene) -> Record:
    """Daily yields, then sum across days using `reduce`."""
    goose = scene.pick_character(role="yielder", species="goose")
    owner = scene.pick_character(role_classes=("trader",))

    days = scene.pick_int(3, 7)
    yields = [scene.pick_int(1, 4) for _ in range(days)]

    expr = Let(
        bindings=[("daily-yields", Lit(list(yields)))],
        body=App("reduce",
                 [Fn(["a", "b"], App("+", [Var("a"), Var("b")])),
                  Lit(0),
                  Var("daily-yields")]),
    )
    answer = evaluate(expr)

    yields_str = ", ".join(str(y) for y in yields)
    user_msg = (
        f"{owner.name}'s {species_phrase(goose)} laid different numbers "
        f"of eggs each day for {n_unit(days, 'day')}: {yields_str}.\n\n"
        f"Question: How many eggs in total over the {n_unit(days, 'day')}?"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"The total is {answer} eggs."
    narrative   = (
        "I use reduce with + to sum the daily yields starting from 0."
    )
    calls = _build_tool_calls(scene, primary={"total_eggs": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
            ("total", App("reduce",
                          [Fn(["a", "b"], App("+", [Var("a"), Var("b")])),
                           Lit(0),
                           Var("daily-yields")])),
            ("days", App("count", [Var("daily-yields")])),
        ],
        body=App("quot", [Var("total"), Var("days")]),
    )
    answer = evaluate(expr)

    yields_str = ", ".join(str(y) for y in yields)
    user_msg = (
        f"{owner.name}'s {species_phrase(goose)} laid these eggs on "
        f"successive days: {yields_str}.\n\n"
        f"Question: What is the average (integer quotient) eggs per day?"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"The average is {answer} eggs per day."
    narrative   = (
        "I compute the total with reduce, divide by the count, taking "
        "integer quotient."
    )
    calls = _build_tool_calls(scene, primary={"avg_eggs_per_day": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
    boy   = scene.pick_character(role_classes=("liar", "shepherd"))
    n_villagers = scene.pick_int(3, 10)
    n_alarms    = scene.pick_int(2, 6)
    minutes_per = scene.pick_int(5, 20)

    expr = Let(
        bindings=[
            ("villagers", Lit(n_villagers)),
            ("alarms",    Lit(n_alarms)),
            ("each",      Lit(minutes_per)),
        ],
        body=App("*", [Var("villagers"), Var("alarms"), Var("each")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{boy.name} watched sheep on the hill. Bored, "
        f"{boy.he_she} cried 'Wolf!' {n_unit(n_alarms, 'time')} "
        f"falsely. Each time, {n_villagers} villagers ran from "
        f"the village to the field, taking {n_unit(minutes_per, 'minute')} "
        f"each.\n\n"
        f"Question: How many total minutes did the villagers waste "
        f"running to {n_unit(n_alarms, 'false alarm')}?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The villagers wasted {answer} minutes in total."
    narrative   = "I multiply villagers × alarms × minutes per trip."
    calls = _build_tool_calls(scene, primary={"total_minutes": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="boy-wolf",
        chapter="false-alarms",
    )


def _bw_sheep_eaten(scene: Scene) -> Record:
    """Real wolf comes; villagers don't believe; wolf eats S sheep."""
    boy = scene.pick_character(role_classes=("liar", "shepherd"))
    flock = scene.pick_int(20, 80)
    eaten = scene.pick_int(3, min(flock - 1, 15))

    expr = Let(
        bindings=[("flock", Lit(flock)), ("eaten", Lit(eaten))],
        body=App("-", [Var("flock"), Var("eaten")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{boy.name} had a flock of {n_unit(flock, 'sheep', 'sheep')}. "
        f"After many false alarms, a real wolf came and the villagers "
        f"did not believe {boy.him_her}. The wolf ate "
        f"{n_unit(eaten, 'sheep', 'sheep')}.\n\n"
        f"Question: How many sheep does {boy.name} have left?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{boy.name} has {answer} sheep left."
    narrative   = "I subtract the eaten sheep from the original flock."
    calls = _build_tool_calls(scene, primary={"sheep_remaining": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="boy-wolf",
        chapter="sheep-eaten",
    )


def _bw_trust_threshold(scene: Scene) -> Record:
    """Villagers stop coming after K false alarms. Will they come on alarm N?"""
    boy = scene.pick_character(role_classes=("liar", "shepherd"))
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

    user_msg = (
        f"The villagers in {boy.name}'s village stop responding to alarms "
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
    calls = _build_tool_calls(scene, primary={"villagers_come": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
    """Ant collects G grains/day for D days. Total grains?"""
    ant = scene.pick_character(role_classes=("saver",), species="ant")
    location = scene.pick_location(tags_any=("nature",), indoor=False)
    per_day = scene.pick_int(2, 8)
    days    = scene.pick_int(20, 90)

    expr = Let(
        bindings=[("per-day", Lit(per_day)), ("days", Lit(days))],
        body=App("*", [Var("per-day"), Var("days")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"Through the summer at {location.article} {location.name}, "
        f"{species_phrase(ant)} collected {per_day} "
        f"{unit(per_day, 'grain')} every day for {n_unit(days, 'day')}.\n\n"
        f"Question: How many grains did {ant.name} collect by the end "
        f"of summer?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{ant.name} collected {n_unit(answer, 'grain')}."
    narrative   = "I multiply the daily collection rate by the number of days."
    calls = _build_tool_calls(scene, primary={"total_grains": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="ant-grasshopper",
        chapter="summer-stockpile",
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

    user_msg = (
        f"{species_phrase(ant)} has {n_unit(stockpile, 'grain')} stored "
        f"for winter. {cap(ant.he_she)} eats {n_unit(per_day, 'grain')} "
        f"per day.\n\n"
        f"Question: For how many whole days will {ant.name}'s stockpile "
        f"last?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The stockpile lasts {n_unit(answer, 'day')}."
    narrative   = "I divide the stockpile by daily consumption (integer quotient)."
    calls = _build_tool_calls(scene, primary={"days_lasting": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"After {n_unit(days, 'day')} of winter, {species_phrase(ant)} "
        f"started with {n_unit(ant_stock, 'grain')} and ate "
        f"{ant_per_day} per day. Meanwhile {species_phrase(grasshopper)} "
        f"started with {n_unit(gh_stock, 'grain')} and ate {gh_per_day} "
        f"per day.\n\n"
        f"Question: How many grains does {ant.name} have left after "
        f"winter? (Use 0 if {ant.he_she} ran out.)"
    )

    code_block  = render_code(expr, form="inline", value=answer)
    result_text = f"{ant.name} has {answer} grains left."
    narrative   = (
        f"I compute leftover for {ant.name} (initial - days × rate), then "
        "clamp to 0 if negative using max."
    )
    calls = _build_tool_calls(scene, primary={"ant_grains_left": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{maid.name} carried a pail of milk to market and dreamed of "
        f"the future. She would buy {n_unit(eggs, 'egg')}; each would "
        f"hatch into a hen; each hen would lay {n_unit(eggs_per_hen_per_year, 'egg')} "
        f"per year; each egg would sell for {n_unit(coins_per_egg, 'coin')}.\n\n"
        f"Question: If everything went perfectly, how many coins would "
        f"{maid.name} earn after one year?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{maid.name} would earn {n_unit(answer, 'coin')} in a year."
    narrative   = (
        "I multiply eggs × eggs-per-hen-per-year × coins-per-egg "
        "to get the total."
    )
    calls = _build_tool_calls(scene, primary={"total_coins": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{maid.name} bought a cow for {n_unit(cow_cost, 'coin')}. The "
        f"cow gives {n_unit(cups_per_day, 'cup')} of milk per day, and "
        f"each cup sells for {n_unit(coin_per_cup, 'coin')}.\n\n"
        f"Question: How many whole days until {maid.name} recovers the "
        f"cost of the cow? (Round up.)"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"It takes {n_unit(answer, 'day')} to break even."
    narrative   = (
        "I find daily revenue (cups × coin-per-cup), then ceiling-divide "
        "the cow's cost by that revenue."
    )
    calls = _build_tool_calls(scene, primary={"days_to_break_even": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{maid.name} carried a pail with {n_unit(full_cups, 'cup')} "
        f"of milk. She tripped and spilled {n_unit(spilled, 'cup')}. "
        f"Each cup of milk would have sold for "
        f"{n_unit(per_cup, 'coin')}.\n\n"
        f"Question: How many coins did {maid.name} lose by spilling?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{maid.name} lost {n_unit(answer, 'coin')}."
    narrative   = "I multiply the spilled cups by the price per cup."
    calls = _build_tool_calls(scene, primary={"coins_lost": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
                                species="fox")
    body_height = scene.pick_int(2, 4)
    jump_height = scene.pick_int(1, 4)

    expr = Let(
        bindings=[("body-height", Lit(body_height)),
                  ("jump-height", Lit(jump_height))],
        body=App("+", [Var("body-height"), Var("jump-height")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(fox)} stood on hind legs, reaching "
        f"{n_unit(body_height, 'foot', 'feet')} high, and could leap "
        f"another {n_unit(jump_height, 'foot', 'feet')}.\n\n"
        f"Question: What is the highest point {fox.name} can reach with "
        f"a single leap?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{fox.name} can reach {n_unit(answer, 'foot', 'feet')} high."
    narrative   = "I add the body-stand height and the jump height."
    calls = _build_tool_calls(scene, primary={"max_reach_feet": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="fox-grapes",
        chapter="max-reach",
    )


def _fg_jumps_needed(scene: Scene) -> Record:
    """Each jump goes up J feet. Grapes are G feet. Min jumps to reach grapes
    (assume re-stack progress; hypothetical/dream scenario)."""
    fox = scene.pick_character(role_classes=("cunning", "hungry"),
                                species="fox")
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

    user_msg = (
        f"{species_phrase(fox)} dreamed of climbing a magical tree where "
        f"each jump lifted {fox.him_her} {n_unit(per_jump, 'foot', 'feet')} "
        f"higher. The grapes hung at {n_unit(grape_height, 'foot', 'feet')}.\n\n"
        f"Question: What is the smallest number of jumps to reach the grapes?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{fox.name} needs {n_unit(answer, 'jump')}."
    narrative   = (
        "I ceiling-divide grape-height by per-jump (add per-jump-1 "
        "before quot)."
    )
    calls = _build_tool_calls(scene, primary={"jumps": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="fox-grapes",
        chapter="jumps-needed",
    )


def _fg_give_up(scene: Scene) -> Record:
    """Fox gives up after K attempts. Has tried T already. Will fox try again?"""
    fox = scene.pick_character(role_classes=("cunning", "hungry"),
                                species="fox")
    threshold = scene.pick_int(3, 8)
    tried     = scene.pick_int(0, 10)

    expr = Let(
        bindings=[("threshold", Lit(threshold)),
                  ("tried",     Lit(tried))],
        body=If(App("<", [Var("tried"), Var("threshold")]),
                Lit("yes"), Lit("no")),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(fox)} grew tired of jumping for the grapes. "
        f"{cap(fox.he_she)} would give up after {n_unit(threshold, 'attempt')}. "
        f"So far {fox.he_she} had tried {n_unit(tried, 'time')}.\n\n"
        f"Question: Will {fox.name} try again? Answer yes or no."
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The answer is {answer}."
    narrative   = "I check whether tried is still below the threshold."
    calls = _build_tool_calls(scene, primary={"try_again": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{species_phrase(country)} of the countryside had "
        f"{n_unit(a, food.name, food.plural)}, while "
        f"{species_phrase(city)} of the city had "
        f"{n_unit(b, food.name, food.plural)}.\n\n"
        f"Question: What is the absolute difference in {food.plural} "
        f"between the two mice?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"The difference is {n_unit(answer, food.name, food.plural)}."
    narrative   = "I take the absolute value of the difference."
    calls = _build_tool_calls(scene, primary={"difference": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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

    user_msg = (
        f"{species_phrase(country)} and {species_phrase(city)} hosted "
        f"a feast for {n_unit(n_mice, 'mouse', 'mice')} (counting "
        f"themselves). They had {n_unit(total, food.name, food.plural)} "
        f"to share equally.\n\n"
        f"Question: How many {food.plural} does each mouse get? "
        f"(Use integer division.)"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"Each mouse gets {n_unit(answer, food.name, food.plural)}."
    narrative   = "I integer-divide the total by the number of mice."
    calls = _build_tool_calls(scene, primary={"per_mouse": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
            ("start",  Lit(start)),
            ("travel", Lit(travel)),
            ("food",   Lit(food)),
        ],
        body=App("-", [Var("start"), Var("travel"), Var("food")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(mouse)} began the journey with "
        f"{n_unit(start, 'coin')}. {cap(mouse.he_she)} spent "
        f"{n_unit(travel, 'coin')} on travel and {n_unit(food, 'coin')} "
        f"on food.\n\n"
        f"Question: How many coins does {mouse.name} have left?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{mouse.name} has {n_unit(answer, 'coin')} remaining."
    narrative   = "I subtract travel and food from the starting coins."
    calls = _build_tool_calls(scene, primary={"coins_remaining": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
    dog = scene.pick_character(role_classes=("everyman",), species="dog")
    bones = scene.pick_int(2, 8)

    expr = Let(
        bindings=[("bones", Lit(bones))],
        body=App("dec", [Var("bones")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(dog)} crossed a stream carrying "
        f"{n_unit(bones, 'bone')}. Looking down, {dog.he_she} saw "
        f"{dog.his_her} reflection and thought it was another dog with "
        f"more bones. {cap(dog.he_she)} dropped one bone to grab the "
        f"shadow's, but the bone fell into the stream.\n\n"
        f"Question: How many bones does {dog.name} have now?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} has {n_unit(answer, 'bone')} left."
    narrative   = "I subtract 1 (the dropped bone) from the original count."
    calls = _build_tool_calls(scene, primary={"bones_remaining": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="dog-shadow",
        chapter="double-loss",
    )


def _ds_regret(scene: Scene) -> Record:
    """If dog hadn't dropped, would've had B. Now has B-1. Difference."""
    dog = scene.pick_character(role_classes=("everyman",), species="dog")
    expected_bones = scene.pick_int(3, 12)

    expr = Let(
        bindings=[("expected", Lit(expected_bones)),
                  ("actual",   App("dec", [Var("expected")]))],
        body=App("-", [Var("expected"), Var("actual")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(dog)} expected to bring home "
        f"{n_unit(expected_bones, 'bone')}, but lost one chasing a "
        f"shadow and ended up with one fewer.\n\n"
        f"Question: How many bones did {dog.name} fall short by, "
        f"compared to what {dog.he_she} expected?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} fell short by {n_unit(answer, 'bone')}."
    narrative   = "I compute expected-actual where actual is expected-1."
    calls = _build_tool_calls(scene, primary={"shortfall": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="dog-shadow",
        chapter="regret",
    )


def _ds_exchange_loss(scene: Scene) -> Record:
    """Dog had B bones. Trader offered N bones for M of dog's. Dog accepted but
    trader cheated — gave only K. Net change?"""
    dog    = scene.pick_character(role_classes=("everyman",), species="dog")
    trader = scene.pick_character(role_classes=("trader",))
    start  = scene.pick_int(5, 15)
    given  = scene.pick_int(2, start - 1)
    received = scene.pick_int(0, given - 1)  # cheated: less than given

    expr = Let(
        bindings=[("start",    Lit(start)),
                  ("given",    Lit(given)),
                  ("received", Lit(received))],
        body=App("+", [App("-", [Var("start"), Var("given")]),
                       Var("received")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(dog)} had {n_unit(start, 'bone')}. {trader.name} "
        f"offered to trade — {dog.name} would give {n_unit(given, 'bone')} "
        f"in exchange for some larger ones. But the trader cheated and "
        f"only gave back {n_unit(received, 'bone')}.\n\n"
        f"Question: How many bones does {dog.name} have after the trade?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{dog.name} ends with {n_unit(answer, 'bone')}."
    narrative   = "I subtract given, then add received back to the start."
    calls = _build_tool_calls(scene, primary={"final_bones": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
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
    lion = scene.pick_character(role_classes=("predator",), species="lion")
    n_bulls    = scene.pick_int(3, 6)
    days_each  = scene.pick_int(1, 4)

    expr = Let(
        bindings=[("bulls",     Lit(n_bulls)),
                  ("days-each", Lit(days_each))],
        body=App("*", [Var("bulls"), Var("days-each")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(lion)} watched {n_unit(n_bulls, 'bull')} grazing. "
        f"Once they scattered, {lion.he_she} could attack one at a time, "
        f"taking {n_unit(days_each, 'day')} per bull.\n\n"
        f"Question: How many total days does {lion.name} need to defeat "
        f"all {n_bulls} bulls?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{lion.name} needs {n_unit(answer, 'day')}."
    narrative   = "I multiply the number of bulls by the days needed for each."
    calls = _build_tool_calls(scene, primary={"total_days": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="lion-bulls",
        chapter="days-to-defeat",
    )


def _lb_remaining_after_k(scene: Scene) -> Record:
    """N bulls, K already defeated. Remaining?"""
    lion = scene.pick_character(role_classes=("predator",), species="lion")
    n_bulls = scene.pick_int(3, 8)
    defeated = scene.pick_int(0, n_bulls)

    expr = Let(
        bindings=[("bulls",    Lit(n_bulls)),
                  ("defeated", Lit(defeated))],
        body=App("-", [Var("bulls"), Var("defeated")]),
    )
    answer = evaluate(expr)

    user_msg = (
        f"{species_phrase(lion)} faced {n_unit(n_bulls, 'bull')} grazing "
        f"alone in the field. After several days, {lion.he_she} had "
        f"defeated {n_unit(defeated, 'of them', 'of them')}.\n\n"
        f"Question: How many bulls remain?"
    )

    code_block  = render_code(expr, form=scene.code_form(), value=answer)
    result_text = f"{n_unit(answer, 'bull')} remain."
    narrative   = "I subtract the defeated from the original count."
    calls = _build_tool_calls(scene, primary={"bulls_remaining": answer})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="lion-bulls",
        chapter="remaining-after-k",
    )


def _lb_divide_conquer_bool(scene: Scene) -> Record:
    """Lion needs S strength to defeat all bulls together. Has L. Together
    bulls > L. Alone, bulls have B each (B*N == total). Can lion defeat
    them one at a time?"""
    lion = scene.pick_character(role_classes=("predator",), species="lion")
    lion_strength = scene.pick_int(5, 15)
    n_bulls       = scene.pick_int(3, 5)
    bull_strength = scene.pick_int(2, lion_strength)  # individually beatable

    expr = Let(
        bindings=[
            ("lion-strength",  Lit(lion_strength)),
            ("bulls",          Lit(n_bulls)),
            ("bull-strength",  Lit(bull_strength)),
            ("together",       App("*", [Var("bulls"), Var("bull-strength")])),
        ],
        body=And_clauses(  # workaround: 'and' is not a special form in our AST
            App(">", [Var("lion-strength"), Var("bull-strength")]),
            App("<", [Var("lion-strength"), Var("together")]),
        ),
    )
    answer = evaluate(expr)
    answer_str = "yes" if answer else "no"

    user_msg = (
        f"{species_phrase(lion)} has strength {lion_strength}. Each of "
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
    calls = _build_tool_calls(scene, primary={"divide_required": answer_str})
    asst = assemble_assistant_msg(
        preface_style=scene.preface_style(),
        narrative=narrative,
        code_block=code_block,
        result_text=result_text,
        tool_call_line=render_tool_calls(calls),
    )
    return Record(
        system_msg="You are a friendly tutor. Solve story problems with Clojure code, then answer with a tool call.",
        user_msg=user_msg,
        assistant_msg=asst,
        tool_calls=calls,
        expected=answer,
        code_str=emit_clojure(expr),
        fable="lion-bulls",
        chapter="divide-conquer-bool",
    )


def And_clauses(*clauses):
    """Helper: emit `(and a b ...)` as App."""
    return App("and", list(clauses))


# ─────────────────────── tool-call helpers ───────────────────────


def _build_tool_calls(scene: Scene, *,
                      primary: dict,
                      secondary_lookups: list[tuple[str, dict]] | None = None
                      ) -> list[dict]:
    """Build a tool_calls list. Single-call most of the time; multi-call
    occasionally, with the primary 'answer' call always last."""
    n = scene.n_tool_calls()
    if n == 1 or not secondary_lookups:
        return [{"name": "answer", "args": primary}]
    # Multi-call: precede the answer with 1-2 lookup-style helper calls.
    calls = []
    for k, args in (secondary_lookups[: n - 1] if secondary_lookups else []):
        calls.append({"name": k, "args": args})
    calls.append({"name": "answer", "args": primary})
    return calls


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
        # Verify the tool call answer matches the eval result.
        last_call = rec.tool_calls[-1]
        assert last_call["name"] == "answer"
        # Simple sanity: the answer value appears somewhere in the tool call args.
        assert any(_eq_relaxed(v, rec.expected) for v in last_call["args"].values()), (
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
