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
(no-preface / fixed-short / NL-narrative), and tool-call pattern (single
`answer` call vs `eval`+`answer` chain).

Tool-call surface (universal across fables):
  answer(value)  — submit final answer; value is any Clojure-shaped JSON
                   value (literal numbers/strings/lists are themselves;
                   string-encoded forms get evaluated by the runtime).
  eval(form)     — evaluate a Clojure-source string and return result.
                   Used in compositional pattern: eval(form) → answer(value).

The system prompt declares this catalog on every record so that arg
names + tool names appear verbatim in the input — model never has to
guess template-internal keys.
"""
from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass, field
from typing import Any, Iterable

from mmllm.aesop import ontology as ont
from mmllm.aesop.expr  import Expr, evaluate, emit_clojure


# ─────────────────────── Tool catalog ───────────────────────


# Single-tool catalog (used for ~75% of records).
ANSWER_ONLY: tuple[dict, ...] = (
    {
        "name": "answer",
        "params": ({"name": "value", "type": "any"},),
        "description": "submit the final answer (literal value or "
                       "Clojure-source string that the runtime will eval)",
    },
)

# Two-tool catalog (used for ~25% of records, paired with eval+answer chain).
ANSWER_AND_EVAL: tuple[dict, ...] = (
    {
        "name": "eval",
        "params": ({"name": "form", "type": "string"},),
        "description": "evaluate a Clojure-source string and return the result",
    },
    {
        "name": "answer",
        "params": ({"name": "value", "type": "any"},),
        "description": "submit the final answer",
    },
)


def render_tool_catalog(catalog: tuple[dict, ...] | list[dict]) -> str:
    """Format a tool catalog as the bullet list that goes in the system
    prompt. Output is deterministic for a given catalog tuple."""
    lines = ["Available tools:"]
    for t in catalog:
        params = ", ".join(f"{p['name']}: {p['type']}" for p in t["params"])
        line = f"- {t['name']}({params})"
        if t.get("description"):
            line += f" — {t['description']}"
        lines.append(line)
    return "\n".join(lines)


def system_prompt(use_eval: bool = True) -> str:
    """Eval-first system prompt. When the user asks a question, the
    model writes a Clojure expression whose evaluation produces the
    answer, and submits it via the `eval` tool. `answer(value)` is
    reserved for simple yes/no/string verdicts that aren't naturally
    expressed as a form.

    `use_eval=False` falls back to the answer-only catalog — used for
    chapters whose natural output is a yes/no string answer.
    """
    if use_eval:
        return (
            "You are a tool-using assistant with access to a Clojure "
            "evaluator. When asked a question, write a Clojure expression "
            "whose evaluation gives the answer, and submit it via the "
            "`eval` tool. Use `answer(value)` only for yes/no or "
            "string verdicts that aren't naturally a form.\n\n"
            + render_tool_catalog(ANSWER_AND_EVAL)
        )
    return (
        "You are a tool-using assistant. Submit your final answer "
        "directly with `answer(value)`.\n\n"
        + render_tool_catalog(ANSWER_ONLY)
    )


def build_tool_calls(*,
                     value:        Any,
                     form_str:     str,
                     prefer_eval:  bool,
                     ) -> list[dict]:
    """Eval-first tool-call builder. Two patterns:

      - eval(form):  the standard pattern. The form is the Clojure
                     expression that, when evaluated, produces the
                     answer. Used for ~85%+ of records.
      - answer(value): the verdict pattern. Used when the natural answer
                       is a literal yes/no or a short string that the
                       chapter's narrative makes more sensible to submit
                       directly than to re-encode as a form.
    """
    if prefer_eval:
        return [{"name": "eval", "args": {"form": form_str}}]
    return [{"name": "answer", "args": {"value": value}}]


# ─────────────────────── Record ───────────────────────


@dataclass
class Record:
    """One generated training record. After verifier passes, gets serialized
    via ChatTemplate into the byte-bin training corpus."""
    system_msg:    str
    user_msg:      str
    assistant_msg: str               # full assistant turn body
    tool_calls:    list[dict]        # canonical: [{"name": "...", "args": {...}}]
    expected:      object             # ground-truth answer for verifier
    code_str:      str               # the Clojure source as embedded
    fable:         str               # which fable generated it (for stats)
    chapter:       str               # which chapter / variant
    catalog:       tuple[dict, ...]  # tool catalog declared in system_msg


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
        """'inline', 'block', or 'block-mixed'.

        - inline: full Let tree as one expression with Clojure-formatted
          bindings (the default, most common).
        - block: every Let binding pulled out as `(def ...)` lines
          followed by the body.
        - block-mixed: first 1-2 bindings as `(def ...)` (top-level
          definitions), remaining bindings inside an inner `let` —
          closer to idiomatic Clojure (defs for constants, let for
          local computation).
        """
        return self.rng.choices(
            ["inline", "block", "block-mixed"],
            weights=[0.55, 0.20, 0.25],
        )[0]

    def phrase(self, *options: str) -> str:
        """Pick one of the given phrasings. Used inside narratives to
        avoid template-formula feel:
            phrase(scene, "started off", "began", "first")
        Each call is independent — same context can produce different
        renderings across records."""
        return self.rng.choice(options)

    def preface_style(self) -> str:
        """'none', 'fixed', or 'narrative'."""
        return self.rng.choices(
            ["none", "fixed", "narrative"],
            weights=[0.25, 0.4, 0.35],
        )[0]

    def use_eval_chain(self) -> bool:
        """LEGACY (kept for any leftover callers). Eval-first design has
        deprecated this — use prefer_eval / answer-only chapters instead."""
        return self.coin(0.25)

    def show_reasoning(self) -> bool:
        """Should the assistant include a short plan-only preface before
        the tool call? About 50% of records have a one-sentence plan; the
        rest emit just the eval call."""
        return self.coin(0.5)


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


def verb_for(c: ont.Character, base: str) -> str:
    """Conjugate a verb for character `c`'s pronoun. 'eat' → 'eats' for
    he/she, but 'eat' (plural) for they/them. Same for 'walk', 'run',
    etc. Special-cases 'is' / 'has' irregulars."""
    if c.gender == "n":
        # they/them — plural agreement, base form
        if base == "is":   return "are"
        if base == "has":  return "have"
        if base == "was":  return "were"
        return base
    # he/she — third-person singular: append 's' or 'es'
    if base == "is":   return "is"
    if base == "has":  return "has"
    if base == "was":  return "was"
    if base.endswith(("s", "x", "z", "ch", "sh")):
        return base + "es"
    if base.endswith("y") and len(base) > 1 and base[-2] not in "aeiou":
        return base[:-1] + "ies"
    return base + "s"


def smart_pronoun(c: ont.Character, others: Iterable[ont.Character]) -> str:
    """If any character in `others` shares c's pronoun, return c.name to
    disambiguate. Otherwise return the pronoun. Avoids "He bragged while
    he plodded" two-male-character ambiguity."""
    for o in others:
        if o is c:
            continue
        if o.he_she == c.he_she:
            return c.name
    return c.he_she


