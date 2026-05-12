#!/usr/bin/env bash
# run_consolidation_chain.sh — two 1k-step rounds back-to-back, same config,
# round 2 resumes from round 1's end-state. Tests whether Net's Δ keeps
# climbing across consecutive runs (consolidation chain) or saturates.
#
# Round 1: from round-6/step-5000 baseline (dense.pt + fp16 V_net seed).
#          Expected: Δ_net 0.054 (step 100) → ~0.080 (step 1000).
# Round 2: from round 1 step-1000 end-state (dense + V_local + V_net).
#          Expected if chain works: Δ_net ~0.08 (step 100) → > 0.08 (step 1000).
#
# Config (both rounds identical, the spike-6 winning recipe):
#   - distill: residual target, direction-only, coef 0.5→5.0 cosine
#   - magnitude: 0→1.0 cosine with clamp 10.0
#   - LR_BANK 10→0.001 cosine; LR_NET 0.001→0.1; LR_DENSE 0.05→0.005
#   - warmup 700 steps (phase split: wake 0-700, sleep 700-1000)
#   - Net-default Bernoulli gate

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── Spike-6 config (locked across both rounds) ─────────────────────────────
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
export MMLLM_LR_WARMUP=700

export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=100

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

# Sanity check: round-6 baseline exists.
for f in "${ROUND6_BASE}/dense.pt" \
         "${ROUND6_BASE}/bank-net-latest.0.fp16.bin" \
         "${ROUND6_BASE}/bank-net-latest.1.fp16.bin" \
         "${ROUND6_BASE}/bank-net-latest.2.fp16.bin" \
         "${ROUND6_BASE}/bank-net-latest.3.fp16.bin"; do
  if [ ! -f "$f" ]; then echo "MISSING: $f" >&2; exit 1; fi
done

# ════════════════════════ Round 1 setup ══════════════════════════════════
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "  Round 1: spike-6 recipe from round-6/step-5000 baseline"
echo "════════════════════════════════════════════════════════════════"

# Wipe contaminated V banks + ckpts.
rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin

# Stage round-6 dense.pt at step-1.
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# Restore V_net from round-6 fp16 seed (fp16 → fp32 expand).
python3 - "${ROUND6_BASE}" "${BANK_BASE}" <<'PY'
import sys, numpy as np
from pathlib import Path
src_dir = Path(sys.argv[1])
bank_base = sys.argv[2]
for fp16_file in sorted(src_dir.glob("bank-net-latest.*.fp16.bin")):
    layer = int(fp16_file.name.split(".")[1])
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    out = Path(f"{bank_base}-net.{layer}.bin")
    arr16.astype(np.float32).tofile(out)
    print(f"  V_net layer {layer} restored from fp16 seed ({out.stat().st_size/1e6:.1f} MB)")
PY

ROUND1_LOG=/tmp/mmllm-cpu/chain-round1.train.log
mmllm train-fim "$FIM_BASE" "$BANK_BASE" 1001 100 1000 2>&1 | tee "$ROUND1_LOG"

# Archive round 1 end-state for round 2 resume.
ARCHIVE_R1=/tmp/mmllm-cpu/chain-round1-end-state
rm -rf "$ARCHIVE_R1" && mkdir -p "$ARCHIVE_R1"
cp "${FIM_BASE}.ckpts/step-1000/dense.pt" "$ARCHIVE_R1/dense.pt" 2>/dev/null || \
  cp "${FIM_BASE}.ckpts/step-1001/dense.pt" "$ARCHIVE_R1/dense.pt"
cp "${BANK_BASE}".0.bin    "$ARCHIVE_R1/V_local.0.bin"
cp "${BANK_BASE}".1.bin    "$ARCHIVE_R1/V_local.1.bin"
cp "${BANK_BASE}".2.bin    "$ARCHIVE_R1/V_local.2.bin"
cp "${BANK_BASE}".3.bin    "$ARCHIVE_R1/V_local.3.bin"
cp "${BANK_BASE}"-net.0.bin "$ARCHIVE_R1/V_net.0.bin"
cp "${BANK_BASE}"-net.1.bin "$ARCHIVE_R1/V_net.1.bin"
cp "${BANK_BASE}"-net.2.bin "$ARCHIVE_R1/V_net.2.bin"
cp "${BANK_BASE}"-net.3.bin "$ARCHIVE_R1/V_net.3.bin"

