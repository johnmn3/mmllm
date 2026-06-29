#!/usr/bin/env zsh
# ─────────────────────────────────────────────────────────────────────────────
# NEXT CONTINUATION — off f256round100 (RB(100)), restored real source.
# Launches EXACTLY like f256 did: PAR=4, NO free-RAM gate, NO per-bird memory cap.
# f256's real memory safeguards are where they always were:
#   • WAVE_STAGGER=3   — staggers the 4 bird spawns so they don't all peak at once
#   • bird MLX_CACHE_MB — caps the MLX buffer cache (genesis_composed_bird.py)
#   • StreamV / NET_CACHE_ROWS — bounded LRU bank cache (set in the bird)
#   • chain @@@JANITOR + WAVE_KEEP — GCs consumed scratch each wave
#   • iogpu.wired_limit_mb — yours to set via sudo for a hard system ceiling
# BASE = verified-exact f256 recipe.  NEW WORK fenced below (Tier-1/2 + #55 sweep).
# ─────────────────────────────────────────────────────────────────────────────
set -e
G=$HOME/models/genesis
SRC=$G/mmllm-src
VENV=/Users/john/src/mmllm/.venv/bin/python3
TAG=${WAVE_TAG:-f256x}
SEED=${WAVE_SEED:-f256round100}
PAR=${WAVE_PAR:-2}                        # PAR=2: H-Net smoke (hnsmoke2, 2026-06-28) showed avail troughs
                                          # to ~3.5GB free at PAR=2/T=384 → PAR=4 would OOM-hang the 32GB box.
# ── LONG-RUN GUARD (H-Net smoke hnsmoke2 FAILED on DISK — now FIXED via cold-share) ───────────────────
#   hnsmoke2 (PAR=2,T=384): H-Net mechanics all GREEN (build, chunking, trie leaf-fill+revive, per-bird
#   harvest+reseed, versioning .ver/.vidx deltas, bpc) — but wave 1 died at the 4th bird (code) with
#   [Errno 28] No space left on device. ROOT CAUSE: the torch NetBank build RECREATES (w+) every module's
#   bin at full dense size (144 blocks × 32 layers ≈ 9.2GB/module), so EACH bird materialized all 4 modules
#   (~37GB) and 4 birds/wave accumulated ~145GB before the wave-end GC — disk-full.
#   FIX (2026-06-28): MMLLM_NET_COLD_SHARE=1 (in the H-Net block below). Each bird clones+recreates ONLY its
#   hot module; the 3 cold modules are read READ-ONLY from the shared immutable round-bank inode (torch
#   mmap mode=r + StreamV readonly), made corruption-safe by VERSIONING's immutable base snapshot. Cold
#   modules emit no deltas / never write. MEASURED collapse (cswith vs cswithout, real 4-bird wave):
#   per-wave peak disk 39GB WITH vs ~145GB WITHOUT (~4x); harvest + versioned netver-delta sidecars fire.
WAVE_N=${WAVE_N:-2}                        # kept LOW for now (smoke). Disk blocker fixed → safe to set 100 for the long run.

echo "── pre-flight (correctness only — NO RAM gate) ──"
ls $G/$SEED.ckpts/step-*/dense_named.pt >/dev/null 2>&1 || { echo "ABORT: seed ckpt $SEED missing"; exit 1; }
ls $G/$SEED-bank-net.text.0.bin        >/dev/null 2>&1 || { echo "ABORT: seed banks $SEED missing"; exit 1; }
PYTHONPATH=$SRC $VENV -c "import basilisp.main as m; m.init(); import mmllm.core, mmllm.mlx, mmllm.mlx.stream_v" >/dev/null 2>&1 \
  || { echo "ABORT: restored source failed to import"; exit 1; }
# CONTINUE the global step counter from the seed's checkpoint instead of resetting to the 1437
# default. Without this, total (≈1437) < resume_step (199937) → trainer clamps n_steps to 1
# (the 1-step-per-wave bug). f256 only worked because its g256 seed sat near the default.
SEED_STEP=$(ls $G/$SEED.ckpts 2>/dev/null | grep -oE 'step-[0-9]+' | grep -oE '[0-9]+' | sort -n | tail -1)
[ -z "$SEED_STEP" ] && { echo "ABORT: can't read seed step from $SEED.ckpts"; exit 1; }
echo "  seed + source OK | PAR=$PAR, 100 waves × 500 steps | continuing from step $SEED_STEP"

# wake/sleep cycle, hot-reloadable mid-run. cycle-1 = f256's ENDGAME shape (period-5); from
# cycle-2 the structural sweep draws a fresh shape per cycle (period spans 5→12).
cat > $G/${TAG}_live.json <<JSON
{ "WAVE_TRUNK_CYCLE_PERIOD": 5, "WAVE_TRUNK_CYCLE_WARM": 2, "WAVE_TRUNK_CYCLE_WARM_MULT": 0.25,
  "WAVE_TRUNK_CYCLE_COOL_MULT": 0.25, "WAVE_TRUNK_CYCLE_COOL_DECAY": 0.80, "WAVE_TRUNK_CYCLE_JITTER": 0.15 }
JSON

