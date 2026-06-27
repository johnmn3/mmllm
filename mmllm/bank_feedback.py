"""Bank → dense feedback: how the product-key bank's output influences
the dense network's input before q-proj.

Mirror of `mmllm.bank_query` (which controls how the dense net feeds
the bank). `bank_query.ctx-add` lets the dense weights shape the BANK
QUERY; this module's `BankToInputFeedback` lets the bank's OUTPUT
shape the DENSE QUERY. Combined, you get bidirectional retrieval-
augmented attention per layer:

  - dense → bank: bank_query = q_long_flat + W_ctx · x         (bank_query.py)
  - bank  → dense: q = q_proj(x + W_back · bank(W_probe · x))  (this file)

When feedback is enabled the bank is queried TWICE per attention call:
  1. probe_q  = W_probe · x         (small Linear, default init)
     probe_mem = memory(probe_q)     (existing PKM forward)
     delta   = W_back · probe_mem   (zero-init Linear → delta=0 at step 0)
     x_for_q = x + delta
     q-full  = q_proj(x_for_q)
  2. q_long_flat = q_long reshape   (existing path; may also pass through
                                     bank_query.ctx-add)
     mem_out = memory(bank_q)        (existing path)

W_back zero-init mirrors `bank_query.ctx-add`: at step 0, x_for_q = x,
so behavior is identical to the no-feedback baseline. As loss flows
back, W_back develops weights; once non-zero, gradient also reaches
W_probe, which specializes the exploratory query.

Only the q-proj input is modulated — k-proj-s, v-proj-s, k-proj-l,
v-proj-l still see the unmodified `x`. So the bank shapes what the
dense net ASKS, not what it stores in the KV caches.

Cost: one extra PKM lookup per layer per forward. PKM is O(sqrt(N)),
so this roughly doubles the bank-side compute and ~doubles the per-
step rows touched by sparse-grad SGD. The dirty-page tracker dedupes
across both lookups within a single step.
"""
import torch
import torch.nn as nn


class PlainFeedback(nn.Module):
    """Baseline: no bank → dense feedback. Forward returns None, which
    the attention block reads as 'use x unchanged for q-proj'."""

    def __init__(self, d_model: int, q_dim: int):
        super().__init__()

    def forward(self, x, memory):
        return None


class BankToInputFeedback(nn.Module):
    """Probe the bank with W_probe·x, then add W_back·probe_mem to x
    before q-proj.

    W_probe uses torch's default Linear init (Kaiming-uniform); W_back
    is zero-init so the feedback delta is exactly 0 at step 0 and the
    model is bit-identical to the no-feedback baseline. SGD develops
    W_back from the loss; gradient then flows back through probe_mem
    to W_probe so it can specialize beyond a fixed random projection.
    """

    def __init__(self, d_model: int, q_dim: int):
        super().__init__()
        self.probe = nn.Linear(d_model, q_dim, bias=False)
        self.back = nn.Linear(q_dim, d_model, bias=False)
        nn.init.zeros_(self.back.weight)

    def forward(self, x, memory):
        probe_q = self.probe(x)        # (B, T, q_dim)
        probe_mem = memory(probe_q)    # (B, T, q_dim) via the same PKM
        return self.back(probe_mem)    # (B, T, d_model)


def build_bank_feedback(kind: str, d_model: int, q_dim: int) -> nn.Module:
    """Factory: 'plain' | 'feedback' → bank-feedback Module."""
    if kind == "plain":
        return PlainFeedback(d_model, q_dim)
    if kind == "feedback":
        return BankToInputFeedback(d_model, q_dim)
    raise ValueError(
        f"unknown bank-feedback kind: {kind!r} "
        f"(expected one of 'plain', 'feedback')"
    )
