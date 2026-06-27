"""Clojure-subset AST + evaluator + source emitter.

Single source of truth for the math in capstone records. Every fable
template builds an Expr tree; the same tree gets:

  • EVALUATED in Python (ground-truth answer for the tool-call)
  • EMITTED as Clojure source (what the model sees in the assistant turn)

This rules out hallucinated arithmetic — if the template builds
`(App "+" [Lit(3), Lit(2)])`, the model trains on `(+ 3 2)` and the
tool-call answer is `5`. Both come from the same tree.

Supported subset (≈ Clojure core, what a small model should internalize):

  arithmetic       + - * / quot rem mod inc dec abs min max
  predicates       = < > <= >= not= zero? pos? neg? odd? even? empty?
  logic            and or not
  conditionals     (special forms) if when cond case
  bindings         (special forms) let fn def
  sequences        list vector range repeat take drop count first last
                   rest butlast conj into reverse sort distinct partition
  higher-order     map filter reduce comp partial juxt apply
  maps             hash-map get assoc dissoc keys vals merge contains?
  strings          str clojure.string/upper-case clojure.string/lower-case
                   clojure.string/join clojure.string/split
  threading        -> ->>  (sugar; desugared to plain App chains for both
                   eval and Clojure emit, with optional preserve_thread
                   flag if a template wants to actually emit -> in source)

Numeric type fidelity: we keep ints int and emit `5` not `5.0`. Division
always uses `quot` for integer division to keep results exact and
serializable as ints — the templates are responsible for picking
`/ vs quot vs rem vs mod` according to what the model should emit.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import Any, Callable


# ─────────────────────── AST ───────────────────────


@dataclass
class Expr:
    """Base for all AST nodes. Subclasses must implement eval + emit."""
    def eval(self, env: dict) -> Any:                 # noqa: A003 - shadow ok
        raise NotImplementedError(type(self).__name__)
    def emit(self, indent: int = 0) -> str:
        raise NotImplementedError(type(self).__name__)


@dataclass
class Lit(Expr):
    """Literal value: int, float, str, bool, None, keyword, vector, map, set."""
    value: Any
    is_kw: bool = False  # treat str as Clojure keyword (`:foo`)
    is_set: bool = False # treat list as Clojure set (`#{...}`)
    is_char: bool = False # str came from `\X` Clojure char literal (vs `"X"`)

    def eval(self, env: dict) -> Any:
        if self.is_kw:
            return ("__kw__", self.value)
        if self.is_set:
            return frozenset(_eval_v(v, env) for v in self.value)
        if isinstance(self.value, list):
            return [_eval_v(v, env) for v in self.value]
        if isinstance(self.value, dict):
            return {_eval_v(k, env): _eval_v(v, env)
                    for k, v in self.value.items()}
        return self.value

    def emit(self, indent: int = 0) -> str:
        return _emit_value(self.value, is_kw=self.is_kw, is_set=self.is_set)


@dataclass
class Var(Expr):
    """Variable reference. Also resolves to a Python callable wrapping
    the op-table when the name matches a known op — this lets
    `(reduce + xs)` and `(apply + xs)` work without registering each
    op as a closure in the env."""
    name: str
    def eval(self, env: dict) -> Any:
        if self.name in env:
            return env[self.name]
        op = OPS.get(self.name)
        if op is not None:
            # Wrap into the (args, env) → result calling convention.
            return lambda args, _env=env, _op=op: _op(list(args), _env)
        raise NameError(f"unbound symbol: {self.name}")
    def emit(self, indent: int = 0) -> str:
        return self.name


@dataclass
class App(Expr):
    """Function application: (op arg ...)."""
    op:   str
    args: list[Expr]
    inline: bool = True  # render single-line by default

    def eval(self, env: dict) -> Any:
        evaled = [a.eval(env) for a in self.args]
        f = OPS.get(self.op)
        if f is not None:
            return f(evaled, env)
        # Fall back to env-bound callables (defn / let-bound fn).
        if self.op in env:
            ef = env[self.op]
            if callable(ef):
                return ef(evaled)
        raise NameError(f"unknown op: {self.op}")

    def emit(self, indent: int = 0) -> str:
        if not self.args:
            return f"({self.op})"
        body = " ".join(a.emit(indent + 2) for a in self.args)
        if self.inline and "\n" not in body:
            return f"({self.op} {body})"
        # multi-line form: each arg on its own line
        sp   = " " * (indent + len(self.op) + 2)
        head = f"({self.op}"
        first, *rest = self.args
        first_s = first.emit(indent + len(self.op) + 2)
        out = head + " " + first_s
        for a in rest:
            out += "\n" + sp + a.emit(indent + len(self.op) + 2)
        return out + ")"


@dataclass
class If(Expr):
    cond:    Expr
    then:    Expr
    else_:   Expr

    def eval(self, env: dict) -> Any:
        c = self.cond.eval(env)
        return self.then.eval(env) if _truthy(c) else self.else_.eval(env)

    def emit(self, indent: int = 0) -> str:
        c = self.cond.emit(indent + 4)
        t = self.then.emit(indent + 4)
        e = self.else_.emit(indent + 4)
        line = f"(if {c} {t} {e})"
        if "\n" not in line and len(line) < 80:
            return line
        sp = " " * (indent + 4)
        return f"(if {c}\n{sp}{t}\n{sp}{e})"


@dataclass
class When(Expr):
    cond: Expr
    body: list[Expr]

    def eval(self, env: dict) -> Any:
        if not _truthy(self.cond.eval(env)):
            return None
        last = None
        for e in self.body:
            last = e.eval(env)
        return last

    def emit(self, indent: int = 0) -> str:
        c = self.cond.emit(indent + 6)
        body_strs = [e.emit(indent + 6) for e in self.body]
        line = f"(when {c} " + " ".join(body_strs) + ")"
        if "\n" not in line and len(line) < 80:
            return line
        sp = " " * (indent + 6)
        return f"(when {c}\n" + "\n".join(sp + b for b in body_strs) + ")"


@dataclass
class Cond(Expr):
    """(cond test1 result1 test2 result2 … :else default)."""
    clauses: list[tuple[Expr, Expr]]   # last clause's test is the literal :else by convention
    default: Expr | None = None

    def eval(self, env: dict) -> Any:
        for test, result in self.clauses:
            if _truthy(test.eval(env)):
                return result.eval(env)
        return None if self.default is None else self.default.eval(env)

    def emit(self, indent: int = 0) -> str:
        sp = " " * (indent + 6)
        out = "(cond"
        for test, result in self.clauses:
            out += f"\n{sp}{test.emit(indent + 6)} {result.emit(indent + 6)}"
        if self.default is not None:
            out += f"\n{sp}:else {self.default.emit(indent + 6)}"
        return out + ")"


@dataclass
class Let(Expr):
    bindings: list[tuple[str, Expr]]
    body:     Expr | list[Expr]

    def eval(self, env: dict) -> Any:
        new_env = dict(env)
        for k, v in self.bindings:
            new_env[k] = v.eval(new_env)
        if isinstance(self.body, list):
            last = None
            for e in self.body:
                last = e.eval(new_env)
            return last
        return self.body.eval(new_env)

    def emit(self, indent: int = 0) -> str:
        # vector of bindings, each on its own line if more than 1 pair
        if len(self.bindings) == 1:
            k, v = self.bindings[0]
            binds = f"[{k} {v.emit(indent + 6 + len(k))}]"
        else:
            sp_b = " " * (indent + 6)
            binds = "[" + (
                "\n" + sp_b
            ).join(f"{k} {v.emit(indent + 6 + len(k) + 1)}"
                   for k, v in self.bindings) + "]"
        body_indent = indent + 2
        if isinstance(self.body, list):
            sp_body = " " * body_indent
            body = "\n".join(sp_body + e.emit(body_indent) for e in self.body)
        else:
            body = self.body.emit(body_indent)
        if "\n" not in binds and "\n" not in body and len(binds) + len(body) < 70:
            return f"(let {binds} {body})"
        return f"(let {binds}\n{' '*body_indent}{body})"


@dataclass
class Fn(Expr):
    """Anonymous function. Params are a list of symbol names."""
    params: list[str]
    body:   Expr

    def eval(self, env: dict) -> Any:
        params = self.params
        body = self.body
        def _fn(args: list[Any]) -> Any:
            sub = dict(env)
            for p, a in zip(params, args):
                sub[p] = a
            return body.eval(sub)
        return _fn

    def emit(self, indent: int = 0) -> str:
        ps = " ".join(self.params)
        return f"(fn [{ps}] {self.body.emit(indent + 4 + len(ps))})"


@dataclass
class Def(Expr):
    """Top-level definition. `(def name expr)`."""
    name: str
    body: Expr

    def eval(self, env: dict) -> Any:
        env[self.name] = self.body.eval(env)
        return env[self.name]

    def emit(self, indent: int = 0) -> str:
        return f"(def {self.name} {self.body.emit(indent + 6 + len(self.name))})"


@dataclass
class Do(Expr):
    """Sequence of expressions; value is the last one's value."""
    body: list[Expr]
    def eval(self, env: dict) -> Any:
        last = None
        for e in self.body:
            last = e.eval(env)
        return last
    def emit(self, indent: int = 0) -> str:
        return "\n".join(e.emit(indent) for e in self.body)


