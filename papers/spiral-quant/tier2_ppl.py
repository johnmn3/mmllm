"""Tier 2 — End-to-end perplexity with quantized K (post-RoPE).

Instead of implementing true cache surgery, we install a round-trip
quantizer on K immediately after RoPE: K -> Q -> Q^{-1}. This is
mathematically identical (up to numerical precision) to a KV cache
that quantizes on write and dequantizes on read, with the simplification
that the quantization scales are computed from the current batch's K
distribution rather than from a calibrated rolling estimate.

We then measure cross-entropy / perplexity on a small held-out text
sample and compare to the FP32 baseline.

Outputs:
  - tier2_results.md
  - tier2_per_config.csv
"""

import csv
import math
import os
import time
from pathlib import Path

import torch

from tier1_recon import (
    quant_cart_uniform_t, quant_polar_t, quant_log_polar_t,
    quant_fp4_like_t, quant_log_polar_hybrid_t, quant_polar_hybrid_t,
    quant_log_polar_zerofloor_t, quant_turbo_t, _TURBOQUANT_AVAILABLE,
)

HERE = Path(__file__).resolve().parent
MODEL_ID = os.environ.get("MODEL_ID", "HuggingFaceTB/SmolLM2-135M")
N_SEQS = int(os.environ.get("N_SEQS", "16"))
SEQ_LEN = int(os.environ.get("SEQ_LEN", "256"))
DEVICE = "cpu"
DTYPE = os.environ.get("MMLLM_DTYPE", "fp32").lower()
OUT_TAG = os.environ.get("OUT_TAG", "")
FAST = os.environ.get("FAST", "0") == "1"  # skip non-headline configs to save wall time

EVAL_TEXTS = [
    # Domain-diverse, longer than training prompts to stress the K cache.
    "Photosynthesis is the process by which green plants and certain other "
    "organisms transform light energy into chemical energy. During this "
    "process, sunlight, carbon dioxide, and water are converted into glucose "
    "and oxygen. Most photosynthesis occurs in the chloroplasts of plant "
    "cells, which contain the pigment chlorophyll. Chlorophyll absorbs light "
    "primarily in the red and blue parts of the visible spectrum, reflecting "
    "green light, which gives plants their characteristic colour. The overall "
    "reaction can be summarized as: six molecules of carbon dioxide plus six "
    "molecules of water, in the presence of light energy, produce one "
    "molecule of glucose plus six molecules of oxygen.",

    "A prime number is a natural number greater than one whose only positive "
    "divisors are one and itself. The first few primes are two, three, five, "
    "seven, eleven, thirteen, seventeen, nineteen, twenty-three, and "
    "twenty-nine. The fundamental theorem of arithmetic states that every "
    "integer greater than one can be expressed uniquely, up to ordering, as a "
    "product of prime numbers. Euclid proved around three hundred BC that "
    "there are infinitely many primes. The distribution of primes is a "
    "central topic in number theory, with the prime number theorem giving an "
    "asymptotic estimate for the count of primes up to a given value.",

    "The transformer architecture has become the dominant approach to natural "
    "language processing since its introduction in two thousand seventeen. "
    "Unlike recurrent neural networks, transformers process the entire input "
    "sequence in parallel through a mechanism called self-attention. Each "
    "position in the sequence can attend to every other position, allowing "
    "the model to capture long-range dependencies efficiently. Modern "
    "language models such as the GPT, Llama, and Qwen families all use "
    "variants of the transformer. Key innovations include rotary position "
    "embeddings, grouped-query attention, and various forms of normalization "
    "such as RMSNorm.",

    "Beethoven's Ninth Symphony in D minor, opus one hundred twenty five, was "
    "completed in eighteen twenty four and first performed in Vienna that "
    "same year. The work is notable for being the first example of a major "
    "composer using voices in a symphony. The fourth and final movement "
    "features a chorus and four vocal soloists singing a setting of Friedrich "
    "Schiller's poem Ode to Joy. The symphony is considered one of the "
    "greatest masterpieces of Western classical music. Its main theme has "
    "been adopted as the anthem of the European Union, and the manuscript "
    "is on the UNESCO Memory of the World register.",

    "The Pacific Ocean is the largest and deepest of the Earth's five "
    "oceanic divisions, covering approximately sixty three million square "
    "miles. It extends from the Arctic Ocean in the north to the Southern "
    "Ocean in the south and is bounded by Asia and Australia in the west and "
    "the Americas in the east. The deepest point on Earth, the Challenger "
    "Deep in the Mariana Trench, lies in the western Pacific at a depth of "
    "about thirty six thousand feet below sea level. The ocean contains over "
    "twenty five thousand islands, more than the total in the rest of the "
    "world's oceans combined.",

    "In computer science, sorting algorithms arrange elements of a list into "
    "a specific order, typically numerical or lexicographic. Important "
    "sorting algorithms include quicksort, mergesort, heapsort, and "
    "timsort. Quicksort works by selecting a pivot element and partitioning "
    "the array around it, then recursively sorting the partitions. "
    "Mergesort divides the array into halves, sorts each half, and merges "
    "the sorted halves. Both have average time complexity of O of n log n. "
    "Comparison-based sorting algorithms have a lower bound of n log n "
    "comparisons in the worst case.",

    "Quantum mechanics describes the behaviour of matter and light at the "
    "atomic and subatomic scales. It departs sharply from classical physics "
    "through phenomena such as wave-particle duality, the uncertainty "
    "principle, and quantum entanglement. The state of a quantum system is "
    "represented by a wavefunction, whose squared magnitude gives the "
    "probability density of finding a particle in a given configuration. "
    "Measurement collapses the wavefunction to one of its eigenstates. The "
    "Schrödinger equation governs the time evolution of wavefunctions in "
    "non-relativistic quantum mechanics.",

    "The Roman Republic was the era of classical Roman civilization between "
    "the overthrow of the Roman Kingdom in five hundred nine BC and the "
    "establishment of the Roman Empire in twenty seven BC. During this "
    "period Rome's control expanded from the city's immediate surroundings "
    "to hegemony over the entire Mediterranean world. The Republic was "
    "governed by a complex constitution centred on the principles of a "
    "separation of powers and checks and balances. The evolution of the "
    "constitution was heavily influenced by the struggle between the "
    "aristocracy and the ordinary citizens.",
]