echo "── launching $TAG ──"
caffeinate -i nohup env \
  `# ===== f256-EXACT BASE =====` \
  WAVE_MODULES="text,math,agentic,code" WAVE_N=${WAVE_N:-100} WAVE_PAR=$PAR WAVE_STEPS=${WAVE_STEPS:-500} \
  WAVE_STAGGER=3 WAVE_REPORT=15 WAVE_KEEP=3 WAVE_SEED=$SEED WAVE_TAG=$TAG WAVE_BASE_STEP=$SEED_STEP \
  WB_BATCH=1 WB_D_MODEL=256 WB_D_FF=768 WB_N_BLOCKS=160 WB_DENSE_MULT=1.0 WB_DENSE_WD=5e-5 \
  MMLLM_LR_BATCH_SCALE=sqrt MMLLM_SHORT_WINDOW=256 MMLLM_LONG_WINDOW=256 \
  MMLLM_STRATIFIED=1 MMLLM_STRAT_BUCKETS="256:0.7,512:0.3" \
  WAVE_LATE_FRAC=0.22 WAVE_LATE_DECAY=0.90 \
  WAVE_TRUNK_CYCLE_PERIOD=5 WAVE_TRUNK_CYCLE_WARM=2 WAVE_TRUNK_CYCLE_WARM_MULT=0.25 \
  WAVE_TRUNK_CYCLE_COOL_MULT=0.25 WAVE_TRUNK_CYCLE_COOL_DECAY=0.80 \
  WAVE_TRUNK_CYCLE_JITTER=0.15 WAVE_JITTER_SALT=2 \
  `# ===== NEW WORK (Tier-1 router learning) =====` \
  MMLLM_NET_ROUTER=true MMLLM_NET_ROUTER_BIAS_U=0.002 MMLLM_NET_ROUTER_GATE=sigmoid \
  MMLLM_NET_ROUTER_AUX_COEF=0.1 \
  `# ===== NEW WORK (Tier-2 ODM) =====` \
  WAVE_ODM=1 WAVE_ODM_GAMMA=0.1 WAVE_ODM_ETA=0.3 \
  `# ===== NEW WORK (#55 structural sweep) =====` \
  WAVE_TRUNK_SWEEP=1 WAVE_SWEEP_PERIOD_MIN=5 WAVE_SWEEP_PERIOD_MAX=12 \
  WAVE_SWEEP_WARM_MIN=2 WAVE_SWEEP_WARM_MAX=4 \
  WAVE_SWEEP_CREST_MIN=0.25 WAVE_SWEEP_CREST_MAX=0.80 \
  WAVE_SWEEP_DECAY_MIN=0.50 WAVE_SWEEP_DECAY_MAX=0.75 \
  `# ===== H-NET PRODUCTION TURN-ON (smoke-verified at d=256, 2026-06-28) ===========================` \
  `#  NOTE: the all-32 "fix-forward" stanza (LOCAL_BANK_LAYERS=0..31 + dup NET_USE_ALL32 + WB_LOCAL_MULT` \
  `#  + ABLATE_LOCAL) was DROPPED here — the depth-2 trie IS the memory scheme now; local-everywhere is` \
  `#  redundant and adds memory pressure. The H-Net block keeps its own NET_USE_ALL32=1 below.` \
  `#  Gated stack: H-Net spine (enc/chunker/trunk@chunk-rate/dec) + depth-2 trie NetBank w/ VQ-revive` \
  `#  + 8-head MTP + n-gram hash features + Phase-D netbank versioning (COW .ver/.vidx delta sidecars).` \
  `#  TRIE RECONCILIATION (n_blocks = branch^depth, overrides WB_N_BLOCKS): depth=2, branch=12 → 144.` \
  `#  WHY 144 not ~160: bird clones the seed's 160-block V bin; StreamV._read_row preads by raw offset` \
  `#  with NO EOF guard, so any leaf id >=160 would pread past EOF → frombuffer broadcast CRASH. 144<=160` \
  `#  keeps EVERY leaf in-bounds of the cloned bin, = ~90% of today's V (memory "~=160"), no resize, no` \
  `#  crash. WB_N_BLOCKS=144 here OVERRIDES the base 160 so the bird's declared n_blocks matches the trie.` \
  MMLLM_HNET=1 MMLLM_NET_USE_ALL32=1 MMLLM_NET_MODULES=text,math,agentic,code \
  MMLLM_NET_TRIE_DEPTH=2 MMLLM_NET_TRIE_BRANCH=12 WB_N_BLOCKS=144 \
  MMLLM_NET_VQ_REVIVE=true MMLLM_NET_VQ_REVIVE_EVERY=50 \
  MMLLM_MTP_COEF=0.1 MMLLM_MTP_HEADS=8 MMLLM_NGRAM_HASH=2:4096,3:8192 \
  MMLLM_NET_VERSIONING=1 MMLLM_HNET_RATIO_COEF=0.03 \
  `# COLD-SHARE: the DISK fix. Each bird clones ONLY its hot module (32 bins) and reads the 3 cold` \
  `#  modules read-only from the SHARED immutable round-bank inode (no per-bird clone/recreate). Made` \
  `#  corruption-safe by VERSIONING's immutable base snapshot (cold = mmap mode=r both backends).` \
  `#  Smoke (cswith vs cswithout, 4-bird wave): per-wave peak disk 39GB WITH vs ~145GB WITHOUT (~4x).` \
  MMLLM_NET_COLD_SHARE=1 \
  `# T reduced 1024→384: fits comfortably at PAR=2 on 32GB (~9.9GB free); bird honors WB_SEQ_LEN @bird:88.` \
  WB_SEQ_LEN=384 \
  PYTHONPATH=$SRC $VENV -u $G/scripts/genesis_composed_chain.py >> $G/logs/genesis_${TAG}.log 2>&1 &
echo "  chain pid $! → logs/genesis_${TAG}.log"
if ! pgrep -f train_widget.py >/dev/null 2>&1; then
  WIDGET_TAG=$TAG WIDGET_LOG=$G/logs/genesis_${TAG}.log nohup $VENV $HOME/train_widget.py >/dev/null 2>&1 &
  echo "  widget up (monitoring $TAG)"
fi
echo "── done ──"
