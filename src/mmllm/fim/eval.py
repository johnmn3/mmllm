"""FIM-eval — measure middle-fill capability of a trained ckpt.

Two metrics per example:

  - FIM-bpc: byte-level cross-entropy on the gold middle, conditioned
    on the prefix+suffix layout. Lower = better.

  - FIM-exact: does greedy decoding produce gold middle EXACTLY?
    A binary outcome per example; reported as fraction over the eval
    set.

Both metrics also reported per-language by inspecting the eval JSONL's
`language` field.

Usage from the CLI:
    mmllm fim-eval <ckpt-dir> <eval-jsonl>

The eval JSONL is produced by `scripts/build_fim_eval.py`. Each line:
    {"language": str, "prefix": str, "suffix": str, "gold_middle": str}"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import torch
import torch.nn.functional as F

from mmllm.fim.markers import FIM_PRE, FIM_SUF, FIM_MID, FIM_EOM


def _encode(s: str | bytes) -> bytes:
    if isinstance(s, bytes):
        return s
    return s.encode("utf-8", errors="replace")


def _build_input(prefix: bytes, suffix: bytes) -> bytes:
    """PSM-mode input up to (and including) the <|fim_mid|> marker.
    Model continues from here to fill in the middle."""
    return FIM_PRE + prefix + FIM_SUF + suffix + FIM_MID


def fim_bpc_one(model, forward_fn, prefix: bytes, suffix: bytes,
                gold_middle: bytes, device: str = "cpu") -> tuple[float, int]:
    """Compute byte-level CE on `gold_middle`, conditioned on prefix+suffix.
    Returns (mean_nats_per_byte, n_bytes_scored). Bpc = mean_nats / ln(2).

    Implementation: feed the full input <PRE>p<SUF>s<MID>middle<EOM>
    through forward (one shot), then index into the per-position logits
    at the middle byte positions and compute CE against the actual
    middle byte targets."""
    full = _build_input(prefix, suffix) + gold_middle + FIM_EOM
    x = torch.tensor([list(full)], dtype=torch.long, device=device)
    with torch.no_grad():
        out = forward_fn(model, x)
    logits = out[0]   # (B=1, T, V)

    # Find middle span: between FIM_MID end and FIM_EOM start
    mid_start = full.find(FIM_MID) + len(FIM_MID)
    eom_start = full.find(FIM_EOM)
    if mid_start <= 0 or eom_start <= mid_start:
        return float("nan"), 0

    # Targets are full[mid_start..eom_start). Logits at position t
    # predict full[t+1], so logits at [mid_start-1..eom_start-1) → middle.
    pred_logits = logits[0, mid_start - 1:eom_start - 1, :]   # (n_mid, V)
    targets     = x[0,    mid_start    :eom_start]            # (n_mid,)
    n = targets.shape[0]
    if n == 0:
        return float("nan"), 0
    log_p = F.log_softmax(pred_logits, dim=-1)
    log_p_true = log_p.gather(-1, targets.unsqueeze(-1)).squeeze(-1)
    nats = -log_p_true.sum().item() / max(n, 1)
    return nats, n


def fim_greedy_decode(model, forward_fn, prefix: bytes, suffix: bytes,
                      max_middle: int = 256, device: str = "cpu") -> bytes:
    """Greedy-decode the middle from <|fim_mid|> until <|fim_eom|>
    (or max_middle exceeded). Returns the decoded middle bytes."""
    inp = list(_build_input(prefix, suffix))
    out_bytes = bytearray()
    eom_bytes = list(FIM_EOM)

    for _ in range(max_middle):
        x = torch.tensor([inp], dtype=torch.long, device=device)
        with torch.no_grad():
            out = forward_fn(model, x)
        logits = out[0][0, -1, :]   # last position
        next_b = int(torch.argmax(logits).item())
        out_bytes.append(next_b)
        inp.append(next_b)
        # Did we just complete an <|fim_eom|>?
        if (len(out_bytes) >= len(eom_bytes) and
            list(out_bytes[-len(eom_bytes):]) == eom_bytes):
            return bytes(out_bytes[:-len(eom_bytes)])
    return bytes(out_bytes)


def run_fim_eval(model, forward_fn, eval_path: Path | str, *,
                 device: str = "cpu",
                 do_greedy: bool = True,
                 max_middle: int = 256) -> dict:
    """Run the full FIM-eval over an eval-jsonl. Returns a dict with
    per-language and aggregate FIM-bpc + FIM-exact stats."""
    eval_path = Path(eval_path)
    per_lang_nats: dict[str, list[float]] = defaultdict(list)
    per_lang_bytes: dict[str, list[int]]  = defaultdict(list)
    per_lang_exact: dict[str, list[int]]  = defaultdict(list)

    n_total = 0
    with open(eval_path) as f:
        for line in f:
            row = json.loads(line)
            lang = row.get("language", "?")
            prefix = _encode(row["prefix"])
            suffix = _encode(row["suffix"])
            gold   = _encode(row["gold_middle"])

            nats, n = fim_bpc_one(model, forward_fn, prefix, suffix, gold, device=device)
            if n > 0:
                per_lang_nats[lang].append(nats * n)
                per_lang_bytes[lang].append(n)

            if do_greedy:
                pred = fim_greedy_decode(model, forward_fn, prefix, suffix,
                                         max_middle=max_middle, device=device)
                per_lang_exact[lang].append(1 if pred == gold else 0)
            n_total += 1

    # Aggregate
    out: dict = {"per_language": {}, "n_examples": n_total}
    overall_nats = 0.0
    overall_bytes = 0
    overall_exact_hits = 0
    overall_exact_total = 0
    for lang in sorted(per_lang_nats):
        nats_sum = sum(per_lang_nats[lang])
        bytes_sum = sum(per_lang_bytes[lang])
        bpc = (nats_sum / max(bytes_sum, 1)) / math.log(2)
        exact = per_lang_exact.get(lang, [])
        exact_pct = (sum(exact) / max(len(exact), 1)) * 100 if exact else None
        out["per_language"][lang] = {
            "n_examples":  len(per_lang_bytes[lang]),
            "n_bytes":     bytes_sum,
            "bpc":         bpc,
            "exact_pct":   exact_pct,
        }
        overall_nats += nats_sum
        overall_bytes += bytes_sum
        overall_exact_hits  += sum(exact) if exact else 0
        overall_exact_total += len(exact)

    out["overall"] = {
        "bpc":        (overall_nats / max(overall_bytes, 1)) / math.log(2),
        "exact_pct":  (overall_exact_hits / max(overall_exact_total, 1)) * 100
                      if overall_exact_total > 0 else None,
        "n_bytes":    overall_bytes,
    }
    return out


def print_summary(result: dict) -> None:
    print(f"=== FIM eval summary ({result['n_examples']} examples) ===")
    print(f"{'language':>10s}  {'n':>4s}  {'bytes':>6s}  {'bpc':>6s}  {'exact%':>8s}")
    for lang, r in result["per_language"].items():
        ex = f'{r["exact_pct"]:.1f}' if r["exact_pct"] is not None else "  -"
        print(f"{lang:>10s}  {r['n_examples']:>4d}  {r['n_bytes']:>6d}  "
              f"{r['bpc']:>6.3f}  {ex:>8s}")
    o = result["overall"]
    ex = f'{o["exact_pct"]:.1f}' if o["exact_pct"] is not None else "  -"
    print(f"{'OVERALL':>10s}  ----  {o['n_bytes']:>6d}  {o['bpc']:>6.3f}  {ex:>8s}")