@dataclass
class Try(Expr):
    """try / catch. body executes; on exception, bind to `binding` and
    evaluate `handler`."""
    body:    Expr
    binding: str
    handler: Expr

    def eval(self, env: dict) -> Any:
        try:
            return self.body.eval(env)
        except Exception as exc:
            sub = dict(env)
            sub[self.binding] = exc
            return self.handler.eval(sub)

    def emit(self, indent: int = 0) -> str:
        b = self.body.emit(indent + 5)
        h = self.handler.emit(indent + 5)
        return f"(try {b} (catch Exception {self.binding} {h}))"


@dataclass
class Thread(Expr):
    """Threading macro. style='->' or '->>'."""
    style: str
    init:  Expr
    steps: list[Expr]    # each is an App with the thread argument elided

    def _expand(self) -> Expr:
        cur = self.init
        for st in self.steps:
            assert isinstance(st, App), "thread step must be an App"
            new_args = list(st.args)
            if self.style == "->":
                new_args.insert(0, cur)
            else:  # ->>
                new_args.append(cur)
            cur = App(st.op, new_args)
        return cur

    def eval(self, env: dict) -> Any:
        return self._expand().eval(env)

    def emit(self, indent: int = 0) -> str:
        sp = " " * (indent + len(self.style) + 2)
        head = f"({self.style} {self.init.emit(indent + len(self.style) + 2)}"
        for st in self.steps:
            head += "\n" + sp + st.emit(indent + len(self.style) + 2)
        return head + ")"


