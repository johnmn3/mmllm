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


def netbank_forward(p, q):
    """MLX NetBank eval forward.

    p: dict of mx.array params {q_norm_w, K_a, K_b, V, expander_w} + ints/floats
       {sub_dim, sqrt_n, sub_top_k, top_k, eps}. q: [B,T,q_dim] -> [B,T,q_dim].
    """
    q = _rms_norm(q, p["q_norm_w"], p["eps"])
    q_a = q[..., : p["sub_dim"]]
    q_b = q[..., p["sub_dim"]:]
    top_scores, top_global = _pkm_select(
        q_a, q_b, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"]
    )
    latent = mx.take(p["V"], top_global, axis=0).astype(mx.float32)  # [B,T,top_k,c_net]
    weights = mx.softmax(top_scores, axis=-1)
    weighted_latent = mx.einsum("btkc,btk->btc", latent, weights)
    return weighted_latent @ p["expander_w"].T          # expander Linear (bias=False)


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
