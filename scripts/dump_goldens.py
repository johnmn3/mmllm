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

--optim mode (M5a, spec §2 recipe / gate G4 optimizer-delta half) writes the
LR-schedule + optimizer goldens (self-contained; no model build needed):

  schedule.npz         per-step (base, dense, kab, bank, net) lr table for
                       steps 0..99 at the prod recipe env (LR=3e-3,
                       LR_MIN=3e-3, warmup=70, extend_chain.sh group mults),
                       computed by CALLING the core.lpy vars (lr-at-step +
                       pick-lr-*-mult arity-2), plus an rb_* variant with
                       MMLLM_LR_ROUND_BASE=40 / MMLLM_LR_RAMP_FLOOR=0.1 /
                       warmup=68 to pin the chain-round-resume semantics
  adamw.npz            8x4 param + 5 fixed dense grads through torch AdamW
                       exactly as make-opt-dense builds it (prod: KAB_MULT
                       unset == DENSE_MULT -> single group, lr=pick-lr-dense,
                       torch defaults incl. weight_decay=1e-2); param dumped
                       after each step
  sparse_adam.npz      optim.py CPUOffloadSparseAdam trajectories, 5 steps of
                       hand-built sparse grads with overlapping/duplicate/
                       unsorted rows: (a) 64x4 non-V_local param at prod
                       MMLLM_SQRT_N=128, (b) 48x4 V_local-shaped param (3
                       trunks of sqrt_local²=16 at MMLLM_SQRT_N=4) covering
                       the LOCAL_MULT=0.05 rule, (c) three 32x4 V_local
                       params with MMLLM_LR_LAYER_MULTS=2.0,0.5 and grad-less
                       steps, covering layer-mult tiling + the per-param step
                       counter + the counter-skips-gradless-params quirk

