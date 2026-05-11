#!/usr/bin/env bash
# run_round6.sh — sleep-cycle FIM round-6.
#
# Usage:  bash scripts/run_round6.sh <HANDLE>
#
# Differs from run_round2.sh in three places:
#   1. MMLLM_SLEEP_CYCLE_EVERY=1000 — zero V_local every 1000 steps.
#      5 sleep events across a 5k run.
#   2. MMLLM_DISTILL_COEF=0 — distill pulls Net toward Local's output,
#      which after sleep (V_local=0) means pulling Net toward zero.
#      Wrong direction; disable for now.
#   3. MMLLM_REPLAY_EVERY=0 — replay buffer fires when plain-CE < 0.5
#      (Local mastered the position). Sleep cycle resets V_local so
#      Local cannot stably master anything; replay would never fire
#      anyway, and the buffer overhead is wasted.
#
# Round-5→6 deep-dive context: round-5a step-5000 reported Δ_local=3.76
# Δ_net=0.0004 Δ_both=4.18, but Δ_both − Δ_local = 0.4166 (Net's
# masked capacity). Spike test at that ckpt — zeroed V_local, froze
# LR_BANK at 1e-6, ran 800 steps with distill off — pushed Δ_net to
# 0.65+ within 250 steps. This script generalizes that to a repeating
# multi-cycle schedule on a fresh round-2-resumed run.

set -e

HANDLE="${1:-}"
if [ -z "$HANDLE" ]; then
  echo "usage: bash scripts/run_round6.sh <HANDLE>" >&2
  exit 1
fi

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── NetBank knobs (must be set before preflight) ────────────────────────────
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32

# ── 3-way SwitchGate + alpha_net ────────────────────────────────────────────
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true

# ── Distill: OFF for round-6 ────────────────────────────────────────────────
# Rationale: distill is MSE(net_out, local_out.detach()) — it pulls Net
# toward Local. After sleep zeros V_local, Local's output → 0, so distill
# pulls Net toward 0. That cancels the very gain we're trying to extract.
# Round-7 will revisit a wake-phase pause + flipped distill (Net teaches
# Local) once we have a sleep-cycle baseline to compare against.
export MMLLM_DISTILL_COEF=0
export MMLLM_DISTILL_DIRECTION_ONLY=false   # no-op when coef=0

# ── Replay: OFF for round-6 ─────────────────────────────────────────────────
# Replay threshold (plain-CE < 0.5) only fires once Local has mastered a
# position. With Local periodically zeroed, mastery is fleeting; replay
# buffer fills slowly if at all. Disable rather than ship a no-op feature.
export MMLLM_REPLAY_EVERY=0

# ── LR schedule: flat (sleep cycle replaces the cosine sleep cycle) ─────────
# Round-5 used a cosine that swept LR_BANK 10→1 and LR_NET 1→10 over
# training, simulating a slow sleep-cycle. Round-6 uses an explicit
# discrete sleep event (V_local ← 0 every 1000 steps), so the cosine is
# unnecessary. Constant LRs: Local at 1× base (relearns from CE), Net
# at 10× base (faster consolidation between sleeps).
export MMLLM_LR_BANK_MULT=1.0
export MMLLM_LR_BANK_MULT_END=1.0
export MMLLM_LR_NET_MULT=10.0
export MMLLM_LR_NET_MULT_END=10.0
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3

# ── NetBank V warm-start (carries forward across rounds) ────────────────────
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=true

# ── Sleep cycle (the round-6 mechanism) ─────────────────────────────────────
# Every 1000 steps, zero V_local across all blocks. K_a/K_b (routing
# keys) are preserved — only the value table is wiped. Local relearns
# from CE loss but specializes on residuals because Net+sdpa already
# carry most of what Local previously covered.
#
# 5k-step run with sleep every 1000 → 5 sleep events at 1000/2000/3000/
# 4000/5000. Ablations at 250-step cadence (20 events total) capture
# pre-sleep and post-sleep Δ_net trajectories around each cycle.
export MMLLM_SLEEP_CYCLE_EVERY=1000

# ── Tracking: finer ablation cadence to capture pre/post-sleep deltas ──────
# Round-2..5 used 1000-step ablation (5 events, aligned with sleep).
# Round-6 uses 250 (20 events, 4 between each pair of sleeps) — gives
# the Δ_net rise + relaxation shape that single-point sampling misses.
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"

# ── 0. Preflight (fail-loud, fail-cheap) ────────────────────────────────────
bash scripts/preflight_fim_run.sh || { echo "preflight failed; aborting" >&2; exit 1; }
source /tmp/mmllm-cpu/preflight.env   # sets RESUME_FROM=<path-or-empty>

# ── 1. Corpus (synth xlam; no HF auth) ──────────────────────────────────────
SRC=/tmp/mmllm-cpu/sources
mkdir -p "$SRC"
if [ ! -f "$SRC/xlam-synth.train.bin" ]; then
  python scripts/prep_xlam_synth.py "$SRC/xlam-synth" 20000 500000 500000
fi

