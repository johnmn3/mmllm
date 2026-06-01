"""MLX transformer block: dual-tier attention (RoPE/GQA/SDPA short+long) +
PKM bank retrieval + gate + SwiGLU. Mirrors attention_kernel.py's EVAL forward
(no KV cache, T>1 causal prefill — the path eval-bpc / training use).

Each block is driven by a plain param dict `b` (extracted from the torch model
by role), keeping the forward a pure function of (params, x) so model.forward
can be wrapped in mx.value_and_grad later (Stage 2).
"""
from __future__ import annotations

import math
import mlx.core as mx

from mmllm.mlx import banks


def rope_cache(max_seq_len, head_dim, theta):
    """(cos, sin) each (max_seq_len, head_dim). Matches core.lpy build-rope-cache."""
    idx = mx.arange(0, head_dim, 2).astype(mx.float32)
    inv_freq = mx.exp(-(idx / head_dim) * math.log(theta))
    pos = mx.arange(max_seq_len).astype(mx.float32)
    freqs = mx.outer(pos, inv_freq)                       # (T, head_dim/2)
    cos = mx.concatenate([mx.cos(freqs), mx.cos(freqs)], axis=-1)
    sin = mx.concatenate([mx.sin(freqs), mx.sin(freqs)], axis=-1)
    return cos, sin


def _rotate_half(x):
    half = x.shape[-1] // 2
    return mx.concatenate([-x[..., half:], x[..., :half]], axis=-1)


def _apply_rope(x, cos, sin):
    return x * cos + _rotate_half(x) * sin


def _rms_norm(x, w, eps):
    return (x * mx.rsqrt(mx.mean(x * x, axis=-1, keepdims=True) + eps)) * w


def _sdpa_causal(q, k, v, head_dim):
    # q,k,v: (B,H,T,hd). MLX fused SDPA with causal mask (T>1 prefill path).
    return mx.fast.scaled_dot_product_attention(
        q, k, v, scale=1.0 / math.sqrt(head_dim), mask="causal"
    )


def _gqa(x, repeat):
    # repeat_interleave along the head axis (axis=1): (B,Hkv,T,hd)->(B,Hkv*r,T,hd)
    return mx.repeat(x, repeat, axis=1) if repeat > 1 else x


def sum_gate(q_long, sdpa_out, mem_out, net_out=None, collect_distill=False):
    """SumGate: unweighted sum of available tiers (no params). No distill."""
    if mem_out is None:
        out = sdpa_out if net_out is None else sdpa_out + net_out
    elif net_out is None:
        out = sdpa_out + mem_out
    else:
        out = sdpa_out + mem_out + net_out
    return (out, None) if collect_distill else out


def switch_gate_eval(p, q_long, sdpa_out, mem_out, net_out=None, collect_distill=False):
    """SwitchGate EVAL forward (gating.py:135). p holds gate params (some None):
    gate_proj (H,D), gate_proj_3 (H,3,D), alpha_net (H,)|None,
    local_active_proj (H,D)|None, local_active_bias (H,)|None.

    Eval uses local_decision = local_prob (the smooth expectation of the
    training-time Bernoulli) — matches the eval branch exactly.

    When collect_distill and BOTH mem & net are present, also returns the
    per-block distill MSE (net learns Local's UNIQUE-vs-sdpa residual contribution,
    target detached) — mirrors _compute_block_distill_inline's default
    (target=residual). distill is None on 2-way / SumGate layers."""
    distill = None
    if mem_out is None and net_out is not None:        # 2-way sdpa+net (Net-only layer)
        gate = mx.sigmoid(mx.einsum("bhtd,hd->bht", q_long, p["gate_proj"]))
        if p.get("alpha_net") is not None:
            net_out = p["alpha_net"].reshape(1, -1, 1, 1) * net_out
        out = gate[..., None] * sdpa_out + (1.0 - gate)[..., None] * net_out
    elif net_out is None:                              # 2-way sdpa+mem
        gate = mx.sigmoid(mx.einsum("bhtd,hd->bht", q_long, p["gate_proj"]))
        out = gate[..., None] * sdpa_out + (1.0 - gate)[..., None] * mem_out
    else:
        weights = mx.softmax(mx.einsum("bhtd,hkd->bhtk", q_long, p["gate_proj_3"]), axis=-1)
        if p.get("alpha_net") is not None:
            net_out = p["alpha_net"].reshape(1, -1, 1, 1) * net_out
        if p.get("local_active_proj") is None:         # legacy 3-way softmax mix
            out = (weights[..., 0:1] * sdpa_out + weights[..., 1:2] * mem_out
                   + weights[..., 2:3] * net_out)
        else:                                          # Net-default Bernoulli (eval)
            local_logit = (mx.einsum("bhtd,hd->bht", q_long, p["local_active_proj"])
                           + p["local_active_bias"].reshape(1, -1, 1))
            local_prob = mx.sigmoid(local_logit)
            w_sdpa = weights[..., 0]; w_local = weights[..., 1] * local_prob; w_net = weights[..., 2]
            total = (w_sdpa + w_local + w_net + 1e-6)[..., None]
            out = (w_sdpa[..., None] / total * sdpa_out
                   + w_local[..., None] / total * mem_out
                   + w_net[..., None] / total * net_out)
        if collect_distill:                            # net vs detached (local - sdpa)
            tgt = mx.stop_gradient(mem_out - sdpa_out)
            diff = net_out - tgt
            distill = (diff * diff).mean()
    return (out, distill) if collect_distill else out


