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
    byte position — fully data-driven.

    Numerical guard: log_p_true is clamped to >= -50 before use.
    Without this, an extremely peaked softmax (log p_true → -∞ when
    a bank lookup or projection produces a huge logit gap) produces
    NaN in backward via the `p_true * log_p_true = 0 * -∞` term in
    the gradient of `(1-p)^γ * log p`. Clamping at -50 keeps loss
    finite (bounded by ~50) and eliminates the NaN path. This was
    seen empirically: at step 18050 the loaded ckpt produced a
    pathological logit distribution that triggered the NaN guard."""
    log_p = F.log_softmax(logits, dim=-1)                       # (..., V)
    # Gather log p for the true class, then clamp away -inf path.
    log_p_true = log_p.gather(-1, y.unsqueeze(-1)).squeeze(-1)   # (...,)
    log_p_true = log_p_true.clamp(min=-50.0)
    p_true = log_p_true.exp()                                    # in [exp(-50), 1]
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
    """Per-position difficulty predictor — Linear(d_model, 1) + softplus
    over the model's final hidden state. Output is a non-negative scalar
    per position, intended to estimate how hard the next-byte prediction
    is at that position.

    DESIGN — read carefully (v1 had a degenerate bug; this is v2):

      * IH is trained via a SEPARATE aux loss (MSE against detached
        per_pos_ce), not via the main loss it modulates. The
        train-step decouples the two paths so the optimizer can't
        learn to suppress IH output to "free" loss reduction.

      * As a multiplier on the main loss, IH is ALSO detached and
        re-normalized to mean=1 per batch. Detach prevents gradient
        flow from main loss into IH. Mean-1 normalization preserves
        the total loss magnitude so IH only RE-BALANCES per-position
        weight — easy bytes get < 1×, hard bytes get > 1×.

      * Bias init = inverse_softplus(1.0) = ln(e - 1) ≈ 0.5413 so
        softplus(0 + bias) ≈ 1.0 at step 0. Matches "uniform mean-1
        weight" baseline: identical to plain mean CE before IH starts
        differentiating. (v1 had bias=0 → output ≈ 0.69 → loss looked
        ~30% lower than plain CE — confusing.)

    v1 bug for posterity: gradient on IH from main loss `imp·CE` is
    `per_pos_ce`, which is positive. Optimizer minimized loss by
    pushing IH DOWN on hard bytes (the opposite of intent). Net
    effect was IH collapsed toward 0 on hard bytes, training signal
    vanished, model drifted into NaN."""

    # Inverse of softplus at y=1: x such that ln(1 + e^x) = 1.
    # Solve: e^x = e - 1, x = ln(e - 1) ≈ 0.5413.
    _BIAS_INIT = 0.5413248546129181

    def __init__(self, d_model: int):
        super().__init__()
        self.proj = nn.Linear(d_model, 1, bias=True)
        nn.init.zeros_(self.proj.weight)
        nn.init.constant_(self.proj.bias, self._BIAS_INIT)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """x: (B, T, d_model) → (B, T) softplus-transformed difficulty.
        softplus is a smooth >0 activation so the multiplier is always
        positive and differentiable everywhere."""
        return F.softplus(self.proj(x)).squeeze(-1)


def importance_weighted_loss(per_pos_ce: torch.Tensor,
                             importance_raw: torch.Tensor,
                             aux_coef: float = 1.0,
                             eps: float = 1e-8) -> torch.Tensor:
    """v2 importance-weighted loss with decoupled gradient paths.

    Args
    ----
    per_pos_ce     : (N,) — per-position CE loss (with grad; flows back
                     through the model's logits).
    importance_raw : (N,) — IH(final_x) output (with grad; flows back
                     ONLY through the aux MSE, NOT through the main
                     loss multiplication).
    aux_coef       : scale on the IH self-supervised aux loss.
                     1.0 is a reasonable default (per-position MSE
                     between IH and per_pos_ce; same units as CE).
    eps            : numerical floor on imp_used.mean() before
                     dividing — prevents 0/0 if IH predicts 0.

    Returns scalar loss = main_weighted_mean + aux_coef · ih_aux_mse.

    Path semantics:
      * imp_used = importance_raw.detach() / max(mean(imp_used), eps)
        → mean = 1, all positive, NO grad path back to IH.
      * weighted = imp_used · per_pos_ce  (grad path: per_pos_ce only)
      * aux = MSE(importance_raw, per_pos_ce.detach())  (grad path: IH only)

    Result: IH learns to predict per-position CE; that prediction is
    used (detached, mean-1) as a re-balancing weight; main optimizer
    sees a per-position-reweighted CE that conserves total magnitude."""
    imp_detached = importance_raw.detach()
    imp_mean = imp_detached.mean().clamp(min=eps)
    imp_used = imp_detached / imp_mean                        # mean = 1, no grad
    weighted_main = (imp_used * per_pos_ce).mean()            # grad → CE / model
    ih_aux = F.mse_loss(importance_raw, per_pos_ce.detach())  # grad → IH only
    return weighted_main + aux_coef * ih_aux


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

    Init: gate weights = zero AND output scalar α = zero → gate output
    is zero AND scaled-residual is zero at step 0 → exact identity.
    Differentiable through both gate and α; both grow during training.

    Magnitude bound: without normalization, the EMA scales with x's
    magnitude (decay=0.992 ema → mean of last ~86 x_t), so a non-zero
    gate would make carry ≈ gate · x. Then `x + carry ≈ (1+gate)·x`
    is multiplicative, and across 5 layers per forward × many forwards
    this produces exponential growth in x → eventual overflow at the
    deepest block. Empirically: NaN at block-4-out by step ~18700 in
    a real training run with carry on.

    Fix: RMSNorm the carry residual before adding back, and gate the
    whole thing by a zero-init learnable scalar α. RMSNorm bounds the
    residual to unit-RMS regardless of EMA magnitude; α grows linearly
    during training so the additive contribution to x is `α · O(1)`,
    not `O(x)`. Linear (not exponential) growth across layers.

    v1 used softmax over zero gate logits → uniform weights → non-zero
    carry at init, broke ckpt back-compat. v2 dropped softmax (raw
    linear gate, zero-init → carry=0 at init). v3 (this version) adds
    out-norm + α to bound steady-state magnitude — carry is still
    exact identity at init."""

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
        # Small-random init (NOT zero) so gate(x) · ema is nonzero at
        # step 0 — that's what gives `out_norm.weight` a nonzero
        # gradient. If gate were zero AND out_norm.weight were zero,
        # the entire carry path would be `0 · 0 = 0` and BOTH grads
        # would also be zero — module permanently stuck. Small std
        # keeps initial residual magnitude small after norm × weight.
        self.gate = nn.Linear(d_model, n_clocks, bias=False)
        nn.init.normal_(self.gate.weight, std=0.01)
        # RMSNorm on the carry residual. Two roles:
        #
        #   1. Bound residual magnitude to ~|weight|·unit-RMS regardless
        #      of EMA size. Breaks the multiplicative-on-x feedback loop
        #      that caused block-4-out NaN at step ~18700.
        #
        #   2. The norm's `weight` parameter starts at 0 (overridden
        #      below) so the residual is exact 0 at step 0 — module
        #      is identity at init. The weight itself has a nonzero
        #      gradient on the first backward (via dL/dweight = dL/dy
        #      · normalized_carry), so the optimizer can grow it during
        #      training and the carry comes online smoothly.
        self.out_norm = nn.RMSNorm(d_model)
        nn.init.zeros_(self.out_norm.weight)

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
        # Bound the residual magnitude regardless of EMA size. With
        # out_norm.weight zero-init, the residual is exact 0 at init
        # (identity); weight grows during training and the carry comes
        # online smoothly with bounded magnitude.
        return x + self.out_norm(out_carry)


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