JSON_DIR="$SRC/xlam-json"
if [ ! -d "$JSON_DIR" ] || [ -z "$(ls "$JSON_DIR" 2>/dev/null)" ]; then
  mkdir -p "$JSON_DIR"
  python3 - <<'PY'
from pathlib import Path
data = Path("/tmp/mmllm-cpu/sources/xlam-synth.train.bin").read_bytes()
docs = [d for d in data.split(b"\n\n") if 100 < len(d) < 4096][:20000]
out = Path("/tmp/mmllm-cpu/sources/xlam-json")
for i, d in enumerate(docs):
    (out / f"doc-{i:05d}.json").write_bytes(d)
print(f"wrote {len(docs)} files")
PY
fi

FIM_BASE=/tmp/mmllm-cpu/fim-json
if [ ! -f "${FIM_BASE}.train.bin" ]; then
  mmllm fim-build-corpus json "$JSON_DIR" "$FIM_BASE" 0.7 0.5 42
fi

# ── 2. Resume seed (preflight set RESUME_FROM if available) ─────────────────
# Same staging convention as round-2..5 (step-1 + step.txt, nuke prior
# ckpts dir, expand fp16 NetBank V into the runtime mmap).
if [ -n "${RESUME_FROM:-}" ] && [ -f "${RESUME_FROM}" ]; then
  rm -rf "${FIM_BASE}.ckpts"
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${RESUME_FROM}" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  echo "  resuming from ${RESUME_FROM} (staged at step-1; ckpts dir wiped first)"

  RESUME_DIR=$(dirname "${RESUME_FROM}")
  python3 - "${RESUME_DIR}" "/tmp/mmllm-cpu/fim-bank" <<'PY'
import sys, numpy as np
from pathlib import Path
resume_dir = Path(sys.argv[1])
bank_base  = sys.argv[2]
restored = 0
for fp16_file in sorted(resume_dir.glob("bank-net-latest.*.fp16.bin")):
    parts = fp16_file.name.split(".")
    if len(parts) < 4: continue
    try:    layer = int(parts[1])
    except: continue
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    out   = Path(f"{bank_base}-net.{layer}.bin")
    out.parent.mkdir(parents=True, exist_ok=True)
    arr16.astype(np.float32).tofile(out)
    restored += 1
    print(f"  NetBank V layer {layer} restored from community core "
          f"({out.stat().st_size/1e6:.1f} MB fp32 expanded from {fp16_file.stat().st_size/1e6:.1f} MB fp16)")
if restored == 0:
    print(f"  no bank-net-latest.*.fp16.bin in {resume_dir} — NetBank V will start from K_a/K_b warm-start + random V")
else:
    print(f"  ✓ {restored} NetBank V layers carried forward from community core")
PY
fi

# ── 3. Train ────────────────────────────────────────────────────────────────
BANK_BASE=/tmp/mmllm-cpu/fim-bank
TRAIN_LOG=/tmp/mmllm-cpu/round6-${HANDLE}.train.log
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-250}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi

FIM_EVAL_LOG=/tmp/mmllm-cpu/round6-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round6-${HANDLE}.agent-eval.txt
mmllm eval-agent "$FIM_BASE" "${TOTAL_STEPS}" "$BANK_BASE" \
    "$SRC/xlam-synth.test.bin" xlam 100 256 2>&1 | tee "$AGENT_EVAL_LOG" || true

# ── 5. Extract numbers, write meta.json + journal stub ──────────────────────
WORKER_DIR="workers/$HANDLE/step-${TOTAL_STEPS}"
mkdir -p "$WORKER_DIR"
cp "${FIM_BASE}.ckpts/step-${TOTAL_STEPS}/dense.pt" "$WORKER_DIR/dense.pt"

# NetBank V persistence: fp16 to fit under GitHub's 100 MB blob limit.
python3 - "${BANK_BASE}" "${WORKER_DIR}" <<'PY'
import sys, numpy as np
from pathlib import Path
bank_base = sys.argv[1]
wdir      = Path(sys.argv[2])
shipped   = 0
for src in sorted(Path("/tmp/mmllm-cpu").glob(f"{Path(bank_base).name}-net.*.bin")):
    parts = src.name.split(".")
    try:    layer = int(parts[1])
    except: continue
    arr32 = np.fromfile(src, dtype=np.float32)
    dst   = wdir / f"bank-net-latest.{layer}.fp16.bin"
    arr32.astype(np.float16).tofile(dst)
    shipped += 1
    print(f"  staged NetBank V layer {layer}: {dst.name} "
          f"({dst.stat().st_size/1e6:.1f} MB fp16 from {src.stat().st_size/1e6:.1f} MB fp32)")
if shipped == 0:
    print(f"  no NetBank V files at {bank_base}-net.*.bin — NetBank either disabled or no training happened")
PY

cp "${FIM_BASE}.log.jsonl" "$WORKER_DIR/log.jsonl" 2>/dev/null || true

python3 - "$HANDLE" "$TRAIN_LOG" "$FIM_EVAL_LOG" "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, tlog, felog, aelog, wdir, total_steps = sys.argv[1:7]
total_steps = int(total_steps)
tokens_trained = total_steps * 4 * 128

