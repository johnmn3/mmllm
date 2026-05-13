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
# Build guard. Two paths:
#   (a) prebuilt _pkm_kernels.so next to memory.py (from setup.py path)
#   (b) JIT-compile via torch.utils.cpp_extension.load() on first import.
# We try (a) first; fall back to (b); fall back to pure Python.
#
# JIT cache lives under TORCH_EXTENSIONS_DIR (default ~/.cache/torch_extensions/),
# so the .so is built once per host and reused across processes. The first
# build takes ~15s; subsequent imports are near-instant.
#
# Default is OFF — at cpu-mini scale the kernels deliver ~0 speedup
# (V=3.3 MB / outer-sum temp=8 MB are already cache-fast; the autograd
# Function + sparse_coo_tensor wrapper overhead eats whatever the C++
# saves). Set MMLLM_ENABLE_PKM_CPP=true to opt in — useful for cpu-tiny
# scale (V=26 MB) or for any future config where the kernels show
# benefit. See CLAUDE.md "PKM C++ kernels" for the benchmark.
# ------------------------------------------------------------------ #
import os as _os
from pathlib import Path as _Path

_pkm_kernels = None
HAS_CPP_KERNELS = False

if _os.environ.get("MMLLM_ENABLE_PKM_CPP", "").lower() == "true":
    try:
        from . import _pkm_kernels as _prebuilt  # type: ignore[attr-defined]
        _pkm_kernels = _prebuilt
        HAS_CPP_KERNELS = True
    except ImportError:
        # JIT-compile from the .cpp source bundled next to this file.
        try:
            from torch.utils.cpp_extension import load as _torch_load
            _src = _Path(__file__).parent / "_pkm_kernels.cpp"
            if _src.exists():
                _pkm_kernels = _torch_load(
                    name="_pkm_kernels",
                    sources=[str(_src)],
                    extra_cflags=["-fopenmp", "-O3", "-march=native", "-std=c++17"],
                    extra_ldflags=["-fopenmp"],
                    verbose=False,
                )
                HAS_CPP_KERNELS = True
        except Exception:  # noqa: BLE001 — JIT build failure → fall back
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


# ============================================================ #
# F-FULL — fused inference-only one-shot PKM forward
# ============================================================ #
# Reusable empty (0,) int64 tensor passed when no multi-trunk offset is
# needed. Allocated once at module import, never mutated. The C++ kernel
# treats `.numel() == 0` as "no offsets" and skips the per-batch add.
_EMPTY_OFFSETS: "torch.Tensor | None" = None


def _get_empty_offsets() -> torch.Tensor:
    global _EMPTY_OFFSETS
    if _EMPTY_OFFSETS is None:
        _EMPTY_OFFSETS = torch.empty((0,), dtype=torch.int64)
    return _EMPTY_OFFSETS


def pkm_inference_forward(
    memory_module,
    q: torch.Tensor,
    trunk_ids: "torch.Tensor | None" = None,
) -> torch.Tensor:
    """One-shot fused PKM forward — inference-only fast path.

    Pulls K_a, K_b, V.weight, top_k, sub_top_k, sub_dim, n_trunks,
    n_per_trunk from `memory_module` (a ProductKeyMemory or NetBank-tier
    PKM) and calls `_pkm_kernels.pkm_full_forward` exactly once.
    Returns the (B, T, q_dim) output. Drops top_global — inference
    doesn't use it.

    CONTRACT: caller must be under torch.no_grad() / module.training=False.
    The C++ kernel uses NoGradGuard internally but the Python boundary
    still won't track the inputs for backward; using this in a training
    loop would silently break grad flow.

    Falls back to memory_module.forward(q, trunk_ids) when:
      - HAS_CPP_KERNELS is False (extension didn't build)
      - V isn't on CPU (e.g. CUDA training; the fused kernel is CPU-only)
      - any input dtype isn't fp32 (we assume the bank is fp32 throughout)
    """
    V_weight = memory_module.V.weight
    if (not HAS_CPP_KERNELS
            or not V_weight.is_cpu
            or V_weight.dtype != torch.float32):
        # Fallback: full Python path. Use the existing forward() so the
        # behavior matches exactly. Caller is responsible for no_grad.
        return memory_module(q, trunk_ids=trunk_ids)

    # Q-norm via the functional API. The Module's .__call__ adds ~5 µs of
    # dispatch overhead per call; functional is the same math without it.
    # Matches Python forward exactly: self.q_norm(q) = F.rms_norm(q,
    # (q.shape[-1],), self.q_norm.weight, self.q_norm.eps).
    qn = memory_module.q_norm
    q_normed = F.rms_norm(q, (q.shape[-1],), qn.weight, qn.eps)

    # Multi-trunk offsets. Pass empty tensor when n_trunks == 1 or when
    # no trunk_ids were supplied (single-trunk default).
    if memory_module.n_trunks > 1 and trunk_ids is not None:
        offsets = (trunk_ids.to(dtype=torch.int64)
                            * memory_module.n_per_trunk).contiguous()
    else:
        offsets = _get_empty_offsets()

    out, _top_global = _pkm_kernels.pkm_full_forward(
        q_normed.contiguous(),
        memory_module.K_a.detach().contiguous(),
        memory_module.K_b.detach().contiguous(),
        V_weight.detach().contiguous() if not V_weight.is_contiguous() else V_weight.detach(),
        int(memory_module.sub_top_k),
        int(memory_module.top_k),
        offsets,
    )
    return out


def netbank_inference_forward(
    netbank_module,
    q: torch.Tensor,
) -> torch.Tensor:
    """One-shot fused NetBank forward — inference-only fast path.

    NetBank differs from ProductKeyMemory:
      - V_net stores c_net-dim bottleneck latents (not q_dim).
      - The weighted-sum output (B, T, c_net) is projected back to q_dim
        by a learned linear `expander` (Linear(c_net, q_dim)).
      - No multi-trunk routing (NetBank is a single shared tier).
      - No simulated network delay at inference.

    The C++ kernel handles V row width independent of q_dim, so it can
    return the (B, T, c_net) tensor in one fused call; the caller (this
    function) then runs the small Linear forward.

    Falls back to netbank_module.forward(q) when:
      - HAS_CPP_KERNELS is False
      - V isn't CPU fp32 (e.g. fp16 / cuda)
    """
    V_weight = netbank_module.V.weight
    if (not HAS_CPP_KERNELS
            or not V_weight.is_cpu
            or V_weight.dtype != torch.float32):
        return netbank_module(q)

    # Functional q_norm (skip Module dispatch).
    qn = netbank_module.q_norm
    q_normed = F.rms_norm(q, (q.shape[-1],), qn.weight, qn.eps)

    out_latent, _top_global = _pkm_kernels.pkm_full_forward(
        q_normed.contiguous(),
        netbank_module.K_a.detach().contiguous(),
        netbank_module.K_b.detach().contiguous(),
        V_weight.detach().contiguous() if not V_weight.is_contiguous() else V_weight.detach(),
        int(netbank_module.sub_top_k),
        int(netbank_module.top_k),
        _get_empty_offsets(),
    )
    # out_latent: (B, T, c_net) → expand to q_dim via the learned linear.
    return netbank_module.expander(out_latent)
