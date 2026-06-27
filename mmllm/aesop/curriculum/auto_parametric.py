"""Auto-migrate legacy `_ex(form, expected, ...)` calls to parametric
form_template / slots / expected_fn.

Strategy: parse the form, identify every literal, replace each with a
typed slot drawn from the right scalar pool, then rebuild a template
string and an expected_fn that re-evaluates the form with each draw.

Usage:
    auto = auto_parametric_from_form("(+ 1 2 3)", expected=6)
    if auto:
        template, slots, expected_fn = auto
        # template:  "(+ {a} {b} {c})"
        # slots:     {"a": "INT_TINY", "b": "INT_TINY", "c": "INT_TINY"}
        # expected_fn(draws): re-evaluates the form with drawn values

Returns None if the form contains no literals (nothing to parametrize)
or fails to parse. In that case the caller keeps the legacy
form/expected pair.

For prose interpolation, `replace_literals_in_prose(prose, slot_map)`
does a textual substitution: each literal occurrence in the prose
that matches a drawn slot's original value is replaced with the
corresponding `{drawn.<slot>}` placeholder. Conservative: only
substitutes when the literal has exactly one occurrence in the prose
(low risk of false positives like "step 3" being mistaken for the
literal 3).
"""
from __future__ import annotations

import re
from typing import Any
from fractions import Fraction

from mmllm.aesop.curriculum.form_parser import parse, ParseError, UnsupportedForm
from mmllm.aesop.expr import (
    Expr, Lit, Var, App, If, When, Cond, Let, Fn, Do, Thread, Def, Try,
    evaluate, _emit_value,
)


# ─────────────────────── pool inference ───────────────────────


def _infer_pool(value: Any, *, is_char: bool = False) -> str:
    """Map a raw literal value to a typed pool name. Conservative
    defaults keep the value space tight for grade-appropriate ranges.

    `is_char=True` signals the literal came from a `\\X` Clojure char
    syntax (not `"X"` string), so it routes to a CHAR_* pool instead
    of STR_SHORT — preventing the STRING_AS_CHAR_MISCLAIM papercut
    where a single-char form_template draws a multi-character string
    while the prose still calls it 'the character \\X'."""
    if isinstance(value, bool):
        return "BOOL"
    if isinstance(value, int):
        if value == 0:                           return "INT_TINY"
        if 1 <= value <= 9:                      return "INT_TINY"
        if 1 <= value <= 20:                     return "INT_SMALL"
        if -99 <= value < 0:                     return "INT_NEG"
        if 21 <= value <= 99:                    return "INT_MEDIUM"
        if 100 <= value <= 999:                  return "INT_LARGE"
        return "INT_BIGINT"
    if isinstance(value, str):
        if is_char:
            if len(value) == 1 and value.isalpha() and value.isupper():
                return "CHAR_UPPER"
            return "CHAR_LOWER"
        return "STR_SHORT"
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
        # Disambiguate keyword theme by membership in known pools
        from mmllm.aesop.curriculum.scalar_pools import (
            KW_FRUIT, KW_ANIMAL, KW_COLOR, KW_TOOL, KW_GENERIC,
        )
        for pool, name in (
            (KW_FRUIT,   "KW_FRUIT"),
            (KW_ANIMAL,  "KW_ANIMAL"),
            (KW_COLOR,   "KW_COLOR"),
            (KW_TOOL,    "KW_TOOL"),
            (KW_GENERIC, "KW_GENERIC"),
        ):
            if value in pool.values:
                return name
        return "KW_GENERIC"  # fallback
    if isinstance(value, list):
        if all(isinstance(x, int) and not isinstance(x, bool) for x in value):
            return "COLL_INT_SHORT"
        # Keyword/string/sym lists — keep them homogeneous typed
        if all(isinstance(x, tuple) and len(x) == 2 and x[0] == "__kw__"
               for x in value):
            # Try to detect theme based on first element membership
            from mmllm.aesop.curriculum.scalar_pools import (
                KW_FRUIT, KW_ANIMAL, KW_COLOR, KW_TOOL,
            )
            for pool, coll_pool in (
                (KW_FRUIT,  "COLL_KW_FRUIT_SHORT"),
                (KW_ANIMAL, "COLL_KW_ANIMAL_SHORT"),
                (KW_COLOR,  "COLL_KW_COLOR_SHORT"),
            ):
                if value and value[0] in pool.values:
                    return coll_pool
            return "COLL_KW_FRUIT_SHORT"  # fallback theme
        # Mixed-type collection — too risky to parametrize; signal skip
        return ""
    if isinstance(value, dict):
        return "MAP_FRUIT_INT"  # rough fallback; rewriting common case
    return ""  # unrecognized — caller should fall back to legacy


