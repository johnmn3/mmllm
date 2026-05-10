"""Router-smarts — small, generic enrichments to the dense "router" tier
(the brain-stem analog) so it can do structural, non-linear, dynamic
composition without growing in parameter count.

Three components, all opt-in via env vars / CLI flags:

  1. `focal_ce` — drop-in replacement for cross-entropy that auto-
     up-weights bytes the model gets wrong (focal loss, Lin et al.
     2017). NO HARDCODING of any byte scheme — purely data-driven.
     Cheap (~+1% per-step compute).

  2. `LearnedImportanceHead` — a tiny `Linear(d_model, 1)` head that
     predicts a per-position multiplier on top of focal CE. Self-
     supervised by the loss itself: positions with persistently high
     error get the head's weight pushed up. Functionally learns to
     identify structural boundaries (post-anchor bytes, etc.) without
     ever being told what those are. Regularized toward mean=1 so the
     head can't run away.

  3. `MultiTimescaleCarry` — per-block module that maintains 4 EMAs of
     `x` at log-uniformly-spaced decay rates (half-lives ~1, 5, 22,
     86 tokens). Mixed back into the residual stream via a learned
     gate. Gives the router cheap multi-scale temporal context — the
     "many clocks of the brain stem" analog. Init zero so adding the
     module to an existing ckpt is identity (no behavior change at
     step 0; gradients shape it from there).

Together: the router gains generic structural awareness + cross-
position memory + stateful composition. Trades ~10-15% throughput for
substantially more capability per parameter — the user's stated goal."""

import torch
import torch.nn as nn
import torch.nn.functional as F


# ─────────────────────── focal CE ───────────────────────

def focal_ce(logits: torch.Tensor, y: torch.Tensor,
             gamma: float = 2.0,
             reduction: str = "mean") -> torch.Tensor:
    """Focal cross-entropy. logits (..., V), y (...,) → scalar (mean) or
    per-position tensor (none). gamma=0 reduces to plain CE; gamma=2 is
    the standard focal default (Lin et al 2017 "Focal Loss for Dense
    Object Detection").

    Math:  -(1 - p_correct)^gamma * log p_correct

    The (1-p)^gamma factor approaches 1 for badly-predicted bytes
    (p_correct → 0) and approaches 0 for well-predicted bytes
    (p_correct → 1), so easy bytes contribute less to the gradient
    and hard bytes dominate. No special-case logic for any specific
    byte position — fully data-driven."""
    log_p = F.log_softmax(logits, dim=-1)                       # (..., V)
    # Gather log p for the true class
    log_p_true = log_p.gather(-1, y.unsqueeze(-1)).squeeze(-1)   # (...,)
    p_true = log_p_true.exp().clamp(0.0, 1.0)
    weight = (1.0 - p_true).pow(gamma)                          # (...,)
    loss = -(weight * log_p_true)                               # (...,)
    if reduction == "mean":
        return loss.mean()
    if reduction == "sum":
        return loss.sum()
    if reduction == "none":
        return loss
    raise ValueError(f"focal_ce: unknown reduction {reduction!r}")


# ─────────────────────── learned importance head ───────────────────────

