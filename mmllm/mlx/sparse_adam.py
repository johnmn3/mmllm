"""Hand-rolled per-row sparse Adam for the PKM bank V tables — MLX has no
SparseAdam. Reproduces CPUOffloadSparseAdam's update math (optim.py:323-344)
exactly so an MLX bird's optimizer state is harvest-compatible:

    m = beta1*m + (1-beta1)*g
    v = beta2*v + (1-beta2)*g^2
    delta = -lr*layer_mult * (m/(1-beta1^t)) / (sqrt(v/(1-beta2^t)) + eps)

Only TOUCHED rows update their moments (untouched rows do NOT decay — the
defining property of sparse Adam vs dense Adam). The gradient is obtained the
cheap way (the spike-validated path): differentiate only the gathered
[M, c] slice, then scatter-coalesce per touched row — never materializing a
dense [N, c] gradient through autograd.

State (m, v dense [N, c] fp32 + step) serializes to the torch
{step, m_buf, v_buf, row_to_buf} chunk format in Stage 5 (bridge.py).
"""
from __future__ import annotations

import numpy as np
import mlx.core as mx


def coalesce_row_grads(idx_flat, grad_flat, n_rows):
    """idx_flat [M] (int), grad_flat [M, c] -> (rows [R] unique, row_grad [R,c]
    summed over duplicate touches). Coalesce = scatter-add into a dense [N,c]
    accumulator (touched rows nonzero), then pick unique touched rows."""
    c = grad_flat.shape[-1]
    acc = mx.zeros((n_rows, c))
    acc = acc.at[idx_flat].add(grad_flat)
    rows_np = np.unique(np.array(idx_flat).reshape(-1))   # host: small (~M)
    rows = mx.array(rows_np)
    return rows, acc[rows]


class SparseAdam:
    def __init__(self, n_rows, dim, lr, betas=(0.9, 0.999), eps=1e-8,
                 layer_mult=1.0):
        self.m = mx.zeros((n_rows, dim))
        self.v = mx.zeros((n_rows, dim))
        self.step_count = 0
        self.lr = lr
        self.b1, self.b2 = betas
        self.eps = eps
        self.layer_mult = layer_mult

    def step(self, V, rows, row_grads):
        """Apply one Adam step to V's `rows` using coalesced `row_grads` [R,c].
        rows must be UNIQUE (coalesced). Returns the updated V."""
        self.step_count += 1
        s = self.step_count
        m_old = self.m[rows]
        v_old = self.v[rows]
        m_new = self.b1 * m_old + (1.0 - self.b1) * row_grads
        v_new = self.b2 * v_old + (1.0 - self.b2) * (row_grads * row_grads)
        bc1 = 1.0 - self.b1 ** s
        bc2 = 1.0 - self.b2 ** s
        m_hat = m_new / bc1
        v_hat = v_new / bc2
        delta = (-self.lr * self.layer_mult) * m_hat / (mx.sqrt(v_hat) + self.eps)
        # write moments back to the touched (unique) rows; add-of-difference
        # is an exact "set" because rows are unique (no duplicate scatter).
        self.m = self.m.at[rows].add(m_new - m_old)
        self.v = self.v.at[rows].add(v_new - v_old)
        return V.at[rows].add(delta)
