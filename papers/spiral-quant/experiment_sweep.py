"""Ablation sweeps for the spiral-quant paper:

  1. bit budget sweep at 4..12 bits/pair (even split)
  2. asymmetric (rho:theta) bit split sweep at 8 bits/pair
  3. multiple seeds for noise bars

Pure stdlib.
"""

import math
import random
import statistics

from experiment import (
    gen_gaussian, gen_lognormal_radius, gen_outlier_gaussian, gen_rope_pair,
    quant_cartesian_uniform, quant_polar, quant_log_polar, quant_fp4_like,
    metrics,
)


DATASETS = {
    "gaussian":  lambda: gen_gaussian(5_000),
    "lognormal": lambda: gen_lognormal_radius(5_000),
    "outlier":   lambda: gen_outlier_gaussian(5_000),
    "rope_pair": lambda: gen_rope_pair(5_000),
}


def quant_polar_split(samples, br, bt):
    """Polar quantization with explicit (radius_bits, theta_bits) split."""
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


def quant_log_polar_split(samples, br, bt, eps=1e-6):
    """Log-polar with explicit (rho_bits, theta_bits) split."""
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


def mean_std(xs):
    return statistics.mean(xs), statistics.stdev(xs) if len(xs) > 1 else 0.0


# ----- sweep 1: bit budget --------------------------------------------------

def sweep_bit_budget(seeds=(1, 2, 3)):
    print("=" * 72)
    print("SWEEP 1: bit budget at even split, mean ± stdev MSE across 3 seeds")
    print("=" * 72)
    print()
    budgets = [4, 6, 8, 10, 12]
    header = f"{'dataset':<12} {'quant':<14} " + " ".join(f"{b:>9}b" for b in budgets)
    print(header)
    print("-" * len(header))

    for ds_name, ds_fn in DATASETS.items():
        for q_name in ("cart_uniform", "polar", "log_polar"):
            row = [f"{ds_name:<12}", f"{q_name:<14}"]
            for b in budgets:
                mses = []
                for s in seeds:
                    random.seed(s)
                    samples = ds_fn()
                    if q_name == "cart_uniform":
                        recon = quant_cartesian_uniform(samples, b)
                    elif q_name == "polar":
                        recon = quant_polar(samples, b)
                    else:
                        recon = quant_log_polar(samples, b)
                    mses.append(metrics(samples, recon)["mse"])
                m, sd = mean_std(mses)
                row.append(f"{m:9.3g}")
            print(" ".join(row))
        print()


# ----- sweep 2: asymmetric bit split at 8 bits/pair -------------------------

def sweep_bit_split():
    print("=" * 72)
    print("SWEEP 2: rho:theta split at fixed 8 bits/pair (seed=1)")
    print("=" * 72)
    print()
    splits = [(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)]
    header = f"{'dataset':<12} {'quant':<10} " + " ".join(
        f"{br}r:{bt}t".rjust(10) for br, bt in splits
    )
    print(header)
    print("-" * len(header))
    for ds_name, ds_fn in DATASETS.items():
        for q_name in ("polar", "log_polar"):
            row = [f"{ds_name:<12}", f"{q_name:<10}"]
            for br, bt in splits:
                random.seed(1)
                samples = ds_fn()
                if q_name == "polar":
                    recon = quant_polar_split(samples, br, bt)
                else:
                    recon = quant_log_polar_split(samples, br, bt)
                row.append(f"{metrics(samples, recon)['mse']:10.4g}")
            print(" ".join(row))
        print()


# ----- sweep 3: same sweep on RELATIVE error --------------------------------

def sweep_relative_error():
    print("=" * 72)
    print("SWEEP 3: median relative error at 8 bits/pair, even split, 3 seeds")
    print("=" * 72)
    print()
    header = f"{'dataset':<12} " + " ".join(
        q.rjust(14) for q in ("cart_uniform", "polar", "log_polar", "fp4_like")
    )
    print(header)
    print("-" * len(header))
    for ds_name, ds_fn in DATASETS.items():
        row = [f"{ds_name:<12}"]
        for q_name in ("cart_uniform", "polar", "log_polar", "fp4_like"):
            rels = []
            for s in (1, 2, 3):
                random.seed(s)
                samples = ds_fn()
                if q_name == "cart_uniform":
                    recon = quant_cartesian_uniform(samples, 8)
                elif q_name == "polar":
                    recon = quant_polar(samples, 8)
                elif q_name == "log_polar":
                    recon = quant_log_polar(samples, 8)
                else:
                    recon = quant_fp4_like(samples, 8)
                rels.append(metrics(samples, recon)["rel_med"])
            m, sd = mean_std(rels)
            row.append(f"{m:>10.4g}±{sd:.2g}".rjust(14))
        print(" ".join(row))
    print()


# ----- sweep 4: angular preservation (cosine sim) ---------------------------

def sweep_cosine():
    print("=" * 72)
    print("SWEEP 4: median cosine similarity at 8 bits/pair, even split, 3 seeds")
    print("=" * 72)
    print()
    header = f"{'dataset':<12} " + " ".join(
        q.rjust(14) for q in ("cart_uniform", "polar", "log_polar", "fp4_like")
    )
    print(header)
    print("-" * len(header))
    for ds_name, ds_fn in DATASETS.items():
        row = [f"{ds_name:<12}"]
        for q_name in ("cart_uniform", "polar", "log_polar", "fp4_like"):
            cs = []
            for s in (1, 2, 3):
                random.seed(s)
                samples = ds_fn()
                if q_name == "cart_uniform":
                    recon = quant_cartesian_uniform(samples, 8)
                elif q_name == "polar":
                    recon = quant_polar(samples, 8)
                elif q_name == "log_polar":
                    recon = quant_log_polar(samples, 8)
                else:
                    recon = quant_fp4_like(samples, 8)
                cs.append(metrics(samples, recon)["cos_med"])
            m, sd = mean_std(cs)
            row.append(f"{m:>10.4g}±{sd:.2g}".rjust(14))
        print(" ".join(row))
    print()


if __name__ == "__main__":
    sweep_bit_budget()
    sweep_bit_split()
    sweep_relative_error()
    sweep_cosine()
