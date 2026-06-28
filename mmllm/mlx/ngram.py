"""Phase C — MLX mirror of mmllm/ngram.py (the live path). Computes the same
rolling polynomial g-gram hash (same HASH_BASE, same modulus) so a torch-built
NgramHashEmb's tables transfer to MLX unchanged. `ngram_embed` does the embedding
lookup + sum that is added to the byte input embedding in model.forward.
"""
from __future__ import annotations

import mlx.core as mx

HASH_BASE = 257                     # keep in sync with mmllm/ngram.py


def hash_ids(tokens, g, H, base=HASH_BASE):
    """tokens: int (B,T) -> int (B,T) bucket id of the g-gram ending at each
    position, mod H. Missing leading bytes are left-zero-padded (treated as 0)."""
    B, T = tokens.shape
    acc = mx.zeros((B, T), dtype=mx.int32)
    coef = 1
    for i in range(g):
        if i == 0:
            shifted = tokens.astype(mx.int32)
        else:
            pad = mx.zeros((B, i), dtype=mx.int32)
            shifted = mx.concatenate([pad, tokens[:, :T - i].astype(mx.int32)], axis=1)
        acc = acc + shifted * coef
        coef = coef * base
    return acc % H


def ngram_embed(tables, specs, tokens):
    """tables: list of (H_g, d_model) mx arrays; specs: [(g, H), ...].
    Returns (B,T,d_model) summed n-gram contribution to add to tok_emb."""
    out = None
    for (g, H), table in zip(specs, tables):
        ids = hash_ids(tokens, g, H)
        e = table[ids]
        out = e if out is None else out + e
    return out