# ─────────────────────── Helpers ───────────────────────


def _eval_v(v: Any, env: dict) -> Any:
    return v.eval(env) if isinstance(v, Expr) else v


def _truthy(v: Any) -> bool:
    """Clojure truthiness: nil and false are falsy; everything else truthy."""
    return v is not None and v is not False


def _emit_value(v: Any, *, is_kw: bool = False, is_set: bool = False) -> str:
    from fractions import Fraction
    if is_kw:
        return f":{v}"
    # Sentinels round-tripped from eval.
    if isinstance(v, tuple) and len(v) == 2:
        if v[0] == "__kw__":  return f":{v[1]}"
        if v[0] == "__sym__": return f"'{v[1]}"
    if v is None:
        return "nil"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, Fraction):
        return f"{v.numerator}/{v.denominator}"
    if isinstance(v, str):
        # Clojure string: escape backslash + double-quote.
        esc = v.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{esc}"'
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return str(v)
    if isinstance(v, list):
        prefix = "#" if is_set else ""
        return prefix + "[" + " ".join(
            _emit_value(x.value, is_kw=getattr(x, "is_kw", False),
                                  is_set=getattr(x, "is_set", False))
            if isinstance(x, Lit) else x.emit() if isinstance(x, Expr)
            else _emit_value(x)
            for x in v) + "]"
    if isinstance(v, dict):
        items = []
        for k, val in v.items():
            ks = _emit_value(k.value, is_kw=getattr(k, "is_kw", False)) \
                 if isinstance(k, Lit) else k.emit() if isinstance(k, Expr) \
                 else _emit_value(k)
            vs = _emit_value(val.value, is_kw=getattr(val, "is_kw", False)) \
                 if isinstance(val, Lit) else val.emit() if isinstance(val, Expr) \
                 else _emit_value(val)
            items.append(f"{ks} {vs}")
        return "{" + ", ".join(items) + "}"
    return str(v)


# ─────────────────────── Operations ───────────────────────


# Each op is a function (args, env) -> result. `args` is a list of already-
# evaluated argument values. `env` is provided in case an op needs it (only
# `apply` does, currently).

def _op_plus(args, _):
    return sum(args) if args else 0
def _op_minus(args, _):
    if not args:
        return 0
    if len(args) == 1:
        return -args[0]
    out = args[0]
    for x in args[1:]:
        out -= x
    return out
def _op_times(args, _):
    out = 1
    for x in args:
        out *= x
    return out
def _op_div(args, _):
    """Integer args produce a Fraction (Clojure ratio); float args
    produce a float. Matches Clojure's promoting `/` semantics."""
    from fractions import Fraction
    if len(args) == 1:
        a = args[0]
        if isinstance(a, int) and not isinstance(a, bool):
            return Fraction(1, a)
        return 1 / a
    if all(isinstance(x, int) and not isinstance(x, bool) for x in args):
        out = Fraction(args[0])
        for x in args[1:]:
            out = out / x
        return int(out) if out.denominator == 1 else out
    out = args[0]
    for x in args[1:]:
        out = out / x
    return out
def _op_quot(args, _):
    a, b = args
    return int(a / b) if (a < 0) != (b < 0) and a % b else a // b
def _op_rem(args, _):
    a, b = args
    r = abs(a) % abs(b)
    return r if a >= 0 else -r
def _op_mod(args, _):
    return args[0] % args[1]
def _op_inc(args, _):  return args[0] + 1
def _op_dec(args, _):  return args[0] - 1
def _op_abs(args, _):  return abs(args[0])
def _op_min(args, _):  return min(args)
def _op_max(args, _):  return max(args)

def _op_eq(args, _):
    a = args[0]
    return all(x == a for x in args[1:])
