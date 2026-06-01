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


def offload_netbank_to_disk(params, cache_dir):
    """MODE 2 (gpu/disk-netbank): move each NetBank V table from a GPU mx.array to
    an on-disk numpy memmap, freeing ~1 GB of unified memory. The decode then
    host-gathers only the top-k rows per step (banks.netbank_forward's V_mmap
    path). Use the EAGER `generate()` with these params — the host gather can't be
    mx.compile'd, so this mode doesn't use make_compiled_decoder.

    For Apple-Silicon boxes where the full NetBank won't fit in unified memory
    alongside the model + KV cache. Slower than mode 1 (per-layer GPU<->host sync)
    — a memory fallback, not a speed mode. Returns the mutated params."""
    import os
    import numpy as np
    os.makedirs(cache_dir, exist_ok=True)
    for i, b in enumerate(params["blocks"]):
        nb = b.get("netbank")
        if nb is not None and "V" in nb:
            V = np.asarray(nb["V"]).astype(np.float32)
            path = os.path.join(cache_dir, f"vnet.{i}.bin")
            V.tofile(path)
            nb["V_mmap"] = np.memmap(path, dtype=np.float32, mode="r", shape=V.shape)
            del nb["V"]
    return params


# ── Three local-inference modes (a FIM agent picks one by hardware) ───────────
#   MODE 1  gpu/gpu      : MLX, NetBank V on GPU. make_compiled_decoder + the
#                          compiled decode. Fastest (~134 tok/s on M5). Apple
#                          Silicon with enough unified memory (default).
#   MODE 2  gpu/disk-net : MLX, dense+Local on GPU, NetBank V mmap'd via
#                          offload_netbank_to_disk(); EAGER generate(). Saves
#                          ~1 GB; slower (~55 tok/s, host sync). Tight-VRAM Apple
#                          Silicon — a memory fallback, NOT a speed mode (on the
#                          M5 it's slower than mode 3 because of the sync).
#   MODE 3  cpu/disk-net : the TORCH CPU path (core.lpy bench-inference / sample,
#                          MMLLM_BANK_ON_GPU=false). The only mode that runs on
#                          non-Apple-Silicon (e.g. a 2018 Intel Mac). ~93 tok/s M5.
# All three run on an M-series box; modes 1-2 require Apple Silicon (MLX).


def make_compiled_decoder(params, B, max_t):
    """Build an mx.compile'd single-token decode step over a PREALLOCATED
    (B, H, max_t, hd) KV cache. Fixed shapes + `pos` as a runtime array → compiles
    once and replays, collapsing the 56-bank × 32-layer per-token Python
    orchestration into one graph (the measured ~2x over eager; compile traces
    through the bank gather/topk fine). Cache writes are functional (mask-blend)
    so they're compile-safe. Returns (step_fn, fresh_cache_fn)."""
    cos, sin = params["rope_cos"], params["rope_sin"]

    def _proj(x, W, nkv, hd):
        return mx.transpose((x @ W.T).reshape(B, 1, nkv, hd), (0, 2, 1, 3))

    def step(token, kc, pos):
        oh = (mx.arange(max_t) == pos).reshape(1, 1, max_t, 1).astype(mx.float32)
        am = mx.where(mx.arange(max_t) <= pos, 0.0, -1e9).reshape(1, 1, 1, max_t)
        cp = mx.take(cos, pos, axis=0).reshape(1, 1, 1, -1)
        sp = mx.take(sin, pos, axis=0).reshape(1, 1, 1, -1)
        x = params["tok_emb"][token]
        new_kc = []
        for b, (ks, vs, kl, vl) in zip(params["blocks"], kc):
            H, Hs, Hl = b["n_heads"], b["n_short_heads"], b["n_long_heads"]
            Hskv, Hlkv, hd = b["n_short_kv"], b["n_long_kv"], b["head_dim"]
            xn = blocks._rms_norm(x, b["norm1_w"], b["norm1_eps"])
            qf = (xn @ b["q_proj"].T).reshape(B, 1, H, hd)
            qsh = mx.transpose(qf[:, :, :Hs], (0, 2, 1, 3))
            qlo = mx.transpose(qf[:, :, Hs:Hs + Hl], (0, 2, 1, 3))
            nks = _proj(xn, b["k_proj_s"], Hskv, hd); nvs = _proj(xn, b["v_proj_s"], Hskv, hd)
            nkl = _proj(xn, b["k_proj_l"], Hlkv, hd); nvl = _proj(xn, b["v_proj_l"], Hlkv, hd)
            qsh = blocks._apply_rope(qsh, cp, sp); nks = blocks._apply_rope(nks, cp, sp)
            ks = ks * (1 - oh) + nks * oh; vs = vs * (1 - oh) + nvs * oh
            kl = kl * (1 - oh) + nkl * oh; vl = vl * (1 - oh) + nvl * oh
            sc = 1.0 / math.sqrt(hd)
            a_s = mx.fast.scaled_dot_product_attention(
                qsh, blocks._gqa(ks, Hs // Hskv), blocks._gqa(vs, Hs // Hskv), scale=sc, mask=am)
            a_l = mx.fast.scaled_dot_product_attention(
                qlo, blocks._gqa(kl, Hl // Hlkv), blocks._gqa(vl, Hl // Hlkv), scale=sc, mask=am)
            if b.get("memory") or b.get("netbank"):
                bq = mx.transpose(qlo, (0, 2, 1, 3)).reshape(B, 1, Hl * hd)
                mo = lo = None
                if b.get("memory"):
                    mo = mx.transpose(banks.local_forward(b["memory"], bq, b.get("trunk_ids")).reshape(B, 1, Hl, hd), (0, 2, 1, 3))
                if b.get("netbank"):
                    lo = mx.transpose(banks.netbank_forward(b["netbank"], bq).reshape(B, 1, Hl, hd), (0, 2, 1, 3))
                a_l = b["gate"](qlo, a_l, mo, lo)
            o = mx.transpose(mx.concatenate([a_s, a_l], axis=1), (0, 2, 1, 3)).reshape(B, 1, H * hd) @ b["o_proj"].T
            x = x + o
            h = blocks._rms_norm(x, b["norm2_w"], b["norm2_eps"]); g = h @ b["gate_proj"].T
            x = x + ((g * mx.sigmoid(g)) * (h @ b["up_proj"].T)) @ b["down_proj"].T
            new_kc.append((ks, vs, kl, vl))
        return x @ params["tok_emb"].T, new_kc

    def fresh_cache():
        return [[mx.zeros((B, b["n_short_kv"], max_t, b["head_dim"])),
                 mx.zeros((B, b["n_short_kv"], max_t, b["head_dim"])),
                 mx.zeros((B, b["n_long_kv"], max_t, b["head_dim"])),
                 mx.zeros((B, b["n_long_kv"], max_t, b["head_dim"]))]
                for b in params["blocks"]]
    return mx.compile(step), fresh_cache


def bench_compiled(params, n_new=128, B=1, max_t=224, warmup=8):
    """tok/s for the compiled fixed-cache decoder (~2x the eager path)."""
    step, fresh = make_compiled_decoder(params, B, max_t)
    def run(n):
        kc = fresh()
        lg = None
        for i in range(n):
            lg, kc = step(mx.zeros((B, 1), dtype=mx.int32), kc, mx.array(i, dtype=mx.int32))
        mx.eval(lg, kc[-1][0])
    run(warmup); mx.synchronize()
    t0 = time.time(); run(n_new); mx.synchronize()
    dt = time.time() - t0
    return (n_new * B) / dt, 1000.0 * dt / n_new


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
