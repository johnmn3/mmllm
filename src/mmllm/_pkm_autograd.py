"""Python autograd wrappers for the C++ PKM kernels.

Two custom autograd Functions:

* `PKMGather`        — F2: rows of V at flat indices, with sparse backward
                       keyed on the same indices so CPUOffloadSparseAdam /
                       CPUSparseSGD's index_add_ path is unchanged.

* `PKMFusedTopK`     — F3: fused outer-sum + top-K. Backward routes the
                       gradient of `top_scores` back to `top_a_s` and
                       `top_b_s` via the saved (top_local_ia, top_local_ib)
                       — each output score is a simple sum of two inputs,
                       so the gradient is an identity-selector scatter-add.

If the C++ extension isn't built (import fails), both Functions fall back
to the existing pure-PyTorch implementations. Tests / fresh checkouts
keep working; the speedup is gated on a successful build.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

# ------------------------------------------------------------------ #
# Import guard. _pkm_kernels lives next to memory.py inside the
# package; setup.py drops the .so into src/mmllm/.
# ------------------------------------------------------------------ #
try:
    from . import _pkm_kernels  # type: ignore[attr-defined]
    HAS_CPP_KERNELS = True
except ImportError:
    _pkm_kernels = None
    HAS_CPP_KERNELS = False


# ============================================================ #
# F2 — gather (read-only on V; sparse grad on backward)
# ============================================================ #
class PKMGather(torch.autograd.Function):
    """V[idx] with a sparse gradient on V.

    Forward:  out = V[idx]    shape = idx.shape + (D,)
    Backward: grad_V is a sparse_coo_tensor with indices=idx.flatten(),
              values=grad_out.flatten(0, -2), shape=V.shape.
              The existing optimizer dispatches sparse grads through
              index_add_(-lr * grad) which is exactly what we want.

    NOTE: V must be a leaf with requires_grad=True for the sparse grad
    to flow into the optimizer. idx is treated as constant (no grad).
    """

    @staticmethod
    def forward(ctx, V: torch.Tensor, idx: torch.Tensor) -> torch.Tensor:
        if HAS_CPP_KERNELS and V.is_cpu and V.dtype == torch.float32 and idx.is_cpu:
            out = _pkm_kernels.pkm_gather_rows(V.detach(), idx.detach().contiguous())
        else:
            out = F.embedding(idx, V)  # fallback — dense path

        ctx.save_for_backward(idx)
        ctx.V_shape = V.shape
        ctx.V_requires_grad = V.requires_grad
        # We need to track that V participated so autograd builds the edge.
        # Returning a tensor whose grad_fn references V via save_for_backward
        # is enough; we don't actually save V (saves memory — could be GBs).
        return out

    @staticmethod
    def backward(ctx, grad_out: torch.Tensor):
        (idx,) = ctx.saved_tensors
        if not ctx.V_requires_grad:
            return None, None

        # Flatten leading dims: idx is (..,) → (M,); grad_out is (.., D) → (M, D).
        D = grad_out.shape[-1]
        idx_flat = idx.reshape(-1).contiguous()       # (M,) int64
        grad_flat = grad_out.reshape(-1, D).contiguous()  # (M, D) fp32

        # sparse_coo_tensor wants indices as (1, nnz) for a 2D target.
        # CPUSparseSGD / CPUOffloadSparseAdam coalesce + index_add_ this
        # exactly like the F.embedding(sparse=True) backward does today.
        grad_V = torch.sparse_coo_tensor(
            idx_flat.unsqueeze(0),                    # (1, M)
            grad_flat,                                # (M, D)
            size=ctx.V_shape,
        )
        # NOTE: leaving uncoalesced. The existing optimizer path calls
        # .coalesce() before index_add_, so duplicating that here would
        # be wasted work. If a future consumer needs coalesced, add it.
        return grad_V, None


# ============================================================ #
# F3 — fused outer-sum + top-K
# ============================================================ #
class PKMFusedTopK(torch.autograd.Function):
    """Top-K over the (S, S) outer-sum of two sorted score vectors.

    Forward returns (top_scores, top_global) — flat indices into the
    sqrt_n × sqrt_n value-bank addressing space.

    Backward: top_scores[b,t,k] = top_a_s[b,t,ia_local[b,t,k]]
                                 + top_b_s[b,t,ib_local[b,t,k]]
    where ia_local / ib_local are the LOCAL (0..S-1) sub-key positions
    of the chosen pair — NOT the global keys ai/bi. We need both flat
    streams from the C++ side; the easiest path is to scan the saved
    global indices once on backward to recover the local positions.

    For tightness we just save top_a_i / top_b_i and use them to recover
    the local positions in backward. ALTERNATIVELY: extend the C++
    kernel to return local positions directly (cheaper). See the
    `IF_RETURNING_LOCAL` branch below — currently disabled.
    """

    @staticmethod
    def forward(ctx,
                top_a_s: torch.Tensor, top_a_i: torch.Tensor,
                top_b_s: torch.Tensor, top_b_i: torch.Tensor,
                sqrt_n: int, top_k: int):
        if HAS_CPP_KERNELS and top_a_s.is_cpu:
            top_scores, top_global = _pkm_kernels.pkm_fused_outer_topk(
                top_a_s.detach().contiguous(),
                top_a_i.detach().contiguous(),
                top_b_s.detach().contiguous(),
                top_b_i.detach().contiguous(),
                int(sqrt_n), int(top_k),
            )
        else:
            # Fallback: current Python path.
            B, T, S = top_a_s.shape
            combined = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
            idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, S)
            idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, S, -1)
            combined_idx = (idx_a * sqrt_n + idx_b).flatten(-2)
            top_scores, top_local = combined.topk(top_k, dim=-1)
            top_global = combined_idx.gather(-1, top_local)

        # Save what backward needs. Note: we save the GLOBAL ai/bi
        # because they're cheap to keep and let backward recover local
        # positions by searching. For B*T*top_k=O(10k) entries with
        # S=32 the search is fast. If it ever shows up in profiles,
        # extend the C++ kernel to emit local positions directly.
        ctx.save_for_backward(top_a_i, top_b_i, top_global)
        ctx.sqrt_n = int(sqrt_n)
        ctx.S = int(top_a_s.shape[-1])
        ctx.shape_ab = top_a_s.shape   # (B, T, S)
        return top_scores, top_global

    @staticmethod
    def backward(ctx, grad_top_scores: torch.Tensor, grad_top_global):
        # grad_top_global is discarded — indices are non-differentiable.
        top_a_i, top_b_i, top_global = ctx.saved_tensors
        sqrt_n = ctx.sqrt_n
        S = ctx.S
        B, T, K = grad_top_scores.shape

        # Decompose flat global index → (global_a, global_b)
        global_a = torch.div(top_global, sqrt_n, rounding_mode="floor")  # (B,T,K)
        global_b = top_global - global_a * sqrt_n                        # (B,T,K)

        # Recover local position in [0, S): for each (b,t,k), find which
        # entry of top_a_i[b,t,:] equals global_a[b,t,k]. Same for b.
        # `searchsorted` doesn't apply because top_a_i isn't sorted by
        # key value — it's sorted by score. Use equality match via
        # broadcasting; cost is O(B*T*K*S) which is small (16*32 per row).
        match_a = (top_a_i.unsqueeze(-2) == global_a.unsqueeze(-1))      # (B,T,K,S)
        match_b = (top_b_i.unsqueeze(-2) == global_b.unsqueeze(-1))      # (B,T,K,S)
        local_a = match_a.float().argmax(-1)                              # (B,T,K)
        local_b = match_b.float().argmax(-1)                              # (B,T,K)

        grad_a_s = torch.zeros(ctx.shape_ab, dtype=grad_top_scores.dtype,
                                device=grad_top_scores.device)
        grad_b_s = torch.zeros(ctx.shape_ab, dtype=grad_top_scores.dtype,
                                device=grad_top_scores.device)
        grad_a_s.scatter_add_(-1, local_a, grad_top_scores)
        grad_b_s.scatter_add_(-1, local_b, grad_top_scores)

        # Order matches forward signature: top_a_s, top_a_i, top_b_s, top_b_i, sqrt_n, top_k
        return grad_a_s, None, grad_b_s, None, None, None
