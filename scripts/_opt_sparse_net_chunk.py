"""Split / merge / fedavg opt-sparse-net.pt across V_net layers.

opt-sparse-net.pt at design-sized V_net (sqrt_n=1024 c_net=8) is ~230 MB —
over GitHub's 100 MB per-file limit. The state_dict has one entry per
V_net layer (32 layers); per-layer sizes are 2-13 MB. Splitting per-pid
keeps each artifact well under the limit and naturally aligns with the
per-layer FedAvg the harvester already does on V_net.

CPUOffloadSparseAdam state_dict shape (per pid):
    {"step": int, "m_buf": (R, dim), "v_buf": (R, dim),
     "row_to_buf": {vrow: bufidx}}
where R = unique V-rows that worker touched, dim = c_net.

Per-pid FedAvg semantics:
- Union all workers' touched V-rows for this layer.
- For each unioned row, sum m_buf and v_buf across the workers that
  TOUCHED it, divide by the touch-count for that row. (Row touched by
  one worker → that worker's moments; touched by all → ordinary mean.
  Workers that didn't touch the row contribute nothing — averaging in
  zero moments would damp the EMA falsely.)
- step: max across workers (same recipe → same value modulo races).

File layout in a chunk dir:
    opt-sparse-net.meta.pt     -- {"param_groups": [...], "pids": [...]}
    opt-sparse-net.<pid>.pt    -- per-layer state subdict (one per pid)

Usage:
    python3 _opt_sparse_net_chunk.py split <in.pt> <out_dir>
    python3 _opt_sparse_net_chunk.py merge <in_dir> <out.pt>
    python3 _opt_sparse_net_chunk.py fedavg <out_dir> <in_dir_1> <in_dir_2> ...
"""
import os, sys, torch

PREFIX = "opt-sparse-net"

def _meta_path(d):  return f"{d}/{PREFIX}.meta.pt"
def _pid_path(d, p): return f"{d}/{PREFIX}.{p}.pt"

def split(in_path, out_dir):
    sd = torch.load(in_path, map_location="cpu", weights_only=False)
    os.makedirs(out_dir, exist_ok=True)
    state = sd.get("state", {}) if isinstance(sd, dict) else {}
    param_groups = sd.get("param_groups", []) if isinstance(sd, dict) else []
    pids = sorted(state.keys())
    torch.save({"param_groups": param_groups, "pids": pids}, _meta_path(out_dir))
    sizes = []
    for pid in pids:
        p = _pid_path(out_dir, pid)
        torch.save(state[pid], p)
        sizes.append(os.path.getsize(p))
    if pids:
        print(f"split: {len(pids)} chunks, sizes={min(sizes)/1e6:.2f}-{max(sizes)/1e6:.2f} MB, "
              f"total={sum(sizes)/1e6:.1f} MB → {out_dir}")
    else:
        print(f"split: input was empty/non-Adam; wrote empty meta only → {out_dir}")

def merge(in_dir, out_path):
    meta_p = _meta_path(in_dir)
    if not os.path.exists(meta_p):
        print(f"merge: no meta at {meta_p}", file=sys.stderr); sys.exit(2)
    meta = torch.load(meta_p, map_location="cpu", weights_only=False)
    sd = {"param_groups": meta["param_groups"], "state": {}}
    for pid in meta["pids"]:
        sd["state"][pid] = torch.load(_pid_path(in_dir, pid),
                                       map_location="cpu", weights_only=False)
    torch.save(sd, out_path)
    print(f"merge: {len(meta['pids'])} chunks → {out_path} "
          f"({os.path.getsize(out_path)/1e6:.1f} MB)")

