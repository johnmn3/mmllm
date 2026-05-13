"""Tests for the PKM C++ kernels (F2 gather, F3 fused topk, F-FULL).

Run with: pytest tests/test_pkm_kernels.py -x

If _pkm_kernels didn't build (HAS_CPP_KERNELS=False), the whole module
is skipped — the fallback path is exercised by the existing memory.py
test suite.
"""

import os

# Force the C++ extension on for these tests, even though the default is
# off in production (the extension is opt-in via MMLLM_ENABLE_PKM_CPP).
os.environ.setdefault("MMLLM_ENABLE_PKM_CPP", "true")

import pytest
import torch
import torch.nn.functional as F

from mmllm._pkm_autograd import (
    HAS_CPP_KERNELS,
    PKMGather,
    PKMFusedTopK,
    pkm_inference_forward,
    _pkm_kernels,
)

pytestmark = pytest.mark.skipif(
    not HAS_CPP_KERNELS,
    reason="_pkm_kernels C++ extension not built",
)


# ============================================================ #
# F2 — gather (read-only on V; sparse grad on backward)
# ============================================================ #
def test_gather_numerical_eq():
    """C++ memcpy gather equals F.embedding bitwise (no math, just copies)."""
    V = torch.randn(51_200, 64)
    idx = torch.randint(0, V.shape[0], (2, 4, 16), dtype=torch.long)
    assert torch.equal(PKMGather.apply(V, idx), F.embedding(idx, V))


def test_gather_autograd():
    """Sparse grad on V matches dense F.embedding backward after coalesce."""
    torch.manual_seed(0)
    V1 = torch.randn(1024, 32, requires_grad=True)
    V2 = V1.detach().clone().requires_grad_(True)
    idx = torch.randint(0, 1024, (3, 5, 8), dtype=torch.long)

    out_cpp = PKMGather.apply(V1, idx)
    out_ref = F.embedding(idx, V2)
    out_cpp.sum().backward()
    out_ref.sum().backward()

    grad_cpp_dense = V1.grad.to_dense() if V1.grad.is_sparse else V1.grad
    grad_ref_dense = V2.grad.to_dense() if V2.grad.is_sparse else V2.grad
    assert torch.allclose(grad_cpp_dense, grad_ref_dense, atol=1e-6)


def test_gather_empty_idx():
    """Edge case: idx with zero elements returns shape (..., D) tensor cleanly."""
    V = torch.randn(100, 16)
    idx = torch.empty((0,), dtype=torch.long)
    assert PKMGather.apply(V, idx).shape == (0, 16)


# ============================================================ #
# F3 — fused outer-sum + top-K
# ============================================================ #
def test_fused_topk_eq():
    """Fused C++ equals current Python outer-sum + topk.

    Tie-break caveat: when two (ia, ib) pairs have identical score, the
    Python torch.topk and the C++ min-heap may pick different ones. To
    avoid spurious failures, we use random fp32 inputs (collision
    probability ~0) and assert on sorted score multisets.
    """
    torch.manual_seed(42)
    B, T, S, K, sqrt_n = 2, 3, 32, 16, 2048
    top_a_s = torch.randn(B, T, S)
    top_a_i = torch.randint(0, sqrt_n, (B, T, S), dtype=torch.long)
    top_b_s = torch.randn(B, T, S)
    top_b_i = torch.randint(0, sqrt_n, (B, T, S), dtype=torch.long)

    ts_cpp, tg_cpp = PKMFusedTopK.apply(
        top_a_s, top_a_i, top_b_s, top_b_i, sqrt_n, K
    )

    # Python reference
    combined = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
    idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, S)
    idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, S, -1)
    combined_idx = (idx_a * sqrt_n + idx_b).flatten(-2)
    ts_py, top_local = combined.topk(K, dim=-1)
    tg_py = combined_idx.gather(-1, top_local)

    # Sorted multisets agree (handles unsorted output order).
    assert torch.allclose(
        ts_cpp.sort(-1).values, ts_py.sort(-1).values, atol=1e-5
    )
    assert torch.equal(tg_cpp.sort(-1).values, tg_py.sort(-1).values)


