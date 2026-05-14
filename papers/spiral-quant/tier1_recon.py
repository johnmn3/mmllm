"""Tier 1 — Reconstruction-error benchmark on real post-RoPE K tensors.

Reads the dump produced by tier0_precheck.py and applies the four
quantizers from the paper (cart_uniform, polar, log_polar, fp4_like)
plus a dense-and-sparse hybrid variant for log_polar and polar, at
bit budgets {6, 8, 10}. Measures per-layer and aggregate metrics.

Outputs:
  - tier1_results.md  : structured results in markdown
  - tier1_per_layer.csv : per-layer raw numbers for the paper
"""

import csv
import math
import statistics
import time
from pathlib import Path

import torch

HERE = Path(__file__).resolve().parent
DUMPS = HERE / "dumps"


# ---------------------------------------------------------------------------
# torch-vectorized quantizers — input shape (..., D) with D even
# ---------------------------------------------------------------------------

def _split_pairs(t: torch.Tensor):
    """HF Llama-style RoPE is *blocked*: dims [0..D/2) rotate together with
    dims [D/2..D). Pair k is (dim_k, dim_{k+D/2}).
    Returns (x, y) each shape (..., D/2)."""
    half = t.shape[-1] // 2
    return t[..., :half], t[..., half:]


def _join_pairs(x, y):
    return torch.cat([x, y], dim=-1)


def quant_cart_uniform_t(t: torch.Tensor, bits_total: int) -> torch.Tensor:
    orig_dtype = t.dtype
    t = t.float()  # upcast: fp16 squares overflow at |v|>~255
    bx = bits_total // 2
    by = bits_total - bx
    Lx, Ly = (1 << bx), (1 << by)
    x, y = _split_pairs(t)
    ax = max(x.abs().max().item(), 1e-9)
    ay = max(y.abs().max().item(), 1e-9)
    sx = 2 * ax / (Lx - 1)
    sy = 2 * ay / (Ly - 1)
    xh = ((x + ax) / sx).round().clamp(0, Lx - 1) * sx - ax
    yh = ((y + ay) / sy).round().clamp(0, Ly - 1) * sy - ay
    return _join_pairs(xh, yh).to(orig_dtype)


def quant_polar_t(t: torch.Tensor, bits_total: int) -> torch.Tensor:
    orig_dtype = t.dtype
    t = t.float()  # upcast for sqrt(x^2+y^2) safety
    br = bits_total // 2
    bt = bits_total - br
    Lr, Lt = (1 << br), (1 << bt)
    x, y = _split_pairs(t)
    r = (x * x + y * y).sqrt()
    theta = torch.atan2(y, x)
    r_max = max(r.max().item(), 1e-9)
    sr = r_max / (Lr - 1)
    st = 2 * math.pi / Lt
    ir = (r / sr).round().clamp(0, Lr - 1)
    it = ((theta + math.pi) / st).round().clamp(0, Lt - 1)
    rh = ir * sr
    th = it * st - math.pi
    return _join_pairs(rh * torch.cos(th), rh * torch.sin(th)).to(orig_dtype)


def quant_log_polar_t(t: torch.Tensor, bits_total: int, eps: float = 1e-6) -> torch.Tensor:
    orig_dtype = t.dtype
    t = t.float()
    br = bits_total // 2
    bt = bits_total - br
    Lr, Lt = (1 << br), (1 << bt)
    x, y = _split_pairs(t)
    r = (x * x + y * y).sqrt()
    theta = torch.atan2(y, x)
    r_max = max(r.max().item(), 1e-9)
    rho_max = math.log(r_max)
    rho_min = math.log(eps * r_max)
    r_clamped = r.clamp(min=eps * r_max)
    rho = r_clamped.log()
    s_rho = (rho_max - rho_min) / (Lr - 1)
    st = 2 * math.pi / Lt
    ir = ((rho - rho_min) / s_rho).round().clamp(0, Lr - 1)
    it = ((theta + math.pi) / st).round().clamp(0, Lt - 1)
    rho_h = ir * s_rho + rho_min
    th = it * st - math.pi
    r_h = rho_h.exp()
    return _join_pairs(r_h * torch.cos(th), r_h * torch.sin(th)).to(orig_dtype)