def smart_possessive(c: ont.Character, others: Iterable[ont.Character]) -> str:
    """Like smart_pronoun but for `his`/`her`/`their`. If ambiguous,
    returns `<name>'s` instead."""
    for o in others:
        if o is c:
            continue
        if o.his_her == c.his_her:
            return f"{c.name}'s"
    return c.his_her


def maybe_plural(item: ont.Item, n: int) -> str:
    return item.plural if n != 1 else item.name


def unit(n: int, singular: str, plural: str | None = None) -> str:
    """`unit(1, 'mile') -> 'mile'`, `unit(3, 'mile') -> 'miles'`. For
    irregular plurals (e.g., 'foot' / 'feet'), pass plural explicitly."""
    if n == 1:
        return singular
    return plural if plural is not None else singular + "s"


def n_unit(n: int, singular: str, plural: str | None = None) -> str:
    """`n_unit(1, 'mile') -> '1 mile'`, `n_unit(3, 'mile') -> '3 miles'`."""
    return f"{n} {unit(n, singular, plural)}"


# ─────────────────────── narrative scaffolding ───────────────────────


def time_phrase(scene: "Scene") -> str:
    """Atmospheric time-of-day / season opener."""
    return scene.rng.choice((
        "One bright morning,", "Late one summer afternoon,",
        "Just before dawn,", "On a cold autumn day,",
        "As the sun was setting,", "Under a wide blue sky,",
        "On a quiet spring morning,", "On a windy day,",
        "One foggy morning,", "After a long night of rain,",
    ))