def _op_neq(args, _): return not _op_eq(args, _)
def _op_lt(args, _):  return all(args[i] <  args[i+1] for i in range(len(args)-1))
def _op_le(args, _):  return all(args[i] <= args[i+1] for i in range(len(args)-1))
def _op_gt(args, _):  return all(args[i] >  args[i+1] for i in range(len(args)-1))
def _op_ge(args, _):  return all(args[i] >= args[i+1] for i in range(len(args)-1))
def _op_zero(args, _):  return args[0] == 0
def _op_pos(args, _):   return args[0] > 0
def _op_neg(args, _):   return args[0] < 0
def _op_odd(args, _):   return args[0] % 2 != 0
def _op_even(args, _):  return args[0] % 2 == 0
def _op_empty(args, _): return len(args[0]) == 0

def _op_and(args, _):
    last = True
    for v in args:
        if not _truthy(v):
            return v
        last = v
    return last
def _op_or(args, _):
    for v in args:
        if _truthy(v):
            return v
    return args[-1] if args else None
def _op_not(args, _):
    return not _truthy(args[0])

# Sequences
def _op_list(args, _):    return list(args)
def _op_vector(args, _):  return list(args)
def _op_range(args, _):
    if len(args) == 1:
        return list(range(args[0]))
    if len(args) == 2:
        return list(range(args[0], args[1]))
    return list(range(args[0], args[1], args[2]))
def _op_repeat(args, _):
    n, v = args
    return [v] * n
def _op_take(args, _):    n, xs = args; return list(xs[:n])
def _op_drop(args, _):    n, xs = args; return list(xs[n:])
def _op_count(args, _):
    v = args[0]
    return 0 if v is None else len(v)
def _op_first(args, _):
    xs = args[0]
    return xs[0] if xs else None
def _op_last(args, _):
    xs = args[0]
    return xs[-1] if xs else None
def _op_rest(args, _):    return list(args[0][1:])
def _op_butlast(args, _): return list(args[0][:-1])
def _op_conj(args, _):
    coll, *rest = args
    if isinstance(coll, list):
        return list(coll) + list(rest)
    if isinstance(coll, frozenset):
        return coll | frozenset(rest)
    return list(coll) + list(rest)
def _op_into(args, _):
    to, frm = args
    if isinstance(to, list):
        return list(to) + list(frm)
    if isinstance(to, frozenset):
        return to | frozenset(frm)
    return list(to) + list(frm)
def _op_reverse(args, _):  return list(reversed(args[0]))
def _op_sort(args, _):     return sorted(args[0])
def _op_distinct(args, _):
    out, seen = [], set()
    for x in args[0]:
        if x not in seen:
            seen.add(x); out.append(x)
    return out
def _op_partition(args, _):
    n, xs = args
    return [list(xs[i:i+n]) for i in range(0, len(xs), n) if len(xs[i:i+n]) == n]

# Higher-order
def _op_map(args, _):
    f, *colls = args
    return [f(list(t)) for t in zip(*colls)]
def _op_filter(args, _):
    f, xs = args
    return [x for x in xs if _truthy(f([x]))]
def _op_reduce(args, _):
    if len(args) == 2:
        f, xs = args
        if not xs: return None
        out = xs[0]
        for x in xs[1:]:
            out = f([out, x])
        return out
    f, init, xs = args
    out = init
    for x in xs:
        out = f([out, x])
    return out
def _op_apply(args, env):
    f, *rest = args
    *fixed, last = rest
    return f(list(fixed) + list(last))
def _op_comp(args, _):
    fns = args
    def _c(xs):
        out = xs
        for f in reversed(fns):
            out = [f(out)]
        return out[0]
    return _c
def _op_partial(args, _):
    f, *fixed = args
    def _p(more):
        return f(list(fixed) + list(more))
    return _p

# Maps
def _op_hash_map(args, _):
    return {args[i]: args[i+1] for i in range(0, len(args), 2)}
def _op_get(args, _):
    if len(args) == 2:
        coll, k = args
        return coll.get(k) if isinstance(coll, dict) else (
            coll[k] if 0 <= k < len(coll) else None
        )
    coll, k, default = args
    if isinstance(coll, dict):
        return coll.get(k, default)
    return coll[k] if 0 <= k < len(coll) else default
def _op_assoc(args, _):
    coll, k, v = args[0], args[1], args[2]
    rest = args[3:]
    new = dict(coll) if isinstance(coll, dict) else list(coll)
    if isinstance(new, dict):
        new[k] = v
        for i in range(0, len(rest), 2):
            new[rest[i]] = rest[i+1]
    else:
        new[k] = v
    return new
def _op_dissoc(args, _):
    coll, *ks = args
    new = dict(coll)
    for k in ks:
        new.pop(k, None)
    return new
def _op_keys(args, _):     return list(args[0].keys())
def _op_vals(args, _):     return list(args[0].values())
def _op_merge(args, _):
    out = {}
    for d in args:
        if d: out.update(d)
    return out
