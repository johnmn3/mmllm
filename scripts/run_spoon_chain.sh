#!/usr/bin/env bash
# run_spoon_chain.sh — chain 5 × 100-step spoons.
#
# Round 1 starts fresh from round-6 baseline (V_net seed, V_local zero-init).
# Each subsequent round resumes from the previous round's end-state, with
# V_local AND V_net carried forward, dense.pt staged at step-1 for a fresh
# schedule replay. Archives between rounds so the chain trajectory is
# inspectable end-to-end.
#
# Pass: Δ_net at round 5 > Δ_net at round 1.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32
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

export MMLLM_LR_BANK_MULT=10.0
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

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
ARCHIVE_ROOT=/tmp/mmllm-cpu/spoon-chain-$(date -u +%H%M)
mkdir -p "$ARCHIVE_ROOT"

run_round() {
  local round_num=$1
  local resume_from_dense=$2     # path to dense.pt (or "BASELINE" for round-6)
  local resume_v_local=$3        # "ZERO" or path-prefix to V_local archive
  local resume_v_net=$4          # "FP16_SEED" or path-prefix to V_net archive

  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  SPOON ROUND $round_num"
  echo "═══════════════════════════════════════════════════════════════"

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"

  # Stage dense.pt.
  if [ "$resume_from_dense" = "BASELINE" ]; then
    cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  else
    cp "$resume_from_dense" "${FIM_BASE}.ckpts/step-1/dense.pt"
  fi
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Stage V_net.
  if [ "$resume_v_net" = "FP16_SEED" ]; then
    python3 - "${ROUND6_BASE}" "${BANK_BASE}" <<'PY'
import sys, numpy as np
from pathlib import Path
src_dir = Path(sys.argv[1]); bank_base = sys.argv[2]
for fp16_file in sorted(src_dir.glob("bank-net-latest.*.fp16.bin")):
    layer = int(fp16_file.name.split(".")[1])
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    Path(f"{bank_base}-net.{layer}.bin").write_bytes(arr16.astype(np.float32).tobytes())
PY
  else
    for i in 0 1 2 3; do cp "${resume_v_net}.${i}.bin" "${BANK_BASE}-net.${i}.bin"; done
  fi

  # Stage V_local.
  if [ "$resume_v_local" = "ZERO" ]; then
    python3 - "${BANK_BASE}" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
for i in range(4):
    arr = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(65536, 128))
    arr[:] = 0.0
    arr.flush()
PY
  else
    for i in 0 1 2 3; do cp "${resume_v_local}.${i}.bin" "${BANK_BASE}.${i}.bin"; done
  fi

  echo "  → training (100 steps, ablate every 25)"
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 100 2>&1 | tee /tmp/mmllm-cpu/spoon-r${round_num}.train.log | grep -E "ablation Δ|Δ_local|Δ_net|Δ_both|training complete" || true

  # Archive this round's end-state. Skip V_local (it's zeroed each round
  # anyway, so no need to preserve it). Only V_net and dense flow forward.
  local ROUND_DIR="$ARCHIVE_ROOT/round-${round_num}"
  mkdir -p "$ROUND_DIR"
  cp "${BANK_BASE}-net.0.bin"    "$ROUND_DIR/V_net.0.bin"
  cp "${BANK_BASE}-net.1.bin"    "$ROUND_DIR/V_net.1.bin"
  cp "${BANK_BASE}-net.2.bin"    "$ROUND_DIR/V_net.2.bin"
  cp "${BANK_BASE}-net.3.bin"    "$ROUND_DIR/V_net.3.bin"
  local LATEST=$(ls -1d "${FIM_BASE}.ckpts/step-"* 2>/dev/null | sort -V | tail -1)
  cp "$LATEST/dense.pt"          "$ROUND_DIR/dense.pt"
  cp /tmp/mmllm-cpu/fim-json-v3.log.jsonl "$ROUND_DIR/log.jsonl"
  echo "  → archived to $ROUND_DIR"
}

# Round 1: fresh from baseline (V_local zero, V_net seed).
run_round 1 BASELINE ZERO FP16_SEED

# Rounds 2-5: V_local zeroed each round (fresh hill climber);
# V_net carried forward (consolidating bank); dense carried forward.
for r in 2 3 4 5; do
  prev=$((r - 1))
  run_round "$r" \
    "$ARCHIVE_ROOT/round-${prev}/dense.pt" \
    ZERO \
    "$ARCHIVE_ROOT/round-${prev}/V_net"
done

# Summary across rounds.
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  SPOON CHAIN SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
python3 - "$ARCHIVE_ROOT" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
print(f"{'round':>5}  {'step':>5}  {'Δ_local':>9}  {'Δ_net':>9}  {'Δ_both':>9}")
for r in (1, 2, 3, 4, 5):
    rd = root / f"round-{r}"
    log = rd / "log.jsonl"
    if not log.exists(): continue
    for line in log.read_text().splitlines():
        try: ev = json.loads(line)
        except: continue
        if ev.get("event") == "ablation_intermediate":
            print(f"{r:>5}  {ev['step']:>5}  {ev['delta_local']:>+9.4f}  {ev['delta_net']:>+9.4f}  {ev['delta_both']:>+9.4f}")
    print()
PY
echo "  archives at: $ARCHIVE_ROOT"
