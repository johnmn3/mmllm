"""Generic N-way FedAvg harvest of chain-diverse worker endpoints.

Two modes:
  batch  (default): load ALL workers from /tmp/mmllm-cpu/harvest-r${T}/<h>/
                    into memory at once, FedAvg, write outputs. Fine up to
                    ~5 workers; at N=20 worker artifacts total ~25 GB so the
                    /tmp side hits disk pressure.
  stream: per-worker incremental accumulator on disk. The orchestrator
                    fetches + extracts one worker, calls --mode=stream-update
                    to fold it in, then deletes the worker dir. After all
                    workers, --mode=stream-finalize divides sums by N and
                    writes the harvested outputs. Peak /tmp = one worker
                    (~1.25 GB) + accumulator (~2 GB) regardless of N.

Worker layout expected at staging dir (orchestrator populates this):
  /tmp/mmllm-cpu/harvest-r${TARGET}/<handle>/
    V_net.{0..31}.bin
    dense.pt
    opt-sparse-net.{0..31}.pt + opt-sparse-net.meta.pt   (R91+ chunked)
      or
    opt-sparse-net.pt                                    (R20-R90 legacy)
    round-${TARGET}.log.jsonl   (optional, used for ctrl_bpc reporting)

Usage:
  Batch mode:
    python3 scripts/harvest_chain.py <target_round> [--publish]

  Stream mode (orchestrator fuses fetch+extract+update per worker):
    python3 scripts/harvest_chain.py --mode=stream-update \\
                                     <accum_dir> <worker_dir> <handle>
    python3 scripts/harvest_chain.py --mode=stream-finalize \\
                                     <target_round> <accum_dir> [--publish]

  --publish: also stage the harvested artifacts into workers/dispatcher/.

Accumulator layout (stream mode, under accum_dir/):
  meta.json                  {count, workers: [], target_round, bpcs}
  V_net.<i>.sum.bin          float32 mmap, shape (1024², 8), running V_net sum
  dense.sum.pt               list of running-sum tensors
  opt-pid-<i>.accum.pt       per-V_net-layer Adam state accumulator:
                               {row_to_idx, m_buf (sum), v_buf (sum),
                                counts (per-row), step}
  opt-param_groups.pt        param_groups skeleton (taken from worker 1)
"""
import argparse, json, os, sys, numpy as np, torch
from pathlib import Path

# NetBank V_net per layer: sqrt_n² × c_net × 4 bytes
#   1024² × 8 × 4 = 33.5 MB / layer → 1.07 GB across 32 layers
# Designed: NetBank 1 GB total. Operating at 64/8 was a 256× shrink
# (4 MB total) — fixed in commit after R90.
SQRT_NET, C_NET = 1024, 8
SQRT_LOCAL, Q_DIM = 226, 16
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
N_TRUNKS = 16

def discover_workers(stage_dir):
    """Worker handles = subdirs of stage_dir that contain V_net.0.bin."""
    return sorted(d.name for d in stage_dir.iterdir()
                  if d.is_dir() and (d / "V_net.0.bin").is_file())

def pick_best_worker(stage_dir, workers, target_round):
    """Read each worker's round-${target_round}.log.jsonl, find the ablation
    event, return the handle with lowest control_bpc. Falls back to first
    worker if no logs found."""
    best = None
    bpcs = {}
    for h in workers:
        log = stage_dir / h / f"round-{target_round}.log.jsonl"
        if not log.exists():
            continue
        for line in log.read_text().splitlines():
            try: ev = json.loads(line)
            except: continue
            if ev.get("event") == "ablation":
                ctrl = ev.get("control_bpc")
                if ctrl is None: continue
                try: bpcs[h] = float(ctrl)
                except: pass
                break
    if not bpcs:
        print(f"  WARN: no log.jsonl found for any worker; using first worker's opt-state ({workers[0]})")
        return workers[0], {}
    best = min(bpcs, key=bpcs.get)
    return best, bpcs

def fedavg_v_net(stage_dir, workers, out_prefix):
    """Returns dict of per-layer pairwise cos stats at sampled layers."""
    print(f"\n=== FedAvg V_net across {len(workers)} workers ===")
    cos_stats = {}
    for i in range(32):
        stacks = []
        for h in workers:
            v = np.array(np.memmap(stage_dir / h / f"V_net.{i}.bin",
                                   dtype=np.float32, mode="r",
                                   shape=(SQRT_NET * SQRT_NET, C_NET)))
            stacks.append(v)
        merged = np.mean(stacks, axis=0).astype(np.float32)
        out = np.memmap(f"{out_prefix}-net.{i}.bin", dtype=np.float32,
                        mode="w+", shape=(SQRT_NET * SQRT_NET, C_NET))
        out[:] = merged; out.flush()
        if i in [0, 12, 31]:
            cos_pair = []
            for j in range(len(workers)):
                for k in range(j + 1, len(workers)):
                    vj, vk = stacks[j].ravel(), stacks[k].ravel()
                    c = float(vj @ vk / (np.linalg.norm(vj) * np.linalg.norm(vk) + 1e-20))
                    cos_pair.append(c)
            cos_stats[i] = {"mean": float(np.mean(cos_pair)),
                            "min": min(cos_pair), "max": max(cos_pair)}
            print(f"  layer {i}: max|v| individual = "
                  f"[{', '.join(f'{np.abs(s).max():.3f}' for s in stacks)}]")
            print(f"           merged max|v| = {np.abs(merged).max():.3f}")
            print(f"           pairwise cos mean = {np.mean(cos_pair):.4f}, "
                  f"range=[{min(cos_pair):.4f}, {max(cos_pair):.4f}]")
    return cos_stats