def _op_contains(args, _):
    coll, k = args
    if isinstance(coll, dict):
        return k in coll
    if isinstance(coll, frozenset):
        return k in coll
    return 0 <= k < len(coll)

# Strings
def _op_str(args, _):
    parts = []
    for a in args:
        if a is None:
            continue
        if a is True:
            parts.append("true")
        elif a is False:
            parts.append("false")
        else:
            parts.append(str(a))
    return "".join(parts)
def _op_str_upper(args, _):  return args[0].upper()
def _op_str_lower(args, _):  return args[0].lower()
def _op_str_join(args, _):
    if len(args) == 1:
        sep, xs = "", args[0]
    else:
        sep, xs = args
    return sep.join(str(x) for x in xs)
def _op_str_split(args, _):
    s, sep = args
    return s.split(sep)


# ─────────────────────── Type predicates ───────────────────────


def _is_kw(v):  return isinstance(v, tuple) and len(v) == 2 and v[0] == "__kw__"
def _is_sym(v): return isinstance(v, tuple) and len(v) == 2 and v[0] == "__sym__"


def _op_nil_q(args, _):       return args[0] is None
def _op_some_q(args, _):      return args[0] is not None
def _op_true_q(args, _):      return args[0] is True
def _op_false_q(args, _):     return args[0] is False
def _op_keyword_q(args, _):   return _is_kw(args[0])
def _op_symbol_q(args, _):    return _is_sym(args[0])
def _op_string_q(args, _):    return isinstance(args[0], str) and not _is_kw(args[0]) and not _is_sym(args[0])
def _op_number_q(args, _):
    v = args[0]
    if isinstance(v, bool):  return False
    from fractions import Fraction
    return isinstance(v, (int, float, Fraction))
def _op_integer_q(args, _):
    v = args[0]
    return isinstance(v, int) and not isinstance(v, bool)
def _op_ratio_q(args, _):
    from fractions import Fraction
    return isinstance(args[0], Fraction)
def _op_float_q(args, _):     return isinstance(args[0], float)
def _op_char_q(args, _):
    v = args[0]
    return isinstance(v, str) and len(v) == 1 and not _is_kw(v) and not _is_sym(v)
def _op_boolean_q(args, _):   return isinstance(args[0], bool)
def _op_list_q(args, _):      return isinstance(args[0], list)
def _op_vector_q(args, _):    return isinstance(args[0], list)  # Clojure can distinguish; we treat as list
def _op_map_q(args, _):       return isinstance(args[0], dict)
def _op_set_q(args, _):       return isinstance(args[0], (set, frozenset))
def _op_coll_q(args, _):      return isinstance(args[0], (list, dict, set, frozenset))
def _op_seq_q(args, _):       return isinstance(args[0], (list, tuple)) and not _is_kw(args[0]) and not _is_sym(args[0])
def _op_seqable_q(args, _):
    v = args[0]
    return v is None or isinstance(v, (list, dict, set, frozenset, str, tuple))
def _op_fn_q(args, _):        return callable(args[0])
def _op_assoc_q(args, _):
    return isinstance(args[0], dict) or isinstance(args[0], list)


# ─────────────────────── More collection ops ───────────────────────


def _op_seq(args, _):
    v = args[0]
    if v is None:                return None
    if isinstance(v, dict):      return list(v.items()) if v else None
    if hasattr(v, "__len__"):    return list(v) if len(v) else None
    return list(v)


def _op_nth(args, _):
    coll, idx = args[0], args[1]
    default = args[2] if len(args) > 2 else None
    try:
        return coll[idx]
    except (IndexError, KeyError):
        if len(args) > 2: return default
        raise


def _op_concat(args, _):
    out = []
    for x in args:
        if x is None: continue
        out.extend(list(x))
    return out


def _op_interpose(args, _):
    sep, coll = args
    coll = list(coll)
    if not coll: return []
    out = [coll[0]]
    for x in coll[1:]:
        out.append(sep)
        out.append(x)
    return out


def _op_interleave(args, _):
    if not args: return []
    seqs = [list(s) for s in args]
    if not seqs: return []
    n = min(len(s) for s in seqs)
    out = []
    for i in range(n):
        for s in seqs:
            out.append(s[i])
    return out


def _op_flatten(args, _):
    def _walk(x):
        if isinstance(x, (list, tuple)):
            for y in x:
                yield from _walk(y)
        else:
            yield x
    return list(_walk(args[0]))


def _op_frequencies(args, _):
    out = {}
    for x in args[0]:
        key = tuple(x) if isinstance(x, list) else x
        out[key] = out.get(key, 0) + 1
    return out


def _op_group_by(args, _):
    f, coll = args
    out = {}
    for x in coll:
        k = f([x])
        out.setdefault(k, []).append(x)
    return out


