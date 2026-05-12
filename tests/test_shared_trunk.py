"""Smoke tests for shared-trunk (option A) multi-trunk Local Bank routing.

These exercise `ProductKeyMemory` and `attention_kernel.block_forward` at
N_TRUNKS=1 (legacy) and N_TRUNKS=2 (multi-trunk) to verify:

  1. The trunk_ids kwarg routes per-batch-row gather into the right V slice.
  2. Swapping trunk_ids produces different outputs (proves the routing
     isn't ignored).
  3. The N=1 legacy path (no trunk_ids passed) still works.
  4. Sparse gradients land at the right (trunk, row) cells on backward.

Run with: python3 -m pytest tests/test_shared_trunk.py -v
"""
from __future__ import annotations
import os
import sys

# Force bank_on_gpu=true so we exercise the plain nn.Embedding path
# (no mmap). The routing logic is identical on both code paths; the
# mmap path adds I/O we don't need here.
os.environ.setdefault("MMLLM_BANK_ON_GPU", "true")

import torch
import torch.nn as nn

# Make the src/ tree importable when invoked without an install.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mmllm.memory import ProductKeyMemory
from mmllm.attention_kernel import block_forward


def _build_stub_block(d_model: int, n_heads: int, n_short_heads: int,
                      n_long_heads: int, head_dim: int, d_ff: int):
    """Construct the dense modules + gates needed by block_forward."""
    q_proj    = nn.Linear(d_model, n_heads * head_dim, bias=False)
    k_proj_s  = nn.Linear(d_model, 1 * head_dim, bias=False)
    v_proj_s  = nn.Linear(d_model, 1 * head_dim, bias=False)
    k_proj_l  = nn.Linear(d_model, 1 * head_dim, bias=False)
    v_proj_l  = nn.Linear(d_model, 1 * head_dim, bias=False)
    o_proj    = nn.Linear(n_heads * head_dim, d_model, bias=False)
    norm1     = nn.RMSNorm(d_model)
    norm2     = nn.RMSNorm(d_model)
    gate_proj = nn.Linear(d_model, d_ff, bias=False)
    up_proj   = nn.Linear(d_model, d_ff, bias=False)
    down_proj = nn.Linear(d_ff, d_model, bias=False)

    class _SumGate(nn.Module):
        def forward(self, q_long, sdpa, mem, net=None):
            return sdpa + mem if net is None else sdpa + mem + net

    class _PlainBankQuery(nn.Module):
        def forward(self, x):
            return None

    class _PlainFeedback(nn.Module):
        def forward(self, x, memory):
            return None

    return dict(
        q_proj=q_proj, k_proj_s=k_proj_s, v_proj_s=v_proj_s,
        k_proj_l=k_proj_l, v_proj_l=v_proj_l, o_proj=o_proj,
        norm1=norm1, norm2=norm2,
        gate_proj=gate_proj, up_proj=up_proj, down_proj=down_proj,
        long_gate=_SumGate(), bank_query=_PlainBankQuery(),
        bank_feedback=_PlainFeedback(),
    )


def _identity_rope(max_t, head_dim):
    """RoPE-shape cos/sin tensors that produce identity rotation (no-op)."""
    return torch.ones(max_t, head_dim), torch.zeros(max_t, head_dim)


def _run_block(memory, block, x, trunk_ids, n_heads, n_short_heads,
               n_long_heads, head_dim, max_t):
    cos, sin = _identity_rope(max_t, head_dim)
    return block_forward(
        block["norm1"], block["norm2"],
        block["q_proj"], block["k_proj_s"], block["v_proj_s"],
        block["k_proj_l"], block["v_proj_l"], block["o_proj"],
        memory, block["long_gate"], block["bank_query"], block["bank_feedback"],
        block["gate_proj"], block["up_proj"], block["down_proj"],
        n_heads, n_short_heads, n_long_heads, 1, 1, head_dim, max_t,
        None, None,
        x, cos, sin, None, None,
        skip_bank=False, netbank=None,
        trunk_ids=trunk_ids,
    )


# ── tests ──

