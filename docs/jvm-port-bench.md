# JVM port M6 benchmark — per-router thread parallelism

Deliverable of spec §10 / milestone M6 (docs/jvm-port-spec.md): steps/s
of the full 16-router sym24 train step vs thread count, against the
torch reference on the same box. Correctness of the parallel step is
gate G6 (`mmllm.jvm.thread-parity`), not this document — every number
here was measured AFTER G6 passed (16-thread ≡ 1-thread bit-identical).

## Environment

- 4-core Intel Xeon @ 2.10 GHz, 15 GB RAM (a CI-class box; the spec's
  16-thread payoff scenario needs a ≥16-core machine — see caveats)
- OpenJDK 21, `-XX:+UseParallelGC`, `_JAVA_OPTIONS=-Xmx11g`
- torch 2.12.1+cpu (MKL), same `.venv` the reference trains with
- 2026-07-04, branch claude/diamond-onnxrt-portability-4t9t8y

## Workload

One full sym24 prod-recipe train step at effective batch 16
(16 routers × B=1, trunk_ids 0..15), T=64, KD_EVERY=2 — so each
config's 4 timed steps are 2 KD steps (main + teacher + student
forwards, main + student backwards) and 2 non-KD steps. NetBank delay
0, PKM C++ kernels off (inert at cpu-mini per CLAUDE.md), synthetic
byte batch, mid-warmup prod lrs. Both runtimes execute the identical
recipe math; the JVM side is `mmllm.jvm.bench-step` (fresh env per
config, untimed JIT warmup first), the torch side is
`scripts/bench_torch_step.py` calling the core.lpy `train-step` var —
i.e. the whole reference stack including Basilisp dispatch, which is
the thing the port replaces.

Commands:

    _JAVA_OPTIONS=-Xmx11g jvm/run.sh -m mmllm.jvm.bench-step 64 4 seq 1 2 4 8 16
    .venv/bin/python scripts/bench_torch_step.py --T 64 --steps 4 --grad-checkpoint false
    .venv/bin/python scripts/bench_torch_step.py --T 64 --steps 4 --grad-checkpoint false --threads 1

## Results (T=64, B=16 effective, 4 steps/config)

JVM (per-router platform threads, deterministic mode — which is the
only mode; the parallel step is bit-deterministic by construction):

| config                  | total(s) | steps/s | speedup vs 1-thread | median kd / non-kd step |
|-------------------------|---------:|--------:|--------------------:|------------------------:|
| sequential `train-step!`|    306.2 |  0.0131 |               1.00× |         97.2 s / 55.9 s |
| parallel, 1 thread      |    307.5 |  0.0130 |               1.00× |         99.0 s / 54.8 s |
| parallel, 2 threads     |    175.1 |  0.0228 |               1.76× |         54.4 s / 33.1 s |
| parallel, 4 threads     |    114.9 |  0.0348 |               2.68× |         37.1 s / 20.4 s |
| parallel, 8 threads     |    119.7 |  0.0334 |               2.57× |         35.5 s / 24.4 s |
| parallel, 16 threads    |    119.8 |  0.0334 |               2.57× |         37.1 s / 22.8 s |

torch reference (single process, one B=16 tensor, MKL intra-op):

| config                  | steps/s | median kd / non-kd step | vs JVM best (4 thr) |
|-------------------------|--------:|------------------------:|--------------------:|
| torch, 1 intra-op thread|  0.1076 |          12.2 s / 6.4 s |                   — |
| torch, 4 intra-op threads| 0.1897 |           7.0 s / 3.6 s |               5.45× |

## Reading the numbers honestly

- **The scaling curve is the port's deliverable, and it's real.** The
  parallel path costs nothing at 1 thread (307.5 s vs 306.2 s
  sequential, +0.4%), scales 1.76× at 2 and 2.68× at 4 threads (67%
  parallel efficiency on 4 cores, GC and the single-threaded optimizer
  phase eat the rest), and degrades gracefully — not catastrophically —
  when oversubscribed past the core count. For comparison, giving torch
  the same 4 cores via MKL intra-op threading yields only 1.76×
  (44% efficiency): at d_model=32 the matrices are too small for
  intra-op threading, exactly the spec §10 premise. Outer per-router
  parallelism is the right axis; this box just runs out of cores at 4.