# FP4 (E2M1) levels per axis at 4 bits, with absmax scaling.
FP4_LEVELS = torch.tensor([
    -6.0, -4.0, -3.0, -2.0, -1.5, -1.0, -0.5,
     0.0,
     0.5,  1.0,  1.5,  2.0,  3.0,  4.0,  6.0,
])

# TurboQuant: use the community open-source implementation (fused_turboquant)
# which uses Randomized Hadamard Transform per the ICLR 2026 paper.
# Per-(head_dim, bits) instance is cached to avoid re-initializing the
# random rotation matrix per call.
try:
    from fused_turboquant import TurboQuantMSE
    _TURBOQUANT_AVAILABLE = True
except ImportError:
    _TURBOQUANT_AVAILABLE = False

_turbo_cache: dict = {}


def quant_turbo_t(t: torch.Tensor, bits_total: int) -> torch.Tensor:
    """TurboQuant KV-cache quantization (Zandieh et al., ICLR 2026).

    Uses the open-source `fused_turboquant` implementation which applies
    a Randomized Hadamard Transform (D @ H, where D is a random ±1 diagonal
    and H is Walsh-Hadamard) to per-token K vectors, then uniform-quantizes
    each rotated coordinate, then inverse-rotates.

    bits_total is bits per pair to match the rest of the harness;
    per-coordinate bits = bits_total // 2."""
    if not _TURBOQUANT_AVAILABLE:
        raise RuntimeError("fused_turboquant package not installed")
    orig_dtype = t.dtype
    t32 = t.float()
    head_dim = t32.shape[-1]
    bits = bits_total // 2
    key = (head_dim, bits)
    if key not in _turbo_cache:
        _turbo_cache[key] = TurboQuantMSE(
            head_dim=head_dim, bits=bits, device="cpu",
        )
    tq = _turbo_cache[key]
    compressed = tq.encode(t32)
    decoded = tq.decode(compressed)
    return decoded.to(orig_dtype)


def quant_fp4_like_t(t: torch.Tensor, bits_total: int = 8) -> torch.Tensor:
    if bits_total != 8:
        raise ValueError("fp4_like assumes 8 bits/pair (4 per axis)")
    orig_dtype = t.dtype
    t = t.float()
    x, y = _split_pairs(t)
    ax = max(x.abs().max().item(), 1e-9)
    ay = max(y.abs().max().item(), 1e-9)
    sx = ax / 6.0
    sy = ay / 6.0
    levels = FP4_LEVELS.to(t.device, t.dtype)
    def snap(v, scale):
        v_scaled = v / scale
        diff = (v_scaled.unsqueeze(-1) - levels).abs()
        idx = diff.argmin(dim=-1)
        return levels[idx] * scale
    return _join_pairs(snap(x, sx), snap(y, sy)).to(orig_dtype)


def quant_log_polar_hybrid_t(t: torch.Tensor, bits_total: int,
                              sparse_frac: float = 0.01) -> torch.Tensor:
    orig_dtype = t.dtype
    t = t.float()
    x, y = _split_pairs(t)
    r = (x * x + y * y).sqrt()
    # threshold on the GLOBAL r distribution to keep top sparse_frac
    if sparse_frac > 0 and r.numel() > 0:
        k = max(1, int(sparse_frac * r.numel()))
        thresh = r.flatten().topk(k).values.min()
        mask = (r >= thresh).unsqueeze(-1).expand(*r.shape, 1)
    else:
        mask = torch.zeros(*r.shape, 1, dtype=torch.bool)

    quantized = quant_log_polar_t(t, bits_total)
    full = t.clone()
    # Where mask is True, keep FP value; else use quantized.
    # mask is on r (one bool per pair); apply to both halves.
    half = t.shape[-1] // 2
    mask_full = torch.cat([mask, mask], dim=-1).squeeze(-2) if mask.dim() > t.dim() else mask
    # easier: rebuild
    x_q, y_q = _split_pairs(quantized)
    mask2 = mask.squeeze(-1) if mask.dim() > r.dim() else mask  # bool of shape r
    x_out = torch.where(mask2, x, x_q)
    y_out = torch.where(mask2, y, y_q)
    return _join_pairs(x_out, y_out).to(orig_dtype)