def _make_quantizer(name: str, bits: int):
    if name == "fp32":
        return None  # no quantization (baseline)
    if name == "cart":
        return lambda t: quant_cart_uniform_t(t, bits)
    if name == "polar":
        return lambda t: quant_polar_t(t, bits)
    if name == "log_polar":
        return lambda t: quant_log_polar_t(t, bits)
    if name == "fp4_like":
        return lambda t: quant_fp4_like_t(t, 8)
    if name == "log_polar_hyb1pct":
        return lambda t: quant_log_polar_hybrid_t(t, bits, 0.01)
    if name == "polar_hyb1pct":
        return lambda t: quant_polar_hybrid_t(t, bits, 0.01)
    if name == "log_polar_zf25":
        return lambda t: quant_log_polar_zerofloor_t(t, bits, 0.25)
    if name == "log_polar_zf50":
        return lambda t: quant_log_polar_zerofloor_t(t, bits, 0.50)
    if name == "log_polar_zf75":
        return lambda t: quant_log_polar_zerofloor_t(t, bits, 0.75)
    if name == "turbo":
        return lambda t: quant_turbo_t(t, bits)
    raise ValueError(f"unknown quantizer {name}")


class QuantHook:
    """Replaces the model's `apply_rotary_pos_emb` with a version that
    quantize-then-dequantizes K right after RoPE. Q is left alone.

    Handles two signatures:
    - Llama/Qwen: ``apply_rotary_pos_emb(q, k, cos, sin)`` → tuple
    - Gemma 4:    ``apply_rotary_pos_emb(x, cos, sin, unsqueeze_dim=...)``
      called separately for Q and K; we identify K by its smaller head count
      under GQA (cached per-call by examining the head count vs the
      historical min/max during this run).
    """

    def __init__(self, q_fn):
        self.q_fn = q_fn
        # head-count tracking for the gemma-style single-tensor case
        self._head_counts = set()

    def patched_apply(self, original_fn):
        import inspect
        try:
            sig = inspect.signature(original_fn)
            params = list(sig.parameters.keys())
        except (ValueError, TypeError):
            params = []
        is_dual = (
            len(params) >= 2 and
            params[0].lower() in ("q", "query", "query_states") and
            params[1].lower() in ("k", "key", "key_states")
        )
        if is_dual:
            def wrapper(q, k, cos, sin, *args, **kwargs):
                out_q, out_k = original_fn(q, k, cos, sin, *args, **kwargs)
                if self.q_fn is not None:
                    with torch.no_grad():
                        out_k = self.q_fn(out_k)
                return out_q, out_k
            return wrapper
        else:
            # Single-tensor RoPE: we don't know if it's Q or K from the call
            # alone. Apply quantization only when the tensor's head count is
            # the smaller of (Q, K) — i.e. K under GQA. We learn the head
            # counts adaptively: the first time we see two distinct counts,
            # we know which is K.
            def wrapper(x, *args, **kwargs):
                out = original_fn(x, *args, **kwargs)
                if self.q_fn is None:
                    return out
                # K is the smaller head count; we track and decide.
                h = out.shape[-2]
                self._head_counts.add(h)
                if len(self._head_counts) >= 2 and h == min(self._head_counts):
                    with torch.no_grad():
                        out = self.q_fn(out)
                # If we've only ever seen one head count so far, defer; we
                # cannot tell Q from K yet. This means we miss the first
                # K of the run, but on a multi-layer forward this is at
                # most one layer's worth of K (≪ 1 % of total).
                return out
            return wrapper


