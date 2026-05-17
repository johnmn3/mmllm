"""Pure-Python attention + block-forward kernel.

Why this module exists: basilisp compiles to Python, but the resulting
data structures (persistent vectors, persistent maps, keyword keys) are
opaque to torch.compile/Dynamo, which refuses to trace them
("Dynamo does not know how to trace pvectorc.pvector"). It also caused
recompile-limit thrash on every cache-position change.

This module provides the per-block forward pass as a plain Python
function over Python-native data:
  - block fields are passed positionally (post-destructure on the
    basilisp side)
  - KV cache is a Python `tuple (k_buf, v_buf, pos)` — Python natives
    that torch.compile traces cleanly

basilisp's `attention` and `block-forward` become thin shims that
destructure the block map once and call into here. The outer layer
loop (in `forward`) stays in basilisp.

Phase-1c semantics preserved:
  - KV cache is pre-allocated to (B, n_kv, max_t, head_dim) on first
    forward; subsequent T_new tokens copy_ into slot [pos:pos+T_new].
  - Sliding-window narrows the SDPA view, not the buffer position.
  - Short tier RoPE; long tier no RoPE; bank queried via PKM with
    optional ctx-add modulation; long-tier outputs combined via gate.
"""
from __future__ import annotations

import os
from typing import Optional


def _compute_block_distill_inline(gate):
    """Per-block distillation MSE, computed inside the (potentially
    checkpointed) block forward scope so its autograd graph is part of
    the block's checkpointed return rather than a side-stash on the gate
    module. Reads gate.last_local_out / last_net_out / last_sdpa_out
    that the 3-way SwitchGate path just set, then immediately CLEARS
    those attributes so the autograd graph isn't pinned alive past the
    block. The returned scalar is what gets summed across blocks.

    Mirrors the standard path of core.lpy's collect-distill-loss (no
    per-layer gate-weights / gate-indices — those experimental knobs
    aren't supported through this fast path; if MMLLM_DISTILL_GATE_*
    is set, set MMLLM_GRAD_CHECKPOINT=false and use the old collector).

    Returns scalar tensor with autograd, or None when no distill term
    applies (2-way gate, or last_X not set)."""
    import torch.nn.functional as F
    lo = getattr(gate, "last_local_out", None)
    no = getattr(gate, "last_net_out",   None)
    so = getattr(gate, "last_sdpa_out",  None)
    # Clear immediately — having attempted to read them, we no longer
    # want the gate to pin them alive after we return.
    gate.last_local_out = None
    gate.last_net_out   = None
    gate.last_sdpa_out  = None
    if lo is None or no is None:
        return None
    target_kind = os.environ.get("MMLLM_DISTILL_TARGET", "residual")
    dir_only    = os.environ.get("MMLLM_DISTILL_DIRECTION_ONLY", "false").lower() in ("1", "true", "yes")
    try: mag_coef = float(os.environ.get("MMLLM_DISTILL_MAGNITUDE_COEF", "0.0"))
    except ValueError: mag_coef = 0.0
    try: mag_clamp = float(os.environ.get("MMLLM_DISTILL_MAGNITUDE_CLAMP", "0.0"))
    except ValueError: mag_clamp = 0.0
    eps = 1e-6
    if target_kind == "residual" and so is not None:
        tgt = lo.detach() - so.detach()
    else:
        tgt = lo.detach()
    if dir_only:
        tgt_n = tgt.norm(dim=-1, keepdim=True) + eps
        no_n  = no.norm(dim=-1, keepdim=True)  + eps
        dir_mse = F.mse_loss(no / no_n, tgt / tgt_n)
        if mag_coef > 0:
            tgt_mag = tgt_n.clamp(max=mag_clamp) if mag_clamp > 0 else tgt_n
            mag_mse = F.mse_loss(no_n, tgt_mag.detach())
            return (1.0 - mag_coef) * dir_mse + mag_coef * mag_mse
        return dir_mse
    return F.mse_loss(no, tgt)


