#!/usr/bin/env bash
# run_round2.sh — full FIM round-2 contribution in one command.
#
# Usage:  bash scripts/run_round2.sh <HANDLE>
#
# Does preflight → corpus → train → eval → stage → commit → push.
# Refuses to start anything expensive if preflight fails. Captures
# all measured numbers into workers/<HANDLE>/step-${TOTAL_STEPS}/meta.json.
# Agent's job is dispatch this, watch it run, then write narrative
# into the journal stub it leaves behind.

set -e

HANDLE="${1:-}"
if [ -z "$HANDLE" ]; then
  echo "usage: bash scripts/run_round2.sh <HANDLE>" >&2
  exit 1
fi

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── NetBank knobs (must be set before preflight) ────────────────────────────
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024   # ~512 MB on disk; fits a 4-vCPU box
export MMLLM_NET_C_NET=32

# ── 3-way SwitchGate + alpha_net (REQUIRED for consolidation to actually
#    happen — without these the long-gate is SumGate, which just adds
#    sdpa + mem + net with equal weight and exposes no routing decision.
#    Crucially, SumGate doesn't stash last_local_out / last_net_out, so
#    MMLLM_DISTILL_COEF has nothing to compute against → distill loss
#    silently stays at 0. Rounds 1/2/3 all ran with SumGate and saw
#    Δ_net ≈ 0 across every ablation as a result.) ────────────────────────
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true

# ── Consolidation knobs (this is how knowledge flows Local → Net) ───────────
# Distill: every train step, push Local's attention output into NetBank
# (direction-only — less brittle than L2 magnitude matching).
export MMLLM_DISTILL_COEF=0.1
# Round-4 deep-dive: direction-only=true aligns Net's direction to Local
# at 99.95% cosine, makes Net redundant with Local, alpha_net decays
# per-head, V can never grow magnitude. Switching to magnitude-aware
# distill puts MSE pressure on ||V|| too — breaks the redundancy basin.
export MMLLM_DISTILL_DIRECTION_ONLY=false

# Replay: when Local has mastered a position (plain-CE < threshold),
# stash it in a replay buffer and re-train on it periodically. Stops
# Local from forgetting earlier wins as it pushes into harder patterns.
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5

# ── Sleep-cycle LR schedule (Local hill-walks first, Net consolidates) ──────
# Cosine schedule sweeps the multiplier from START → END across training.
# Goal: Local dominant early (high lr_b), Net dominant late (high lr_n).
export MMLLM_LR_BANK_MULT=10.0       # Local Bank starts at 10× base
export MMLLM_LR_BANK_MULT_END=1.0    # ... cooling to 1× by end
export MMLLM_LR_NET_MULT=1.0         # NetBank starts at 1× base
export MMLLM_LR_NET_MULT_END=10.0    # ... rising to 10× by end (sleep cycle)

# Flatten the global cosine: MMLLM_LR_MIN = base lr keeps NetBank's
# ABSOLUTE effective LR high during the sleep cycle instead of decaying
# back to ~base. Round-2 finding: without this, lr_n×base_lr_decay
# cancels most of the rise, NetBank gets ~9e-3 only briefly at midpoint.
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3

# ── NetBank V warm-start (round-3 fix) ──────────────────────────────────────
# Round-2 finding: Δ_net stayed near 0 because V starts at random init.
# Only K_a/K_b were warm-started from Local, so retrieval geometry was
# correct but every retrieved row was uninitialized noise. With this flag,
# Local's V tensor is projected through the NetBank expander's pseudo-
# inverse and copied into NetBank's V[:n_copy] at warm-start time. Gives
# NetBank trained CONTENT at step 0, not just trained addressing.
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=true

