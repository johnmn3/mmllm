#!/usr/bin/env bash
# run_local_bird.sh — run THIS machine as a first-class mmllm bird.
#
# Trains a few 50-step rounds on local silicon (Apple-Silicon MPS / CUDA / CPU)
# and pushes the minimal changeset (a claude/train-sym24-… branch) to your fork,
# exactly like a GitHub-Actions fork bird. Upstream's hourly harvest then scans
# forks and FedAvg-merges your contribution into the chain. It routes through
# scripts/train.sh, so a local bird is byte-identical to a fork bird — just on
# your hardware, which is usually much faster than the 7 GB CI runner.
#
# ── One-time setup ──────────────────────────────────────────────────────────
#   1. Fork  github.com/johnmn3/mmllm  and clone YOUR fork; cd into it.
#   2. gh auth login            (GitHub CLI, with push access to your fork)
#   3. Install uv               (https://docs.astral.sh/uv/) — env auto-bootstraps.
#
# ── Usage ───────────────────────────────────────────────────────────────────
#   bash scripts/run_local_bird.sh [N_ROUNDS]     # default 5 rounds × 50 steps
#   MMLLM_DEVICE=cpu bash scripts/run_local_bird.sh 3   # force CPU, 3 rounds
set -euo pipefail

UPSTREAM="johnmn3/mmllm"
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "✗ not in a git repo — clone your fork of $UPSTREAM first."; exit 1; }
cd "$ROOT"
N_ROUNDS="${1:-5}"

# ── 1) Python env — auto-bootstrap with uv ──────────────────────────────────
[ -z "${VIRTUAL_ENV:-}" ] && [ -f .venv/bin/activate ] && source .venv/bin/activate
if ! python3 -c 'import mmllm' >/dev/null 2>&1; then
  echo "▶ bootstrapping venv (mmllm not importable)…"
  if ! command -v uv >/dev/null 2>&1; then
    echo "✗ need 'uv' to bootstrap the env:  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "  (or make your own venv with python>=3.10 and 'pip install -e .')"
    exit 1
  fi
  uv venv --python 3.12
  source .venv/bin/activate
  # Pin basilisp to the prod wheel version (avoids the resolver picking a
  # pre-3.12 basilisp off the >=0.3 floor).
  uv pip install -e . 'basilisp==0.5.1'
  python3 -c 'import mmllm' >/dev/null 2>&1 || { echo "✗ mmllm still not importable after bootstrap."; exit 1; }
fi
echo "✓ env ready (python $(python3 -c 'import sys;print(".".join(map(str,sys.version_info[:3])))'), mmllm importable)"

# ── 2) Preflight — gh auth + push target ────────────────────────────────────
command -v gh >/dev/null 2>&1 || { echo "✗ need GitHub CLI 'gh':  https://cli.github.com"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "✗ run 'gh auth login' first (the bird pushes to your fork)."; exit 1; }
ORIGIN_URL=$(git remote get-url origin 2>/dev/null || true)
[ -n "$ORIGIN_URL" ] || { echo "✗ no 'origin' remote — clone your fork of $UPSTREAM."; exit 1; }
ORIGIN_SLUG=$(echo "$ORIGIN_URL" | sed -E 's#.*github\.com[:/]##; s#\.git$##')
if [ "$ORIGIN_SLUG" = "$UPSTREAM" ]; then
  echo "✓ origin = $ORIGIN_SLUG (upstream itself — fine if you have write access)"
else
  echo "✓ origin = $ORIGIN_SLUG (bird branch pushes here; $UPSTREAM harvest scans forks)"
fi

# ── 3) Device + threads ─────────────────────────────────────────────────────
if [ -z "${MMLLM_DEVICE:-}" ]; then
  if python3 -c 'import torch,sys; sys.exit(0 if torch.backends.mps.is_available() else 1)' 2>/dev/null; then
    MMLLM_DEVICE=mps
  elif python3 -c 'import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)' 2>/dev/null; then
    MMLLM_DEVICE=cuda
  else
    MMLLM_DEVICE=cpu
  fi
fi
export MMLLM_DEVICE
if [ "$MMLLM_DEVICE" = mps ] || [ "$MMLLM_DEVICE" = cuda ]; then
  export PYTORCH_ENABLE_MPS_FALLBACK=1     # unsupported ops fall back to CPU (never blocks)
  export MMLLM_ENABLE_PKM_CPP=false        # C++ PKM kernel is CPU-only; GPU uses torch ops
  echo "  device=$MMLLM_DEVICE — full retrieval bandwidth (design defaults)"
else
  # Reduced bandwidth on CPU for tractability (top-k is not a bank dim — same
  # checkpoint either way). Mirrors scripts/run_port_distill.sh.
  export MMLLM_MEMORY_TOP_K="${MMLLM_MEMORY_TOP_K:-16}" MMLLM_MEMORY_SUB_TOP_K="${MMLLM_MEMORY_SUB_TOP_K:-16}"
  export MMLLM_NET_TOP_K="${MMLLM_NET_TOP_K:-64}"       MMLLM_NET_SUB_TOP_K="${MMLLM_NET_SUB_TOP_K:-8}"
  export MMLLM_ENABLE_PKM_CPP=false
  echo "  device=cpu — reduced bandwidth for tractability"
fi
if [ -z "${MMLLM_NUM_THREADS:-}" ]; then
  if [ "$(uname -s)" = Darwin ]; then
    MMLLM_NUM_THREADS=$(sysctl -n hw.perflevel0.logicalcpu 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 8)
  else
    MMLLM_NUM_THREADS=$(nproc 2>/dev/null || echo 8)
  fi
fi
export MMLLM_NUM_THREADS

# ── 4) Bird identity + dose ─────────────────────────────────────────────────
# Stable per-host handle so this box is recognizable in the chain's contributors.
HOST_TAG=$(python3 -c "import hashlib,socket; print('L'+hashlib.sha1(socket.gethostname().encode()).hexdigest()[:4])")
export MMLLM_HANDLE="${MMLLM_HANDLE:-$HOST_TAG}"
export MMLLM_N_ROUNDS="$N_ROUNDS"
export MMLLM_STEPS_PER_ROUND="${MMLLM_STEPS_PER_ROUND:-50}"
export MMLLM_CHAIN_PREFIX="${MMLLM_CHAIN_PREFIX:-sym24}"
export MMLLM_LOCAL_BIRD=1     # train.sh: skip linux offline wheels (use this venv)

echo "▶ local bird  handle=$MMLLM_HANDLE  device=$MMLLM_DEVICE  threads=$MMLLM_NUM_THREADS  dose=${MMLLM_N_ROUNDS}×${MMLLM_STEPS_PER_ROUND}  chain=$MMLLM_CHAIN_PREFIX"
echo "  → scripts/train.sh: fetch head+corpora from $UPSTREAM releases → train on-device → push to $ORIGIN_SLUG (chunked, self-pruning)"

# ── 5) Run the bird (identical path to a fork bird) ─────────────────────────
exec bash scripts/train.sh