def quant_log_polar_zerofloor_t(t: torch.Tensor, bits_total: int,
                                  zero_frac: float = 0.5,
                                  eps: float = 1e-3) -> torch.Tensor:
    orig_dtype = t.dtype
    t = t.float()
    """LPQ with a 'snap-to-exact-zero' code for the smallest magnitudes.
    Reserves one of the 2^br ρ-codes for r=0, snaps the bottom `zero_frac`
    of values to it. The remaining (2^br - 1) codes span (eps*r_max, r_max)
    in log-spaced bins.

    Motivation: attention dot products are forgiving of zero K but sensitive
    to multiplicative noise on small K. Plain LPQ amplifies tiny values to
    eps*r_max via the log-quantizer floor, which adds spurious score mass."""
    br = bits_total // 2
    bt = bits_total - br
    Lr, Lt = (1 << br), (1 << bt)
    # one ρ-code is reserved for zero; (Lr - 1) codes left for log range
    Lr_eff = max(Lr - 1, 1)
    x, y = _split_pairs(t)
    r = (x * x + y * y).sqrt()
    theta = torch.atan2(y, x)
    r_max = max(r.max().item(), 1e-9)
    # threshold below which we snap to zero (per-tensor, by quantile)
    if zero_frac > 0 and r.numel() > 0:
        flat = r.flatten()
        k = max(1, int(zero_frac * flat.numel()))
        thresh = flat.kthvalue(k).values.item()
    else:
        thresh = 0.0
    rho_max = math.log(r_max)
    rho_min = math.log(max(thresh, eps * r_max))
    r_clamped = r.clamp(min=math.exp(rho_min))
    rho = r_clamped.log()
    s_rho = (rho_max - rho_min) / max(Lr_eff - 1, 1)
    st = 2 * math.pi / Lt
    ir = ((rho - rho_min) / s_rho).round().clamp(0, Lr_eff - 1)
    it = ((theta + math.pi) / st).round().clamp(0, Lt - 1)
    rho_h = ir * s_rho + rho_min
    th = it * st - math.pi
    r_h = rho_h.exp()
    # snap-to-zero mask
    zero_mask = r < thresh
    x_h = torch.where(zero_mask, torch.zeros_like(x), r_h * torch.cos(th))
    y_h = torch.where(zero_mask, torch.zeros_like(y), r_h * torch.sin(th))
    return _join_pairs(x_h, y_h).to(orig_dtype)


def quant_polar_hybrid_t(t, bits_total, sparse_frac=0.01):
    orig_dtype = t.dtype
    t = t.float()
    x, y = _split_pairs(t)
    r = (x * x + y * y).sqrt()
    if sparse_frac > 0 and r.numel() > 0:
        k = max(1, int(sparse_frac * r.numel()))
        thresh = r.flatten().topk(k).values.min()
        mask2 = r >= thresh
    else:
        mask2 = torch.zeros_like(r, dtype=torch.bool)
    quantized = quant_polar_t(t, bits_total)
    x_q, y_q = _split_pairs(quantized)
    x_out = torch.where(mask2, x, x_q)
    y_out = torch.where(mask2, y, y_q)
    return _join_pairs(x_out, y_out).to(orig_dtype)