def _op_not_empty(args, _):
    v = args[0]
    return v if v else None


def _op_second(args, _):
    v = args[0]
    return v[1] if len(v) > 1 else None


def _op_nthrest(args, _):
    return list(args[0][args[1]:])


def _op_take_while(args, _):
    f, coll = args
    out = []
    for x in coll:
        if not f([x]):
            break
        out.append(x)
    return out


def _op_drop_while(args, _):
    f, coll = args
    coll = list(coll)
    i = 0
    while i < len(coll) and f([coll[i]]):
        i += 1
    return coll[i:]


def _op_remove(args, _):
    f, coll = args
    return [x for x in coll if not f([x])]


def _op_some(args, _):
    """`(some pred coll)` — returns the first truthy `pred(x)` value
    for x in coll, else nil. Common in Clojure for "any matches."""
    f, coll = args
    for x in coll:
        v = f([x])
        if _truthy(v):
            return v
    return None


def _op_every(args, _):
    f, coll = args
    return all(_truthy(f([x])) for x in coll)


def _op_not_any(args, _):
    f, coll = args
    return not any(_truthy(f([x])) for x in coll)


def _op_cons(args, _):
    x, coll = args
    if coll is None:
        return [x]
    return [x] + list(coll)


def _op_keep(args, _):
    f, coll = args
    out = []
    for x in coll:
        v = f([x])
        if v is not None:
            out.append(v)
    return out


def _op_juxt(args, _):
    funcs = args
    def _juxt_fn(in_args):
        return [f(list(in_args)) for f in funcs]
    return _juxt_fn


def _op_complement(args, _):
    f = args[0]
    return lambda in_args: not _truthy(f(list(in_args)))


def _op_constantly(args, _):
    val = args[0]
    return lambda in_args: val


def _op_identity(args, _):
    return args[0]


def _op_max_key(args, _):
    f, *coll = args
    if len(coll) == 1:
        coll = coll[0]
    return max(coll, key=lambda x: f([x]))


def _op_min_key(args, _):
    f, *coll = args
    if len(coll) == 1:
        coll = coll[0]
    return min(coll, key=lambda x: f([x]))


def _op_partition_by(args, _):
    f, coll = args
    out = []
    cur = []
    last_key = object()  # sentinel
    for x in coll:
        k = f([x])
        if k != last_key and cur:
            out.append(cur)
            cur = []
        cur.append(x)
        last_key = k
    if cur:
        out.append(cur)
    return out


def _op_sort_by(args, _):
    f, coll = args
    return sorted(coll, key=lambda x: f([x]))


def _op_iterate(args, _):
    # (iterate f x) → infinite seq; we cap at 100 for safety
    f, x = args
    out = [x]
    for _ in range(100):
        x = f([x])
        out.append(x)
    return out


def _op_repeatedly(args, _):
    if len(args) == 2:
        n, f = args
        return [f([]) for _ in range(n)]
    raise ValueError("repeatedly without n is unbounded")


def _op_zipmap(args, _):
    keys, vals = args
    return {k: v for k, v in zip(keys, vals)}


def _op_select_keys(args, _):
    m, ks = args
    return {k: m[k] for k in ks if k in m}


def _op_update(args, env):
    m, k, f, *rest = args
    new = dict(m)
    new[k] = f([m.get(k), *rest])
    return new


def _op_count_kw(args, _):
    """count behaves on nil → 0."""
    v = args[0]
    return 0 if v is None else len(v)


# ─────────────────────── String/IO ops ───────────────────────


def _op_println(args, _):
    # Side-effect-free: return nil. The model never sees stdout.
    return None


def _op_print(args, _):    return None
def _op_pr(args, _):       return None
def _op_prn(args, _):      return None
def _op_newline(args, _):  return None


def _op_str_starts(args, _):
    s, prefix = args
    return s.startswith(prefix)


def _op_str_ends(args, _):
    s, suffix = args
    return s.endswith(suffix)


def _op_str_includes(args, _):
    s, sub = args
    return sub in s


def _op_str_replace(args, _):
    s, a, b = args
    return s.replace(a, b)


def _op_str_trim(args, _):
    return args[0].strip()


def _op_str_blank(args, _):
    v = args[0]
    return v is None or v == "" or (isinstance(v, str) and v.strip() == "")


def _op_count_chars(args, _):
    return len(args[0])


def _op_subs(args, _):
    s = args[0]
    if len(args) == 2:
        return s[args[1]:]
    return s[args[1]:args[2]]


def _op_boolean(args, _):
    """Clojure's `boolean` coercion: nil and false → false; everything
    else → true."""
    v = args[0]
    return _truthy(v)


def _op_symbol(args, _):
    if len(args) == 1:
        return ("__sym__", args[0])
    return ("__sym__", f"{args[0]}/{args[1]}")


