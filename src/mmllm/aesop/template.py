"""Template binding state + record shape for capstone fables.

Each fable is a Python function `(scene: Scene) -> Record`. The fable
body uses Scene's typed helpers to pick consistent entities (characters
with the right roles, items that fit in chosen containers, etc.), builds
an Expr tree representing the math, evaluates it for the ground-truth
answer, and renders narrative text around the code.

This is "DSL" only in the sense that Scene's API enforces the constraints.
There's no parser — Python's syntax is the host language.

Diversity knobs live on the Record / fable side: each fable function
flips coins to choose code form (inline vs block), preface style
(no-preface / fixed-short / NL-narrative), single-call vs multi-tool-call.
"""
from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass, field
from typing import Iterable

from mmllm.aesop import ontology as ont
from mmllm.aesop.expr  import Expr, evaluate, emit_clojure


# ─────────────────────── Record ───────────────────────


@dataclass
class Record:
    """One generated training record. After verifier passes, gets serialized
    via ChatTemplate into the byte-bin training corpus."""
    system_msg:    str
    user_msg:      str
    assistant_msg: str               # full assistant turn body (narrative + code + result_text + tool_call_json)
    tool_calls:    list[dict]        # canonical: [{"name": "...", "args": {...}}]
    expected:      object             # ground-truth answer for verifier
    code_str:      str               # the Clojure source as embedded
    fable:         str               # which fable generated it (for stats)
    chapter:       str               # which chapter / variant


# ─────────────────────── Scene ───────────────────────


