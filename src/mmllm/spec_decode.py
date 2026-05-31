"""Speculative decoding for mmllm — Phase 5 of the inference plan.

The bank-zeroed forward (skip_bank=True) becomes the cheap draft;
the full forward verifies. With our hard-split tiered architecture
the draft saves ~17% per forward step (the bank's K_a/K_b matmuls
+ top-k + gather), so theoretical speedup over autoregressive is
modest — closer to 1.1-1.3× than the textbook 2× — but the
infrastructure is identical to standard speculative decoding and
generalizes to a tiny separately-trained draft model later.

Algorithm (single-batch decode):
  1. Save cache pos counters before drafting.
  2. Draft K tokens autoregressively using skip_bank=True; cache
     advances naturally.
  3. Rewind cache pos to the saved value.
  4. Verify: ONE batched forward of the K draft tokens through the
     full model (skip_bank=False). Returns logits at all K positions
     in parallel via a custom (T, prev_pos+T) attention mask
     (see attention_kernel._verify_mask).
  5. Walk K positions: accept while draft argmax matches full model
     argmax. At first divergence, sample a new token from the full
     logits and stop. Cache pos = saved + n_accepted (+ 1 if
     resampled).
  6. Repeat until target token count.

KV cache state on rejection: with the (k_buf, v_buf, pos) Phase-1c
representation, "rewind" is just decrementing pos. The buffer
positions saved+n_accepted..saved+K-1 hold stale verify-write K/V
that get overwritten on the next outer iteration's draft.
"""
from __future__ import annotations

from typing import Callable, Optional

import torch
import torch.nn.functional as F


def _cache_save_pos(caches: list) -> list:
    """Snapshot just the integer pos of each per-layer cache. Layers
    where the cache is nil/None contribute 0 (will overwrite cleanly
    on first append)."""
    out = []
    for c in caches:
        if c is None:
            out.append(0)
        else:
            out.append(c[2])
    return out


def _cache_rewind(caches: list, saved_pos: list) -> list:
    """Return new caches with pos rewound to saved values. Buffers
    are reused (same tensors); only the int pos changes."""
    out = []
    for c, p in zip(caches, saved_pos):
        if c is None:
            out.append(None)
        else:
            out.append((c[0], c[1], p))
    return out


