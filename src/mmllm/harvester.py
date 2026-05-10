"""mmllm community harvester — merge multiple worker checkpoints into a shared core.

Runs locally (no Modal dependency). A Modal wrapper can call into this
function unchanged. Inputs:

  workers_dir/
    worker-1/
      step-N/
        dense.pt           ← merged FedAvg-style across workers
        opt-dense.pt       ← discarded (workers' optimizer state is local)
        opt-sparse.pt      ← discarded
      bank-latest.0.bin    ← per-worker Local Bank V (NOT merged; each worker
      bank-latest.1.bin       keeps its own — Local = personal cortex)
      ...
      meta.json            ← {"tokens_trained": N, "label": "...", ...}
    worker-2/
      ...

  output_dir/
    step-N/
      dense.pt             ← weighted average of worker dense.pt files
      meta.json            ← {"sources": [...], "n_workers": K, "ts": ...}
    bank-latest.<i>.bin    ← optional shared NetBank (union/average of
                              touched rows from each worker, if any)

The harvester does NOT merge Local Banks. Per the triune-brain mapping,
Local Bank is the per-worker cortex — task-specific, never shared. Only
the trunk (dense params) and optionally NetBank (cerebellum) merge.

Usage:

  # Local — pure file system
  python -m mmllm.harvester \\
    --workers ./workers \\
    --output  ./core-merged \\
    --weighted-by tokens_trained

  # Modal — same logic, run inside a Modal function
  modal run modal_app.py::harvest --workers /data/workers --output /data/core
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Iterable

import torch


# ─────────────────── per-worker discovery ───────────────────


def find_worker_ckpts(workers_dir: Path) -> list[dict]:
    """Scan workers_dir/<worker>/step-N for dense.pt + meta.json. Returns
    a list of dicts with worker_id, step, dense_path, meta. Skips any
    worker without a valid step-N directory."""
    found = []
    if not workers_dir.exists():
        return found
    for worker in sorted(workers_dir.iterdir()):
        if not worker.is_dir():
            continue
        # Pick the latest step-N for this worker
        step_dirs = [d for d in worker.iterdir() if d.is_dir() and d.name.startswith("step-")]
        if not step_dirs:
            continue
        latest = max(step_dirs, key=lambda d: int(d.name.split("-", 1)[1]))
        dense_path = latest / "dense.pt"
        if not dense_path.exists():
            continue
        meta_path = worker / "meta.json"
        meta = {}
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text())
            except Exception:
                meta = {}
        found.append({
            "worker_id":  worker.name,
            "step":       int(latest.name.split("-", 1)[1]),
            "dense_path": dense_path,
            "worker_dir": worker,
            "meta":       meta,
        })
    return found


# ─────────────────── dense FedAvg ───────────────────


def _weight_for(meta: dict, mode: str) -> float:
    """Compute a worker's averaging weight from its meta.json."""
    if mode == "uniform":
        return 1.0
    if mode == "tokens_trained":
        return float(meta.get("tokens_trained") or 1)
    if mode == "steps":
        return float(meta.get("steps") or 1)
    raise ValueError(f"unknown weighted-by mode: {mode!r}")


def fedavg_dense(workers: list[dict], weighted_by: str = "tokens_trained") -> list[torch.Tensor]:
    """Load each worker's dense.pt and produce a weighted-average list of
    tensors. Workers must agree on tensor shapes; mismatches raise.

    dense.pt is a `list[Tensor]` (positional, per the trainer's
    save-checkpoint! code). We average tensor-by-tensor."""
    weights: list[float] = []
    arrays: list[list[torch.Tensor]] = []
    for w in workers:
        wt = _weight_for(w["meta"], weighted_by)
        if wt <= 0:
            print(f"  skip {w['worker_id']}: weight<=0 ({wt})")
            continue
        tensors = torch.load(w["dense_path"], map_location="cpu")
        weights.append(wt)
        arrays.append(list(tensors))
        print(f"  load {w['worker_id']:20s}  step={w['step']:>6}  weight={wt:>10.0f}  "
              f"#tensors={len(tensors)}")

    if not arrays:
        raise RuntimeError("no usable worker checkpoints found")

    n_tensors = len(arrays[0])
    # Validate shape consistency
    for i, a in enumerate(arrays[1:], start=1):
        if len(a) != n_tensors:
            raise RuntimeError(
                f"worker[0] has {n_tensors} tensors but worker[{i}] has {len(a)}; "
                "topologies differ — cannot FedAvg")

    total_w = sum(weights)
    print(f"  total weight: {total_w:.1f} across {len(weights)} workers")

    # Tensor-by-tensor weighted average
    averaged: list[torch.Tensor] = []
    for ti in range(n_tensors):
        shapes = {tuple(a[ti].shape) for a in arrays}
        if len(shapes) > 1:
            print(f"  WARN: shape mismatch at tensor {ti}: {shapes} — "
                  f"using worker[0] unchanged (no merge)")
            averaged.append(arrays[0][ti].clone())
            continue
        acc = torch.zeros_like(arrays[0][ti], dtype=torch.float32)
        for w, a in zip(weights, arrays):
            acc.add_(a[ti].to(torch.float32), alpha=w / total_w)
        averaged.append(acc.to(arrays[0][ti].dtype))
    return averaged


