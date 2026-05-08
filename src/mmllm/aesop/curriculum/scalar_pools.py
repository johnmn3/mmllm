"""Typed scalar pools for parametric curriculum forms.

Every Clojure form in the K-12 curriculum draws its scalars from one
of these pools at render time — there are no hardcoded scalars. Each
pool exposes:

  • `.draw(rng)`              random pick
  • `.draw_unique(rng, k)`    k distinct picks (where supported)
  • `.constrained(rng, pred)` repeat-draw until predicate fires
  • `.clojure_lit(value)`     render value as Clojure source

Pools are sized to ≥ 12 entries (most much larger) so per-example
multiplicity multiplies the variation budget by 10²–10⁴ over what
hardcoded forms produced.

Slot dependencies (e.g. `(quot a b)` requires `b != 0` AND `a % b == 0`
for clean integer division) are expressed via `Slot.depends_on` and
draw ordering in `draw_slots`.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable

from mmllm.aesop.expr import _emit_value


# ─────────────────────── core types ───────────────────────


class ConstraintFailure(Exception):
    """Raised when constrained_draw can't satisfy a predicate in N tries."""


@dataclass(frozen=True)
class ScalarPool:
    name:        str
    values:      tuple = ()         # static set
    sampler:     Callable[[random.Random], Any] | None = None
    is_advanced: bool = False

    def draw(self, rng: random.Random) -> Any:
        if self.sampler is not None:
            return self.sampler(rng)
        return rng.choice(self.values)

    def draw_unique(self, rng: random.Random, k: int) -> list:
        if self.sampler is not None:
            seen = set()
            out  = []
            for _ in range(k * 20):
                v = self.sampler(rng)
                key = _hashable(v)
                if key in seen:
                    continue
                seen.add(key)
                out.append(v)
                if len(out) == k:
                    return out
            raise ConstraintFailure(
                f"{self.name}: could not draw {k} unique in 20× budget")
        if k > len(self.values):
            raise ValueError(
                f"{self.name} has {len(self.values)} entries; can't draw {k}")
        return rng.sample(list(self.values), k)

    def constrained(self,
                    rng: random.Random,
                    predicate: Callable[[Any], bool],
                    max_tries: int = 80) -> Any:
        for _ in range(max_tries):
            v = self.draw(rng)
            if predicate(v):
                return v
        raise ConstraintFailure(
            f"{self.name}: predicate unsatisfied in {max_tries} tries")

    def clojure_lit(self, value: Any) -> str:
        # Use expr.py's emitter so collections/keywords/maps render
        # exactly as the evaluator expects.
        if isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
            return f":{value[1]}"
        if isinstance(value, str) and value.startswith(":"):
            return value
        return _emit_value(value)

    def prose(self, value: Any) -> str:
        """English rendering for narrative slots."""
        if isinstance(value, list):
            if len(value) == 0:    return "an empty list"
            if len(value) == 1:    return str(value[0])
            if len(value) == 2:    return f"{value[0]} and {value[1]}"
            return ", ".join(str(v) for v in value[:-1]) + f", and {value[-1]}"
        if isinstance(value, str) and value.startswith(":"):
            return value[1:]   # ":apple" → "apple"
        return str(value)


def _hashable(v: Any):
    if isinstance(v, list):
        return ("__list__", tuple(_hashable(x) for x in v))
    if isinstance(v, dict):
        return ("__dict__", tuple(sorted(
            (k, _hashable(x)) for k, x in v.items())))
    return v


# ─────────────────────── slots & draw ───────────────────────


@dataclass(frozen=True)
class Slot:
    """One parametric slot in a form template.

    `pool` may be a pool name (string) or a ScalarPool. `constraint`
    is `lambda value, draws: bool`. `depends_on` lists slot names
    that must be drawn before this slot (so the constraint can
    reference them).
    """
    pool:       str | ScalarPool
    constraint: Callable[[Any, dict], bool] | None = None
    depends_on: tuple = ()


