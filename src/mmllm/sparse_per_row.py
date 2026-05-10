"""Per-row LR boost for sparse-gradient parameters (PKM bank V).

This is the v1 spike of "per-row Adam" (#1 in the structural-learning
upgrade plan). True per-row Adam would require subclassing
torch.optim.SparseAdam to maintain a per-row step counter and apply
bias correction per-row instead of globally. That's a meaningful
optimizer rewrite (~100 LOC) we can do later if this spike shows
the dynamic is worth chasing.

This spike achieves the SAME high-level effect — cold rows learning
faster than hot rows — through a much simpler pre-step gradient
rescale:

  for each V param touched on this step:
    touch_count[i] += 1                       # for the touched rows i
    boost[i] = 1 + cold_boost / (eps + touch_count[i])
    grad_values[i] *= boost[i]                # scale up cold-row grads

  # Then SparseAdam.step() consumes the rescaled gradient.

A row touched 1 time gets full boost (= 1 + cold_boost / eps).
A row touched 1000 times gets no boost (≈ 1.0).

The touch-count buffer is attached as a non-persistent attribute on the
V parameter; it's reset on process restart (we re-converge quickly to
steady-state per-row touch frequencies in the first few hundred steps
after a resume).
"""
from __future__ import annotations

import os
import torch
import torch.nn as nn


def _cold_boost() -> float:
    """Strength of cold-row gradient boost. Reads MMLLM_BANK_COLD_BOOST
    (default 0.0 = disabled). Reasonable values 1.0-10.0; higher values
    favor cold rows more aggressively. 0 means no boost (back-compat
    with vanilla SparseAdam)."""
    try:
        return float(os.environ.get("MMLLM_BANK_COLD_BOOST", "0.0"))
    except ValueError:
        return 0.0


def _cold_boost_eps() -> float:
    """Smoothing constant in the boost formula `1 + boost / (eps + count)`.
    Reads MMLLM_BANK_COLD_BOOST_EPS (default 1.0). Larger eps → boost
    saturates closer to 1 across all rows; smaller eps → very-cold
    rows get extreme boosts."""
    try:
        return float(os.environ.get("MMLLM_BANK_COLD_BOOST_EPS", "1.0"))
    except ValueError:
        return 1.0


def boost_cold_row_grads_(memory_module: nn.Module) -> None:
    """In-place: rescale the V parameter's sparse gradient on its
    touched rows by (1 + boost / (eps + touch_count)).

    `memory_module` is a ProductKeyMemory (Local Bank) whose `.V` is an
    nn.Embedding with `weight.requires_grad=True` and a sparse gradient
    (set up via `nn.Embedding(..., sparse=True)`).

    Lazily allocates the per-row touch-count buffer on first call.
    Increments counts AFTER computing the boost (so a row's first-ever
    touch gets the maximum boost).

    Safe to call when:
      - boost = 0 (no-op, returns immediately)
      - V is None or has no .grad (no-op)
      - V's grad is dense (skip; only sparse grads are touched)
    """
    boost = _cold_boost()
    if boost <= 0:
        return
    V = getattr(memory_module, "V", None)
    if V is None:
        return
    weight = getattr(V, "weight", None)
    if weight is None or weight.grad is None:
        return
    g = weight.grad
    if not g.is_sparse:
        return  # only sparse-gradient PKM V is supported

    eps = _cold_boost_eps()
    indices = g._indices()  # shape (1, n_touched)
    values  = g._values()   # shape (n_touched, q_dim)
    if indices.numel() == 0 or values.numel() == 0:
        return

    row_idx = indices[0]   # (n_touched,)

    # Lazy-init touch counter on the V tensor itself so it survives
    # across train-steps. Long dtype on the same device as V.
    if not hasattr(weight, "_per_row_touches"):
        weight._per_row_touches = torch.zeros(
            weight.shape[0], dtype=torch.long, device=weight.device,
        )
    counts = weight._per_row_touches

    # Compute boost = 1 + cold_boost / (eps + count) for the touched rows.
    # We use the count BEFORE this step's update so first-ever touches
    # get the maximum boost.
    touched_counts = counts.index_select(0, row_idx).to(values.dtype)
    boost_factor = 1.0 + boost / (eps + touched_counts)   # (n_touched,)
    # Scale values per-row.
    values.mul_(boost_factor.unsqueeze(-1))

    # Increment touch counts AFTER applying the boost.
    counts.index_add_(
        0, row_idx,
        torch.ones_like(row_idx, dtype=counts.dtype),
    )


def boost_all_local_banks_(blocks) -> None:
    """Apply boost_cold_row_grads_ to every block's Local Bank.
    `blocks` is the model's per-layer block list. No-op when boost = 0
    (cheap env-var check inside)."""
    if _cold_boost() <= 0:
        return
    for b in blocks:
        mem = b.get("memory") if isinstance(b, dict) else None
        # basilisp passes blocks as basilisp maps which look like dicts.
        # Fallback: try keyword access if get-by-string didn't work.
        if mem is None:
            try:
                # basilisp's PersistentMap supports __getitem__ with keywords
                from basilisp.lang.keyword import keyword as _kw
                mem = b[_kw("memory")]
            except Exception:
                continue
        boost_cold_row_grads_(mem)