--step mode (M5b, spec §8 / gate G4 full-step half) writes step.npz: THREE
replayed torch train-steps at the prod sym24 recipe env on a REPLAY-friendly
batch (B=2 rows exercising routers 0 and 3 via trunk_ids, T=32,
MMLLM_GRAD_CHECKPOINT=false so aux losses ride the forward return,
KD_EVERY=2 with metrics current_step=10,11,12 so KD fires on steps 10+12,
NetBank delay 0, PKM C++ off). The steps are run by CALLING the core.lpy
`train-step` var directly on the same fresh seed-0 model that dense.npz /
banks/*.bin capture, with the three optimizers built exactly as train-long
builds them and per-step lrs applied exactly as the train loop composes
them. Recorded per step via additive monkeypatches (no reference change):

  torch.rand_like       → deterministic recorded stream (the SwitchGate
                          net-default ST-Bernoulli draws: 24 local layers
                          × (B, H, T) per main forward; teacher/student
                          take 2-way branches and draw nothing)
  ProductKeyMemory.forward → per-layer Local z-loss scalars (first 24 per
                          step = the main forward's; teacher re-runs them
                          under no_grad, sliced off)
  rs.focal_ce           → ce_loss scalar (mean of per-pos CE, γ=0)
  torch.Tensor.backward → loss_total (CE + z) and kd_loss scalars
  opt.step wrappers     → all-698 dense grad L2 norms (NaN = grad None),
                          block-0 local + net sparse dV (coalesced idx+val)

plus post-step FULL values of all 698 dense tensors and the post-step V
rows actually touched (block-0 local + net), and the initial 698 tensors
(asserted identical to dense.npz — same seed-0 build).

Run:  .venv/bin/python scripts/dump_goldens.py [--out jvm/goldens]
      .venv/bin/python scripts/dump_goldens.py --grads   (forward goldens
      must exist first: grads_ce reads full_forward.npz)
      .venv/bin/python scripts/dump_goldens.py --optim
      .venv/bin/python scripts/dump_goldens.py --step    (forward goldens
      must exist first: initial state is asserted against dense.npz)
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


# ── M5a: LR schedule + optimizer goldens ──

# The prod-recipe schedule env (extend_chain.sh:192-233 at STEPS=100).
# MMLLM_LR_KAB_MULT is deliberately NOT set: extend_chain.sh doesn't set it,
# so pick-lr-kab-mult defaults to pick-lr-dense-mult's START (0.05) and its
# _END defaults to that same start — i.e. kab stays CONSTANT 0.05 while
# dense cosines 0.05 -> 0.005 (and make-opt-dense stays single-group).
SCHED_PROD_ENV = {
    "MMLLM_LR": "3e-3",
    "MMLLM_LR_MIN": "3e-3",
    "MMLLM_LR_WARMUP": "70",           # 70% of 100 steps
    "MMLLM_LR_DENSE_MULT": "0.05",
    "MMLLM_LR_DENSE_MULT_END": "0.005",
    "MMLLM_LR_BANK_MULT": "3.0",
    "MMLLM_LR_BANK_MULT_END": "0.001",
    "MMLLM_LR_NET_MULT": "0.001",
    "MMLLM_LR_NET_MULT_END": "5.0",
}


def _core_vars():
    """Bootstrap basilisp + mmllm.core WITHOUT building the model (the
    pick-lr-*/lr-at-step vars are pure env readers) — same rt.Var.find
    pattern as jvm_bridge.build_model / mlx/parity.py."""
    for k, v in SYM24_ENV.items():
        os.environ.setdefault(k, v)
    import basilisp.main
    basilisp.main.init()
    import mmllm.core  # noqa: F401 — registers the namespace
    import basilisp.lang.runtime as rt
    from basilisp.lang import symbol as sym

    def var(n):
        return rt.Var.find(sym.symbol(n, ns="mmllm.core")).value
    return var


def dump_optim(out_dir):
    """Schedule + optimizer goldens (M5a). Schedule values come from CALLING
    the core.lpy vars; optimizer trajectories from torch.optim.AdamW and
    optim.py's CPUOffloadSparseAdam run for 5 steps on fixed grads."""
    import numpy as np
    import torch

    for k, v in SCHED_PROD_ENV.items():
        os.environ[k] = v
    var = _core_vars()

    # ── schedule.npz ──
    total = 100
    lr_at_step = var("lr-at-step")
    pick_lr, pick_lr_min = var("pick-lr"), var("pick-lr-min")
    pick_warmup = var("pick-lr-warmup")
    mult = {g: var(f"pick-lr-{g}-mult") for g in ("dense", "kab", "bank", "net")}
    arrs = {}

    def sched_table(prefix):
        warmup = int(pick_warmup())
        base = np.array(
            [float(lr_at_step(s, total, pick_lr(), warmup, pick_lr_min()))
             for s in range(total)], dtype=np.float64)
        arrs[prefix + "base"] = base
        # per-group lr exactly as the train loop composes it
        # (core.lpy:4888-4904): cur-lr × pick-lr-*-mult(step, total).
        for gname, fn in mult.items():
            arrs[prefix + gname] = base * np.array(
                [float(fn(s, total)) for s in range(total)], dtype=np.float64)
        arrs[prefix + "warmup"] = np.int64(warmup)

    sched_table("")
    arrs["total"] = np.int64(total)
    arrs["lr"] = np.float64(pick_lr())
    arrs["lr_min"] = np.float64(pick_lr_min())
    for gname, fn in mult.items():
        # arity-0 = start; arity-2 at step>=total = end (captures the
        # kab-defaults-to-dense-start semantics as data).
        arrs[gname + "_start"] = np.float64(fn())
        arrs[gname + "_end"] = np.float64(fn(total, total))

    # Chain-round-resume variant: ROUND_BASE shifts the ramp (s-eff /
    # warmup-eff), RAMP_FLOOR lifts its minimum — while the cosine phase
    # keeps using ABSOLUTE s/warmup (reference quirk, replicated as-is).
    os.environ["MMLLM_LR_ROUND_BASE"] = "40"
    os.environ["MMLLM_LR_RAMP_FLOOR"] = "0.1"
    os.environ["MMLLM_LR_WARMUP"] = "68"
    sched_table("rb_")
    arrs["rb_round_base"] = np.int64(40)
    arrs["rb_ramp_floor"] = np.float64(0.1)
    del os.environ["MMLLM_LR_ROUND_BASE"]
    del os.environ["MMLLM_LR_RAMP_FLOOR"]
    os.environ["MMLLM_LR_WARMUP"] = SCHED_PROD_ENV["MMLLM_LR_WARMUP"]
    np.savez(os.path.join(out_dir, "schedule.npz"), **arrs)
    print(f"schedule.npz: base lr step0={arrs['base'][0]:.3e} "
          f"step69={arrs['base'][69]:.6e} step99={arrs['base'][99]:.6e}; "
          f"net lr step99={arrs['net'][99]:.6e}")

    g = torch.Generator().manual_seed(20260705)

    # ── adamw.npz ──
    p = torch.nn.Parameter(torch.randn(8, 4, generator=g))
    grads = torch.randn(5, 8, 4, generator=g)
    # Exactly make-opt-dense (core.lpy:2303): prod env has KAB_MULT unset ==
    # DENSE_MULT, so the single-group branch: AdamW(params, lr=pick-lr-dense)
    # with torch defaults betas=(0.9,0.999), eps=1e-8, weight_decay=1e-2.
    opt = torch.optim.AdamW([p], lr=float(var("pick-lr-dense")()))
    pg = opt.param_groups[0]
    aw = {"p_init": _np(p).copy(), "grads": _np(grads),
          "lr": np.float64(pg["lr"]),
          "beta1": np.float64(pg["betas"][0]),
          "beta2": np.float64(pg["betas"][1]),
          "eps": np.float64(pg["eps"]),
          "weight_decay": np.float64(pg["weight_decay"])}
    outs = []
    for i in range(5):
        p.grad = grads[i].clone()
        opt.step()
        outs.append(_np(p).copy())
    aw["p_steps"] = np.stack(outs)
    np.savez(os.path.join(out_dir, "adamw.npz"), **aw)
    print(f"adamw.npz: lr={float(aw['lr']):.2e} wd={float(aw['weight_decay'])} "
          f"|Δp| after 5 steps={float(np.abs(aw['p_steps'][-1] - aw['p_init']).max()):.3e}")

    # ── sparse_adam.npz ──
    import mmllm.optim as vbopt

    def reset_optim_caches():
        # _get_local_default_mult / _get_layer_mults cache per-process;
        # we flip MMLLM_SQRT_N / MMLLM_LR_LAYER_MULTS between variants.
        for f in (vbopt._get_layer_mults, vbopt._get_local_default_mult):
            if hasattr(f, "_cache"):
                delattr(f, "_cache")

    lr_bank = float(pick_lr()) * float(mult["bank"]())   # 3e-3 × 3.0
    sa = {"beta1": np.float64(0.9), "beta2": np.float64(0.999),
          "eps": np.float64(1e-8), "local_mult": np.float64(0.05)}

    def run_sparse(prefix, params, step_rows):
        opt = vbopt.CPUOffloadSparseAdam(list(params), lr=lr_bank)
        for j, pp in enumerate(params):
            sa[f"{prefix}_p{j}_init"] = _np(pp).copy()
        for s, per_param in enumerate(step_rows):
            for j, (pp, rows) in enumerate(zip(params, per_param)):
                if rows is None:
                    pp.grad = None
                    continue
                vals = torch.randn(len(rows), pp.shape[1], generator=g)
                idx = torch.tensor([rows], dtype=torch.long)
                pp.grad = torch.sparse_coo_tensor(idx, vals, tuple(pp.shape))
                sa[f"{prefix}_g{s}_p{j}_idx"] = np.asarray(rows, dtype=np.int64)
                sa[f"{prefix}_g{s}_p{j}_val"] = _np(vals).copy()
            opt.step()
            for j, pp in enumerate(params):
                sa[f"{prefix}_p{j}_step{s}"] = _np(pp).copy()

    sa["lr"] = np.float64(lr_bank)

    # (a) non-V_local (V_net-analog) at prod MMLLM_SQRT_N=128: 64 rows don't
    # divide into trunks of 128² -> layer_mult 1.0. Overlapping rows across
    # steps + a duplicate (12,12) + unsorted rows exercise coalesce and the
    # touched-row m/v buffer growth against the ONE-per-param step counter.
    reset_optim_caches()
    sa["a_sqrt_local"] = np.int64(int(os.environ["MMLLM_SQRT_N"]))
    run_sparse("a", [torch.nn.Parameter(torch.randn(64, 4, generator=g))],
               [[[3, 7, 12, 12]], [[7, 20]], [[3, 20, 40]],
                [[12, 63, 7]], [[0, 3]]])

    # (b) V_local-shaped: sqrt_local=4 -> rows_per_trunk=16; 48 rows = 3
    # trunks >= 2 -> _is_v_local -> lr × LOCAL_MULT (default 0.05).
    os.environ["MMLLM_SQRT_N"] = "4"
    reset_optim_caches()
    sa["b_sqrt_local"] = np.int64(4)
    run_sparse("b", [torch.nn.Parameter(torch.randn(48, 4, generator=g))],
               [[[5, 17, 17, 40]], [[5, 47]], [[0, 17, 40]],
                [[47]], [[5, 0]]])

    # (c) three V_local params (32 rows = 2 trunks each) with LAYER_MULTS
    # tiling "2.0,0.5" and grad-less steps: replicates optim.py's
    # v_local_counter, which only counts v-local params WITH grads that
    # step (a grad-less param shifts later params' tile index).
    os.environ["MMLLM_LR_LAYER_MULTS"] = "2.0,0.5"
    reset_optim_caches()
    sa["c_sqrt_local"] = np.int64(4)
    sa["c_layer_mults"] = np.array([2.0, 0.5], dtype=np.float64)
    run_sparse("c", [torch.nn.Parameter(torch.randn(32, 4, generator=g))
                     for _ in range(3)],
               [[[1, 9], [2, 2, 30], [4]],
                [[9, 31], None, [4, 20]],
                [[1], [30, 5], None],
                [None, [2], [20, 4, 31]],
                [[9, 1, 31], [5], [0]]])
    del os.environ["MMLLM_LR_LAYER_MULTS"]
    os.environ["MMLLM_SQRT_N"] = SYM24_ENV["MMLLM_SQRT_N"]
    reset_optim_caches()

    np.savez(os.path.join(out_dir, "sparse_adam.npz"), **sa)
    print(f"sparse_adam.npz: lr={lr_bank:.2e}, variants a(64x4 mult=1.0) "
          f"b(48x4 mult=0.05) c(3x32x4 tiled 2.0,0.5)")
    print(f"optim goldens written to {out_dir}/ (seed_inputs=20260705)")


