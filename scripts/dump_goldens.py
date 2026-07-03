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

--grads mode (M4, spec §7/§12 gate G2) additionally writes gradient goldens
(train-mode modules, fixed seeds, loss = (out * r).sum() with a dumped
random r; every npz is self-contained — it carries the params it used):

  grads_rmsnorm.npz grads_linear.npz grads_silu.npz grads_swiglu.npz
  grads_sdpa.npz grads_rope.npz      per-module input+param grads
  grads_pkm.npz grads_netbank.npz    dq, dK_a, dK_b, dq_norm (+ d_expander
                                     for netbank), sparse dV as
                                     (dV_idx, dV_val) coalesced
  grads_gate.npz                     SwitchGate 3-way net-default TRAIN
                                     branch: torch.rand_like monkeypatched
                                     to replay a dumped R so the
                                     straight-through Bernoulli draw is
                                     reproducible on the JVM; all param
                                     grads + dq/dsdpa/dmem/dnet
  grads_tiedhead.npz                 tied emb: gather + output matmul accum
  grads_ce.npz                       CE grad wrt the full-forward logits

Determinism choices (mirror on the JVM side):
  - MMLLM_DISABLE_PKM_CPP=true — the C++ fused kernel is bit-exact vs the
    Python path EXCEPT top-k tie ordering; goldens pin the Python semantics.
  - eval() mode everywhere: SwitchGate net-default takes the smooth
    expected-value branch (gating.py:227-237), no Bernoulli draws, no
    z-loss/telemetry side effects.
  - NetBank simulated delay env'd to 0 (it wouldn't affect values, only wall).

Run:  .venv/bin/python scripts/dump_goldens.py [--out jvm/goldens]
      .venv/bin/python scripts/dump_goldens.py --grads   (forward goldens
      must exist first: grads_ce reads full_forward.npz)
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


