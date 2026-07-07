"""JVM-port bridge (M0 of docs/jvm-port-spec.md). ADDITIVE tooling only —
imports the torch/Basilisp reference read-only; touches no training path.

The positional dense.pt contract (core.lpy `parameters`, line ~2181) is the
compatibility cliff for any second backend: a JVM bird that emits the wrong
tensor count/order is silently dropped at harvest. This script makes that
contract *inspectable data*:

  manifest   build the sym24 model (prod-recipe env), walk it by NAME in the
             exact order `(parameters m)` uses, and verify the two walks agree
             tensor-by-tensor (by Python identity). Emits:
               - jvm/resources/arch-sym24.manifest.json  (machine)
               - jvm/resources/arch-sym24.edn            (JVM side reads this)
  to-npz     dense.pt -> .npz (+ manifest copy) for the JVM side to load.
  from-npz   .npz -> dense.pt (torch.save'd positional list) — the reverse
             direction a JVM bird uses to emit harvest-compatible ckpts.
  verify     dense.pt -> npz -> dense.pt round-trip; per-tensor BITWISE
             equality (torch.equal + dtype + shape). Zip-container bytes are
             not compared (torch.save archives embed non-deterministic
             metadata); tensor payloads are what FedAvg reads.

Run inside the repo venv:  .venv/bin/python scripts/jvm_bridge.py manifest
"""
from __future__ import annotations

import argparse
import json
import os
import sys


# ── sym24 prod-recipe environment ──
# Mirrors chain_meta.json (authoritative arch) + extend_chain.sh defaults.
# Same set mlx/parity.py uses for MLX_PARITY_PROD, plus the sym24 layer set
# and local sqrt_n. Applied BEFORE mmllm.core import (pick-* fns read env at
# build time).
SYM24_ENV = {
    "MMLLM_DEVICE": "cpu",
    "MMLLM_NETBANK_ENABLED": "true",
    "MMLLM_LONG_TIER_MIX": "switch",
    "MMLLM_ALPHA_NET": "true",
    "MMLLM_GATE_NET_DEFAULT": "true",
    "MMLLM_N_TRUNKS": "16",
    "MMLLM_NETBANK_SHARED": "false",
    "MMLLM_NET_SQRT_N": "1024",
    "MMLLM_NET_C_NET": "8",
    "MMLLM_NET_TOP_K": "512",
    "MMLLM_NET_SUB_TOP_K": "24",
    "MMLLM_MEMORY_TOP_K": "128",
    "MMLLM_MEMORY_SUB_TOP_K": "24",
    "MMLLM_SQRT_N": "128",
    "MMLLM_LOCAL_BANK_LAYERS": ",".join(str(i) for i in range(24)),
    "MMLLM_NETBANK_DELAY_MS_MIN": "0",
    "MMLLM_NETBANK_DELAY_MS_MAX": "0",
    # K_a/K_b two-group dense optimizer (c0449a3: extend_chain.sh prod
    # defaults) — kab-mult != dense-mult makes make-opt-dense put every
    # block's memory.K_a/K_b into AdamW group 1 with its own lr schedule.
    # Optimizer grouping only; does NOT affect arch/tensor count (698).
    "MMLLM_LR_KAB_MULT": "0.15",
    "MMLLM_LR_KAB_MULT_END": "0.001",
    # keep the manifest build off any mmap files / GPU
    "MMLLM_BANK_ON_GPU": "true",
}


def _apply_env():
    for k, v in SYM24_ENV.items():
        os.environ.setdefault(k, v)


def build_model():
    """Build the sym24 cpu-mini model via the Basilisp reference and return
    (model_map, K, var) accessors — same bootstrap as mlx/parity.py."""
    _apply_env()
    import basilisp.main
    basilisp.main.init()
    import mmllm.core  # noqa: F401 — registers the namespace
    import basilisp.lang.runtime as rt
    from basilisp.lang import keyword as kw, symbol as sym
    import torch

    K = kw.keyword

    def var(n):
        return rt.Var.find(sym.symbol(n, ns="mmllm.core")).value

    torch.manual_seed(0)
    cfg = var("default-config-cpu-mini")
    m = var("build-model")(cfg)
    return m, K, var


