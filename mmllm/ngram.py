"""Phase C — n-gram hash input features (byte-level analog of hash embeddings /
fastText). For each position t and each configured g-gram length g, we hash the
preceding g bytes b[t-g+1..t] into one of H buckets and add the looked-up vector
to the byte input embedding:

    e_t = tok_emb[b_t] + Σ_{g∈G} HashEmb_g[ hash_g(b[t-g+1..t]) mod H_g ]

The hash is a rolling polynomial over the uint8 window (cheap; computable on the
token array directly). `HashEmb_g` is an nn.Embedding(H_g, d_model), ZERO-INIT so
the add path is inert at step 0 — enabling the feature on a live ckpt is a no-op
until gradients shape the tables (back-compat + collision-noise safety, doc §4.4).

Spec format (env MMLLM_NGRAM_HASH): comma list of `g:H` pairs, e.g.
"2:65536,3:262144". `parse_spec` returns [(g, H), ...].

This module is the torch reference; `mmllm/mlx/ngram.py` mirrors `hash_ids` /
`ngram_embed` for the live MLX path. MLX is the source of truth; the two hash
implementations are kept bit-identical (same base, same modulus) so a torch ckpt's
tables transfer to MLX unchanged.
"""
from __future__ import annotations

import torch
import torch.nn as nn

# Polynomial rolling-hash base. Coprime-ish with the byte alphabet (256); a small
# odd prime spreads the 256 byte values across buckets without obvious structure.
HASH_BASE = 257


def parse_spec(spec):
    """"2:65536,3:262144" -> [(2, 65536), (3, 262144)]. Empty/None -> []."""
    if not spec:
        return []
    out = []
    for pair in str(spec).split(","):
        pair = pair.strip()
        if not pair:
            continue
        g, h = pair.split(":")
        out.append((int(g.strip()), int(h.strip())))
    return out


def hash_ids(tokens, g, H, base=HASH_BASE):
    """tokens: int64 (B,T) -> int64 (B,T) bucket id of the g-gram ENDING at each
    position, mod H. Positions with fewer than g preceding bytes hash their
    available prefix (missing bytes treated as 0 via left zero-pad). Pure torch so
    it can run in the data loader or the forward."""
    B, T = tokens.shape
    acc = torch.zeros((B, T), dtype=torch.int64, device=tokens.device)
    coef = 1
    for i in range(g):                      # i = age of the byte (0 = current b_t)
        if i == 0:
            shifted = tokens
        else:
            shifted = torch.zeros_like(tokens)
            shifted[:, i:] = tokens[:, :T - i]
        acc = acc + shifted.to(torch.int64) * coef
        coef = (coef * base)
    return torch.remainder(acc, H)


class NgramHashEmb(nn.Module):
    """Σ_g HashEmb_g[hash_g(window)] summed into the byte embedding. Zero-init →
    inert at step 0. Built behind MMLLM_NGRAM_HASH; lives at END of (parameters)."""

    def __init__(self, specs, d_model):
        super().__init__()
        self.specs = list(specs)                     # [(g, H), ...]
        self.tables = nn.ModuleList(
            [nn.Embedding(H, d_model) for (_g, H) in self.specs])
        for t in self.tables:
            nn.init.zeros_(t.weight)                 # inert add at step 0

    def forward(self, tokens):
        """tokens: (B,T) int64 -> (B,T,d_model) summed n-gram contribution."""
        out = None
        for (g, H), table in zip(self.specs, self.tables):
            ids = hash_ids(tokens, g, H)
            e = table(ids)
            out = e if out is None else out + e
        return out