# ─────────────────── optional NetBank merge ───────────────────


def merge_netbank_files(workers: list[dict], output_dir: Path,
                       weighted_by: str = "tokens_trained") -> bool:
    """If workers carry per-layer NetBank V mmap files (named
    `bank-net-latest.<i>.bin` in the worker's step-N directory), produce
    a weighted average and write to <output>/bank-net-latest.<i>.bin.

    NetBank V is the shared cerebellum — averaging it across workers IS
    the consolidation step. Local Bank V is NOT merged (per-worker cortex).

    Returns True if any files were merged."""
    # Scan for NetBank files in each worker's latest step-N dir
    per_layer_files: dict[int, list[tuple[Path, float]]] = {}
    for w in workers:
        wt = _weight_for(w["meta"], weighted_by)
        if wt <= 0:
            continue
        step_dir = w["dense_path"].parent
        for f in step_dir.glob("bank-net-latest.*.bin"):
            try:
                layer = int(f.name.split(".")[1])
            except (ValueError, IndexError):
                continue
            per_layer_files.setdefault(layer, []).append((f, wt))

    if not per_layer_files:
        return False

    output_dir.mkdir(parents=True, exist_ok=True)
    for layer, file_weights in sorted(per_layer_files.items()):
        # Determine shape from first file's size (raw fp32 bytes / 4)
        # — we don't have a header. Trust the first worker as canonical.
        first_path, _ = file_weights[0]
        # We don't know rows × cols a priori; require all files same byte size.
        sizes = {f.stat().st_size for f, _ in file_weights}
        if len(sizes) > 1:
            print(f"  WARN: layer {layer} NetBank file sizes differ {sizes} — using first only")
            (output_dir / f"bank-net-latest.{layer}.bin").write_bytes(first_path.read_bytes())
            continue

        size = first_path.stat().st_size
        n_floats = size // 4
        total_w = sum(w for _, w in file_weights)
        # Weighted average — read each as fp32 mmap, accumulate.
        import numpy as np
        acc = np.zeros(n_floats, dtype=np.float32)
        for fp, wt in file_weights:
            arr = np.fromfile(fp, dtype=np.float32, count=n_floats)
            acc += arr * (wt / total_w)
        out_path = output_dir / f"bank-net-latest.{layer}.bin"
        acc.tofile(out_path)
        print(f"  NetBank layer {layer}: {len(file_weights)} workers → {out_path} "
              f"({size / 1024**2:.1f} MB)")
    return True


# ─────────────────── main ───────────────────


def harvest(workers_dir: Path, output_dir: Path,
            weighted_by: str = "tokens_trained",
            output_step: int | None = None) -> dict:
    """End-to-end harvest. Returns a summary dict."""
    workers = find_worker_ckpts(workers_dir)
    if not workers:
        raise RuntimeError(f"no worker checkpoints under {workers_dir}")
    print(f"== harvester ==  workers_dir={workers_dir}  output={output_dir}")
    print(f"   found {len(workers)} workers; weighted-by={weighted_by}")

    averaged = fedavg_dense(workers, weighted_by=weighted_by)

    # Determine output step number — caller-supplied or max worker step
    if output_step is None:
        output_step = max(w["step"] for w in workers)
    out_step_dir = output_dir / f"step-{output_step}"
    out_step_dir.mkdir(parents=True, exist_ok=True)

    out_dense = out_step_dir / "dense.pt"
    torch.save(averaged, out_dense)
    print(f"  wrote merged dense → {out_dense} ({out_dense.stat().st_size / 1024**2:.1f} MB)")

    # NetBank merge (if any worker carries it)
    netbank_merged = merge_netbank_files(workers, output_dir, weighted_by=weighted_by)

    summary = {
        "ts":             time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "n_workers":      len(workers),
        "output_step":    output_step,
        "weighted_by":    weighted_by,
        "netbank_merged": netbank_merged,
        "sources": [
            {"worker_id": w["worker_id"], "step": w["step"], "meta": w["meta"]}
            for w in workers
        ],
    }
    (out_step_dir / "meta.json").write_text(json.dumps(summary, indent=2))
    print(f"  wrote meta → {out_step_dir / 'meta.json'}")
    return summary


def cli() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--workers", required=True, type=Path,
                    help="directory containing per-worker subdirs each with step-N/dense.pt")
    ap.add_argument("--output", required=True, type=Path,
                    help="directory to write merged step-N/dense.pt + bank-net-latest.<i>.bin")
    ap.add_argument("--weighted-by",
                    choices=["uniform", "tokens_trained", "steps"],
                    default="tokens_trained",
                    help="how to weight workers in the FedAvg average")
    ap.add_argument("--step", type=int, default=None,
                    help="output step number (default: max worker step)")
    args = ap.parse_args()
    harvest(args.workers, args.output,
            weighted_by=args.weighted_by, output_step=args.step)


if __name__ == "__main__":
    cli()
