"""S-expression parser for the curriculum's Clojure subset.

Consumes a rendered Clojure form (string) and produces an `Expr` tree
that `mmllm.aesop.expr.evaluate` can run. The verifier round-trips
every parametric form through this parser so the answer is computed
by the same engine the model is supposed to internalize.

Subset coverage matches `expr.py`:

  literals     ints (incl. negative), bigints, ratios (a/b), bools
               (true/false), nil, keywords (:foo), strings ("…"),
               characters (\\a), vectors [...], maps {...}, sets #{...}
  symbols      → Var()
  function     (sym arg*)              → App
  special      (if c t e), (when c body…), (cond …), (let […] body…),
               (fn [params] body), (do …), (-> x f1 f2…), (->> x f1 f2…)

Anything outside this subset raises `UnsupportedForm` so the test pass
will flag it explicitly.
"""
from __future__ import annotations

import re
from typing import Any

from mmllm.aesop.expr import (
    Expr, Lit, Var, App, If, When, Cond, Let, Fn, Do, Thread, Def, Try,
)


class ParseError(Exception): pass
class UnsupportedForm(ParseError): pass


# ─────────────────────── tokenize ───────────────────────


# Token regex: parens/brackets/braces, #{ for sets, strings, char lits,
# numbers (incl. ratios + bigints), keywords, symbols, comments.
_TOKEN_RE = re.compile(r"""
    (?P<ws>      [\s,]+                                        ) |
    (?P<comment> ;[^\n]*                                       ) |
    (?P<lparen>  \(                                            ) |
    (?P<rparen>  \)                                            ) |
    (?P<lbrack>  \[                                            ) |
    (?P<rbrack>  \]                                            ) |
    (?P<lbrace>  \{                                            ) |
    (?P<rbrace>  \}                                            ) |
    (?P<setopen> \#\{                                          ) |
    (?P<quote>   '                                             ) |
    (?P<string>  " (?: \\. | [^"\\] )* "                       ) |
    (?P<charlit> \\ (?: newline|space|tab|return|\S )          ) |
    (?P<ratio>   -? \d+ / \d+                                  ) |
    (?P<bigint>  -? \d+ N                                      ) |
    (?P<number>  -? \d+ (?: \.\d+ )?                           ) |
    (?P<keyword> :: ?[A-Za-z_*+!?<>=/.\-][A-Za-z0-9_*+!?<>=/.\-]* | : [A-Za-z_*+!?<>=/.\-][A-Za-z0-9_*+!?<>=/.\-]* ) |
    (?P<symbol>  [A-Za-z_*+!?<>=/.\-][A-Za-z0-9_*+!?<>=/.\-]*  )
""", re.VERBOSE)


def tokenize(src: str) -> list[tuple[str, str]]:
    out  = []
    pos  = 0
    end  = len(src)
    while pos < end:
        m = _TOKEN_RE.match(src, pos)
        if m is None:
            ctx = src[max(0, pos - 20):pos + 20]
            raise ParseError(f"tokenize fail at {pos}: …{ctx!r}…")
        kind = m.lastgroup
        text = m.group()
        pos  = m.end()
        if kind in ("ws", "comment"):
            continue
        out.append((kind, text))
    return out


# ─────────────────────── parse ───────────────────────


def parse(src: str) -> Expr:
    """Parse a single top-level form. Raises ParseError on garbage."""
    toks = tokenize(src)
    expr, idx = _parse_one(toks, 0)
    if idx != len(toks):
        raise ParseError(f"trailing tokens after parse: {toks[idx:]!r}")
    return expr


