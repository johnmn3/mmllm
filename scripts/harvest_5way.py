"""FedAvg the 4 workers' round-20 endpoints into a single harvested
bank + dense, then build an inf-spork from it and report bpc."""
import os, numpy as np, torch, json

WORKERS = ["opus47-may13", "round11to20", "claude-ext", "opus47"]
BASE = "/tmp/mmllm-cpu/harvest5"
OUT_BANK = "/tmp/mmllm-cpu/harvested5.bank"
OUT_DENSE = "/tmp/mmllm-cpu/harvested5.dense.pt"

SQRT_NET, C_NET = 64, 8

# Workers' published round-20 endpoint metrics (from their reports)
worker_end_bpc = {
    "opus47-may13": 1.2260,
    "round11to20":  1.2241,
    "claude-ext":   1.2231,
    "opus47":       1.2245,
}
print(f"4 workers, all extended dispatcher's round-10 (ctrl 1.5991) → round-20:")
for h, b in worker_end_bpc.items():
    print(f"  {h:<14}  reported ctrl={b:.4f}")

# --- FedAvg V_net (32 layers, 4-way average)
print(f"\n=== FedAvg V_net across {len(WORKERS)} workers ===")
for i in range(32):
    stacks = []
    for h in WORKERS:
        path = f"{BASE}/{h}/V_net.{i}.bin"
        v = np.array(np.memmap(path, dtype=np.float32, mode="r", shape=(SQRT_NET*SQRT_NET, C_NET)))
        stacks.append(v)
    merged = np.mean(stacks, axis=0).astype(np.float32)
    out = np.memmap(f"{OUT_BANK}-net.{i}.bin", dtype=np.float32, mode="w+", shape=(SQRT_NET*SQRT_NET, C_NET))
    out[:] = merged; out.flush()
    if i in [0, 12, 31]:
        # Pairwise cosine between worker V_nets (gauge of state similarity)
        cos_pair = []
        for j in range(len(WORKERS)):
            for k in range(j+1, len(WORKERS)):
                vj, vk = stacks[j].ravel(), stacks[k].ravel()
                c = float(vj @ vk / (np.linalg.norm(vj)*np.linalg.norm(vk) + 1e-20))
                cos_pair.append(c)
        print(f"  layer {i}: max|v| individual = [{', '.join(f'{np.abs(s).max():.3f}' for s in stacks)}]")
        print(f"           merged max|v| = {np.abs(merged).max():.3f}")
        print(f"           pairwise cos mean = {np.mean(cos_pair):.4f}, range=[{min(cos_pair):.4f}, {max(cos_pair):.4f}]")

# --- FedAvg dense.pt
print(f"\n=== FedAvg dense.pt across {len(WORKERS)} workers ===")
worker_dense = [torch.load(f"{BASE}/{h}/dense.pt", map_location="cpu", weights_only=False) for h in WORKERS]
assert all(len(d) == len(worker_dense[0]) for d in worker_dense), "dense.pt tensor count mismatch"
merged = []
for tensors_at_i in zip(*worker_dense):
    if hasattr(tensors_at_i[0], "shape") and all(t.shape == tensors_at_i[0].shape for t in tensors_at_i):
        merged.append(torch.stack(tensors_at_i).mean(0))
    else:
        merged.append(tensors_at_i[0])
print(f"  averaged {len(merged)} tensors, {sum(t.numel() for t in merged if hasattr(t, 'numel')):,} total params")
# Pairwise cosine on the flattened dense
def flat(ts):
    return torch.cat([t.flatten() for t in ts if hasattr(t, "flatten")])
flats = [flat(d) for d in worker_dense]
cos_d = []
for j in range(len(WORKERS)):
    for k in range(j+1, len(WORKERS)):
        c = float(torch.dot(flats[j], flats[k]) / (flats[j].norm() * flats[k].norm() + 1e-20))
        cos_d.append(c)
print(f"  dense pairwise cos mean = {np.mean(cos_d):.4f}, range=[{min(cos_d):.4f}, {max(cos_d):.4f}]")
torch.save(merged, OUT_DENSE)
print(f"  wrote {OUT_DENSE} ({os.path.getsize(OUT_DENSE)/1e6:.2f} MB)")

# V_local Gaussian-fresh
print("\n=== V_local Gaussian-init ===")
SQRT_LOCAL, Q_DIM = 226, 16
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
N_TRUNKS = 16
n_local = N_TRUNKS * SQRT_LOCAL * SQRT_LOCAL
rng = np.random.default_rng(0)
for i in LOCAL_LAYERS:
    a = np.memmap(f"{OUT_BANK}.{i}.bin", dtype=np.float32, mode="w+", shape=(n_local, Q_DIM))
    CHUNK = 4096
    for s in range(0, n_local, CHUNK):
        e = min(s + CHUNK, n_local)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * 0.02).astype(np.float32)
    a.flush()
print(f"  8 layers × {N_TRUNKS} trunks, q_dim={Q_DIM}")

print(f"\n=== READY: /tmp/mmllm-cpu/harvested5.* ===")