def test_fused_topk_autograd():
    """Gradients route to top_a_s + top_b_s at the chosen local positions.

    The C++ kernel breaks ties (identical (a_s + b_s) sums) by (ia, ib)
    ascending, while torch.topk uses an unspecified tie-break. Even with
    random fp32 scores, when duplicate global keys appear in top_a_i /
    top_b_i, the gradient at one local position can shift to a different
    local position with the same global key. To avoid that confound, use
    UNIQUE global indices per (b, t) row — matches the real sub-key topk
    output, which is by construction unique.
    """
    torch.manual_seed(7)
    B, T, S, K, sqrt_n = 1, 2, 16, 8, 256

    top_a_s_1 = torch.randn(B, T, S, requires_grad=True)
    top_b_s_1 = torch.randn(B, T, S, requires_grad=True)
    top_a_s_2 = top_a_s_1.detach().clone().requires_grad_(True)
    top_b_s_2 = top_b_s_1.detach().clone().requires_grad_(True)

    # Unique global indices per row — sample without replacement.
    top_a_i = torch.stack([
        torch.stack([torch.randperm(sqrt_n)[:S] for _ in range(T)])
        for _ in range(B)
    ]).to(torch.long)
    top_b_i = torch.stack([
        torch.stack([torch.randperm(sqrt_n)[:S] for _ in range(T)])
        for _ in range(B)
    ]).to(torch.long)

    ts_1, _ = PKMFusedTopK.apply(top_a_s_1, top_a_i, top_b_s_1, top_b_i, sqrt_n, K)
    ts_1.sum().backward()

    combined = (top_a_s_2.unsqueeze(-1) + top_b_s_2.unsqueeze(-2)).flatten(-2)
    ts_2, _ = combined.topk(K, dim=-1)
    ts_2.sum().backward()

    assert torch.allclose(top_a_s_1.grad, top_a_s_2.grad, atol=1e-5)
    assert torch.allclose(top_b_s_1.grad, top_b_s_2.grad, atol=1e-5)


# ============================================================ #
# F-FULL — pkm_full_forward
# ============================================================ #
@torch.no_grad()
def test_pkm_full_forward_eq():
    """Fused C++ forward equals ProductKeyMemory.forward (Python path).

    Construct a tiny PKM module on CPU, run forward in:
      (1) C++ fast path (default when not training + HAS_CPP_KERNELS + V cpu)
      (2) Python slow path (via .train() mode to bypass the guard — z-loss
          and hit counters get computed but the math is identical)

    Assert outputs match to fp32 precision. Skips the .item() telemetry
    branch (it's only active in training and is non-functional anyway).
    """
    from mmllm.memory import ProductKeyMemory

    torch.manual_seed(0)
    q_dim, sqrt_n, top_k, sub_top_k = 16, 32, 16, 16
    B, T = 2, 4

    m = ProductKeyMemory(
        q_dim=q_dim, sqrt_n=sqrt_n, top_k=top_k, sub_top_k=sub_top_k,
        n_trunks=1,
    )
    # Randomize V (default is N(0, 0.02))
    with torch.no_grad():
        m.V.weight.copy_(torch.randn_like(m.V.weight) * 0.5)

    q = torch.randn(B, T, q_dim)

    # (1) C++ fast path
    m.eval()
    out_cpp = m(q)

    # (2) Python slow path — bypass the guard by going through training mode.
    # We still want no grad to keep it cheap; the math doesn't depend on
    # training mode beyond the no-op z-loss / counters.
    m.train()
    out_py = m(q)
    m.eval()

    # ProductKeyMemory in training mode does an extra .item() at the end
    # for telemetry, but the returned tensor is the same. fp32 precision.
    assert torch.allclose(out_cpp, out_py, atol=1e-5, rtol=1e-5), (
        f"C++ vs Python mismatch: max |diff| = {(out_cpp - out_py).abs().max().item()}"
    )