def _parse_one(toks: list[tuple[str, str]], idx: int) -> tuple[Expr, int]:
    if idx >= len(toks):
        raise ParseError("unexpected end of input")
    kind, text = toks[idx]
    if kind == "lparen":
        return _parse_list(toks, idx + 1)
    if kind == "lbrack":
        return _parse_vector(toks, idx + 1)
    if kind == "lbrace":
        return _parse_map(toks, idx + 1)
    if kind == "setopen":
        return _parse_set(toks, idx + 1)
    if kind == "quote":
        # 'foo → quoted symbol: produces the runtime symbol value
        # `("__sym__", "foo")`. Quoted lists/literals are unused
        # in this curriculum subset.
        if idx + 1 < len(toks) and toks[idx + 1][0] == "symbol":
            sym_text = toks[idx + 1][1]
            return Lit(("__sym__", sym_text)), idx + 2
        inner, idx2 = _parse_one(toks, idx + 1)
        if isinstance(inner, Lit):
            return Lit(inner.value), idx2
        if isinstance(inner, Var):
            return Lit(("__sym__", inner.name)), idx2
        raise UnsupportedForm("quote of non-literal/non-symbol")
    if kind == "rparen" or kind == "rbrack" or kind == "rbrace":
        raise ParseError(f"unbalanced delimiter: {text!r}")
    return _atom(kind, text), idx + 1


def _atom(kind: str, text: str) -> Expr:
    if kind == "number":
        if "." in text:
            return Lit(float(text))
        return Lit(int(text))
    if kind == "bigint":
        return Lit(int(text[:-1]))
    if kind == "ratio":
        from fractions import Fraction
        n_s, d_s = text.split("/")
        return Lit(Fraction(int(n_s), int(d_s)))
    if kind == "string":
        return Lit(_unquote_string(text))
    if kind == "charlit":
        body = text[1:]
        if body == "newline": return Lit("\n", is_char=True)
        if body == "space":   return Lit(" ", is_char=True)
        if body == "tab":     return Lit("\t", is_char=True)
        if body == "return":  return Lit("\r", is_char=True)
        return Lit(body, is_char=True)
    if kind == "keyword":
        # :foo or ::foo — strip leading colon(s)
        return Lit(text.lstrip(":"), is_kw=True)
    if kind == "symbol":
        if text == "true":   return Lit(True)
        if text == "false":  return Lit(False)
        if text == "nil":    return Lit(None)
        return Var(text)
    raise ParseError(f"unknown atom kind: {kind}")


def _unquote_string(text: str) -> str:
    body = text[1:-1]
    out  = []
    i    = 0
    while i < len(body):
        c = body[i]
        if c == "\\" and i + 1 < len(body):
            nxt = body[i + 1]
            mapping = {"n": "\n", "t": "\t", "r": "\r",
                       "\"": "\"", "\\": "\\"}
            out.append(mapping.get(nxt, nxt))
            i += 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def _parse_list(toks, idx: int) -> tuple[Expr, int]:
    """Parse a `(...)` form. First slot is the head."""
    items, idx = _parse_until(toks, idx, "rparen")
    if not items:
        return Lit([]), idx
    head = items[0]
    rest = items[1:]
    if isinstance(head, Var):
        return _parse_call(head.name, rest), idx
    # Inline fn or other expr in head position → application.
    if isinstance(head, (Fn, Let, If, When, Cond, App)):
        return _ApplyExpr(head, rest), idx
    # Keyword in head position → map lookup `(:k m [default])`.
    if isinstance(head, Lit) and head.is_kw:
        return App("__kw_lookup__", [head] + rest), idx
    # Set in head position → set-as-predicate (rare; treat as call).
    if isinstance(head, Lit) and head.is_set:
        return App("__set_contains__", [head] + rest), idx
    # Fallback: data list.
    return Lit([_lit_value(x) for x in items]), idx


