# Threaded births (Phase G) — DONE + validated

## Status: IMPLEMENTED, validated end-to-end incl. PAR=16. Default-off; per-process path byte-unchanged.

### What it does
Run a wave's births as THREADS in ONE process (shared ~runtime + shared cold-share
file cache) instead of N bird processes. Memory-density play (single GPU serializes
compute), to lift PAR past the per-process memory wall.

### The surgery (all landed)
1. **`mmllm/mlx/trainer.py` — build lock.** Module-level `_BUILD_LOCK` + `_build_lock_held`
   (thread-local) + `_release_build_lock_if_held()`. In `train_round`, gated on
   `MMLLM_THREADED_BUILD_LOCK=1`: acquire before `build_model` (668), release right
   after `_extract` (974). Serializes the ONLY real hazard — overlapping build spikes
   (what OOM-hangs the box) — one model build resident at a time; training overlaps.
   Default (env unset) → never acquired → byte-identical. ast-verified + import-tested.
2. **`scripts/genesis_threaded_wave.py` — the launcher.** Threads one `run_round` per
   birth, each fully isolated (own torch model, own trainable, own hot StreamV clone,
   own optimizer, own writeback) — NO shared mutable state, so no writeback race / no
   recipe drift; each thread runs the UNMODIFIED train loop. Shares only the process
   runtime + the readonly cold-share inodes (page cache). Thread-local env overlay for
   per-module {HOT_MODULE, COOL_MODULES, MIX, PROBE, LR_DENSE_MULT, MLX_MAX_STEPS,
   LR_ROUND_BASE}. Per-entry K in `WB_MODULES` ("module:K") → several births of the SAME
   module concurrently (ensemble) → PAR can exceed module count.
3. **`scripts/genesis_composed_chain.py` — wiring.** `MMLLM_THREADED_BIRTHS=1` →
   `run_wave_threaded(specs)` spawns ONE launcher process; writes the SAME per-module
   files spawn() does, so `harvest()` is unchanged. Per-module steps/total/trunk-LR ride
   in `WB_{STEPS,TOTAL,DENSE_MULT}_MAP` so ODM + trunk_controller stay faithful. Default
   off → `run_wave` (per-process) unchanged.

### THE KEY FIX — pressure-aware memory guard (not raw free RAM)
Cold-share mmaps ~8GB of readonly V bins (320MB/bin × 32 layers × 4 modules) that page
in during the netbank forward. Those are CLEAN, RECLAIMABLE file-cache pages, but raw
`free`(=free+inactive+speculative) reads the trough as exhaustion and FALSE-ABORTS (the
per-process chain tolerates the identical trough — it has no such gate, relies on OS
reclaim). The poller now gates on the kernel's OWN accounting:
`kern.memorystatus_level` (% available, reclaim-aware) + `kern.memorystatus_vm_pressure_level`
(1/2/4). Abort only on pressure≥4 (critical) or level < `WB_MEM_FLOOR_PCT` (6%). Start
backpressure: `WB_MEM_GATE_PCT` (15%). This is the real box-hang guard, tolerant of
reclaimable cache. (Earlier raw-free aborts at 1.5-1.9GB were ALL this false-positive.)

### Validated (this session, off f256round100 seed, full H-Net prod env)
- 1 birth: build→8 steps→StreamV writeback (38668 rows)→versioning (32 snapshots, delta
  sidecars)→composed_bpc 4.99. 81s. level held 73%.
- 2 concurrent: text+math, both trained+wrote back independently, 133s (not 162 → overlap),
  level 74-75%. Build lock serialized text→release→math cleanly.
- **16 concurrent (4 modules × 4 K-births): all 16 build+train+writeback, 0 errors. mem
  level dipped to ~34%/pressure-2 (warn) at peak then recovered to 68%+/pressure-1 as
  births finished. PAR=16 FITS on 32GB.**

### Run it
- Standalone scaling test: `scratchpad/runcheck_par16.sh` (16 births, STEPS=4).
- In the chain: add `MMLLM_THREADED_BIRTHS=1` to run_next.sh's env. For PAR>module-count
  (ensemble), the chain currently emits 1 birth/module; to do 4×4 in-chain, generate
  ensemble specs (module:K) — straightforward follow-up.

### Notes / follow-ups
- Compute is GPU-serialized: 16 births ≈ 16× single-birth compute wall-clock (time-sliced),
  NOT faster — the win is memory-density + harvest diversity, as designed.
- `MMLLM_BATCH=1` MUST be set (launcher does it) — pick-batch default=4 → 4× activation RAM.
- corpus→module "text-10g not in modules" warning is PRE-EXISTING (matches the bird);
  isolation comes from HOT_MODULE stop-grad, not the corpus tag. Benign.
