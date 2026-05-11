#!/usr/bin/env bash
# run_round7.sh — sharded-corpus FIM round-7.
#
# Usage:  bash scripts/run_round7.sh <HANDLE> <SHARD_INDEX> [<N_SHARDS>]
#
# Round-6 verdict: 5 workers on the SAME corpus + FedAvg merge produced
# a non-trivial breakthrough (format_validity 0.110 vs best-individual
# 0.020; fim_eval 5.804 vs best 6.204). But distillation harvest matched
# FedAvg and didn't exceed it — the ensemble average has nothing
# meaningfully different from individual workers' generic-but-noisy
# outputs because all workers trained on the same data.
#
# Round-7 hypothesis: when workers see DIFFERENT slices of the corpus,
# each consolidates a different specialization into its NetBank. The
# subsequent harvest (FedAvg or distillation) then has actually-
# complementary content to combine, not 5 different local optima of
# the same function.
#
# Round-7 setup vs round-6:
#   1. Resume from core/round-6/step-5000 (the round-6 FedAvg merge),
#      NOT core/round-2. NetBank V is carried forward via the fp16
#      expansion AND warm-start is suppressed so the harvested NetBank
#      content is preserved (MMLLM_SKIP_NETBANK_WARMSTART=true).
#   2. Per-worker corpus shard: hash-by-doc-id partition. Worker N
#      (0-based) gets docs with (id mod N_SHARDS) == N.
#   3. Sleep cycle, distill, replay, LR — same as round-6.

set -e

HANDLE="${1:-}"
SHARD_INDEX="${2:-}"
N_SHARDS="${3:-5}"
if [ -z "$HANDLE" ] || [ -z "$SHARD_INDEX" ]; then
  echo "usage: bash scripts/run_round7.sh <HANDLE> <SHARD_INDEX> [<N_SHARDS=5>]" >&2
  exit 1
fi

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── NetBank knobs ───────────────────────────────────────────────────────────
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32

# ── 3-way SwitchGate + alpha_net ────────────────────────────────────────────
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true

# ── Round-6 setup, unchanged ────────────────────────────────────────────────
export MMLLM_DISTILL_COEF=0
export MMLLM_DISTILL_DIRECTION_ONLY=false
export MMLLM_REPLAY_EVERY=0
export MMLLM_LR_BANK_MULT=1.0
export MMLLM_LR_BANK_MULT_END=1.0
export MMLLM_LR_NET_MULT=10.0
export MMLLM_LR_NET_MULT_END=10.0
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_SLEEP_CYCLE_EVERY=1000
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"

# ── Round-7 specific: preserve harvested NetBank V ──────────────────────────
# Without this, train-long's warm-start fires (because opt-sparse-net.pt
# is absent in the round-6 core) and rewrites NetBank V from Local V's
# pseudo-inverse projection — destroying the cross-worker consolidation
# the harvester just produced. The fp16-expansion step below writes V
# into the runtime mmap; this knob makes the train-long resume path
# trust that and skip the warm-start.
export MMLLM_SKIP_NETBANK_WARMSTART=true

# NetBank warm-start from Local is also unnecessary on resume from the
# round-6 core since both Local AND NetBank already have meaningful
# state. Keep the flag set so future rounds inherit the behavior.
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

# ── 0. Preflight ────────────────────────────────────────────────────────────
bash scripts/preflight_fim_run.sh || { echo "preflight failed; aborting" >&2; exit 1; }
source /tmp/mmllm-cpu/preflight.env

# Confirm we're resuming from round-6 (or fail loud — round-7 must resume from
# the harvested round-6, otherwise the experiment is meaningless).
if [[ "${RESUME_FROM:-}" != *"round-6"* ]]; then
  echo "round-7 needs core/round-6/step-5000/ as resume seed but preflight selected: ${RESUME_FROM:-(none)}" >&2
  echo "(latest core/round-* dir is what preflight selects — make sure round-6 is committed and round-7 isn't sitting in core/)" >&2
  exit 1
fi
echo "  ✓ resuming from round-6 community core: ${RESUME_FROM}"