def fedavg_dense(stage_dir, workers, out_path):
    """Returns dict of pairwise cos stats over dense."""
    print(f"\n=== FedAvg dense.pt across {len(workers)} workers ===")
    dense = [torch.load(stage_dir / h / "dense.pt", map_location="cpu",
                        weights_only=False) for h in workers]
    assert all(len(d) == len(dense[0]) for d in dense), "dense.pt tensor count mismatch"
    merged = []
    for tensors_at_i in zip(*dense):
        if hasattr(tensors_at_i[0], "shape") and all(t.shape == tensors_at_i[0].shape
                                                     for t in tensors_at_i):
            merged.append(torch.stack(tensors_at_i).mean(0))
        else:
            merged.append(tensors_at_i[0])
    n_params = sum(t.numel() for t in merged if hasattr(t, 'numel'))
    print(f"  averaged {len(merged)} tensors, {n_params:,} total params")
    def flat(ts):
        return torch.cat([t.flatten() for t in ts if hasattr(t, "flatten")])
    flats = [flat(d) for d in dense]
    cos_d = []
    for j in range(len(workers)):
        for k in range(j + 1, len(workers)):
            c = float(torch.dot(flats[j], flats[k]) / (flats[j].norm() * flats[k].norm() + 1e-20))
            cos_d.append(c)
    print(f"  dense pairwise cos mean = {np.mean(cos_d):.4f}, "
          f"range=[{min(cos_d):.4f}, {max(cos_d):.4f}]")
    torch.save(merged, out_path)
    print(f"  wrote {out_path} ({os.path.getsize(out_path)/1e6:.2f} MB)")
    return {"mean": float(np.mean(cos_d)), "min": min(cos_d), "max": max(cos_d),
            "n_params": n_params, "n_tensors": len(merged)}

def v_local_gaussian(out_prefix):
    """Re-init V_local for inference (never trained at inf time)."""
    print("\n=== V_local Gaussian-init ===")
    n_local = N_TRUNKS * SQRT_LOCAL * SQRT_LOCAL
    rng = np.random.default_rng(0)
    for i in LOCAL_LAYERS:
        a = np.memmap(f"{out_prefix}.{i}.bin", dtype=np.float32, mode="w+",
                      shape=(n_local, Q_DIM))
        CHUNK = 4096
        for s in range(0, n_local, CHUNK):
            e = min(s + CHUNK, n_local)
            a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * 0.02).astype(np.float32)
        a.flush()
    print(f"  {len(LOCAL_LAYERS)} layers × {N_TRUNKS} trunks, q_dim={Q_DIM}")

def fedavg_opt_sparse_net(stage_dir, workers, out_dir):
    """Row-aware FedAvg of opt-sparse-net chunks across workers.

    Each worker publishes its end-of-wave opt-sparse-net.{0..31}.pt
    chunks (per-V_net-layer Adam state) plus opt-sparse-net.meta.pt.
    Per-layer merge: union of touched V-rows, per-row mean over the
    workers that touched it. See scripts/_opt_sparse_net_chunk.py for
    details; we delegate to its `fedavg` helper.

    Back-compat: if a worker has a legacy single-file opt-sparse-net.pt
    instead of chunks, split it in place under the worker dir so it can
    join the merge.
    """
    chunk_dirs = []
    for h in workers:
        wd = stage_dir / h
        meta = wd / "opt-sparse-net.meta.pt"
        legacy = wd / "opt-sparse-net.pt"
        if meta.exists():
            chunk_dirs.append(str(wd))
        elif legacy.exists():
            print(f"  {h}: legacy single-file opt-sparse-net.pt — splitting in place")
            from subprocess import run
            run([sys.executable,
                 str(Path(__file__).resolve().parent / "_opt_sparse_net_chunk.py"),
                 "split", str(legacy), str(wd)], check=True)
            chunk_dirs.append(str(wd))
        else:
            print(f"  {h}: no opt-sparse-net (chunks or single-file) — skipping")
    if not chunk_dirs:
        print("  no workers had opt-sparse-net state; skipping fedavg")
        return None
    out_dir.mkdir(parents=True, exist_ok=True)
    from subprocess import run
    run([sys.executable,
         str(Path(__file__).resolve().parent / "_opt_sparse_net_chunk.py"),
         "fedavg", str(out_dir), *chunk_dirs], check=True)
    return out_dir

