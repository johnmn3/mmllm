"""Parametric form-template families for the K-12 Clojure curriculum.

Each family is a small factory: returning `(form_template, slots,
expected_fn)`. Per-fable grade files call these to populate
SubjectExample.form_template / .slots / .expected_fn so the same form
shape can be re-used across fables with the same scalar-pool draw
behavior.

The families cover the canonical pedagogical subset (see
form_parser.py). Anything outside this subset (macros, host interop,
deftype, etc.) belongs in the bb-verify path, not here.

Design contract:
  • slots is a dict from slot-name → either a pool name (str) or a
    Slot dataclass (see scalar_pools.py)
  • expected_fn(draws) → the value evaluating the rendered form
    must produce; verified by form_parser.parse + expr.evaluate
  • Every family is named after the pedagogical operation it
    teaches, not the pool it draws from
"""
from __future__ import annotations

from typing import Any, Callable
from fractions import Fraction

from mmllm.aesop.curriculum.scalar_pools import Slot


# ─────────────────────── atom literals ───────────────────────


def atom_int_small():
    """A small int literal. Form is just the literal; expected is the
    same int. Used for grade-1 atom subjects."""
    return ("{n}",
            {"n": "INT_SMALL"},
            lambda d: d["n"])


def atom_int_negative():
    return ("{n}",
            {"n": "INT_NEG"},
            lambda d: d["n"])


def atom_int_large():
    return ("{n}",
            {"n": "INT_LARGE"},
            lambda d: d["n"])


def atom_int_bigint():
    return ("{n}",
            {"n": "INT_BIGINT"},
            lambda d: d["n"])


def atom_zero():
    return ("0", {}, lambda d: 0)


def atom_keyword(theme: str = "fruit"):
    pool = {"fruit":   "KW_FRUIT",
            "animal":  "KW_ANIMAL",
            "color":   "KW_COLOR",
            "tool":    "KW_TOOL",
            "generic": "KW_GENERIC"}[theme]
    return ("{k}", {"k": pool}, lambda d: d["k"])


def atom_string():
    return ("{s}",
            {"s": "STR_SHORT"},
            lambda d: d["s"])


def atom_bool():
    return ("{b}",
            {"b": "BOOL"},
            lambda d: d["b"])


def atom_nil():
    return ("nil", {}, lambda d: None)


# ─────────────────────── arithmetic ───────────────────────


def add_two():
    return ("(+ {a} {b})",
            {"a": "INT_SMALL", "b": "INT_SMALL"},
            lambda d: d["a"] + d["b"])


