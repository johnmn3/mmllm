"""Pure-Python inference path — bypasses basilisp dispatch for ~2.1×
decode throughput on CPU. Mirrors core.lpy's `forward` and `sample-batch`
but calls `mmllm.attention_kernel.block_forward` directly with positional
arguments unpacked from each block's basilisp PersistentMap.

Profile of the basilisp forward path (cpu-mini, B=1, T=1 decode):
  ~25% nn.Module.__call__ overhead (cumulative across all submodules)
  ~55% basilisp seq/get/eq/runtime dispatch
  ~20% actual torch ops (matmul, softmax, etc.)

Removing the ~55% basilisp slice via this module → 39.3 tok/s vs 18.6 tok/s
(2.1×). Further inlining of F.linear / F.rms_norm gave ~0% more (Module
dispatch isn't actually a meaningful chunk at this scale).

Usage:
    from mmllm.inference import unpack_model, decode_batch
    bundle = unpack_model(model)        # one-time prep
    decode_batch(bundle, prompt, n_warm, B)
"""
from __future__ import annotations

import time
from typing import Optional

import torch
import torch.nn.functional as F

import basilisp.lang.keyword as bkw
from .attention_kernel import block_forward as _block_forward


def _K(s):
    return bkw.keyword(s)


def unpack_model(m) -> dict:
    """Pre-extract everything the hot path needs from a basilisp model map
    into a plain Python dict. Call once before the decode loop; reuse for
    every forward."""
    blocks_lisp = list(m.val_at(_K("blocks")))

    def _unpack_block(blk):
        g = lambda name: blk.val_at(_K(name))
        return (
            g("norm1"), g("norm2"),
            g("q-proj"), g("k-proj-s"), g("v-proj-s"),
            g("k-proj-l"), g("v-proj-l"), g("o-proj"),
            g("memory"), g("long-gate"), g("bank-query"), g("bank-feedback"),
            g("gate-proj"), g("up-proj"), g("down-proj"),
            g("n-heads"), g("n-short-heads"), g("n-long-heads"),
            g("n-short-kv-heads"), g("n-long-kv-heads"), g("head-dim"), g("max-t"),
            g("short-window"), g("long-window"),
            g("netbank"), g("carry"),
        )

    return {
        "blocks":     [_unpack_block(b) for b in blocks_lisp],
        "tok_emb":    m.val_at(_K("tok-emb")),
        "norm_final": m.val_at(_K("norm-final")),
        "rope_cos":   m.val_at(_K("rope-cos")),
        "rope_sin":   m.val_at(_K("rope-sin")),
        "device":     m.val_at(_K("device")),
    }


@torch.no_grad()
def forward_inf(
    bundle: dict,
    tokens: torch.Tensor,
    short_caches: Optional[list] = None,
    long_caches: Optional[list] = None,
) -> tuple:
    """Pure-Python forward pass. Returns (logits, new_short_caches,
    new_long_caches). `short_caches` / `long_caches` are per-block lists
    of (k_buf, v_buf, pos) tuples or None for first call (prefill).

    No basilisp involvement after unpack_model. nn.Module submodules are
    still called via Module.__call__ (PKM, gating, bank_query, carry).
    Linear/RMSNorm/Embedding are kept as Modules too — inlining them
    didn't help measurably on cpu-mini.
    """
    x = bundle["tok_emb"](tokens)
    rope_cos = bundle["rope_cos"]
    rope_sin = bundle["rope_sin"]
    new_s_list, new_l_list = [], []

    for i, b in enumerate(bundle["blocks"]):
        (norm1, norm2,
         q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
         memory, long_gate, bank_query, bank_feedback,
         gate_proj, up_proj, down_proj,
         n_heads, n_short_heads, n_long_heads,
         n_short_kv_heads, n_long_kv_heads, head_dim, max_t,
         short_window, long_window, netbank, carry) = b
        sc = short_caches[i] if short_caches is not None else None
        lc = long_caches[i] if long_caches is not None else None
        x_out, ns, nl = _block_forward(
            norm1, norm2,
            q_proj, k_proj_s, v_proj_s, k_proj_l, v_proj_l, o_proj,
            memory, long_gate, bank_query, bank_feedback,
            gate_proj, up_proj, down_proj,
            n_heads, n_short_heads, n_long_heads,
            n_short_kv_heads, n_long_kv_heads, head_dim, max_t,
            short_window, long_window,
            x, rope_cos, rope_sin, sc, lc,
            skip_bank=False, netbank=netbank, trunk_ids=None,
        )
        if carry is not None:
            x_out = carry(x_out)
        x = x_out
        new_s_list.append(ns)
        new_l_list.append(nl)

    x = bundle["norm_final"](x)
    # Weight-tied LM head: logits = x @ tok_emb.weight.T
    logits = torch.matmul(x, bundle["tok_emb"].weight.t())
    return logits, new_s_list, new_l_list


def _encode_bytes(s: str, device) -> torch.Tensor:
    return torch.tensor(
        [[b for b in s.encode("utf-8")]],
        dtype=torch.long,
        device=device,
    )


@torch.no_grad()
def decode_batch(bundle: dict, prompt: str, n: int, B: int) -> None:
    """Decode `n` tokens for B parallel sequences from the same prompt.
    Pure-Python equivalent of core.lpy:sample-batch — returns nothing,
    used for throughput benchmarking.
    """
    device = bundle["device"]
    prompt_1 = _encode_bytes(prompt, device)
    T_prompt = prompt_1.size(1)
    prompt_toks = prompt_1.expand(B, T_prompt).contiguous()

    logits, sc, lc = forward_inf(bundle, prompt_toks)
    for _ in range(n):
        last = logits[:, -1, :]
        probs = F.softmax(last, dim=-1)
        next_tok = torch.multinomial(probs, 1)
        logits, sc, lc = forward_inf(bundle, next_tok, sc, lc)


@torch.no_grad()
def bench_decode(bundle: dict, prompt: str, n_warm: int, n_time: int, B: int) -> dict:
    """Warmup + timed decode. Returns dict with tok/sec metrics."""
    # Warmup (compile JIT, page in mmap banks, populate KV cache)
    decode_batch(bundle, prompt, n_warm, B)

    t0 = time.time()
    decode_batch(bundle, prompt, n_time, B)
    dt = time.time() - t0

    per_seq_tps = n_time / dt
    agg_tps = B * per_seq_tps
    ms_per_tok = 1000.0 * dt / n_time
    return {
        "B": B,
        "n_time": n_time,
        "wall_s": dt,
        "per_seq_tps": per_seq_tps,
        "aggregate_tps": agg_tps,
        "ms_per_tok": ms_per_tok,
    }