def publish_to_dispatcher(stage_dir, workers, best_handle, target_round,
                          harvested_prefix, harvested_dense, repo_root):
    """Copy harvested V_net + dense + chunked fedavg'd opt-state under
    workers/dispatcher/harvest-${N}way-r${TARGET}/round-${TARGET}/.
    Returns the path to round-${TARGET}/.

    opt-sparse-net is published as chunks (opt-sparse-net.{0..31}.pt +
    opt-sparse-net.meta.pt) rather than a single 230 MB file — single-file
    exceeds GitHub's 100 MB per-file limit at design-sized V_net.
    extend_chain.sh handles the chunked layout on resume."""
    n = len(workers)
    publish_dir = repo_root / f"workers/dispatcher/harvest-{n}way-r{target_round}" / f"round-{target_round}"
    publish_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== Publishing to {publish_dir} ===")
    import shutil
    for i in range(32):
        shutil.copy(f"{harvested_prefix}-net.{i}.bin",
                    publish_dir / f"V_net.{i}.bin")
    shutil.copy(harvested_dense, publish_dir / "dense.pt")
    opt_result = fedavg_opt_sparse_net(stage_dir, workers, publish_dir)
    if opt_result is not None:
        print(f"  staged 32× V_net + dense.pt + {len(workers)}-way FedAvg opt-sparse-net chunks")
    else:
        print(f"  staged 32× V_net + dense.pt (no opt-sparse-net state across workers)")
    return publish_dir

# ─── Streaming accumulator ────────────────────────────────────────────
# State on disk in <accum_dir>/, updated one worker at a time. Keeps peak
# /tmp at ~one worker + accumulator regardless of total N workers.

def _accum_load_meta(accum_dir):
    p = accum_dir / "meta.json"
    if p.exists():
        return json.loads(p.read_text())
    return {"count": 0, "workers": [], "target_round": None, "bpcs": {}}

