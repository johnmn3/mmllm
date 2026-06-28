"""Phase B — cosine dynamic chunker (H-Net, arXiv:2507.07955) for MLX.

Router decides chunk boundaries from a cosine-similarity between adjacent
positions, downsamples bytes -> chunks, and (after the transformer runs on
chunks) dechunks chunk outputs back to byte rate with a straight-through
confidence that routes gradient to the boundary probabilities.

  q_t = x̂_t·W_q ,  k_t = x̂_t·W_k
  p_t = ½(1 − cos(q_t, k_{t−1})) ,  p_0 ≡ 1
  b_t = 𝟙{p_t ≥ 0.5}  (b_0 ≡ 1)            hard boundary
  chunk rep z̃_j = x̂ at the j-th boundary position (downsample)
  c_t = p_t if b_t else 1−p_t              confidence (∈[0.5,1] at a clean cut)
  dechunk: ŷ_t = chunk_out[chunk_id(t)] · (c_t / sg(c_t))   STE: fwd=chunk_out,
           grad → c_t → p_t → W_q/W_k.  Optional smoothing-EMA on chunk side.
  ratio loss pins E[chunk size] → N (H-Net eq. 10).

Everything is a pure forward function of a param dict so it composes with
mx.value_and_grad.  Default-OFF: only invoked when model.forward sees
params["hnet"].
"""
from __future__ import annotations

import mlx.core as mx


def boundary_probs(xhat, Wq, Wk):
    """xhat:(B,L,d) -> p:(B,L) boundary prob, with p[:,0]=1.0 forced.
    p_t = ½(1 − cos(q_t, k_{t−1}))."""
    B, L, d = xhat.shape
    q = xhat @ Wq.T                                            # (B,L,d)
    k = xhat @ Wk.T
    qn = q / (mx.linalg.norm(q, axis=-1, keepdims=True) + 1e-6)
    kn = k / (mx.linalg.norm(k, axis=-1, keepdims=True) + 1e-6)
    k_prev = mx.concatenate([kn[:, :1] * 0.0, kn[:, :-1]], axis=1)   # k_{t-1}, k_{-1}:=0
    cos = mx.sum(qn * k_prev, axis=-1)                        # (B,L); cos[:,0]=0
    p = 0.5 * (1.0 - cos)                                     # (B,L)
    # force p_0 = 1 (first byte always starts a chunk)
    first = mx.concatenate([mx.ones((B, 1)), mx.zeros((B, L - 1))], axis=1)
    p = first + (1.0 - first) * p
    return p


def ratio_loss(p, b, target_n):
    """H-Net ratio loss (eq. 10): pins E[chunk size] -> N.
    F = mean(p), G = mean(b).  L = N/(N-1)·((N-1)·F·G + (1−F)·(1−G)).
    Minimised at F = G = 1/N (i.e. one boundary every N bytes)."""
    N = float(target_n)
    F = mx.mean(p)
    G = mx.mean(b.astype(mx.float32))
    return (N / (N - 1.0)) * ((N - 1.0) * F * G + (1.0 - F) * (1.0 - G))


def downsample(xhat, b):
    """Gather the boundary positions into fixed-width chunk reps.
    xhat:(B,L,d), b:(B,L) bool/0-1 -> (z:(B,M,d), keep_idx:(B,M) int32,
    valid:(B,M) 0/1, chunk_id:(B,L) int32) where M = max #boundaries over the
    batch (rows padded; padded slots point at a non-boundary, valid=0).

    Index bookkeeping is built with argsort (no scatter — scatter has no VJP in
    MLX) on the DETACHED boundary mask, so the only differentiable path out is
    the gather of `xhat` into the chunk reps (grad flows to the encoder)."""
    B, L, d = xhat.shape
    bb = mx.stop_gradient(b)                                   # boundaries are a hard
    bi = bb.astype(mx.int32)                                   # threshold → constant
    # chunk_id[t] = (#boundaries at positions ≤ t) − 1  (0-based id of t's chunk)
    chunk_id = mx.cumsum(bi, axis=1) - 1                       # (B,L)
    M = max(int(mx.max(mx.sum(bi, axis=1)).item()), 1)
    pos = mx.broadcast_to(mx.arange(L)[None, :], (B, L))       # (B,L)
    # sort key: boundary positions get their index (0..L-1); non-boundaries get a
    # large key (≥L) so they fall after all real boundaries → first M slots are the
    # boundary positions in ascending order.
    key = pos + (1 - bi) * (L + 1)
    order = mx.argsort(key, axis=1).astype(mx.int32)           # (B,L)
    keep_idx = mx.stop_gradient(order[:, :M])                  # (B,M)
    valid = mx.take_along_axis(bb.astype(mx.float32), keep_idx, axis=1)  # (B,M)
    z = mx.take_along_axis(xhat, keep_idx[:, :, None], axis=1)  # (B,M,d) chunk reps
    z = z * valid[:, :, None]
    return z, keep_idx, valid, chunk_id


def confidence(p, b):
    """c_t = p_t if b_t else 1−p_t  (∈[0.5,1])."""
    bf = b.astype(mx.float32)
    return bf * p + (1.0 - bf) * (1.0 - p)


def dechunk(chunk_out, chunk_id, c, smooth=False):
    """Scatter chunk outputs back to byte positions with the STE confidence gate.
    chunk_out:(B,M,d), chunk_id:(B,L), c:(B,L) -> (B,L,d).

    Forward value is the routed chunk output (c/sg(c)=1) so it is byte-identical
    to a plain upsample; the gradient flows through c → p → W_q/W_k (the STE).
    smooth=True applies the H-Net causal EMA  ŷ_t = c_t·z_t + (1−c_t)·ŷ_{t−1}."""
    z = mx.take_along_axis(chunk_out, chunk_id[:, :, None], axis=1)  # (B,L,d) upsample
    ste = c / mx.stop_gradient(c)                                    # =1 fwd, grad→c
    if not smooth:
        return z * ste[:, :, None]
    # causal EMA over time, vectorised via the same affine prefix scan as mamba:
    #   ŷ_t = (1−c_t)·ŷ_{t−1} + c_t·z_t
    B, L, d = z.shape
    a = mx.broadcast_to((1.0 - c)[:, :, None], (B, L, d))
    x = (c[:, :, None]) * z
    step = 1
    while step < L:
        a_sh = mx.concatenate([mx.ones((B, step, d)), a[:, : L - step]], axis=1)
        x_sh = mx.concatenate([mx.zeros((B, step, d)), x[:, : L - step]], axis=1)
        x = a * x_sh + x
        a = a * a_sh
        step *= 2
    return x * ste[:, :, None]


def chunk(xhat, Wq, Wk):
    """Full chunk pass: returns (z, keep_idx, valid, chunk_id, p, b, c).
    z:(B,M,d) chunk reps; b:(B,L) 0/1 boundaries; c:(B,L) confidence."""
    p = boundary_probs(xhat, Wq, Wk)
    b = (p >= 0.5).astype(mx.float32)
    z, keep_idx, valid, chunk_id = downsample(xhat, b)
    c = confidence(p, b)
    return z, keep_idx, valid, chunk_id, p, b, c