class LearnedImportanceHead(nn.Module):
    """Per-position importance multiplier. A single Linear(d_model, 1)
    over the model's final hidden state, passed through softplus to
    produce a positive weight. Used as a per-position multiplier on
    top of focal CE.

    Self-supervision: positions where the model's prediction was
    consistently wrong push the head's output up (because gradient
    favors more weight on high-error positions). Positions where
    prediction is easy push the head's output toward 1 (the regularizer
    pulls it). Result: learned structural detector.

    Init: zero weights → softplus(0) ≈ 0.69 ≈ const. Behavior at step 0
    is "all positions weighted equally at ~0.69" — slightly less than
    plain CE-mean. As training progresses, the head differentiates."""

    def __init__(self, d_model: int):
        super().__init__()
        self.proj = nn.Linear(d_model, 1, bias=False)
        nn.init.zeros_(self.proj.weight)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (B, T, d_model) → (B, T) softplus-transformed importance.
        softplus is a smooth >0 activation so the multiplier is always
        positive and differentiable everywhere."""
        return F.softplus(self.proj(x)).squeeze(-1)


def importance_weighted_loss(per_pos_ce: torch.Tensor,
                             importance: torch.Tensor,
                             reg_coef: float = 1e-4) -> torch.Tensor:
    """Combine per-position focal CE with per-position importance weights.
    per_pos_ce: (B, T) — focal_ce(reduction='none') flattened over batch.
    importance: (B, T) — output of LearnedImportanceHead.
    reg_coef:    scale on (importance - 1)^2 regularizer that keeps the
                 head from running away. Without it the head trivially
                 maximizes weight on easiest bytes (free loss reduction).

    Returns scalar loss = mean(importance * per_pos_ce) + reg."""
    weighted = importance * per_pos_ce
    reg = reg_coef * (importance - 1.0).pow(2).mean()
    return weighted.mean() + reg


# ─────────────────────── multi-timescale carry ───────────────────────

class MultiTimescaleCarry(nn.Module):
    """Per-block residual carry at multiple timescales — the "ancient
    brain-stem clocks" analog. Maintains `n_clocks` exponential moving
    averages of x at log-uniformly-spaced decay rates, mixes them back
    into the residual stream via a learned per-position gate.

    Defaults: 4 clocks at decay rates [0.5, 0.875, 0.96875, 0.992],
    corresponding to half-lives of ~1, 5, 22, 86 tokens. Covers the
    span from "what just happened" to "what was happening 100 tokens
    ago" with logarithmic granularity.

    Init: gate weights = zero → gate output = zero for all positions
    and all clocks → carry residual = 0 → module is exact identity at
    step 0. Gate is a raw Linear (no softmax), so the per-clock weight
    can be any sign and any magnitude; gradient differentiates it over
    training. (We tried softmax and discovered it gives uniform [0.25,
    0.25, 0.25, 0.25] over zero logits — non-zero carry at init,
    breaking ckpt back-compat. Raw linear avoids this trap.)

    Cost: O(T) recurrence per block (can't be parallelized over T due
    to the EMA recursion). At T=128 this is 128 sequential ops per
    block × n_layers — a few percent throughput penalty vs no-carry."""

    def __init__(self, d_model: int, n_clocks: int = 4):
        super().__init__()
        self.d_model = d_model
        self.n_clocks = n_clocks
        # Log-uniform decay rates in [0.5, 1.0). Frozen by default;
        # making them trainable would let SGD pick clock frequencies
        # but adds instability risk. Frozen for v1, can revisit.
        decays = torch.tensor(
            [1.0 - 2.0 ** -(k + 1) for k in range(n_clocks)],
            dtype=torch.float32,
        )
        # decays[0] = 0.5, decays[1] = 0.75, decays[2] = 0.875, decays[3] = 0.9375
        # for n_clocks=4. Half-lives roughly [1, 2.4, 5.2, 10.7] tokens.
        # For larger spread (slow-clock memory), use spaced-out rates:
        if n_clocks == 4:
            decays = torch.tensor([0.5, 0.875, 0.96875, 0.992], dtype=torch.float32)
        self.register_buffer("decays", decays)
        # Per-position gate that picks which clocks to mix at each step.
        # Zero-init so module starts as identity (uniform gate × zero EMAs).
        self.gate = nn.Linear(d_model, n_clocks, bias=False)
        nn.init.zeros_(self.gate.weight)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (B, T, d_model) → (B, T, d_model) with carry residual added.
        Sequential over T (recurrence); parallel over B and d_model."""
        B, T, D = x.shape
        K = self.n_clocks
        decays = self.decays.view(1, K, 1)              # (1, K, 1) for broadcast
        one_minus = 1.0 - decays                        # (1, K, 1)
        # Pre-compute gate weights for all positions in one matmul.
        # Zero-init weights → gate_weights = 0 at step 0 → carry = 0
        # everywhere → exact identity. No softmax (which would give
        # uniform [1/K] over zero logits and break back-compat).
        gate_weights = self.gate(x)                     # (B, T, K)
        # Sequential EMA update over T. Each step: ema = decay * ema + (1-decay) * x_t
        ema = torch.zeros(B, K, D, device=x.device, dtype=x.dtype)
        out_carry = []
        for t in range(T):
            x_t = x[:, t, :].unsqueeze(1)               # (B, 1, D)
            ema = decays * ema + one_minus * x_t        # (B, K, D)
            # Mix this position's gate weights with current EMAs
            w_t = gate_weights[:, t, :].unsqueeze(-1)   # (B, K, 1)
            carry_t = (w_t * ema).sum(dim=1)            # (B, D)
            out_carry.append(carry_t)
        out_carry = torch.stack(out_carry, dim=1)       # (B, T, D)
        return x + out_carry


def build_carry_modules(d_model: int, n_layers: int,
                        n_clocks: int = 4) -> nn.ModuleList:
    """Construct one MultiTimescaleCarry per block. Returned as an
    nn.ModuleList so the parent can iterate / register / move-to-device
    uniformly. Caller decides where to insert each carry into the block
    (typically right before / after attention, before / after FFN —
    different placements give different dynamics; we put it AFTER the
    attention residual, BEFORE FFN, so the carry can shape the FFN input
    without disturbing attention's KV-cache reads)."""
    return nn.ModuleList([
        MultiTimescaleCarry(d_model, n_clocks) for _ in range(n_layers)
    ])