def _fedavg_one_pid(states):
    """Row-aware FedAvg of one pid's state across N workers.

    states: list of per-worker dicts {step, m_buf, v_buf, row_to_buf}.
    Returns a merged dict in the same shape.
    """
    union_rows = sorted({vrow for s in states for vrow in s["row_to_buf"].keys()})
    new_r2b = {vrow: i for i, vrow in enumerate(union_rows)}
    dim = states[0]["m_buf"].shape[-1] if states[0]["m_buf"].numel() else \
          states[0]["v_buf"].shape[-1]
    R = len(union_rows)
    new_m = torch.zeros((R, dim), dtype=torch.float32)
    new_v = torch.zeros((R, dim), dtype=torch.float32)
    counts = torch.zeros((R,), dtype=torch.float32)
    for s in states:
        if not s["row_to_buf"]:
            continue
        # Build row_idx → new_idx tensor for vectorised gather/scatter.
        vrows = list(s["row_to_buf"].keys())
        bufidxs = list(s["row_to_buf"].values())
        new_idxs = torch.tensor([new_r2b[v] for v in vrows], dtype=torch.long)
        src_idxs = torch.tensor(bufidxs, dtype=torch.long)
        new_m.index_add_(0, new_idxs, s["m_buf"][src_idxs].to(torch.float32))
        new_v.index_add_(0, new_idxs, s["v_buf"][src_idxs].to(torch.float32))
        counts.index_add_(0, new_idxs, torch.ones((len(new_idxs),), dtype=torch.float32))
    # Avoid div-by-zero on rows with count 0 (shouldn't happen by construction).
    counts.clamp_(min=1.0)
    new_m.div_(counts.unsqueeze(-1))
    new_v.div_(counts.unsqueeze(-1))
    step = max((s.get("step", 0) for s in states), default=0)
    return {"step": step, "m_buf": new_m, "v_buf": new_v, "row_to_buf": new_r2b}

def fedavg(out_dir, in_dirs):
    """Combine N workers' chunk dirs into one merged chunk set.

    Per-layer: row-aware FedAvg (union of touched rows, per-row mean over
    workers that touched it). param_groups taken from worker 0 (identical
    across workers by construction).
    """
    if len(in_dirs) < 1:
        print("fedavg: need at least 1 input dir", file=sys.stderr); sys.exit(2)
    metas = [torch.load(_meta_path(d), map_location="cpu", weights_only=False)
             for d in in_dirs]
    pids_per = [set(m["pids"]) for m in metas]
    common = sorted(set.intersection(*pids_per)) if pids_per else []
    if not common:
        print("fedavg: no common pids across workers", file=sys.stderr); sys.exit(2)
    # Warn if any worker had pids the others didn't (shouldn't happen at
    # design-sized 32-layer V_net but be loud if so).
    all_pids = set.union(*pids_per)
    extra = all_pids - set(common)
    if extra:
        print(f"fedavg: WARN — pids present in only some workers, dropping: {sorted(extra)}",
              file=sys.stderr)

    os.makedirs(out_dir, exist_ok=True)
    torch.save({"param_groups": metas[0]["param_groups"], "pids": common},
               _meta_path(out_dir))
    print(f"fedavg: {len(in_dirs)} workers × {len(common)} layers")
    total_in = 0
    total_out = 0
    for pid in common:
        states = [torch.load(_pid_path(d, pid), map_location="cpu",
                             weights_only=False) for d in in_dirs]
        for d, s in zip(in_dirs, states):
            total_in += sum(t.numel() * t.element_size() for t in
                            (s.get("m_buf"), s.get("v_buf")) if t is not None)
        merged = _fedavg_one_pid(states)
        out_p = _pid_path(out_dir, pid)
        torch.save(merged, out_p)
        total_out += os.path.getsize(out_p)
        union_R = merged["m_buf"].shape[0]
        per_R = [s["m_buf"].shape[0] for s in states]
        print(f"  layer {pid:2d}: rows per-worker={per_R}  union={union_R}  "
              f"out={os.path.getsize(out_p)/1e6:.2f} MB")
    print(f"fedavg: total input ~{total_in/1e6:.1f} MB, merged ~{total_out/1e6:.1f} MB → {out_dir}")

def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "split" and len(sys.argv) == 4:
        split(sys.argv[2], sys.argv[3])
    elif cmd == "merge" and len(sys.argv) == 4:
        merge(sys.argv[2], sys.argv[3])
    elif cmd == "fedavg" and len(sys.argv) >= 4:
        fedavg(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__, file=sys.stderr); sys.exit(1)

if __name__ == "__main__":
    main()
