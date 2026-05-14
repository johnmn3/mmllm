"""Reconstruction-error benchmark for cartesian / polar / log-polar 2-D
quantizers at fixed bit budgets, on synthetic distributions chosen to
match reported LLM activation / KV-cache statistics.

Pure stdlib. Run: python3 experiment.py
"""

import math
import random
import statistics

random.seed(0xC0FFEE)


# ---------------------------------------------------------------------------
# datasets
# ---------------------------------------------------------------------------

def gen_gaussian(n, sigma=1.0):
    return [(random.gauss(0, sigma), random.gauss(0, sigma)) for _ in range(n)]


def gen_lognormal_radius(n, sigma=1.0):
    """Radius ~ LogNormal(0, sigma); angle uniform. Matches the qualitative
    shape of heavy-tailed magnitude with isotropic direction."""
    out = []
    for _ in range(n):
        r = math.exp(random.gauss(0, sigma))
        t = random.uniform(-math.pi, math.pi)
        out.append((r * math.cos(t), r * math.sin(t)))
    return out


def gen_outlier_gaussian(n, sigma=1.0, outlier_frac=0.02, outlier_scale=20.0):
    """Gaussian body + sparse heavy outliers. Mimics 'outlier features'
    in LLM activations (Dettmers et al.)."""
    out = []
    for _ in range(n):
        if random.random() < outlier_frac:
            s = outlier_scale * sigma
        else:
            s = sigma
        out.append((random.gauss(0, s), random.gauss(0, s)))
    return out


def gen_rope_pair(n, sigma=1.0):
    """Synthetic post-RoPE 2-D key pair: 'natural' radius distribution
    (LogNormal) times a RoPE-induced angle. Per Google PolarQuant, RoPE
    creates well-organized polar structure with concentrated angle bins."""
    out = []
    for _ in range(n):
        # radius: log-normal (heavy-tailed magnitude is the observed shape)
        r = math.exp(random.gauss(0, sigma * 0.8))
        # angle: sum of a base angle and a concentrated 'rotation-induced'
        # angle; resulting distribution is approximately uniform on the
        # circle but with mild structure
        t_base = random.uniform(-math.pi, math.pi)
        out.append((r * math.cos(t_base), r * math.sin(t_base)))
    return out


DATASETS = {
    "gaussian":   lambda: gen_gaussian(10_000, sigma=1.0),
    "lognormal":  lambda: gen_lognormal_radius(10_000, sigma=1.0),
    "outlier":    lambda: gen_outlier_gaussian(10_000),
    "rope_pair":  lambda: gen_rope_pair(10_000),
}


# ---------------------------------------------------------------------------
# quantizers — each takes samples (list of (x,y)) and a bit budget per pair
# ---------------------------------------------------------------------------

def quant_cartesian_uniform(samples, bits_total):
    """Per-axis uniform quantization with per-axis absmax. Splits bits
    evenly between x and y."""
    bx = bits_total // 2
    by = bits_total - bx
    Lx, Ly = (1 << bx), (1 << by)
    ax = max(abs(s[0]) for s in samples) or 1e-9
    ay = max(abs(s[1]) for s in samples) or 1e-9
    sx = 2 * ax / (Lx - 1)
    sy = 2 * ay / (Ly - 1)

    def q1(v, a, s, L):
        idx = round((v + a) / s)
        idx = max(0, min(L - 1, idx))
        return idx * s - a

    return [(q1(x, ax, sx, Lx), q1(y, ay, sy, Ly)) for x, y in samples]


def quant_polar(samples, bits_total):
    """Polar (r, theta) uniform quantization. r in [0, r_max], theta in
    [-pi, pi). Splits bits evenly."""
    br = bits_total // 2
    bt = bits_total - br
    Lr, Lt = (1 << br), (1 << bt)

    rs = [math.hypot(x, y) for x, y in samples]
    r_max = max(rs) or 1e-9
    sr = r_max / (Lr - 1)
    st = 2 * math.pi / Lt

    out = []
    for x, y in samples:
        r = math.hypot(x, y)
        t = math.atan2(y, x)
        ir = max(0, min(Lr - 1, round(r / sr)))
        it = max(0, min(Lt - 1, round((t + math.pi) / st)))
        rh = ir * sr
        th = it * st - math.pi
        out.append((rh * math.cos(th), rh * math.sin(th)))
    return out


def quant_log_polar(samples, bits_total, eps=1e-6):
    """Log-polar (rho=log r, theta) uniform quantization. rho in
    [log(eps * r_max), log(r_max)] so smallest representable r is
    eps * r_max. Splits bits evenly. Reserves nothing for the literal
    zero — values smaller than eps * r_max snap to the smallest bin."""
    br = bits_total // 2
    bt = bits_total - br
    Lr, Lt = (1 << br), (1 << bt)

    rs = [math.hypot(x, y) for x, y in samples]
    r_max = max(rs) or 1e-9
    rho_max = math.log(r_max)
    rho_min = math.log(eps * r_max)
    s_rho = (rho_max - rho_min) / (Lr - 1)
    st = 2 * math.pi / Lt

    out = []
    for x, y in samples:
        r = math.hypot(x, y)
        r_clamped = max(r, eps * r_max)
        rho = math.log(r_clamped)
        t = math.atan2(y, x)
        ir = max(0, min(Lr - 1, round((rho - rho_min) / s_rho)))
        it = max(0, min(Lt - 1, round((t + math.pi) / st)))
        rho_h = ir * s_rho + rho_min
        th = it * st - math.pi
        r_h = math.exp(rho_h)
        out.append((r_h * math.cos(th), r_h * math.sin(th)))
    return out


