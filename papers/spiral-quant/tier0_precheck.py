"""Tier 0 — Distributional pre-check.

Loads a small RoPE-based open LLM (default: SmolLM2-135M), runs forward
passes on a corpus sample, captures key vectors *after* RoPE at every
layer, splits them into the natural 2-D dimension pairs, and reports
distributional statistics needed to decide whether log-polar
quantization (LPQ) is worth pursuing on real data.

Outputs:
  - dumps/k_post_rope.pt   : raw tensor dump for Tier 1 to reuse
  - tier0_results.md       : human-readable findings

Pure-CPU. No training. No backward.
"""

import json
import math
import os
import statistics
import time
from pathlib import Path

import torch

HERE = Path(__file__).resolve().parent
DUMPS = HERE / "dumps"
DUMPS.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# config
# ---------------------------------------------------------------------------

MODEL_ID = os.environ.get("MODEL_ID", "HuggingFaceTB/SmolLM2-135M")
N_SEQS = int(os.environ.get("N_SEQS", "32"))
SEQ_LEN = int(os.environ.get("SEQ_LEN", "256"))
DEVICE = "cpu"
DTYPE = os.environ.get("MMLLM_DTYPE", "fp32").lower()
OUT_TAG = os.environ.get("OUT_TAG", "")  # e.g. "qwen1_5b" — appended to results.md

# Default WikiText-2-ish prompts (we don't download a dataset; we synthesize
# a small but diverse text source). Note: K distribution stats are dominated
# by the model + RoPE structure, not by content — see Liu et al. 2024.
DEFAULT_TEXTS = [
    "The Roman Empire was founded by Augustus in 27 BC. Over the next few "
    "centuries, it expanded across Europe, North Africa, and the Middle East. "
    "Its legal and administrative systems profoundly influenced later European "
    "civilizations.",
    "In mathematics, a prime number is a natural number greater than 1 that "
    "is not a product of two smaller natural numbers. The fundamental theorem "
    "of arithmetic establishes that every integer greater than 1 can be "
    "uniquely written as a product of primes.",
    "Photosynthesis is the process by which green plants convert sunlight, "
    "carbon dioxide, and water into glucose and oxygen. Chlorophyll absorbs "
    "light in the blue and red wavelengths while reflecting green, which is "
    "why most leaves appear green.",
    "The transformer architecture, introduced in 'Attention Is All You Need' "
    "by Vaswani et al. in 2017, has become the dominant approach in natural "
    "language processing. Its self-attention mechanism allows the model to "
    "weigh the importance of different tokens in a sequence.",
    "Beethoven's Ninth Symphony, completed in 1824, was his final complete "
    "symphony and is widely regarded as a masterpiece of Western classical "
    "music. The fourth movement features a chorus singing Friedrich Schiller's "
    "poem 'Ode to Joy'.",
    "Quantum mechanics describes nature at the smallest scales of energy "
    "levels of atoms and subatomic particles. It departs from classical "
    "mechanics primarily at quantum levels through phenomena such as "
    "superposition, entanglement, and uncertainty.",
    "The Great Barrier Reef, off the coast of Queensland, Australia, is the "
    "world's largest coral reef system. It is composed of over 2,900 "
    "individual reefs and 900 islands stretching for over 2,300 kilometers.",
    "Programming is the process of designing and building executable computer "
    "programs to accomplish specific computing results. It involves analysis, "
    "algorithms, coding, verification, debugging, and maintenance of source "
    "code.",
]


# ---------------------------------------------------------------------------
# hooking
# ---------------------------------------------------------------------------