@torch.no_grad()
def test_pkm_full_forward_shape():
    """Output shape is (B, T, q_dim) regardless of B/T/top_k."""
    from mmllm.memory import ProductKeyMemory

    torch.manual_seed(1)
    q_dim, sqrt_n = 16, 16
    for B, T, top_k, sub_top_k in [(1, 1, 4, 8), (3, 5, 16, 16), (2, 8, 8, 8)]:
        m = ProductKeyMemory(
            q_dim=q_dim, sqrt_n=sqrt_n, top_k=top_k, sub_top_k=sub_top_k,
        )
        m.eval()
        q = torch.randn(B, T, q_dim)
        out = m(q)
        assert out.shape == (B, T, q_dim), f"B={B} T={T} → shape={out.shape}"


@torch.no_grad()
def test_pkm_full_forward_no_autograd():
    """C++ path returns a tensor with no grad_fn (inference contract)."""
    from mmllm.memory import ProductKeyMemory

    torch.manual_seed(2)
    m = ProductKeyMemory(q_dim=16, sqrt_n=32, top_k=8, sub_top_k=16)
    m.eval()

    # Even with requires_grad=True on input, the C++ fast path must not
    # attach a grad graph. (Inside no_grad ctx the test is trivially true;
    # without the ctx, the C++ kernel's NoGradGuard is what saves us.)
    q = torch.randn(2, 3, 16, requires_grad=True)
    # Force-disable the test-level no_grad by using a small inner block.
    with torch.enable_grad():
        out = m(q)
    assert out.grad_fn is None, (
        f"Inference C++ path leaked autograd: grad_fn={out.grad_fn}"
    )


@torch.no_grad()
def test_pkm_full_forward_multi_trunk():
    """row_offsets correctly route batch rows to per-trunk V slices."""
    from mmllm.memory import ProductKeyMemory

    torch.manual_seed(3)
    q_dim, sqrt_n, top_k, sub_top_k = 16, 16, 8, 8
    n_trunks = 4
    B, T = n_trunks, 2

    m = ProductKeyMemory(
        q_dim=q_dim, sqrt_n=sqrt_n, top_k=top_k, sub_top_k=sub_top_k,
        n_trunks=n_trunks,
    )
    m.eval()
    # Make each trunk's V slice distinguishable: trunk t has values
    # filled with sentinel value (t + 1).
    n_per_trunk = sqrt_n * sqrt_n
    with torch.no_grad():
        for t in range(n_trunks):
            m.V.weight.data[t * n_per_trunk:(t + 1) * n_per_trunk] = (t + 1) * 0.1

    q = torch.randn(B, T, q_dim)
    trunk_ids = torch.arange(n_trunks, dtype=torch.long)
    out = m(q, trunk_ids=trunk_ids)

    # Each batch row b should produce values centered around (b+1)*0.1
    # (softmax of any top_k entries all with the same value → same value
    # everywhere → output equals that constant scalar).
    for b in range(n_trunks):
        expected = (b + 1) * 0.1
        assert torch.allclose(out[b], torch.full_like(out[b], expected), atol=1e-5), (
            f"batch row {b}: expected {expected}, got mean={out[b].mean().item()}"
        )


@torch.no_grad()
def test_netbank_inference_forward_eq():
    """C++ fast path on NetBank equals NetBank.forward (Python path).

    NetBank uses V with c_net rows (different from q_dim); the kernel must
    handle the row-width difference and the caller's expander projection.
    """
    from mmllm.netbank import NetBank

    torch.manual_seed(0)
    q_dim, sqrt_n, c_net = 16, 32, 8
    top_k, sub_top_k = 16, 16
    B, T = 2, 4

    m = NetBank(
        q_dim=q_dim, sqrt_n=sqrt_n, c_net=c_net,
        top_k=top_k, sub_top_k=sub_top_k,
        mmap_path=None,
        delay_ms_min=0.0, delay_ms_max=0.0,
        bank_on_gpu=False,
    )
    # Randomize V (default is N(0, 0.02))
    with torch.no_grad():
        m.V.weight.copy_(torch.randn_like(m.V.weight) * 0.5)

    q = torch.randn(B, T, q_dim)

    # (1) C++ fast path
    m.eval()
    out_cpp = m(q)

    # (2) Python path
    m.train()
    out_py = m(q)
    m.eval()

    assert out_cpp.shape == (B, T, q_dim)
    assert torch.allclose(out_cpp, out_py, atol=1e-5, rtol=1e-5), (
        f"NetBank C++ vs Python mismatch: max |diff| = "
        f"{(out_cpp - out_py).abs().max().item()}"
    )


