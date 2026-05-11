#!/usr/bin/env bash
# preflight_fim_run.sh — validate everything a FIM dogfood run needs
# BEFORE burning hours of compute.
#
# Exit code 0 = ready to run. Non-zero = stop, fix the listed gaps.
#
# Add new checks here, not in the dogfood prompt. The prompt should
# just call this and trust the result.

set -u
FAIL=0

red()   { printf "\033[31m✗\033[0m %s\n"  "$1"; FAIL=1; }
green() { printf "\033[32m✓\033[0m %s\n"  "$1"; }
yellow(){ printf "\033[33m!\033[0m %s\n"  "$1"; }

echo "── FIM run preflight ──"

# 1. CLI verbs registered
for verb in fim-build-corpus train-fim fim-eval eval-agent; do
  if mmllm 2>&1 | grep -q "$verb"; then
    green "verb: mmllm $verb"
  else
    red   "verb missing: mmllm $verb  (try: pip install -e .)"
  fi
done

# 2. Required scripts present
for f in scripts/prep_xlam_synth.py scripts/build_fim_eval.py; do
  if [ -f "$f" ]; then green "script: $f"
  else                 red   "script missing: $f  (pull the FIM branch — see Setup)"
  fi
done

# 3. Round-N community core to resume from
# Ensure target dir exists BEFORE writing to it (round-3 dispatches hit
# a "no such file or directory" because the mkdir was only in the
# else-branch). Idempotent — always mkdir, then proceed.
mkdir -p /tmp/mmllm-cpu
LATEST_ROUND=$(ls -d core/round-*/step-* 2>/dev/null | sort -V | tail -1)
if [ -n "${LATEST_ROUND}" ] && [ -f "${LATEST_ROUND}/dense.pt" ]; then
  green "community core: ${LATEST_ROUND}/dense.pt ($(du -h "${LATEST_ROUND}/dense.pt" | cut -f1))"
  echo  "RESUME_FROM=${LATEST_ROUND}/dense.pt" > /tmp/mmllm-cpu/preflight.env
else
  yellow "no community core found under core/round-*/  — will start from random init"
  echo  "RESUME_FROM=" > /tmp/mmllm-cpu/preflight.env
fi

# 4. NetBank env vars set (round 2+ goal is Δ_net > 0)
if [ "${MMLLM_NETBANK_ENABLED:-}" = "true" ]; then
  green "MMLLM_NETBANK_ENABLED=true"
else
  red   "MMLLM_NETBANK_ENABLED not 'true' — NetBank won't train (Δ_net will stay 0)"
fi
if [ -n "${MMLLM_NET_SQRT_N:-}" ]; then
  green "MMLLM_NET_SQRT_N=${MMLLM_NET_SQRT_N}"
else
  yellow "MMLLM_NET_SQRT_N unset — defaults to 8192 (~68 GB). Set to 1024 for CPU."
fi

# 5. Data source — synth needs no auth (deliberately, so token gaps can't break us)
if [ -f scripts/prep_xlam_synth.py ]; then
  green "data source: synthetic (no HF auth required)"
else
  red   "scripts/prep_xlam_synth.py missing — falling back to HF xlam needs HF_TOKEN"
fi

# 6. Disk budget — rough check (10k-step run + 512MB NetBank + ckpts ≈ 5 GB)
FREE_GB=$(df -BG /tmp 2>/dev/null | awk 'NR==2 {gsub("G","",$4); print $4}')
if [ -n "${FREE_GB}" ] && [ "${FREE_GB}" -ge 8 ]; then
  green "free disk on /tmp: ${FREE_GB} GB"
elif [ -n "${FREE_GB}" ]; then
  red   "free disk on /tmp: ${FREE_GB} GB (need ≥ 8 GB for 10k-step run + NetBank)"
fi

echo "──"
if [ "$FAIL" -ne 0 ]; then
  echo "PREFLIGHT FAILED — fix the items marked ✗ before running."
  exit 1
fi
echo "PREFLIGHT OK — safe to proceed."
echo "Resume-from path written to /tmp/mmllm-cpu/preflight.env (source it before training)."
exit 0
