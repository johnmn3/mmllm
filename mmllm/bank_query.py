"""Bank-query shaping: how the dense network influences what gets
asked of the product-key memory bank.

The default (PlainBankQuery) sends `q_long_flat` directly to the bank
— the bank query is just the long-head Q vectors concatenated. The
dense weights have no separate channel to "shape" the question; the
bank gets whatever Q falls out of q_proj.

Alternatives let the dense weights contribute an additive context
modulation: "given this token's full residual context, here's how I
want to bias the bank query." This lets thinking patterns flow from
the dense weights INTO the bank query, so the bank can be consulted
for what the dense network has *decided to look up*, not only for
what the local long-head Q happens to be.

The bank is always consulted; only the QUERY changes. (For decisions
about WHEN to consult the bank — i.e., per-token routing on the
output side — see `mmllm.gating`.)
"""
import torch
import torch.nn as nn


class PlainBankQuery(nn.Module):
    """Baseline: no context modulation. Forward returns None, which
    the attention block reads as 'use q_long_flat unchanged'."""

    def __init__(self, d_model: int, q_dim: int):
        super().__init__()

    def forward(self, x):
        return None


class CtxAddBankQuery(nn.Module):
    """Additive context modulation: bank_query = q_long_flat + W_ctx · x.

    W_ctx is a learned Linear over the post-norm residual stream
    (the same x that q_proj sees), zero-initialized so the bank query
    starts identical to the plain case at step 0. Gradient flow then
    grows whatever modulation reduces loss — the dense weights learn
    "given this context, ask the bank THIS instead."
    """

    def __init__(self, d_model: int, q_dim: int):
        super().__init__()
        self.proj = nn.Linear(d_model, q_dim, bias=False)
        nn.init.zeros_(self.proj.weight)

    def forward(self, x):
        return self.proj(x)


def build_bank_query(kind: str, d_model: int, q_dim: int) -> nn.Module:
    """Factory: 'plain' | 'ctx-add' → bank-query shaper Module."""
    if kind == "plain":
        return PlainBankQuery(d_model, q_dim)
    if kind == "ctx-add":
        return CtxAddBankQuery(d_model, q_dim)
    raise ValueError(
        f"unknown bank-query kind: {kind!r} "
        f"(expected one of 'plain', 'ctx-add')"
    )
