"""Load the R30 5-way harvested state, run eval_bpc on Glaive val.

Stages the harvested-r30 artifacts into /tmp/mmllm-cpu/inf-spork-r30.{fim,bank}
format so eval_battery can target them via MMLLM_INF_BASE / MMLLM_INF_BANK
env vars (or a parallel r30 script)."""
import os, shutil, sys, torch, time
os.environ.setdefault("MMLLM_ENABLE_PKM_CPP", "true")
os.environ.setdefault("MMLLM_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NET_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NETBANK_ENABLED", "true")
os.environ.setdefault("MMLLM_LONG_TIER_MIX", "switch")
os.environ.setdefault("MMLLM_ALPHA_NET", "true")
os.environ.setdefault("MMLLM_GATE_NET_DEFAULT", "true")
os.environ.setdefault("MMLLM_NET_SQRT_N", "64")
os.environ.setdefault("MMLLM_NET_C_NET", "8")
os.environ.setdefault("MMLLM_NET_TOP_K", "64")
os.environ.setdefault("MMLLM_NET_SUB_TOP_K", "8")

from mmllm._entry import _patch_torch
_patch_torch()
from basilisp.main import init
init()

import mmllm.core as core
import mmllm.corpus as corp
import basilisp.lang.keyword as bkw
from pathlib import Path

def K(s): return bkw.keyword(s)

# Stage harvested into inf-spork-r30.* layout
SRC_DENSE = "/tmp/mmllm-cpu/harvested5-r30.dense.pt"
SRC_BANK_PREFIX = "/tmp/mmllm-cpu/harvested5-r30.bank"  # .{i}.bin + -net.{i}.bin
INF_BASE = "/tmp/mmllm-cpu/inf-spork-r30.fim"
INF_BANK = "/tmp/mmllm-cpu/inf-spork-r30.bank"

ckpt_dir = Path(f"{INF_BASE}.ckpts/step-1")
ckpt_dir.mkdir(parents=True, exist_ok=True)
shutil.copy(SRC_DENSE, ckpt_dir / "dense.pt")
print(f"staged dense → {ckpt_dir/'dense.pt'}")

# bank files - copy/symlink mmaps
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
for i in range(32):
    src = f"{SRC_BANK_PREFIX}-net.{i}.bin"
    dst = f"{INF_BANK}-net.{i}.bin"
    if os.path.exists(dst): os.remove(dst)
    os.symlink(src, dst)
for i in LOCAL_LAYERS:
    src = f"{SRC_BANK_PREFIX}.{i}.bin"
    dst = f"{INF_BANK}.{i}.bin"
    if os.path.exists(dst): os.remove(dst)
    os.symlink(src, dst)
print(f"staged 32 V_net + 8 V_local symlinks → {INF_BANK}.*")

# Build the model
cfg = core.default_config_cpu_mini
cfg = cfg.assoc(K("memory-mmap-path"), INF_BANK)
cfg = cfg.assoc(K("device"), "cpu")
cfg = cfg.assoc(K("bank-on-gpu"), False)
cfg = cfg.assoc(K("net-bank-on-gpu"), False)

print("\nLoading harvested R30 cpu-mini …")
m = core.build_model(cfg)
saved = list(torch.load(f"{INF_BASE}.ckpts/step-1/dense.pt", map_location="cpu", weights_only=False))
for p, s in zip(core.parameters(m), saved):
    if p.data.shape == s.shape:
        p.data.copy_(s)
core.set_eval_mode__BANG__(m)
torch.set_grad_enabled(False)

# eval Glaive val
print("\nEvaluating on Glaive val …")
glaive_val = corp.load_as_tensor("/tmp/mmllm-cpu/fim-json-v3.val.bin")
t0 = time.time()
r = core.eval_bpc(m, glaive_val, 128, 16, 100_000)
print(f"  glaive-fim-val: bpc={r.val_at(K('bpc')):.4f}  ppl={r.val_at(K('ppl')):.4f}  wall={time.time()-t0:.1f}s")
print(f"\n  R20-harvest baseline: 1.4813 / 2.79")
print(f"  best worker R30:      1.2492 / 2.27 (opus47)")
print(f"  mean worker R30:      1.2826 / 2.36")