def _parse_call(op: str, args: list[Expr]) -> Expr:
    if op == "if":
        if len(args) == 2:
            return If(args[0], args[1], Lit(None))
        if len(args) == 3:
            return If(args[0], args[1], args[2])
        raise ParseError(f"if takes 2 or 3 args, got {len(args)}")
    if op == "when":
        if len(args) < 2:
            raise ParseError("when needs cond + body")
        return When(args[0], args[1:])
    if op == "cond":
        if len(args) % 2 != 0:
            raise ParseError("cond needs even arg count (test/expr pairs)")
        clauses = []
        default = Lit(None)
        for i in range(0, len(args), 2):
            test, expr = args[i], args[i + 1]
            if isinstance(test, Lit) and test.is_kw and test.value == "else":
                default = expr
                break
            if isinstance(test, Lit) and test.value is True:
                # (cond true x …) — fold to default
                default = expr
                break
            clauses.append((test, expr))
        return Cond(clauses=clauses, default=default)
    if op == "let":
        if len(args) < 2:
            raise ParseError("let needs binding-vector + body")
        bind = args[0]
        # Binding vector arrived as Lit([…]) of vars/values; we need
        # to recover them as a list of (name, expr) pairs. The vector
        # got parsed eagerly, so we re-tokenize-and-reparse the binding
        # vector by intercepting it during list parse. Simpler: route
        # vectors as raw items below.
        if not isinstance(bind, _BindingVec):
            raise ParseError(
                "let binding vector lost shape (parser bug); "
                "this means the binding vector wasn't routed through "
                "_parse_vector_for_bindings")
        bindings = bind.pairs
        body = args[1:]
        body_expr = body[0] if len(body) == 1 else Do(body)
        return Let(bindings=bindings, body=body_expr)
    if op == "fn":
        if len(args) < 2:
            raise ParseError("fn needs param-vector + body")
        params = args[0]
        if not isinstance(params, _ParamVec):
            raise ParseError("fn params not a vector")
        body = args[1:]
        body_expr = body[0] if len(body) == 1 else Do(body)
        return Fn(params=params.names, body=body_expr)
    if op == "do":
        return Do(args)
    if op == "quote":
        if len(args) != 1:
            raise ParseError(f"quote takes 1 arg, got {len(args)}")
        a = args[0]
        if isinstance(a, Var):
            return Lit(("__sym__", a.name))
        if isinstance(a, Lit):
            return a
        raise UnsupportedForm(f"quote of non-symbol/literal: {type(a).__name__}")
    if op == "def":
        # (def name expr)
        if len(args) != 2:
            raise ParseError(f"def takes 2 args, got {len(args)}")
        nm = args[0]
        if not isinstance(nm, Var):
            raise ParseError(f"def: name must be a symbol, got {nm!r}")
        return Def(name=nm.name, body=args[1])
    if op == "defn":
        # (defn name [params] body…) → (def name (fn [params] body…))
        if len(args) < 3:
            raise ParseError(f"defn needs name + params + body")
        nm = args[0]
        if not isinstance(nm, Var):
            raise ParseError(f"defn: name must be a symbol, got {nm!r}")
        params = args[1]
        if not isinstance(params, _ParamVec):
            raise ParseError(f"defn: params must be a vector, got {params!r}")
        body_forms = args[2:]
        body_expr = body_forms[0] if len(body_forms) == 1 else Do(body_forms)
        return Def(name=nm.name,
                   body=Fn(params=params.names, body=body_expr))
    if op == "case":
        # (case expr v1 r1 v2 r2 … default?)
        if len(args) < 3:
            raise ParseError(f"case needs subject + at least one clause")
        subject = args[0]
        rest = args[1:]
        clauses = []
        default = Lit(None)
        i = 0
        while i < len(rest):
            if i + 1 < len(rest):
                # (val result)
                val = rest[i]
                res = rest[i + 1]
                clauses.append(
                    (App("=", [subject, _value_for_case(val)]), res))
                i += 2
            else:
                # final default
                default = rest[i]
                i += 1
        return Cond(clauses=clauses, default=default)
    if op == "try":
        # (try body (catch ExceptionType binding handler))
        if len(args) < 2:
            raise ParseError("try needs body + catch clause")
        # Catch clause is the last App with op = "catch"
        body_forms = []
        binding = "e"
        handler = Lit(None)
        for a in args:
            if isinstance(a, App) and a.op == "catch":
                if len(a.args) < 3:
                    raise ParseError("catch needs Exception + binding + handler")
                # a.args[0] = Exception type (Var), a.args[1] = binding (Var)
                bnd = a.args[1]
                if not isinstance(bnd, Var):
                    raise ParseError("catch binding must be a symbol")
                binding = bnd.name
                handler_forms = a.args[2:]
                handler = (handler_forms[0] if len(handler_forms) == 1
                           else Do(handler_forms))
            else:
                body_forms.append(a)
        body = body_forms[0] if len(body_forms) == 1 else Do(body_forms)
        return Try(body=body, binding=binding, handler=handler)
    if op == "loop":
        raise UnsupportedForm("loop/recur not supported; use reduce/iterate")
    if op == "for":
        raise UnsupportedForm("for not supported; use map/filter")
    if op == "defmacro":
        raise UnsupportedForm("defmacro requires bb pre-flight verifier")
    if op == "defprotocol" or op == "defrecord" or op == "deftype":
        raise UnsupportedForm(f"{op} requires bb pre-flight verifier")
    if op in ("->", "->>"):
        if len(args) < 1:
            raise ParseError(f"{op} needs at least an init expression")
        init = args[0]
        steps = []
        for s in args[1:]:
            if isinstance(s, App):
                steps.append(s)
            elif isinstance(s, Var):
                # bare symbol — equivalent to (sym)
                steps.append(App(s.name, []))
            else:
                raise ParseError(f"{op} step must be a call or symbol")
        return Thread(style=op, init=init, steps=steps)
    # Default: function application.
    return App(op, args)