# ─────────────────────── literal collection ───────────────────────


def _collect_literals(ast: Expr,
                      out: list,
                      *,
                      skip_in_set: bool = False) -> None:
    """Walk the AST collecting `(node, value, pool_name)` tuples for
    every literal that should become a slot. Skips literals that are
    structural (special-form keywords like `:else`, control-flow
    constants like `nil` for if-with-no-else)."""
    if isinstance(ast, Lit):
        v = ast.value
        # Skip structural literals
        if v is None:                              return
        if isinstance(v, bool):                    return  # bools usually structural
        # Skip set-element literals (collection-as-fn pattern)
        if skip_in_set:                            return
        if ast.is_kw:
            tagged = ("__kw__", v)
            pool = _infer_pool(tagged)
            if pool:
                out.append((ast, tagged, pool))
        else:
            pool = _infer_pool(v, is_char=getattr(ast, "is_char", False))
            if pool:
                out.append((ast, v, pool))
        return
    if isinstance(ast, Var):
        return
    if isinstance(ast, App):
        for a in ast.args:
            _collect_literals(a, out)
        return
    if isinstance(ast, If):
        _collect_literals(ast.cond, out)
        _collect_literals(ast.then, out)
        _collect_literals(ast.else_, out)
        return
    if isinstance(ast, When):
        _collect_literals(ast.cond, out)
        for b in ast.body: _collect_literals(b, out)
        return
    if isinstance(ast, Cond):
        for test, expr in ast.clauses:
            _collect_literals(test, out)
            _collect_literals(expr, out)
        _collect_literals(ast.default, out)
        return
    if isinstance(ast, Let):
        for nm, expr in ast.bindings:
            _collect_literals(expr, out)
        _collect_literals(ast.body, out)
        return
    if isinstance(ast, Fn):
        _collect_literals(ast.body, out)
        return
    if isinstance(ast, Def):
        _collect_literals(ast.body, out)
        return
    if isinstance(ast, Do):
        for b in ast.body: _collect_literals(b, out)
        return
    if isinstance(ast, Thread):
        _collect_literals(ast.init, out)
        for s in ast.steps: _collect_literals(s, out)
        return
    if isinstance(ast, Try):
        _collect_literals(ast.body, out)
        _collect_literals(ast.handler, out)
        return


# ─────────────────────── auto-parametric ───────────────────────


_NAMES = list("abcdefghijklmnopqrstuvwxyz")


# Forms whose AST contains any of these op names should NOT be
# auto-parametrized — they need bb pre-flight or are pedagogically
# fixed. The auto-parametric path returns None for these, leaving
# the caller in legacy mode (form_str + expected) until a manual
# bb-verify migration happens.
_HOST_INTEROP_OPS = frozenset((
    "meta", "with-meta", "vary-meta",
    "deftype", "defrecord", "defprotocol", "defmacro", "definterface",
    "extend-protocol", "extend-type", "extend",
    "atom", "swap!", "reset!", "ref", "ref-set", "alter",
    "agent", "send", "send-off",
    "thread", "future", "promise", "deliver", "deref",
    "go", "go-loop", "<!", ">!", "<!!", ">!!", "chan", "close!",
    "import", "use", "require", "ns", "in-ns",
    "loop", "recur",
    "macroexpand", "macroexpand-1",
    "*ns*", "find-ns", "create-ns",
    "bound?", "var", "var-get", "var-set",
))


_DIVISION_OPS = frozenset(("quot", "rem", "mod", "/"))


