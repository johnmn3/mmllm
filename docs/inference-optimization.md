# Inference Optimization Plan

Comprehensive plan for getting mmllm's inference path from "decent
prototype numbers" to "production-quality serving" for both GPU and
CPU deployments. Written 2026-05-03 after the first end-to-end
benchmark of the trained 5B-token checkpoint.

This is a living document. Update bench numbers + cross out items as
they ship.

## Architecture priors

mmllm is a hard-split tiered transformer with three memory tiers per
attention block:

- **Short tier**: 5 RoPE'd Q heads → SDPA over a per-conversation
  in-RAM KV cache (`k-proj-s`, `v-proj-s`).
- **Long tier (KV cache half)**: 7 Q heads → SDPA over a per-conversation
  in-RAM KV cache (`k-proj-l`, `v-proj-l`). Set-style; no RoPE.
- **Long tier (bank half)**: same 7 Q heads project a query into a
  product-key memory bank V (sqrt_n²=4.2M rows × q_dim=224 fp32). The
  bank V lives in either GPU VRAM or as an mmap'd file on disk;
  retrieval is sub-linear top-K via product-key search.

Two architectural facts drive everything in this plan:

1. **Dense parameters are tiny (~10 M)**. The dense path fits in CPU
   L3 cache with room to spare. Per-token dense compute is ~10 M FLOPs
   — nothing for any modern hardware.

2. **Bank V is huge (~18.8 GB at sqrt_n=2048) but read sparsely**.
   Per token, only top-K=16 rows × 224 fp32 = 14 KB are read per layer
   (5 layers → 70 KB / token total). The bank is content-addressed via
   product-key search; nothing else accesses it. The bank's role is
   exactly the same as a trained model weight — just stored in an
   address-by-content layout instead of address-by-position.

The split lets us keep dense weights hot in CPU cache while paging the
bank from disk on demand. The kernel page cache does most of the work:
hot rows stay resident, cold rows fault in. This is the architectural
seam we want to exploit.

## Current bench

5B-trained checkpoint at step 305 000, sqrt_n=2048 (18.8 GB bank V
across 5 layers), batch=1, 50-token warmup before timed run, single
H100 / 8-vCPU container on Modal.

| Setup                                | tok/sec | ms/tok | vs initial baseline |
|--------------------------------------|---------|--------|---------------------|
| H100 + bank in VRAM                  | **206.1** | 4.85 | +18%                |
| H100 + bank in VRAM, torch.compile   | 30.2    | 33.12  | -83% (broken)       |
| 8-vCPU + bank mmap'd disk            | **106.7** | 9.37 | +5%                 |
| 8-vCPU + bank mmap'd disk, compile   | 8.9     | 112.86 | -91% (broken)       |

Initial baseline (basilisp implementation, pre-Phase-1): 174 / 150 / 102 tok/sec.

Quality: BPC=1.27 on Pile-Github val, ablation Δ=+4.77 (bank carries
71 % of useful predictive signal). The bench target is to *keep the
quality* and improve the throughput.

## Phase 1 results

| sub-task | shipped | gain | notes |
|---|---|---|---|
| 1b: thread tuning (`MMLLM_NUM_THREADS`) | yes | ambiguous (interacts with rest) | `cpu_count` default; 1-shot at cli-main |
| 1c: pre-alloc KV cache, 3-tuple | yes | enabled later phases | O(T²) → O(T) memory traffic; cache now `(k_buf, v_buf, pos)` |
| 1a as planned (torch.compile) | **incompatible** | -83% / -91% | sympy `pow_by_natural` failures; recompile thrash; bank's sparse gather untraceable |
| **1a-actual: Python kernel port** | yes | **+18% GPU, +5% CPU** | new `mmllm.attention_kernel`; basilisp shims destructure block once and forward positionally |
| 1d: CUDA graphs | not attempted | — | requires `cudagraph_mark_step_begin` boundaries with the persistent KV buffer; deferred |