def attention(b, x, cos, sin, collect_aux=False):
    """Dual-tier attention, eval/no-cache. Returns (B,T,n_heads*head_dim)->o_proj.
    When collect_aux, also returns (distill_term, z_term) — None where N/A."""
    B, T, _ = x.shape
    H = b["n_heads"]; Hs = b["n_short_heads"]; Hl = b["n_long_heads"]
    Hskv = b["n_short_kv"]; Hlkv = b["n_long_kv"]; hd = b["head_dim"]

    # bank_feedback is PlainFeedback (identity) under default env -> x_for_q = x.
    q_full = (x @ b["q_proj"].T).reshape(B, T, H, hd)
    q_short = mx.transpose(q_full[:, :, :Hs], (0, 2, 1, 3))          # (B,Hs,T,hd)
    q_long = mx.transpose(q_full[:, :, Hs:Hs + Hl], (0, 2, 1, 3))    # (B,Hl,T,hd)

    def proj_heads(W, nkv):
        return mx.transpose((x @ W.T).reshape(B, T, nkv, hd), (0, 2, 1, 3))
    k_s = proj_heads(b["k_proj_s"], Hskv); v_s = proj_heads(b["v_proj_s"], Hskv)
    k_l = proj_heads(b["k_proj_l"], Hlkv); v_l = proj_heads(b["v_proj_l"], Hlkv)

    # SHORT tier: RoPE on q,k; GQA expand; causal SDPA.
    cos_t = cos[:T]; sin_t = sin[:T]
    q_short = _apply_rope(q_short, cos_t, sin_t)
    k_s = _apply_rope(k_s, cos_t, sin_t)
    attn_s = _sdpa_causal(q_short, _gqa(k_s, Hs // Hskv), _gqa(v_s, Hs // Hskv), hd)

    # LONG tier (a): set-style SDPA, no RoPE.
    attn_l_sdpa = _sdpa_causal(q_long, _gqa(k_l, Hl // Hlkv), _gqa(v_l, Hl // Hlkv), hd)

    # LONG tier (b/c): PKM retrieval. bank_query is PlainBankQuery (None) by
    # default -> bank_q = q_long flattened across the long heads.
    distill = z = None
    if b.get("memory") is None and b.get("netbank") is None:
        attn_l = attn_l_sdpa
    else:
        bank_q = mx.transpose(q_long, (0, 2, 1, 3)).reshape(B, T, Hl * hd)
        attn_l_mem = None
        if b.get("memory") is not None:
            r = banks.local_forward(b["memory"], bank_q, b.get("trunk_ids"), want_z=collect_aux)
            mem_out, z = r if collect_aux else (r, None)
            attn_l_mem = mx.transpose(mem_out.reshape(B, T, Hl, hd), (0, 2, 1, 3))
        attn_l_net = None
        if b.get("netbank") is not None:
            net_out = banks.netbank_forward(b["netbank"], bank_q)
            attn_l_net = mx.transpose(net_out.reshape(B, T, Hl, hd), (0, 2, 1, 3))
        if collect_aux:
            attn_l, distill = b["gate"](q_long, attn_l_sdpa, attn_l_mem, attn_l_net,
                                        collect_distill=True)
        else:
            attn_l = b["gate"](q_long, attn_l_sdpa, attn_l_mem, attn_l_net)

    attn = mx.concatenate([attn_s, attn_l], axis=1)                  # (B,H,T,hd)
    out = mx.transpose(attn, (0, 2, 1, 3)).reshape(B, T, H * hd)
    out = out @ b["o_proj"].T
    return (out, distill, z) if collect_aux else out


def block_forward(b, x, cos, sin, collect_aux=False):
    """Pre-norm attention + SwiGLU FFN, both residual. Mirrors block_forward.
    When collect_aux, returns (x, distill_term, z_term)."""
    r = attention(b, _rms_norm(x, b["norm1_w"], b["norm1_eps"]), cos, sin, collect_aux)
    attn_out, distill, z = r if collect_aux else (r, None, None)
    x = x + attn_out
    h = _rms_norm(x, b["norm2_w"], b["norm2_eps"])
    g = h @ b["gate_proj"].T
    ffn = ((g * mx.sigmoid(g)) * (h @ b["up_proj"].T)) @ b["down_proj"].T  # SwiGLU
    x = x + ffn
    return (x, distill, z) if collect_aux else x