def grep_last(path, pat, cast=float):
    try:
        ms = re.findall(pat, Path(path).read_text())
        return cast(ms[-1]) if ms else None
    except FileNotFoundError:
        return None

ablation_trajectory = []
sleep_events = []
log_jsonl = Path(wdir) / "log.jsonl"
if log_jsonl.exists():
    for line in log_jsonl.read_text().splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        if ev.get("event") in ("ablation", "ablation_intermediate"):
            ablation_trajectory.append({
                "step":              ev.get("step"),
                "kind":              ev.get("event"),
                "delta_local":       ev.get("delta_local"),
                "delta_net":         ev.get("delta_net"),
                "delta_both":        ev.get("delta_both"),
                "consolidation_idx": ev.get("consolidation_idx"),
            })
        elif ev.get("event") == "sleep_cycle":
            sleep_events.append({"step": ev.get("step")})

meta = {
    "tokens_trained": tokens_trained,
    "steps":          total_steps,
    "label":          handle,
    "fim": {
        "language":           "json",
        "fim_ratio":          0.7,
        "psm_ratio":          0.5,
        "splitter":           "json-value-boundary",
        "source_corpus":      "synthetic-xlam (scripts/prep_xlam_synth.py)",
        "sleep_cycle_every":  1000,
        "distill_coef":       0,
        "val_bpc_final":      grep_last(tlog,  r"bpc=(\d+\.\d+)\s+ppl="),
        "ablation_delta_local_final": grep_last(tlog, r"Δ_local:\s*\S+\s*→\s*([+\-\d\.]+)"),
        "ablation_delta_net_final":   grep_last(tlog, r"Δ_net:\s*\S+\s*→\s*([+\-\d\.]+)"),
        "ablation_trajectory": ablation_trajectory,
        "sleep_events":        sleep_events,
        "fim_eval_bpc":       grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "fim_eval_exact_pct": grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "agent_format_validity": grep_last(aelog, r"format[=:]?\s*([\d\.]+)"),
        "agent_name_match":      grep_last(aelog, r"name[=:]?\s*([\d\.]+)"),
        "agent_args_match":      grep_last(aelog, r"args[=:]?\s*([\d\.]+)"),
    },
}
Path(f"{wdir}/meta.json").write_text(json.dumps(meta, indent=2))
print(f"wrote {wdir}/meta.json with {len(ablation_trajectory)} ablation events, {len(sleep_events)} sleep events")
print(json.dumps(meta, indent=2))
PY

# ── 6. Journal stub ─────────────────────────────────────────────────────────
TS=$(date -u +%Y-%m-%d-%H%M)
JOURNAL="docs/journal/${TS}-round6-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 6 — Sleep cycle — ${HANDLE}

## Mechanism
- sleep cycle: V_local ← 0 every ${MMLLM_SLEEP_CYCLE_EVERY} steps
- distill: OFF (would pull Net→0 with V_local=0)
- replay: OFF (mastery threshold can't fire under repeated Local resets)
- LR: flat — bank=1× base, net=10× base
- ablate cadence: ${MMLLM_ABLATE_EVERY} steps (captures pre/post-sleep Δ trajectory)

## Round-5 → 6 baseline
- Round-5a step-5000: Δ_local=3.7601, Δ_net=0.0004, Δ_both=4.1767
- Δ_both − Δ_local = +0.4166 (Net's masked capacity at that ckpt)
- 10-min spike at the same ckpt with V_local zeroed + LR_BANK frozen:
  Δ_net jumped 0.0004 → 0.7381 within 250 steps.
  Δ_net = 0.6486 by step 5750 (steady).

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- resume from: ${RESUME_FROM:-random init}
- NetBank: enabled, sqrt_n=${MMLLM_NET_SQRT_N}, c_net=${MMLLM_NET_C_NET}

## Hypothesis
Each sleep cycle frees Local's V; Net's masked contribution becomes visible
in Δ_net. As cycles repeat, Net densifies further and Δ_net grows. Local
specializes on what Net+sdpa don't cover (because gate routes those
residuals to Local once Net is established). End-of-run target:
Δ_net ≥ 0.5, ideally rising across cycles.

## Results
See: ${WORKER_DIR}/meta.json

## Train log tail
\`\`\`
$(tail -25 "$TRAIN_LOG")
\`\`\`

## FIM eval
\`\`\`
$(cat "$FIM_EVAL_LOG")
\`\`\`

## Agent eval
\`\`\`
$(cat "$AGENT_EVAL_LOG")
\`\`\`

## Narrative
<agent: chart the Δ_net trajectory across sleep cycles. Does it rise
monotonically, oscillate, or saturate? Does control_bpc degrade across
sleeps or hold steady (steady = Net is genuinely consolidating)? What's
the final Δ_net vs the spike's 0.65?>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push ────────────────────────────────────────────────────────
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts staged at $WORKER_DIR and $JOURNAL"
  echo "── DONE ──  $HANDLE (commit skipped via MMLLM_SKIP_COMMIT)"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-6 worker: ${HANDLE}"
  git push -u origin "$BRANCH"
  echo "── DONE ──  $HANDLE on $BRANCH"
fi