class KCapture:
    """Captures key tensors *after* RoPE by monkey-patching
    `apply_rotary_pos_emb`. Handles two function signatures:

    - Llama / Qwen style: ``apply_rotary_pos_emb(q, k, cos, sin)`` returning
      a tuple. We grab the K return.
    - Gemma 4 style: ``apply_rotary_pos_emb(x, cos, sin, unsqueeze_dim=...)``
      called separately for Q and K. We capture every output and then
      identify K tensors by their shape (fewer heads than Q under GQA).

    The captured tensors are filtered post-hoc to keep only K (by shape:
    the smaller head-count branch).
    """

    def __init__(self):
        self.k_per_layer = []      # filtered list, K only
        self._all_outs = []        # raw capture, both Q and K
        self._signature = None     # "qk" (llama-style) or "single" (gemma4-style)

    def reset(self):
        self.k_per_layer = []
        self._all_outs = []

    def finalize(self):
        """After the forward pass, if we captured single-tensor outputs
        (Gemma 4 style), filter to keep only the K tensors. K is identified
        as the smaller-num-heads of the (Q, K) pair within each layer."""
        if self._signature == "qk":
            return  # k_per_layer already populated correctly
        if not self._all_outs:
            return
        # Gemma 4 style: outputs alternate Q, K, Q, K, ...
        # On shared-KV layers, K may be missing — so we identify K by
        # shape rather than position.
        # Heuristic: the unique head counts in self._all_outs tells us
        # Q vs K. The smaller one is K (under GQA).
        head_counts = set()
        for t in self._all_outs:
            # shape is (B, T, H, D) or (B, H, T, D) — head dim is at index 1 or 2
            # For Gemma 4 the call is before transpose, so (B, T, H, D)
            # H is the second-to-last dim before head_dim
            head_counts.add(t.shape[-2])
        if len(head_counts) == 1:
            # No GQA detected (or shape ambiguity) — treat every other as K
            self.k_per_layer = self._all_outs[1::2]
        else:
            k_heads = min(head_counts)
            self.k_per_layer = [t for t in self._all_outs if t.shape[-2] == k_heads]

    def patched_apply(self, original_fn):
        # Detect signature by inspecting parameters
        import inspect
        try:
            sig = inspect.signature(original_fn)
            params = list(sig.parameters.keys())
        except (ValueError, TypeError):
            params = []

        # Heuristic: if first 2 params look like (q, k) it's the dual form
        is_dual = (
            len(params) >= 2 and
            params[0].lower() in ("q", "query", "query_states") and
            params[1].lower() in ("k", "key", "key_states")
        )

        if is_dual:
            self._signature = "qk"
            def wrapper(q, k, cos, sin, *args, **kwargs):
                out_q, out_k = original_fn(q, k, cos, sin, *args, **kwargs)
                self.k_per_layer.append(out_k.detach().to("cpu").float().clone())
                return out_q, out_k
            return wrapper
        else:
            self._signature = "single"
            def wrapper(x, *args, **kwargs):
                out = original_fn(x, *args, **kwargs)
                self._all_outs.append(out.detach().to("cpu").float().clone())
                return out
            return wrapper


# ---------------------------------------------------------------------------
# statistics on (x, y) pair distributions
# ---------------------------------------------------------------------------

