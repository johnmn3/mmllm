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
        # Asymmetric architecture: mem_out=None on Net-only layers.
        if mem_out is None:
            return sdpa_out if net_out is None else sdpa_out + net_out
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
        # Asymmetric architecture: mem_out=None on Net-only layers.
        if mem_out is None:
            if net_out is None:
                return a * sdpa_out
            c = self.gamma.view(1, -1, 1, 1)
            return a * sdpa_out + c * net_out
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
        # alpha_net is owned by the parent block (not by SwitchGate) so
        # that adding it doesn't shift positional ckpt-load alignment for
        # params declared after gate_proj_3. The block sets it after
        # construction; defaults to None until set, in which case forward
        # runs with α=1 (identity).
        self.alpha_net: nn.Parameter | None = None
        # Net-default Bernoulli routing — attached after construction by the
        # block builder when MMLLM_GATE_NET_DEFAULT=true, same pattern as
        # alpha_net so ckpt-load alignment isn't shifted. When both are
        # None, forward runs the legacy 3-way softmax mix unchanged.
        #
        # local_active_proj: (n_long_heads, head_dim) — produces the per-
        # (B, H, T) logit for "Local should fire on this query".
        # local_active_bias: (n_long_heads,) — additive bias on that logit.
        # Init plan (set by block builder): proj=zeros, bias=-2.0 so the
        # initial Bernoulli firing rate is sigmoid(-2.0) ≈ 12% per query.
        # Net is the default (always runs); Local fires for ~12% of queries
        # at step 0, gate then learns from gradients.
        self.local_active_proj: nn.Parameter | None = None
        self.local_active_bias: nn.Parameter | None = None
        self.last_gate_dist = None      # tuple (sdpa, local, net) of floats or None
        self.last_local_out = None      # (B, H, T, D) tensor or None — for distillation
        self.last_net_out   = None      # (B, H, T, D) tensor or None — for distillation
        self.last_sdpa_out  = None      # (B, H, T, D) tensor or None — for residual distillation
                                        #   target = (local_out - sdpa_out).detach() — Net learns
                                        #   Local's UNIQUE contribution beyond sdpa, not Local's
                                        #   full output (the round-5 redundancy basin).
        self.last_local_firing_rate = None  # float — mean Bernoulli decision in last forward

    def forward(self, q_long, sdpa_out, mem_out, net_out=None):
        # Asymmetric architecture: layers without a Local Bank pass
        # mem_out=None. Reduce to a 2-way (sdpa + net) sigmoid mix using
        # the same gate_proj head — semantically "how much should this
        # layer trust Net vs SDPA?".
        if mem_out is None and net_out is not None:
            logits = torch.einsum("bhtd,hd->bht", q_long, self.gate_proj)
            gate = torch.sigmoid(logits)
            if self.training:
                with torch.no_grad():
                    g_mean = float(gate.mean().item())
                    self.last_gate_dist = (g_mean, float("nan"), 1.0 - g_mean)
            if self.alpha_net is not None:
                alpha = self.alpha_net.view(1, -1, 1, 1)
                net_out = alpha * net_out
            # PORT (port-distill-24layer): stash Net (and sdpa) so aggregate-local
            # distill can reach these Net-only layers. last_local_out stays None
            # (no Local Bank here); the collector uses the mean Local residual from
            # the 3-way layers as the shared target for every block's last_net_out.
            # Without this, 24/32 NetBanks were invisible to distill → Δ_net≈0.
            if self.training:
                self.last_local_out = None
                self.last_net_out   = net_out
                self.last_sdpa_out  = sdpa_out
            return gate.unsqueeze(-1) * sdpa_out + (1.0 - gate).unsqueeze(-1) * net_out
        if net_out is None:
            # q_long: (B, H, T, D); gate_proj: (H, D); logits: (B, H, T)
            logits = torch.einsum("bhtd,hd->bht", q_long, self.gate_proj)
            gate = torch.sigmoid(logits)
            if self.training:
                with torch.no_grad():
                    g_mean = float(gate.mean().item())
                    self.last_gate_dist = (g_mean, 1.0 - g_mean, float("nan"))
            return gate.unsqueeze(-1) * sdpa_out + (1.0 - gate).unsqueeze(-1) * mem_out
        # 3-way: q_long: (B, H, T, D); gate_proj_3: (H, 3, D); logits: (B, H, T, 3)
        logits = torch.einsum("bhtd,hkd->bhtk", q_long, self.gate_proj_3)
        weights = F.softmax(logits, dim=-1)                       # (B, H, T, 3)
        # Per-head alpha_net scaling on Net's path (attached after construction).
        if self.alpha_net is not None:
            alpha = self.alpha_net.view(1, -1, 1, 1)
            net_out = alpha * net_out
        # Stash per-tier outputs (still in autograd graph) for distillation.
        # last_sdpa_out enables residual-target distill: target =
        # (local - sdpa).detach() so Net learns Local's UNIQUE contribution
        # beyond sdpa, not Local's full output. Without that subtraction,
        # distill MSE(net, local) pulls Net to mimic Local; if Local is
        # already mostly sdpa+epsilon, Net learns sdpa, and Δ_net collapses
        # (the round-5 / round-8 redundancy basin).
        #
        # ONLY needed at training time. At inference these tensors are
        # never read — and stashing the full (B,H,T,D) tensors holds them
        # alive past the forward (memory pressure) and tying them to the
        # autograd graph in eval is wasted work.
        if self.training:
            self.last_local_out = mem_out
            self.last_net_out   = net_out
            self.last_sdpa_out  = sdpa_out

        # Legacy 3-way: full softmax mix (Net-default Bernoulli not attached).
        if self.local_active_proj is None:
            if self.training:
                with torch.no_grad():
                    mean_w = weights.mean(dim=(0, 1, 2))
                    self.last_gate_dist = (
                        float(mean_w[0].item()),
                        float(mean_w[1].item()),
                        float(mean_w[2].item()),
                    )
                    self.last_local_firing_rate = 1.0
            w0 = weights[..., 0].unsqueeze(-1)
            w1 = weights[..., 1].unsqueeze(-1)
            w2 = weights[..., 2].unsqueeze(-1)
            return w0 * sdpa_out + w1 * mem_out + w2 * net_out

        # Net-default path: straight-through Bernoulli gate on Local. Net
        # and sdpa always contribute; Local only fires when the gate says
        # so. The gate weights are renormalized so the surviving tiers
        # sum to 1 (when Local is skipped, sdpa+net share the full mass).
        #
        # local_logit: (B, H, T)
        local_logit = (torch.einsum("bhtd,hd->bht", q_long, self.local_active_proj)
                       + self.local_active_bias.view(1, -1, 1))
        local_prob = torch.sigmoid(local_logit)                   # (B, H, T)
        if self.training:
            # Stochastic Bernoulli sample so the gradient sees diverse decisions.
            rand = torch.rand_like(local_prob)
            local_hard = (local_prob > rand).float()
            # Straight-through: forward uses the hard 0/1 decision; backward
            # gets the sigmoid's smooth gradient through local_prob. The
            # `hard + soft - soft.detach()` trick keeps the value=hard and
            # ∂value/∂x = ∂soft/∂x.
            local_decision = local_hard + local_prob - local_prob.detach()
        else:
            # Eval mode: use the expected (smooth) value of the training-time
            # stochastic gate. E[local_decision | training] = local_prob,
            # because local_hard ~ Bernoulli(local_prob). Using local_prob
            # directly here makes eval deterministic AND non-degenerate: the
            # previous `(local_prob > 0.5)` thresholded to exactly 0 at
            # bias=-2.0 (the init), so Local never fired in eval and the
            # ablation Δ_local was always zero regardless of V_local content.
            # local_hard tracks the expected fire-rate for telemetry below.
            local_hard = local_prob
            local_decision = local_prob

        # Apply decision to Local's gate weight, then renormalize the
        # 3-way mass over the surviving tiers.
        w_sdpa  = weights[..., 0]                                 # (B, H, T)
        w_local = weights[..., 1] * local_decision                # zero where decision=0
        w_net   = weights[..., 2]
        total   = w_sdpa + w_local + w_net + 1e-6
        w_sdpa  = w_sdpa  / total
        w_local = w_local / total
        w_net   = w_net   / total

        if self.training:
            with torch.no_grad():
                self.last_gate_dist = (
                    float(w_sdpa.mean().item()),
                    float(w_local.mean().item()),
                    float(w_net.mean().item()),
                )
                self.last_local_firing_rate = float(local_hard.mean().item())

        return (w_sdpa.unsqueeze(-1)  * sdpa_out
              + w_local.unsqueeze(-1) * mem_out
              + w_net.unsqueeze(-1)   * net_out)


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
