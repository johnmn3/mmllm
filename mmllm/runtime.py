"""Inference-time runtime helpers: torch.compile wrappers, dtype casts,
CUDA graphs.

Phase-1a (torch.compile) and Phase-1d (CUDA graphs) of the inference
optimization plan land here. The basilisp `forward` function is just a
Python callable after compilation, so torch.compile can wrap it directly.

Graceful fallback throughout — if compile or CUDA-graph capture fails
(e.g., dynamic shapes the compiler can't handle, sparse-gather ops in
the bank lookup, basilisp idioms torch.compile doesn't trace), the
caller gets back the original callable and a warning is printed.
Inference must never break because of an optimization step.
"""
from __future__ import annotations

import os
from typing import Callable

import torch


def _opt_in(env_var: str) -> bool:
    return os.environ.get(env_var, "false").lower() in ("1", "true", "yes")


def maybe_compile_forward(forward_callable: Callable) -> Callable:
    """Wrap `forward_callable` in `torch.compile` when MMLLM_COMPILE=true.

    Returns the original callable if compile is disabled or if
    compilation raises. Caller invokes the result identically to the
    original forward.

    Mode: `default` — graph-level optimization without CUDA graph
    capture. CUDA graphs (mode=`reduce-overhead`) are Phase-1d's
    territory and conflict with the persistent pre-alloc KV buffer
    that's intentionally reused across forward calls — graph capture
    sees the buffer as "graph output overwritten by subsequent run"
    and refuses. To use cudagraphs cleanly, the buffer would need
    explicit `cudagraph_mark_step_begin()` boundaries.

    `dynamic=True` lets the pre-allocated KV cache narrow position
    vary without recompilation. `fullgraph=False` allows graph breaks
    on Python-level control flow (the per-layer loop in `forward`);
    only the inner tensor ops get compiled.

    Tunables via env:
      - MMLLM_COMPILE        — opt in (default false)
      - MMLLM_COMPILE_MODE   — passed through to torch.compile
                               (default 'default'; pass 'reduce-overhead'
                               only after wiring cudagraph_mark_step_begin
                               around forward calls — see Phase-1d)
    """
    if not _opt_in("MMLLM_COMPILE"):
        return forward_callable

    mode = os.environ.get("MMLLM_COMPILE_MODE", "default")
    try:
        compiled = torch.compile(
            forward_callable,
            mode=mode,
            dynamic=True,
            fullgraph=False,
        )
        print(f"  forward: torch.compile enabled (mode={mode}, dynamic=True)")
        return compiled
    except Exception as e:
        print(f"  forward: torch.compile failed ({e!r}); falling back to eager")
        return forward_callable


def maybe_cast_dense_bf16(model: dict) -> dict:
    """Cast dense Linear/Embedding weights to bfloat16 when
    MMLLM_DENSE_DTYPE=bf16. Bank V is left alone (sparse-grad / fp32
    SparseAdam state on CPU).

    Modern CPUs (Intel Sapphire Rapids+, AMD Zen4+, Apple M-series)
    have native bf16 matmul instructions; halving memory bandwidth on
    dense matmuls is the Phase-1 step C1 win for the CPU bench.
    """
    if os.environ.get("MMLLM_DENSE_DTYPE", "").lower() not in ("bf16", "bfloat16"):
        return model
    import torch.nn as nn

    def _cast(mod: nn.Module) -> None:
        for m in mod.modules():
            # Skip the bank's V — that lives on disk via mmap (or stays
            # fp32 even when on GPU because SparseAdam needs fp32).
            if m.__class__.__name__ == "CPUPinnedEmbedding":
                continue
            if isinstance(m, (nn.Linear, nn.Embedding)):
                m.to(torch.bfloat16)
            elif isinstance(m, nn.RMSNorm):
                m.to(torch.bfloat16)

    # Walk the model dict — basilisp builds it as nested dicts of
    # nn.Module objects, not a single nn.Module tree.
    for v in model.values():
        if isinstance(v, nn.Module):
            _cast(v)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    for sub in item.values():
                        if isinstance(sub, nn.Module):
                            _cast(sub)
    print("  dense weights cast to bfloat16")
    return model
