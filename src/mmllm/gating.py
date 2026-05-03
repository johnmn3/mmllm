"""Long-tier path-mixing gates.

The long heads have TWO parallel sources at attention time:
  - attn_sdpa: SDPA over the per-conversation long-tier KV cache (k-proj-l, v-proj-l)
  - attn_mem:  product-key retrieval from the learned bank V

How those two get combined is a knob. This module ships three options
that all have the SAME (gate, sdpa, mem) → out signature, so the
attention block can swap between them without conditional code:

  - SumGate    (baseline): out = sdpa + mem
                  No learned parameters. The model has to balance the
                  two pathways implicitly through the gradient flow
                  into the upstream q-proj. Risk: SGD favors the easy
                  SDPA path, bank becomes dead weight.

  - ScalarGate: out = α[h] · sdpa + β[h] · mem
                  Two learnable scalars per long head. Cheap (2N
                  params total). Lets a head explicitly say "I'm a
                  recent-context head" (β→0) or "I'm a semantic-
                  memory head" (α→0). Init at α=β=1 (matches
                  SumGate behavior at step 0).

  - SwitchGate: gate[B,h,T] = sigmoid(Q · w_h)
                out = gate · sdpa + (1 - gate) · mem
                  Per-query convex mixing. The model picks per
                  position+head whether this query needs episodic
                  context (cache) or semantic memory (bank).
                  Linear over head_dim per long head. n_long_heads ×
                  head_dim params total. Init at zeros → sigmoid(0)
                  = 0.5 → balanced 50/50 mix at step 0.

All three return shape (B, n_long_heads, T, head_dim) — same as the
inputs sdpa_out and mem_out.
"""
import torch
import torch.nn as nn


class SumGate(nn.Module):
    """Baseline: pass through the sum, no learned parameters."""

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()

    def forward(self, q_long, sdpa_out, mem_out):
        return sdpa_out + mem_out


class ScalarGate(nn.Module):
    """Per-head learned scalars α, β. Initial α=β=1."""

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()
        self.alpha = nn.Parameter(torch.ones(n_long_heads))
        self.beta = nn.Parameter(torch.ones(n_long_heads))

    def forward(self, q_long, sdpa_out, mem_out):
        a = self.alpha.view(1, -1, 1, 1)
        b = self.beta.view(1, -1, 1, 1)
        return a * sdpa_out + b * mem_out


class SwitchGate(nn.Module):
    """Per-query convex mixing via sigmoid(Q · w_h). Init weights = 0
    → sigmoid(0) = 0.5 → 50/50 mix at step 0."""

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()
        self.gate_proj = nn.Parameter(torch.zeros(n_long_heads, head_dim))

    def forward(self, q_long, sdpa_out, mem_out):
        # q_long: (B, H, T, D); gate_proj: (H, D); logits: (B, H, T)
        logits = torch.einsum("bhtd,hd->bht", q_long, self.gate_proj)
        gate = torch.sigmoid(logits).unsqueeze(-1)
        return gate * sdpa_out + (1.0 - gate) * mem_out


def build_gate(kind: str, n_long_heads: int, head_dim: int) -> nn.Module:
    """Factory: 'sum' | 'scalar' | 'switch' → gate Module."""
    if kind == "sum":
        return SumGate(n_long_heads, head_dim)
    if kind == "scalar":
        return ScalarGate(n_long_heads, head_dim)
    if kind == "switch":
        return SwitchGate(n_long_heads, head_dim)
    raise ValueError(
        f"unknown long-tier-mix kind: {kind!r} "
        f"(expected one of 'sum', 'scalar', 'switch')"
    )
