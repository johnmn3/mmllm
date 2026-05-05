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


def system_prompt(use_eval: bool) -> str:
    """Canonical system prompt declaring the tool catalog. Two variants:
    answer-only (most records) or answer+eval (when the assistant uses a
    real eval-then-answer chain)."""
    catalog = ANSWER_AND_EVAL if use_eval else ANSWER_ONLY
    return (
        "You are a tool-using assistant. Solve the problem with Clojure code, "
        "then submit your answer as a tool call.\n\n"
        + render_tool_catalog(catalog)
    )


def build_tool_calls(value: Any, code_str: str, *, use_eval: bool) -> list[dict]:
    """Build the tool-call list. Two patterns:

      Pattern A (single):  [{name: answer, args: {value}}]
      Pattern C (chain):   [{name: eval, args: {form}}, {name: answer, args: {value}}]

    Pattern B (form-as-answer-string) was rejected — JSON-native values
    handle literals cleanly; the form-string variant overlaps with
    pattern C and adds no signal.
    """
    if use_eval:
        return [
            {"name": "eval",   "args": {"form": code_str}},
            {"name": "answer", "args": {"value": value}},
        ]
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
        """Should this record emit eval(form) + answer(value), or just answer(value)?"""
        return self.coin(0.25)


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


# Synonym pool: short generic prefaces for the 'fixed' preface style.
# The 'narrative' style uses a chapter-specific explanation instead.
FIXED_PREFACES: tuple[str, ...] = (
    "Let me work this out.",
    "Let me solve this step by step.",
    "Here's how I'd compute it.",
    "Let me trace through the math.",
    "Working through this carefully.",
    "I'll figure this out.",
    "Time to compute the answer.",
    "Stepping through the calculation.",
    "Let me think through this.",
)


# Optional opener prefix glued in front of the chapter's result_text.
# Some entries are empty strings — about half the time the result reads
# straight without an opener. Keeps surface variation without rewriting
# the chapter's specific result phrasing.
RESULT_OPENERS: tuple[str, ...] = (
    "", "", "", "",                       # 4× blank → ~50% no-opener
    "So ", "Therefore, ", "Thus, ", "Then ", "After all that, ",
)


def assemble_assistant_msg(*,
                           preface:        str,
                           code_block:     str,
                           result_text:    str,
                           tool_call_line: str) -> str:
    """Compose the assistant turn body. The preface is already resolved
    by the caller (could be empty, a fixed-pool pick, or a chapter
    narrative). Tool call line is always last."""
    parts = []
    if preface:
        parts.append(preface)
    parts.append(code_block)
    if result_text:
        parts.append(result_text)
    parts.append(tool_call_line)
    return "\n\n".join(p for p in parts if p)


def resolve_preface(scene: "Scene", chapter_narrative: str) -> str:
    """Pick the preface text based on scene's preface_style choice:
      - 'none'      → empty
      - 'fixed'     → random pick from FIXED_PREFACES
      - 'narrative' → the chapter-specific narrative passed in
    """
    style = scene.preface_style()
    if style == "fixed":
        return scene.rng.choice(FIXED_PREFACES)
    if style == "narrative":
        return chapter_narrative
    return ""


def resolve_result_text(scene: "Scene", chapter_result: str) -> str:
    """Apply a random opener prefix; sometimes drop result entirely
    (15% of the time) so the JSON tool call carries the answer alone —
    teaches the model that result-text-before-tool-call is optional."""
    if not chapter_result:
        return ""
    if scene.coin(0.15):
        return ""
    opener = scene.rng.choice(RESULT_OPENERS)
    if opener and chapter_result and chapter_result[0].isupper() and opener[-1] == " ":
        # If we're prepending an opener, lowercase the first letter of
        # the result text (e.g., "After all that, the stockpile lasts
        # 21 days." instead of "After all that, The stockpile lasts…").
        return opener + chapter_result[0].lower() + chapter_result[1:]
    return opener + chapter_result


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

    calls_a = build_tool_calls(15, "(+ 7 8)", use_eval=False)
    assert calls_a == [{"name": "answer", "args": {"value": 15}}]
    calls_c = build_tool_calls(15, "(+ 7 8)", use_eval=True)
    assert calls_c[0]["name"] == "eval" and calls_c[1]["name"] == "answer"

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