def _op_keyword(args, _):
    if len(args) == 1:
        v = args[0]
        if isinstance(v, str):
            return ("__kw__", v)
        if isinstance(v, tuple) and len(v) == 2 and v[0] in ("__kw__", "__sym__"):
            return ("__kw__", v[1])
    return ("__kw__", f"{args[0]}/{args[1]}")


def _op_name(args, _):
    v = args[0]
    if isinstance(v, tuple) and len(v) == 2 and v[0] in ("__kw__", "__sym__"):
        return v[1]
    if isinstance(v, str):
        return v
    raise TypeError(f"name expects keyword/symbol/string, got {v!r}")


def _op_namespace(args, _):
    v = args[0]
    if isinstance(v, tuple) and len(v) == 2 and v[0] in ("__kw__", "__sym__"):
        if "/" in v[1]:
            return v[1].split("/", 1)[0]
        return None
    return None


# ─────────────────────── Keyword-as-fn / map-as-fn / set-as-fn ─────────────


def _op_kw_lookup(args, _):
    """Keyword-as-function for map lookup: (:k m) → (get m :k).
    Identified by the parser when it sees a keyword in head position."""
    if len(args) == 2:
        kw, m = args
        if isinstance(m, dict):
            return m.get(kw)
        return None
    if len(args) == 3:
        kw, m, dflt = args
        if isinstance(m, dict):
            return m.get(kw, dflt)
        return dflt
    raise ValueError("keyword-as-fn takes 1-2 args after the keyword")


# ─────────────────────── case ───────────────────────


# Note: `case` is implemented in the parser by lowering to Cond — see
# form_parser. No runtime op needed.


OPS: dict[str, Callable[[list[Any], dict], Any]] = {
    "+":  _op_plus, "-": _op_minus, "*": _op_times, "/": _op_div,
    "quot": _op_quot, "rem": _op_rem, "mod": _op_mod,
    "inc": _op_inc,  "dec": _op_dec, "abs": _op_abs,
    "min": _op_min,  "max": _op_max,

    "=":  _op_eq, "not=": _op_neq,
    "<": _op_lt, "<=": _op_le, ">": _op_gt, ">=": _op_ge,
    "zero?": _op_zero, "pos?": _op_pos, "neg?": _op_neg,
    "odd?": _op_odd, "even?": _op_even, "empty?": _op_empty,

    "and": _op_and, "or": _op_or, "not": _op_not,

    "list": _op_list, "vector": _op_vector,
    "range": _op_range, "repeat": _op_repeat,
    "take": _op_take, "drop": _op_drop,
    "count": _op_count, "first": _op_first, "last": _op_last,
    "rest": _op_rest, "butlast": _op_butlast,
    "conj": _op_conj, "into": _op_into,
    "reverse": _op_reverse, "sort": _op_sort,
    "distinct": _op_distinct, "partition": _op_partition,

    "map": _op_map, "filter": _op_filter, "reduce": _op_reduce,
    "apply": _op_apply, "comp": _op_comp, "partial": _op_partial,

    "hash-map": _op_hash_map,
    "get": _op_get, "assoc": _op_assoc, "dissoc": _op_dissoc,
    "keys": _op_keys, "vals": _op_vals, "merge": _op_merge,
    "contains?": _op_contains,

    "str": _op_str,
    "clojure.string/upper-case":  _op_str_upper,
    "clojure.string/lower-case":  _op_str_lower,
    "clojure.string/join":        _op_str_join,
    "clojure.string/split":       _op_str_split,
    "clojure.string/starts-with?": _op_str_starts,
    "clojure.string/ends-with?":   _op_str_ends,
    "clojure.string/includes?":    _op_str_includes,
    "clojure.string/replace":      _op_str_replace,
    "clojure.string/trim":         _op_str_trim,
    "clojure.string/blank?":       _op_str_blank,

    "nil?": _op_nil_q, "some?": _op_some_q,
    "true?": _op_true_q, "false?": _op_false_q,
    "keyword?": _op_keyword_q, "symbol?": _op_symbol_q,
    "string?": _op_string_q, "number?": _op_number_q,
    "integer?": _op_integer_q, "int?": _op_integer_q,
    "ratio?": _op_ratio_q, "float?": _op_float_q,
    "char?": _op_char_q, "boolean?": _op_boolean_q,
    "list?": _op_list_q, "vector?": _op_vector_q,
    "map?": _op_map_q, "set?": _op_set_q,
    "coll?": _op_coll_q, "seq?": _op_seq_q,
    "seqable?": _op_seqable_q, "fn?": _op_fn_q,
    "associative?": _op_assoc_q,

    "seq": _op_seq, "nth": _op_nth, "second": _op_second,
    "concat": _op_concat, "interpose": _op_interpose,
    "interleave": _op_interleave, "flatten": _op_flatten,
    "frequencies": _op_frequencies, "group-by": _op_group_by,
    "not-empty": _op_not_empty, "nthrest": _op_nthrest,
    "take-while": _op_take_while, "drop-while": _op_drop_while,
    "remove": _op_remove, "iterate": _op_iterate,
    "repeatedly": _op_repeatedly, "zipmap": _op_zipmap,
    "select-keys": _op_select_keys, "update": _op_update,
    "some": _op_some, "every?": _op_every, "not-any?": _op_not_any,
    "cons": _op_cons, "keep": _op_keep, "juxt": _op_juxt,
    "complement": _op_complement, "constantly": _op_constantly,
    "identity": _op_identity,
    "max-key": _op_max_key, "min-key": _op_min_key,
    "partition-by": _op_partition_by, "sort-by": _op_sort_by,

    "println": _op_println, "print": _op_print,
    "pr": _op_pr, "prn": _op_prn, "newline": _op_newline,

    "subs": _op_subs, "boolean": _op_boolean,
    "symbol": _op_symbol, "keyword": _op_keyword,
    "name": _op_name, "namespace": _op_namespace,

    "__kw_lookup__": _op_kw_lookup,
}