def _bank_repeat_n() -> int:
    """How many iterative refinement passes through Local Bank to run
    per forward. Reads MMLLM_BANK_REPEAT_N (default 1 = no iteration,
    legacy behavior). When > 1, feeds the previous iteration's mem_out
    back into bank_q (scaled by MMLLM_BANK_REPEAT_ALPHA) and re-queries
    the bank. Cost scales linearly: ~+1 PKM lookup per extra repeat.
    Tier-3 spike #7+8."""
    try:
        return max(1, int(os.environ.get("MMLLM_BANK_REPEAT_N", "1")))
    except ValueError:
        return 1


def _bank_repeat_alpha() -> float:
    """Scale on the previous iteration's mem_out when feeding it back
    into bank_q. Reads MMLLM_BANK_REPEAT_ALPHA (default 0.1). Small
    so iterative refinement converges; too high diverges."""
    try:
        return float(os.environ.get("MMLLM_BANK_REPEAT_ALPHA", "0.1"))
    except ValueError:
        return 0.1

import torch
import torch.nn.functional as F
import torch.utils.checkpoint as _torch_checkpoint


# ── RoPE helpers (Python copy of the basilisp ones) ──

def _rotate_half(x: torch.Tensor) -> torch.Tensor:
    last_dim = x.dim() - 1
    half = x.size(last_dim) // 2
    x1 = x.narrow(last_dim, 0, half)
    x2 = x.narrow(last_dim, half, half)
    return torch.cat([-x2, x1], dim=-1)