# Save round 1's log under a stable name (round 2 will overwrite the live log).
cp "${FIM_BASE}.log.jsonl" "$ARCHIVE_R1/log.jsonl" 2>/dev/null || true

# ════════════════════════ Round 2 setup ══════════════════════════════════
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "  Round 2: spike-6 recipe, resumed from round 1 end-state"
echo "════════════════════════════════════════════════════════════════"

# Re-stage round-1 end-state at step-1 for a fresh schedule replay.
rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "$ARCHIVE_R1/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# V_local and V_net stay in-place — they already reflect round 1 end-state.
# But the train loop may try to restore from bank-latest in the (now wiped)
# ckpts dir; pre-create those from the archive to keep it happy.
cp "$ARCHIVE_R1/V_local.0.bin" "${FIM_BASE}.ckpts/bank-latest.0.bin"
cp "$ARCHIVE_R1/V_local.1.bin" "${FIM_BASE}.ckpts/bank-latest.1.bin"
cp "$ARCHIVE_R1/V_local.2.bin" "${FIM_BASE}.ckpts/bank-latest.2.bin"
cp "$ARCHIVE_R1/V_local.3.bin" "${FIM_BASE}.ckpts/bank-latest.3.bin"

ROUND2_LOG=/tmp/mmllm-cpu/chain-round2.train.log
mmllm train-fim "$FIM_BASE" "$BANK_BASE" 1001 100 1000 2>&1 | tee "$ROUND2_LOG"

# ════════════════════════ Chain summary ══════════════════════════════════
echo ""
echo "════════════════════════════════════════════════════════════════"
echo "  Consolidation chain summary"
echo "════════════════════════════════════════════════════════════════"
python3 - "$ARCHIVE_R1/log.jsonl" "${FIM_BASE}.log.jsonl" <<'PY'
import json, sys
from pathlib import Path
def trajectory(path):
    out = []
    if not Path(path).exists(): return out
    for line in Path(path).read_text().splitlines():
        try:    ev = json.loads(line)
        except: continue
        if ev.get("event") in ("ablation","ablation_intermediate"):
            out.append((ev.get("step"), ev.get("delta_local"), ev.get("delta_net"), ev.get("delta_both")))
    return out

r1 = trajectory(sys.argv[1])
r2 = trajectory(sys.argv[2])

def fmt(t):
    s, dl, dn, db = t
    dl_s = f"{dl:+.4f}" if isinstance(dl,(int,float)) else "    n/a"
    dn_s = f"{dn:+.4f}" if isinstance(dn,(int,float)) else "    n/a"
    db_s = f"{db:+.4f}" if isinstance(db,(int,float)) else "    n/a"
    return f"  step {s:>5}  Δ_local={dl_s}  Δ_net={dn_s}  Δ_both={db_s}"

print("Round 1 (from round-6 baseline):")
for t in r1: print(fmt(t))

print()
print("Round 2 (resumed from round 1 end):")
for t in r2: print(fmt(t))

# Per-round gain.
def gain(traj):
    nets = [t[2] for t in traj if isinstance(t[2],(int,float))]
    return (nets[0], nets[-1], nets[-1] - nets[0]) if len(nets) >= 2 else None

g1 = gain(r1); g2 = gain(r2)
print()
print("Per-round Δ_net gain:")
if g1: print(f"  round 1: {g1[0]:.4f} → {g1[1]:.4f}   gain {g1[2]:+.4f}")
if g2: print(f"  round 2: {g2[0]:.4f} → {g2[1]:.4f}   gain {g2[2]:+.4f}")
PY