# ── Tracking: mid-training ablation cadence (Δ_local / Δ_net / Δ_both) ──────
# Fires every 1000 steps → 5 events across a 5k run. Each event zeros
# Local V, evals; zeros Net V, evals; zeros both, evals; restores.
# This is the canonical instrumentation for "movement of knowledge into
# Local then into Net". Without it we'd only get a single end-of-run point.
# Overridable so smoke runs at smaller TOTAL_STEPS can scale this down.
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-1000}"

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
# IMPORTANT: stage at step-1, NOT step-0. core.lpy's resume gate is
# `(when (pos? start-step) ...)` so a step-0 ckpt is silently ignored
# and training falls through to random init. Round-3 lost the experiment
# to exactly this bug.
#
# ALSO: nuke any leftover step-N dirs from a prior round on this box,
# then stage step-1. core.lpy's `latest-checkpoint-step` picks the
# HIGHEST step-N it finds, so a stale step-5000 from a previous round
# would shadow the staged round-2 community core. Round-4's first
# dispatch hit exactly this — agent had to manually clean state.
if [ -n "${RESUME_FROM:-}" ] && [ -f "${RESUME_FROM}" ]; then
  rm -rf "${FIM_BASE}.ckpts"
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${RESUME_FROM}" "${FIM_BASE}.ckpts/step-1/dense.pt"
  # Touch a step.txt so train-long picks step-1 as latest unambiguously
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  echo "  resuming from ${RESUME_FROM} (staged at step-1; ckpts dir wiped first)"

  # NetBank V persistence (round-4 deep-dive finding):
  # The community core may ship per-layer bank-net-latest.{i}.fp16.bin
  # files alongside dense.pt. Expand them to fp32 at the runtime mmap
  # path (<bank-path>-net.{i}.bin) so NetBank V is carried forward
  # across rounds rather than re-randomized every dispatch.
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
TRAIN_LOG=/tmp/mmllm-cpu/round2-${HANDLE}.train.log
# 5k steps: ~30-45 min wall on CPU with the full consolidation stack
# (distill + replay + 5 ablation events). Keeps a dispatch under an hour.
# Smoke runs can override via env. Production dispatches leave these alone.
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-1000}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi

FIM_EVAL_LOG=/tmp/mmllm-cpu/round2-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round2-${HANDLE}.agent-eval.txt
mmllm eval-agent "$FIM_BASE" "${TOTAL_STEPS}" "$BANK_BASE" \
    "$SRC/xlam-synth.test.bin" xlam 100 256 2>&1 | tee "$AGENT_EVAL_LOG" || true

# ── 5. Extract numbers, write meta.json + journal stub ──────────────────────
WORKER_DIR="workers/$HANDLE/step-${TOTAL_STEPS}"
mkdir -p "$WORKER_DIR"
cp "${FIM_BASE}.ckpts/step-${TOTAL_STEPS}/dense.pt" "$WORKER_DIR/dense.pt"

# NetBank V persistence (round-4 deep-dive finding): without these
# files in the worker payload, the harvester has nothing to merge for
# NetBank, no community core gets bank-net files, every round
# retrains V from scratch and consolidation can never accumulate.
#
# fp32 files are 128 MB each at sqrt_n=1024 × c_net=32 — over GitHub's
# 100 MB blob limit. Convert to fp16 for the upload (precision loss is
# negligible for retrieval values; SparseAdam already operates on
# in-memory fp32 during training). Resume code in the next round will
# expand back to fp32 in /tmp before the model loads.
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

# Preserve the structured train log — every ablation / eval / router /
# slot_usage event lives in here. This is the canonical record of
# knowledge moving through Local → Net.
cp "${FIM_BASE}.log.jsonl" "$WORKER_DIR/log.jsonl" 2>/dev/null || true

python3 - "$HANDLE" "$TRAIN_LOG" "$FIM_EVAL_LOG" "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, tlog, felog, aelog, wdir, total_steps = sys.argv[1:7]
total_steps = int(total_steps)
# Training: B=4, T=128 — match what train-fim uses on cpu-tiny default
tokens_trained = total_steps * 4 * 128

