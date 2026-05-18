"""Run the BPC battery on the harvested cpu-mini model.

For each test.bin under /tmp/mmllm-cpu/battery/, compute byte-level
cross-entropy on a fixed-token cap. Reports per-dataset + overall.

Agentic-style scoring (format-validity, tool-name-match, tool-args-match
on commitpackft / xlam) requires paired (prompt, gold) JSONL which the
prepare-hf-dataset path doesn't produce — to be added separately.

Usage:
    MMLLM_ENABLE_PKM_CPP=true python3 scripts/run_eval_battery.py
"""
import os, sys, torch, time
os.environ.setdefault("MMLLM_ENABLE_PKM_CPP", "true")
os.environ.setdefault("MMLLM_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NET_BANK_ON_GPU", "false")
os.environ.setdefault("MMLLM_NETBANK_ENABLED", "true")
os.environ.setdefault("MMLLM_LONG_TIER_MIX", "switch")
os.environ.setdefault("MMLLM_ALPHA_NET", "true")
os.environ.setdefault("MMLLM_GATE_NET_DEFAULT", "true")
os.environ.setdefault("MMLLM_NET_SQRT_N", "1024")
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

# Paths can be overridden via env vars so this script handles any harvest
# (R20, R30, R40, ...). Defaults preserve the original cpu-mini harvest path.
INF_BASE = os.environ.get("MMLLM_INF_BASE", "/tmp/mmllm-cpu/inf-spork.fim")
INF_BANK = os.environ.get("MMLLM_INF_BANK", "/tmp/mmllm-cpu/inf-spork.bank")
OUT_JSONL = os.environ.get("MMLLM_BATTERY_OUT", "workers/dispatcher/harvest-5way/eval_battery.jsonl")
BATTERY = "/tmp/mmllm-cpu/battery"
EVAL_TOKEN_CAP = 100_000   # bytes per dataset eval
SEQ_LEN = 128
B = 16

# Datasets in the battery + their notes. Stars mark non-gated substitutes
# for default_eval_battery items that were inaccessible on this sandbox.
DATASETS = [
    ("cosmopedia",       "synthetic English textbook (BPC)"),
    ("fineweb-edu",      "curated English web (BPC)"),
    ("magicoder",        "* Python instruction code (replaces the-stack-v2-py)"),
    ("hermes-funcall",   "* function-call corpus (replaces xlam — Hermes)"),
    ("toolace",          "* function-call corpus (replaces xlam — ToolACE)"),
    ("tiny-stories",     "TinyStories — simple English grammar"),
    ("aesop-fables",     "in-house aesop-fables (Clojure code + JSON tool-calls)"),
    ("open-web-math",    "OpenWebMath — math reasoning (proofs, math.SE, lecture notes)"),
]

# Build the model
cfg = core.default_config_cpu_mini
cfg = cfg.assoc(K("memory-mmap-path"), INF_BANK)
cfg = cfg.assoc(K("device"), "cpu")
cfg = cfg.assoc(K("bank-on-gpu"), False)
cfg = cfg.assoc(K("net-bank-on-gpu"), False)

print("Loading harvested cpu-mini model …")
m = core.build_model(cfg)
saved = list(torch.load(f"{INF_BASE}.ckpts/step-1/dense.pt", map_location="cpu", weights_only=False))
for p, s in zip(core.parameters(m), saved):
    if p.data.shape == s.shape:
        p.data.copy_(s)
core.set_eval_mode__BANG__(m)
torch.set_grad_enabled(False)

# Reference: in-domain Glaive FIM (skip gracefully when corpus isn't built)
glaive = None
glaive_path = Path("/tmp/mmllm-cpu/fim-json-v3.val.bin")
if glaive_path.exists():
    print("\nWarmup: in-domain Glaive FIM val …")
    glaive_val = corp.load_as_tensor(str(glaive_path))
    t0 = time.time()
    glaive = core.eval_bpc(m, glaive_val, SEQ_LEN, B, EVAL_TOKEN_CAP)
    print(f"  glaive-fim-val: bpc={glaive.val_at(K('bpc')):.4f} ppl={glaive.val_at(K('ppl')):.4f}  wall={time.time()-t0:.1f}s")
else:
    print(f"\nWarmup: in-domain Glaive FIM val SKIPPED ({glaive_path} not on disk)")
    print("  build via `bash scripts/prep_chain_diverse_corpora.sh` to enable.")

# Run each battery dataset
print(f"\n=== Battery (eval cap = {EVAL_TOKEN_CAP:,} bytes, B={B}, T={SEQ_LEN}) ===\n")
rows = [("dataset", "bpc", "ppl", "n_bytes", "wall_s", "notes")]
for key, notes in DATASETS:
    path = f"{BATTERY}/{key}.test.bin"
    if not Path(path).exists():
        rows.append((key, "missing", "-", "-", "-", "test.bin not built"))
        continue
    n_bytes = Path(path).stat().st_size
    print(f"  {key:24s} ({n_bytes/1e6:.1f} MB) …", end=" ", flush=True)
    try:
        data = corp.load_as_tensor(path)
        t0 = time.time()
        r = core.eval_bpc(m, data, SEQ_LEN, B, EVAL_TOKEN_CAP)
        dt = time.time() - t0
        bpc = float(r.val_at(K("bpc")))
        ppl = float(r.val_at(K("ppl")))
        print(f"bpc={bpc:.4f} ppl={ppl:.3f}  ({dt:.1f}s)")
        rows.append((key, f"{bpc:.4f}", f"{ppl:.3f}", f"{n_bytes/1e6:.1f} MB", f"{dt:.1f}", notes))
    except Exception as e:
        print(f"FAILED: {e}")
        rows.append((key, "err", "-", "-", "-", str(e)[:60]))

# Print final table
print()
print("=" * 96)
print(f"{'dataset':<22} | {'bpc':>8} | {'ppl':>8} | {'n_bytes':>9} | {'wall':>5} | notes")
print("-" * 96)
if glaive is not None:
    print(f"{'glaive-fim-val':<22} | {glaive.val_at(K('bpc')):>8.4f} | {glaive.val_at(K('ppl')):>8.3f} | {'in-domain':>9} | {'-':>5} | training set (reference)")
else:
    print(f"{'glaive-fim-val':<22} | {'skipped':>8} | {'-':>8} | {'-':>9} | {'-':>5} | corpus not built")
for r in rows[1:]:
    print(f"{r[0]:<22} | {r[1]:>8} | {r[2]:>8} | {r[3]:>9} | {r[4]:>5} | {r[5]}")
print("=" * 96)

# Save to a JSONL
import json
log = []
if glaive is not None:
    log.append({"dataset": "glaive-fim-val", "bpc": float(glaive.val_at(K("bpc"))), "ppl": float(glaive.val_at(K("ppl"))), "kind": "reference"})
for key, notes in DATASETS:
    row = next((r for r in rows[1:] if r[0] == key), None)
    if row and row[1] not in ("err", "missing"):
        log.append({"dataset": key, "bpc": float(row[1]), "ppl": float(row[2]), "kind": "bpc"})
out = Path(OUT_JSONL)
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w") as f:
    for e in log:
        f.write(json.dumps(e) + "\n")
print(f"\nSaved → {out}")