def dump_grads(out_dir):
    """Gradient goldens (M4). Train-mode modules, fresh seed-0 model (same
    params as dense.npz / banks/*.bin), loss = (out * r).sum() per module."""
    import numpy as np
    import torch
    import torch.nn.functional as F

    m, K, var = build_model()          # train mode by default — no set_eval
    blocks = list(m.get(K("blocks")))
    b0 = blocks[0]
    mem = b0.get(K("memory"))
    nb = b0.get(K("netbank"))
    gate = b0.get(K("long-gate"))

    g = torch.Generator().manual_seed(20260703)

    def rand(*shape, scale=1.0):
        return torch.randn(*shape, generator=g) * scale

    def clear_grads():
        for p in var("parameters")(m):
            p.grad = None
        mem.V.weight.grad = None
        nb.V.weight.grad = None

    def save(name, **arrs):
        np.savez(os.path.join(out_dir, name + ".npz"), **arrs)

    # ── rmsnorm (block-0 norm1) ──
    norm1 = b0.get(K("norm1"))
    x = rand(2, 7, 32).requires_grad_(True)
    r = rand(2, 7, 32)
    y = norm1(x)
    clear_grads()
    (y * r).sum().backward()
    save("grads_rmsnorm", x=_np(x), r=_np(r), y=_np(y), w=_np(norm1.weight),
         dx=_np(x.grad), dw=_np(norm1.weight.grad))

    # ── linear (block-0 q_proj, bias-free) ──
    qp = b0.get(K("q-proj"))
    assert qp.bias is None, "q_proj grew a bias; grads_linear golden assumes none"
    x = rand(2, 5, 32).requires_grad_(True)
    r = rand(2, 5, 32)
    y = qp(x)
    clear_grads()
    (y * r).sum().backward()
    save("grads_linear", x=_np(x), r=_np(r), y=_np(y), W=_np(qp.weight),
         dx=_np(x.grad), dW=_np(qp.weight.grad))

    # ── silu (pure activation) ──
    x = rand(3, 4, 16).requires_grad_(True)
    r = rand(3, 4, 16)
    (F.silu(x) * r).sum().backward()
    save("grads_silu", x=_np(x), r=_np(r), dx=_np(x.grad))

    # ── swiglu (block-0 FFN weights) ──
    gate_p, up_p, down_p = (b0.get(K(k)) for k in
                            ["gate-proj", "up-proj", "down-proj"])
    x = rand(2, 5, 32).requires_grad_(True)
    r = rand(2, 5, 32)
    y = down_p(F.silu(gate_p(x)) * up_p(x))
    clear_grads()
    (y * r).sum().backward()
    save("grads_swiglu", x=_np(x), r=_np(r), y=_np(y),
         Wg=_np(gate_p.weight), Wu=_np(up_p.weight), Wd=_np(down_p.weight),
         dx=_np(x.grad), dWg=_np(gate_p.weight.grad),
         dWu=_np(up_p.weight.grad), dWd=_np(down_p.weight.grad))

    # ── causal SDPA ──
    qq = rand(1, 2, 16, 8).requires_grad_(True)
    kk = rand(1, 2, 16, 8).requires_grad_(True)
    vv = rand(1, 2, 16, 8).requires_grad_(True)
    r = rand(1, 2, 16, 8)
    o = F.scaled_dot_product_attention(qq, kk, vv, is_causal=True)
    (o * r).sum().backward()
    save("grads_sdpa", q=_np(qq), k=_np(kk), v=_np(vv), r=_np(r), y=_np(o),
         dq=_np(qq.grad), dk=_np(kk.grad), dv=_np(vv.grad))

    # ── rope (position offset 3, same slice semantics as rope.npz) ──
    from mmllm.attention_kernel import apply_rope
    rope_cos, rope_sin = m.get(K("rope-cos")), m.get(K("rope-sin"))
    q = rand(1, 2, 5, 8).requires_grad_(True)
    r = rand(1, 2, 5, 8)
    yq = apply_rope(q, rope_cos.narrow(0, 3, 5), rope_sin.narrow(0, 3, 5))
    (yq * r).sum().backward()
    save("grads_rope", q=_np(q), r=_np(r), pos_offset=3, y=_np(yq),
         dq=_np(q.grad))

    # ── Local PKM (block-0, train mode, routers 0 and 3) ──
    qb = rand(2, 4, 16, scale=0.5).requires_grad_(True)
    r = rand(2, 4, 16)
    tid = torch.tensor([0, 3], dtype=torch.long)
    y = mem(qb, trunk_ids=tid)
    clear_grads()
    (y * r).sum().backward()
    gV = mem.V.weight.grad.coalesce()
    save("grads_pkm", q=_np(qb), r=_np(r), trunk_ids=_np(tid), y=_np(y),
         Ka=_np(mem.K_a), Kb=_np(mem.K_b), qnorm_w=_np(mem.q_norm.weight),
         dq=_np(qb.grad), dKa=_np(mem.K_a.grad), dKb=_np(mem.K_b.grad),
         dqnorm_w=_np(mem.q_norm.weight.grad),
         dV_idx=_np(gV.indices()[0]), dV_val=_np(gV.values()))

    # ── NetBank (block-0, train mode) ──
    qn = rand(1, 4, 16, scale=0.5).requires_grad_(True)
    r = rand(1, 4, 16)
    y = nb(qn)
    clear_grads()
    (y * r).sum().backward()
    gV = nb.V.weight.grad.coalesce()
    save("grads_netbank", q=_np(qn), r=_np(r), y=_np(y),
         Ka=_np(nb.K_a), Kb=_np(nb.K_b), qnorm_w=_np(nb.q_norm.weight),
         expander_w=_np(nb.expander.weight),
         dq=_np(qn.grad), dKa=_np(nb.K_a.grad), dKb=_np(nb.K_b.grad),
         dqnorm_w=_np(nb.q_norm.weight.grad),
         dexpander=_np(nb.expander.weight.grad),
         dV_idx=_np(gV.indices()[0]), dV_val=_np(gV.values()))

    # ── SwitchGate 3-way net-default, TRAIN branch (ST-Bernoulli replay) ──
    # zero-init gate params make the golden degenerate — perturb, dump the
    # perturbed values with the golden, restore after. torch.rand_like is
    # monkeypatched to return the dumped R so the hard Bernoulli decision
    # (local_prob > R) is replayable bit-for-bit on the JVM.
    saved = {n: p.detach().clone() for n, p in gate.named_parameters()}
    with torch.no_grad():
        for _, p in gate.named_parameters():
            p.add_(rand(*p.shape, scale=0.3))
    R = torch.rand(1, 2, 6, generator=g)
    ql, sd, me, ne = (rand(1, 2, 6, 8).requires_grad_(True) for _ in range(4))
    r = rand(1, 2, 6, 8)
    orig_rand_like = torch.rand_like
    torch.rand_like = lambda t, **kw: R.clone().to(t.dtype)
    try:
        assert gate.training
        yg = gate(ql, sd, me, ne)
        clear_grads()
        (yg * r).sum().backward()
    finally:
        torch.rand_like = orig_rand_like
    assert gate.gate_proj.grad is None  # 2-way head unused on the 3-way path
    save("grads_gate", q=_np(ql), sdpa=_np(sd), mem=_np(me), net=_np(ne),
         R=_np(R), r=_np(r), y=_np(yg),
         dq=_np(ql.grad), dsdpa=_np(sd.grad), dmem=_np(me.grad),
         dnet=_np(ne.grad),
         dgate_proj_3=_np(gate.gate_proj_3.grad),
         dalpha_net=_np(gate.alpha_net.grad),
         dlap=_np(gate.local_active_proj.grad),
         dlab=_np(gate.local_active_bias.grad),
         **{f"p_{n}": _np(p) for n, p in gate.named_parameters()})
    with torch.no_grad():
        for n, p in gate.named_parameters():
            p.copy_(saved[n])

    # ── tied head: emb gather + weight-tied output matmul accumulation ──
    W = m.get(K("tok-emb")).weight.detach().clone().requires_grad_(True)
    toks = torch.randint(0, 256, (8,), generator=g)
    logits = W[toks] @ W.T
    r = rand(8, 256)
    (logits * r).sum().backward()
    save("grads_tiedhead", W=_np(W), tokens=_np(toks), r=_np(r),
         logits=_np(logits), dW=_np(W.grad))

    # ── CE from the full-forward golden logits ──
    ff_path = os.path.join(out_dir, "full_forward.npz")
    if not os.path.exists(ff_path):
        raise SystemExit("full_forward.npz missing — run without --grads first")
    ff = np.load(ff_path)
    lg = torch.from_numpy(ff["logits"]).clone().requires_grad_(True)
    toks = torch.from_numpy(ff["tokens"])
    ce = F.cross_entropy(lg[:, :-1].reshape(-1, 256), toks[:, 1:].reshape(-1))
    ce.backward()
    save("grads_ce", logits=ff["logits"], tokens=ff["tokens"],
         loss=float(ce.item()), dlogits=_np(lg.grad))

    print(f"grad goldens written to {out_dir}/ (seed_inputs=20260703)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="jvm/goldens")
    ap.add_argument("--grads", action="store_true",
                    help="dump gradient goldens (train mode) instead of "
                         "the forward goldens")
    args = ap.parse_args()

    if args.grads:
        os.makedirs(args.out, exist_ok=True)
        dump_grads(args.out)
        return

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
