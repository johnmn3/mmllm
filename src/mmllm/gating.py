"""Long-tier path-mixing gates.

The long heads have up to THREE parallel sources at attention time:
  - attn_sdpa: SDPA over the per-conversation long-tier KV cache (k-proj-l, v-proj-l)
  - attn_mem:  product-key retrieval from the learned LOCAL bank V
  - attn_net:  product-key retrieval from the learned NETBANK V (off-machine, optional)

How those get combined is a knob. This module ships gates that all have the
same `(gate, sdpa, mem, net) → out` signature so the attention block can swap
between them without conditional code. When `net` is None (NetBank disabled),
each gate falls back to its 2-source behavior.

  - SumGate    (baseline): out = sdpa + mem (+ net)
                  No learned parameters. Risk: SGD favors the easy
                  SDPA path, bank/netbank become dead weight.

  - ScalarGate: out = α[h] · sdpa + β[h] · mem (+ γ[h] · net)
                  Per-head learnable scalars. Lets a head explicitly say
                  "I'm a recent-context head" or "I'm a semantic-memory
                  head" or "I'm a long-term-memory head". Init at all-1s
                  (matches SumGate behavior at step 0).

  - SwitchGate: 2-way: gate = sigmoid(Q · w_h); out = gate · sdpa + (1-gate) · mem
                3-way: weights = softmax(Q · W_3way); out = w0·sdpa + w1·mem + w2·net
                  Per-query convex mixing. The model picks per position
                  + head which source to consult. Linear over head_dim;
                  zero-init → uniform 1/N mix at step 0.

All return shape (B, n_long_heads, T, head_dim) — same as the inputs.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class SumGate(nn.Module):
    """Baseline: pass through the sum of available inputs, no learned parameters."""

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()

    def forward(self, q_long, sdpa_out, mem_out, net_out=None):
        if net_out is None:
            return sdpa_out + mem_out
        return sdpa_out + mem_out + net_out


class ScalarGate(nn.Module):
    """Per-head learned scalars. 2-way: α, β. 3-way: α, β, γ. All init 1."""

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()
        self.alpha = nn.Parameter(torch.ones(n_long_heads))
        self.beta = nn.Parameter(torch.ones(n_long_heads))
        # γ used only when net_out is provided. Always present so ckpts
        # are stable across NetBank-on/off training sessions.
        self.gamma = nn.Parameter(torch.ones(n_long_heads))

    def forward(self, q_long, sdpa_out, mem_out, net_out=None):
        a = self.alpha.view(1, -1, 1, 1)
        b = self.beta.view(1, -1, 1, 1)
        if net_out is None:
            return a * sdpa_out + b * mem_out
        c = self.gamma.view(1, -1, 1, 1)
        return a * sdpa_out + b * mem_out + c * net_out


class SwitchGate(nn.Module):
    """Per-query convex mixing.

    2-way: sigmoid(q · w_h) → gate ∈ [0,1]; out = gate · sdpa + (1-gate) · mem.
    3-way: softmax(q · W_3way) → weights ∈ Δ²; out = w0·sdpa + w1·mem + w2·net.

    Both `gate_proj` (2-way) and `gate_proj_3` (3-way) are stored so the
    same module supports either branch depending on whether net_out is
    provided. Both are zero-init → balanced mix at step 0.

    Diagnostic: stores `last_gate_dist`, the most recent forward's mean
    gate weights `(sdpa_frac, local_frac, net_frac)` averaged over
    (B, H, T). 2-way fills net_frac with NaN. None until first forward.
    Logged at slot-log events to track tier-utilization drift over time.

    Distillation hooks: in 3-way mode also stashes `last_local_out` and
    `last_net_out` (the raw per-tier attention contributions, shape
    (B, H, T, D)) so train-step can compute a Net→Local distillation
    loss across all blocks. Both still in the autograd graph; train-step
    detaches Local in the loss path so only Net learns to mimic Local.
    Cleared after each forward to avoid stale tensors holding GPU memory.
    """

    def __init__(self, n_long_heads: int, head_dim: int):
        super().__init__()
        # 2-way path (kept for backward compatibility with NetBank-disabled runs).
        self.gate_proj = nn.Parameter(torch.zeros(n_long_heads, head_dim))
        # 3-way path. Output 3 logits per (head, position) → softmax.
        self.gate_proj_3 = nn.Parameter(torch.zeros(n_long_heads, 3, head_dim))
        self.last_gate_dist = None  # tuple (sdpa, local, net) of floats or None
        self.last_local_out = None  # (B, H, T, D) tensor or None — for distillation
        self.last_net_out   = None  # (B, H, T, D) tensor or None — for distillation

    def forward(self, q_long, sdpa_out, mem_out, net_out=None):
        if net_out is None:
            # q_long: (B, H, T, D); gate_proj: (H, D); logits: (B, H, T)
            logits = torch.einsum("bhtd,hd->bht", q_long, self.gate_proj)
            gate = torch.sigmoid(logits)
            with torch.no_grad():
                g_mean = float(gate.mean().item())
                self.last_gate_dist = (g_mean, 1.0 - g_mean, float("nan"))
            return gate.unsqueeze(-1) * sdpa_out + (1.0 - gate).unsqueeze(-1) * mem_out
        # 3-way: q_long: (B, H, T, D); gate_proj_3: (H, 3, D); logits: (B, H, T, 3)
        logits = torch.einsum("bhtd,hkd->bhtk", q_long, self.gate_proj_3)
        weights = F.softmax(logits, dim=-1)                       # (B, H, T, 3)
        with torch.no_grad():
            # Average over (B, H, T) → 3 floats summing to 1.
            mean_w = weights.mean(dim=(0, 1, 2))
            self.last_gate_dist = (
                float(mean_w[0].item()),
                float(mean_w[1].item()),
                float(mean_w[2].item()),
            )
        # Stash per-tier attention outputs (still in autograd graph) so
        # train-step can compute Net→Local distillation across all blocks.
        # Detach happens in train-step's loss path, not here.
        self.last_local_out = mem_out
        self.last_net_out   = net_out
        w0 = weights[..., 0].unsqueeze(-1)
        w1 = weights[..., 1].unsqueeze(-1)
        w2 = weights[..., 2].unsqueeze(-1)
        return w0 * sdpa_out + w1 * mem_out + w2 * net_out


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