- **Absolute throughput: torch wins by 8.3× at 1 thread** (0.1076 vs
  0.0130 steps/s). That is the kernel gap: the JVM port's tensor ops
  are hand-rolled scalar loops (deliberately, for auditable parity
  through M5), vs MKL GEMMs + vectorized everything. The gap narrows to
  5.45× at full box because the JVM out-scales torch, but closing the
  rest belongs to the planned Neanderthal/MKL backend swap behind
  tensor.clj (deps.edn already stages the dep) — NOT to more threads.
  Extrapolating the measured efficiencies, JVM×16 threads on a
  ≥16-core box (~0.13 steps/s at 60% efficiency) would roughly match
  torch×4-cores with today's naive kernels; with MKL-backed kernels the
  16-router step would be decisively ahead. That claim needs a big-box
  measurement before it's treated as fact.
- **16-thread numbers here are NOT the spec's 16-thread scenario.**
  nproc=4: the 8/16-thread rows only demonstrate oversubscription
  behavior (flat, ~4% worse than 4 threads). Per the M6 instructions
  the curve is benched to nproc; re-run on ≥16 cores for the headline.

## Why T=64 (not T=1024, not T=256)

- RAM, not wall clock, is the binding constraint — and it's the JVM
  port's own data structures, stated plainly: sparse V grads / Adam
  moments / bank overlays are boxed `HashMap<Long, float[]>` rows at
  ~115 B per touched row. A B=16 step touches ~min(T·512·16, 1024²)
  V_net rows per layer × 32 layers: at T=64 that's ~0.4 M rows/layer
  (≈9 GB peak across per-task grads + merged grads + moments + overlays
  — measured fine under Xmx11g); at T=256 it saturates toward 1 M
  rows/layer and the projected footprint exceeds the 15 GB box, and
  T=1024 is far past it. The torch reference packs the same data as
  flat tensors (~3.5× denser, no boxing) and fits T=1024 with
  grad-checkpointing on a 15 GB CI box. **Follow-up for production-scale
  JVM training: packed (primitive-array / index-sorted) sparse
  accumulators and moment stores.** Wall clock would also have been
  unreasonable (a 1-thread T=1024 step extrapolates to tens of
  minutes), but memory alone forces the fallback.
  **Landed (M7, jvm/src/mmllm/jvm/rowstore.clj):** sparse V grads,
  sparse-Adam moments and bank overlays now live in packed
  open-addressing row stores (long-key table + chunked float pools,
  ~2-3× denser than the boxed rows, and the hogwild V_local container
  is per-trunk-sharded instead of a ConcurrentHashMap). All five parity
  gates stayed green across the swap (bit-identical semantics);
  thread-parity now fits in -Xmx6g (was 11g). The G5 spoon
  (mmllm.jvm.spoon) trains T=128 × B=16 × 100 steps in ~12 GB peak RSS
  on the 15 GB box — memory no longer forces T=64. On THIS 4-core box
  the binding constraint at T=256 is now wall clock (~3 h for 100
  steps, extrapolated from ~37 s/step measured at T=128), not RAM.
- Same-T comparison is preserved: torch was measured at T=64 too, with
  `MMLLM_GRAD_CHECKPOINT=false` — the honest equivalent, since the JVM
  backward never materializes (T,T) attention and never pays torch's
  checkpoint recompute (spec §9). Prod CI runs torch WITH checkpointing
  (memory fit), which is slower than the torch numbers above — so the
  torch column is torch at its best.

## Other caveats

- KD steps dominate (2 of 4 steps): they cost ~1.8× a plain step on
  both runtimes (3 forwards + 2 backwards vs 1+1). Medians are reported
  per class; steps/s mixes them 50/50 like the prod cadence.
- The G6 gate additionally pins the parallel path's numerics: 1-thread
  vs 16-thread bit-identical (grads, post-step params, touched V rows,
  loss scalars); loss scalars bit-identical to the SEQUENTIAL step;
  dense/V_net grads within 1e-5 relative of sequential (fp
  reassociation from per-task partial sums); V_local grads bit-identical
  to sequential (single-writer trunk slices).
- Timing noise: single run per config, 4 steps each, quiet box. Spread
  between the two same-cost configs (8 vs 16 threads: 0.1%) suggests
  ~±2% noise; the 1-thread-vs-sequential delta (0.4%) is within it.
- tokens/s, if you prefer that unit: steps/s × 1024 tokens (16 rows ×
  T=64). JVM 4-thread ≈ 35.6 tok/s; torch 4-thread ≈ 194 tok/s.