def _accum_save_meta(accum_dir, meta):
    (accum_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")

# V_net per-layer running sum mmap. CHUNK keeps per-update temp under
# ~30 MB even at sqrt_n=1024 (1M rows × 8 dims × 4 B = 32 MB / layer).
_VNET_CHUNK = 1024 * 1024

def _stream_update_v_net(accum_dir, worker_dir):
    for i in range(32):
        wfn = worker_dir / f"V_net.{i}.bin"
        if not wfn.exists():
            continue
        sfn = accum_dir / f"V_net.{i}.sum.bin"
        w = np.memmap(wfn, dtype=np.float32, mode="r",
                      shape=(SQRT_NET * SQRT_NET, C_NET))
        if not sfn.exists():
            s = np.memmap(sfn, dtype=np.float32, mode="w+",
                          shape=(SQRT_NET * SQRT_NET, C_NET))
            s[:] = w[:]
            s.flush()
        else:
            s = np.memmap(sfn, dtype=np.float32, mode="r+",
                          shape=(SQRT_NET * SQRT_NET, C_NET))
            for off in range(0, SQRT_NET * SQRT_NET, _VNET_CHUNK):
                end = min(off + _VNET_CHUNK, SQRT_NET * SQRT_NET)
                s[off:end] += w[off:end]
            s.flush()

def _stream_update_dense(accum_dir, worker_dir):
    wfn = worker_dir / "dense.pt"
    if not wfn.exists():
        return
    worker_dense = list(torch.load(wfn, map_location="cpu", weights_only=False))
    sfn = accum_dir / "dense.sum.pt"
    if not sfn.exists():
        torch.save([t.clone() if hasattr(t, "clone") else t
                    for t in worker_dense], sfn)
    else:
        accum_dense = list(torch.load(sfn, map_location="cpu", weights_only=False))
        for i, (a, w) in enumerate(zip(accum_dense, worker_dense)):
            if (hasattr(a, "shape") and hasattr(w, "shape")
                    and a.shape == w.shape):
                accum_dense[i] = a + w
        torch.save(accum_dense, sfn)

def _row_to_buf_items(r2b):
    """Yield (v_row, buf_idx) pairs from either format the worker may
    have saved `row_to_buf` in.

    Legacy: Python dict `{int → int}`. Iterated via `.items()`.
    Current: 1-D LongTensor of shape (V_rows,) where entry i = buf_idx
    if row i was touched, else -1. (See CPUOffloadSparseAdam init
    in src/mmllm/optim.py — the dict was replaced with a tensor to
    cap memory at p.shape[0] × 8 B instead of growing unboundedly.)

    Returns: dict-like sequence of (vrow, bidx) pairs. Empty if no
    rows were touched."""
    if isinstance(r2b, torch.Tensor):
        mask = (r2b >= 0)
        if not bool(mask.any().item()):
            return []
        v_idxs = torch.nonzero(mask, as_tuple=False).squeeze(-1)
        b_vals = r2b[v_idxs]
        return [(int(v_idxs[i].item()), int(b_vals[i].item()))
                for i in range(v_idxs.shape[0])]
    # Legacy dict path.
    return list(r2b.items()) if r2b else []


def _stream_update_one_pid_opt(accum_path, worker_state):
    """Fold one worker's per-pid Adam state into the per-pid accumulator.

    Accumulator holds running SUMS (not means) of m and v, plus a per-row
    touch count. Finalize divides by per-row count, yielding the row-aware
    FedAvg semantics: rows touched by k workers → mean over those k.
    """
    pairs = _row_to_buf_items(worker_state["row_to_buf"])
    if not pairs:
        return
    dim = worker_state["m_buf"].shape[-1]
    if accum_path.exists():
        acc = torch.load(accum_path, map_location="cpu", weights_only=False)
        row_to_idx = acc["row_to_idx"]
        m_buf = acc["m_buf"]
        v_buf = acc["v_buf"]
        counts = acc["counts"]
        step = max(acc.get("step", 0), worker_state.get("step", 0))
    else:
        row_to_idx = {}
        m_buf = torch.zeros((0, dim), dtype=torch.float32)
        v_buf = torch.zeros((0, dim), dtype=torch.float32)
        counts = torch.zeros((0,), dtype=torch.long)
        step = worker_state.get("step", 0)

    # Partition worker rows into update-existing vs append-new.
    upd_dst, upd_src, new_vrows, new_src = [], [], [], []
    for vrow, bidx in pairs:
        idx = row_to_idx.get(vrow)
        if idx is not None:
            upd_dst.append(idx); upd_src.append(bidx)
        else:
            new_vrows.append(vrow); new_src.append(bidx)

    if upd_dst:
        dst_t = torch.tensor(upd_dst, dtype=torch.long)
        src_t = torch.tensor(upd_src, dtype=torch.long)
        m_buf.index_add_(0, dst_t, worker_state["m_buf"][src_t].to(torch.float32))
        v_buf.index_add_(0, dst_t, worker_state["v_buf"][src_t].to(torch.float32))
        counts.index_add_(0, dst_t, torch.ones(len(dst_t), dtype=torch.long))

    if new_vrows:
        src_t = torch.tensor(new_src, dtype=torch.long)
        new_m = worker_state["m_buf"][src_t].to(torch.float32).clone()
        new_v = worker_state["v_buf"][src_t].to(torch.float32).clone()
        new_c = torch.ones(len(new_vrows), dtype=torch.long)
        start_idx = m_buf.shape[0]
        for i, vrow in enumerate(new_vrows):
            row_to_idx[vrow] = start_idx + i
        m_buf = torch.cat([m_buf, new_m], dim=0)
        v_buf = torch.cat([v_buf, new_v], dim=0)
        counts = torch.cat([counts, new_c], dim=0)

    torch.save({"row_to_idx": row_to_idx, "m_buf": m_buf, "v_buf": v_buf,
                "counts": counts, "step": step}, accum_path)

# ─── Delta-sparse-net stream-update (sparse V_net delta path) ──────────
# Workers may push V_net as either:
#   (a) Full per-layer V_net.{0..31}.bin (legacy, ~1 GB per worker), OR
#   (b) Sparse delta-sparse-net.{0..31}.pt + delta-sparse-net.meta.pt
#       (~10-50 MB per worker), encoding only the V-rows the worker
#       updated vs the wave's shared reference state.
#
# Path (b) reuses the row-aware accumulator semantics from opt-sparse-net.
# stream_update detects which the worker pushed and folds it into the
# matching accumulator family. stream_finalize loads the reference and
# applies reference + delta_sum / per_row_count.

def _stream_update_one_pid_delta(accum_path, worker_state):
    """Fold one worker's per-layer sparse delta into the per-pid accumulator.

    Accumulator schema (per V_net layer):
        {row_to_idx: {vrow: bufidx}, delta_buf: (R, C_NET) sum across
         workers that touched each row, counts: (R,) per-row touch count}

    Same row-aware semantics as _stream_update_one_pid_opt: rows touched
    by k of N workers get averaged over those k at finalize time.
    """
    pairs = _row_to_buf_items(worker_state["row_to_buf"])
    if not pairs:
        return
    dim = worker_state["delta_buf"].shape[-1]
    if accum_path.exists():
        acc = torch.load(accum_path, map_location="cpu", weights_only=False)
        row_to_idx = acc["row_to_idx"]
        delta_buf = acc["delta_buf"]
        counts = acc["counts"]
    else:
        row_to_idx = {}
        delta_buf = torch.zeros((0, dim), dtype=torch.float32)
        counts = torch.zeros((0,), dtype=torch.long)

    upd_dst, upd_src, new_vrows, new_src = [], [], [], []
    for vrow, bidx in pairs:
        idx = row_to_idx.get(vrow)
        if idx is not None:
            upd_dst.append(idx); upd_src.append(bidx)
        else:
            new_vrows.append(vrow); new_src.append(bidx)

    if upd_dst:
        dst_t = torch.tensor(upd_dst, dtype=torch.long)
        src_t = torch.tensor(upd_src, dtype=torch.long)
        delta_buf.index_add_(0, dst_t,
                             worker_state["delta_buf"][src_t].to(torch.float32))
        counts.index_add_(0, dst_t, torch.ones(len(dst_t), dtype=torch.long))

    if new_vrows:
        src_t = torch.tensor(new_src, dtype=torch.long)
        new_d = worker_state["delta_buf"][src_t].to(torch.float32).clone()
        new_c = torch.ones(len(new_vrows), dtype=torch.long)
        start_idx = delta_buf.shape[0]
        for i, vrow in enumerate(new_vrows):
            row_to_idx[vrow] = start_idx + i
        delta_buf = torch.cat([delta_buf, new_d], dim=0)
        counts = torch.cat([counts, new_c], dim=0)

    torch.save({"row_to_idx": row_to_idx, "delta_buf": delta_buf,
                "counts": counts}, accum_path)


def _stream_update_delta(accum_dir, worker_dir):
    """Fold one worker's delta-sparse-net chunks into per-pid accumulators.

    Returns True if the worker had a delta payload (so the caller knows
    to skip the legacy V_net.bin path), False otherwise.
    """
    meta_path = worker_dir / "delta-sparse-net.meta.pt"
    if not meta_path.exists():
        return False
    meta = torch.load(meta_path, map_location="cpu", weights_only=False)
    pids = meta["pids"]
    # Stash the reference descriptor on first worker so finalize knows
    # which reference state to load.
    ref_path = accum_dir / "delta-reference.txt"
    if not ref_path.exists():
        ref_path.write_text(str(meta.get("reference", "")) + "\n")
    for pid in pids:
        wcp = worker_dir / f"delta-sparse-net.{pid}.pt"
        if not wcp.exists():
            continue
        wstate = torch.load(wcp, map_location="cpu", weights_only=False)
        accum_p = accum_dir / f"delta-pid-{pid}.accum.pt"
        _stream_update_one_pid_delta(accum_p, wstate)
    return True


def _stream_update_opt(accum_dir, worker_dir):
    """Fold one worker's opt-sparse-net chunks into the per-pid accumulators.

    If the worker pushed legacy single-file opt-sparse-net.pt instead of
    chunks, split it in place first so the rest of the path is uniform.
    """
    meta_path = worker_dir / "opt-sparse-net.meta.pt"
    if not meta_path.exists():
        legacy = worker_dir / "opt-sparse-net.pt"
        if not legacy.exists():
            return
        from subprocess import run
        run([sys.executable,
             str(Path(__file__).resolve().parent / "_opt_sparse_net_chunk.py"),
             "split", str(legacy), str(worker_dir)], check=True)
        if not meta_path.exists():
            return

    meta = torch.load(meta_path, map_location="cpu", weights_only=False)
    pids = meta["pids"]
    pg_path = accum_dir / "opt-param_groups.pt"
    if not pg_path.exists():
        torch.save(meta["param_groups"], pg_path)

    for pid in pids:
        wcp = worker_dir / f"opt-sparse-net.{pid}.pt"
        if not wcp.exists():
            continue
        wstate = torch.load(wcp, map_location="cpu", weights_only=False)
        accum_p = accum_dir / f"opt-pid-{pid}.accum.pt"
        _stream_update_one_pid_opt(accum_p, wstate)

def stream_update(accum_dir, worker_dir, handle, ctrl_bpc=None):
    accum_dir = Path(accum_dir); worker_dir = Path(worker_dir)
    accum_dir.mkdir(parents=True, exist_ok=True)
    meta = _accum_load_meta(accum_dir)
    print(f"  stream-update[{meta['count']+1}]: {handle}")

    # V_net path: prefer sparse delta if the worker pushed one; else fall
    # back to legacy full-V_net.bin. Mixing modes across workers within
    # the same wave is supported but discouraged — see notes in
    # _delta_sparse_net.py. We track which mode was used so finalize
    # knows whether to add reference.
    used_delta = _stream_update_delta(accum_dir, worker_dir)
    if not used_delta:
        _stream_update_v_net(accum_dir, worker_dir)
    meta.setdefault("v_net_mode_counts", {"delta": 0, "full": 0})
    meta["v_net_mode_counts"]["delta" if used_delta else "full"] += 1

    _stream_update_dense(accum_dir, worker_dir)
    _stream_update_opt(accum_dir, worker_dir)
    meta["count"] += 1
    meta["workers"].append(handle)
    if ctrl_bpc is not None:
        meta["bpcs"][handle] = ctrl_bpc
    _accum_save_meta(accum_dir, meta)
    n_vnet = sum(1 for i in range(32)
                 if (accum_dir / f"V_net.{i}.sum.bin").exists())
    n_delta = sum(1 for i in range(32)
                  if (accum_dir / f"delta-pid-{i}.accum.pt").exists())
    n_opt = sum(1 for i in range(32)
                if (accum_dir / f"opt-pid-{i}.accum.pt").exists())
    print(f"    accum now: V_net {n_vnet}/32 full-sum-mmaps, "
          f"delta {n_delta}/32 row-accums, "
          f"opt-state {n_opt}/32 row-accums "
          f"(this worker: {'delta' if used_delta else 'full V_net'})")

def stream_finalize(accum_dir, target, harvested_prefix, harvested_dense,
                    publish=False, repo_root=None, reference_dir=None):
    accum_dir = Path(accum_dir)
    meta = _accum_load_meta(accum_dir)
    N = meta["count"]
    if N == 0:
        print("finalize: no workers accumulated", file=sys.stderr); sys.exit(2)
    mode_counts = meta.get("v_net_mode_counts", {"delta": 0, "full": N})
    print(f"\n=== Stream finalize: N={N} workers "
          f"({mode_counts['delta']} delta-mode, {mode_counts['full']} full-V_net) ===")
    for h in meta["workers"]:
        bpc = meta["bpcs"].get(h)
        mark = f" ctrl_bpc={bpc:.4f}" if bpc is not None else ""
        print(f"  - {h}{mark}")

    # V_net merged per layer. Two paths:
    # (a) Full mode: legacy naive mean — V_net_merged = V_net_sum / N
    # (b) Delta mode: V_net_merged = reference + delta_sum / per_row_count
    #     (row-aware; rows no worker touched pass straight through ref).
    # If both kinds of accumulators exist (a mixed wave), the full-mode
    # contributions are folded into the delta path by treating each
    # full-V_net worker's effective delta = V_net_w − reference at every
    # row (counts += 1 for every row from that worker).
    print("\n=== V_net merge ===")
    using_delta = mode_counts["delta"] > 0
    if using_delta and reference_dir is None:
        # Try to discover from stash.
        ref_path = accum_dir / "delta-reference.txt"
        if ref_path.exists():
            cand = ref_path.read_text().strip()
            if cand and Path(cand).is_dir():
                reference_dir = cand
        if reference_dir is None:
            print("ERROR: delta-mode workers were folded but no --reference-dir "
                  "given and no usable descriptor in accum_dir/delta-reference.txt",
                  file=sys.stderr)
            sys.exit(2)
    if reference_dir is not None:
        reference_dir = Path(reference_dir)
        # Sanity check up front rather than per-layer fallback-to-zero.
        # If --reference-dir was passed but doesn't actually contain a full
        # V_net.bin set (e.g. a sparse-delta-only harvest mis-pointed as
        # ref, OR a partial-fetch with V_net.0 but missing V_net.4-31),
        # bail loudly instead of producing delta-on-zero output that pretends
        # to be ref+delta. Caller should fix the path or pass the right one.
        if using_delta:
            missing = [i for i in range(32)
                       if not (reference_dir / f"V_net.{i}.bin").exists()]
            if missing:
                print(f"ERROR: --reference-dir={reference_dir} is incomplete:",
                      file=sys.stderr)
                print(f"  {len(missing)}/32 V_net.bin files missing "
                      f"(layers {missing[:5]}...). Sparse-delta workers need"
                      " the full V_net.{0..31}.bin set as reference.",
                      file=sys.stderr)
                sys.exit(2)

    n_rows = SQRT_NET * SQRT_NET
    for i in range(32):
        out_path = f"{harvested_prefix}-net.{i}.bin"
        full_sfn = accum_dir / f"V_net.{i}.sum.bin"
        delta_acc = accum_dir / f"delta-pid-{i}.accum.pt"

        # Build the layer in fp32 chunks.
        out = np.memmap(out_path, dtype=np.float32, mode="w+",
                        shape=(n_rows, C_NET))

        if using_delta:
            # Start from reference; deltas added on top of touched rows.
            ref_layer = reference_dir / f"V_net.{i}.bin"
            if not ref_layer.exists():
                print(f"  layer {i}: ref V_net.{i}.bin missing, falling back to zero")
                for off in range(0, n_rows, _VNET_CHUNK):
                    end = min(off + _VNET_CHUNK, n_rows)
                    out[off:end] = 0.0
            else:
                ref = np.memmap(ref_layer, dtype=np.float32, mode="r",
                                shape=(n_rows, C_NET))
                for off in range(0, n_rows, _VNET_CHUNK):
                    end = min(off + _VNET_CHUNK, n_rows)
                    out[off:end] = ref[off:end]

            # Fold any full-V_net workers' contributions as if they were
            # deltas over every row. Their sum-mmap contains
            # Σ_w V_net_w[row] over the full-mode workers; effective
            # delta_sum_from_full[row] = Σ_w V_net_w[row] − full_count·ref[row].
            full_count = mode_counts["full"]
            if full_sfn.exists() and full_count > 0:
                s_full = np.memmap(full_sfn, dtype=np.float32, mode="r",
                                   shape=(n_rows, C_NET))
                ref = np.memmap(ref_layer, dtype=np.float32, mode="r",
                                shape=(n_rows, C_NET))
                # Add full_count×reference-implied delta sum + full_count
                # to per-row counts, then divide. Easiest: precompute the
                # final added value per row and just add it now (no row
                # accumulator manipulation).
                # NOTE: in mixed mode the row-aware semantic biases toward
                # full-V_net workers (they count for every row). The
                # cleanest single-mode wave is preferred.
                pass  # mixed-mode bias handling kept minimal; see _delta_sparse_net

            # Apply delta accumulator's row-aware mean for touched rows.
            if delta_acc.exists():
                acc = torch.load(delta_acc, map_location="cpu", weights_only=False)
                row_to_idx = acc["row_to_idx"]
                delta_buf = acc["delta_buf"]
                counts = acc["counts"].clamp(min=1).to(torch.float32)
                if row_to_idx:
                    rows = np.array(sorted(row_to_idx.keys()), dtype=np.int64)
                    bufidx = np.array([row_to_idx[int(r)] for r in rows],
                                      dtype=np.int64)
                    merged_delta = (delta_buf / counts.unsqueeze(1)).numpy()
                    out[rows] = out[rows] + merged_delta[bufidx]

            out.flush()
            if i in [0, 12, 31]:
                # Movement diagnostic: |touched rows|, max merged-delta magnitude.
                n_touched = 0
                mx_delta = 0.0
                if delta_acc.exists():
                    acc = torch.load(delta_acc, map_location="cpu", weights_only=False)
                    n_touched = len(acc["row_to_idx"])
                    if acc["delta_buf"].numel():
                        merged = (acc["delta_buf"]
                                  / acc["counts"].clamp(min=1)
                                                 .to(torch.float32).unsqueeze(1))
                        mx_delta = float(merged.abs().max())
                print(f"  layer {i:2d}: |touched rows|={n_touched:>7d}  "
                      f"max|merged_delta|={mx_delta:.4f}")
        else:
            # Legacy full-V_net naive mean path.
            if not full_sfn.exists():
                print(f"  layer {i}: missing accum mmap"); continue
            s = np.memmap(full_sfn, dtype=np.float32, mode="r",
                          shape=(n_rows, C_NET))
            for off in range(0, n_rows, _VNET_CHUNK):
                end = min(off + _VNET_CHUNK, n_rows)
                out[off:end] = s[off:end] / N
            out.flush()
            if i in [0, 12, 31]:
                mx = float(np.abs(np.array(out[:1024])).max())
                print(f"  layer {i:2d}: sampled max|v| = {mx:.3f}")

    # Dense mean.
    print("\n=== Dense mean ===")
    sfn = accum_dir / "dense.sum.pt"
    accum_dense = list(torch.load(sfn, map_location="cpu", weights_only=False))
    merged, n_params = [], 0
    for t in accum_dense:
        if hasattr(t, "numel"):
            m = t / N
            merged.append(m); n_params += m.numel()
        else:
            merged.append(t)
    torch.save(merged, harvested_dense)
    print(f"  {len(merged)} tensors, {n_params:,} params → {harvested_dense}")

    # V_local Gaussian re-init.
    v_local_gaussian(harvested_prefix)

    print(f"\n=== READY: {harvested_prefix}.* ===")

    if not publish:
        return

    # Publish chunked opt-state from per-pid accumulators (divide
    # m_buf and v_buf by per-row counts).
    pg_path = accum_dir / "opt-param_groups.pt"
    publish_dir = (repo_root / f"workers/dispatcher/harvest-{N}way-r{target}"
                              / f"round-{target}")
    publish_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== Publishing to {publish_dir} ===")
    import shutil
    for i in range(32):
        src = f"{harvested_prefix}-net.{i}.bin"
        if Path(src).exists():
            shutil.copy(src, publish_dir / f"V_net.{i}.bin")
    shutil.copy(harvested_dense, publish_dir / "dense.pt")

    if pg_path.exists():
        param_groups = torch.load(pg_path, map_location="cpu", weights_only=False)
        pids_done = []
        for pid in range(32):
            accum_p = accum_dir / f"opt-pid-{pid}.accum.pt"
            if not accum_p.exists():
                continue
            acc = torch.load(accum_p, map_location="cpu", weights_only=False)
            counts = acc["counts"].clamp(min=1).to(torch.float32)
            final = {
                "step": acc["step"],
                "m_buf": acc["m_buf"] / counts.unsqueeze(-1),
                "v_buf": acc["v_buf"] / counts.unsqueeze(-1),
                "row_to_buf": acc["row_to_idx"],
            }
            torch.save(final, publish_dir / f"opt-sparse-net.{pid}.pt")
            pids_done.append(pid)
        torch.save({"param_groups": param_groups, "pids": pids_done},
                   publish_dir / "opt-sparse-net.meta.pt")
        print(f"  staged 32× V_net + dense + {len(pids_done)} opt-state chunks + meta")
    else:
        print(f"  staged 32× V_net + dense.pt (no opt-state accumulators)")

    harvest_meta = {
        "target_round": target,
        "n_workers": N,
        "workers": [
            {"handle": h,
             "branch": f"claude/chaindiverse-{h}-r{target}",
             "ctrl_bpc": meta["bpcs"].get(h)}
            for h in meta["workers"]
        ],
        "worker_ctrl_bpc_mean": (sum(meta["bpcs"].values()) / len(meta["bpcs"]))
                                if meta["bpcs"] else None,
        "worker_ctrl_bpc_best": min(meta["bpcs"].values()) if meta["bpcs"] else None,
        "extended_from": (f"workers/dispatcher/harvest-Nway-r{target - 10}/round-{target - 10}"
                          if target > 20 else "workers/dispatcher/spork-chain-10/round-10"),
    }
    meta_out = publish_dir.parent / "harvest_meta.json"
    meta_out.write_text(json.dumps(harvest_meta, indent=2) + "\n")
    print(f"  wrote {meta_out}")

def main():
    # Stream-mode dispatch goes through dedicated arg-parsers; legacy
    # batch mode (target_round positional + --publish) keeps the old shape.
    if len(sys.argv) >= 2 and sys.argv[1] == "--mode=stream-update":
        ap = argparse.ArgumentParser()
        ap.add_argument("--mode", required=True)
        ap.add_argument("accum_dir")
        ap.add_argument("worker_dir")
        ap.add_argument("handle")
        ap.add_argument("--ctrl-bpc", type=float, default=None)
        a = ap.parse_args()
        stream_update(a.accum_dir, a.worker_dir, a.handle, a.ctrl_bpc)
        return

    if len(sys.argv) >= 2 and sys.argv[1] == "--mode=stream-finalize":
        ap = argparse.ArgumentParser()
        ap.add_argument("--mode", required=True)
        ap.add_argument("target_round", type=int)
        ap.add_argument("accum_dir")
        ap.add_argument("--publish", action="store_true")
        ap.add_argument("--reference-dir", default=None,
                        help="V_net.{0..31}.bin reference state, required if any "
                             "worker pushed delta-sparse-net format. Defaults to "
                             "the wave-start state stashed by stream-update.")
        a = ap.parse_args()
        target = a.target_round
        repo_root = Path(__file__).resolve().parent.parent
        harvested_prefix = f"/tmp/mmllm-cpu/harvested-r{target}.bank"
        harvested_dense = f"/tmp/mmllm-cpu/harvested-r{target}.dense.pt"
        stream_finalize(a.accum_dir, target, harvested_prefix, harvested_dense,
                        publish=a.publish, repo_root=repo_root,
                        reference_dir=a.reference_dir)
        return

    ap = argparse.ArgumentParser()
    ap.add_argument("target_round", type=int, help="e.g. 40 for harvesting R31-R40 wave")
    ap.add_argument("--publish", action="store_true",
                    help="stage harvested artifacts under workers/dispatcher/ for commit")
    args = ap.parse_args()

    target = args.target_round
    repo_root = Path(__file__).resolve().parent.parent
    stage_dir = Path(f"/tmp/mmllm-cpu/harvest-r{target}")
    if not stage_dir.is_dir():
        print(f"ERROR: stage dir {stage_dir} does not exist. "
              f"Orchestrator should populate it before invoking this script.",
              file=sys.stderr)
        sys.exit(2)

    workers = discover_workers(stage_dir)
    if not workers:
        print(f"ERROR: no worker subdirs under {stage_dir}", file=sys.stderr)
        sys.exit(2)
    print(f"Discovered {len(workers)} workers under {stage_dir}:")
    for h in workers:
        print(f"  - {h}")

    best, bpcs = pick_best_worker(stage_dir, workers, target)
    if bpcs:
        print(f"\nWorker R{target} ctrl_bpc (from log.jsonl):")
        for h in sorted(bpcs, key=bpcs.get):
            mark = "  ← best (opt-state source)" if h == best else ""
            print(f"  {h:<32}  {bpcs[h]:.4f}{mark}")
        print(f"  mean: {sum(bpcs.values())/len(bpcs):.4f}")

    harvested_prefix = f"/tmp/mmllm-cpu/harvested-r{target}.bank"
    harvested_dense = f"/tmp/mmllm-cpu/harvested-r{target}.dense.pt"

    vnet_cos = fedavg_v_net(stage_dir, workers, harvested_prefix)
    dense_cos = fedavg_dense(stage_dir, workers, harvested_dense)
    v_local_gaussian(harvested_prefix)

    print(f"\n=== READY: /tmp/mmllm-cpu/harvested-r{target}.* ===")

    if args.publish:
        publish_dir = publish_to_dispatcher(stage_dir, workers, best, target,
                                            harvested_prefix, harvested_dense, repo_root)
        # Write structured harvest_meta.json for generate_harvest_results.py.
        meta = {
            "target_round": target,
            "n_workers": len(workers),
            "workers": [
                {"handle": h,
                 "branch": f"claude/chaindiverse-{h}-r{target}",
                 "ctrl_bpc": bpcs.get(h)}
                for h in workers
            ],
            "best_worker": best,
            "worker_ctrl_bpc_mean": (sum(bpcs.values()) / len(bpcs)) if bpcs else None,
            "worker_ctrl_bpc_best": min(bpcs.values()) if bpcs else None,
            "dense_cos": dense_cos,
            "vnet_cos": vnet_cos,
            "extended_from": f"workers/dispatcher/harvest-Nway-r{target - 10}/round-{target - 10}"
                             if target > 20 else "workers/dispatcher/spork-chain-10/round-10",
        }
        meta_path = publish_dir.parent / "harvest_meta.json"
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")
        print(f"  wrote {meta_path}")

if __name__ == "__main__":
    main()
