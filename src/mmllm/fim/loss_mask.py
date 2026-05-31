"""Per-position loss mask for FIM training.

When `MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY=true` the train-step searches each
batch's input bytes for `<|fim_mid|>` ... `<|fim_eom|>` spans and zeroes
the per-position CE outside them. The model trains only on the middle
prediction; prefix and suffix bytes are conditioning context.

For mixed corpora (some FIM, some raw causal), examples without a
`<|fim_mid|>` marker get an all-1 mask (full CE everywhere — standard
causal LM behavior preserved).

Implementation: simple byte-pattern match per row. CPU loop, ~100 µs per
batch at B=16; negligible vs the forward pass. Vectorizable later if
benchmarks show it as a hot spot."""

from __future__ import annotations

import torch

from mmllm.fim.markers import FIM_MID, FIM_EOM


def _find_all(haystack: bytes, needle: bytes) -> list[int]:
    """Return all start indices of `needle` in `haystack`."""
    out: list[int] = []
    i = haystack.find(needle, 0)
    while i != -1:
        out.append(i)
        i = haystack.find(needle, i + 1)
    return out


def fim_loss_mask(x_bytes: torch.Tensor) -> torch.Tensor:
    """x_bytes: (B, T) int64 byte ids.
    Returns: (B, T) float32 mask with 1.0 inside any
    `<|fim_mid|>...<|fim_eom|>` span, 0.0 elsewhere.

    Special case: rows that don't contain `<|fim_mid|>` get an all-1.0
    mask (preserves standard causal LM behavior on non-FIM batches).

    The mask aligns with the y (target) tensor — position t in the mask
    is the weight on the model's prediction at byte position t."""
    B, T = x_bytes.shape
    out = torch.zeros(B, T, dtype=torch.float32, device=x_bytes.device)
    mid_len = len(FIM_MID)
    eom_len = len(FIM_EOM)

    # CPU per-row scan — correct, fast enough for typical batch sizes
    cpu_x = x_bytes.detach().cpu()
    for b in range(B):
        row = bytes(cpu_x[b].numpy().tolist())
        mid_starts = _find_all(row, FIM_MID)
        if not mid_starts:
            # Non-FIM example — full causal CE
            out[b].fill_(1.0)
            continue
        eom_starts = _find_all(row, FIM_EOM)

        # Greedy pair: each mid start pairs with the next eom start after it
        ei = 0
        for ms in mid_starts:
            mid_inside_start = ms + mid_len
            # Advance to first eom after this mid
            while ei < len(eom_starts) and eom_starts[ei] < mid_inside_start:
                ei += 1
            if ei < len(eom_starts):
                end = eom_starts[ei]
                ei += 1
            else:
                end = T
            # Clip to row bounds
            s = min(mid_inside_start, T)
            e = min(end, T)
            if s < e:
                out[b, s:e].fill_(1.0)
    return out