# ── M5b: full train-step goldens (gate G4) ──

# Prod sym24 recipe env on top of SYM24_ENV + SCHED_PROD_ENV: the logitkd
# KD recipe (extend_chain.sh:187-191) + explicit z coef + grad-checkpoint
# OFF (replay-friendly: aux losses thread through the forward return and
# no torch.utils.checkpoint recompute in the graph) + adam-cpu sparse opt.
STEP_ENV = {
    "MMLLM_DISTILL_OBJECTIVE": "logitkd",
    "MMLLM_KD_TEMP": "2.0",
    "MMLLM_KD_COEF": "1.0",
    "MMLLM_KD_FREEZE": "trunk",
    "MMLLM_KD_EVERY": "2",
    "MMLLM_Z_LOSS_COEF": "1e-5",
    "MMLLM_GRAD_CHECKPOINT": "false",
    "MMLLM_SPARSE_OPT": "adam-cpu",
    "MMLLM_GRAD_CLIP": "0.0",
}

# metrics current_step for the three replayed steps. Mid-warmup so every
# lr is non-zero (step 0's warmup lr is 0.0 — a degenerate parity point)
# and KD_EVERY=2 fires on the 1st and 3rd (10, 12) but not the 2nd.
STEP_STEPS = [10, 11, 12]
STEP_TOTAL = 100
STEP_B, STEP_T = 2, 32


