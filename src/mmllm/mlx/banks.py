"""MLX implementations of the two PKM bank forwards — the novel, retrieval-heavy
part of the model (the spike measured these 4.5x faster than torch-MPS).

Both mirror the EVAL forward of their torch counterparts (no training-only
telemetry: z-loss, bincount hit-counters, last_output_norm — all skipped):

  NetBank (netbank.py:295):  q_norm -> q_a@K_a.T / q_b@K_b.T -> topk(sub_top_k)
    -> outer-sum -> topk(top_k) -> decode global idx -> gather V_net (c_net)
    -> softmax-weighted einsum -> expander Linear -> q_dim.
  Local PKM (memory.py):     same pipeline but V rows are q_dim directly (no
    expander), optional per-router (trunk) index offset, no q_norm.

The output is permutation-invariant over the selected top-k set (the softmax
einsum sums over k), so MLX's unordered argpartition matches torch's sorted topk
as long as the selected sets agree — boundary ties are the only divergence, and
the parity gate tolerates them (top-1 > 99.5%).
"""
from __future__ import annotations

import mlx.core as mx


def _rms_norm(x, weight, eps):
    # Matches torch RMSNorm: x / sqrt(mean(x^2,-1)+eps) * weight
    return (x * mx.rsqrt(mx.mean(x * x, axis=-1, keepdims=True) + eps)) * weight


def _topk_idx(a, k):
    """Top-k (by value, descending-set) indices along the last axis + their
    values. Unordered within the k — fine, the downstream contraction is
    permutation-invariant. argpartition(-a, k)[:k] gives the k largest."""
    idx = mx.argpartition(-a, k, axis=-1)[..., :k]
    return mx.take_along_axis(a, idx, axis=-1), idx


def _pkm_select(q_a, q_b, K_a, K_b, sqrt_n, sub_top_k, top_k):
    """Shared score -> sub-topk -> outer-sum -> topk -> global-index decode.
    Returns (top_scores [B,T,top_k], top_global [B,T,top_k] int32)."""
    scores_a = q_a @ K_a.T          # [B,T,sqrt_n]
    scores_b = q_b @ K_b.T
    top_a_s, top_a_i = _topk_idx(scores_a, sub_top_k)   # [B,T,sub_top_k]
    top_b_s, top_b_i = _topk_idx(scores_b, sub_top_k)
    # outer-sum re-rank over the sub_top_k^2 grid
    comb = (top_a_s[..., :, None] + top_b_s[..., None, :])
    comb = comb.reshape(comb.shape[0], comb.shape[1], -1)   # [B,T,sub_top_k^2]
    top_scores, top_local = _topk_idx(comb, top_k)
    a_within = top_local // sub_top_k
    b_within = top_local - a_within * sub_top_k
    top_a_global = mx.take_along_axis(top_a_i, a_within, axis=-1)
    top_b_global = mx.take_along_axis(top_b_i, b_within, axis=-1)
    top_global = top_a_global * sqrt_n + top_b_global
    return top_scores, top_global


