"""MLX model forward: token embedding -> N blocks -> final RMSNorm -> weight-tied
LM head. Mirrors core.lpy `forward` (eval/no-cache path). Pure function of
(params, tokens) so it composes with mx.value_and_grad in Stage 2.

`params` is a dict:
  {"tok_emb": (vocab,d_model), "norm_final_w": (d_model,), "norm_final_eps": f,
   "rope_cos","rope_sin": (max_pos,head_dim), "blocks": [block_param_dict, ...]}
Each block_param_dict is what blocks.block_forward consumes.
"""
from __future__ import annotations

import mlx.core as mx

from mmllm.mlx import blocks


def forward(params, tokens, collect_aux=False):
    """tokens: int array (B,T) -> logits (B,T,vocab). Weight-tied LM head.
    When collect_aux, returns (logits, distill_total, z_total, n_distill) where
    the totals SUM the per-block aux terms (n_distill = #blocks contributing a
    distill term, for mean-normalization in the loss)."""
    x = params["tok_emb"][tokens]                       # embedding lookup
    cos = params["rope_cos"]; sin = params["rope_sin"]
    if not collect_aux:
        for b in params["blocks"]:
            x = blocks.block_forward(b, x, cos, sin)
        x = blocks._rms_norm(x, params["norm_final_w"], params["norm_final_eps"])
        return x @ params["tok_emb"].T
    distill_total = mx.array(0.0); z_total = mx.array(0.0); n_distill = 0
    for b in params["blocks"]:
        x, distill, z = blocks.block_forward(b, x, cos, sin, collect_aux=True)
        if distill is not None:
            distill_total = distill_total + distill; n_distill += 1
        if z is not None:
            z_total = z_total + z
    x = blocks._rms_norm(x, params["norm_final_w"], params["norm_final_eps"])
    logits = x @ params["tok_emb"].T
    return logits, distill_total, z_total, n_distill
