"""Sparse-delta encoding of V_net for git-friendly worker publish.

Workers train V_net for N rounds starting from a shared reference state
(the prior harvest's published V_net). At the end of the wave each
worker's V_net has drifted from the reference, but the drift is sparse:
only the V-rows that the worker's router selected for some training
batch were updated. Untouched rows are bit-identical to the reference.

Pushing the *full* per-worker V_net (32 layers × 33.5 MB = 1.07 GB) is
redundant — most of those bytes are the reference. Pushing only
(touched_rows, delta_values) collapses the upload to the parts that
actually changed.

File layout in a chunk dir (mirrors opt-sparse-net.{0..31}.pt format
so harvest_chain.py's row-aware fedavg path applies verbatim):

    delta-sparse-net.meta.pt   {pids: [0..31], reference: <descriptor>,
                                sqrt_net: int, c_net: int}
    delta-sparse-net.<pid>.pt  {delta_buf: (R, c_net) fp32,
                                row_to_buf: {vrow: bufidx}}

where R = unique V-rows the worker touched on this layer.

Size budget at design banks (sqrt_n=1024, c_net=8): a worker that
touches 50K rows on a "hot" layer and 1K rows on a "cold" layer
produces a chunk of 50K × 8 × 4 = 1.6 MB or 1K × 8 × 4 = 32 KB. Across
32 layers, total ~10-50 MB per worker — 25-100× less than the full
V_net push. Far under GitHub's 100 MB per-file limit, no chunking
gymnastics needed.

FedAvg semantics (already correct in harvest_chain.py for opt-sparse-net,
this module just feeds the same format):

    union_rows = ⋃_w touched_rows_w
    for each unioned row r:
        delta_merged[r] = (1 / touch_count[r]) · Σ_w delta_buf_w[r]
        V_net_merged[r] = reference[r] + delta_merged[r]

Rows only touched by k of N workers get averaged over those k, not over
N — fixes the row-dilution bug in the current naive-mean V_net fedavg
(where untouched rows of N-1 workers drag the touched row toward
reference).

Usage:
    python3 _delta_sparse_net.py encode <reference_dir> <current_dir> <out_dir>
        # writes out_dir/delta-sparse-net.meta.pt + per-pid chunks
    python3 _delta_sparse_net.py apply  <reference_dir> <delta_dir>  <out_dir>
        # reconstructs full V_net.{0..31}.bin from reference + delta
    python3 _delta_sparse_net.py fedavg <out_dir> <worker_dir_1> <worker_dir_2> ...
        # row-aware merge across workers, writes merged delta to out_dir

CLI is here for one-off use; the harvester imports the Python functions
directly.
"""
import json
import os
import sys
from pathlib import Path
import numpy as np
import torch

PREFIX = "delta-sparse-net"
SQRT_NET, C_NET = 1024, 8
N_LAYERS = 32
# Numerical floor for "row was actually touched". Below this the row is
# considered identical to reference (typical CPU fp32 noise is ~1e-7,
# untouched rows should be bit-equal so 1e-12 catches only real updates).
TOUCH_EPS = 1e-12


def meta_path(d):
    return Path(d) / f"{PREFIX}.meta.pt"


def pid_path(d, pid):
    return Path(d) / f"{PREFIX}.{pid}.pt"