def test_n1_legacy_forward_runs():
    """At N_TRUNKS=1 (default), trunk_ids=None — same code path as
    pre-multi-trunk. Forward must return the expected output shape."""
    torch.manual_seed(0)
    d_model, n_heads, n_short_heads, n_long_heads = 16, 4, 2, 2
    head_dim = d_model // n_heads
    q_dim = n_long_heads * head_dim  # = 8
    block = _build_stub_block(d_model, n_heads, n_short_heads, n_long_heads,
                              head_dim, d_ff=32)
    mem = ProductKeyMemory(q_dim=q_dim, sqrt_n=4, top_k=2, sub_top_k=2)
    assert mem.n == 16
    assert mem.n_trunks == 1
    assert mem.V.weight.shape == (16, q_dim)

    x = torch.randn(2, 3, d_model)
    out, _, _ = _run_block(mem, block, x, None,
                           n_heads, n_short_heads, n_long_heads, head_dim, 8)
    assert out.shape == (2, 3, d_model), f"unexpected out shape {out.shape}"


def test_n2_routing_changes_output():
    """At N_TRUNKS=2 with distinct V values per trunk, swapping trunk_ids
    must change the gathered values (proves routing is actually used,
    not silently fallen back to trunk-0)."""
    torch.manual_seed(0)
    d_model, n_heads, n_short_heads, n_long_heads = 16, 4, 2, 2
    head_dim = d_model // n_heads
    q_dim = n_long_heads * head_dim  # = 8
    sqrt_n = 4
    block = _build_stub_block(d_model, n_heads, n_short_heads, n_long_heads,
                              head_dim, d_ff=32)
    mem = ProductKeyMemory(q_dim=q_dim, sqrt_n=sqrt_n, top_k=2, sub_top_k=2,
                            n_trunks=2)
    assert mem.n == 32
    assert mem.V.weight.shape == (32, q_dim)

    n_per_trunk = sqrt_n * sqrt_n  # 16
    with torch.no_grad():
        mem.V.weight[:n_per_trunk]  =  1.0   # trunk 0
        mem.V.weight[n_per_trunk:]  = -1.0   # trunk 1

    x = torch.randn(2, 3, d_model)
    out_a, _, _ = _run_block(mem, block, x,
                             torch.tensor([0, 1], dtype=torch.long),
                             n_heads, n_short_heads, n_long_heads, head_dim, 8)
    out_b, _, _ = _run_block(mem, block, x,
                             torch.tensor([1, 0], dtype=torch.long),
                             n_heads, n_short_heads, n_long_heads, head_dim, 8)

    diff = (out_a - out_b).abs().mean().item()
    assert diff > 1e-4, (
        f"trunk-id swap should change output materially, got mean-abs-diff={diff}"
    )


def test_n2_sparse_grad_partitions_by_trunk():
    """After backward, the sparse gradient on V.weight should touch rows
    in trunk 0's slice [0, n_per_trunk) AND trunk 1's slice
    [n_per_trunk, 2*n_per_trunk) — at least one row in each."""
    torch.manual_seed(0)
    q_dim, sqrt_n = 8, 4
    mem = ProductKeyMemory(q_dim=q_dim, sqrt_n=sqrt_n, top_k=2, sub_top_k=2,
                            n_trunks=2)
    n_per_trunk = sqrt_n * sqrt_n
    q = torch.randn(2, 4, q_dim)
    trunk_ids = torch.tensor([0, 1], dtype=torch.long)

    out = mem(q, trunk_ids=trunk_ids)
    out.sum().backward()
    grad = mem.V.weight.grad
    assert grad.is_sparse, "expected sparse grad on V.weight"
    rows = grad.coalesce().indices()[0]
    n_t0 = int((rows <  n_per_trunk).sum().item())
    n_t1 = int((rows >= n_per_trunk).sum().item())
    assert n_t0 > 0, "trunk 0 should receive at least one gradient row"
    assert n_t1 > 0, "trunk 1 should receive at least one gradient row"


if __name__ == "__main__":
    test_n1_legacy_forward_runs()
    test_n2_routing_changes_output()
    test_n2_sparse_grad_partitions_by_trunk()
    print("OK")