`torch.compile` failure modes observed:

- `Dynamo does not know how to trace pvectorc.pvector` — basilisp persistent vectors. Solved by Python-tuple caches.
- `failed while executing pow_by_natural([VR[-12, 0], VR[-1, -1]])` — sympy shape symbolic reasoning crash on the dynamic narrow position in the pre-alloc cache.
- `Cache line invalidated... torch._dynamo hit config.recompile_limit (8)` — cache position changes every token, dynamo specializes per-shape and exhausts compile budget.
- `ProductKeyMemory.forward` sparse gather (`nn.Embedding(sparse=True)` content-addressed top-K) isn't cleanly traceable.

Conclusion: torch.compile in its standard form is incompatible with the bank-V architecture's hot path. Making it work would require carving out a "trace-only" subset (q/k/v projections + SDPA + FFN) excluding the bank lookup and dirty-page tracking. Deferred — the Python kernel port already captured most of the per-token dispatch overhead.

## Phase 3 results (int8 bank V quantization)

Shipped in commit `2aad81c`:

  - `mmllm.memory.Int8ProductKeyMemory` — same product-key search,
    V loaded as fp16 scales + int8 rows, on-the-fly dequant at gather.
  - `quantize_fp32_bank_to_int8_shaped` — streams an fp32 raw bank
    file in chunks, per-row symmetric int8 quantization with
    fp16-stored scale, writes a header-prefixed file.
  - `mmllm bank-quantize` CLI verb + Modal `quantize_bank` function.
  - Build-block reads `MMLLM_BANK_DTYPE` env var to dispatch fp32 vs int8.

Compression at sqrt_n=2048, q_dim=224 (per layer):

  - fp32: ~3.76 GB
  - int8: ~0.94 GB (header + scales + int8 rows)
  - ratio: ~4.0×

Across 5 layers: 18.8 GB → 4.7 GB (4× smaller deploy footprint).

Quantization roundtrip on a synthetic small bank (sqrt_n=8, q_dim=16):

  - mean abs retrieval error: 0.0011
  - relative retrieval error: 0.59%
  - 0 rows clamped on N(0, 0.5²) input

Acceptance test on the trained 5B bank (BPC delta within +0.005)
runs once the 5B+fb training completes and `quantize_bank` runs. The
int8 bench numbers will then update the table at the top of this doc.

## Phase 4 results (mmap layout)

Shipped in commit `<TBD>` (Phase 4b):

  - `_madvise_top_k_pages` helper — issues `MADV_WILLNEED` on the
    pages containing the top-K row indices BEFORE the actual gather.
    Kernel begins paging them in async; gather hits warm pages.
  - Wired into `ProductKeyMemory.forward` (CPU mmap path) and
    `Int8ProductKeyMemory.forward`. Page boundary alignment (4 KB)
    + dedupe so we issue ~4-16 unique syscalls per layer per token.

Phase 4a (hot-row consolidation) deferred:

  - Reordering V's rows would require coordinated permutation of
    K_a / K_b sub-keys (the flat row index `i_a · sqrt_n + i_b`
    is structurally tied to the sub-key positions in the product-
    key search). A separate permutation table + lookup adds an
    indirection layer of its own, partially offsetting the gain.
    The 4b prefetch alone covers the dominant cold-cache cost.

Phase 4c (threaded gather) deferred:

  - The premise was "16 row reads fetched sequentially in a Python
    loop" — but our gather uses torch's advanced indexing
    (`int8_rows[top_global]`), which is a single C++ kernel that
    releases the GIL. Python-level threading around it doesn't
    help. The cold-cache latency that 4c targeted is already
    addressed by 4b's prefetch.

## Bottleneck analysis

At batch=1 the H100 is at <1 % utilization. Compute is not the
bottleneck — overhead is. Where time goes per token:

1. **Python / PyTorch dispatch overhead.** Each layer call is a
   sequence of Python-level method invocations (q-proj, k-proj, v-proj,
   apply-rope, SDPA, bank lookup, FFN). Each dispatches through
   PyTorch's eager-mode bookkeeping. For a 10 M-param model, this
   overhead dwarfs the actual matmul cost.

2. **KV cache `torch.cat` per token.** Both short and long caches
   currently reallocate on every token via `torch.cat`. For a generation
   of length T, total cache memory traffic is O(T²). Standard
   inference engines avoid this with pre-allocated ring buffers.

3. **Bank top-K gather.** On GPU: the 16 row gather is ~70 KB per token
   over PCIe (when bank is mmap'd) or HBM (when in VRAM). Trivial in
   absolute terms, but adds latency every layer because the gather is
   serialized to wait for the product-key search result.

4. **mmap page faults**. Cold-cache page faults on first access to bank
   pages. Mostly amortized after warmup; remains a long-tail latency
   source for tokens that hit unfamiliar regions of the bank.

5. **CUDA kernel launches**. Each PyTorch op = one kernel launch =
   ~5-10 µs overhead. 5 layers × ~10 ops/layer = 50 launches/token =
   250-500 µs/token in launch overhead alone. CUDA graphs eliminate
   this for repeatable shapes.

What we *do well* already:

- Bank product-key search is sub-linear (O(√N)) — scales with bank
  size cleanly.
- Bank mmap allows the bank to be shared across N parallel inference
  instances at zero per-instance memory cost (just kernel page cache
  pressure).
- BPC and ablation Δ confirm the architecture works — nothing in the
  optimization plan should compromise quality.

## Optimization roadmap

Phased so each phase is independently shippable and benchmarkable.
Each phase ends with a re-bench and a row added to the table above.

### Phase 1 — Easy wins (effort: 1-2 days total)

**1a. `torch.compile` of the forward pass.** Wrap the per-layer
forward into a compiled function. Reduces Python dispatch overhead
substantially. Expected gain: **30-50 % across all three benches**.

  - File: `src/mmllm/core.lpy`, `forward` function (line 449).
  - Implementation: add a `compile-forward` flag; build a Python
    helper in `src/mmllm/runtime.py` that takes the basilisp-built
    model and applies `torch.compile()`. Call from `bench-inference`
    and `sample`.
  - Caveat: `torch.compile` doesn't always handle dynamic shapes well.
    The KV cache cat operation might break compilation; pre-allocated
    buffer (1c below) makes shapes static.

**1b. CPU thread tuning.** Explicitly set thread counts for both
intra-op and inter-op parallelism.

  - File: `src/mmllm/core.lpy`, in `pick-device` or a new
    `setup-threads!`. Add MMLLM_NUM_THREADS env var.
  - Implementation:
    ```clojure
    (defn setup-threads! []
      (let [n (python/int (.get (.- os environ) "MMLLM_NUM_THREADS"
                                (str (os/cpu_count))))]
        (torch/set_num_threads n)
        (torch/set_num_interop_threads (max 1 (quot n 4)))))
    ```
  - Also set `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `MKL_DYNAMIC=FALSE`,
    `OMP_DYNAMIC=FALSE` in `bench_inference_cpu` Modal entrypoint.
  - Expected gain: **10-30 % on CPU bench specifically.**

**1c. Pre-allocated KV cache buffer.** Replace `torch.cat` with
write-into-slot.

  - File: `src/mmllm/core.lpy`, `attention` function (line ~315).
  - Implementation: at first call, allocate `kv_buffer = zeros(B,
    n_kv_heads, MAX_T, head_dim)`. Each subsequent token writes
    `kv_buffer[:, :, t, :] = new_kv` and uses `kv_buffer.narrow(2, 0,
    t+1)` for SDPA. Need MAX_T config (default 4096?).
  - Saves O(T²) memory traffic on long generations. Also makes shapes
    static which unblocks `torch.compile` (1a).
  - Expected gain: **10-20 % on long generations**, plus enables 1a.

**1d. CUDA graphs for batch=1 GPU inference.** For repeatable
T=1-incremental forward, capture the GPU op sequence once and replay
with new input pointers.

  - File: `src/mmllm/runtime.py` (new).
  - Implementation: `torch.cuda.CUDAGraph()` captures the forward
    pass after warmup; per-token decode replays it. Requires static
    shapes (KV buffer from 1c).
  - Expected gain: **30-50 % on H100 batch=1**, less on H100 batch=64.
  - CPU-only deploy: skip — CUDA graphs are GPU-specific.

**1e. Re-bench after 1a-1d.** Update the table.

Realistic Phase-1 outcome:
- H100 + bank in VRAM: 174 → ~300 tok/sec
- H100 + bank mmap'd: 150 → ~250 tok/sec
- 8-vCPU: 102 → ~180 tok/sec

### Phase 2 — Continuous batching (effort: 3-5 days)

GPU at batch=1 is wildly underutilized. Multi-instance throughput is
where the real gains are.

**2a. Batched `sample` function.** Generalize sample to accept multiple
prompts in parallel.

  - File: `src/mmllm/core.lpy`, new `sample-batch` function.
  - Implementation: prompts as a (B, T_prompt) tensor with right-padding;
    short_caches and long_caches as lists of B tensors (each
    conversation has its own).
  - Bank V is shared (read-only at inference) — already sharable via
    mmap.

**2b. Server entry point.** A long-running process that accepts new
prompts and merges them into the active batch.

  - File: `src/mmllm/server.py` (new).
  - Implementation: simple async HTTP server using `aiohttp` or
    `fastapi`. Maintains an active batch of N conversations; each
    forward call processes one new token across all N. New prompts
    enter when slots free up. Standard "continuous batching" pattern
    (vLLM-style, but lighter — no paged attention needed because
    each conversation has its own contiguous KV cache).

**2c. Per-conversation KV cache management.** With continuous batching,
B varies as conversations join and leave. The pre-allocated KV
buffers (1c) become per-conversation; the batch dimension is dynamic.

  - This is the trickiest piece. For first cut, fix B (=64) and
    reject new prompts when full. Iterate to dynamic batching later.

**2d. Bench at batch=64.**

Realistic Phase-2 outcome:
- H100 + bank in VRAM: 300 tok/sec @ B=1 → 6000-10000 aggregate tok/sec
  @ B=64 (~100-150 tok/sec maintained per conversation).
- This is the throughput-per-dollar win that makes the architecture
  serve-able commercially.

CPU-only deploy: continuous batching helps less on CPU (compute
already saturated by the matmul threads). Probably 2× aggregate at
B=8, then plateau.

### Phase 3 — Bank V quantization (effort: 2-3 days)

Bank V at fp32 is 18.8 GB. Quantizing to int8 → 4.7 GB. The matmul
cost is unchanged (we dequantize to fp16 just before SDPA), but:

- 4× less memory bandwidth for bank reads.
- 4× more rows fit per 4 KB page → fewer page faults on cold reads.
- Better CPU L3 cache utilization (CPU L3 is typically 32-64 MB; one
  layer's int8 bank is 1.18 GB — still doesn't fit in L3, but the
  "hot" subset much more likely to).

**3a. Per-row int8 quantization with stored scale.** Each row stored
as 224 int8 + 1 fp16 scale. Row size: 224 + 2 = 226 bytes (vs 896
fp32). 18 rows per 4 KB page (vs 4).

  - File: `src/mmllm/memory.py`, new `Int8ProductKeyMemory` class.
  - Implementation: at retrieval, gather int8 rows + scales, dequantize
    to fp16 in a small buffer, do attention. Quantization of the
    trained fp32 bank happens once offline via a CLI verb
    `mmllm bank-quantize <in.bin> <out.bin>`.

**3b. Calibration-based quantization.** Per-row min-max alone may lose
accuracy. Implement per-row symmetric int8 with optional outlier
clamp at ±3σ. Validate by re-running BPC eval on the quantized bank.

  - Acceptance: int8 bank's BPC must be within +0.005 of fp32 bank's
    BPC. (Empirically this is achievable for product-key memory; the
    retrieval is robust to small per-row noise because top-K already
    averages over rows.)

**3c. Bench int8 vs fp32.**

Realistic Phase-3 outcome (CPU-focused):
- 8-vCPU bank-mmap: ~180 tok/sec (post-Phase-1) → ~280-350 tok/sec
  with int8 bank. Mainly from L3 cache hit rate improvements and
  fewer page faults.
- BPC delta: <+0.005 (negligible quality loss).
- Disk usage: 18.8 GB → 4.7 GB (4× smaller deploy footprint).

### Phase 4 — Bank V mmap layout optimization (CPU-specific, effort: 3-4 days)

The kernel page cache is the most important runtime structure on the
CPU bench. Current bank layout is naive: row i at offset i × row_size.
Two improvements:

**4a. Hot-row consolidation.** After training, profile which row IDs
get retrieved most often on representative validation data. Reorder
the bank file so hot rows are at the front. Two benefits:

  - Hot rows share fewer pages (better cache density).
  - On startup, you can `mlock` the first M MB of the bank (the hot
    region) into RAM, guaranteeing zero page faults for the common
    path.

  - File: `src/mmllm/bank_layout.py` (new).
  - CLI verb: `mmllm bank-reorder <in.bin> <profile.json> <out.bin>`.
  - Profile is generated by running BPC eval and counting per-row hit
    frequencies (the existing PKM has this info available).

**4b. Top-K row prefetch.** The product-key search produces top-K row
IDs *before* the actual gather. Use `madvise(MADV_WILLNEED)` on the
pages containing those rows. Kernel starts paging them in async; by
the time the gather happens, they're warm.

  - File: `src/mmllm/memory.py`, modify `ProductKeyMemory.forward` (CPU
    path).
  - Per-token: ~16 madvise calls per layer × 5 layers = 80 syscalls.
    Cheap relative to the page faults they prevent.
  - Expected gain on cold-cache path: **2-5×** on first-N-tokens
    latency.

**4c. Per-thread bank read parallelism.** The 16 row reads in a top-K
gather are independent. Currently a single Python loop fetches them
sequentially. With a small thread pool (or AVX-512 gather instructions),
fetch them in parallel.

  - File: `src/mmllm/memory.py`, gather path.
  - Implementation choice:
    - Thread pool (concurrent.futures): 16 reads → 4 threads × 4 reads
      each. Simple, ~30 % gain.
    - AVX-512 gather (via numpy): one CPU instruction does 8 fp64
      gathers (or 16 fp32). Requires raw mmap pointer access. ~50-70 %
      gain but Python wrapping is fiddly.
    - Cython/C++ helper: full control. ~80 % gain. Best long-term.
  - Pick the simplest first (threads); upgrade if profiling shows it
    matters.

Realistic Phase-4 outcome (CPU-focused):
- 8-vCPU bank-mmap (post-Phase-3): ~300 tok/sec → ~450-550 tok/sec.
- Cold-cache first-50-tokens latency: roughly halved.

### Phase 5 — Speculative decoding (effort: 4-5 days)

Within a single conversation, sequential token generation is
fundamental — each token depends on the previous. The only way to
parallelize is **speculative decoding**: a small "draft" model
proposes K tokens cheaply, the full model verifies them all in one
batched forward. Accepted tokens advance; rejected tokens fall back.

**5a. Use bank-zeroed model as draft.** mmllm has a natural draft:
the same architecture with the bank set to zero. We measured this
gives BPC=2.10 (vs 1.27 with bank — Δ=4.77 from the ablation). The
draft is much faster (no bank lookup) and "agrees" with the full
model on the easy tokens.

  - Per-token cost of draft: ~30 % of full model (no bank lookup).
  - Acceptance rate empirical estimate: ~60-70 % of draft tokens
    survive verification (the ones bank wasn't going to influence).
  - Speedup: ~2-2.5× on top of all other optimizations.

**5b. Implementation.** Standard speculative-decoding loop:

  - Draft: K tokens generated autoregressively, fast.
  - Verify: one batched (1, K) forward through full model; logits are
    compared against the draft's chosen tokens.
  - For first divergence, accept K_accepted tokens, sample new from
    the full model's logit distribution, restart draft.

  - File: `src/mmllm/spec_decode.py` (new).
  - Tricky bit: maintaining KV cache state in sync between draft and
    full model. The draft uses the same cache; on rejection, rewind
    cache to the last-accepted token's position.

**5c. Bench and tune K.** K=4 is typical; tune for our specific
bank-zero ablation Δ to find optimum.

Realistic Phase-5 outcome:
- All scenarios: roughly **2× speedup on top of cumulative gains**.
- H100 batch=1 final: 174 → ~600+ tok/sec.
- 8-vCPU final: 102 → ~800+ tok/sec.
- These are aggressive estimates; conservative is 50 % of these.

## CPU-specific deep dive: dense-in-RAM + bank-on-mmap

Per the user's call-out: this section dives deeper on the CPU
deployment path and the dense/bank locality strategy.

### The locality story

CPU L3 cache typical sizes (2026 hardware):
- Mid-range desktop (Ryzen 7700, i7-13700K): 32-36 MB
- High-end desktop (Ryzen 7950X, i7-13900K): 64 MB
- Server (EPYC 9654): 384 MB
- Apple M3 Pro: 32 MB unified

mmllm working set inventory:
- Dense weights (fp32): ~40 MB (10 M params × 4 bytes)
- Dense weights (bf16): ~20 MB
- Dense weights (int8): ~10 MB
- Per-conversation short cache (default 1024 tokens): ~10 MB
- Per-conversation long cache (default 4096 tokens): ~40 MB
- Bank V (fp32): **18.8 GB** — never fits in L3
- Bank V (int8): **4.7 GB** — never fits in L3 either
- Bank V hot subset (top 1 % of rows): ~190 MB at fp32, ~47 MB at int8

**Strategy:**
1. Keep all dense weights in L3 cache. At fp32 (40 MB) this fits on
   high-end CPUs but spills on mid-range. At bf16 (20 MB) it
   comfortably fits everywhere.
2. Keep the bank's hot subset in RAM (kernel page cache).
3. Cold bank rows pay a page-fault penalty on first access; that's
   acceptable for tail-latency tokens.

### Sequence of optimizations targeted at the CPU dense+bank path

In dependency order:

**Step C1: BFloat16 dense weights** (subsumed by Phase 1 + minor extra
work).

  - Cast all dense Linear weights to bf16 at load time.
  - Forward with bf16 input → fp32 accumulation in matmul → bf16 output.
  - Modern CPUs (Intel Sapphire Rapids+, AMD Zen4+, Apple M-series)
    have native BF16 matmul instructions (AMX, AVX-512 BF16, NEON BF16).
  - File: `src/mmllm/runtime.py` (Phase-1's compile helper). Add a
    `cast-to-bf16!` function called after model load.
  - Expected gain on CPU: **15-25 %** from halved memory bandwidth on
    dense matmuls + better L3 fit.
  - Acceptable accuracy loss: virtually none for inference.

**Step C2: Per-row int8 bank V** (= Phase 3).

  - As described above.
  - Expected gain on CPU: **40-80 %** (this is the big one — bank reads
    dominate cache misses).

**Step C3: Bank prefetch via madvise** (= Phase 4b).

  - Per-layer: after product-key search produces top-K row IDs, call
    `madvise(MADV_WILLNEED)` on those rows' pages BEFORE issuing the
    actual gather. The kernel begins paging in async; by the time the
    gather (~5 µs later for the matmul-based search) requests the
    rows, they're warm.
  - Implementation detail: cumulative offset of row i = i × row_bytes.
    Page boundary alignment: madvise expects (addr, len) where addr
    is page-aligned. Round each row's start down to the nearest 4 KB.
  - Expected gain: **2-5× on cold-cache tokens**, **10-20 % steady-state**.

**Step C4: Threaded bank gather** (= Phase 4c).

  - Split the 16-row gather across N threads.
  - Conservative: thread pool with 4 threads, 4 reads each.
  - Expected gain: **20-40 %** at 4+ cores.

**Step C5: Hot-row layout optimization** (= Phase 4a).

  - Profile + reorder. After 1B inference tokens of representative
    workload, count per-row retrieval frequency. Reorder bank file so
    top 1 % of rows is at the front. Optionally `mlock` the first
    47 MB of int8 bank into RAM at startup.
  - Expected gain: **eliminates cold-cache penalty for ~99 % of
    retrievals** (because the hot 1 % of rows handles most queries by
    Zipf's law).

**Step C6: Speculative decoding** (= Phase 5).

  - 2× on top of everything else.

### Cumulative CPU projection

| Phase                    | CPU tok/sec (est.) |
|--------------------------|---------------------|
| Current                  | 102                 |
| + Phase 1 (compile + threads + KV buf) | ~180   |
| + Step C1 (bf16 dense)   | ~220                |
| + Phase 3 (int8 bank)    | ~330                |
| + Phase 4b (madvise)     | ~370                |
| + Phase 4c (threaded gather) | ~470            |
| + Phase 4a (hot rows)    | ~520                |
| + Phase 5 (speculative)  | **~1000**           |

Aggressive but plausible. ~10× over current. On a modern desktop CPU
(non-cloud — Modal's vCPUs are conservative), expect 30-50 % more.

### CPU multi-instance scaling

For multi-tenant CPU serving (single user running 50 parallel
conversations):

- Each conversation has its own short + long caches in RAM (~50 MB
  each; total: 2.5 GB for 50 conversations).
- Bank V is shared via mmap (4.7 GB at int8). All conversations hit
  the same kernel page cache, so the hot 47 MB stays warm regardless
  of how many conversations are running.
- Dense weights are shared (single process, shared pages).
- Continuous batching (Phase 2) bundles all 50 conversations into one
  forward call → all 50 get computed in roughly the same time as 1
  did, modulo memory bandwidth limits.

Expected aggregate throughput at CPU + 50 instances: ~5000 tok/sec.

### Hardware recommendations for CPU deploy

For someone running mmllm on their own hardware:

- **Required**: 8 GB RAM (for bank int8 + dense + caches), 4 cores,
  AVX-512 or NEON SVE2.
- **Recommended**: 16 GB RAM, 8 cores, AVX-512 BF16 or AMX (Sapphire
  Rapids / Zen4+ / M3+), NVMe SSD for the bank file.
- **Optimal**: 32 GB RAM (whole bank in page cache), 16 cores, fast
  PCIe NVMe.

The bank file does NOT need to fit in RAM. mmap + kernel page cache
handles graceful degradation when only the hot subset fits.

## Concrete next-step file paths

Phase 1 work touches:

- `src/mmllm/core.lpy` — `forward`, `attention`, `sample`, add
  thread-setup utility.
- `src/mmllm/runtime.py` (NEW) — `compile-model`, `cast-to-bf16`,
  CUDA graph helper.
- `src/mmllm/memory.py` — wire pre-allocated KV buffer into the
  forward call signature.
- `modal_app.py` — pass `MMLLM_NUM_THREADS` and `MMLLM_DTYPE` env
  vars; re-run benches.

Phase 2 (continuous batching):

- `src/mmllm/server.py` (NEW) — fastapi/aiohttp server, request
  queue, batch scheduler.
- `src/mmllm/core.lpy` — `sample-batch` function, paged KV cache.

Phase 3 (int8 bank):

- `src/mmllm/memory.py` — `Int8ProductKeyMemory` class with
  per-row scale.
- `src/mmllm/cli.py` — `bank-quantize` command.
- `mmllm bank-quantize <in> <out>` end-to-end on the trained 5B
  bank, validate BPC delta.

Phase 4 (mmap layout):

- `src/mmllm/memory.py` — `madvise` calls, threaded gather.
- `src/mmllm/bank_layout.py` (NEW) — profiling + reordering.
- CLI: `bank-profile`, `bank-reorder`.

Phase 5 (speculative):

- `src/mmllm/spec_decode.py` (NEW) — speculative loop with KV cache
  rewind on rejection.
- `src/mmllm/core.lpy` — variant of `forward` that returns logits
  for all input positions (needed for verification).

## Tracking + benchmark protocol

Every phase ends with:

1. Re-run all three benches (`bench_inference` GPU bank-on-VRAM,
   GPU bank-on-mmap, `bench_inference_cpu`).
2. Update the bench table in this doc + in the README.
3. Validate BPC on val split — must remain within +0.005 of the
   pre-phase BPC.
4. Commit + push with `mmllm: phase-N <description>` message format.

Bench parameters (held constant for comparability):

- Checkpoint: `/data/pile-github.bin.ckpts/step-305000` (the 5B-trained model).
- Bank: `/data/pile-bank-3tier.<i>.bin` (the trained 5B bank V).
- sqrt_n=2048, batch=1 unless explicitly testing batched throughput.
- 50 warmup tokens, 500 timed tokens for GPU; 50 warmup, 100 timed for CPU.
- 5 measurement runs per setup; report median.

## Out of scope (explicitly)

- Distillation to a smaller dense backbone. The whole point of mmllm
  is the bank-V architecture; we want to keep the shape.
- Multi-GPU model parallelism. Current model is small enough for
  single-GPU; multi-GPU adds complexity without clear win.
- KV cache compression (e.g. 4-bit). Skip until we exhaust the
  cheaper wins.

## Known-unknowns / risks

- `torch.compile` may not handle the bank's product-key search nicely
  (sparse gather). May need to hand-write a compiled-friendly path.
- Speculative decoding speedup depends heavily on agreement rate
  between draft and full model. Our bank-zeroed BPC=2.10 vs 1.27
  control suggests draft quality is OK but agreement-rate measurement
  is needed to size the gain.
- CUDA graphs interact poorly with dynamic-shape KV growth even with
  pre-allocated buffer if the slot index changes. Workaround: capture
  graphs at multiple cache lengths and dispatch by length.
- Per-row int8 quantization of bank V may degrade rare-row retrieval
  more than hot-row retrieval (rare rows seen less during calibration).
  Need a "calibration coverage" metric per-row.

## Summary

| Phase                           | GPU bank-VRAM | GPU bank-mmap | CPU bank-mmap |
|---------------------------------|---------------|----------------|----------------|
| Current                         | 174           | 150            | 102            |
| 1 (compile + threads + KV buf)  | ~250          | ~220           | ~180           |
| 2 (continuous batching)         | ~6000 agg     | ~5000 agg      | ~2500 agg      |
| 3 (int8 bank)                   | ~270 / 6500   | ~250 / 5500    | ~330 / 4000    |
| 4 (mmap layout / threading)     | ~280 / 7000   | ~280 / 6500    | ~520 / 6500    |
| 5 (speculative decoding)        | ~600 / 14000  | ~580 / 13000   | ~1000 / 13000  |

CPU efficiency (bottom row) is the critical user-facing path; the
plan delivers a **10× improvement** over current numbers, with
quality preserved.