def add_three():
    return ("(+ {a} {b} {c})",
            {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_SMALL"},
            lambda d: d["a"] + d["b"] + d["c"])


def add_many():
    """Sum of 4-6 small ints."""
    return ("(+ {a} {b} {c} {d} {e})",
            {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_SMALL",
             "d": "INT_SMALL", "e": "INT_SMALL"},
            lambda d: d["a"] + d["b"] + d["c"] + d["d"] + d["e"])


def sub_two():
    """Subtraction with a >= b so result stays non-negative."""
    return ("(- {a} {b})",
            {"a": "INT_MEDIUM",
             "b": Slot(pool="INT_SMALL",
                       constraint=lambda v, dd: v <= dd.get("a", 999),
                       depends_on=("a",))},
            lambda d: d["a"] - d["b"])


def sub_three():
    return ("(- {a} {b} {c})",
            {"a": "INT_MEDIUM",
             "b": "INT_SMALL", "c": "INT_SMALL"},
            lambda d: d["a"] - d["b"] - d["c"])


def mul_two():
    return ("(* {a} {b})",
            {"a": "INT_SMALL", "b": "INT_SMALL"},
            lambda d: d["a"] * d["b"])


def mul_three():
    return ("(* {a} {b} {c})",
            {"a": "INT_TINY", "b": "INT_TINY", "c": "INT_TINY"},
            lambda d: d["a"] * d["b"] * d["c"])


def quot_clean():
    """Integer division producing a clean integer (a is a multiple of b)."""
    return ("(quot {a} {b})",
            {"b": Slot(pool="INT_SMALL",
                       constraint=lambda v, _: v != 0),
             "a": Slot(pool="INT_MEDIUM",
                       constraint=lambda v, dd: v % dd["b"] == 0,
                       depends_on=("b",))},
            lambda d: d["a"] // d["b"])


def rem_op():
    """Remainder with a > b so result is non-negative."""
    return ("(rem {a} {b})",
            {"b": Slot(pool="INT_SMALL",
                       constraint=lambda v, _: v != 0),
             "a": Slot(pool="INT_MEDIUM",
                       constraint=lambda v, dd: v >= dd["b"],
                       depends_on=("b",))},
            lambda d: d["a"] - (abs(d["a"]) // abs(d["b"])) * d["b"]
                      if d["a"] >= 0
                      else -(abs(d["a"]) % abs(d["b"])))


def mod_op():
    return ("(mod {a} {b})",
            {"b": Slot(pool="INT_SMALL",
                       constraint=lambda v, _: v != 0),
             "a": "INT_MEDIUM"},
            lambda d: d["a"] % d["b"])


def div_ratio():
    """Integer / Integer producing a Fraction (Clojure ratio).
    Choose a / b where they don't divide cleanly, so the result is
    a non-trivial ratio."""
    return ("(/ {a} {b})",
            {"b": Slot(pool="INT_SMALL",
                       constraint=lambda v, _: v > 1),
             "a": Slot(pool="INT_SMALL",
                       constraint=lambda v, dd: v % dd["b"] != 0,
                       depends_on=("b",))},
            lambda d: Fraction(d["a"], d["b"]))


def inc_op():
    return ("(inc {n})",
            {"n": "INT_SMALL"},
            lambda d: d["n"] + 1)


def dec_op():
    return ("(dec {n})",
            {"n": "INT_SMALL"},
            lambda d: d["n"] - 1)


def abs_op():
    return ("(abs {n})",
            {"n": "INT_NEG"},
            lambda d: abs(d["n"]))


def min_three():
    return ("(min {a} {b} {c})",
            {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_SMALL"},
            lambda d: min(d["a"], d["b"], d["c"]))


def max_three():
    return ("(max {a} {b} {c})",
            {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_SMALL"},
            lambda d: max(d["a"], d["b"], d["c"]))


# ─────────────────────── predicates ───────────────────────


def lt_chain_3():
    """(< a b c) where a < b < c so it's true."""
    return ("(< {a} {b} {c})",
            {"a": "INT_SMALL",
             "b": Slot(pool="INT_MEDIUM",
                       constraint=lambda v, dd: v > dd["a"],
                       depends_on=("a",)),
             "c": Slot(pool="INT_LARGE",
                       constraint=lambda v, dd: v > dd["b"],
                       depends_on=("b",))},
            lambda d: True)


def gt_chain_3():
    return ("(> {c} {b} {a})",
            {"a": "INT_SMALL",
             "b": Slot(pool="INT_MEDIUM",
                       constraint=lambda v, dd: v > dd["a"],
                       depends_on=("a",)),
             "c": Slot(pool="INT_LARGE",
                       constraint=lambda v, dd: v > dd["b"],
                       depends_on=("b",))},
            lambda d: True)


def eq_two_int():
    """Equality where the values may or may not match. Two
    independent draws — usually unequal but we don't constrain."""
    return ("(= {a} {b})",
            {"a": "INT_SMALL", "b": "INT_SMALL"},
            lambda d: d["a"] == d["b"])


def eq_two_int_match():
    """Both args are the same drawn value (so it's true)."""
    return ("(= {a} {a})",
            {"a": "INT_SMALL"},
            lambda d: True)


def zero_p():
    return ("(zero? {n})",
            {"n": "INT_SMALL"},
            lambda d: d["n"] == 0)


def pos_p():
    return ("(pos? {n})",
            {"n": "INT_SMALL_NZ"},
            lambda d: d["n"] > 0)


def neg_p():
    return ("(neg? {n})",
            {"n": "INT_SMALL_NZ"},
            lambda d: d["n"] < 0)


def odd_p():
    return ("(odd? {n})",
            {"n": "INT_SMALL"},
            lambda d: d["n"] % 2 != 0)


def even_p():
    return ("(even? {n})",
            {"n": "INT_SMALL"},
            lambda d: d["n"] % 2 == 0)


# ─────────────────────── logic ───────────────────────


def and_two():
    return ("(and {a} {b})",
            {"a": "BOOL", "b": "BOOL"},
            lambda d: d["a"] and d["b"])


def or_two():
    return ("(or {a} {b})",
            {"a": "BOOL", "b": "BOOL"},
            lambda d: d["a"] or d["b"])


def not_op():
    return ("(not {a})",
            {"a": "BOOL"},
            lambda d: not d["a"])


# ─────────────────────── conditionals ───────────────────────


def if_pos_branch():
    """(if (pos? n) :positive :nonpositive) — both branches keyword."""
    def expected(d):
        return ("__kw__", "positive") if d["n"] > 0 else ("__kw__", "nonpositive")
    return ("(if (pos? {n}) :positive :nonpositive)",
            {"n": "INT_SMALL_NZ"},
            expected)


def if_eq_branch():
    """(if (= a b) :match :differ)."""
    def expected(d):
        return ("__kw__", "match") if d["a"] == d["b"] else ("__kw__", "differ")
    return ("(if (= {a} {b}) :match :differ)",
            {"a": "INT_TINY", "b": "INT_TINY"},
            expected)


def when_pos():
    """(when (pos? n) n) — yields n or nil."""
    return ("(when (pos? {n}) {n})",
            {"n": "INT_SMALL_NZ"},
            lambda d: d["n"] if d["n"] > 0 else None)


def cond_three_arms():
    """(cond (pos? n) :positive (neg? n) :negative :else :zero)."""
    def expected(d):
        n = d["n"]
        if n > 0:  return ("__kw__", "positive")
        if n < 0:  return ("__kw__", "negative")
        return ("__kw__", "zero")
    return ("(cond (pos? {n}) :positive (neg? {n}) :negative :else :zero)",
            {"n": "INT_SMALL"},
            expected)


# ─────────────────────── let / fn ───────────────────────


def let_one_binding():
    """(let [x N] (* x x)) — binding then square."""
    return ("(let [x {a}] (* x x))",
            {"a": "INT_SMALL"},
            lambda d: d["a"] * d["a"])


def let_two_bindings_sum():
    """(let [a A b B] (+ a b))."""
    return ("(let [a {a} b {b}] (+ a b))",
            {"a": "INT_SMALL", "b": "INT_SMALL"},
            lambda d: d["a"] + d["b"])


def let_chain():
    """(let [a A b (* a 2)] b) — second binding uses first."""
    return ("(let [a {a} b (* a 2)] b)",
            {"a": "INT_SMALL"},
            lambda d: d["a"] * 2)


def fn_iife_square():
    """((fn [x] (* x x)) N)."""
    return ("((fn [x] (* x x)) {a})",
            {"a": "INT_SMALL"},
            lambda d: d["a"] * d["a"])


def fn_iife_add():
    return ("((fn [a b] (+ a b)) {a} {b})",
            {"a": "INT_SMALL", "b": "INT_SMALL"},
            lambda d: d["a"] + d["b"])


def defn_then_call_double():
    """(do (defn dbl [x] (* x 2)) (dbl N))."""
    return ("(do (defn dbl [x] (* x 2)) (dbl {a}))",
            {"a": "INT_SMALL"},
            lambda d: d["a"] * 2)


# ─────────────────────── threading ───────────────────────


def thread_first_inc_dec():
    """(-> N inc inc dec)."""
    return ("(-> {a} inc inc dec)",
            {"a": "INT_SMALL"},
            lambda d: d["a"] + 1)


def thread_first_arith():
    """(-> N (+ A) (* B))."""
    return ("(-> {a} (+ {b}) (* {c}))",
            {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_TINY"},
            lambda d: (d["a"] + d["b"]) * d["c"])


def thread_last_pipeline():
    """(->> coll (map inc) (filter even?) count)."""
    return ("(->> {coll} (map inc) (filter even?) count)",
            {"coll": "COLL_INT_SHORT"},
            lambda d: sum(1 for x in d["coll"] if (x + 1) % 2 == 0))


# ─────────────────────── sequence ops ───────────────────────


def count_coll():
    return ("(count {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: len(d["coll"]))


def first_coll():
    return ("(first {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: d["coll"][0] if d["coll"] else None)


def last_coll():
    return ("(last {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: d["coll"][-1] if d["coll"] else None)


def rest_coll():
    return ("(rest {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: list(d["coll"][1:]))


def nth_coll():
    """(nth coll i) where 0 <= i < len(coll)."""
    return ("(nth {coll} {i})",
            {"coll": "COLL_INT_MED",
             "i": Slot(pool="INT_TINY",
                       constraint=lambda v, dd: v < len(dd["coll"]),
                       depends_on=("coll",))},
            lambda d: d["coll"][d["i"]])


def conj_int():
    return ("(conj {coll} {x})",
            {"coll": "COLL_INT_SHORT", "x": "INT_SMALL"},
            lambda d: list(d["coll"]) + [d["x"]])


def reverse_coll():
    return ("(reverse {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: list(reversed(d["coll"])))


def sort_coll():
    return ("(sort {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: sorted(d["coll"]))


def distinct_coll():
    return ("(distinct {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: list(dict.fromkeys(d["coll"])))


# ─────────────────────── HOFs ───────────────────────


def map_inc():
    return ("(map inc {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: [x + 1 for x in d["coll"]])


def map_double():
    return ("(map (fn [x] (* x 2)) {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: [x * 2 for x in d["coll"]])


def filter_even():
    return ("(filter even? {coll})",
            {"coll": "COLL_INT_MED"},
            lambda d: [x for x in d["coll"] if x % 2 == 0])


def filter_pos():
    return ("(filter pos? {coll})",
            {"coll": "COLL_INT_MED"},
            lambda d: [x for x in d["coll"] if x > 0])


def reduce_sum():
    return ("(reduce + {coll})",
            {"coll": "COLL_INT_SHORT"},
            lambda d: sum(d["coll"]))


def reduce_sum_init():
    return ("(reduce + {init} {coll})",
            {"init": "INT_SMALL", "coll": "COLL_INT_SHORT"},
            lambda d: d["init"] + sum(d["coll"]))


def reduce_max():
    return ("(reduce max {coll})",
            {"coll": "COLL_INT_MED"},
            lambda d: max(d["coll"]))


def reduce_product():
    return ("(reduce * {coll})",
            {"coll": "COLL_INT_UNIQUE_SHORT"},
            lambda d: _product(d["coll"]))


def _product(xs):
    out = 1
    for x in xs:
        out *= x
    return out


# ─────────────────────── maps ───────────────────────


def get_kw_int():
    """(get m :k) where m is keyword→int and :k is in m."""
    def expected(d):
        return d["m"][d["k"]]

    return ("(get {m} {k})",
            {"m": "MAP_FRUIT_INT",
             "k": Slot(pool="KW_FRUIT",
                       constraint=lambda v, dd: v in dd["m"],
                       depends_on=("m",))},
            expected)


def kw_as_lookup():
    """(:k m) — keyword as fn, look up its own value."""
    def expected(d):
        return d["m"][d["k"]]

    return ("({k} {m})",
            {"m": "MAP_FRUIT_INT",
             "k": Slot(pool="KW_FRUIT",
                       constraint=lambda v, dd: v in dd["m"],
                       depends_on=("m",))},
            expected)


def assoc_kw_int():
    def expected(d):
        m2 = dict(d["m"])
        m2[d["k"]] = d["v"]
        return m2

    return ("(assoc {m} {k} {v})",
            {"m": "MAP_FRUIT_INT", "k": "KW_FRUIT", "v": "INT_SMALL"},
            expected)


def keys_op():
    return ("(keys {m})",
            {"m": "MAP_FRUIT_INT"},
            lambda d: list(d["m"].keys()))


def vals_op():
    return ("(vals {m})",
            {"m": "MAP_FRUIT_INT"},
            lambda d: list(d["m"].values()))


def contains_kw():
    """(contains? m :k) — :k may or may not be in m."""
    return ("(contains? {m} {k})",
            {"m": "MAP_FRUIT_INT", "k": "KW_FRUIT"},
            lambda d: d["k"] in d["m"])


# ─────────────────────── strings ───────────────────────


def str_concat_two():
    """(str S1 S2)."""
    return ("(str {a} {b})",
            {"a": "STR_SHORT", "b": "STR_SHORT"},
            lambda d: d["a"] + d["b"])


def str_count():
    """(count S)."""
    return ("(count {s})",
            {"s": "STR_SHORT"},
            lambda d: len(d["s"]))


def str_upper():
    return ("(clojure.string/upper-case {s})",
            {"s": "STR_SHORT"},
            lambda d: d["s"].upper())


def str_lower():
    return ("(clojure.string/lower-case {s})",
            {"s": "STR_GREETING"},
            lambda d: d["s"].lower())


def string_p_str():
    return ("(string? {s})",
            {"s": "STR_SHORT"},
            lambda d: True)


# ─────────────────────── type predicates ───────────────────────


def nil_p_nil():
    return ("(nil? nil)", {}, lambda d: True)


def keyword_p_kw():
    return ("(keyword? {k})",
            {"k": "KW_FRUIT"},
            lambda d: True)


def number_p_int():
    return ("(number? {n})",
            {"n": "INT_SMALL"},
            lambda d: True)


# ─────────────────────── try / catch ───────────────────────


def try_div_by_zero():
    """(try (/ a 0) (catch ArithmeticException e :error))."""
    return ("(try (/ {a} 0) (catch ArithmeticException e :error))",
            {"a": "INT_SMALL_NZ"},
            lambda d: ("__kw__", "error"))


# ─────────────────────── registry ───────────────────────


FAMILIES: dict[str, Callable[[], tuple]] = {
    f.__name__: f for f in [
        atom_int_small, atom_int_negative, atom_int_large, atom_int_bigint,
        atom_zero, atom_keyword, atom_string, atom_bool, atom_nil,
        add_two, add_three, add_many, sub_two, sub_three,
        mul_two, mul_three, quot_clean, rem_op, mod_op, div_ratio,
        inc_op, dec_op, abs_op, min_three, max_three,
        lt_chain_3, gt_chain_3, eq_two_int, eq_two_int_match,
        zero_p, pos_p, neg_p, odd_p, even_p,
        and_two, or_two, not_op,
        if_pos_branch, if_eq_branch, when_pos, cond_three_arms,
        let_one_binding, let_two_bindings_sum, let_chain,
        fn_iife_square, fn_iife_add, defn_then_call_double,
        thread_first_inc_dec, thread_first_arith, thread_last_pipeline,
        count_coll, first_coll, last_coll, rest_coll, nth_coll,
        conj_int, reverse_coll, sort_coll, distinct_coll,
        map_inc, map_double, filter_even, filter_pos,
        reduce_sum, reduce_sum_init, reduce_max, reduce_product,
        get_kw_int, kw_as_lookup, assoc_kw_int, keys_op, vals_op, contains_kw,
        str_concat_two, str_count, str_upper, str_lower,
        nil_p_nil, keyword_p_kw, number_p_int, string_p_str,
        try_div_by_zero,
    ]
}


# ─────────────────────── self-test: every family parses + verifies ─────────


def smoke_test() -> None:
    """For each family, draw with a fixed seed and confirm:
       1. Form parses cleanly
       2. Evaluator answer == expected_fn(draws)
    Ensures the families library doesn't have silent mismatches.
    """
    import random
    from mmllm.aesop.curriculum.scalar_pools import render_form
    from mmllm.aesop.curriculum.form_parser import parse
    from mmllm.aesop.expr import evaluate

    rng = random.Random(0)
    fails = []
    for name, factory in FAMILIES.items():
        template, slots, expected_fn = factory()
        for trial in range(5):  # 5 draws each to catch random mismatches
            try:
                form_str, draws = render_form(template, slots, rng)
                ast = parse(form_str)
                got = evaluate(ast)
                want = expected_fn(draws)
                if got != want:
                    fails.append(
                        f"{name} trial {trial}: form={form_str!r} "
                        f"got={got!r} want={want!r}")
            except Exception as e:
                fails.append(f"{name} trial {trial}: exception {e!r}")
    if fails:
        print(f"FAILED: {len(fails)} family-trials failed")
        for f in fails[:20]:
            print(f"  {f}")
        raise AssertionError(f"{len(fails)} family-trial failures")
    print(f"form_families.py smoke_test: ok "
          f"({len(FAMILIES)} families × 5 trials = {len(FAMILIES) * 5} verified)")


if __name__ == "__main__":
    smoke_test()
