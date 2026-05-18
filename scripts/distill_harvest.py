"""Distillation harvest — teacher-ensemble → student NetBank.

The naive FedAvg harvester (`mmllm.harvester`) averages NetBank V row-by-row,
which fails when workers learned different *bases* (different K_a/K_b
trajectories landed the same patterns at different physical row indices).
Empirically: across 5 round-6 workers, layer-{1,2,3} merged V norm ≈
avg_individual / √5 — pure uncorrelated-vector cancellation.

This script distills the teacher *ensemble's output* into a fresh student
NetBank. The student picks its own internal basis to reproduce the average
of teachers' net_outs at the SAME queries. No row-by-row alignment needed.

Pipeline:
  1. Pull each worker's NetBank state (K_a/K_b/expander from dense.pt at
     positional indices, V from bank-net-latest.<i>.fp16.bin).
  2. Build per-layer teacher NetBanks (5 × 4 = 20 frozen instances).
  3. Build per-layer student NetBanks (4 trainable instances) initialized
     to zero.
  4. Generate query batches (Gaussian, scaled to typical q_long magnitude).
  5. For each batch:
       - For each layer:
           target = mean_i NB_teacher_i(q[layer])      # frozen, no grad
           pred   = NB_student(q[layer])
           loss   += MSE(pred, target)
       - Backward; SparseAdam on student V (+ AdamW on K_a/K_b/expander).
  6. Write the distilled NetBank V to <output>/bank-net-latest.<i>.fp16.bin
     and the (slightly-shifted) K_a/K_b/expander back into a refined
     dense.pt for an end-to-end-evaluable output.

Why per-layer independent NetBanks: each layer's NetBank is parameterized
separately (own K_a/K_b/expander/V), so distillation factorizes across
layers exactly. We don't need a full model forward, just NetBank forwards.

This is round-6's harvest. Round-7 can iterate (trunk distillation, real
query distribution from corpus, multi-teacher full-model distillation).
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

# Suppress NetBank's 1-10ms simulated network delay during distillation;
# we don't need WAN realism here, just the function.
os.environ.setdefault("MMLLM_NET_DELAY_MS_MIN", "0.0")
os.environ.setdefault("MMLLM_NET_DELAY_MS_MAX", "0.0")
os.environ.setdefault("MMLLM_NUM_THREADS", "4")

import numpy as np
import torch
import torch.nn.functional as F

from mmllm.netbank import NetBank


# Tensor indices in dense.pt for per-layer NetBank dense params.
# Derived from `parameters` in core.lpy (NetBank dense at the END, after
# tok-emb, per-block core×4, norm-final, memory-q-norm×4, gate-params×8).
# For cpu-tiny default (4 layers, 4 params per NetBank layer):
#   block 0: K_a=66, K_b=67, q_norm.w=68, expander.w=69
#   block 1: K_a=70, K_b=71, q_norm.w=72, expander.w=73
#   block 2: K_a=74, K_b=75, q_norm.w=76, expander.w=77
#   block 3: K_a=78, K_b=79, q_norm.w=80, expander.w=81
NETBANK_PARAM_INDICES = [
    {"K_a": 66, "K_b": 67, "q_norm": 68, "expander": 69},
    {"K_a": 70, "K_b": 71, "q_norm": 72, "expander": 73},
    {"K_a": 74, "K_b": 75, "q_norm": 76, "expander": 77},
    {"K_a": 78, "K_b": 79, "q_norm": 80, "expander": 81},
]
N_LAYERS = 4
Q_DIM    = 128
SQRT_N   = 1024
C_NET    = 32


def build_teacher_netbank(dense: list[torch.Tensor], v_fp32: np.ndarray,
                          layer: int) -> NetBank:
    """One frozen teacher NetBank for a given layer, initialized from a
    worker's dense.pt indices + that worker's bank-net-latest.<layer>.fp16.bin.

    The teacher is kept on CPU, eval mode, with grad off and the simulated
    network delay disabled."""
    idx = NETBANK_PARAM_INDICES[layer]
    # In-RAM init (mmap_path=None) — fits since each teacher is just
    # the per-layer NetBank, not a full model. 1024² × 32 × 4 = 128MB per
    # layer per worker → 128 × 5 × 4 = 2.6 GB total for all teachers.
    nb = NetBank(
        q_dim=Q_DIM, sqrt_n=SQRT_N, c_net=C_NET,
        top_k=64, sub_top_k=64,
        mmap_path=None, bank_on_gpu=False,
        delay_ms_min=0.0, delay_ms_max=0.0,
        dtype="fp32",
    )
    nb.K_a.data.copy_(dense[idx["K_a"]])
    nb.K_b.data.copy_(dense[idx["K_b"]])
    nb.q_norm.weight.data.copy_(dense[idx["q_norm"]])
    nb.expander.weight.data.copy_(dense[idx["expander"]])
    v_tensor = torch.from_numpy(v_fp32).reshape(SQRT_N * SQRT_N, C_NET)
    nb.V.weight.data.copy_(v_tensor)
    nb.eval()
    for p in nb.parameters():
        p.requires_grad_(False)
    return nb


def build_student_netbank(merged_dense: list[torch.Tensor], layer: int,
                          init: str = "zeros") -> NetBank:
    """One trainable student NetBank for a given layer.

    Inherits K_a/K_b/expander from the FedAvg-merged dense.pt (this is
    fine — the merged routing geometry is what the student will USE at
    inference). V is the part that needs distillation; initialize to
    zeros (clean signal) by default.
    """
    idx = NETBANK_PARAM_INDICES[layer]
    nb = NetBank(
        q_dim=Q_DIM, sqrt_n=SQRT_N, c_net=C_NET,
        top_k=64, sub_top_k=64,
        mmap_path=None, bank_on_gpu=False,
        delay_ms_min=0.0, delay_ms_max=0.0,
        dtype="fp32",
    )
    nb.K_a.data.copy_(merged_dense[idx["K_a"]])
    nb.K_b.data.copy_(merged_dense[idx["K_b"]])
    nb.q_norm.weight.data.copy_(merged_dense[idx["q_norm"]])
    nb.expander.weight.data.copy_(merged_dense[idx["expander"]])
    if init == "zeros":
        nb.V.weight.data.zero_()
    elif init == "merged":
        # FedAvg V — useful baseline if distillation gets stuck
        pass  # caller must set V externally
    else:
        raise ValueError(f"unknown init: {init!r}")
    nb.train()
    return nb


def main() -> int:
    ap = argparse.ArgumentParser(description="Distill teacher ensemble → student NetBank")
    ap.add_argument("--workers", required=True, type=Path,
                    help="harvester-format workers dir (e.g. /tmp/.../harvest-r6)")
    ap.add_argument("--merged",  required=True, type=Path,
                    help="output of FedAvg harvest (dense.pt + bank-net-latest.*.fp16.bin)")
    ap.add_argument("--output",  required=True, type=Path,
                    help="destination for distilled bank-net-latest.*.fp16.bin")
    ap.add_argument("--steps",   type=int, default=500)
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--seq-len", type=int, default=128)
    ap.add_argument("--query-scale", type=float, default=1.0,
                    help="(unused when --captured-queries is set) std of Gaussian query distribution")
    ap.add_argument("--captured-queries", type=Path, default=None,
                    help="path to a .pt file produced by scripts/capture_queries.py — "
                         "list[Tensor] of real q_long per layer. When set, distill samples "
                         "from this pool instead of generating Gaussian noise.")
    ap.add_argument("--lr-v",    type=float, default=1e-2,
                    help="SparseAdam LR for student V (the main distillation target)")
    ap.add_argument("--lr-kab",  type=float, default=1e-4,
                    help="AdamW LR for student K_a/K_b/expander/q_norm (trunk-ish, smaller)")
    ap.add_argument("--seed",    type=int, default=42)
    ap.add_argument("--log-every", type=int, default=50)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    # Discover workers (one subdir per worker; latest step-N inside)
    worker_dirs = sorted(d for d in args.workers.iterdir() if d.is_dir())
    print(f"== distill harvest ==  {len(worker_dirs)} workers")
    for d in worker_dirs:
        print(f"  - {d.name}")

    # Load merged dense.pt — provides student's K_a/K_b/expander/q_norm
    merged_step_dir = next(args.merged.glob("step-*"))
    merged_dense = list(torch.load(merged_step_dir / "dense.pt",
                                    map_location="cpu", weights_only=False))
    print(f"\nMerged dense loaded from {merged_step_dir}: {len(merged_dense)} tensors")

    # Load per-worker NetBank state — per layer per worker
    teachers_per_layer: list[list[NetBank]] = [[] for _ in range(N_LAYERS)]
    n_elems_v = SQRT_N * SQRT_N * C_NET   # 33,554,432
    for wd in worker_dirs:
        step_dir = next(wd.glob("step-*"))
        dense = list(torch.load(step_dir / "dense.pt",
                                map_location="cpu", weights_only=False))
        for layer in range(N_LAYERS):
            fp16 = step_dir / f"bank-net-latest.{layer}.fp16.bin"
            v_fp32 = np.fromfile(fp16, dtype=np.float16).astype(np.float32)
            assert v_fp32.size == n_elems_v, \
                f"{fp16}: expected {n_elems_v} elements, got {v_fp32.size}"
            teachers_per_layer[layer].append(
                build_teacher_netbank(dense, v_fp32, layer)
            )
        del dense
    print(f"Built {N_LAYERS} × {len(worker_dirs)} = "
          f"{N_LAYERS * len(worker_dirs)} teacher NetBanks")

    # Build per-layer students from merged dense
    students: list[NetBank] = []
    for layer in range(N_LAYERS):
        students.append(build_student_netbank(merged_dense, layer, init="zeros"))
    print(f"Built {N_LAYERS} student NetBanks (V=zeros)\n")

    # Optimizers — separate LR for V (sparse) vs K_a/K_b/expander/q_norm (dense)
    v_params   = [s.V.weight for s in students]
    kab_params = [p for s in students
                  for p in [s.K_a, s.K_b, s.q_norm.weight, s.expander.weight]]
    opt_v   = torch.optim.SparseAdam(v_params,   lr=args.lr_v)
    opt_kab = torch.optim.AdamW    (kab_params, lr=args.lr_kab)

    # Optional: load captured real queries
    captured_pool = None
    if args.captured_queries is not None:
        captured_pool = torch.load(args.captured_queries, map_location="cpu",
                                    weights_only=False)
        print(f"\nLoaded captured queries from {args.captured_queries}:")
        for layer, t in enumerate(captured_pool):
            if t is None:
                print(f"  layer {layer}: None (skipped)")
            else:
                print(f"  layer {layer}: {tuple(t.shape)}  std={t.std().item():.4f}  mean={t.mean().item():.4f}")

    # Distillation loop
    qmode = ("captured" if captured_pool is not None
             else f"gaussian(scale={args.query_scale})")
    print(f"distilling: steps={args.steps}  B={args.batch_size}  "
          f"T={args.seq_len}  q={qmode}  "
          f"lr_v={args.lr_v}  lr_kab={args.lr_kab}")
    t0 = time.time()
    for step in range(1, args.steps + 1):
        # Per layer (allows the loss to factorize across NetBanks): generate
        # or sample queries independently.
        total_loss = torch.zeros((), dtype=torch.float32)
        per_layer_losses = []
        for layer in range(N_LAYERS):
            if captured_pool is not None and captured_pool[layer] is not None:
                # Sample B (B, T, q_dim) rows uniformly from the pool. Each
                # row is one captured forward pass at a real position.
                pool = captured_pool[layer]
                n_pool = pool.shape[0]
                idx = torch.randint(0, n_pool, (args.batch_size,))
                q = pool[idx]                              # (B, T, q_dim)
            else:
                q = torch.randn(args.batch_size, args.seq_len, Q_DIM) * args.query_scale

            with torch.no_grad():
                teacher_outs = torch.stack(
                    [t(q) for t in teachers_per_layer[layer]], dim=0
                )                                          # (K, B, T, q_dim)
                target = teacher_outs.mean(dim=0)          # (B, T, q_dim)

            student_out = students[layer](q)               # (B, T, q_dim)
            loss = F.mse_loss(student_out, target)
            total_loss = total_loss + loss
            per_layer_losses.append(float(loss.item()))

        opt_v.zero_grad(); opt_kab.zero_grad()
        total_loss.backward()
        opt_v.step(); opt_kab.step()

        if step == 1 or step % args.log_every == 0 or step == args.steps:
            elapsed = time.time() - t0
            steps_per_s = step / max(elapsed, 1e-6)
            per_l_str = "  ".join(f"L{i}={l:.4f}" for i, l in enumerate(per_layer_losses))
            print(f"  step {step:>4d}  loss={float(total_loss.item()):.4f}  "
                  f"({per_l_str})  {steps_per_s:.2f} steps/s")

    # Save distilled NetBank V back to fp16
    args.output.mkdir(parents=True, exist_ok=True)
    print(f"\nWriting distilled NetBank V → {args.output}")
    for layer in range(N_LAYERS):
        v = students[layer].V.weight.detach().cpu().numpy().astype(np.float16)
        out = args.output / f"bank-net-latest.{layer}.fp16.bin"
        v.tofile(out)
        v_norm = float(np.linalg.norm(v.astype(np.float32)))
        print(f"  layer {layer}: norm={v_norm:.2f}  → {out.name} ({out.stat().st_size/1e6:.1f} MB)")

    # Save refined dense.pt (K_a/K_b/q_norm/expander were lightly trained)
    refined_dense = list(merged_dense)
    for layer in range(N_LAYERS):
        idx = NETBANK_PARAM_INDICES[layer]
        refined_dense[idx["K_a"]]      = students[layer].K_a.detach().clone()
        refined_dense[idx["K_b"]]      = students[layer].K_b.detach().clone()
        refined_dense[idx["q_norm"]]   = students[layer].q_norm.weight.detach().clone()
        refined_dense[idx["expander"]] = students[layer].expander.weight.detach().clone()
    out_step_dir = args.output / merged_step_dir.name
    out_step_dir.mkdir(parents=True, exist_ok=True)
    torch.save(refined_dense, out_step_dir / "dense.pt")
    print(f"  refined dense → {out_step_dir / 'dense.pt'}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