def pair_stats(k_layer: torch.Tensor) -> dict:
    """k_layer shape (B, H, T, D). Split D into D/2 pairs along the last
    axis (per RoPE's interleave-or-block convention). HF Llama-style RoPE
    pairs are *blocked*: dims [0..D/2) rotate with dims [D/2..D). We use
    the blocked convention.

    Returns aggregate stats over all (B, H, T, D/2) pairs:
      r_mean, r_median, r_std, r_max, r_min_nz, r_p95, r_p99, r_p999
      theta_uniformity (mean of |cos(K*theta)| over K=1..8 — 0 if uniform)
      tail_alpha (Hill estimator with k = top 5%)
      log_normality_score (KS-like distance to fitted lognormal)
    """
    B, H, T, D = k_layer.shape
    assert D % 2 == 0
    half = D // 2
    x = k_layer[..., :half]   # (B, H, T, D/2)
    y = k_layer[..., half:]   # (B, H, T, D/2)

    r = (x * x + y * y).sqrt().flatten()
    theta = torch.atan2(y, x).flatten()
    n = r.numel()

    r_sorted, _ = r.sort()
    nz_mask = r_sorted > 1e-12
    r_nz = r_sorted[nz_mask]

    def pct(t, p):
        idx = max(0, min(t.numel() - 1, int(p * t.numel())))
        return float(t[idx])

    # Hill tail exponent on top 5%
    if r_nz.numel() > 100:
        k = max(10, int(0.05 * r_nz.numel()))
        top = r_nz[-k:]
        cutoff = r_nz[-k - 1]
        if cutoff > 0:
            alpha_hat = 1.0 / (torch.log(top).mean() - math.log(cutoff)).item()
        else:
            alpha_hat = float("nan")
    else:
        alpha_hat = float("nan")

    # Angular uniformity: mean over K of |E[cos(K*theta)]| ; 0 if perfectly
    # uniform, increases with concentration
    ang_score = 0.0
    for kk in range(1, 9):
        ang_score += float(torch.cos(kk * theta).mean().abs())
    ang_score /= 8.0

    # Log-normality: compare empirical log-r quantiles to a normal fit
    if r_nz.numel() > 1000:
        log_r = r_nz.log()
        mu, sigma = float(log_r.mean()), float(log_r.std())
        # KS-ish distance using a sub-sample of quantiles
        from math import erf, sqrt
        zs = (log_r - mu) / max(sigma, 1e-9)
        zs_sorted, _ = zs.sort()
        m = zs_sorted.numel()
        # empirical CDF at each point: i/m
        # theoretical CDF: Phi(z)
        # KS = max |F_emp - Phi|
        ks = 0.0
        step = max(1, m // 1000)
        for i in range(0, m, step):
            z = float(zs_sorted[i])
            phi = 0.5 * (1 + erf(z / sqrt(2)))
            f_emp = (i + 1) / m
            ks = max(ks, abs(f_emp - phi))
        log_normality_ks = ks
    else:
        log_normality_ks = float("nan")

    return {
        "n_pairs": n,
        "r_mean": float(r.mean()),
        "r_median": pct(r_sorted, 0.50),
        "r_std": float(r.std()),
        "r_max": float(r_sorted[-1]),
        "r_min_nz": float(r_nz[0]) if r_nz.numel() else float("nan"),
        "r_p95": pct(r_sorted, 0.95),
        "r_p99": pct(r_sorted, 0.99),
        "r_p999": pct(r_sorted, 0.999),
        "r_dyn_range": pct(r_sorted, 0.999) / max(pct(r_sorted, 0.001), 1e-9),
        "tail_alpha_hill": alpha_hat,
        "ang_uniformity_score": ang_score,
        "log_normality_ks": log_normality_ks,
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    print(f"[tier0] model={MODEL_ID} device={DEVICE}")
    print(f"[tier0] N_SEQS={N_SEQS} SEQ_LEN={SEQ_LEN}")
    t0 = time.time()

    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"[tier0] dtype={DTYPE}")
    print("[tier0] loading tokenizer + model...")
    tok = AutoTokenizer.from_pretrained(MODEL_ID)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    torch_dtype = {"fp16": torch.float16, "bf16": torch.bfloat16,
                   "fp32": torch.float32}[DTYPE]
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype=torch_dtype)
    model.eval()
    model.to(DEVICE)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"[tier0] loaded {n_params/1e6:.1f}M params in {time.time()-t0:.1f}s")

    # Monkey-patch apply_rotary_pos_emb in the model's modeling module
    cap = KCapture()
    # Locate the function
    # transformers organizes per-model, e.g. transformers.models.llama.modeling_llama
    mod = type(model).__module__
    import importlib
    modeling = importlib.import_module(mod)
    if hasattr(modeling, "apply_rotary_pos_emb"):
        original = modeling.apply_rotary_pos_emb
        modeling.apply_rotary_pos_emb = cap.patched_apply(original)
        print(f"[tier0] patched {mod}.apply_rotary_pos_emb")
    else:
        raise RuntimeError(f"could not find apply_rotary_pos_emb in {mod}")

    # Tokenize and pad/truncate to SEQ_LEN
    texts = []
    for i in range(N_SEQS):
        texts.append(DEFAULT_TEXTS[i % len(DEFAULT_TEXTS)])
    enc = tok(texts, return_tensors="pt", padding="max_length",
              max_length=SEQ_LEN, truncation=True)
    input_ids = enc["input_ids"].to(DEVICE)
    attention_mask = enc["attention_mask"].to(DEVICE)
    print(f"[tier0] tokenized {N_SEQS} seqs, shape={tuple(input_ids.shape)}")

    # Forward pass with hook capturing K post-RoPE
    print("[tier0] running forward pass...")
    t_fw = time.time()
    cap.reset()
    with torch.no_grad():
        _ = model(input_ids=input_ids, attention_mask=attention_mask,
                  use_cache=False)
    fw_secs = time.time() - t_fw
    cap.finalize()
    n_layers = len(cap.k_per_layer)
    print(f"[tier0] forward in {fw_secs:.1f}s, captured {n_layers} layers of K "
          f"(sig={cap._signature}, raw_outs={len(cap._all_outs)})")

    if not cap.k_per_layer:
        raise RuntimeError("no K captured; check RoPE patch")

    sample = cap.k_per_layer[0]
    print(f"[tier0] K[layer0] shape = {tuple(sample.shape)}, dtype={sample.dtype}")

    # Per-layer stats
    print("[tier0] computing per-layer statistics...")
    per_layer = []
    for i, kt in enumerate(cap.k_per_layer):
        s = pair_stats(kt)
        s["layer"] = i
        per_layer.append(s)

    # Aggregate stats — stack all layers into one tensor
    print("[tier0] computing aggregate statistics...")
    # Gemma 4 has heterogeneous head_dim per layer (local vs global
    # attention). Pool the per-pair (r, theta) directly instead of
    # concatenating raw tensors.
    head_dims = sorted({kt.shape[-1] for kt in cap.k_per_layer})
    if len(head_dims) == 1:
        all_k = torch.cat([kt.reshape(-1, kt.shape[-1]) for kt in cap.k_per_layer], dim=0)
        all_k = all_k.unsqueeze(0).unsqueeze(0)  # (1, 1, N, D)
        agg = pair_stats(all_k)
    else:
        # Mixed head_dim: aggregate per-pair quantities across all layers
        import math as _math
        print(f"[tier0]   heterogeneous head_dims: {head_dims}")
        rs, thetas = [], []
        for kt in cap.k_per_layer:
            B, H, T, D = kt.shape
            half = D // 2
            x = kt[..., :half].reshape(-1)
            y = kt[..., half:].reshape(-1)
            rs.append((x * x + y * y).sqrt())
            thetas.append(torch.atan2(y, x))
        r_all = torch.cat(rs)
        theta_all = torch.cat(thetas)
        # Build a synthetic tensor to feed pair_stats: shape (1, 1, N, 2)
        # with first half = r*cos(theta), second half = r*sin(theta).
        # Round-trip preserves the pair statistics.
        N = r_all.numel()
        synth = torch.empty(1, 1, N, 2)
        synth[0, 0, :, 0] = r_all * theta_all.cos()
        synth[0, 0, :, 1] = r_all * theta_all.sin()
        agg = pair_stats(synth)

    # Save tensors for tier 1
    print("[tier0] saving K dumps for tier 1...")
    torch.save({
        "k_per_layer": cap.k_per_layer,
        "model_id": MODEL_ID,
        "n_seqs": N_SEQS,
        "seq_len": SEQ_LEN,
    }, DUMPS / "k_post_rope.pt")

    # Write results.md
    out = []
    out.append(f"# Tier 0 — Distributional Pre-check\n")
    out.append(f"\nModel: `{MODEL_ID}`  ")
    out.append(f"\nN_seqs × seq_len: {N_SEQS} × {SEQ_LEN}  ")
    out.append(f"\nLayers captured: {n_layers}  ")
    out.append(f"\nForward time (CPU): {fw_secs:.1f}s\n")

    out.append("\n## Aggregate stats (all layers pooled)\n")
    for k, v in agg.items():
        if isinstance(v, float):
            out.append(f"- **{k}**: {v:.4g}")
        else:
            out.append(f"- **{k}**: {v}")
    out.append("")

    out.append("\n## Per-layer stats\n")
    fields = ["layer", "r_median", "r_p99", "r_p999", "r_dyn_range",
              "tail_alpha_hill", "ang_uniformity_score", "log_normality_ks"]
    out.append("| " + " | ".join(fields) + " |")
    out.append("|" + "---|" * len(fields))
    for s in per_layer:
        row = []
        for f in fields:
            v = s[f]
            if isinstance(v, float):
                row.append(f"{v:.4g}")
            else:
                row.append(str(v))
        out.append("| " + " | ".join(row) + " |")

    # Interpretation
    out.append("\n## Interpretation\n")
    alphas = [s["tail_alpha_hill"] for s in per_layer
              if not math.isnan(s["tail_alpha_hill"])]
    dynr = [s["r_dyn_range"] for s in per_layer]
    ks_log = [s["log_normality_ks"] for s in per_layer
              if not math.isnan(s["log_normality_ks"])]
    if alphas:
        out.append(f"- Median Hill tail exponent across layers: **{statistics.median(alphas):.3g}** "
                   f"(min {min(alphas):.3g}, max {max(alphas):.3g}). "
                   f"Lower = heavier tail. Gaussian ≈ ∞; lognormal varies; "
                   f"Pareto with finite mean has α > 1.")
    if dynr:
        out.append(f"- Median dynamic range (p999/p001) across layers: **{statistics.median(dynr):.3g}**. "
                   f"This is the multiplicative span LPQ's ρ axis needs to cover.")
    if ks_log:
        out.append(f"- Median KS distance to log-normal fit: **{statistics.median(ks_log):.3g}**. "
                   f"Lower = closer to lognormal. Values < 0.05 are strong support.")
    angs = [s["ang_uniformity_score"] for s in per_layer]
    if angs:
        out.append(f"- Median angular uniformity score: **{statistics.median(angs):.3g}** "
                   f"(0 = perfectly uniform; the RoPE-pair angle distribution is "
                   f"reportedly near-uniform with mild concentration).")

    suffix = f".{OUT_TAG}" if OUT_TAG else ""
    out_path = HERE / f"tier0_results{suffix}.md"
    with open(out_path, "w") as fh:
        fh.write("\n".join(out))
    print(f"[tier0] wrote {out_path.name}")
    print(f"[tier0] total wall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