def _parse_until(toks, idx: int, terminator: str) -> tuple[list[Expr], int]:
    """Parse forms until we hit `terminator`. Special-case bracket
    vectors that should be parsed as binding/param vectors rather than
    data literals:
      • `let [pairs] body…`        → binding vector at position 1
      • `fn [params] body…`        → param vector at position 1
      • `defn name [params] body…` → param vector at position 2
      • `loop [pairs] body…`       → would be binding (we reject loop
                                     in _parse_call so this is moot)
    """
    items = []
    while idx < len(toks) and toks[idx][0] != terminator:
        if (len(items) >= 1
            and isinstance(items[0], Var)
            and toks[idx][0] == "lbrack"):
            head_name = items[0].name
            if head_name == "let" and len(items) == 1:
                vec, idx = _parse_binding_vec(toks, idx + 1)
                items.append(vec)
                continue
            if head_name == "fn" and len(items) == 1:
                vec, idx = _parse_param_vec(toks, idx + 1)
                items.append(vec)
                continue
            if head_name == "defn" and len(items) == 2:
                vec, idx = _parse_param_vec(toks, idx + 1)
                items.append(vec)
                continue
        expr, idx = _parse_one(toks, idx)
        items.append(expr)
    if idx >= len(toks):
        raise ParseError(f"unbalanced — missing {terminator}")
    return items, idx + 1


def _parse_vector(toks, idx: int) -> tuple[Expr, int]:
    items, idx = _parse_until(toks, idx, "rbrack")
    return Lit([_lit_value(x) for x in items]), idx


def _parse_map(toks, idx: int) -> tuple[Expr, int]:
    items, idx = _parse_until(toks, idx, "rbrace")
    if len(items) % 2 != 0:
        raise ParseError("map literal needs even token count")
    pairs = {}
    for i in range(0, len(items), 2):
        k = _lit_value(items[i])
        v = _lit_value(items[i + 1])
        pairs[k] = v
    return Lit(pairs), idx


def _parse_set(toks, idx: int) -> tuple[Expr, int]:
    items, idx = _parse_until(toks, idx, "rbrace")
    return Lit([_lit_value(x) for x in items], is_set=True), idx


def _value_for_case(e: Expr) -> Expr:
    """In `case`, the test values are unevaluated Clojure literals.
    We treat bare symbols as quoted symbols and pass-through everything
    else."""
    if isinstance(e, Var):
        return Lit(("__sym__", e.name))
    return e


def _lit_value(e: Expr) -> Any:
    """Reduce an Expr that should be a literal value (inside vector/map)
    to its raw Python value. Variables and calls inside data literals
    are unsupported in this curriculum subset."""
    if isinstance(e, Lit):
        if e.is_kw:
            return ("__kw__", e.value)
        return e.value
    if isinstance(e, Var):
        # Allow bare symbols inside data literals only as keyword-style
        # tokens (rare; we don't expect this in our forms).
        raise UnsupportedForm(
            f"variable {e.name!r} inside data literal")
    raise UnsupportedForm(f"non-literal {type(e).__name__} in data literal")


# ─────────────────────── let/fn binding helpers ───────────────────────


from dataclasses import dataclass


@dataclass
class _BindingVec(Expr):
    pairs: list  # [(name, Expr), ...]
    def eval(self, env): raise RuntimeError("binding vec is meta")
    def emit(self, indent=0): raise RuntimeError("binding vec is meta")


