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

import math
import os

import mlx.core as mx


def max_chunks_bound(L):
    """STATIC (data-independent) upper bound on the #chunks for a length-L byte
    seq, used to size the gathered chunk tensor WITHOUT a host-sync (`.item()`).

    Default = ceil(L / MIN_CHUNK) with MIN_CHUNK=2 (env MMLLM_HNET_MIN_CHUNK),
    i.e. ~L/2 ≪ L so the H-Net compute reduction is preserved (the transformer
    runs on chunk-rate, not byte-rate), while staying safely above the typical
    real chunk count (ratio loss targets avg chunk size N≈6, so ≈L/6 boundaries
    — the L/2 bound is ~3× headroom and is essentially never hit). MIN_CHUNK=2
    is also robust at init, where ~half the positions can be boundaries.

    Override the whole bound with MMLLM_HNET_MAX_CHUNKS. Result is clamped to
    [1, L] (a chunk seq can never be longer than the byte seq). L is a Python
    int (a static tensor dim), so this introduces no host-sync."""
    cap = os.environ.get("MMLLM_HNET_MAX_CHUNKS")
    if cap:
        return max(1, min(int(cap), int(L)))
    min_chunk = max(1, int(os.environ.get("MMLLM_HNET_MIN_CHUNK", "2")))
    return max(1, min(math.ceil(int(L) / min_chunk), int(L)))


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


def downsample(xhat, b, max_chunks=None):
    """Gather the boundary positions into fixed-width chunk reps.
    xhat:(B,L,d), b:(B,L) bool/0-1 -> (z:(B,M,d), keep_idx:(B,M) int32,
    valid:(B,M) 0/1, chunk_id:(B,L) int32) where M = `max_chunks` is a STATIC
    (data-independent) bound — NOT a `.item()` of the batch's max boundary count.
    Rows are padded to M; padded slots point at a non-boundary (valid=0, z=0) and,
    because the sort puts them AFTER all real boundaries, they land at chunk
    positions ≥ real-count. Causal attention downstream therefore never lets a
    real chunk attend to a padded slot, and dechunk only ever gathers chunk_id ∈
    [0, real-count) — so the static padding is exactly equivalent to the old
    dynamic M (within the bound) yet carries no host-sync / data-dependent shape.

    Index bookkeeping is built with argsort (no scatter — scatter has no VJP in
    MLX) on the DETACHED boundary mask, so the only differentiable path out is
    the gather of `xhat` into the chunk reps (grad flows to the encoder).

    Overflow (a row with > M real boundaries — rare: the ratio loss pins avg
    chunk size ≫ L/M) is handled GRACEFULLY: the first M boundaries are kept and
    chunk_id is clamped to M-1 so the trailing bytes merge into the last chunk
    (no OOB gather in dechunk, no crash, no silent wrong-gather)."""
    B, L, d = xhat.shape
    M = max_chunks_bound(L) if max_chunks is None else max(1, min(int(max_chunks), int(L)))
    bb = mx.stop_gradient(b)                                   # boundaries are a hard
    bi = bb.astype(mx.int32)                                   # threshold → constant
    # chunk_id[t] = (#boundaries at positions ≤ t) − 1  (0-based id of t's chunk)
    chunk_id = mx.cumsum(bi, axis=1) - 1                       # (B,L)
    pos = mx.broadcast_to(mx.arange(L)[None, :], (B, L))       # (B,L)
    # sort key: boundary positions get their index (0..L-1); non-boundaries get a
    # large key (≥L) so they fall after all real boundaries → first M slots are the
    # boundary positions in ascending order.
    key = pos + (1 - bi) * (L + 1)
    order = mx.argsort(key, axis=1).astype(mx.int32)           # (B,L)
    keep_idx = mx.stop_gradient(order[:, :M])                  # (B,M) STATIC width
    valid = mx.take_along_axis(bb.astype(mx.float32), keep_idx, axis=1)  # (B,M)
    z = mx.take_along_axis(xhat, keep_idx[:, :, None], axis=1)  # (B,M,d) chunk reps
    z = z * valid[:, :, None]
    # graceful overflow clamp: keep dechunk gathers in-bounds for any row whose
    # real boundary count exceeds the static bound (sync-free min, no `.item()`).
    chunk_id = mx.minimum(chunk_id, M - 1)
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


def overflow_count(b, max_chunks=None):
    """#rows whose real boundary count exceeds the static `max_chunks` bound, as a
    LAZY mx scalar (no host-sync). Returned so the caller can stash/log it without
    forcing an eval in the forward trace; only float()/.item() it off the hot path
    (e.g. an env-gated diagnostic). 0 in the typical regime."""
    M = max_chunks_bound(b.shape[1]) if max_chunks is None else int(max_chunks)
    cnt = mx.sum(mx.stop_gradient(b).astype(mx.int32), axis=1)     # (B,) per-row #boundaries
    return mx.sum((cnt > M).astype(mx.int32))


def chunk(xhat, Wq, Wk, max_chunks=None):
    """Full chunk pass: returns (z, keep_idx, valid, chunk_id, p, b, c).
    z:(B,M,d) chunk reps (M = static `max_chunks` bound, default ceil(L/2));
    b:(B,L) 0/1 boundaries; c:(B,L) confidence. The cut DYNAMICS (cosine p_t,
    0.5 threshold, STE, smoothing-EMA) are unchanged — only the gather is now
    static+masked rather than `.item()`-sized."""
    p = boundary_probs(xhat, Wq, Wk)
    b = (p >= 0.5).astype(mx.float32)
    z, keep_idx, valid, chunk_id = downsample(xhat, b, max_chunks=max_chunks)
    c = confidence(p, b)
    return z, keep_idx, valid, chunk_id, p, b, c
