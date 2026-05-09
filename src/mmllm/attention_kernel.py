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

from typing import Optional

import torch
import torch.nn.functional as F


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
    if short_cache is None and T > 1:
        attn_s = F.scaled_dot_product_attention(
            q_short_r, k_s_rep, v_s_rep, is_causal=True,
        )
    elif short_cache is not None and T > 1:
        attn_s = F.scaled_dot_product_attention(
            q_short_r, k_s_rep, v_s_rep,
            attn_mask=_verify_mask(T, k_s_rep.size(2), q_short_r.dtype, q_short_r.device),
        )
    else:
        attn_s = F.scaled_dot_product_attention(q_short_r, k_s_rep, v_s_rep)

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
        attn_l_sdpa = F.scaled_dot_product_attention(
            q_long, k_l_rep, v_l_rep, is_causal=True,
        )
    elif long_cache is not None and T > 1:
        attn_l_sdpa = F.scaled_dot_product_attention(
            q_long, k_l_rep, v_l_rep,
            attn_mask=_verify_mask(T, k_l_rep.size(2), q_long.dtype, q_long.device),
        )
    else:
        attn_l_sdpa = F.scaled_dot_product_attention(q_long, k_l_rep, v_l_rep)

    # LONG tier (b/c): retrieval. (b) is the local PKM bank (semantic /
    # working memory); (c) is NetBank (off-machine long-term memory),
    # only present when `netbank` is non-None. Phase-5 draft mode skips
    # both — saves the bank-side matmuls + gather + simulated network
    # latency. Required for SwitchGate's gate(1-gate) combiner to produce
    # only the SDPA contribution.
    if skip_bank:
        attn_l = attn_l_sdpa
    else:
        q_long_flat = (
            q_long.transpose(1, 2)
                  .contiguous()
                  .reshape(B, T, n_long_heads * head_dim)
        )
        ctx_mod = bank_query(x)
        bank_q = q_long_flat + ctx_mod if ctx_mod is not None else q_long_flat
        mem_out = memory(bank_q)
        attn_l_mem = mem_out.reshape(B, T, n_long_heads, head_dim).transpose(1, 2)
        # NetBank queries off-machine. Same query vector as Local; the
        # gate decides per-token how much to weight each source.
        if netbank is not None:
            net_out = netbank(bank_q)
            attn_l_net = net_out.reshape(B, T, n_long_heads, head_dim).transpose(1, 2)
            attn_l = long_gate(q_long, attn_l_sdpa, attn_l_mem, attn_l_net)
        else:
            attn_l = long_gate(q_long, attn_l_sdpa, attn_l_mem)

    # Concat short + long head outputs, project
    attn = torch.cat([attn_s, attn_l], dim=1)
    out = attn.transpose(1, 2).contiguous().reshape(B, T, n_heads * head_dim)
    out = o_proj(out)

    return out, new_short_cache, new_long_cache


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
) -> tuple:
    """Pre-norm decoder block with three-tier attention + SwiGLU FFN.

    `skip_bank=True` (Phase-5 draft mode) routes through to the
    attention kernel; bank PKM lookup is skipped.
    `netbank` (optional): NetBank module for the off-machine long-term
    memory tier. When non-None, attention uses the 3-way long_gate path."""
    attn_out, new_s, new_l = attention(
        q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
        memory, long_gate, bank_query, bank_feedback,
        n_heads, n_short_heads, n_long_heads,
        n_short_kv_heads, n_long_kv_heads, head_dim, max_t,
        short_window, long_window,
        norm1(x), cos, sin, short_cache, long_cache,
        skip_bank=skip_bank,
        netbank=netbank,
    )
    x = x + attn_out
    x_norm = norm2(x)
    ffn_out = down_proj(F.silu(gate_proj(x_norm)) * up_proj(x_norm))
    x = x + ffn_out
    return x, new_s, new_l