def named_dense_walk(m, K):
    """(name, param) pairs in the EXACT order core.lpy `parameters` emits.

    This mirrors core.lpy:2181 clause by clause. `manifest` cross-checks the
    result against the real `(parameters m)` by identity, so if the reference
    ordering ever changes, this walk fails loudly instead of drifting.
    """
    import torch.nn as nn

    out = []

    def add_module(prefix, mod):
        if mod is None:
            return
        for pname, p in mod.named_parameters():
            out.append((f"{prefix}.{pname}", p))

    blocks = list(m.get(K("blocks")))

    # 1. tok-emb
    add_module("tok_emb", m.get(K("tok-emb")))

    # 2. per-block CORE
    core_keys = ["norm1", "norm2", "q-proj", "k-proj-s", "v-proj-s",
                 "k-proj-l", "v-proj-l", "o-proj", "gate-proj", "up-proj",
                 "down-proj", "bank-query", "bank-feedback"]
    for i, b in enumerate(blocks):
        for key in core_keys:
            add_module(f"blocks.{i}.{key.replace('-', '_')}", b.get(K(key)))
        mem = b.get(K("memory"))
        if mem is not None:
            out.append((f"blocks.{i}.memory.K_a", mem.K_a))
            out.append((f"blocks.{i}.memory.K_b", mem.K_b))

    # 3. norm-final
    add_module("norm_final", m.get(K("norm-final")))

    # 4. mtp-head (optional)
    add_module("mtp_head", m.get(K("mtp-head")))

    # 5. per-block memory.q_norm (end-appended)
    for i, b in enumerate(blocks):
        mem = b.get(K("memory"))
        if mem is not None:
            out.append((f"blocks.{i}.memory.q_norm.weight", mem.q_norm.weight))

    # 6. per-block long-gate, minus late-attached attrs
    late = {"alpha_net", "local_active_proj", "local_active_bias"}
    for i, b in enumerate(blocks):
        gate = b.get(K("long-gate"))
        if gate is None:
            continue
        for pname, p in gate.named_parameters():
            if pname in late:
                continue
            out.append((f"blocks.{i}.long_gate.{pname}", p))

    # 7. per-block netbank dense, deduped by identity (NETBANK_SHARED=true)
    seen = set()
    nb_names = ["K_a", "K_b", "q_norm.weight", "expander.weight"]
    for i, b in enumerate(blocks):
        nb = b.get(K("netbank"))
        if nb is None:
            continue
        for name, p in zip(nb_names, nb.dense_parameters()):
            if id(p) in seen:
                continue
            seen.add(id(p))
            out.append((f"blocks.{i}.netbank.{name}", p))

    # 8. importance-head + per-block carry
    add_module("importance_head", m.get(K("importance-head")))
    for i, b in enumerate(blocks):
        add_module(f"blocks.{i}.carry", b.get(K("carry")))

    # 9. per-block alpha_net
    for i, b in enumerate(blocks):
        gate = b.get(K("long-gate"))
        a = getattr(gate, "alpha_net", None) if gate is not None else None
        if isinstance(a, nn.Parameter):
            out.append((f"blocks.{i}.long_gate.alpha_net", a))

    # 10. per-block local_active_proj + local_active_bias
    for i, b in enumerate(blocks):
        gate = b.get(K("long-gate"))
        if gate is None:
            continue
        lp = getattr(gate, "local_active_proj", None)
        lb = getattr(gate, "local_active_bias", None)
        if isinstance(lp, nn.Parameter):
            out.append((f"blocks.{i}.long_gate.local_active_proj", lp))
        if isinstance(lb, nn.Parameter):
            out.append((f"blocks.{i}.long_gate.local_active_bias", lb))

    # 11. delim-head (optional)
    add_module("delim_head", m.get(K("delim-head")))

    return out


def sparse_manifest(m, K):
    """Bank (non-dense.pt) tensors: per-layer V shapes + on-disk layout."""
    out = []
    for i, b in enumerate(m.get(K("blocks"))):
        mem = b.get(K("memory"))
        if mem is not None:
            out.append({
                "name": f"blocks.{i}.memory.V", "kind": "local",
                "layer": i, "shape": list(mem.V.weight.shape),
                "dtype": "float32", "n_trunks": mem.n_trunks,
                "sqrt_n": mem.sqrt_n, "q_dim": mem.q_dim,
                "top_k": mem.top_k, "sub_top_k": mem.sub_top_k,
                "file": f"bank-latest.{i}.bin",
            })
        nb = b.get(K("netbank"))
        if nb is not None:
            out.append({
                "name": f"blocks.{i}.netbank.V", "kind": "net",
                "layer": i, "shape": list(nb.V.weight.shape),
                "dtype": nb.dtype_str, "sqrt_n": nb.sqrt_n,
                "c_net": nb.c_net, "q_dim": nb.q_dim,
                "top_k": nb.top_k, "sub_top_k": nb.sub_top_k,
                "file": f"V_net.{i}.bin",
            })
    return out


