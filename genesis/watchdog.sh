#!/usr/bin/env zsh
# OVERNIGHT WATCHDOG for the f256x chain. Keeps a chain RUNNING + making PROGRESS:
#  • chain process gone + not at wave 100  → relaunch.
#  • THREADED crashes ≥2× WITHOUT advancing the wave → FALL BACK to the proven
#    per-process run_next.sh (so progress continues regardless).
#  • progress made (wave advanced) → reset the failure counter (keep using threaded).
#  • chain genuinely DONE (wave 100) → exit.
# Stop it with:  pkill -f watchdog.sh
set -u
G=$HOME/models/genesis
TAG=${WAVE_TAG:-f256x}                     # tag-aware: guard whichever chain we launched
WLOG=$G/logs/watchdog.log
CHAINLOG=$G/logs/genesis_${TAG}.log
THREADED=$G/scripts/run_next_threaded.sh
PERPROC=$G/scripts/run_next.sh
SCRIPT=$PERPROC                           # PRIMARY = proven per-process (threaded hits a hard Metal
                                          # per-context buffer limit 499000 with 2+ sustained births).
FAILS=0
FALLBACK_AT=99                            # no fallback needed — already on the proven path
cur_wave() { grep -oE 'WAVE [0-9]+/' $CHAINLOG 2>/dev/null | grep -oE '[0-9]+' | sort -n | tail -1; }
log() { echo "$(date '+%Y-%m-%d %H:%M:%S')  $1" >> $WLOG; }
log "watchdog START — guarding $SCRIPT (fallback→per-process after ${FALLBACK_AT} no-progress crashes)"
LAST_WAVE=$(cur_wave); LAST_WAVE=${LAST_WAVE:-0}
LAST_PROGRESS_TS=$(date +%s)
STALL_SECS=5400                           # 90 min with no wave advance + a wave running = STUCK → relaunch
# give the run that's already up a chance before judging
sleep 60
while true; do
  NOW_W=$(cur_wave); NOW_W=${NOW_W:-0}
  if [ "$NOW_W" -gt "$LAST_WAVE" ]; then log "progress: wave $LAST_WAVE → $NOW_W"; LAST_WAVE=$NOW_W; LAST_PROGRESS_TS=$(date +%s); FAILS=0; fi
  if pgrep -f genesis_composed_chain.py >/dev/null 2>&1; then
    # alive — but is it STUCK? (no wave progress for STALL_SECS while a chain is up)
    if [ $(( $(date +%s) - LAST_PROGRESS_TS )) -ge "$STALL_SECS" ]; then
      FAILS=$((FAILS+1))
      if [ "$SCRIPT" = "$THREADED" ] && [ "$FAILS" -ge "$FALLBACK_AT" ]; then
        log "THREADED STALLED ${FAILS}× (no progress ${STALL_SECS}s, wave $NOW_W) — FALLING BACK to per-process"
        SCRIPT=$PERPROC; FAILS=0
      fi
      log "chain STUCK at wave $NOW_W (no progress ${STALL_SECS}s, fails=$FAILS) — killing + relaunch $(basename $SCRIPT)"
      pkill -f genesis_threaded_wave 2>/dev/null; pkill -f genesis_composed_bird 2>/dev/null
      pkill -f genesis_composed_chain 2>/dev/null; sleep 4
      WAVE_TAG=$TAG MMLLM_ALLOW_ARCH_GROWTH=1 zsh $SCRIPT >> $WLOG 2>&1; LAST_PROGRESS_TS=$(date +%s); sleep 45
    else
      FAILS=0                             # alive & progressing (or within the stall window)
    fi
  else
    NOW=$(cur_wave); NOW=${NOW:-0}
    if grep -q "COMPOSED-GENESIS DONE" $CHAINLOG 2>/dev/null && [ "$NOW" -ge 100 ]; then
      log "chain DONE at wave $NOW — watchdog exiting"; break
    fi
    if [ "$NOW" -gt "$LAST_WAVE" ]; then   # progress since last crash → threaded is working
      log "progress: wave $LAST_WAVE → $NOW; resetting fail counter"; FAILS=0; LAST_WAVE=$NOW
    fi
    FAILS=$((FAILS+1))
    if [ "$SCRIPT" = "$THREADED" ] && [ "$FAILS" -ge "$FALLBACK_AT" ]; then
      log "THREADED crashed ${FAILS}× without advancing past wave $NOW — FALLING BACK to per-process (run_next.sh)"
      SCRIPT=$PERPROC; FAILS=0
    fi
    log "chain DOWN (wave=$NOW, fails=$FAILS) — pkill stragglers + relaunch $(basename $SCRIPT)"
    pkill -f genesis_threaded_wave 2>/dev/null; pkill -f genesis_composed_bird 2>/dev/null
    pkill -f genesis_composed_chain 2>/dev/null; sleep 4
    WAVE_TAG=$TAG MMLLM_ALLOW_ARCH_GROWTH=1 zsh $SCRIPT >> $WLOG 2>&1
    sleep 45                              # let it boot before the next health check
  fi
  sleep 60
done