# ── 1. Corpus prep ──────────────────────────────────────────────────────────
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

# Sharded FIM corpus: this worker only sees docs where (id mod N_SHARDS) == SHARD_INDEX
SHARD_JSON_DIR="${SRC}/xlam-json-shard-${SHARD_INDEX}-of-${N_SHARDS}"
if [ ! -d "$SHARD_JSON_DIR" ] || [ -z "$(ls "$SHARD_JSON_DIR" 2>/dev/null)" ]; then
  mkdir -p "$SHARD_JSON_DIR"
  python3 - "$JSON_DIR" "$SHARD_JSON_DIR" "$SHARD_INDEX" "$N_SHARDS" <<'PY'
import os, sys, shutil
from pathlib import Path
src, dst, idx, n = sys.argv[1:5]
idx, n = int(idx), int(n)
docs = sorted(Path(src).iterdir())
mine = [d for d in docs if int(d.stem.split("-")[1]) % n == idx]
for d in mine:
    # symlink to avoid copying ~50MB; idempotent
    target = Path(dst) / d.name
    if not target.exists():
        os.symlink(d.resolve(), target)
total = len(docs)
print(f"  shard {idx}/{n}: {len(mine)} of {total} docs ({100*len(mine)/total:.1f}%) → {dst}")
PY
fi

# Per-shard FIM bin so workers don't clobber each other if they ever
# run on the same machine. Shard suffix in path keeps it isolated.
FIM_BASE=/tmp/mmllm-cpu/fim-json-shard-${SHARD_INDEX}-of-${N_SHARDS}
if [ ! -f "${FIM_BASE}.train.bin" ]; then
  mmllm fim-build-corpus json "$SHARD_JSON_DIR" "$FIM_BASE" 0.7 0.5 42
fi

# ── 2. Resume seed staging ──────────────────────────────────────────────────
if [ -n "${RESUME_FROM:-}" ] && [ -f "${RESUME_FROM}" ]; then
  rm -rf "${FIM_BASE}.ckpts"
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${RESUME_FROM}" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  echo "  resuming from ${RESUME_FROM} (staged at step-1; ckpts dir wiped first)"

  # Round-7: write an empty opt-sparse-net.pt so the warm-start gate
  # also recognizes "NetBank state already present" via the existing
  # path-existence check. Belt-and-suspenders alongside the env knob.
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Expand harvested NetBank V (round-6 fp16) into the runtime mmap.
  RESUME_DIR=$(dirname "${RESUME_FROM}")
  python3 - "${RESUME_DIR}" "/tmp/mmllm-cpu/fim-bank-shard-${SHARD_INDEX}" <<'PY'
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
    print(f"  NetBank V layer {layer} restored from round-6 core "
          f"({out.stat().st_size/1e6:.1f} MB fp32 expanded from {fp16_file.stat().st_size/1e6:.1f} MB fp16)")
if restored == 0:
    print(f"  WARN: no bank-net-latest.*.fp16.bin in {resume_dir} — NetBank V will be uninitialized")
else:
    print(f"  ✓ {restored} NetBank V layers carried forward from round-6 community core")
PY
fi

# ── 3. Train (sharded) ──────────────────────────────────────────────────────
BANK_BASE=/tmp/mmllm-cpu/fim-bank-shard-${SHARD_INDEX}
TRAIN_LOG=/tmp/mmllm-cpu/round7-${HANDLE}.train.log
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-250}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi

FIM_EVAL_LOG=/tmp/mmllm-cpu/round7-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round7-${HANDLE}.agent-eval.txt
mmllm eval-agent "$FIM_BASE" "${TOTAL_STEPS}" "$BANK_BASE" \
    "$SRC/xlam-synth.test.bin" xlam 100 256 2>&1 | tee "$AGENT_EVAL_LOG" || true

# ── 5. Stage worker output + meta.json ──────────────────────────────────────
WORKER_DIR="workers/$HANDLE/step-${TOTAL_STEPS}"
mkdir -p "$WORKER_DIR"
cp "${FIM_BASE}.ckpts/step-${TOTAL_STEPS}/dense.pt" "$WORKER_DIR/dense.pt"

