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

  # FIM-aware merge — weight workers by measured FIM-bpc (lower = better)
  python -m mmllm.harvester \\
    --workers ./workers \\
    --output  ./core-merged \\
    --weighted-by fim_quality

  # Modal — same logic, run inside a Modal function
  modal run modal_app.py::harvest --workers /data/workers --output /data/core

FIM workers should populate `meta.fim` in their worker meta.json:

    {
      "tokens_trained": 5120000,
      "steps": 10000,
      "label": "your-handle",
      "fim": {
        "language": "clojure",
        "fim_ratio": 0.5,
        "splitter": "clojure-form-boundary",
        "fim_eval_bpc": 1.42,
        "fim_eval_exact_pct": 12.3
      }
    }

See docs/fim-plan.md §4 for the language-specialization merge story.
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
    """Compute a worker's averaging weight from its meta.json.

    Modes:
      - uniform: 1.0 for every worker
      - tokens_trained: meta.tokens_trained (proxy for compute spent)
      - steps: meta.steps
      - fim_bpc: 1 / max(meta.fim.fim_eval_bpc, 0.1) — lower bpc is
        better consolidation, so reward it linearly. Workers without
        meta.fim.fim_eval_bpc get weight 0 (excluded from FIM merge).
      - fim_quality: tokens_trained / max(meta.fim.fim_eval_bpc, 0.1)
        — combine compute spent with measured quality."""
    if mode == "uniform":
        return 1.0
    if mode == "tokens_trained":
        return float(meta.get("tokens_trained") or 1)
    if mode == "steps":
        return float(meta.get("steps") or 1)
    if mode == "fim_bpc":
        bpc = (meta.get("fim") or {}).get("fim_eval_bpc")
        if bpc is None:
            return 0.0
        return 1.0 / max(float(bpc), 0.1)
    if mode == "fim_quality":
        tokens = float(meta.get("tokens_trained") or 1)
        bpc = (meta.get("fim") or {}).get("fim_eval_bpc")
        if bpc is None:
            return 0.0
        return tokens / max(float(bpc), 0.1)
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
            print(f"  skip {w['worker_id']}: weight<=0 ({wt})  "
                  f"(check meta.json — fim modes need meta.fim.fim_eval_bpc)")
            continue
        tensors = torch.load(w["dense_path"], map_location="cpu")
        weights.append(wt)
        arrays.append(list(tensors))
        fim = (w["meta"].get("fim") or {})
        fim_str = (f"  fim-bpc={fim['fim_eval_bpc']:.2f}"
                   if fim.get("fim_eval_bpc") is not None else "")
        lang = fim.get("language", "")
        lang_str = f"  lang={lang}" if lang else ""
        print(f"  load {w['worker_id']:20s}  step={w['step']:>6}  weight={wt:>10.2f}  "
              f"#tensors={len(tensors)}{lang_str}{fim_str}")

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
    """If workers carry per-layer NetBank V mmap files, produce a weighted
    average and write to the output dir. NetBank V is the shared
    cerebellum — averaging it across workers IS the consolidation step.
    Local Bank V is NOT merged (per-worker cortex).

    Recognizes two file conventions:
      bank-net-latest.{i}.bin       — fp32 (legacy, ~128 MB at sqrt_n=1024)
      bank-net-latest.{i}.fp16.bin  — fp16 (round-5+, ~64 MB, fits in
                                            GitHub's 100 MB blob limit)
    Detected by filename suffix. Output preserves whichever the inputs
    used (all-fp16 → fp16 out; mixed or all-fp32 → fp32 out).

    Returns True if any files were merged."""
    import numpy as np

    # Scan for NetBank files in each worker's latest step-N dir
    per_layer_files: dict[int, list[tuple[Path, float, str]]] = {}
    for w in workers:
        wt = _weight_for(w["meta"], weighted_by)
        if wt <= 0:
            continue
        step_dir = w["dense_path"].parent
        # Prefer .fp16.bin if present (newer convention); fall back to .bin.
        # Don't double-count: if both exist for the same layer, pick fp16.
        fp16_layers = set()
        for f in step_dir.glob("bank-net-latest.*.fp16.bin"):
            try:    layer = int(f.name.split(".")[1])
            except: continue
            per_layer_files.setdefault(layer, []).append((f, wt, "fp16"))
            fp16_layers.add(layer)
        for f in step_dir.glob("bank-net-latest.*.bin"):
            if ".fp16.bin" in f.name: continue   # already handled
            try:    layer = int(f.name.split(".")[1])
            except: continue
            if layer in fp16_layers: continue    # prefer the fp16 we already grabbed
            per_layer_files.setdefault(layer, []).append((f, wt, "fp32"))

    if not per_layer_files:
        return False

    output_dir.mkdir(parents=True, exist_ok=True)
    for layer, entries in sorted(per_layer_files.items()):
        # All inputs for a given layer must have matching element-count
        # (different bytes-per-element is fine — fp16 vs fp32 distinguish).
        def _n_elems(path: Path, dt: str) -> int:
            bpe = 2 if dt == "fp16" else 4
            return path.stat().st_size // bpe
        n_set = {_n_elems(f, dt) for f, _, dt in entries}
        if len(n_set) > 1:
            first_path, _, _ = entries[0]
            print(f"  WARN: layer {layer} NetBank element-counts differ {n_set} — using worker[0] unchanged")
            (output_dir / first_path.name).write_bytes(first_path.read_bytes())
            continue
        n_elems = n_set.pop()
        total_w = sum(w for _, w, _ in entries)
        # Weighted average in fp32 regardless of input dtype, for numerical safety.
        acc = np.zeros(n_elems, dtype=np.float32)
        for fp, wt, dt in entries:
            np_dt = np.float16 if dt == "fp16" else np.float32
            arr = np.fromfile(fp, dtype=np_dt, count=n_elems).astype(np.float32)
            acc += arr * (wt / total_w)
        # Output dtype: if ALL inputs were fp16, write fp16; otherwise fp32.
        all_fp16 = all(dt == "fp16" for _, _, dt in entries)
        if all_fp16:
            out_path = output_dir / f"bank-net-latest.{layer}.fp16.bin"
            acc.astype(np.float16).tofile(out_path)
        else:
            out_path = output_dir / f"bank-net-latest.{layer}.bin"
            acc.tofile(out_path)
        size_mb = out_path.stat().st_size / 1024**2
        print(f"  NetBank layer {layer}: {len(entries)} workers → {out_path.name} "
              f"({size_mb:.1f} MB)")
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

    # Aggregate FIM stats across workers (if any reported)
    fim_workers = [w for w in workers
                   if (w["meta"].get("fim") or {}).get("fim_eval_bpc") is not None]
    fim_summary: dict | None = None
    if fim_workers:
        langs = sorted({(w["meta"].get("fim") or {}).get("language", "?")
                        for w in fim_workers})
        bpcs = [(w["meta"]["fim"]["fim_eval_bpc"]) for w in fim_workers]
        fim_summary = {
            "n_fim_workers":  len(fim_workers),
            "languages":      langs,
            "fim_bpc_min":    min(bpcs),
            "fim_bpc_max":    max(bpcs),
            "fim_bpc_mean":   sum(bpcs) / len(bpcs),
        }
        print(f"  FIM stats: {len(fim_workers)} workers across languages={langs}; "
              f"bpc range [{min(bpcs):.2f}..{max(bpcs):.2f}]")

    summary = {
        "ts":             time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "n_workers":      len(workers),
        "output_step":    output_step,
        "weighted_by":    weighted_by,
        "netbank_merged": netbank_merged,
        "fim":            fim_summary,
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
                    choices=["uniform", "tokens_trained", "steps",
                             "fim_bpc", "fim_quality"],
                    default="tokens_trained",
                    help="how to weight workers in the FedAvg average. "
                         "fim_bpc and fim_quality require meta.fim.fim_eval_bpc.")
    ap.add_argument("--step", type=int, default=None,
                    help="output step number (default: max worker step)")
    args = ap.parse_args()
    harvest(args.workers, args.output,
            weighted_by=args.weighted_by, output_step=args.step)


if __name__ == "__main__":
    cli()