@dataclass
class Scene:
    """Binding state for one generated record. Owns the RNG so generation
    is reproducible per seed."""
    rng:      random.Random
    bindings: dict[str, object] = field(default_factory=dict)
    used_names: set[str] = field(default_factory=set)

    # ─── character picking ───
    def pick_character(self, *,
                       role:          str | None = None,
                       role_classes:  Iterable[str] = (),
                       species:       str | None = None,
                       species_in:    Iterable[str] | None = None,
                       gender:        str | None = None,
                       not_:          ont.Character | Iterable[ont.Character] | None = None,
                       ) -> ont.Character:
        """Pick a character matching constraints. Already-used names are
        excluded automatically (so two main characters never collide)."""
        candidates = list(ont.CHARACTERS)
        if role:
            candidates = [c for c in candidates if role in c.role_classes]
        rs = list(role_classes)
        if rs:
            candidates = [c for c in candidates
                          if all(r in c.role_classes for r in rs)]
        if species:
            candidates = [c for c in candidates if c.species == species]
        if species_in:
            sset = set(species_in)
            candidates = [c for c in candidates if c.species in sset]
        if gender:
            candidates = [c for c in candidates if c.gender == gender]
        # Exclude already-used names (avoid Alice == Alice).
        excludes: set[str] = set(self.used_names)
        if not_ is not None:
            if isinstance(not_, ont.Character):
                excludes.add(not_.name)
            else:
                for x in not_:
                    excludes.add(x.name)
        candidates = [c for c in candidates if c.name not in excludes]
        if not candidates:
            raise ValueError(
                f"no character matches: role={role} role_classes={list(role_classes)}"
                f" species={species} species_in={species_in} gender={gender}"
                f" excludes={excludes}"
            )
        c = self.rng.choice(candidates)
        self.used_names.add(c.name)
        return c

    # ─── item picking ───
    def pick_item(self, *,
                  size:        int | None = None,
                  size_max:    int | None = None,
                  size_in:     Iterable[int] | None = None,
                  edible:      bool | None = None,
                  countable:   bool | None = None,
                  tag:         str | None = None,
                  tags_any:    Iterable[str] | None = None,
                  not_:        ont.Item | Iterable[ont.Item] | None = None,
                  ) -> ont.Item:
        cs = list(ont.ITEMS)
        if size is not None:
            cs = [i for i in cs if i.size == size]
        if size_max is not None:
            cs = [i for i in cs if i.size <= size_max]
        if size_in is not None:
            ss = set(size_in)
            cs = [i for i in cs if i.size in ss]
        if edible is not None:
            cs = [i for i in cs if i.edible == edible]
        if countable is not None:
            cs = [i for i in cs if i.countable == countable]
        if tag is not None:
            cs = [i for i in cs if tag in i.tags]
        if tags_any:
            ts = set(tags_any)
            cs = [i for i in cs if ts & set(i.tags)]
        excludes: set[str] = set()
        if not_ is not None:
            if isinstance(not_, ont.Item):
                excludes.add(not_.name)
            else:
                for x in not_:
                    excludes.add(x.name)
        cs = [i for i in cs if i.name not in excludes]
        if not cs:
            raise ValueError(
                f"no item matches: size={size} size_max={size_max} "
                f"edible={edible} tag={tag} tags_any={tags_any}"
            )
        return self.rng.choice(cs)

    # ─── container picking ───
    def pick_container(self, *,
                       fits_for:    ont.Item | None = None,
                       qty:         int | None = None,
                       max_size_geq: int | None = None,
                       tag:         str | None = None,
                       tags_any:    Iterable[str] | None = None,
                       is_body_part: bool | None = None,
                       ) -> ont.Container:
        cs = list(ont.CONTAINERS)
        if fits_for is not None and qty is not None:
            cs = [c for c in cs if c.fits_count(fits_for, qty)]
        elif fits_for is not None:
            cs = [c for c in cs if c.max_size >= fits_for.size]
        if max_size_geq is not None:
            cs = [c for c in cs if c.max_size >= max_size_geq]
        if tag is not None:
            cs = [c for c in cs if tag in c.tags]
        if tags_any:
            ts = set(tags_any)
            cs = [c for c in cs if ts & set(c.tags)]
        if is_body_part is not None:
            cs = [c for c in cs if c.is_body_part == is_body_part]
        if not cs:
            raise ValueError(
                f"no container matches: fits_for={fits_for} qty={qty} "
                f"max_size_geq={max_size_geq} tag={tag}"
            )
        return self.rng.choice(cs)

    # ─── location picking ───
    def pick_location(self, *,
                      indoor: bool | None = None,
                      tag:    str | None = None,
                      tags_any: Iterable[str] | None = None) -> ont.Location:
        cs = list(ont.LOCATIONS)
        if indoor is not None:
            cs = [l for l in cs if l.indoor == indoor]
        if tag is not None:
            cs = [l for l in cs if tag in l.tags]
        if tags_any:
            ts = set(tags_any)
            cs = [l for l in cs if ts & set(l.tags)]
        if not cs:
            raise ValueError(f"no location matches: indoor={indoor} tag={tag}")
        return self.rng.choice(cs)

    # ─── numeric picking ───
    def pick_int(self, lo: int, hi: int) -> int:
        return self.rng.randint(lo, hi)

    def pick_choice(self, options: Iterable):
        opts = list(options)
        return self.rng.choice(opts)

    def coin(self, p: float = 0.5) -> bool:
        return self.rng.random() < p

    def scale_tier(self) -> str:
        """Pick a numerical scale tier — used by templates to scale
        their numbers across {tiny: 1-10, medium: 1-100, large: 1-1000}."""
        return self.rng.choices(
            ["tiny", "medium", "large"],
            weights=[0.4, 0.4, 0.2],
        )[0]

    def code_form(self) -> str:
        """'inline' or 'block'."""
        return "inline" if self.coin(0.6) else "block"

    def preface_style(self) -> str:
        """'none', 'fixed', or 'narrative'."""
        return self.rng.choices(
            ["none", "fixed", "narrative"],
            weights=[0.25, 0.4, 0.35],
        )[0]

    def n_tool_calls(self) -> int:
        """1 (most), 2, or 3 — multi-call probability lower than single."""
        return self.rng.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]


# ─────────────────────── prose helpers ───────────────────────


def article(word: str) -> str:
    """'a' or 'an' picked from `word`'s first phoneme."""
    return "an" if word and word[0].lower() in "aeiou" else "a"


def cap(s: str) -> str:
    return s[:1].upper() + s[1:] if s else s