def perplexity_ce(model, input_ids, attention_mask):
    """Compute mean cross-entropy in nats over the non-pad next-token
    positions. Returns (ce_nats, n_tokens_scored)."""
    with torch.no_grad():
        out = model(input_ids=input_ids, attention_mask=attention_mask,
                    use_cache=False)
    logits = out.logits  # (B, T, V)
    # Standard LM loss: predict next token from current logits
    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = input_ids[:, 1:].contiguous()
    shift_mask = attention_mask[:, 1:].contiguous().float()
    # Cross-entropy per position
    log_probs = shift_logits.log_softmax(dim=-1)
    nll = -log_probs.gather(2, shift_labels.unsqueeze(-1)).squeeze(-1)
    nll = nll * shift_mask
    total_nll = nll.sum().item()
    total_n = shift_mask.sum().item()
    return total_nll, total_n


def main():
    t0 = time.time()
    print(f"[tier2] model={MODEL_ID} N_SEQS={N_SEQS} SEQ_LEN={SEQ_LEN}")

    from transformers import AutoModelForCausalLM, AutoTokenizer
    import importlib

    print(f"[tier2] dtype={DTYPE}")
    print("[tier2] loading model...")
    tok = AutoTokenizer.from_pretrained(MODEL_ID)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    torch_dtype = {"fp16": torch.float16, "bf16": torch.bfloat16,
                   "fp32": torch.float32}[DTYPE]
    model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype=torch_dtype)
    model.eval()
    model.to(DEVICE)

    # Tokenize once
    texts = [EVAL_TEXTS[i % len(EVAL_TEXTS)] for i in range(N_SEQS)]
    enc = tok(texts, return_tensors="pt", padding="max_length",
              max_length=SEQ_LEN, truncation=True)
    input_ids = enc["input_ids"].to(DEVICE)
    attention_mask = enc["attention_mask"].to(DEVICE)
    print(f"[tier2] tokenized {N_SEQS} seqs, shape={tuple(input_ids.shape)}")

    mod_name = type(model).__module__
    modeling = importlib.import_module(mod_name)
    original_apply = modeling.apply_rotary_pos_emb

    # Configs to evaluate
    configs = [("fp32", 0)]
    if FAST:
        # Headline-only: 6/8/10 bits/pair = 3/4/5 bits/element, the
        # production-relevant zone for KV-cache quant.
        for bits in (6, 8, 10):
            configs.append(("cart", bits))
            configs.append(("polar", bits))
            configs.append(("log_polar", bits))
            configs.append(("log_polar_zf25", bits))
            configs.append(("log_polar_zf50", bits))
            # TurboQuant (fused_turboquant) supports only 2/3/4 b/coord
            # = 4/6/8 b/pair. Skip at 10 b/pair.
            if _TURBOQUANT_AVAILABLE and bits in (6, 8):
                configs.append(("turbo", bits))
        configs.append(("fp4_like", 8))
    else:
        for bits in (6, 8, 10):
            configs.append(("cart", bits))
            configs.append(("polar", bits))
            configs.append(("log_polar", bits))
        configs.append(("fp4_like", 8))
        configs.append(("polar_hyb1pct", 8))
        configs.append(("log_polar_hyb1pct", 8))
        for zf in (0.25, 0.50, 0.75):
            name = f"log_polar_zf{int(zf*100)}"
            for bits in (6, 8, 10):
                configs.append((name, bits))

    results = []
    for q_name, bits in configs:
        q_fn = _make_quantizer(q_name, bits)
        hook = QuantHook(q_fn)
        modeling.apply_rotary_pos_emb = hook.patched_apply(original_apply)
        t_a = time.time()
        ce, n = perplexity_ce(model, input_ids, attention_mask)
        wall = time.time() - t_a
        ce_per_tok = ce / max(n, 1)
        ppl = math.exp(ce_per_tok)
        bpc = ce_per_tok / math.log(2)
        print(f"[tier2] {q_name:>18s} b={bits:>2d}  "
              f"ce={ce_per_tok:.4f}  ppl={ppl:.3f}  bpc={bpc:.4f}  "
              f"wall={wall:.1f}s")
        results.append({
            "quantizer": q_name, "bits": bits,
            "ce_nats": ce_per_tok, "ppl": ppl, "bpc": bpc,
            "n_tokens": n, "wall_s": wall,
        })
        # restore baseline
        modeling.apply_rotary_pos_emb = original_apply

    # Compute deltas vs baseline
    baseline_ce = next(r["ce_nats"] for r in results
                       if r["quantizer"] == "fp32")
    baseline_ppl = math.exp(baseline_ce)
    for r in results:
        r["delta_ce"] = r["ce_nats"] - baseline_ce
        r["delta_ppl"] = r["ppl"] - baseline_ppl
        r["delta_bpc"] = r["bpc"] - baseline_ce / math.log(2)
        r["ppl_ratio"] = r["ppl"] / baseline_ppl

    # CSV
    fields = ["quantizer", "bits", "ce_nats", "bpc", "ppl",
              "delta_ce", "delta_bpc", "delta_ppl", "ppl_ratio",
              "n_tokens", "wall_s"]
    suffix = f".{OUT_TAG}" if OUT_TAG else ""
    with open(HERE / f"tier2_per_config{suffix}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in results:
            w.writerow({f: r.get(f, "") for f in fields})

    # Markdown
    out = []
    out.append("# Tier 2 — End-to-end perplexity with K-cache quantization\n")
    out.append(f"\nModel: `{MODEL_ID}`  ")
    out.append(f"\nEval: {N_SEQS} sequences × {SEQ_LEN} tokens "
               f"({results[0]['n_tokens']} scored tokens)\n")
    out.append(f"\nBaseline FP32 PPL: **{baseline_ppl:.3f}** "
               f"(BPC {baseline_ce/math.log(2):.4f})\n")

    head = ["quantizer", "bits", "PPL", "ΔPPL", "PPL ratio",
            "BPC", "ΔBPC", "wall (s)"]
    out.append("| " + " | ".join(head) + " |")
    out.append("|" + "---|" * len(head))
    for r in sorted(results, key=lambda x: (x["bits"], x["quantizer"])):
        row = [
            r["quantizer"],
            str(r["bits"]) if r["bits"] else "—",
            f"{r['ppl']:.3f}",
            f"{r['delta_ppl']:+.3f}",
            f"{r['ppl_ratio']:.3f}",
            f"{r['bpc']:.4f}",
            f"{r['delta_bpc']:+.4f}",
            f"{r['wall_s']:.1f}",
        ]
        out.append("| " + " | ".join(row) + " |")

    suffix = f".{OUT_TAG}" if OUT_TAG else ""
    out_md = HERE / f"tier2_results{suffix}.md"
    with open(out_md, "w") as fh:
        fh.write("\n".join(out))
    print(f"[tier2] wrote {out_md.name}  ({len(results)} configs)")
    print(f"[tier2] total wall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