QUANTIZERS_BY_BITS = {
    6:  {"cart": quant_cart_uniform_t,    "polar": quant_polar_t,       "log_polar": quant_log_polar_t},
    8:  {"cart": quant_cart_uniform_t,    "polar": quant_polar_t,       "log_polar": quant_log_polar_t,
         "fp4_like": quant_fp4_like_t,
         "log_polar_hyb1pct":  lambda t, b: quant_log_polar_hybrid_t(t, b, 0.01),
         "polar_hyb1pct":      lambda t, b: quant_polar_hybrid_t(t, b, 0.01),
         "log_polar_hyb01pct": lambda t, b: quant_log_polar_hybrid_t(t, b, 0.001),
         },
    10: {"cart": quant_cart_uniform_t,    "polar": quant_polar_t,       "log_polar": quant_log_polar_t},
}


# ---------------------------------------------------------------------------
# metrics
# ---------------------------------------------------------------------------

def metrics_t(orig: torch.Tensor, recon: torch.Tensor) -> dict:
    """Pair-level metrics. Reduces to scalar values over all 2-D pairs."""
    x, y = _split_pairs(orig)
    xh, yh = _split_pairs(recon)
    dx = x - xh
    dy = y - yh
    sq = (dx * dx + dy * dy).flatten()
    err = sq.sqrt()
    n = (x * x + y * y).sqrt().flatten()
    nh = (xh * xh + yh * yh).sqrt().flatten()
    eps = 1e-9
    nz = n > eps
    rel = (err[nz] / n[nz])
    cos_num = (x * xh + y * yh).flatten()
    cos_den = (n * nh)
    cos = cos_num[nz] / (cos_den[nz].clamp(min=eps))

    def pct(t, p):
        if t.numel() == 0:
            return float("nan")
        s, _ = t.sort()
        i = max(0, min(t.numel() - 1, int(p * t.numel())))
        return float(s[i])

    return {
        "mse":      float(sq.mean()),
        "rmse":     float(sq.mean().sqrt()),
        "max_err":  float(err.max()),
        "p99_err":  pct(err, 0.99),
        "p999_err": pct(err, 0.999),
        "rel_med":  pct(rel, 0.50),
        "rel_p95":  pct(rel, 0.95),
        "rel_p99":  pct(rel, 0.99),
        "cos_med":  pct(cos, 0.50),
        "cos_p01":  pct(cos, 0.01),
        "n_pairs":  int(sq.numel()),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print("[tier1] loading dumps/k_post_rope.pt ...")
    dump = torch.load(DUMPS / "k_post_rope.pt", weights_only=False)
    k_per_layer = dump["k_per_layer"]
    n_layers = len(k_per_layer)
    print(f"[tier1] {n_layers} layers, K[0] shape = {tuple(k_per_layer[0].shape)}")

    # All-layers pooled tensor for aggregate metrics
    all_k = torch.cat([kt.reshape(-1, kt.shape[-1]) for kt in k_per_layer], dim=0)
    print(f"[tier1] pooled tensor shape = {tuple(all_k.shape)}")

    # Run sweep
    results = []  # list of dicts
    csv_rows = []
    for bits in sorted(QUANTIZERS_BY_BITS):
        for q_name, q_fn in QUANTIZERS_BY_BITS[bits].items():
            print(f"[tier1] bits={bits} q={q_name} ... ", end="", flush=True)
            t_a = time.time()
            # Aggregate
            recon = q_fn(all_k, bits)
            m_agg = metrics_t(all_k, recon)
            m_agg["bits"] = bits
            m_agg["quantizer"] = q_name
            m_agg["layer"] = "ALL"
            results.append(m_agg)
            csv_rows.append(m_agg)
            # Per-layer
            for li, kt in enumerate(k_per_layer):
                rec = q_fn(kt, bits)
                m = metrics_t(kt, rec)
                m["bits"] = bits
                m["quantizer"] = q_name
                m["layer"] = li
                csv_rows.append(m)
            print(f"{time.time()-t_a:.1f}s")

    # CSV dump
    fields = ["bits", "quantizer", "layer",
              "mse", "rmse", "max_err", "p99_err", "p999_err",
              "rel_med", "rel_p95", "rel_p99",
              "cos_med", "cos_p01", "n_pairs"]
    with open(HERE / "tier1_per_layer.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in csv_rows:
            w.writerow({f: r.get(f, "") for f in fields})
    print(f"[tier1] wrote tier1_per_layer.csv ({len(csv_rows)} rows)")

    # Markdown summary
    out = []
    out.append("# Tier 1 — Reconstruction error on real K (post-RoPE)\n")
    out.append(f"\nSource dump: `{dump['model_id']}`, "
               f"N={dump['n_seqs']}×{dump['seq_len']}, {n_layers} layers.\n")

    out.append("\n## Aggregate metrics (all layers pooled)\n")
    head = ["bits", "quantizer", "mse", "rmse", "p99_err", "p999_err",
            "rel_med", "rel_p99", "cos_med", "cos_p01"]
    out.append("| " + " | ".join(head) + " |")
    out.append("|" + "---|" * len(head))
    for r in results:
        row = []
        for f in head:
            v = r[f]
            if isinstance(v, float):
                row.append(f"{v:.4g}")
            else:
                row.append(str(v))
        out.append("| " + " | ".join(row) + " |")

    # Cross-layer summary — for each (bits, q), give median/min/max MSE across layers
    out.append("\n## Per-layer summary: MSE (median / min / max across 30 layers)\n")
    layer_rows = [r for r in csv_rows if r["layer"] != "ALL"]
    by_key = {}
    for r in layer_rows:
        key = (r["bits"], r["quantizer"])
        by_key.setdefault(key, []).append(r["mse"])
    head2 = ["bits", "quantizer", "mse_median", "mse_min", "mse_max"]
    out.append("| " + " | ".join(head2) + " |")
    out.append("|" + "---|" * len(head2))
    for key in sorted(by_key, key=lambda k: (k[0], k[1])):
        vs = by_key[key]
        out.append(f"| {key[0]} | {key[1]} | "
                   f"{statistics.median(vs):.4g} | {min(vs):.4g} | {max(vs):.4g} |")

    # Same for rel_med — the headline LPQ property
    out.append("\n## Per-layer summary: rel_med (median / min / max across 30 layers)\n")
    by_key = {}
    for r in layer_rows:
        key = (r["bits"], r["quantizer"])
        by_key.setdefault(key, []).append(r["rel_med"])
    out.append("| " + " | ".join(head2).replace("mse", "rel_med") + " |")
    out.append("|" + "---|" * len(head2))
    for key in sorted(by_key, key=lambda k: (k[0], k[1])):
        vs = by_key[key]
        out.append(f"| {key[0]} | {key[1]} | "
                   f"{statistics.median(vs):.4g} | {min(vs):.4g} | {max(vs):.4g} |")

    out.append("\n## Per-layer summary: cos_med (median / min / max across 30 layers)\n")
    by_key = {}
    for r in layer_rows:
        key = (r["bits"], r["quantizer"])
        by_key.setdefault(key, []).append(r["cos_med"])
    out.append("| " + " | ".join(head2).replace("mse", "cos_med") + " |")
    out.append("|" + "---|" * len(head2))
    for key in sorted(by_key, key=lambda k: (k[0], k[1])):
        vs = by_key[key]
        out.append(f"| {key[0]} | {key[1]} | "
                   f"{statistics.median(vs):.4g} | {min(vs):.4g} | {max(vs):.4g} |")

    with open(HERE / "tier1_results.md", "w") as fh:
        fh.write("\n".join(out))
    print(f"[tier1] wrote tier1_results.md")
    print(f"[tier1] total wall: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