def encode(reference_dir, current_dir, out_dir, *, reference_descriptor=None):
    """Compute delta = current - reference, sparse-encode per-layer.

    reference_dir: contains V_net.{0..31}.bin at SQRT_NET²×C_NET fp32.
    current_dir:   contains V_net.{0..31}.bin (same shape) from worker.
    out_dir:       written to with meta + per-pid chunks.

    A row is considered "touched" if max|delta_row| > TOUCH_EPS. Untouched
    rows are dropped entirely (they'll fall through to reference at apply
    time).
    """
    reference_dir = Path(reference_dir)
    current_dir = Path(current_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pids = list(range(N_LAYERS))
    sizes = []
    total_touched = 0
    n_rows = SQRT_NET * SQRT_NET
    for i in pids:
        ref_path = reference_dir / f"V_net.{i}.bin"
        cur_path = current_dir / f"V_net.{i}.bin"
        if not ref_path.exists() or not cur_path.exists():
            # Layer missing on either side: write an empty chunk so the
            # pid still appears in meta. Harvester treats empty same as
            # "this worker didn't touch this layer".
            torch.save({"delta_buf": torch.zeros((0, C_NET), dtype=torch.float32),
                        "row_to_buf": {}},
                       pid_path(out_dir, i))
            continue

        ref = np.memmap(ref_path, dtype=np.float32, mode="r",
                        shape=(n_rows, C_NET))
        cur = np.memmap(cur_path, dtype=np.float32, mode="r",
                        shape=(n_rows, C_NET))
        # Touched mask: per-row max(|delta|) > TOUCH_EPS.
        # Done in 1M-row chunks so peak temp memory ≤ 32 MB.
        touched_rows = []
        deltas = []
        CHUNK = 1024 * 1024
        for off in range(0, n_rows, CHUNK):
            end = min(off + CHUNK, n_rows)
            d_chunk = cur[off:end] - ref[off:end]
            row_max = np.max(np.abs(d_chunk), axis=1)
            mask = row_max > TOUCH_EPS
            if mask.any():
                local_idx = np.flatnonzero(mask)
                touched_rows.append(local_idx + off)
                deltas.append(d_chunk[local_idx].copy())  # detach mmap view

        if touched_rows:
            rows = np.concatenate(touched_rows)
            delta_buf = np.concatenate(deltas, axis=0)
            row_to_buf = {int(r): j for j, r in enumerate(rows.tolist())}
        else:
            delta_buf = np.zeros((0, C_NET), dtype=np.float32)
            row_to_buf = {}

        chunk = {"delta_buf": torch.from_numpy(delta_buf.astype(np.float32)).clone(),
                 "row_to_buf": row_to_buf}
        torch.save(chunk, pid_path(out_dir, i))
        sz = os.path.getsize(pid_path(out_dir, i))
        sizes.append(sz)
        total_touched += len(row_to_buf)

    meta = {"pids": pids, "reference": reference_descriptor or str(reference_dir),
            "sqrt_net": SQRT_NET, "c_net": C_NET}
    torch.save(meta, meta_path(out_dir))

    full_v_net_bytes = N_LAYERS * n_rows * C_NET * 4
    print(f"encode: {N_LAYERS} layers, {total_touched:,} touched rows total")
    if sizes:
        print(f"        chunk sizes {min(sizes)/1e6:.2f}-{max(sizes)/1e6:.2f} MB, "
              f"total {sum(sizes)/1e6:.1f} MB "
              f"(vs full V_net {full_v_net_bytes/1e6:.0f} MB, "
              f"{full_v_net_bytes/max(sum(sizes),1):.1f}× compression)")
    print(f"        → {out_dir}")


def apply(reference_dir, delta_dir, out_dir):
    """Reconstruct V_net.{0..31}.bin = reference + delta. Mostly for tests."""
    reference_dir = Path(reference_dir)
    delta_dir = Path(delta_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not meta_path(delta_dir).exists():
        print(f"apply: no meta at {meta_path(delta_dir)}", file=sys.stderr)
        sys.exit(2)
    meta = torch.load(meta_path(delta_dir), map_location="cpu", weights_only=False)
    n_rows = meta["sqrt_net"] ** 2
    c_net = meta["c_net"]

    for pid in meta["pids"]:
        ref_path = reference_dir / f"V_net.{pid}.bin"
        out_path = out_dir / f"V_net.{pid}.bin"
        ref = np.memmap(ref_path, dtype=np.float32, mode="r",
                        shape=(n_rows, c_net))
        out = np.memmap(out_path, dtype=np.float32, mode="w+",
                        shape=(n_rows, c_net))
        # Copy in chunks to stay memory-bounded.
        CHUNK = 1024 * 1024
        for off in range(0, n_rows, CHUNK):
            end = min(off + CHUNK, n_rows)
            out[off:end] = ref[off:end]

        chunk_p = pid_path(delta_dir, pid)
        if chunk_p.exists():
            d = torch.load(chunk_p, map_location="cpu", weights_only=False)
            if d["row_to_buf"]:
                rows = np.array(sorted(d["row_to_buf"].keys()), dtype=np.int64)
                bufidx = np.array([d["row_to_buf"][int(r)] for r in rows],
                                  dtype=np.int64)
                delta = d["delta_buf"].numpy()[bufidx]
                out[rows] = out[rows] + delta
        out.flush()
    print(f"apply: reconstructed {len(meta['pids'])} V_net layers → {out_dir}")


def fedavg(out_dir, worker_dirs):
    """Row-aware FedAvg across workers' delta chunks.

    Writes merged delta to out_dir/ in the same chunk format.

    Memory: streams workers one at a time per pid. After each load we
    drop the reference and force gc; without that, pytorch's CPU
    caching allocator holds onto storages and memory grows linearly
    with bird count even though we never hold more than one bird's
    payload at a time logically.
    """
    import gc, resource
    def _rss_mb():
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    worker_dirs = [Path(w) for w in worker_dirs]

    # Use first worker's meta as the template; sanity-check the rest.
    metas = [torch.load(meta_path(w), map_location="cpu", weights_only=False)
             for w in worker_dirs]
    pids = metas[0]["pids"]
    for m, w in zip(metas[1:], worker_dirs[1:]):
        if m["pids"] != pids:
            print(f"fedavg: pid mismatch at {w}", file=sys.stderr); sys.exit(2)
        if m["sqrt_net"] != metas[0]["sqrt_net"] or m["c_net"] != metas[0]["c_net"]:
            print(f"fedavg: shape mismatch at {w}", file=sys.stderr); sys.exit(2)
    torch.save(metas[0], meta_path(out_dir))
    c_net = metas[0]["c_net"]
    del metas
    gc.collect()

    print(f"fedavg: starting {len(pids)}-pid merge across "
          f"{len(worker_dirs)} workers (peak RSS so far: {_rss_mb():.0f} MB)")

    for pid_idx, pid in enumerate(pids):
        # Pass 1: collect the union of touched rows. Load each worker
        # one at a time, take just the keys, drop the rest immediately.
        union_set = set()
        worker_paths = []
        for w in worker_dirs:
            p = pid_path(w, pid)
            if not p.exists():
                continue
            d = torch.load(p, map_location="cpu", weights_only=False)
            if d.get("row_to_buf"):
                union_set.update(d["row_to_buf"].keys())
                worker_paths.append(p)
            del d
        gc.collect()

        if not worker_paths:
            torch.save({"delta_buf": torch.zeros((0, c_net), dtype=torch.float32),
                        "row_to_buf": {}},
                       pid_path(out_dir, pid))
            continue

        union = sorted(union_set)
        R = len(union)
        new_r2b = {vrow: i for i, vrow in enumerate(union)}
        delta_sum = torch.zeros((R, c_net), dtype=torch.float32)
        counts = torch.zeros((R,), dtype=torch.long)
        del union_set, union  # we have new_r2b; the source sets are no longer needed
        gc.collect()

        # Pass 2: stream each worker's delta into the accumulator,
        # dropping the loaded payload immediately after use.
        for p in worker_paths:
            s = torch.load(p, map_location="cpu", weights_only=False)
            r2b = s.get("row_to_buf") or {}
            if r2b:
                src_rows = []
                dst_rows = []
                for vrow, bidx in r2b.items():
                    src_rows.append(bidx)
                    dst_rows.append(new_r2b[vrow])
                src_t = torch.tensor(src_rows, dtype=torch.long)
                dst_t = torch.tensor(dst_rows, dtype=torch.long)
                contrib = s["delta_buf"][src_t].to(torch.float32)
                delta_sum.index_add_(0, dst_t, contrib)
                counts.index_add_(0, dst_t, torch.ones(len(dst_t), dtype=torch.long))
                del contrib, src_t, dst_t, src_rows, dst_rows
            del s, r2b
            gc.collect()

        # Per-row mean over the workers that touched it.
        delta_merged = delta_sum / counts.unsqueeze(1).to(torch.float32)
        torch.save({"delta_buf": delta_merged, "row_to_buf": new_r2b},
                   pid_path(out_dir, pid))
        del delta_sum, counts, delta_merged, new_r2b
        gc.collect()

        if pid_idx % 8 == 0 or pid_idx == len(pids) - 1:
            print(f"  pid {pid_idx + 1}/{len(pids)}: R={R}, "
                  f"workers={len(worker_paths)}, RSS={_rss_mb():.0f} MB")

    print(f"fedavg: merged {len(worker_dirs)} workers' deltas → {out_dir}")


def _cli():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "encode" and len(sys.argv) == 5:
        encode(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "apply" and len(sys.argv) == 5:
        apply(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "fedavg" and len(sys.argv) >= 4:
        fedavg(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__); sys.exit(2)


if __name__ == "__main__":
    _cli()