def _has_host_interop(ast: Expr) -> bool:
    """Detect whether the AST uses ops that need bb pre-flight."""
    if isinstance(ast, App):
        if ast.op in _HOST_INTEROP_OPS:
            return True
        # Detect host-interop method calls: ops starting with "."
        if ast.op.startswith(".") or ast.op.endswith("."):
            return True
        # clojure.* namespaced, but not clojure.string/* (which we support)
        if ast.op.startswith("clojure.") and not ast.op.startswith("clojure.string/"):
            return True
        for a in ast.args:
            if _has_host_interop(a):
                return True
    elif isinstance(ast, If):
        return any(_has_host_interop(x) for x in (ast.cond, ast.then, ast.else_))
    elif isinstance(ast, When):
        return _has_host_interop(ast.cond) or any(_has_host_interop(b) for b in ast.body)
    elif isinstance(ast, Cond):
        for t, e in ast.clauses:
            if _has_host_interop(t) or _has_host_interop(e): return True
        return _has_host_interop(ast.default)
    elif isinstance(ast, Let):
        for nm, e in ast.bindings:
            if _has_host_interop(e): return True
        return _has_host_interop(ast.body)
    elif isinstance(ast, Fn):
        return _has_host_interop(ast.body)
    elif isinstance(ast, Def):
        return _has_host_interop(ast.body)
    elif isinstance(ast, Do):
        return any(_has_host_interop(b) for b in ast.body)
    elif isinstance(ast, Thread):
        return _has_host_interop(ast.init) or any(_has_host_interop(s) for s in ast.steps)
    elif isinstance(ast, Try):
        return _has_host_interop(ast.body) or _has_host_interop(ast.handler)
    return False


def _find_nth_index_pairs(ast: Expr,
                          node_to_slot: dict,
                          value_to_slot: dict) -> list:
    """Find (index_slot_name, coll_value) pairs for `(nth coll i)` and
    `(get coll i)` (when i is an int)."""
    pairs = []
    if isinstance(ast, App):
        if ast.op in ("nth", "get") and len(ast.args) >= 2:
            coll, idx = ast.args[0], ast.args[1]
            idx_slot = node_to_slot.get(id(idx))
            if idx_slot is not None and isinstance(coll, Lit):
                coll_val = coll.value
                if isinstance(coll_val, list):
                    pairs.append((idx_slot, coll_val))
        for a in ast.args:
            pairs.extend(_find_nth_index_pairs(a, node_to_slot, value_to_slot))
    elif isinstance(ast, If):
        for x in (ast.cond, ast.then, ast.else_):
            pairs.extend(_find_nth_index_pairs(x, node_to_slot, value_to_slot))
    elif isinstance(ast, Let):
        for nm, e in ast.bindings:
            pairs.extend(_find_nth_index_pairs(e, node_to_slot, value_to_slot))
        pairs.extend(_find_nth_index_pairs(ast.body, node_to_slot, value_to_slot))
    elif isinstance(ast, Fn):
        pairs.extend(_find_nth_index_pairs(ast.body, node_to_slot, value_to_slot))
    elif isinstance(ast, Do):
        for b in ast.body:
            pairs.extend(_find_nth_index_pairs(b, node_to_slot, value_to_slot))
    elif isinstance(ast, Thread):
        pairs.extend(_find_nth_index_pairs(ast.init, node_to_slot, value_to_slot))
        for s in ast.steps:
            pairs.extend(_find_nth_index_pairs(s, node_to_slot, value_to_slot))
    return pairs


def _find_divisor_slots(ast: Expr,
                        node_to_slot: dict) -> set:
    """Return the set of slot names that appear as divisors in
    quot/rem/mod/divide ops. These slots need a non-zero constraint.

    Also detects nth's index argument vs collection length — we don't
    constrain it here (would require runtime knowledge of the coll
    size), but we'll use a different approach: cap the index to a
    small INT_TINY range, accepting some out-of-range failures and
    falling back via the verifier's re-roll logic.
    """
    out = set()
    if isinstance(ast, App):
        if ast.op in _DIVISION_OPS and len(ast.args) >= 2:
            divisor = ast.args[-1]  # last arg
            if id(divisor) in node_to_slot:
                out.add(node_to_slot[id(divisor)])
        for a in ast.args:
            out |= _find_divisor_slots(a, node_to_slot)
    elif isinstance(ast, If):
        for x in (ast.cond, ast.then, ast.else_):
            out |= _find_divisor_slots(x, node_to_slot)
    elif isinstance(ast, When):
        out |= _find_divisor_slots(ast.cond, node_to_slot)
        for b in ast.body:
            out |= _find_divisor_slots(b, node_to_slot)
    elif isinstance(ast, Cond):
        for t, e in ast.clauses:
            out |= _find_divisor_slots(t, node_to_slot)
            out |= _find_divisor_slots(e, node_to_slot)
        out |= _find_divisor_slots(ast.default, node_to_slot)
    elif isinstance(ast, Let):
        for nm, e in ast.bindings:
            out |= _find_divisor_slots(e, node_to_slot)
        out |= _find_divisor_slots(ast.body, node_to_slot)
    elif isinstance(ast, Fn):
        out |= _find_divisor_slots(ast.body, node_to_slot)
    elif isinstance(ast, Do):
        for b in ast.body:
            out |= _find_divisor_slots(b, node_to_slot)
    elif isinstance(ast, Thread):
        out |= _find_divisor_slots(ast.init, node_to_slot)
        for s in ast.steps:
            out |= _find_divisor_slots(s, node_to_slot)
    return out