# ─────────────────────── Public helpers ───────────────────────


def evaluate(expr: Expr, env: dict | None = None) -> Any:
    return expr.eval(dict(env or {}))


def emit_clojure(expr: Expr) -> str:
    return expr.emit(0)


def emit_clojure_inline(expr: Expr) -> str:
    """Single-line Clojure rendering — collapses multi-line layouts so
    the form fits cleanly inside a JSON-encoded `eval(form: …)` arg."""
    import re
    return re.sub(r"\s*\n\s*", " ", expr.emit(0))


# ─────────────────────── Self-test ───────────────────────


def smoke_test() -> None:
    # Arithmetic
    e1 = App("+", [Lit(3), Lit(2)])
    assert evaluate(e1) == 5
    assert emit_clojure(e1) == "(+ 3 2)"

    # Let with multiple bindings
    e2 = Let(
        [("alice", Lit(3)), ("gift", Lit(2))],
        App("+", [Var("alice"), Var("gift")]),
    )
    assert evaluate(e2) == 5

    # If
    e3 = If(App(">", [Lit(8), Lit(6)]), Lit("Shelly"), Lit("Whisker"))
    assert evaluate(e3) == "Shelly"

    # Cond
    e4 = Cond(
        clauses=[
            (App("=", [Var("n"), Lit(0)]), Lit("zero")),
            (App("pos?", [Var("n")]), Lit("positive")),
        ],
        default=Lit("negative"),
    )
    assert evaluate(e4, {"n": 0})  == "zero"
    assert evaluate(e4, {"n": 5})  == "positive"
    assert evaluate(e4, {"n": -3}) == "negative"

    # Higher-order: map / filter / reduce
    e5 = App("map", [Fn(["x"], App("*", [Var("x"), Lit(2)])),
                     Lit([1, 2, 3])])
    assert evaluate(e5) == [2, 4, 6]

    e6 = App("filter", [Fn(["x"], App("even?", [Var("x")])),
                        App("range", [Lit(10)])])
    assert evaluate(e6) == [0, 2, 4, 6, 8]

    e7 = App("reduce", [Fn(["a", "b"], App("+", [Var("a"), Var("b")])),
                        Lit(0),
                        App("range", [Lit(1), Lit(11)])])
    assert evaluate(e7) == 55

    # Threading macro: (-> 5 inc inc dec) → 6
    e8 = Thread("->", Lit(5),
                [App("inc", []), App("inc", []), App("dec", [])])
    assert evaluate(e8) == 6
    s8 = emit_clojure(e8)
    assert s8.startswith("(->"), s8

    # Strings
    e9 = App("str", [Lit("Alice has "), Lit(3), Lit(" apples")])
    assert evaluate(e9) == "Alice has 3 apples"

    # Maps
    e10 = App("get", [App("hash-map", [Lit("a"), Lit(1), Lit("b"), Lit(2)]),
                      Lit("b")])
    assert evaluate(e10) == 2

    # Crow + pitcher style: how many stones to raise water?
    # (let [start 5  target 10  per-stone 1]
    #   (quot (- target start) per-stone))
    e11 = Let(
        [("start", Lit(5)), ("target", Lit(10)), ("per-stone", Lit(1))],
        App("quot",
            [App("-", [Var("target"), Var("start")]), Var("per-stone")]),
    )
    assert evaluate(e11) == 5

    # Goose: 30 days × 1 egg/day × 100 coins/egg
    e12 = App("*", [Lit(30), Lit(1), Lit(100)])
    assert evaluate(e12) == 3000

    # Milkmaid chained: (* eggs (- 1 spoiled-frac) coins-per-hen)
    # uses ints only — mock at quot 1 (no fractional spoilage)
    e13 = App("*", [Lit(12), Lit(5)])
    assert evaluate(e13) == 60

    print("expr smoke OK — all 13 cases pass")


if __name__ == "__main__":
    smoke_test()
