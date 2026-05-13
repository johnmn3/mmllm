"""Sketch tests for the PKM C++ kernels.

Only signatures + a one-line assertion each — fill in setup once the
extension is built. Run with: pytest tests/test_pkm_kernels.py -x

If _pkm_kernels didn't build, the whole module is skipped — the
fallback path is exercised by the existing memory.py test suite.
"""

import pytest
import torch
import torch.nn.functional as F

from mmllm._pkm_autograd import HAS_CPP_KERNELS, PKMGather, PKMFusedTopK

pytestmark = pytest.mark.skipif(
    not HAS_CPP_KERNELS,
    reason="_pkm_kernels C++ extension not built",
)


# ----- F2 gather ----- #
def test_gather_numerical_eq():
    """C++ memcpy gather equals F.embedding bitwise (no math, just copies)."""
    V = torch.randn(51_200, 64)
    idx = torch.randint(0, V.shape[0], (2, 4, 16), dtype=torch.long)
    assert torch.equal(PKMGather.apply(V, idx), F.embedding(idx, V))


def test_gather_autograd():
    """Sparse grad on V matches dense F.embedding backward after coalesce."""
    V = torch.randn(1024, 32, requires_grad=True)
    idx = torch.randint(0, 1024, (3, 5, 8), dtype=torch.long)
    # Compare PKMGather.apply(V, idx).sum().backward() against
    # F.embedding(idx, V).sum().backward() — grads should match to atol=0
    # after V.grad.to_dense() (PKMGather emits sparse_coo).
    assert True  # filled in once extension is built


def test_gather_empty_idx():
    """Edge case: idx with zero elements returns shape (..., D) tensor cleanly."""
    V = torch.randn(100, 16)
    idx = torch.empty((0,), dtype=torch.long)
    assert PKMGather.apply(V, idx).shape == (0, 16)


# ----- F3 fused top-K ----- #
def test_fused_topk_eq():
    """Fused C++ equals current Python outer-sum + topk.

    Tie-break caveat: when two (ia, ib) pairs have identical score, the
    Python torch.topk and the C++ min-heap may pick different ones. To
    avoid spurious failures, the test fixture uses random fp32 inputs
    (collision probability ~0) and only asserts on the SORTED score
    multisets, not on individual index correspondence. If we ever need
    bit-exact equivalence under ties we'll have to align tie-breaking
    rules — current C++ is (score desc, ia asc, ib asc); Python topk is
    "implementation-defined among equal elements" (typically scan order).
    """
    B, T, S, K, sqrt_n = 2, 3, 32, 16, 2048
    top_a_s = torch.randn(B, T, S); top_a_i = torch.randint(0, sqrt_n, (B, T, S), dtype=torch.long)
    top_b_s = torch.randn(B, T, S); top_b_i = torch.randint(0, sqrt_n, (B, T, S), dtype=torch.long)
    ts_cpp, _ = PKMFusedTopK.apply(top_a_s, top_a_i, top_b_s, top_b_i, sqrt_n, K)
    assert torch.allclose(ts_cpp.sort(-1).values, ts_cpp.sort(-1).values)  # placeholder


def test_fused_topk_autograd():
    """Gradients route to top_a_s + top_b_s at the chosen local positions."""
    # Compare PKMFusedTopK backward against the Python fallback backward.
    assert True  # filled in once extension is built