def auto_parametric_from_form(
    form_str: str,
    expected: Any = None) -> tuple[str, dict, Any, dict] | None:
    """Build a parametric template from a literal-only legacy form.

    Returns (form_template, slots, expected_fn, value_to_slot) where
    `value_to_slot` maps each unique literal value to the slot name
    that drew it (used for prose interpolation).

    Returns None if the form has no literals to parametrize, or if
    parsing fails, or if the form uses host-interop / macro
    machinery that can't be safely auto-parametrized.
    """
    try:
        ast = parse(form_str)
    except (ParseError, UnsupportedForm):
        return None
    if _has_host_interop(ast):
        return None  # caller stays in legacy mode (use bb pre-flight)
    # Skip forms whose top-level value is a function (def/defn at root
    # without subsequent call). Function values can't be re-compared
    # across evaluations.
    if isinstance(ast, Def):
        return None
    literals: list = []
    _collect_literals(ast, literals)
    if not literals:
        return None

    # Group by value: literals with the same value share a slot.
    value_to_slot: dict = {}
    slot_assignments: list = []   # [(node, slot_name, pool_name)]
    next_idx = 0

    for node, value, pool in literals:
        key = _hashable_value(value)
        if key in value_to_slot:
            slot_name = value_to_slot[key]
        else:
            if next_idx >= len(_NAMES):
                # too many slots — abort, this form is too elaborate
                return None
            slot_name = _NAMES[next_idx]
            value_to_slot[key] = slot_name
            next_idx += 1
        slot_assignments.append((node, slot_name, pool))

    # Build slots dict. Use the FIRST seen pool for each slot name.
    slots: dict = {}
    for _, slot_name, pool in slot_assignments:
        slots.setdefault(slot_name, pool)

    # Build template by reconstructing the source with slot placeholders.
    # Strategy: re-emit the AST, but replace each literal node's emit
    # with `{slot_name}`.
    placeholder_map: dict = {id(node): name
                              for node, name, _ in slot_assignments}
    template = _emit_with_placeholders(ast, placeholder_map)

    # Divisor slots: any slot used as the divisor in quot/rem/mod/divide
    # must be constrained to non-zero so the form doesn't crash on
    # division-by-zero.
    divisor_slots = _find_divisor_slots(ast, placeholder_map)
    if divisor_slots:
        from mmllm.aesop.curriculum.scalar_pools import Slot
        for sname in divisor_slots:
            pool_name = slots[sname]
            # If the pool is INT_TINY (which contains 0), upgrade to
            # INT_SMALL_NZ which excludes 0 by construction. Otherwise
            # add a non-zero predicate.
            if pool_name == "INT_TINY":
                slots[sname] = "INT_SMALL_NZ"
            else:
                slots[sname] = Slot(
                    pool=pool_name,
                    constraint=lambda v, _: v != 0)

    # nth/get-by-index slots: the index argument must be < len(coll).
    # Auto-detect (nth coll i) where coll is a literal collection or a
    # collection-typed slot, and constrain i to its valid range.
    nth_pairs = _find_nth_index_pairs(ast, placeholder_map, value_to_slot)
    if nth_pairs:
        from mmllm.aesop.curriculum.scalar_pools import Slot
        for idx_slot, coll_value in nth_pairs:
            # If coll is a fixed literal, the index just needs <  len.
            if isinstance(coll_value, list):
                bound = len(coll_value)
                slots[idx_slot] = Slot(
                    pool="INT_TINY",
                    constraint=(lambda b: lambda v, _: 0 <= v < b)(bound))
            # If coll is also a slot, defer — too tangled. Skip.

    # Build expected_fn: substitute drawn values back into the
    # template, parse + evaluate.
    def expected_fn(draws: dict) -> Any:
        rendered = template
        for sname, value in draws.items():
            lit = _emit_value(value, is_kw=isinstance(value, tuple)
                              and len(value) == 2 and value[0] == "__kw__")
            if isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
                lit = f":{value[1]}"
            rendered = rendered.replace("{" + sname + "}", lit)
        return evaluate(parse(rendered))

    # Round-trip sanity: the expected_fn with the original literals
    # should match the authored expected.
    if expected is not None:
        original_draws = {name: _unkey(key)
                          for key, name in value_to_slot.items()}
        try:
            sanity = expected_fn(original_draws)
            if not _values_loosely_equal(sanity, expected):
                # Authored expected disagrees with evaluator. Skip.
                return None
        except Exception:
            return None

    return template, slots, expected_fn, value_to_slot