def make_manifest():
    m, K, var = build_model()
    params = list(var("parameters")(m))
    named = named_dense_walk(m, K)

    if len(params) != len(named):
        raise SystemExit(
            f"FATAL: (parameters m) has {len(params)} tensors but the named "
            f"walk found {len(named)} — named_dense_walk no longer mirrors "
            f"core.lpy parameters. Fix the walk; do NOT ship this manifest."
        )
    for idx, (p, (name, q)) in enumerate(zip(params, named)):
        if p is not q:
            raise SystemExit(
                f"FATAL: positional mismatch at index {idx}: named walk says "
                f"{name} but (parameters m) has a different tensor there."
            )

    dense = [
        {"index": i, "name": name, "shape": list(p.shape),
         "dtype": str(p.dtype).replace("torch.", "")}
        for i, (name, p) in enumerate(named)
    ]
    manifest = {
        "arch": "sym24",
        "config_name": "cpu-mini",
        "env": {k: os.environ[k] for k in sorted(SYM24_ENV)},
        "n_dense_tensors": len(dense),
        "dense": dense,
        "sparse": sparse_manifest(m, K),
    }
    return manifest


def _edn_str(v):
    if isinstance(v, str):
        return json.dumps(v)
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return "[" + " ".join(_edn_str(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + " ".join(f":{k} {_edn_str(x)}" for k, x in v.items()) + "}"
    raise TypeError(type(v))


def cmd_manifest(args):
    manifest = make_manifest()
    os.makedirs(args.out_dir, exist_ok=True)
    jpath = os.path.join(args.out_dir, "arch-sym24.manifest.json")
    epath = os.path.join(args.out_dir, "arch-sym24.edn")
    with open(jpath, "w") as f:
        json.dump(manifest, f, indent=1)
    with open(epath, "w") as f:
        f.write(";; GENERATED by scripts/jvm_bridge.py manifest — do not edit.\n")
        f.write(";; Positional dense.pt contract for the sym24 chain "
                "(docs/jvm-port-spec.md §5).\n")
        f.write(_edn_str(manifest) + "\n")
    print(f"n_dense_tensors = {manifest['n_dense_tensors']}")
    print(f"n_sparse_banks  = {len(manifest['sparse'])}")
    print(f"wrote {jpath}")
    print(f"wrote {epath}")


def _load_dense_pt(path):
    import torch
    lst = torch.load(path, map_location="cpu", weights_only=True)
    if not isinstance(lst, list):
        raise SystemExit(f"{path} is not a positional list[Tensor] dense.pt")
    return lst


def cmd_to_npz(args):
    import numpy as np
    lst = _load_dense_pt(args.dense_pt)
    arrs = {}
    for i, t in enumerate(lst):
        a = t.detach().cpu().numpy()
        # fp16 etc. save natively; npy dtype records it
        arrs[f"d{i:05d}"] = a
    np.savez(args.out, **arrs)
    print(f"wrote {args.out} ({len(lst)} tensors)")


def cmd_from_npz(args):
    import numpy as np
    import torch
    z = np.load(args.npz)
    keys = sorted(z.files)
    lst = [torch.from_numpy(np.ascontiguousarray(z[k])) for k in keys]
    torch.save(lst, args.out)
    print(f"wrote {args.out} ({len(lst)} tensors)")


def cmd_verify(args):
    import numpy as np
    import torch
    lst = _load_dense_pt(args.dense_pt)
    tmp_npz = args.dense_pt + ".rt.npz"
    tmp_pt = args.dense_pt + ".rt.pt"
    ns = argparse.Namespace(dense_pt=args.dense_pt, out=tmp_npz)
    cmd_to_npz(ns)
    cmd_from_npz(argparse.Namespace(npz=tmp_npz, out=tmp_pt))
    back = _load_dense_pt(tmp_pt)
    assert len(lst) == len(back), f"count {len(lst)} != {len(back)}"
    for i, (a, b) in enumerate(zip(lst, back)):
        assert a.dtype == b.dtype, f"[{i}] dtype {a.dtype} != {b.dtype}"
        assert a.shape == b.shape, f"[{i}] shape {a.shape} != {b.shape}"
        assert torch.equal(a, b), f"[{i}] payload mismatch"
    os.unlink(tmp_npz)
    os.unlink(tmp_pt)
    print(f"round-trip OK: {len(lst)} tensors bitwise-equal")


def cmd_fresh_dense(args):
    """Emit a freshly-built sym24 dense.pt (seed 0) — a stand-in for a chain
    head when none is on disk, for round-trip and JVM-loader testing."""
    import torch
    m, K, var = build_model()
    params = [p.detach().clone() for p in var("parameters")(m)]
    torch.save(params, args.out)
    print(f"wrote {args.out} ({len(params)} tensors)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("manifest")
    p.add_argument("--out-dir", default="jvm/resources")
    p.set_defaults(fn=cmd_manifest)
    p = sub.add_parser("to-npz")
    p.add_argument("dense_pt")
    p.add_argument("out")
    p.set_defaults(fn=cmd_to_npz)
    p = sub.add_parser("from-npz")
    p.add_argument("npz")
    p.add_argument("out")
    p.set_defaults(fn=cmd_from_npz)
    p = sub.add_parser("verify")
    p.add_argument("dense_pt")
    p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("fresh-dense")
    p.add_argument("out")
    p.set_defaults(fn=cmd_fresh_dense)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