def grep_last(path, pat, cast=float):
    try:
        ms = re.findall(pat, Path(path).read_text())
        return cast(ms[-1]) if ms else None
    except FileNotFoundError:
        return None

# Parse the structured train log JSONL for ablation events — gives the
# full trajectory of Δ_local / Δ_net / consolidation_idx across training.
ablation_trajectory = []
log_jsonl = Path(wdir) / "log.jsonl"
if log_jsonl.exists():
    for line in log_jsonl.read_text().splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        # Mid-training ablation events are tagged "ablation_intermediate";
        # the end-of-run event is "ablation". Capture both so the
        # trajectory is complete. (Round-3 dispatches missed every
        # mid-training event because the parser only matched "ablation".)
        if ev.get("event") in ("ablation", "ablation_intermediate"):
            ablation_trajectory.append({
                "step":              ev.get("step"),
                "kind":              ev.get("event"),
                "delta_local":       ev.get("delta_local"),
                "delta_net":         ev.get("delta_net"),
                "delta_both":        ev.get("delta_both"),
                "consolidation_idx": ev.get("consolidation_idx"),
            })

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

        # End-of-run scalars (regexes match the actual log line formats):
        # eval-bpc prints  "bpc=2.3264  ppl=5.02  over N tokens"
        # ablation prints  "Δ_local: 2.3205 → +0.3422"  (delta is after the arrow)
        "val_bpc_final":      grep_last(tlog,  r"bpc=(\d+\.\d+)\s+ppl="),
        "ablation_delta_local_final": grep_last(tlog, r"Δ_local:\s*\S+\s*→\s*([+\-\d\.]+)"),
        "ablation_delta_net_final":   grep_last(tlog, r"Δ_net:\s*\S+\s*→\s*([+\-\d\.]+)"),

        # Trajectory across training — this is the cross-round signal.
        # Authoritative source: log.jsonl ablation events (parsed above).
        # The scalars from the train-log regex are a fallback for runs
        # that didn't emit ablation events.
        "ablation_trajectory": ablation_trajectory,

        # Cross-run comparable evals (deterministic shared sets)
        "fim_eval_bpc":       grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "fim_eval_exact_pct": grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "agent_format_validity": grep_last(aelog, r"format[=:]?\s*([\d\.]+)"),
        "agent_name_match":      grep_last(aelog, r"name[=:]?\s*([\d\.]+)"),
        "agent_args_match":      grep_last(aelog, r"args[=:]?\s*([\d\.]+)"),
    },
}
Path(f"{wdir}/meta.json").write_text(json.dumps(meta, indent=2))
print(f"wrote {wdir}/meta.json with {len(ablation_trajectory)} ablation events")
print(json.dumps(meta, indent=2))
PY

# ── 6. Journal stub ─────────────────────────────────────────────────────────
TS=$(date -u +%Y-%m-%d-%H%M)
JOURNAL="docs/journal/${TS}-round2-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 2 — JSON FIM — ${HANDLE}

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- resume from: ${RESUME_FROM:-random init}
- NetBank: enabled, sqrt_n=${MMLLM_NET_SQRT_N}, c_net=${MMLLM_NET_C_NET}

## Results
See: ${WORKER_DIR}/meta.json

## Train log tail
\`\`\`
$(tail -20 "$TRAIN_LOG")
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
<agent: add your read on whether Δ_net moved off zero, what's surprising, what's next>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push (set MMLLM_SKIP_COMMIT=true to dry-run; smoke tests
#       use this to exercise the full pipeline without polluting the repo) ──
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts staged at $WORKER_DIR and $JOURNAL"
  echo "── DONE ──  $HANDLE (commit skipped via MMLLM_SKIP_COMMIT)"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-2 worker: ${HANDLE}"
  git push -u origin "$BRANCH"
  echo "── DONE ──  $HANDLE on $BRANCH"
fi
