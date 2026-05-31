#!/usr/bin/env bash
# run_measure_features.sh — single 100-step spoon at the smallest config.
# V_local: sqrt_n=226 → ~100 MB total
# V_net:   sqrt_n=8  → ~32 KB total
# Goal: measure local_touched_pages at step 75 (5 steps post phase split).
# That gives the empirical "feature count" used to size V_net for sleep.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false

# Banks.
export MMLLM_SQRT_N=226                     # V_local 100 MB total
export MMLLM_NET_SQRT_N=8                   # V_net 32 KB total
export MMLLM_NET_C_NET=32
# top_k: cpu-tiny-style proportions.
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64                   # capped internally to sqrt_n²=64
export MMLLM_NET_SUB_TOP_K=8                # capped internally to sqrt_n=8

# Spike-6 schedule.
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0
export MMLLM_LR_BANK_MULT=30.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_LR_WARMUP=70
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=25
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-meas
BANK_BASE=/tmp/mmllm-cpu/fim-bank-meas
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin" 2>/dev/null || true

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

python3 - "$BANK_BASE" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 8;    C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
    print(f"  V_local layer {i}: 226² × 128 × 4 = {a.nbytes/1024**2:.1f} MB")
for i in range(4):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
    print(f"  V_net   layer {i}: 8² × 32 × 4 = {a.nbytes} bytes")
PY

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 110 2>&1 | tee /tmp/mmllm-cpu/measure.train.log \
  | grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both|training complete" || true

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  FEATURE-COUNT MEASUREMENT"
echo "═══════════════════════════════════════════════════════════════"
python3 - <<'PY'
import json
from pathlib import Path
log = Path("/tmp/mmllm-cpu/fim-meas.log.jsonl")
events = []
for line in log.read_text().splitlines():
    try: ev = json.loads(line)
    except: continue
    if ev.get("event") == "netbank_telemetry":
        events.append(ev)
print(f"{'step':>5}  {'mean local_touched_pages (across 4 layers)':>50}")
for ev in events:
    layers = ev.get("per_layer", [])
    vals = [l.get("local_touched_pages") for l in layers if l.get("local_touched_pages") is not None]
    if vals:
        mean_pages = sum(vals) / len(vals)
        # page_rows default = 1024; pages × 1024 = row upper bound
        est_rows = mean_pages * 1024
        max_pages = (226*226 + 1023) // 1024
        coverage = mean_pages / max_pages * 100
        print(f"{ev['step']:>5}  mean_pages={mean_pages:>6.1f}  est_rows≤{est_rows:>7.0f}  coverage={coverage:>5.1f}%  (of {max_pages} max)")
print()
print("V_local: sqrt_n=226 → 51076 entries / 51 pages of 1024 rows each")
print("V_net to fit those features: ~sqrt(50 × est_rows) for headroom")
PY
