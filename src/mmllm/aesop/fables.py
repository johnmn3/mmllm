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
    "tortoise-hare": gen_tortoise_hare,
    "crow-pitcher":  gen_crow_pitcher,
    "goose-eggs":    gen_goose_eggs,
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