def apply_rope(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    return x * cos + _rotate_half(x) * sin


# ── speculative-verify mask (Phase-5) ──

def _verify_mask(T: int, total_t: int, dtype, device) -> torch.Tensor:
    """Mask for speculative-decoding verify-K SDPA: K query positions
    over (prev_pos + K) key positions, where prev_pos = total_t - T.

    Query i (logical position prev_pos+i) attends to keys at positions
    0..prev_pos+i — sees the prior cache plus its own and earlier
    draft tokens, but not later draft tokens. Standard auto-regressive
    causal masking restricted to the K-batch suffix.

    Returns (T, total_t) additive mask: 0 where allowed, -inf where
    masked. Cheap to build per-call (~µs); not cached so the dtype/
    device are guaranteed correct without a global LRU.
    """
    prev_pos = total_t - T
    qi = torch.arange(T, device=device).unsqueeze(1)        # (T, 1)
    kj = torch.arange(total_t, device=device).unsqueeze(0)  # (1, total_t)
    masked = kj > (prev_pos + qi)                           # (T, total_t) bool
    out = torch.zeros(T, total_t, dtype=dtype, device=device)
    out.masked_fill_(masked, float("-inf"))
    return out


# ── KV cache append (Phase-1c, native tuple form) ──

def append_kv_to_buffer(
    cache: Optional[tuple],
    k_new: torch.Tensor,
    v_new: torch.Tensor,
    B: int,
    n_kv: int,
    max_t: int,
    head_dim: int,
) -> tuple:
    """Append (B, n_kv, T_new, head_dim) k/v to a pre-alloc'd KV cache.
    Returns a Python tuple `(k_buf, v_buf, new_pos)` that becomes the
    new cache. Allocates fresh buffers on the first call (cache=None).
    """
    T_new = k_new.size(2)
    if cache is not None:
        k_buf, v_buf, pos = cache
        new_pos = pos + T_new
        if new_pos > max_t:
            raise RuntimeError(
                f"KV cache overflow: pos={pos} + T_new={T_new} > max_t={max_t}. "
                f"Bump MMLLM_MAX_T."
            )
        k_buf.narrow(2, pos, T_new).copy_(k_new)
        v_buf.narrow(2, pos, T_new).copy_(v_new)
        return (k_buf, v_buf, new_pos)
    k_buf = torch.zeros(B, n_kv, max_t, head_dim,
                        dtype=k_new.dtype, device=k_new.device)
    v_buf = torch.zeros(B, n_kv, max_t, head_dim,
                        dtype=v_new.dtype, device=v_new.device)
    k_buf.narrow(2, 0, T_new).copy_(k_new)
    v_buf.narrow(2, 0, T_new).copy_(v_new)
    return (k_buf, v_buf, T_new)


# ── attention kernel ──

def attention(
    # block fields, all positional (basilisp destructures and passes)
    q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
    memory, long_gate, bank_query, bank_feedback,
    n_heads: int, n_short_heads: int, n_long_heads: int,
    n_short_kv_heads: int, n_long_kv_heads: int,
    head_dim: int, max_t: int,
    short_window: Optional[int], long_window: Optional[int],
    # tensor inputs
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor,
    short_cache: Optional[tuple], long_cache: Optional[tuple],
    *,
    skip_bank: bool = False,
    netbank=None,
    trunk_ids: Optional[torch.Tensor] = None,
) -> tuple:
    """Three-tier attention with hard-split Q heads.

    Returns (out, new_short_cache, new_long_cache) where each cache is
    a Python tuple (k_buf, v_buf, pos) — torch.compile-friendly.

    `skip_bank=True` (Phase-5 draft mode): bypass the PKM lookup
    entirely. attn_l_mem becomes 0; long_gate sees only the SDPA path.
    With SumGate / ScalarGate this gives a faithful "bank-zeroed"
    forward at ~17% lower FLOPs per layer (bank's K_a/K_b matmuls +
    top-k + gather are skipped). For SwitchGate the gating still
    multiplies the SDPA path by sigmoid(Q·w), so output is
    `gate · attn_l_sdpa` instead of `gate · attn_l_sdpa + (1-gate) · 0`,
    which is the same thing.

    `netbank` (optional): NetBank module for the third long-tier source.
    When provided, queried with the same bank_query as Local; result is
    passed as the 4th argument to long_gate (which switches to its
    3-way path). When None, gates fall back to 2-way.
    """
    B = x.size(0)
    T = x.size(1)

    # Clear any stale aux-loss stashes from prior step. Some attention
    # paths (skip_bank, 2-way gate on Net-only layers, …) don't reset
    # these; without an explicit clear, _compute_block_distill_inline
    # at end-of-attention would read tensors from a previous batch
    # whose autograd graph has been freed by backward — yielding either
    # a stale-grad scalar or a no-grad scalar that wrongly contributes
    # to the distill total.
    if long_gate is not None:
        long_gate.last_local_out = None
        long_gate.last_net_out   = None
        long_gate.last_sdpa_out  = None
    if memory is not None:
        memory.last_z_loss = None

    # Bank → dense feedback (PlainFeedback returns None → identity)
    fb_delta = bank_feedback(x, memory)
    x_for_q = x + fb_delta if fb_delta is not None else x

    # Q projection split into short/long groups
    q_full = q_proj(x_for_q).reshape(B, T, n_heads, head_dim)
    q_short = q_full.narrow(2, 0, n_short_heads).transpose(1, 2)
    q_long = q_full.narrow(2, n_short_heads, n_long_heads).transpose(1, 2)

    # K, V projections per tier
    k_s = k_proj_s(x).reshape(B, T, n_short_kv_heads, head_dim).transpose(1, 2)
    v_s = v_proj_s(x).reshape(B, T, n_short_kv_heads, head_dim).transpose(1, 2)
    k_l = k_proj_l(x).reshape(B, T, n_long_kv_heads,  head_dim).transpose(1, 2)
    v_l = v_proj_l(x).reshape(B, T, n_long_kv_heads,  head_dim).transpose(1, 2)

    # SHORT tier: RoPE on Q+K, append to cache, GQA expand, causal SDPA
    prev_short = short_cache[2] if short_cache is not None else 0
    cos_here_s = cos.narrow(0, prev_short, T)
    sin_here_s = sin.narrow(0, prev_short, T)
    q_short_r = apply_rope(q_short, cos_here_s, sin_here_s)
    k_s_r = apply_rope(k_s, cos_here_s, sin_here_s)

    new_short_cache = append_kv_to_buffer(
        short_cache, k_s_r, v_s, B, n_short_kv_heads, max_t, head_dim,
    )
    new_pos_s = new_short_cache[2]
    k_s_full = new_short_cache[0].narrow(2, 0, new_pos_s)
    v_s_full = new_short_cache[1].narrow(2, 0, new_pos_s)

    if short_window is not None and new_pos_s > short_window:
        k_s_full = k_s_full.narrow(2, new_pos_s - short_window, short_window)
        v_s_full = v_s_full.narrow(2, new_pos_s - short_window, short_window)

    repeat_s = n_short_heads // n_short_kv_heads
    k_s_rep = k_s_full.repeat_interleave(repeat_s, dim=1)
    v_s_rep = v_s_full.repeat_interleave(repeat_s, dim=1)
    # Three SDPA cases:
    #   T==1 decode:               no mask (single query attends to all)
    #   T>1 prefill (no cache):    is_causal=True (square triangular)
    #   T>1 verify (cache+K-batch): custom mask — query i attends to
    #                              keys [0..prev_short+i]; this is the
    #                              speculative-decoding case (Phase-5)
    # SDPA wraps: in TRAINING mode, the math backend (CPU's only path)
    # materializes the full (B, H, T, T) attn-weights tensor and retains
    # it for backward — 8 MB / call × 32 layers × 2 (short+long) = 8 GB
    # at B=16, T=1024. Wrapping each SDPA in torch.utils.checkpoint with
    # use_reentrant=False discards that tensor at forward and recomputes
    # it during backward, saving 8 GB.
    #
    # OPT-IN via MMLLM_SDPA_CHECKPOINT (default false). On CPU, the
    # recompute is the ENTIRE SDPA forward (no flash backend, just the
    # math kernel), which empirically costs ~20× per-step wall (38s/step
    # vs the unwrapped 1.7s/step at cpu-mini × wave-1 bandwidth). The
    # 8 GB saved is only worth that wall hit on tight containers, OR
    # when the model runs on GPU where pytorch's flash backend makes
    # the recompute cheap. Default off so CPU training stays usable.
    _wrap_sdpa = bool(
        os.environ.get("MMLLM_SDPA_CHECKPOINT", "false").lower() in ("1", "true", "yes")
    ) and torch.is_grad_enabled()
    def _sdpa(q_, k_, v_, *, is_causal=False, attn_mask=None):
        if _wrap_sdpa:
            return _torch_checkpoint.checkpoint(
                lambda q__, k__, v__: F.scaled_dot_product_attention(
                    q__, k__, v__, is_causal=is_causal, attn_mask=attn_mask),
                q_, k_, v_, use_reentrant=False)
        return F.scaled_dot_product_attention(q_, k_, v_, is_causal=is_causal, attn_mask=attn_mask)

    if short_cache is None and T > 1:
        attn_s = _sdpa(q_short_r, k_s_rep, v_s_rep, is_causal=True)
    elif short_cache is not None and T > 1:
        attn_s = _sdpa(q_short_r, k_s_rep, v_s_rep,
                       attn_mask=_verify_mask(T, k_s_rep.size(2), q_short_r.dtype, q_short_r.device))
    else:
        attn_s = _sdpa(q_short_r, k_s_rep, v_s_rep)

    # LONG tier (a): set-style SDPA over per-conversation cache (no RoPE)
    new_long_cache = append_kv_to_buffer(
        long_cache, k_l, v_l, B, n_long_kv_heads, max_t, head_dim,
    )
    new_pos_l = new_long_cache[2]
    k_l_full = new_long_cache[0].narrow(2, 0, new_pos_l)
    v_l_full = new_long_cache[1].narrow(2, 0, new_pos_l)

    if long_window is not None and new_pos_l > long_window:
        k_l_full = k_l_full.narrow(2, new_pos_l - long_window, long_window)
        v_l_full = v_l_full.narrow(2, new_pos_l - long_window, long_window)

    repeat_l = n_long_heads // n_long_kv_heads
    k_l_rep = k_l_full.repeat_interleave(repeat_l, dim=1)
    v_l_rep = v_l_full.repeat_interleave(repeat_l, dim=1)
    if long_cache is None and T > 1:
        attn_l_sdpa = _sdpa(q_long, k_l_rep, v_l_rep, is_causal=True)
    elif long_cache is not None and T > 1:
        attn_l_sdpa = _sdpa(q_long, k_l_rep, v_l_rep,
                            attn_mask=_verify_mask(T, k_l_rep.size(2), q_long.dtype, q_long.device))
    else:
        attn_l_sdpa = _sdpa(q_long, k_l_rep, v_l_rep)

    # LONG tier (b/c): retrieval. (b) is the local PKM bank (semantic /
    # working memory); (c) is NetBank (off-machine long-term memory),
    # only present when `netbank` is non-None. Phase-5 draft mode skips
    # both — saves the bank-side matmuls + gather + simulated network
    # latency. Required for SwitchGate's gate(1-gate) combiner to produce
    # only the SDPA contribution.
    if skip_bank:
        attn_l = attn_l_sdpa
    elif memory is None and netbank is None:
        # Asymmetric architecture: this layer has neither bank. Pass
        # through the SDPA tier unchanged.
        attn_l = attn_l_sdpa
    else:
        q_long_flat = (
            q_long.transpose(1, 2)
                  .contiguous()
                  .reshape(B, T, n_long_heads * head_dim)
        )
        ctx_mod = bank_query(x)
        bank_q = q_long_flat + ctx_mod if ctx_mod is not None else q_long_flat
        attn_l_mem = None
        if memory is not None:
            mem_out = memory(bank_q, trunk_ids=trunk_ids)
            # Iterative refinement on Local Bank — feed the previous output
            # back into bank_q and re-query, N times. Lets Local "deliberate"
            # at structural-decision positions. N=1 is identity (legacy).
            n_repeat = _bank_repeat_n()
            if n_repeat > 1:
                alpha = _bank_repeat_alpha()
                for _ in range(n_repeat - 1):
                    bank_q = bank_q + alpha * mem_out
                    mem_out = memory(bank_q, trunk_ids=trunk_ids)
            attn_l_mem = mem_out.reshape(B, T, n_long_heads, head_dim).transpose(1, 2)
        # NetBank queries off-machine. Same query vector as Local; the
        # gate decides per-token how much to weight each source.
        if netbank is not None:
            net_out = netbank(bank_q)
            attn_l_net = net_out.reshape(B, T, n_long_heads, head_dim).transpose(1, 2)
            if attn_l_mem is not None:
                attn_l = long_gate(q_long, attn_l_sdpa, attn_l_mem, attn_l_net)
            else:
                # Net-only layer (no Local Bank). Gate sees sdpa + net.
                # Pass mem_out=None; SwitchGate handles that branch.
                attn_l = long_gate(q_long, attn_l_sdpa, None, attn_l_net)
        else:
            attn_l = long_gate(q_long, attn_l_sdpa, attn_l_mem)

    # Per-block aux losses (distill MSE + z_loss). When grad-checkpointing
    # is OFF, collect them here (with autograd alive) and return them
    # through the block_forward chain so train-step doesn't need a
    # second pass over module-side .last_X stashes.
    # When grad-checkpointing is ON, skip — threading an autograd-alive
    # scalar through the checkpointed function's return alongside x_out
    # keeps the upstream context (NetBank.forward / Local-PKM.forward
    # intermediates) alive (PyTorch cannot independently checkpoint
    # multiple outputs with shared upstream graphs). Aux losses are
    # therefore disabled when MMLLM_GRAD_CHECKPOINT=true. Always clear
    # the module-side stashes so they don't pin autograd alive past
    # this block.
    grad_ckpt = os.environ.get("MMLLM_GRAD_CHECKPOINT", "false").lower() in ("1", "true", "yes")
    if grad_ckpt:
        # Clear stashes only — don't carry their autograd graphs out.
        if long_gate is not None:
            long_gate.last_local_out = None
            long_gate.last_net_out   = None
            long_gate.last_sdpa_out  = None
        if memory is not None:
            memory.last_z_loss = None
        distill_term = None
        z_term       = None
    else:
        distill_term = _compute_block_distill_inline(long_gate) if long_gate is not None else None
        z_term = None
        if memory is not None:
            zlz = getattr(memory, "last_z_loss", None)
            memory.last_z_loss = None
            if zlz is not None:
                z_term = zlz

    # Concat short + long head outputs, project
    attn = torch.cat([attn_s, attn_l], dim=1)
    out = attn.transpose(1, 2).contiguous().reshape(B, T, n_heads * head_dim)
    out = o_proj(out)

    return out, new_short_cache, new_long_cache, distill_term, z_term


# ── block forward (pre-norm + attention + SwiGLU FFN + residuals) ──

def block_forward(
    norm1, norm2,
    q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
    memory, long_gate, bank_query, bank_feedback,
    gate_proj, up_proj, down_proj,
    n_heads: int, n_short_heads: int, n_long_heads: int,
    n_short_kv_heads: int, n_long_kv_heads: int,
    head_dim: int, max_t: int,
    short_window: Optional[int], long_window: Optional[int],
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor,
    short_cache: Optional[tuple], long_cache: Optional[tuple],
    skip_bank: bool = False,
    netbank=None,
    trunk_ids: Optional[torch.Tensor] = None,
    skip_bwd: bool = False,
) -> tuple:
    """Pre-norm decoder block with three-tier attention + SwiGLU FFN.

    `skip_bank=True` (Phase-5 draft mode) routes through to the
    attention kernel; bank PKM lookup is skipped.
    `netbank` (optional): NetBank module for the off-machine long-term
    memory tier. When non-None, attention uses the 3-way long_gate path.

    `skip_bwd=True` runs the entire block (attention + FFN) inside a
    `torch.no_grad()` context — no autograd graph is built for the
    block's internal compute, so backward never traverses these params.
    The block's contribution is added to `x` OUTSIDE the no_grad context
    so `x`'s upstream gradient chain remains alive and earlier blocks
    still backward normally. Stochastic-depth-in-backward."""
    if skip_bwd:
        with torch.no_grad():
            attn_out, new_s, new_l, _d, _z = attention(
                q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
                memory, long_gate, bank_query, bank_feedback,
                n_heads, n_short_heads, n_long_heads,
                n_short_kv_heads, n_long_kv_heads, head_dim, max_t,
                short_window, long_window,
                norm1(x), cos, sin, short_cache, long_cache,
                skip_bank=skip_bank,
                netbank=netbank,
                trunk_ids=trunk_ids,
            )
            x_tmp = x + attn_out
            x_norm = norm2(x_tmp)
            ffn_out = down_proj(F.silu(gate_proj(x_norm)) * up_proj(x_norm))
            combined = attn_out + ffn_out
        # Outside no_grad — `combined` is a no-grad tensor (leaf); `x`
        # still has its grad_fn. The addition produces an output whose
        # backward propagates only to x. Block's internal params are
        # untouched by autograd.
        x_out = x + combined
        return x_out, new_s, new_l, None, None
    attn_out, new_s, new_l, distill_term, z_term = attention(
        q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
        memory, long_gate, bank_query, bank_feedback,
        n_heads, n_short_heads, n_long_heads,
        n_short_kv_heads, n_long_kv_heads, head_dim, max_t,
        short_window, long_window,
        norm1(x), cos, sin, short_cache, long_cache,
        skip_bank=skip_bank,
        netbank=netbank,
        trunk_ids=trunk_ids,
    )
    x = x + attn_out
    x_norm = norm2(x)
    ffn_out = down_proj(F.silu(gate_proj(x_norm)) * up_proj(x_norm))
    x = x + ffn_out
    # Per-block aux losses returned alongside x so their autograd
    # graphs flow through the (potentially checkpointed) block_forward
    # return rather than being pinned alive on module-side .last_X
    # attributes. See `attention` body for how these are collected.
    return x, new_s, new_l, distill_term, z_term


def checkpointed_block_forward(
    norm1, norm2,
    q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
    memory, long_gate, bank_query, bank_feedback,
    gate_proj, up_proj, down_proj,
    n_heads, n_short_heads, n_long_heads,
    n_short_kv_heads, n_long_kv_heads,
    head_dim, max_t, short_window, long_window,
    x, cos, sin, short_cache, long_cache,
    skip_bank=False, netbank=None, trunk_ids=None,
    skip_bwd: bool = False,
):
    """Gradient-checkpoint wrapper around `block_forward`.

    Same positional signature as `block_forward` so basilisp's
    destructure-then-call shim can target either function. Returns
    ONLY x_out — drops (short_cache, long_cache) outputs since
    train-step discards them. Single-tensor return avoids
    torch.utils.checkpoint's non-determinism check tripping on
    block_forward's mixed tensor+tuple return.

    Crucially, this is a top-level Python function (NOT a basilisp
    closure inside loop/recur). Each call's arguments live in their
    own Python locals, so the inner `_fn` closure cell holds the
    correct per-iteration values. A closure defined directly inside
    basilisp's `loop` shares cells across iterations (late-binding),
    so every checkpoint's backward recompute ends up using the LAST
    iteration's block — producing shape mismatches between the
    saved forward tensors and the recomputed ones.

    Returns `(x_out, None, None)` — distill_term / z_term are NOT
    threaded through the checkpoint return because doing so keeps
    upstream context alive (PyTorch cannot independently checkpoint
    multiple outputs with shared upstream graphs; the saved-tensor
    hooks fall back to retaining the shared intermediates). When
    grad-checkpointing is on, the aux losses are intentionally
    disabled by attention setting them to None — see the comment
    in `attention` above the per-block aux-loss collection.
    The (short_cache, long_cache) outputs are dropped (train-step
    discards them) so checkpoint sees only one tensor output."""
    # When skip_bwd is set, route directly through block_forward (which
    # has its own no-grad branch). No point checkpointing a no-grad
    # forward — the recompute on backward would never fire.
    if skip_bwd:
        x_out, _s, _l, _d, _z = block_forward(
            norm1, norm2,
            q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
            memory, long_gate, bank_query, bank_feedback,
            gate_proj, up_proj, down_proj,
            n_heads, n_short_heads, n_long_heads,
            n_short_kv_heads, n_long_kv_heads,
            head_dim, max_t, short_window, long_window,
            x, cos, sin, short_cache, long_cache,
            skip_bank=skip_bank, netbank=netbank, trunk_ids=trunk_ids,
            skip_bwd=True,
        )
        return x_out, None, None
    import torch.utils.checkpoint as _ckpt

    def _fn(x_arg):
        x_out, _s, _l, _d, _z = block_forward(
            norm1, norm2,
            q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
            memory, long_gate, bank_query, bank_feedback,
            gate_proj, up_proj, down_proj,
            n_heads, n_short_heads, n_long_heads,
            n_short_kv_heads, n_long_kv_heads,
            head_dim, max_t, short_window, long_window,
            x_arg, cos, sin, short_cache, long_cache,
            skip_bank=skip_bank, netbank=netbank, trunk_ids=trunk_ids,
        )
        return x_out

    x_ckpt = _ckpt.checkpoint(_fn, x, use_reentrant=False)
    # Match the 3-tuple shape callers expect.
    return x_ckpt, None, None