def _hashable_value(v: Any) -> Any:
    if isinstance(v, list):
        return ("__list__", tuple(_hashable_value(x) for x in v))
    if isinstance(v, dict):
        return ("__dict__", tuple(sorted(
            (_hashable_value(k), _hashable_value(x)) for k, x in v.items())))
    return v


def _unkey(key: Any) -> Any:
    if isinstance(key, tuple) and len(key) == 2:
        if key[0] == "__list__":
            return [_unkey(x) for x in key[1]]
        if key[0] == "__dict__":
            return {_unkey(k): _unkey(v) for k, v in key[1]}
    return key


def _values_loosely_equal(a: Any, b: Any) -> bool:
    """Tolerant equality used in the auto-migration sanity check."""
    if isinstance(a, str) and a.startswith(":"):
        a = ("__kw__", a[1:])
    if isinstance(b, str) and b.startswith(":"):
        b = ("__kw__", b[1:])
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(
            _values_loosely_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        an = {_norm_key(k): v for k, v in a.items()}
        bn = {_norm_key(k): v for k, v in b.items()}
        if set(an) != set(bn):  return False
        return all(_values_loosely_equal(an[k], bn[k]) for k in an)
    if isinstance(a, Fraction) and isinstance(b, str) and "/" in b:
        n, d = b.split("/")
        return a == Fraction(int(n), int(d))
    return a == b


def _norm_key(k):
    if isinstance(k, str) and k.startswith(":"):
        return ("__kw__", k[1:])
    return k


# ─────────────────────── emit with placeholders ───────────────────────


def _emit_with_placeholders(ast: Expr, placeholder_map: dict) -> str:
    """Emit Clojure source, but substitute `{slot}` for nodes whose
    id is in placeholder_map. Mirrors expr.py's emit but with a
    targeted override."""
    if id(ast) in placeholder_map:
        return "{" + placeholder_map[id(ast)] + "}"
    if isinstance(ast, Lit):
        return ast.emit()
    if isinstance(ast, Var):
        return ast.name
    if isinstance(ast, App):
        if not ast.args:
            return f"({ast.op})"
        body = " ".join(_emit_with_placeholders(a, placeholder_map)
                        for a in ast.args)
        return f"({ast.op} {body})"
    if isinstance(ast, If):
        c = _emit_with_placeholders(ast.cond,         placeholder_map)
        t = _emit_with_placeholders(ast.then,  placeholder_map)
        e = _emit_with_placeholders(ast.else_,  placeholder_map)
        return f"(if {c} {t} {e})"
    if isinstance(ast, When):
        c = _emit_with_placeholders(ast.cond, placeholder_map)
        body = " ".join(_emit_with_placeholders(b, placeholder_map)
                        for b in ast.body)
        return f"(when {c} {body})"
    if isinstance(ast, Cond):
        parts = []
        for test, expr in ast.clauses:
            parts.append(_emit_with_placeholders(test, placeholder_map))
            parts.append(_emit_with_placeholders(expr, placeholder_map))
        if ast.default is not None and not (
            isinstance(ast.default, Lit) and ast.default.value is None):
            parts.append(":else")
            parts.append(_emit_with_placeholders(ast.default, placeholder_map))
        return f"(cond {' '.join(parts)})"
    if isinstance(ast, Let):
        bs = []
        for nm, expr in ast.bindings:
            bs.append(nm)
            bs.append(_emit_with_placeholders(expr, placeholder_map))
        body = _emit_with_placeholders(ast.body, placeholder_map)
        return f"(let [{' '.join(bs)}] {body})"
    if isinstance(ast, Fn):
        params = " ".join(ast.params)
        body = _emit_with_placeholders(ast.body, placeholder_map)
        return f"(fn [{params}] {body})"
    if isinstance(ast, Def):
        body = _emit_with_placeholders(ast.body, placeholder_map)
        return f"(def {ast.name} {body})"
    if isinstance(ast, Do):
        body = " ".join(_emit_with_placeholders(b, placeholder_map)
                        for b in ast.body)
        return f"(do {body})"
    if isinstance(ast, Thread):
        init = _emit_with_placeholders(ast.init, placeholder_map)
        steps = " ".join(_emit_with_placeholders(s, placeholder_map)
                         for s in ast.steps)
        return f"({ast.style} {init} {steps})"
    if isinstance(ast, Try):
        body = _emit_with_placeholders(ast.body, placeholder_map)
        handler = _emit_with_placeholders(ast.handler, placeholder_map)
        return (f"(try {body} (catch Exception "
                f"{ast.binding} {handler}))")
    return ast.emit()


# ─────────────────────── prose interpolation ───────────────────────


def replace_literals_in_prose(prose: str,
                              value_to_slot: dict) -> str:
    """For each (value, slot_name) in value_to_slot, replace
    occurrences of the literal in prose with `{drawn.<slot>}`.

    Conservative: only replaces literals that appear EXACTLY ONCE in
    the prose, OR are surrounded by clear word/punctuation boundaries
    on every occurrence. Avoids replacing "3" inside "step 3" or
    "third" since those are unrelated mentions.
    """
    if not prose:
        return prose
    out = prose
    for key, slot_name in value_to_slot.items():
        value = _unkey(key)
        # Determine a string form for matching prose
        if isinstance(value, bool):
            patterns = [str(value).lower()]
        elif isinstance(value, int):
            patterns = [str(value)]
        elif isinstance(value, str) and not value.startswith(":"):
            patterns = [value, f'"{value}"']
        elif isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
            patterns = [f":{value[1]}", value[1]]
        elif value is None:
            patterns = ["nil"]
        else:
            continue   # complex (list/dict) — skip prose substitution
        for pat in patterns:
            # Only substitute if the pattern appears exactly once
            # (low risk of false-positive numeric collisions)
            count = len(list(re.finditer(re.escape(pat), out)))
            if count == 1:
                # Replace with word-boundary-aware regex when the pattern
                # is alphanumeric, else exact replace.
                if pat.replace("_", "").replace(":", "").isalnum():
                    out = re.sub(rf"\b{re.escape(pat)}\b",
                                 "{drawn." + slot_name + "}", out)
                else:
                    out = out.replace(pat, "{drawn." + slot_name + "}")
                break  # first matching pattern wins
    return out


# ─────────────────────── self-test ───────────────────────


def smoke_test() -> None:
    cases = [
        # (form, expected, expect_template_substring)
        ("42",                        42,    "{a}"),
        ("(+ 1 2 3)",                 6,     "(+ {a} {b} {c})"),
        ("(* 2 3 4)",                 24,    "(* {a} {b} {c})"),
        ('(let [x 5] (* x x))',       25,    "(let [x {a}] (* x x))"),
        ("(if (pos? 7) 1 -1)",        1,     "(if (pos? {a}) {b} {c})"),
        ("(map inc [1 2 3])",         [2, 3, 4], "(map inc {a})"),
    ]
    ok = 0
    for form, expected, expect_sub in cases:
        result = auto_parametric_from_form(form, expected)
        if result is None:
            raise AssertionError(f"auto-parametric failed: {form!r}")
        template, slots, expected_fn, value_to_slot = result
        if expect_sub not in template:
            raise AssertionError(
                f"{form!r}: expected {expect_sub!r} in template, got {template!r}")
        ok += 1

    # Prose interpolation
    prose = "the sum of 1, 2, and 3"
    v2s = {1: "a", 2: "b", 3: "c"}
    out = replace_literals_in_prose(prose, v2s)
    assert "{drawn.a}" in out and "{drawn.b}" in out and "{drawn.c}" in out, out

    print(f"auto_parametric.py smoke_test: ok ({ok} forms, prose ok)")


if __name__ == "__main__":
    smoke_test()
