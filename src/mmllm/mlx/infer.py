"""MLX inference: prefill + KV-cache autoregressive decode (the FIM/generation
path). Decode is B=1, T=1 per step over a growing cache — exactly the regime
where MLX's whole-graph fusion beats torch-MPS most (per-op dispatch dominates
torch there). Reuses the verified banks.py + blocks.py kernels at T=1.

The training/eval forward (model.forward) recomputes full causal attention each
call (O(T^2) for decode); this path keeps per-layer k/v caches so each decode
step is O(T_cache), the real generation speed.
"""
from __future__ import annotations

import math
import time
import mlx.core as mx

from mmllm.mlx import banks, blocks


def _proj_heads(x, W, B, T, nkv, hd):
    return mx.transpose((x @ W.T).reshape(B, T, nkv, hd), (0, 2, 1, 3))


def _attn_cached(b, x, cache_l, start_pos, cos, sin):
    """Cached dual-tier attention. x:(B,T,d) — T=prompt len on prefill, 1 on
    decode. start_pos = #tokens already in the cache. Appends this step's k/v
    and attends over the full cache. Returns (B,T,n_heads*hd)->o_proj."""
    B, T, _ = x.shape
    H, Hs, Hl = b["n_heads"], b["n_short_heads"], b["n_long_heads"]
    Hskv, Hlkv, hd = b["n_short_kv"], b["n_long_kv"], b["head_dim"]

    q_full = (x @ b["q_proj"].T).reshape(B, T, H, hd)
    q_short = mx.transpose(q_full[:, :, :Hs], (0, 2, 1, 3))
    q_long = mx.transpose(q_full[:, :, Hs:Hs + Hl], (0, 2, 1, 3))
    k_s = _proj_heads(x, b["k_proj_s"], B, T, Hskv, hd)
    v_s = _proj_heads(x, b["v_proj_s"], B, T, Hskv, hd)
    k_l = _proj_heads(x, b["k_proj_l"], B, T, Hlkv, hd)
    v_l = _proj_heads(x, b["v_proj_l"], B, T, Hlkv, hd)

    # RoPE (short tier) at absolute positions [start_pos, start_pos+T)
    cos_t = cos[start_pos:start_pos + T]; sin_t = sin[start_pos:start_pos + T]
    q_short = blocks._apply_rope(q_short, cos_t, sin_t)
    k_s = blocks._apply_rope(k_s, cos_t, sin_t)

    # append to the per-layer cache (grow along the time axis)
    if cache_l["k_s"] is None:
        cache_l["k_s"], cache_l["v_s"] = k_s, v_s
        cache_l["k_l"], cache_l["v_l"] = k_l, v_l
    else:
        cache_l["k_s"] = mx.concatenate([cache_l["k_s"], k_s], axis=2)
        cache_l["v_s"] = mx.concatenate([cache_l["v_s"], v_s], axis=2)
        cache_l["k_l"] = mx.concatenate([cache_l["k_l"], k_l], axis=2)
        cache_l["v_l"] = mx.concatenate([cache_l["v_l"], v_l], axis=2)

    scale = 1.0 / math.sqrt(hd)
    mask = "causal" if (T > 1 and start_pos == 0) else None   # prefill vs decode
    attn_s = mx.fast.scaled_dot_product_attention(
        q_short, blocks._gqa(cache_l["k_s"], Hs // Hskv),
        blocks._gqa(cache_l["v_s"], Hs // Hskv), scale=scale, mask=mask)
    attn_l_sdpa = mx.fast.scaled_dot_product_attention(
        q_long, blocks._gqa(cache_l["k_l"], Hl // Hlkv),
        blocks._gqa(cache_l["v_l"], Hl // Hlkv), scale=scale, mask=mask)

    # PKM retrieval (works at any T, incl. T=1). bank_query is identity by default.
    if b.get("memory") is None and b.get("netbank") is None:
        attn_l = attn_l_sdpa
    else:
        bank_q = mx.transpose(q_long, (0, 2, 1, 3)).reshape(B, T, Hl * hd)
        attn_l_mem = None
        if b.get("memory") is not None:
            mem_out = banks.local_forward(b["memory"], bank_q, b.get("trunk_ids"))
            attn_l_mem = mx.transpose(mem_out.reshape(B, T, Hl, hd), (0, 2, 1, 3))
        attn_l_net = None
        if b.get("netbank") is not None:
            net_out = banks.netbank_forward(b["netbank"], bank_q)
            attn_l_net = mx.transpose(net_out.reshape(B, T, Hl, hd), (0, 2, 1, 3))
        attn_l = b["gate"](q_long, attn_l_sdpa, attn_l_mem, attn_l_net)

    attn = mx.concatenate([attn_s, attn_l], axis=1)
    out = mx.transpose(attn, (0, 2, 1, 3)).reshape(B, T, H * hd)
    return out @ b["o_proj"].T


def _block_cached(b, x, cache_l, start_pos, cos, sin):
    x = x + _attn_cached(b, blocks._rms_norm(x, b["norm1_w"], b["norm1_eps"]),
                         cache_l, start_pos, cos, sin)
    h = blocks._rms_norm(x, b["norm2_w"], b["norm2_eps"])
    g = h @ b["gate_proj"].T
    return x + ((g * mx.sigmoid(g)) * (h @ b["up_proj"].T)) @ b["down_proj"].T


def _forward_cached(params, tokens, caches, start_pos):
    x = params["tok_emb"][tokens]
    cos, sin = params["rope_cos"], params["rope_sin"]
    for b, cache_l in zip(params["blocks"], caches):
        x = _block_cached(b, x, cache_l, start_pos, cos, sin)
    x = blocks._rms_norm(x, params["norm_final_w"], params["norm_final_eps"])
    return x @ params["tok_emb"].T


def generate(params, prompt_ids, n_new, greedy=True):
    """prompt_ids: (B, T_p) int array. Returns (generated_ids list, timing dict).
    Prefill the prompt, then decode n_new tokens with the KV cache."""
    B = prompt_ids.shape[0]
    caches = [{"k_s": None, "v_s": None, "k_l": None, "v_l": None}
              for _ in params["blocks"]]
    # prefill
    logits = _forward_cached(params, prompt_ids, caches, 0)
    pos = prompt_ids.shape[1]
    last = logits[:, -1, :]
    out = []
    for _ in range(n_new):
        nxt = mx.argmax(last, axis=-1, keepdims=True) if greedy else \
            mx.random.categorical(last)[:, None]
        out.append(nxt)
        logits = _forward_cached(params, nxt, caches, pos)
        last = logits[:, -1, :]
        pos += 1
    mx.eval(out)
    return out


def bench(params, prompt_len=128, n_new=128, B=1, warmup=16):
    """tok/s for B-stream decode. Returns (tok_per_s, ms_per_tok)."""
    prompt = mx.zeros((B, prompt_len), dtype=mx.int32)
    generate(params, prompt, warmup)          # warmup (graph build, cache alloc)
    mx.synchronize()
    t0 = time.time()
    generate(params, prompt, n_new)
    mx.synchronize()
    dt = time.time() - t0
    tps = (n_new * B) / dt
    return tps, 1000.0 * dt / n_new