@dataclass
class _ParamVec(Expr):
    names: list  # [str]
    def eval(self, env): raise RuntimeError("param vec is meta")
    def emit(self, indent=0): raise RuntimeError("param vec is meta")


@dataclass
class _ApplyExpr(Expr):
    """Application of an Expr in head position to args.

    Used for IIFE patterns: `((fn [x] (* x x)) 5)`. The head Expr is
    evaluated to a callable, then applied to evaluated args.
    """
    head: Expr
    args: list

    def eval(self, env):
        f = self.head.eval(env)
        evaled = [a.eval(env) for a in self.args]
        if not callable(f):
            raise TypeError(f"apply: head is not callable: {f!r}")
        return f(evaled)

    def emit(self, indent=0):
        head_s = self.head.emit(indent + 1)
        args_s = " ".join(a.emit(indent + 1) for a in self.args)
        return f"({head_s} {args_s})" if args_s else f"({head_s})"


def _parse_binding_vec(toks, idx: int) -> tuple[_BindingVec, int]:
    items, idx = _parse_until(toks, idx, "rbrack")
    if len(items) % 2 != 0:
        raise ParseError("let binding vector needs even token count")
    pairs = []
    for i in range(0, len(items), 2):
        nm = items[i]
        if not isinstance(nm, Var):
            raise ParseError(f"binding name must be a symbol: {nm!r}")
        pairs.append((nm.name, items[i + 1]))
    return _BindingVec(pairs), idx


def _parse_param_vec(toks, idx: int) -> tuple[_ParamVec, int]:
    items, idx = _parse_until(toks, idx, "rbrack")
    names = []
    for it in items:
        if not isinstance(it, Var):
            raise ParseError(f"fn param must be a symbol: {it!r}")
        names.append(it.name)
    return _ParamVec(names), idx


# ─────────────────────── self-test ───────────────────────


def smoke_test() -> None:
    from mmllm.aesop.expr import evaluate

    cases = [
        ("42",                       42),
        ("0",                        0),
        ("-3",                       -3),
        ("\"hello\"",                "hello"),
        ("nil",                      None),
        ("true",                     True),
        ("(+ 1 2 3)",                6),
        ("(* 2 3 4)",                24),
        ("(- 100 1 2 3)",            94),
        ("(< 1 2 3)",                True),
        ("(<= 1 1 2)",               True),
        ("(if true :a :b)",          ("__kw__", "a")),
        ("(if (> 5 3) 1 2)",         1),
        ("(when (pos? 5) :ok)",      ("__kw__", "ok")),
        ("(let [x 3 y 2] (+ x y))",  5),
        ("(map (fn [n] (* n 2)) [1 2 3])",            [2, 4, 6]),
        ("(filter (fn [n] (even? n)) (range 10))",    [0, 2, 4, 6, 8]),
        ("(reduce + 0 (range 1 11))",                 55),
        ("(-> 5 inc inc dec)",                        6),
        ("(->> [1 2 3 4] (map inc) (filter even?))",  [2, 4]),
        ("(quot 10 3)",                               3),
        ("(rem 10 3)",                                1),
        ("(count [1 2 3 4 5])",                       5),
        ("(first [10 20 30])",                        10),
        ("(rest [1 2 3])",                            [2, 3]),
        ("(get {:a 1 :b 2} :a)",                      1),
        ("(assoc {:a 1} :b 2)",                       {("__kw__", "a"): 1, ("__kw__", "b"): 2}),
    ]
    ok = 0
    for src, expected in cases:
        try:
            ast = parse(src)
        except Exception as e:
            if isinstance(expected, type) and issubclass(expected, Exception):
                ok += 1
                continue
            raise AssertionError(f"parse fail {src!r}: {e}") from e
        if isinstance(expected, type) and issubclass(expected, Exception):
            # We expected this to raise — parsing succeeded, so eval
            # must raise instead.
            try:
                evaluate(ast)
            except Exception:
                ok += 1
                continue
            raise AssertionError(f"expected error for {src!r}, got {evaluate(ast)}")
        got = evaluate(ast)
        if got != expected:
            raise AssertionError(f"{src!r}: got {got!r}, want {expected!r}")
        ok += 1
    print(f"form_parser.py smoke_test: ok ({ok}/{len(cases)})")


if __name__ == "__main__":
    smoke_test()