def speculative_sample(
    forward_fn: Callable,
    model,
    prompt_tokens: torch.Tensor,
    n_tokens: int,
    K: int = 4,
    greedy: bool = True,
) -> tuple:
    """Generate up to `n_tokens` new tokens after `prompt_tokens` via
    speculative decoding.

    forward_fn(model, tokens, sc, lc, skip_bank) -> (logits, sc', lc')

    Returns (full_token_tensor, stats_dict).

    stats_dict:
      n_outer_iters     — speculative loop iterations
      n_drafted         — total draft tokens generated
      n_accepted        — total tokens kept from drafts
      n_resampled       — divergence resamples (one per outer iter
                          unless the entire K-batch was accepted)
      acceptance_rate   — n_accepted / n_drafted
      avg_tokens_per_iter — measured per-iter throughput
    """
    device = prompt_tokens.device

    # Prefill
    logits, sc, lc = forward_fn(model, prompt_tokens, None, None, False)
    last_logits = logits[:, -1, :]                               # (1, vocab)

    toks = prompt_tokens
    n_remaining = n_tokens
    n_outer = 0
    n_drafted_total = 0
    n_accepted_total = 0
    n_resampled_total = 0

    while n_remaining > 0:
        n_outer += 1
        # 1. Snapshot cache positions
        saved_pos_s = _cache_save_pos(sc)
        saved_pos_l = _cache_save_pos(lc)

        # 2. Draft K tokens with skip_bank=True. Greedy by default
        # so the acceptance criterion (argmax match) actually has a
        # non-trivial chance of matching. Stochastic draft + greedy
        # accept gave near-zero acceptance in practice.
        draft_tokens = []
        cur_logits = last_logits
        cur_sc, cur_lc = sc, lc
        K_eff = min(K, n_remaining)
        for _ in range(K_eff):
            if greedy:
                tok = cur_logits.argmax(dim=-1, keepdim=True)    # (1, 1)
            else:
                probs = F.softmax(cur_logits, dim=-1)
                tok = torch.multinomial(probs, 1)
            draft_tokens.append(tok)
            new_logits, cur_sc, cur_lc = forward_fn(
                model, tok, cur_sc, cur_lc, True
            )
            cur_logits = new_logits[:, -1, :]
        n_drafted_total += K_eff

        # 3. Rewind cache to before draft
        sc_rewound = _cache_rewind(sc, saved_pos_s)
        lc_rewound = _cache_rewind(lc, saved_pos_l)

        # 4. Verify: K draft tokens through full model in one forward.
        # Concat the K drafts into a (1, K) tensor.
        draft_tensor = torch.cat(draft_tokens, dim=1)            # (1, K)
        verify_logits, sc_verified, lc_verified = forward_fn(
            model, draft_tensor, sc_rewound, lc_rewound, False
        )                                                         # (1, K, vocab)

        # 5. Accept tokens up to first divergence (greedy match on
        # the full model's argmax). For sampling-based generation
        # we'd use a stochastic acceptance criterion (Leviathan et al.
        # 2023); greedy accept is the simpler proxy and matches what
        # most production implementations ship by default for K small.
        n_accepted = 0
        for k in range(K_eff):
            full_argmax = verify_logits[:, k, :].argmax(dim=-1)  # (1,)
            draft_tok = draft_tokens[k].squeeze(-1)              # (1,)
            if torch.equal(full_argmax, draft_tok):
                n_accepted += 1
            else:
                break

        n_accepted_total += n_accepted

        # Build the accepted-tokens tensor and roll cache forward.
        if n_accepted == K_eff:
            # All accepted: take all draft tokens; cache is already at
            # saved+K (sc_verified). Sample next-token from the verify
            # forward's last logit position to seed the next iter.
            new_tokens = draft_tensor                            # (1, K)
            sc, lc = sc_verified, lc_verified
            last_logits = verify_logits[:, -1, :]
            n_consumed = K_eff
            # NB: no resample — the verify-K logits already gave us
            # the next-token distribution at the K-th position.
        else:
            # Reject from position n_accepted onward. Resample at the
            # divergence point from the full model's logits there.
            n_resampled_total += 1
            divergence_logits = verify_logits[:, n_accepted, :]  # (1, vocab)
            if greedy:
                resampled = divergence_logits.argmax(dim=-1, keepdim=True)
            else:
                resampled = torch.multinomial(
                    F.softmax(divergence_logits, dim=-1), 1
                )                                                 # (1, 1)
            accepted_part = (
                draft_tensor[:, :n_accepted] if n_accepted > 0 else None
            )
            if accepted_part is not None:
                new_tokens = torch.cat([accepted_part, resampled], dim=1)
            else:
                new_tokens = resampled
            # Cache: verify wrote K positions of K/V; rewind to
            # saved + n_accepted, then we still need the resampled
            # token's K/V which the verify forward did NOT compute.
            # The next outer iter's draft will write it on first call.
            # So we pre-roll cache to saved + n_accepted, then run
            # one extra forward to materialize the resampled K/V.
            sc = _cache_rewind(sc_verified, [
                p + n_accepted for p in saved_pos_s
            ])
            lc = _cache_rewind(lc_verified, [
                p + n_accepted for p in saved_pos_l
            ])
            # Forward the resampled token (full mode) to update cache.
            last_full_logits, sc, lc = forward_fn(
                model, resampled, sc, lc, False
            )
            last_logits = last_full_logits[:, -1, :]
            n_consumed = n_accepted + 1

        toks = torch.cat([toks, new_tokens], dim=1)
        n_remaining -= n_consumed

    stats = {
        "n_outer_iters":      n_outer,
        "n_drafted":          n_drafted_total,
        "n_accepted":         n_accepted_total,
        "n_resampled":        n_resampled_total,
        "acceptance_rate":    n_accepted_total / max(n_drafted_total, 1),
        "avg_tokens_per_iter": n_tokens / max(n_outer, 1),
    }
    return toks, stats