def netbank_forward(p, q, want_z=False):
    """MLX NetBank eval forward.

    p: dict of mx.array params {q_norm_w, K_a, K_b, V, expander_w} + ints/floats
       {sub_dim, sqrt_n, sub_top_k, top_k, eps}. q: [B,T,q_dim] -> [B,T,q_dim].

    When want_z, also returns a LOAD-BALANCING loss on the sub-keys (CV² of per-key
    routing importance, summed over the K_a and K_b axes). The NetBank historically
    had NO anti-collapse term, so its keys collapsed (all corpora retrieve a shared
    ~1% hot row set, Jaccard ~0.7). The router-entropy z-loss (logsumexp²) was tried
    and FAILED: it flattens score peaks but top-k is argmax, so it never reorders the
    winners. CV²(importance) penalizes keys that ACCUMULATE soft routing mass, pushing
    that mass toward uniform → under-used keys win the top-k → product rows spread →
    corpora get distinct V_net storage (a prerequisite for cross-round consolidation).
    """
    q = _rms_norm(q, p["q_norm_w"], p["eps"])
    q_a = q[..., : p["sub_dim"]]
    q_b = q[..., p["sub_dim"]:]
    z = None
    if want_z:
        def _cv2(s):                                    # coeff-of-variation² of key importance
            P = mx.softmax(s, axis=-1)                  # [...,sqrt_n] soft routing prob
            imp = P.mean(axis=tuple(range(P.ndim - 1)))  # [sqrt_n] mean mass per key
            return imp.var() / (imp.mean() ** 2 + 1e-9)
        z = _cv2(q_a @ p["K_a"].T) + _cv2(q_b @ p["K_b"].T)
    top_scores, top_global = _pkm_select(
        q_a, q_b, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"]
    )
    if "V_mmap" in p:                                   # mode 2: NetBank V on disk
        # The V table stays mmap'd on disk; gather only the (small) top-k rows on
        # host and upload that payload. Trades the full-V VRAM (1+ GB) for one
        # GPU->host sync per layer per step. p["V_mmap"] is a numpy memmap (N,c).
        import numpy as np
        Vm = p["V_mmap"]
        idx = np.asarray(top_global).reshape(-1)        # GPU->host (top_k int ids)
        rows = np.asarray(Vm[idx], dtype=np.float32)
        latent = mx.array(rows).reshape(*top_global.shape, Vm.shape[1])
    else:                                               # mode 1: V resident on GPU
        latent = mx.take(p["V"], top_global, axis=0).astype(mx.float32)
    weights = mx.softmax(top_scores, axis=-1)
    weighted_latent = mx.einsum("btkc,btk->btc", latent, weights)
    out = weighted_latent @ p["expander_w"].T           # expander Linear (bias=False)
    return (out, z) if want_z else out


def netbank_forward_modular(banks, active, q, want_z=False):
    """Modular MLX NetBank — Apple-Silicon-local-bird counterpart of the torch
    ModularNetBank (mmllm.netbank).

    `banks`:  {module_name: netbank_params_dict} — each dict is exactly what
              netbank_forward() consumes (q_norm_w/K_a/K_b/V|V_mmap/expander_w/…).
    `active`: list of module names to consult (corpus tag at genesis via
              mmllm.skill_modules.module_for_corpus; learned router later);
              None → all modules (composition).

    Single active → route to that module; multiple → sum outputs (a learned
    gate can replace the plain sum past genesis), matching ModularNetBank.
    Cooling is handled upstream by the trainer: a frozen module's V_net is
    excluded from the SparseAdam trainable set (the Ft freeze path), so its
    rows cannot move — the same structural isolation torch freeze_module()
    gives via requires_grad=False.
    """
    names = list(banks) if active is None else [a for a in active if a in banks]
    if not names:                       # routed to nothing present → consult all
        names = list(banks)
    out = None
    z = None
    for n in names:
        r = netbank_forward(banks[n], q, want_z=want_z)
        o = r[0] if want_z else r
        out = o if out is None else out + o
        if want_z and r[1] is not None:
            z = r[1] if z is None else z + r[1]
    return (out, z) if want_z else out


def local_forward(p, q, trunk_ids=None, want_z=False):
    """MLX Local PKM eval forward. Like NetBank but V rows are q_dim (no
    expander) and an optional per-router (trunk) row offset selects the
    router's slice of the shared V table. Applies q_norm like memory.py:forward.

    When want_z, also returns the PKM z-loss (mean lse_a^2 + lse_b^2 over the
    full sub-key scores) — the router-entropy regularizer (memory.py:958)."""
    q = _rms_norm(q, p["q_norm_w"], p["eps"])
    q_a = q[..., : p["sub_dim"]]
    q_b = q[..., p["sub_dim"]:]
    z = None
    if want_z:
        sa = q_a @ p["K_a"].T
        sb = q_b @ p["K_b"].T
        z = (mx.logsumexp(sa, axis=-1) ** 2).mean() + (mx.logsumexp(sb, axis=-1) ** 2).mean()
    top_scores, top_global = _pkm_select(
        q_a, q_b, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"]
    )
    if trunk_ids is not None and p.get("n_trunks", 1) > 1:
        # each router owns a contiguous sqrt_n^2 block of rows
        offset = (trunk_ids * (p["sqrt_n"] * p["sqrt_n"])).reshape(
            trunk_ids.shape[0], 1, 1
        )
        top_global = top_global + offset
    values = mx.take(p["V"], top_global, axis=0).astype(mx.float32)  # [B,T,top_k,q_dim]
    weights = mx.softmax(top_scores, axis=-1)
    out = mx.einsum("btkd,btk->btd", values, weights)
    return (out, z) if want_z else out
