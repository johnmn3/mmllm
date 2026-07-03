"""Golden-vector dumper for the JVM port (M0, docs/jvm-port-spec.md §4/§12).
ADDITIVE tooling — read-only use of the torch/Basilisp reference.

Writes reproducible parity fixtures under jvm/goldens/ (gitignored — they
regenerate in ~a minute; only the scripts and the manifest are committed):

  meta.json            env snapshot + seeds + tolerances
  dense.npz            the seed-0 fresh sym24 dense params (positional keys
                       d00000.. matching arch-sym24.manifest.json)
  banks/*.bin          every Local V / V_net in the NATIVE raw layout the JVM
                       bank_store maps directly (fp32 row-major, headerless)
  rmsnorm.npz rope.npz sdpa.npz swiglu.npz pkm.npz netbank.npz gate.npz
                       per-module (inputs, outputs) pairs
  full_forward.npz     tokens (B=1,T=64) -> logits + bpc, eval mode

Determinism choices (mirror on the JVM side):
  - MMLLM_DISABLE_PKM_CPP=true — the C++ fused kernel is bit-exact vs the
    Python path EXCEPT top-k tie ordering; goldens pin the Python semantics.
  - eval() mode everywhere: SwitchGate net-default takes the smooth
    expected-value branch (gating.py:227-237), no Bernoulli draws, no
    z-loss/telemetry side effects.
  - NetBank simulated delay env'd to 0 (it wouldn't affect values, only wall).

Run:  .venv/bin/python scripts/dump_goldens.py [--out jvm/goldens]
"""
from __future__ import annotations

import argparse
import json
import math
import os

os.environ.setdefault("MMLLM_DISABLE_PKM_CPP", "true")

from jvm_bridge import SYM24_ENV, build_model  # noqa: E402


def set_eval(m, K):
    import torch.nn as nn
    mods = [m.get(K("tok-emb")), m.get(K("norm-final"))]
    for b in m.get(K("blocks")):
        for key in ["norm1", "norm2", "q-proj", "k-proj-s", "v-proj-s",
                    "k-proj-l", "v-proj-l", "o-proj", "gate-proj", "up-proj",
                    "down-proj", "bank-query", "bank-feedback", "memory",
                    "netbank", "long-gate", "carry"]:
            mods.append(b.get(K(key)))
    for mod in mods:
        if isinstance(mod, nn.Module):
            mod.eval()