def dump_step(out_dir):
    import numpy as np
    import torch

    for k, v in SCHED_PROD_ENV.items():
        os.environ[k] = v
    for k, v in STEP_ENV.items():
        os.environ[k] = v

    m, K, var = build_model()          # seed-0 fresh — same as dense.npz
    blocks = list(m.get(K("blocks")))

    # positional param names, verified against (parameters m) by identity
    from jvm_bridge import named_dense_walk
    named = named_dense_walk(m, K)
    params = list(var("parameters")(m))
    assert len(named) == len(params) == 698
    for (nm, q), p in zip(named, params):
        assert q is p, f"positional walk drift at {nm}"

    # initial state must be the dense.npz the JVM already loads
    dz_path = os.path.join(out_dir, "dense.npz")
    if not os.path.exists(dz_path):
        raise SystemExit("dense.npz missing — run without --step first")
    dz = np.load(dz_path)
    for i, p in enumerate(params):
        if not np.array_equal(dz[f"d{i:05d}"], _np(p)):
            raise SystemExit(f"param {i} ({named[i][0]}) != dense.npz — "
                             "model build drifted; regen forward goldens")

    mem0 = blocks[0].get(K("memory"))
    nb0 = blocks[0].get(K("netbank"))

    # optimizers exactly as train-long builds them (core.lpy:4565-4586)
    opt_dense = var("make-opt-dense")(m)
    assert len(opt_dense.param_groups) == 1   # prod: KAB_MULT unset
    sparse_cls = var("pick-sparse-optimizer")()
    opt_sparse = sparse_cls(list(var("sparse-parameters")(m)),
                            lr=float(var("pick-lr-bank")()))
    opt_sparse_net = sparse_cls(list(var("netbank-sparse-parameters")(m)),
                                lr=float(var("pick-lr-net")()))

    # batch: two rows (routers 0 and 3), y = next-byte windows of x
    g = torch.Generator().manual_seed(20260707)
    win = torch.randint(0, 256, (STEP_B, STEP_T + 1), generator=g)
    x, y = win[:, :STEP_T].clone(), win[:, 1:].clone()
    trunk_ids = torch.tensor([0, 3], dtype=torch.long)

    out = {"x": _np(x), "y": _np(y), "trunk_ids": _np(trunk_ids),
           "steps": np.asarray(STEP_STEPS, dtype=np.int64),
           "total": np.int64(STEP_TOTAL),
           "z_coef": np.float64(1e-5), "kd_temp": np.float64(2.0),
           "kd_coef": np.float64(1.0), "kd_every": np.int64(2),
           "local_mult": np.float64(0.05),
           "sqrt_local": np.int64(int(os.environ["MMLLM_SQRT_N"]))}
    # (param names come from the JVM side's manifest — same positional walk)

    # ── recorders (all additive monkeypatches) ──
    rand_rng = torch.Generator().manual_seed(20260711)
    rand_rec = []
    orig_rand_like = torch.rand_like

    def fake_rand_like(t, **kw):
        r = torch.rand(tuple(t.shape), generator=rand_rng,
                       dtype=torch.float32)
        rand_rec.append(_np(r).copy())
        return r.to(t.dtype)

    import mmllm.memory as memmod
    z_rec = []
    orig_mem_fwd = memmod.ProductKeyMemory.forward

    def rec_mem_fwd(self, q, trunk_ids=None):
        o = orig_mem_fwd(self, q, trunk_ids=trunk_ids)
        z = getattr(self, "last_z_loss", None)
        z_rec.append(float(z.item()) if z is not None else float("nan"))
        return o

    import mmllm.router_smarts as rs_mod
    ce_rec = []
    orig_focal = rs_mod.focal_ce

    def rec_focal(*a, **kw):
        r = orig_focal(*a, **kw)
        with torch.no_grad():
            ce_rec.append(float(r.mean().item()))
        return r

    bwd_rec = []
    orig_bwd = torch.Tensor.backward

    def rec_bwd(self, *a, **kw):
        if self.numel() == 1:
            bwd_rec.append(float(self.detach().item()))
        return orig_bwd(self, *a, **kw)

    grad_rec = []          # per opt-dense.step: (698,) L2 norms, NaN=None

    def rec_dense_grads():
        norms = np.full(len(params), np.nan, dtype=np.float64)
        for i, p in enumerate(params):
            if p.grad is not None:
                norms[i] = float(p.grad.detach().norm().item())
        grad_rec.append(norms)

    sparse_rec = []        # per opt-sparse.step: block-0 local (idx, val)
    sparse_net_rec = []

    def rec_sparse(module, sink):
        def cb():
            gv = module.V.weight.grad
            assert gv is not None and gv.is_sparse
            gv = gv.coalesce()
            sink.append((_np(gv.indices()[0]).copy(),
                         _np(gv.values()).copy()))
        return cb

    def wrap_step(opt, cb):
        orig = opt.step

        def step(*a, **kw):
            cb()
            return orig(*a, **kw)
        opt.step = step

    wrap_step(opt_dense, rec_dense_grads)
    wrap_step(opt_sparse, rec_sparse(mem0, sparse_rec))
    wrap_step(opt_sparse_net, rec_sparse(nb0, sparse_net_rec))

    # per-step lr application, composed exactly like the train loop
    # (core.lpy:4888-4904) via the same core vars M5a's schedule.npz pins.
    lr_at_step = var("lr-at-step")
    pick_lr, pick_lr_min = var("pick-lr"), var("pick-lr-min")
    warmup = int(var("pick-lr-warmup")())
    mult = {gname: var(f"pick-lr-{gname}-mult")
            for gname in ("dense", "bank", "net")}
    train_step = var("train-step")
    metrics = m.get(K("metrics"))

    torch.rand_like = fake_rand_like
    memmod.ProductKeyMemory.forward = rec_mem_fwd
    rs_mod.focal_ce = rec_focal
    torch.Tensor.backward = rec_bwd
    try:
        for si, step in enumerate(STEP_STEPS):
            cur = float(lr_at_step(step, STEP_TOTAL, pick_lr(), warmup,
                                   pick_lr_min()))
            lrs = {gname: cur * float(fn(step, STEP_TOTAL))
                   for gname, fn in mult.items()}
            opt_dense.param_groups[0]["lr"] = lrs["dense"]
            opt_sparse.param_groups[0]["lr"] = lrs["bank"]
            opt_sparse_net.param_groups[0]["lr"] = lrs["net"]
            metrics["current_step"] = step
            metrics["total_steps"] = STEP_TOTAL

            n_rand0, n_z0, n_bwd0, n_ce0 = (len(rand_rec), len(z_rec),
                                            len(bwd_rec), len(ce_rec))
            plain_ce = float(train_step(m, opt_dense, opt_sparse,
                                        opt_sparse_net, x, y, False,
                                        trunk_ids))

            kd_fires = step % 2 == 0
            n_rand = len(rand_rec) - n_rand0
            assert n_rand == 24, f"step {step}: {n_rand} rand draws != 24"
            for r in rand_rec[n_rand0:]:
                assert r.shape == (STEP_B, 2, STEP_T), r.shape
            n_z = len(z_rec) - n_z0
            assert n_z == (48 if kd_fires else 24), (step, n_z)
            n_bwd = len(bwd_rec) - n_bwd0
            assert n_bwd == (2 if kd_fires else 1), (step, n_bwd)
            assert len(ce_rec) - n_ce0 == 1

            p = f"s{si}_"
            out[p + "lr_dense"] = np.float64(lrs["dense"])
            out[p + "lr_bank"] = np.float64(lrs["bank"])
            out[p + "lr_net"] = np.float64(lrs["net"])
            out[p + "R"] = np.stack(rand_rec[n_rand0:])   # (24, B, H, T)
            out[p + "z_layers"] = np.asarray(z_rec[n_z0:n_z0 + 24])
            out[p + "ce"] = np.float64(ce_rec[n_ce0])
            out[p + "plain_ce"] = np.float64(plain_ce)
            out[p + "loss_total"] = np.float64(bwd_rec[n_bwd0])
            out[p + "kd"] = np.float64(bwd_rec[n_bwd0 + 1] if kd_fires
                                       else 0.0)
            if kd_fires:
                out[p + "kd_kl"] = np.float64(metrics["kd_local_net"])
                out[p + "teacher_bpc"] = np.float64(metrics["teacher_bpc"])
                out[p + "student_bpc"] = np.float64(metrics["student_bpc"])
            out[p + "grad_norms"] = grad_rec[si]
            li, lv = sparse_rec[si]
            ni, nv = sparse_net_rec[si]
            out[p + "local0_gidx"], out[p + "local0_gval"] = li, lv
            out[p + "net0_gidx"], out[p + "net0_gval"] = ni, nv
            with torch.no_grad():
                out[p + "local0_post"] = _np(
                    mem0.V.weight[torch.from_numpy(li)]).copy()
                out[p + "net0_post"] = _np(
                    nb0.V.weight[torch.from_numpy(ni)]).copy()
            for i, pp in enumerate(params):
                out[f"{p}d{i:05d}"] = _np(pp).copy()
            print(f"step {step}: plain_ce={plain_ce:.6f} "
                  f"loss={out[p + 'loss_total']:.6f} "
                  f"kd={float(out[p + 'kd']):.6f} "
                  f"z_sum={float(np.sum(out[p + 'z_layers'])):.4f} "
                  f"local0_nnz={len(li)} net0_nnz={len(ni)}")
    finally:
        torch.rand_like = orig_rand_like
        memmod.ProductKeyMemory.forward = orig_mem_fwd
        rs_mod.focal_ce = orig_focal
        torch.Tensor.backward = orig_bwd

    np.savez(os.path.join(out_dir, "step.npz"), **out)
    print(f"step goldens written to {out_dir}/step.npz "
          f"(steps={STEP_STEPS}, B={STEP_B}, T={STEP_T})")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="jvm/goldens")
    ap.add_argument("--grads", action="store_true",
                    help="dump gradient goldens (train mode) instead of "
                         "the forward goldens")
    ap.add_argument("--optim", action="store_true",
                    help="dump LR-schedule + optimizer goldens (M5a)")
    ap.add_argument("--step", action="store_true",
                    help="dump full train-step goldens (M5b, gate G4)")
    args = ap.parse_args()

    if args.grads:
        os.makedirs(args.out, exist_ok=True)
        dump_grads(args.out)
        return

    if args.optim:
        os.makedirs(args.out, exist_ok=True)
        dump_optim(args.out)
        return

    if args.step:
        os.makedirs(args.out, exist_ok=True)
        dump_step(args.out)
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