def place_phrase(scene: "Scene", location: ont.Location) -> str:
    """Short setting clause — uses location-appropriate prepositions.

    Different topographies take different prepositions in English:
      - hilltops: 'on / atop / near / at the edge of'
      - roads:    'on / along / near'
      - beaches:  'on / near / by'
      - farms:    'on / at / by / near'  — workspace location, not interior
      - others (meadow, forest, woods, garden, orchard, etc.):
                  'in / near / at the edge of / by'

    'across' is dropped from the default pool because it produces
    awkward verb-preposition pairings ('stopped across the forest')
    in subplot prose.
    """
    if location.indoor:
        prep = scene.rng.choice(("inside", "in", "deep inside"))
        return f"{prep} {location.article} {location.name}"

    name = location.name
    if name == "hilltop":
        prep = scene.rng.choice(("on", "atop", "near", "at the edge of"))
    elif name == "road":
        prep = scene.rng.choice(("on", "along", "near"))
    elif name == "beach":
        prep = scene.rng.choice(("on", "near", "by"))
    elif name == "river bank":
        prep = scene.rng.choice(("on", "near", "by", "along"))
    elif name == "farm":
        # Farms are work-spaces ("on the farm" is idiomatic), not interiors.
        prep = scene.rng.choice(("on", "at", "near", "by"))
    elif name in ("market", "village"):
        # Markets and villages are zones one is "at / in / near", not "on".
        # ("on the village" / "on the market" reads as standing-atop.)
        prep = scene.rng.choice(("at", "in", "near", "by"))
    else:
        prep = scene.rng.choice(("in", "near", "at the edge of", "by"))
    return f"{prep} {location.article} {name}"


def atmosphere(scene: "Scene", location: ont.Location) -> str:
    """One-sentence opening atmosphere — time + place + sensory detail.
    Use as the first sentence of a chapter narrative."""
    when = time_phrase(scene)
    where = place_phrase(scene, location)
    detail = scene.rng.choice((
        f"the air was still {where}",
        f"the wind moved softly {where}",
        f"all was quiet {where}",
        f"birds called overhead {where}",
        f"long shadows stretched {where}",
        f"sunlight filtered through the trees {where}",
        f"a gentle breeze moved {where}",
        f"the smell of wet earth hung {where}",
    ))
    return f"{when} {detail}."


def char_intro(scene: "Scene", c: ont.Character, role_hint: str = "") -> str:
    """One-sentence character introduction. Tries to capture flavor —
    species/role/manner — without dictating action."""
    if c.species == "human":
        if role_hint:
            return f"{c.name}, {role_hint}, was thinking carefully."
        manner = scene.rng.choice((
            "stepped along the path",
            "stopped to look around",
            "set out on errand",
            "walked under the open sky",
        ))
        return f"{c.name} {manner}."
    adj = scene.rng.choice((
        "clever", "patient", "thoughtful", "quick", "curious",
        "wary", "weary", "hungry", "watchful",
    ))
    return f"{adj.capitalize()} {c.name} the {c.species} was nearby."


def question_phrase(scene: "Scene", what: str) -> str:
    """Phrase the closing challenge. Half the time uses an explicit
    'write a Clojure form' framing, half the time uses a plain question
    — the model learns both map onto the same eval-call output."""
    if scene.coin(0.5):
        return f"Write a Clojure expression that computes {what}."
    return f"Question: {what}?"


# ─────────────────────── render helpers ───────────────────────


