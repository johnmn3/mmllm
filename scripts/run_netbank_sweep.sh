#!/usr/bin/env bash
# run_netbank_sweep.sh — 100-step spoon at varying V_net sqrt_n.
# Constants: V_local sqrt_n=720, LR_BANK_MULT=30, spike-6 schedule.
# Sweep: V_net sqrt_n ∈ {8, 32, 128, 512, 1024, 2000}.
# Captures `local_touched_pages` in netbank_telemetry at each ablation —
# this is the empirical "feature count" for the adaptive-sizing design.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

# Common config.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=720
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_C_NET=32
export MMLLM_NET_TOP_K=64        # constant; high-coverage at small sqrt_n, selective at large
export MMLLM_NET_SUB_TOP_K=64

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

FIM_BASE=/tmp/mmllm-cpu/fim-sw
BANK_BASE=/tmp/mmllm-cpu/fim-bank-sw
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin" 2>/dev/null || true

SUMMARY=/tmp/mmllm-cpu/netbank-sweep.summary.csv
: > "$SUMMARY"
echo "sqrt_n_net,Δ_local_step100,Δ_net_step100,Δ_both_step100,ctrl_bpc,local_touched_pages_step75" >> "$SUMMARY"

run_spoon() {
  local sqrt_n=$1
  export MMLLM_NET_SQRT_N=$sqrt_n
  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  SPOON sqrt_n_net=$sqrt_n  ($(python3 -c "print(${sqrt_n}*${sqrt_n}*32*4//1024,'KB' if ${sqrt_n}*${sqrt_n}*32*4 < 1024*1024 else 'MB' if ${sqrt_n}*${sqrt_n}*32*4 < 1024**3 else 'GB')") per layer)"
  echo "═══════════════════════════════════════════════════════════════"

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  python3 - "$BANK_BASE" "$sqrt_n" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
sqrt_net = int(sys.argv[2])
SQRT_LOCAL = 720;  Q_DIM = 128
C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
for i in range(4):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(sqrt_net * sqrt_net, C_NET))
    a[:] = 0.0; a.flush()
print(f"  V_local 4 × 720² × 128 × 4 = 1 GB total")
print(f"  V_net   4 × {sqrt_net}² × 32 × 4 = {4*sqrt_net*sqrt_net*32*4} bytes total")
PY

  local TRAIN_LOG=/tmp/mmllm-cpu/sweep-${sqrt_n}.train.log
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 110 2>&1 | tee "$TRAIN_LOG" \
    | grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both|training complete" || true

  # Extract final values + local_touched_pages at step 75 (just past phase split).
  python3 - "$sqrt_n" >> "$SUMMARY" <<'PY'
import json, sys
from pathlib import Path
sqrt_n = sys.argv[1]
log = Path("/tmp/mmllm-cpu/fim-sw.log.jsonl")
last_ablation = None
touched_at_75 = None
for line in log.read_text().splitlines():
    try: ev = json.loads(line)
    except: continue
    if ev.get("event") == "ablation_intermediate":
        last_ablation = ev
    elif ev.get("event") == "netbank_telemetry" and ev.get("step") == 75:
        # Average touched pages across layers.
        layers = ev.get("per_layer", [])
        vals = [l.get("local_touched_pages", 0) for l in layers]
        touched_at_75 = sum(vals) // len(vals) if vals else 0
if last_ablation is None:
    print(f"{sqrt_n},,,, ,(no ablation)")
else:
    dl = last_ablation['delta_local']; dn = last_ablation['delta_net']
    db = last_ablation['delta_both']; cb = last_ablation['control_bpc']
    tp = touched_at_75 if touched_at_75 is not None else ""
    print(f"{sqrt_n},{dl:.4f},{dn:.4f},{db:.4f},{cb:.4f},{tp}")
PY
}

for sqrt_n in 8 32 128 512 1024 2000; do
  run_spoon "$sqrt_n"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  NETBANK SWEEP SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
cat "$SUMMARY"
