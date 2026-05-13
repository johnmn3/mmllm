"""Generic N-way FedAvg harvest of chain-diverse worker endpoints.

Replaces the per-round harvest_5way_r${N}.py scripts. Takes a target
round number, auto-discovers worker handles from the staging dir, runs
FedAvg on V_net + dense, picks best worker's opt-state, and writes
harvested artifacts to two places:

  1. /tmp/mmllm-cpu/harvested-r${TARGET}.{dense.pt,bank-net.*.bin,bank.*.bin}
     — for the verify+battery step
  2. (optionally) workers/dispatcher/harvest-${N}way-r${TARGET}/round-${TARGET}/
     — published starting state for the next dispatch wave

Worker layout expected at staging dir (orchestrator populates this):
  /tmp/mmllm-cpu/harvest-r${TARGET}/<handle>/
    V_net.{0..31}.bin
    dense.pt
    opt-sparse-net.pt
    round-${TARGET}.log.jsonl   (optional, used for best-worker pick)

Usage:
  python3 scripts/harvest_chain.py <target_round> [--publish]

  --publish: also stage the harvested artifacts into workers/dispatcher/
             so they're committable.
"""
import argparse, json, os, sys, numpy as np, torch
from pathlib import Path

SQRT_NET, C_NET = 64, 8
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

def publish_to_dispatcher(stage_dir, workers, best_handle, target_round,
                          harvested_prefix, harvested_dense, repo_root):
    """Copy harvested V_net + dense + best-worker's opt-state under
    workers/dispatcher/harvest-${N}way-r${TARGET}/round-${TARGET}/.
    Returns the path to round-${TARGET}/."""
    n = len(workers)
    publish_dir = repo_root / f"workers/dispatcher/harvest-{n}way-r{target_round}" / f"round-{target_round}"
    publish_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== Publishing to {publish_dir} ===")
    import shutil
    for i in range(32):
        shutil.copy(f"{harvested_prefix}-net.{i}.bin",
                    publish_dir / f"V_net.{i}.bin")
    shutil.copy(harvested_dense, publish_dir / "dense.pt")
    shutil.copy(stage_dir / best_handle / "opt-sparse-net.pt",
                publish_dir / "opt-sparse-net.pt")
    print(f"  staged 32× V_net + dense.pt + {best_handle}'s opt-sparse-net.pt")
    return publish_dir

def main():
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