def render_code(expr: Expr, *, form: str, value) -> str:
    """Render a Clojure expression block in either 'inline' or 'block' form.

    Annotation is unified to `;=> N` (single semicolon, no leading space,
    space after `=>`) — canonical Clojure REPL style. Both inline and
    block use the same annotation; they differ in how the bindings are
    laid out."""
    src = emit_clojure(expr)
    fence_open  = "```clojure\n"
    fence_close = "\n```"

    if form == "inline":
        return f"{fence_open}{src}\n;=> {_emit_lit(value)}{fence_close}"

    from mmllm.aesop.expr import Let

    # block form: every binding pulled out as (def …) lines, body trails.
    if form == "block" and isinstance(expr, Let):
        lines = []
        for k, v in expr.bindings:
            lines.append(f"(def {k} {emit_clojure(v)})")
        body_src = (emit_clojure(expr.body) if not isinstance(expr.body, list)
                    else "\n".join(emit_clojure(e) for e in expr.body))
        lines.append(body_src)
        full = "\n".join(lines)
        return f"{fence_open}{full}\n;=> {_emit_lit(value)}{fence_close}"

    # block-mixed: first 1-2 bindings as top-level defs, rest in inner let.
    if form == "block-mixed" and isinstance(expr, Let) and len(expr.bindings) >= 3:
        # Pull leading literal-bindings as defs (only Lits — defs of
        # computed expressions tied to inner names look weird at top
        # level). Stop at the first non-literal binding.
        from mmllm.aesop.expr import Lit
        n_def = 0
        for k, v in expr.bindings:
            if isinstance(v, Lit):
                n_def += 1
            else:
                break
        n_def = max(1, min(n_def, 2))   # at least 1, at most 2
        if n_def == 0 or n_def == len(expr.bindings):
            # Nothing useful to split out — fall back to plain block.
            return render_code(expr, form="block", value=value)
        lines = []
        for k, v in expr.bindings[:n_def]:
            lines.append(f"(def {k} {emit_clojure(v)})")
        # Build inner Let with remaining bindings, same body
        inner = Let(bindings=expr.bindings[n_def:], body=expr.body)
        lines.append(emit_clojure(inner))
        full = "\n".join(lines)
        return f"{fence_open}{full}\n;=> {_emit_lit(value)}{fence_close}"

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
    """Single canonical line: `{"tool_calls":[...]}`. Compact JSON, no
    spaces after separators — matches what the eval extractor parses."""
    return json.dumps({"tool_calls": calls},
                      ensure_ascii=False, separators=(",", ":"))


# Plan-only prefaces (NEVER reveal the numeric answer). One of these
# may appear before the tool call when scene.show_reasoning() is true.
# The rest of each record carries the math purely inside the eval form.
GENERIC_PREFACES: tuple[str, ...] = (
    "Let me work that out.",
    "I'll express the answer as a Clojure form.",
    "Time to write the form.",
    "Let me compute that.",
    "Here's the calculation.",
)


def assemble_assistant_msg(*,
                           preface:        str,
                           tool_call_line: str) -> str:
    """Compose the assistant turn body — preface (optional) + tool call.

    Eval-first design: the form inside the eval call IS the work. We
    do NOT print a code block or a result-text line, because those leak
    the answer to the model during training. The tool call's `form`
    arg is the only place the math materializes; the runtime evaluating
    it is what produces the answer.
    """
    parts = []
    if preface:
        parts.append(preface)
    parts.append(tool_call_line)
    return "\n\n".join(p for p in parts if p)


def resolve_preface(scene: "Scene", plan: str) -> str:
    """Pick the preface text. Three modes:

      - empty (~50%): no preface; assistant emits just the tool call
      - plan-only (~25%): chapter-supplied plan describing how the
        computation is structured (NEVER the answer value)
      - generic (~25%): a generic 'Let me compute' style line from
        GENERIC_PREFACES

    The plan supplied by the chapter must be answer-free — describes
    *how* not *what*. Verifier enforces this for chapters that opt in
    via verify_no_answer_in_msg().
    """
    if not scene.show_reasoning():
        return ""
    if plan and scene.coin(0.55):
        return plan
    return scene.rng.choice(GENERIC_PREFACES)


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

    # tool catalog
    sp_eval = system_prompt(use_eval=True)
    assert "eval" in sp_eval and "answer" in sp_eval
    sp_no = system_prompt(use_eval=False)
    assert "eval(" not in sp_no and "answer" in sp_no

    calls_eval = build_tool_calls(value=15, form_str="(+ 7 8)", prefer_eval=True)
    assert calls_eval == [{"name": "eval", "args": {"form": "(+ 7 8)"}}]
    calls_ans = build_tool_calls(value="yes", form_str="(= 1 1)", prefer_eval=False)
    assert calls_ans == [{"name": "answer", "args": {"value": "yes"}}]

    # disambiguation
    bob   = next(c for c in ont.CHARACTERS if c.name == "Bob")
    alice = next(c for c in ont.CHARACTERS if c.name == "Alice")
    char  = next(c for c in ont.CHARACTERS if c.name == "Charlie")
    assert smart_pronoun(bob,   [alice]) == "he"     # different pronouns
    assert smart_pronoun(bob,   [char])  == "Bob"    # both 'he' → name
    assert smart_pronoun(alice, [bob])   == "she"    # different pronouns

    print(
        f"template smoke OK: hare={hare.name} tortoise={tortoise.name} "
        f"item={item.name} container={container.name} n={n}"
    )


if __name__ == "__main__":
    smoke_test()