@torch.no_grad()
def test_pkm_full_forward_v_dim_neq_q_dim():
    """Kernel handles V row width independent of q_dim (NetBank shape)."""
    torch.manual_seed(5)
    B, T, q_dim = 2, 3, 16
    sub_dim = q_dim // 2
    sqrt_n = 32
    sub_top_k, top_k = 16, 16
    c_net = 8                  # V row width != q_dim
    n_rows = sqrt_n * sqrt_n

    q_normed = torch.randn(B, T, q_dim)
    K_a = torch.randn(sqrt_n, sub_dim) * 0.02
    K_b = torch.randn(sqrt_n, sub_dim) * 0.02
    V = torch.randn(n_rows, c_net) * 0.5
    empty_offsets = torch.empty((0,), dtype=torch.int64)

    out, top_global = _pkm_kernels.pkm_full_forward(
        q_normed.contiguous(),
        K_a.contiguous(),
        K_b.contiguous(),
        V.contiguous(),
        sub_top_k, top_k,
        empty_offsets,
    )

    # Output shape uses V's row width, not q_dim.
    assert out.shape == (B, T, c_net), f"got {out.shape}"
    assert top_global.shape == (B, T, top_k)
    assert top_global.min() >= 0
    assert top_global.max() < n_rows


@torch.no_grad()
def test_pkm_full_forward_direct_call():
    """Direct call to _pkm_kernels.pkm_full_forward (no Python wrapper)."""
    torch.manual_seed(4)
    B, T, q_dim = 2, 3, 16
    sub_dim = q_dim // 2
    sqrt_n = 32
    sub_top_k, top_k = 16, 16
    n_rows = sqrt_n * sqrt_n

    q_normed = torch.randn(B, T, q_dim)
    K_a = torch.randn(sqrt_n, sub_dim) * 0.02
    K_b = torch.randn(sqrt_n, sub_dim) * 0.02
    V = torch.randn(n_rows, q_dim) * 0.5
    empty_offsets = torch.empty((0,), dtype=torch.int64)

    out, top_global = _pkm_kernels.pkm_full_forward(
        q_normed.contiguous(),
        K_a.contiguous(),
        K_b.contiguous(),
        V.contiguous(),
        sub_top_k, top_k,
        empty_offsets,
    )

    assert out.shape == (B, T, q_dim)
    assert top_global.shape == (B, T, top_k)
    assert top_global.dtype == torch.int64
    assert top_global.min() >= 0
    assert top_global.max() < n_rows

    # Reference: same computation in PyTorch.
    q_a = q_normed[..., :sub_dim]
    q_b = q_normed[..., sub_dim:]
    scores_a = q_a @ K_a.t()
    scores_b = q_b @ K_b.t()
    top_a_s, top_a_i = scores_a.topk(sub_top_k, dim=-1)
    top_b_s, top_b_i = scores_b.topk(sub_top_k, dim=-1)
    combined_scores = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
    idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, sub_top_k)
    idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, sub_top_k, -1)
    combined_idx = (idx_a * sqrt_n + idx_b).flatten(-2)
    top_scores_ref, top_local = combined_scores.topk(top_k, dim=-1)
    top_global_ref = combined_idx.gather(-1, top_local)
    values = V[top_global_ref]
    weights = F.softmax(top_scores_ref, dim=-1).unsqueeze(-1)
    out_ref = (weights * values).sum(dim=-2)

    assert torch.allclose(out, out_ref, atol=1e-5, rtol=1e-5), (
        f"direct call vs PyTorch ref: max |diff| = {(out - out_ref).abs().max().item()}"
    )
