"""Timing-only torch-reference train step for the M6 JVM-port benchmark
(docs/jvm-port-spec.md §10 / docs/jvm-port-bench.md). ADDITIVE tooling —
read-only use of the reference; nothing is dumped or mutated on disk.

Runs the SAME workload the JVM bench (mmllm.jvm.bench-step) times: the
sym24 prod logitkd recipe (STEP_ENV + SCHED_PROD_ENV over SYM24_ENV) on a
16-router effective batch — torch expresses it as one B=16 tensor with
trunk_ids 0..15 — with KD firing every 2nd step (KD_EVERY=2), NetBank
delay 0, PKM C++ kernels off (inert at cpu-mini per CLAUDE.md anyway).

The steps are run by CALLING the core.lpy `train-step` var directly with
the three optimizers built exactly as train-long builds them, i.e. the
whole reference stack incl. Basilisp dispatch — that IS the thing the
port is benchmarked against.

  .venv/bin/python scripts/bench_torch_step.py --T 256 --steps 4
  .venv/bin/python scripts/bench_torch_step.py --T 1024 --steps 4 \
      --grad-checkpoint true    # 15 GB boxes need checkpointing at T=1024

--grad-checkpoint false is the honest apples-to-apples default (the JVM
port never materializes (T,T) for backward, spec §9); true is the prod-CI
memory-fit configuration and pays the ~recompute overhead.
"""
from __future__ import annotations

import argparse
import os
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("MMLLM_DISABLE_PKM_CPP", "true")

from dump_goldens import SCHED_PROD_ENV, STEP_ENV  # noqa: E402
from jvm_bridge import build_model  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--T", type=int, default=256)
    ap.add_argument("--B", type=int, default=16)
    ap.add_argument("--steps", type=int, default=4,
                    help="timed steps (KD fires on every 2nd)")
    ap.add_argument("--warmup", type=int, default=1)
    ap.add_argument("--grad-checkpoint", default="false",
                    choices=["true", "false"])
    ap.add_argument("--threads", type=int, default=0,
                    help="torch.set_num_threads (0 = torch default)")
    args = ap.parse_args()

    for k, v in SCHED_PROD_ENV.items():
        os.environ[k] = v
    for k, v in STEP_ENV.items():
        os.environ[k] = v
    os.environ["MMLLM_GRAD_CHECKPOINT"] = args.grad_checkpoint

    m, K, var = build_model()
    import torch
    if args.threads:
        torch.set_num_threads(args.threads)

    opt_dense = var("make-opt-dense")(m)
    sparse_cls = var("pick-sparse-optimizer")()
    opt_sparse = sparse_cls(list(var("sparse-parameters")(m)),
                            lr=float(var("pick-lr-bank")()))
    opt_sparse_net = sparse_cls(list(var("netbank-sparse-parameters")(m)),
                                lr=float(var("pick-lr-net")()))

    g = torch.Generator().manual_seed(20260704)
    win = torch.randint(0, 256, (args.B, args.T + 1), generator=g)
    x, y = win[:, :args.T].clone(), win[:, 1:].clone()
    trunk_ids = torch.arange(args.B, dtype=torch.long) % 16

    metrics = m.get(K("metrics"))
    metrics["total_steps"] = 100
    train_step = var("train-step")

    print(f"bench: torch {torch.__version__}, {torch.get_num_threads()} "
          f"intra-op threads, B={args.B}, T={args.T}, "
          f"grad_checkpoint={args.grad_checkpoint}, "
          f"{args.warmup} warmup + {args.steps} timed steps (KD every 2)")

    kd_t, nokd_t, total = [], [], 0.0
    for i in range(args.warmup + args.steps):
        step = 10 + i                      # even → KD fires (KD_EVERY=2)
        metrics["current_step"] = step
        t0 = time.perf_counter()
        train_step(m, opt_dense, opt_sparse, opt_sparse_net, x, y, False,
                   trunk_ids)
        dt = time.perf_counter() - t0
        kd = step % 2 == 0
        tag = " (warmup)" if i < args.warmup else ""
        print(f"   step {i} kd={kd}: {dt:.2f}s{tag}", flush=True)
        if i >= args.warmup:
            (kd_t if kd else nokd_t).append(dt)
            total += dt

    print(f"total {total:.1f}s over {args.steps} steps -> "
          f"{args.steps / total:.4f} steps/s")
    if kd_t:
        print(f"median kd step     {statistics.median(kd_t):.2f}s")
    if nokd_t:
        print(f"median non-kd step {statistics.median(nokd_t):.2f}s")


if __name__ == "__main__":
    main()