def draw_slots(slots: dict[str, Slot | str],
               rng: random.Random,
               *,
               max_tries: int = 80) -> dict[str, Any]:
    """Draw all slots, respecting dependencies.

    Slot values may be either a Slot object or a pool name (sugar for
    `Slot(pool=name)`). Returns `{slot_name: drawn_value}`.
    """
    normalized: dict[str, Slot] = {
        k: (v if isinstance(v, Slot) else Slot(pool=v))
        for k, v in slots.items()
    }
    order = _topo(normalized)
    draws: dict[str, Any] = {}
    for sname in order:
        slot = normalized[sname]
        pool = slot.pool if isinstance(slot.pool, ScalarPool) else POOLS[slot.pool]
        if slot.constraint is None:
            draws[sname] = pool.draw(rng)
        else:
            for _ in range(max_tries):
                v = pool.draw(rng)
                if slot.constraint(v, draws):
                    draws[sname] = v
                    break
            else:
                raise ConstraintFailure(
                    f"slot {sname!r}: predicate unsatisfied in {max_tries} tries")
    return draws


def _topo(slots: dict[str, Slot]) -> list[str]:
    pending = dict(slots)
    out     = []
    while pending:
        ready = [k for k, s in pending.items()
                 if all(d in out for d in s.depends_on)]
        if not ready:
            raise ValueError(f"slot dependency cycle: {list(pending)}")
        ready.sort()  # determinism
        for k in ready:
            out.append(k)
            del pending[k]
    return out


# ─────────────────────── numeric pools ───────────────────────


INT_TINY = ScalarPool(
    "INT_TINY",
    values=tuple(range(0, 10)))                # 0..9     (10)

INT_SMALL = ScalarPool(
    "INT_SMALL",
    values=tuple(range(1, 21)))                # 1..20    (20)

INT_SMALL_NZ = ScalarPool(
    "INT_SMALL_NZ",
    values=tuple(v for v in range(-20, 21) if v != 0))   # -20..20 ex 0  (40)

INT_MEDIUM = ScalarPool(
    "INT_MEDIUM",
    values=tuple(range(21, 100)))              # 21..99   (79)

INT_LARGE = ScalarPool(
    "INT_LARGE",
    values=tuple(range(100, 1000, 7))[:80],    # sampled  (80)
    is_advanced=True)

INT_BIGINT = ScalarPool(
    "INT_BIGINT",
    values=(
        1_000_000, 1_048_576, 2_000_000, 5_000_000, 10_000_000,
        16_777_216, 100_000_000, 1_000_000_000, 2_147_483_647,
        9_999_999_999, 100_000_000_000, 1_000_000_000_000,
        2 ** 40, 2 ** 50, 2 ** 53, 9_223_372_036_854_775_807,
    ),
    is_advanced=True)

INT_NEG = ScalarPool(
    "INT_NEG",
    values=tuple(range(-99, 0)))               # -99..-1  (99)

# Ratios as (num, den) tuples. Renderer emits "num/den" Clojure ratio
# literal. Reduced (gcd=1) so they don't simplify under eval.
def _ratio_pool() -> tuple:
    from math import gcd
    out = []
    for d in range(2, 13):
        for n in range(1, d):
            if gcd(n, d) == 1:
                out.append((n, d))
    return tuple(out)
RATIO = ScalarPool("RATIO", values=_ratio_pool())   # ~46

# Override clojure_lit for ratios.
def _ratio_lit(self, value):
    if isinstance(value, tuple) and len(value) == 2:
        return f"{value[0]}/{value[1]}"
    return _emit_value(value)
RATIO.__class__.clojure_lit  # keep base method; ratios use Slot.pool wrapper
# (Actually subclass below for ratio clarity.)