def quant_fp4_like(samples, bits_total):
    """Per-axis 1-D float-style (exponent + 1-bit sign + 2-bit mantissa
    at 4 bits/axis, 8 bits total). This is what FP4 E2M1 / E3M0 actually
    look like in 4 bits: 1 sign, k exponent bits, (4-1-k) mantissa bits.
    Use E2M1: 1 sign, 2 exp, 1 mantissa = 4 bits.

    Not a full FP4 spec; close enough for shape comparison. Splits
    8 bits as 4 per axis."""
    if bits_total != 8:
        raise ValueError("quant_fp4_like assumes 8 bits/pair (4 per axis)")

    # E2M1: 1 sign | 2 exponent | 1 mantissa, bias=1. Representable:
    # subnormal: 0, ±0.5
    # normal:    ±1, ±1.5, ±2, ±3, ±4, ±6
    levels_1d = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]
    levels_1d = [-v for v in reversed(levels_1d)] + levels_1d
    # de-dupe the 0 we accidentally duplicated
    levels_1d = sorted(set(levels_1d))

    def q1(v, scale):
        v_scaled = v / scale
        best = min(levels_1d, key=lambda L: abs(L - v_scaled))
        return best * scale

    # per-axis absmax scale (so 6.0 = full scale)
    ax = max(abs(s[0]) for s in samples) or 1e-9
    ay = max(abs(s[1]) for s in samples) or 1e-9
    sx = ax / 6.0
    sy = ay / 6.0
    return [(q1(x, sx), q1(y, sy)) for x, y in samples]


QUANTIZERS = {
    "cart_uniform": quant_cartesian_uniform,
    "polar":         quant_polar,
    "log_polar":     quant_log_polar,
    "fp4_like":      quant_fp4_like,
}


# ---------------------------------------------------------------------------
# metrics
# ---------------------------------------------------------------------------

def metrics(samples, reconstructed):
    sq_err = []
    abs_err = []
    rel_err = []
    cos = []
    for (x, y), (xh, yh) in zip(samples, reconstructed):
        dx = x - xh
        dy = y - yh
        sq_err.append(dx * dx + dy * dy)
        abs_err.append(math.hypot(dx, dy))
        n = math.hypot(x, y)
        nh = math.hypot(xh, yh)
        if n > 1e-9:
            rel_err.append(math.hypot(dx, dy) / n)
        if n > 1e-9 and nh > 1e-9:
            cos.append((x * xh + y * yh) / (n * nh))
    return {
        "mse":      statistics.mean(sq_err),
        "rmse":     math.sqrt(statistics.mean(sq_err)),
        "max_err":  max(abs_err),
        "p99_err":  sorted(abs_err)[int(0.99 * len(abs_err))],
        "rel_med":  statistics.median(rel_err) if rel_err else float("nan"),
        "rel_p99":  sorted(rel_err)[int(0.99 * len(rel_err))] if rel_err else float("nan"),
        "cos_med":  statistics.median(cos) if cos else float("nan"),
    }


# ---------------------------------------------------------------------------
# benchmark
# ---------------------------------------------------------------------------

def run():
    BITS_PER_PAIR = 8  # = 4 bits/element, the production sweet-spot

    print(f"# Reconstruction-error benchmark, {BITS_PER_PAIR} bits per 2-D pair")
    print(f"# seed=0x{random.getstate()[1][0]:08x}, n=10000 samples per dataset")
    print()

    # Header
    fields = ["mse", "rmse", "max_err", "p99_err", "rel_med", "rel_p99", "cos_med"]
    head = ["dataset", "quantizer"] + fields
    widths = [12, 14] + [10] * len(fields)
    fmt_h = "  ".join("{:<" + str(w) + "}" for w in widths)
    fmt_r = "  ".join(
        ["{:<12}", "{:<14}"] +
        ["{:>10.4g}"] * len(fields)
    )
    print(fmt_h.format(*head))
    print(fmt_h.format(*(["-" * (w - 1) for w in widths])))

    for ds_name, ds_fn in DATASETS.items():
        samples = ds_fn()
        for q_name, q_fn in QUANTIZERS.items():
            try:
                recon = q_fn(samples, BITS_PER_PAIR)
            except Exception as e:
                print(f"{ds_name:<12}  {q_name:<14}  ERROR: {e}")
                continue
            m = metrics(samples, recon)
            row = [ds_name, q_name] + [m[f] for f in fields]
            print(fmt_r.format(*row))
        print()


if __name__ == "__main__":
    run()