# NetBank V → fp16 for upload (under GitHub's 100 MB blob limit)
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
          f"({dst.stat().st_size/1e6:.1f} MB fp16)")
PY

cp "${FIM_BASE}.log.jsonl" "$WORKER_DIR/log.jsonl" 2>/dev/null || true

python3 - "$HANDLE" "$SHARD_INDEX" "$N_SHARDS" "$TRAIN_LOG" "$FIM_EVAL_LOG" \
        "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, shard, n_shards, tlog, felog, aelog, wdir, total_steps = sys.argv[1:9]
shard, n_shards, total_steps = int(shard), int(n_shards), int(total_steps)
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
        try:    ev = json.loads(line)
        except: continue
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
    "round":          7,
    "tokens_trained": tokens_trained,
    "steps":          total_steps,
    "label":          handle,
    "shard_index":    shard,
    "n_shards":       n_shards,
    "fim": {
        "language":           "json",
        "fim_ratio":          0.7,
        "psm_ratio":          0.5,
        "splitter":           "json-value-boundary",
        "source_corpus":      f"synthetic-xlam shard {shard}/{n_shards} (hash by doc id)",
        "sleep_cycle_every":  1000,
        "distill_coef":       0,
        "resume_from":        "core/round-6/step-5000 (FedAvg merge of 5 round-6 workers)",
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
JOURNAL="docs/journal/${TS}-round7-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 7 — Sharded corpus + harvested-NetBank resume — ${HANDLE}

## Mechanism
- shard: ${SHARD_INDEX}/${N_SHARDS} (hash-by-doc-id of xlam-synth)
- resume from: core/round-6/step-5000 (FedAvg merge of 5 round-6 workers,
  fim_eval=5.804, format_validity=0.110)
- NetBank V: loaded from round-6 harvested fp16, warm-start suppressed
- sleep cycle: V_local ← 0 every ${MMLLM_SLEEP_CYCLE_EVERY} steps
- distill: OFF; replay: OFF; LR_bank=1× LR_net=10× (round-6 settings)

## Round-6 → 7 baseline
| metric | round-2 → round-6 (5×same-corpus) | what round-7 is testing |
|---|---|---|
| best individual fim_eval | 6.204 (ctyiz) | does sharding produce DIVERGENT specialists |
| FedAvg merged | 5.804 | such that the harvest's merge benefit grows |
| distill merged | 5.792-5.809 | beyond what FedAvg = distill achieves |
|                |               | when workers train on the same data |

## Hypothesis
Each shard's worker consolidates a non-overlapping slice of the tool-call
distribution into its NetBank. Harvest (FedAvg or distillation) then has
genuinely complementary content to combine, not 5 near-redundant generalists.

Target: post-harvest fim_eval < 5.5 OR format_validity > 0.150 — beating
round-6's headline by a non-trivial margin.

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- shard: ${SHARD_INDEX} of ${N_SHARDS}
- resume from: ${RESUME_FROM}
- NetBank: enabled, sqrt_n=${MMLLM_NET_SQRT_N}, c_net=${MMLLM_NET_C_NET}

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
<agent: report Δ_net trajectory + sleep-cycle effect, fim_eval vs the
round-6 5.804 baseline, format_validity vs the 0.110 baseline. Did the
worker specialize on its shard (val_bpc compared to round-6's 0.32)?
What's your read on whether harvest will combine constructively across
shards — list the tools your shard's docs emphasize, if obvious from
log inspection.>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push ────────────────────────────────────────────────────────
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts staged at $WORKER_DIR and $JOURNAL"
  echo "── DONE ──  $HANDLE (commit skipped via MMLLM_SKIP_COMMIT)"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-7 worker: ${HANDLE} (shard ${SHARD_INDEX}/${N_SHARDS})"
  git push -u origin "$BRANCH"
  echo "── DONE ──  $HANDLE on $BRANCH"
fi