@dataclass(frozen=True)
class RatioPool(ScalarPool):
    def clojure_lit(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return f"{value[0]}/{value[1]}"
        return super().clojure_lit(value)
    def prose(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return f"{value[0]}/{value[1]}"
        return super().prose(value)

RATIO = RatioPool("RATIO", values=_ratio_pool())


BOOL = ScalarPool("BOOL", values=(True, False))


# ─────────────────────── character / string pools ───────────────────────


@dataclass(frozen=True)
class _CharPool(ScalarPool):
    """ScalarPool that renders single-char values as Clojure char
    literals (`\\h`, `\\space`) instead of strings (`"h"`). Used by
    G1-08 character subjects so the form_template `{a}` renders as
    `\\h` not `"h"` — preventing the STRING_AS_CHAR_MISCLAIM papercut
    where the prose's 'the character \\X' idiom contradicts the form's
    rendered string."""
    def clojure_lit(self, value: Any) -> str:
        if value == " ":   return "\\space"
        if value == "\n":  return "\\newline"
        if value == "\t":  return "\\tab"
        if value == "\r":  return "\\return"
        return "\\" + value

    def prose(self, value: Any) -> str:
        if value == " ":   return "\\space"
        if value == "\n":  return "\\newline"
        if value == "\t":  return "\\tab"
        if value == "\r":  return "\\return"
        return "\\" + value


CHAR_LOWER = _CharPool(
    "CHAR_LOWER",
    values=tuple(chr(c) for c in range(ord('a'), ord('z') + 1)))

CHAR_UPPER = _CharPool(
    "CHAR_UPPER",
    values=tuple(chr(c) for c in range(ord('A'), ord('Z') + 1)))


# Short strings — semantic categories so prose stays coherent.
STR_GREETING = ScalarPool(
    "STR_GREETING",
    values=("hello", "hi", "ahoy", "greetings", "salutations",
            "howdy", "hey", "yo", "welcome", "good morning",
            "good day", "good evening", "well met", "hail",
            "cheers", "bonjour", "konnichiwa", "namaste"))   # 18

STR_SHORT = ScalarPool(
    "STR_SHORT",
    values=("apple", "river", "stone", "candle", "feather",
            "thread", "harbor", "willow", "ember", "bridge",
            "cobalt", "linen", "marble", "pebble", "amber",
            "cedar", "pewter", "saffron", "garnet", "indigo",
            "lichen", "thistle", "myrrh", "auburn", "ochre",
            "topaz", "coral", "raven", "alder", "myrtle"))   # 30


# ─────────────────────── keyword pools ───────────────────────


def _kw(*xs):
    """Wrap as Clojure-keyword sentinels — `("__kw__", name)` tuples
    so they round-trip through the evaluator and emit as `:name` in
    both top-level and nested (dict-key, vector-element) positions."""
    return tuple(("__kw__", x) for x in xs)


KW_FRUIT = ScalarPool(
    "KW_FRUIT",
    values=_kw("apple", "pear", "plum", "fig", "grape", "berry",
               "cherry", "peach", "apricot", "quince", "lemon",
               "lime", "orange", "mango", "papaya", "guava",
               "lychee", "persimmon", "kiwi", "currant",
               "elderberry", "raspberry", "blackberry", "blueberry",
               "strawberry", "pomegranate", "tangerine", "mandarin",
               "nectarine", "kumquat"))   # 30

KW_ANIMAL = ScalarPool(
    "KW_ANIMAL",
    values=_kw("wolf", "crow", "fox", "hare", "tortoise", "owl",
               "stag", "doe", "lark", "mouse", "badger", "raven",
               "lynx", "ibex", "marten", "weasel", "otter", "vole",
               "hedgehog", "salamander", "newt", "toad", "skylark",
               "wren", "thrush", "jay", "magpie", "kestrel",
               "kingfisher", "heron"))   # 30

KW_COLOR = ScalarPool(
    "KW_COLOR",
    values=_kw("red", "ochre", "umber", "saffron", "indigo", "viridian",
               "sienna", "vermilion", "ultramarine", "carmine",
               "verdant", "russet", "scarlet", "crimson", "amber",
               "ivory", "ebony", "azure", "cerulean", "magenta",
               "chartreuse", "violet", "lavender", "lilac", "rose",
               "fuchsia", "teal", "cyan", "tangerine", "mahogany"))  # 30

KW_TOOL = ScalarPool(
    "KW_TOOL",
    values=_kw("pail", "sieve", "ladle", "trowel", "shears", "hoe",
               "rake", "spade", "scythe", "anvil", "bellows", "tongs",
               "hammer", "chisel", "auger", "adze", "mallet", "pestle",
               "mortar", "loom", "shuttle", "spindle", "distaff",
               "harrow", "winnow", "flail", "sickle", "plow", "yoke",
               "harness"))  # 30

KW_GENERIC = ScalarPool(
    "KW_GENERIC",
    values=_kw("a", "b", "c", "x", "y", "z", "alpha", "beta", "gamma",
               "delta", "first", "second", "third", "left", "right",
               "north", "south", "east", "west", "near", "far",
               "high", "low", "fast", "slow", "warm", "cool",
               "soft", "hard", "open"))  # 30


KW_BY_THEME = {
    "fruit":   KW_FRUIT,
    "animal":  KW_ANIMAL,
    "color":   KW_COLOR,
    "tool":    KW_TOOL,
    "generic": KW_GENERIC,
}


# ─────────────────────── collection pools ───────────────────────


def _coll_int_sampler(lo, hi, k_min, k_max):
    def sample(rng: random.Random):
        k = rng.randint(k_min, k_max)
        return [rng.randint(lo, hi) for _ in range(k)]
    return sample


COLL_INT_SHORT = ScalarPool(
    "COLL_INT_SHORT",
    sampler=_coll_int_sampler(1, 20, 3, 5))

COLL_INT_MED = ScalarPool(
    "COLL_INT_MED",
    sampler=_coll_int_sampler(1, 50, 5, 8))

COLL_INT_LONG = ScalarPool(
    "COLL_INT_LONG",
    sampler=_coll_int_sampler(1, 100, 8, 14),
    is_advanced=True)


def _coll_int_unique(lo, hi, k):
    def sample(rng: random.Random):
        return rng.sample(range(lo, hi + 1), k)
    return sample


COLL_INT_UNIQUE_SHORT = ScalarPool(
    "COLL_INT_UNIQUE_SHORT",
    sampler=_coll_int_unique(1, 30, 4))

COLL_INT_UNIQUE_MED = ScalarPool(
    "COLL_INT_UNIQUE_MED",
    sampler=_coll_int_unique(1, 50, 6))


def _coll_kw_sampler(theme: str, k_min: int, k_max: int):
    pool = KW_BY_THEME[theme]
    def sample(rng: random.Random):
        k = rng.randint(k_min, k_max)
        return rng.sample(pool.values, k)
    return sample


COLL_KW_FRUIT_SHORT = ScalarPool(
    "COLL_KW_FRUIT_SHORT",
    sampler=_coll_kw_sampler("fruit", 3, 5))

COLL_KW_ANIMAL_SHORT = ScalarPool(
    "COLL_KW_ANIMAL_SHORT",
    sampler=_coll_kw_sampler("animal", 3, 5))

COLL_KW_COLOR_SHORT = ScalarPool(
    "COLL_KW_COLOR_SHORT",
    sampler=_coll_kw_sampler("color", 3, 5))


# ─────────────────────── map pools ───────────────────────


def _map_kw_int_sampler(theme: str, k_min: int, k_max: int,
                        v_lo: int = 1, v_hi: int = 20):
    pool = KW_BY_THEME[theme]
    def sample(rng: random.Random):
        k = rng.randint(k_min, k_max)
        keys = rng.sample(pool.values, k)
        return {kk: rng.randint(v_lo, v_hi) for kk in keys}
    return sample


MAP_FRUIT_INT  = ScalarPool("MAP_FRUIT_INT",
                            sampler=_map_kw_int_sampler("fruit", 2, 4))
MAP_ANIMAL_INT = ScalarPool("MAP_ANIMAL_INT",
                            sampler=_map_kw_int_sampler("animal", 2, 4))
MAP_TOOL_INT   = ScalarPool("MAP_TOOL_INT",
                            sampler=_map_kw_int_sampler("tool", 2, 4))


# ─────────────────────── registry ───────────────────────


POOLS: dict[str, ScalarPool] = {
    p.name: p for p in [
        INT_TINY, INT_SMALL, INT_SMALL_NZ, INT_MEDIUM, INT_LARGE,
        INT_BIGINT, INT_NEG, RATIO, BOOL,
        CHAR_LOWER, CHAR_UPPER, STR_GREETING, STR_SHORT,
        KW_FRUIT, KW_ANIMAL, KW_COLOR, KW_TOOL, KW_GENERIC,
        COLL_INT_SHORT, COLL_INT_MED, COLL_INT_LONG,
        COLL_INT_UNIQUE_SHORT, COLL_INT_UNIQUE_MED,
        COLL_KW_FRUIT_SHORT, COLL_KW_ANIMAL_SHORT, COLL_KW_COLOR_SHORT,
        MAP_FRUIT_INT, MAP_ANIMAL_INT, MAP_TOOL_INT,
    ]
}


# ─────────────────────── form rendering ───────────────────────


def render_form(template: str,
                slots: dict[str, Slot | str],
                rng: random.Random) -> tuple[str, dict[str, Any]]:
    """Render a parametric form template.

    Returns (rendered_form_source, draws_dict).
      • rendered_form_source: Clojure source with all `{slot}` replaced
        by their pool's `clojure_lit(value)` rendering
      • draws_dict: `{slot_name: raw_value}` for prose interpolation
        and ground-truth verification
    """
    draws = draw_slots(slots, rng)
    rendered = template
    for sname, value in draws.items():
        slot = slots[sname]
        pool = (slot.pool if isinstance(slot, Slot) and isinstance(slot.pool, ScalarPool)
                else POOLS[slot.pool if isinstance(slot, Slot) else slot])
        rendered = rendered.replace("{" + sname + "}", pool.clojure_lit(value))
    return rendered, draws


def render_prose(template: str, draws: dict[str, Any],
                 slots: dict[str, Slot | str] | None = None) -> str:
    """Substitute `{drawn.X}` tokens in narrative text with prose-rendered
    drawn values. Leaves all other `{...}` placeholders intact for the
    template's own format pass."""
    out = template
    for sname, value in draws.items():
        if slots:
            slot = slots[sname]
            pool = (slot.pool if isinstance(slot, Slot)
                    and isinstance(slot.pool, ScalarPool)
                    else POOLS[slot.pool if isinstance(slot, Slot) else slot])
            prose_val = pool.prose(value)
        else:
            prose_val = str(value)
        out = out.replace("{drawn." + sname + "}", prose_val)
    return out


# ─────────────────────── self-test ───────────────────────


def smoke_test() -> None:
    rng = random.Random(0)

    # Basic draw
    v = INT_SMALL.draw(rng)
    assert 1 <= v <= 20, v

    # Constrained draw
    v = INT_SMALL.constrained(rng, lambda x: x % 2 == 0)
    assert v % 2 == 0, v

    # Slots with dependency: clean integer division
    slots = {
        "b": Slot(pool="INT_SMALL", constraint=lambda v, d: v != 0),
        "a": Slot(pool="INT_MEDIUM",
                  constraint=lambda v, d: v % d["b"] == 0,
                  depends_on=("b",)),
    }
    draws = draw_slots(slots, rng)
    assert draws["a"] % draws["b"] == 0, draws

    # Ratio rendering
    src = RATIO.clojure_lit((1, 3))
    assert src == "1/3", src

    # Form rendering
    rendered, draws = render_form(
        "(+ {x} {y} {z})",
        {"x": "INT_SMALL", "y": "INT_SMALL", "z": "INT_SMALL"},
        rng)
    assert rendered.startswith("(+ "), rendered
    assert all(k in draws for k in ("x", "y", "z"))

    # Prose rendering with collection pool
    rng2 = random.Random(1)
    coll = COLL_INT_SHORT.draw(rng2)
    text = COLL_INT_SHORT.prose(coll)
    assert "and" in text or len(coll) <= 1, text

    print(f"scalar_pools.py smoke_test: ok ({len(POOLS)} pools)")


if __name__ == "__main__":
    smoke_test()