def _np(t):
    return t.detach().cpu().numpy()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="jvm/goldens")
    args = ap.parse_args()

    import numpy as np
    import torch
    import torch.nn.functional as F

    m, K, var = build_model()
    set_eval(m, K)
    blocks = list(m.get(K("blocks")))
    b0 = blocks[0]
    os.makedirs(os.path.join(args.out, "banks"), exist_ok=True)

    g = torch.Generator().manual_seed(1234)

    def rand(*shape, scale=1.0):
        return torch.randn(*shape, generator=g) * scale

    # ── dense params (positional, matches manifest) ──
    params = list(var("parameters")(m))
    np.savez(os.path.join(args.out, "dense.npz"),
             **{f"d{i:05d}": _np(p) for i, p in enumerate(params)})

    # ── banks in native raw layout ──
    for i, b in enumerate(blocks):
        mem = b.get(K("memory"))
        if mem is not None:
            _np(mem.V.weight).astype(np.float32).tofile(
                os.path.join(args.out, "banks", f"bank-latest.{i}.bin"))
        nb = b.get(K("netbank"))
        if nb is not None:
            _np(nb.V.weight).astype(np.float32).tofile(
                os.path.join(args.out, "banks", f"V_net.{i}.bin"))

    # ── rmsnorm (block-0 norm1) ──
    x = rand(2, 7, 32)
    with torch.no_grad():
        y = b0.get(K("norm1"))(x)
    np.savez(os.path.join(args.out, "rmsnorm.npz"), x=_np(x), y=_np(y),
             w=_np(b0.get(K("norm1")).weight))

    # ── rope (short-tier semantics: cos/sin slice at position offset 3) ──
    from mmllm.attention_kernel import apply_rope
    rope_cos, rope_sin = m.get(K("rope-cos")), m.get(K("rope-sin"))
    q = rand(1, 2, 5, 8)
    cos, sin = rope_cos.narrow(0, 3, 5), rope_sin.narrow(0, 3, 5)
    with torch.no_grad():
        yq = apply_rope(q, cos, sin)
    np.savez(os.path.join(args.out, "rope.npz"), q=_np(q), pos_offset=3,
             y=_np(yq), cos=_np(rope_cos), sin=_np(rope_sin))

    # ── causal SDPA ──
    qq, kk, vv = rand(1, 2, 16, 8), rand(1, 2, 16, 8), rand(1, 2, 16, 8)
    with torch.no_grad():
        o = F.scaled_dot_product_attention(qq, kk, vv, is_causal=True)
    np.savez(os.path.join(args.out, "sdpa.npz"),
             q=_np(qq), k=_np(kk), v=_np(vv), y=_np(o))

    # ── SwiGLU FFN (block-0 weights) ──
    x = rand(2, 5, 32)
    gate_p, up_p, down_p = (b0.get(K(k)) for k in
                            ["gate-proj", "up-proj", "down-proj"])
    with torch.no_grad():
        y = down_p(F.silu(gate_p(x)) * up_p(x))
    np.savez(os.path.join(args.out, "swiglu.npz"), x=_np(x), y=_np(y))

    # ── Local PKM (block-0 memory, router 0 and router 3) ──
    mem = b0.get(K("memory"))
    qb = rand(2, 4, 16, scale=0.5)
    tid = torch.tensor([0, 3], dtype=torch.long)
    with torch.no_grad():
        y = mem(qb, trunk_ids=tid)
    np.savez(os.path.join(args.out, "pkm.npz"), q=_np(qb),
             trunk_ids=_np(tid), y=_np(y))

    # ── NetBank (block-0) ──
    nb = b0.get(K("netbank"))
    qn = rand(1, 4, 16, scale=0.5)
    with torch.no_grad():
        yn = nb(qn)
    np.savez(os.path.join(args.out, "netbank.npz"), q=_np(qn), y=_np(yn))

    # ── SwitchGate 3-way + alpha_net + net-default (eval path) ──
    gate = b0.get(K("long-gate"))
    # zero-init gate params make the golden degenerate (uniform mix) — nudge
    # them to exercise the softmax/sigmoid paths, then restore.
    saved = {n: p.detach().clone() for n, p in gate.named_parameters()}
    with torch.no_grad():
        for _, p in gate.named_parameters():
            p.add_(rand(*p.shape, scale=0.3))
        ql, sd, me, ne = (rand(1, 2, 6, 8) for _ in range(4))
        yg = gate(ql, sd, me, ne)
    np.savez(os.path.join(args.out, "gate.npz"), q=_np(ql), sdpa=_np(sd),
             mem=_np(me), net=_np(ne), y=_np(yg),
             **{f"p_{n}": _np(p) for n, p in gate.named_parameters()})
    with torch.no_grad():
        for n, p in gate.named_parameters():
            p.copy_(saved[n])

    # ── full forward, eval mode, B=1 T=64, all 16 routers' trunk_id=0 row ──
    forward = var("forward")
    tokens = torch.randint(0, 256, (1, 64), generator=g)
    tid1 = torch.tensor([0], dtype=torch.long)
    with torch.no_grad():
        out = forward(m, tokens, None, None, False, tid1)
        # forward returns a Basilisp persistent vector [logits ...] — not a
        # Python list/tuple, so unwrap by iterating.
        logits = out if torch.is_tensor(out) else next(iter(out))
    y_next = tokens[:, 1:]
    ce = F.cross_entropy(
        logits[:, :-1].reshape(-1, 256), y_next.reshape(-1))
    bpc = ce.item() / math.log(2)
    np.savez(os.path.join(args.out, "full_forward.npz"), tokens=_np(tokens),
             trunk_ids=_np(tid1), logits=_np(logits), bpc=bpc)
    print(f"full-forward bpc = {bpc:.4f}  logits {tuple(logits.shape)}")

    meta = {
        "env": {k: os.environ[k] for k in sorted(SYM24_ENV)},
        "pkm_cpp_disabled": True,
        "seed_model": 0, "seed_inputs": 1234,
        "tolerances": {"module_fwd_rel": 1e-5, "full_fwd_abs": 1e-4},
        "torch_version": torch.__version__,
    }
    with open(os.path.join(args.out, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)
    print(f"goldens written to {args.out}/")


if __name__ == "__main__":
    main()