def species_phrase(c: ont.Character) -> str:
    """`Whisker the hare`. Humans: just the name."""
    if c.species == "human":
        return c.name
    return f"{c.name} the {c.species}"


def the_subject_phrase(c: ont.Character) -> str:
    """`the hare` (animals) or `Bob` (humans). Used for in-paragraph
    subject reference where the name was already introduced."""
    if c.species == "human":
        return c.name
    return f"the {c.species}"


def maybe_plural(item: ont.Item, n: int) -> str:
    return item.plural if n != 1 else item.name


# ─────────────────────── render helpers ───────────────────────


def render_code(expr: Expr, *, form: str, value) -> str:
    """Render a Clojure expression block in either 'inline' or 'block' form.

    inline:
      ```clojure
      (let [a 3 b 2] (+ a b))
      ;=> 5
      ```

    block:
      ```clojure
      (def a 3)
      (def b 2)
      (+ a b)
      ;; a + b = 5
      ```
    """
    src = emit_clojure(expr)
    fence_open  = "```clojure\n"
    fence_close = "\n```"
    if form == "inline":
        return f"{fence_open}{src}\n;=> {_emit_lit(value)}{fence_close}"
    # block form: pull let bindings out as defs, body becomes the trailing form
    if hasattr(expr, "bindings") and hasattr(expr, "body"):
        from mmllm.aesop.expr import Let, Do
        if isinstance(expr, Let):
            lines = []
            for k, v in expr.bindings:
                lines.append(f"(def {k} {emit_clojure(v)})")
            body_src = emit_clojure(expr.body) if not isinstance(expr.body, list) \
                       else "\n".join(emit_clojure(e) for e in expr.body)
            lines.append(body_src)
            full = "\n".join(lines)
            return f"{fence_open}{full}\n;; => {_emit_lit(value)}{fence_close}"
    # Fallback: same as inline.
    return f"{fence_open}{src}\n;=> {_emit_lit(value)}{fence_close}"


def _emit_lit(v) -> str:
    """Render an answer-value as a Clojure literal for ;=> annotation."""
    if v is None:
        return "nil"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, str):
        esc = v.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{esc}"'
    if isinstance(v, list):
        return "[" + " ".join(_emit_lit(x) for x in v) + "]"
    return str(v)


def render_tool_calls(calls: list[dict]) -> str:
    """Single canonical line: `{"tool_calls":[...]}`."""
    return json.dumps({"tool_calls": calls}, ensure_ascii=False, separators=(",", ":"))


def assemble_assistant_msg(*,
                           preface_style: str,
                           narrative: str,
                           code_block: str,
                           result_text: str,
                           tool_call_line: str) -> str:
    """Compose the assistant turn body. Preface choice + result text +
    optional NL bridge + tool call. The tool call line ALWAYS ends the
    turn (the last `<|end|>` boundary the eval extractor looks at)."""
    parts = []
    if preface_style == "fixed":
        parts.append("Let me work this out.")
    elif preface_style == "narrative":
        parts.append(narrative)
    # 'none' adds nothing
    parts.append(code_block)
    if result_text:
        parts.append(result_text)
    parts.append(tool_call_line)
    return "\n\n".join(p for p in parts if p)


# ─────────────────────── Self-test ───────────────────────


def smoke_test() -> None:
    rng = random.Random(0)
    s = Scene(rng=rng)

    hare = s.pick_character(role_classes=("racer", "fast"))
    assert "fast" in hare.role_classes
    tortoise = s.pick_character(role_classes=("racer", "slow"), not_=hare)
    assert tortoise.name != hare.name

    item = s.pick_item(size_max=2, edible=True)
    assert item.size <= 2 and item.edible
    container = s.pick_container(fits_for=item, qty=5)
    assert container.fits_count(item, 5)

    n = s.pick_int(3, 8)
    assert 3 <= n <= 8

    # rendering helpers
    assert article("apple") == "an"
    assert article("ball")  == "a"
    assert species_phrase(hare).startswith(hare.name)
    print(
        f"template smoke OK: hare={hare.name} tortoise={tortoise.name} "
        f"item={item.name} container={container.name} n={n}"
    )


if __name__ == "__main__":
    smoke_test()
