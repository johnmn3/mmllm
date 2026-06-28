"""Phase B — minimal selective-SSM (Mamba-2 style) byte encoder/decoder for MLX.

MLX has no stock Mamba, so this implements the selective scan directly. Two
entry points:

  selective_scan_ref(...)  — explicit O(L) python-loop recurrence (the REFERENCE
                             used only to validate the fast path; not for prod).
  selective_scan(...)      — vectorised Hillis-Steele parallel scan (prod path).

Recurrence (per batch b, inner channel i, state n):
    h_t = dA_t * h_{t-1} + (delta_t * B_t * u_t)
    y_t = Σ_n C_t * h_t + D * u_t
with continuous-time discretisation dA_t = exp(delta_t * A).  A is negative
(A = -exp(A_log)) so dA_t ∈ (0,1].

The fast path uses the cumulative-product identity
    h_t = cp_t · ( h_carry + Σ_{s≤t} dBu_s / cp_s ),   cp_t = Π_{j≤t} dA_j
evaluated in fixed-size time CHUNKS (state carried across chunks) so the cp
division stays numerically bounded.  Pure forward function of param dicts so it
composes with mx.value_and_grad (same discipline as blocks.py).

Default-OFF: nothing here runs unless model.forward sees params["hnet"].
"""
from __future__ import annotations

import mlx.core as mx
import mlx.nn as nn


def _discretize(u, delta, A, Bm):
    """Return dA (B,L,d_in,d_state) and dBu (B,L,d_in,d_state)."""
    dA = mx.exp(delta[..., None] * A[None, None, :, :])          # (B,L,di,ds)
    dBu = delta[..., None] * Bm[:, :, None, :] * u[..., None]    # (B,L,di,ds)
    return dA, dBu


def selective_scan_ref(u, delta, A, Bm, Cm, D):
    """Explicit time-loop reference. u,delta:(B,L,di); A:(di,ds); Bm,Cm:(B,L,ds);
    D:(di,). Returns y:(B,L,di)."""
    Bsz, L, di = u.shape
    ds = A.shape[1]
    dA, dBu = _discretize(u, delta, A, Bm)
    h = mx.zeros((Bsz, di, ds))
    ys = []
    for t in range(L):
        h = dA[:, t] * h + dBu[:, t]                            # (B,di,ds)
        y_t = mx.sum(Cm[:, t][:, None, :] * h, axis=-1)         # (B,di)
        ys.append(y_t)
    y = mx.stack(ys, axis=1)                                    # (B,L,di)
    return y + D[None, None, :] * u


def selective_scan(u, delta, A, Bm, Cm, D):
    """Vectorised selective scan — division-free Hillis-Steele parallel prefix
    scan of the linear recurrence h_t = dA_t·h_{t-1} + dBu_t.  Same
    signature/semantics as the reference but O(log L) sequential depth and no
    cp-division (stable for any dA∈(0,1], unlike the cumprod-ratio form).

    The scan composes per-step affine transfers (a,x): applying transfer e1 then
    e2 gives (a2·a1, a2·x1 + x2); inclusive-scanning from h_0=0 leaves the
    x-component = h_t.  Pure mul/add/shift → differentiable."""
    Bsz, L, di = u.shape
    ds = A.shape[1]
    a, x = _discretize(u, delta, A, Bm)                        # (B,L,di,ds) each
    d = 1
    while d < L:
        a_sh = mx.concatenate(                                  # earlier element a_{t-d}
            [mx.ones((Bsz, d, di, ds)), a[:, : L - d]], axis=1)
        x_sh = mx.concatenate(
            [mx.zeros((Bsz, d, di, ds)), x[:, : L - d]], axis=1)
        x = a * x_sh + x                                        # use current a_t first
        a = a * a_sh
        d *= 2
    h = x                                                       # h_t (B,L,di,ds)
    y = mx.sum(Cm[:, :, None, :] * h, axis=-1)                 # (B,L,di)
    return y + D[None, None, :] * u


def _causal_depthwise_conv1d(x, w, b):
    """Depthwise causal conv along time. x:(B,L,d); w:(d,k); b:(d,) -> (B,L,d).
    Left-pads k-1 zeros so output[t] depends on x[t-k+1..t]."""
    B, L, d = x.shape
    k = w.shape[1]
    xp = mx.pad(x, [(0, 0), (k - 1, 0), (0, 0)])                # (B,L+k-1,d)
    out = mx.zeros((B, L, d))
    for j in range(k):
        out = out + xp[:, j:j + L, :] * w[None, None, :, j]
    return out + b[None, None, :]


def mamba_block(p, x):
    """One minimal Mamba-2 block (forward only), driven by a param dict `p`:
      in_proj_w   (2*d_inner, d_model)      x -> (xz)
      conv_w      (d_inner, d_conv)         depthwise causal conv kernel
      conv_b      (d_inner,)
      x_proj_w    (d_state*2 + dt_rank, d_inner)   -> (dt, B, C)  selective params
      dt_proj_w   (d_inner, dt_rank); dt_proj_b (d_inner,)
      A_log       (d_inner, d_state)        A = -exp(A_log)
      D           (d_inner,)
      out_proj_w  (d_model, d_inner)
      norm_w (d_model,), norm_eps          pre-norm (RMS)
    Residual: x + out_proj(scan(...)).  d_inner may equal d_model."""
    from mmllm.mlx.blocks import _rms_norm
    h = _rms_norm(x, p["norm_w"], p["norm_eps"])
    xz = h @ p["in_proj_w"].T                                   # (B,L,2*d_inner)
    d_inner = p["A_log"].shape[0]
    xs = xz[..., :d_inner]; z = xz[..., d_inner:]
    xs = _causal_depthwise_conv1d(xs, p["conv_w"], p["conv_b"])
    xs = xs * mx.sigmoid(xs)                                    # SiLU
    ds = p["A_log"].shape[1]
    dt_rank = p["dt_proj_w"].shape[1]
    proj = xs @ p["x_proj_w"].T                                 # (B,L, dt_rank+2*ds)
    dt = proj[..., :dt_rank]
    Bm = proj[..., dt_rank:dt_rank + ds]
    Cm = proj[..., dt_rank + ds:]
    delta = nn.softplus(dt @ p["dt_proj_w"].T + p["dt_proj_b"])  # (B,L,d_inner) >0
    A = -mx.exp(p["A_log"])
    y = selective_scan(xs, delta, A, Bm, Cm, p["D"])
    y = y * (z * mx.sigmoid(z))                                 # gated (SiLU(z))
    return x + y @ p["out_proj_w"].T


def mamba_stack(params, x):
    """Run a list of mamba block param dicts. Empty list -> identity (the gate)."""
    for p in params:
        x = mamba_block(p, x)
    return x
