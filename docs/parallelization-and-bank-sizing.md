# Parallelization & bank sizing — next-gen run

Two coupled questions that need to be answered together before
kicking off the agentic-corpus run:

1. **How big should the bank be?** (sets memory + saturation pace)
2. **How do we parallelize training?** (sets wallclock)

Bigger bank = more capacity but slower to saturate. More parallelism =
shorter wallclock but harder coordination. The right answer depends on
how big the corpus is and how long you're willing to wait.

## Bank size — the math

For our hard-split arch with `q_dim=224`, `n_layers=5`:

```
size_per_layer = sqrt_n² × q_dim × dtype_bytes
total          = 5 × size_per_layer
entries        = sqrt_n² (per layer; same N across layers)
```

| sqrt_n | entries / layer | fp32 total | fp16 total | int8 total |
|---|---|---|---|---|
| 1024 | 1.05M  | 4.7 GB   | 2.4 GB   | 1.2 GB   |
| 1536 | 2.36M  | 10.6 GB  | 5.3 GB   | 2.6 GB   |
| **2048** | **4.19M** | **18.8 GB** | **9.4 GB** | **4.7 GB** |
| 3072 | 9.44M  | 42.3 GB  | 21.2 GB  | 10.6 GB  |
| 4096 | 16.78M | 75.2 GB  | 37.6 GB  | 18.8 GB  |
| 5120 | 26.21M | 117 GB   | 58.7 GB  | 29.4 GB  |
| 6144 | 37.75M | 169 GB   | 84.6 GB  | 42.3 GB  |

(Sizes are decimal GB. fp16 ≠ 4× int8 — it's exactly 2× int8 because
fp16=2 bytes, int8=1 byte. The 18.8 GB current bank is **fp32**, not
fp16.)

## Saturation intuition

A bigger bank holds more entries but each entry sees fewer updates
per training step. Roughly:

```
bank_visits_per_entry ≈ (steps × batch × T × top_K) / entries
```

For the just-finished 5B-plain run (sqrt_n=2048, 305k steps, B=128,
T=1024, top_K=32):

```
visits/entry = 305_000 × 128 × 1024 × 32 / 4.19M ≈ 305_000 visits
```

That's a *lot* — yet Δ was still climbing at step 305k, meaning the
bank is *not* a slot-filling memory at saturation. It's a learned
representation that keeps refining indefinitely. So "saturation
steps" is misleading. The real story:

- **Frequent entries** get hit way more than uniform and learn fast
- **Rare entries** never fully train — but they don't matter much because
  they're rarely queried at inference either
- Effective capacity is "how many entries can hold meaningful signal,"
  which is closer to top-K-weighted-by-access-frequency

That said: doubling sqrt_n quadruples entries and roughly halves
visits/entry. The frequent-entry tail still gets hit plenty, but
the long-tail entries will be increasingly random. **Practical rule
of thumb**: pick the smallest bank that still saturates *capacity*
on your corpus. For a richer corpus (our v2 mix is way richer than
pile-github), you can use a bigger bank.

## Recommendations by deployment

### Local laptop (i7-9750H, 20 GB free)

- **Inference target**: sqrt_n=2048 int8 = **4.7 GB** + ~1 GB model + KV cache → fits comfortably
- Larger banks via mmap-from-disk also work but slow per-token by 5-20×
- Sweet spot: int8 sqrt_n=2048 in RAM, OR fp32 sqrt_n=1024 in RAM (4.7 GB) for higher fidelity

### Sandbox / dev box (30 GB total RAM)

- **Training**: dense + opt state + activations + bank = tight at sqrt_n=2048 fp32
- Drop to sqrt_n=1536 fp32 (10.6 GB) or sqrt_n=2048 fp16 (9.4 GB)
- Or use bank-on-disk via `MMLLM_BANK_ON_GPU=false` — slower per step but unbounded by RAM

### Modal (target: 100 GB bank class)

- **Training H100-80GB**: sqrt_n=4096 fp32 (75.2 GB) fits in VRAM with `bank_on_gpu=true` + headroom for activations
- **Training A100-40GB**: bank too big for VRAM at sqrt_n>2048 fp32; use `bank_on_gpu=false` + mmap
- **At 100 GB target** specifically: sqrt_n=4736 fp32 = 100.4 GB. Or sqrt_n=4096 fp16 = 37.6 GB (fits 80 GB H100 with room to spare). Or sqrt_n=6144 fp16 = 84.6 GB (close to H100-80GB cap)

## Recommendation for the v2 run

Stick with **sqrt_n=2048 fp32** for the v2 base run. Here's why:

1. **Comparable to v1**: same bank size means we can directly compare
   ablation Δ trajectories between v1 (5B-plain pile-github) and v2
   (agent corpus). One variable changed at a time.
2. **Already characterized**: we know inference perf, we have the
   int8-quantize path, the laptop pipeline works.
3. **Saturation isn't the bottleneck**: even at 305k steps Δ kept
   climbing. Bigger bank doesn't help unless we also train longer
   to keep visits/entry up.
4. **100 GB experiment is a separate bet**: do that as a v2.1
   *after* we have v2 baseline. Otherwise we confound corpus changes
   (v1→v2) with bank-size changes.

For the **v2.1 follow-up** (the "100 GB on Modal" test the user
mentioned), recommend **sqrt_n=4096 fp16 (37.6 GB)** — gives 4× more
entries than v2 base, fits H100-80GB easily, and fp16 saves us bank
sync bandwidth in the multi-worker setup.

## Parallelization options

Five strategies, ordered by complexity and speedup ratio:

### Option A — Single H100, single worker (status quo)

What it is: one container, one GPU, current code unchanged.

```
Speedup:        1×
Setup:          0
Cost:           ~$3/h × wallclock
Wallclock for 100 B tokens at 5 B/h: ~20 days
```

Verdict: only viable for runs <50 B tokens. Too slow for v2 base.

### Option B — Single 8×H100 node, data-parallel (recommended for v2)

What it is: one Modal container with 8 H100s. Each GPU runs a copy
of the dense model + bank, gradients all-reduce'd via NCCL after
each step. Standard PyTorch DDP — `nn.parallel.DistributedDataParallel`
wraps the dense modules. Bank V is shared across GPUs (one copy
per node, accessed via NVLink).

```
Speedup:        ~6-7× (NCCL all-reduce overhead is small for our
                tiny dense; bank lookup might bottleneck if not
                pinned per-GPU)
Setup:          ~1 day to wire DDP + handle bank state correctly
Cost:           ~$32/h × wallclock
Wallclock for 100 B tokens: ~3 days  (8× speedup × $32 vs 1× × $3 →
                                       roughly 4× cost, 7× faster)
```

Verdict: **the recommended path** for v2. Single-node keeps
NVLink bandwidth high, no cross-machine sync headaches.
Implementation cost is real (must wrap dense in DDP, handle bank
state cleanly across ranks) but well-trodden.

### Option C — Multi-node H100 cluster, data-parallel + Hogwild bank sync

What it is: N separate Modal containers each with a single H100.
Each worker has its own dense+opt+bank copy; bank V mmap'd on
shared Modal Volume. Periodic `volume.commit() + reload()` syncs
dirty bank pages cross-worker (already implemented as
`MMLLM_SYNC_EVERY` — see `mmllm.memory.sync_banks`).

```
Speedup:        ~3-5× at N=4 workers (degrades with N due to volume
                bandwidth bottleneck on bank sync)
Setup:          0 (already implemented)
Cost:           ~$3/h × N × wallclock
Wallclock for 100 B tokens at N=4: ~6-7 days
```

Verdict: works *today*, but the throughput-per-dollar ratio is
worse than B because of volume-sync overhead. Useful when single-
node 8×H100 isn't available, or as a fallback if DDP is too painful
to wire.

### Option D — Single 8×H100 node, FSDP for dense + sharded bank

What it is: dense weights sharded across GPUs via FSDP (Fully
Sharded Data Parallel), bank also sharded (each GPU holds 1/8 of
the bank entries). Top-K query needs an all-gather across ranks.

```
Speedup:        ~5× (sharding helps memory, hurts compute due to
                all-gather overhead on bank)
Setup:          ~3-5 days (bank sharding is the hard part — research-
                level work)
Cost:           ~$32/h × wallclock
```

Verdict: **only if** we want to scale dense beyond what fits on
one GPU (i.e., dense >>1B params). For our current ~50M dense, FSDP
is overkill. Bank sharding is a real research direction but not
something to drop into a production run.

### Option E — 8×H100 single node, FSDP for dense + bank-on-CPU-shared

What it is: like B but bank V lives in CPU RAM (no GPU copy), shared
across all 8 GPU workers via mmap. Top-K query happens on GPU,
indices copied to CPU, V rows gathered on CPU, results copied back.

```
Speedup:        ~6× (PCIe transfer per-token bottlenecks throughput)
Setup:          ~2 days
Memory:         Frees VRAM for activations; supports much bigger banks
                (CPU RAM can hold 128+ GB on H100x8 boxes)
Cost:           ~$32/h × wallclock
```

Verdict: **the right path for the v2.1 100 GB bank experiment**.
For v2 base at sqrt_n=2048 fp32 (18.8 GB), the bank fits in VRAM
fine, so option B is faster.

## Concrete plan

**v2 base run** (~100 B tokens, agent corpus):

- Bank: `sqrt_n=2048 fp32` (18.8 GB), `bank_on_gpu=true`
- Parallelism: **Option B** — single 8×H100 node, DDP for dense
  - Implementation cost: 1-2 days to wire DDP correctly into train-long
    (handle bank state, initialization, ckpt save/restore across ranks)
- Wallclock estimate: 3-5 days
- Cost estimate: ~$2,500-4,000

**v2.1 large-bank experiment** (after v2 baseline lands):

- Bank: `sqrt_n=4096 fp16` (37.6 GB) OR `sqrt_n=4736 fp32` (100 GB target)
- Parallelism: **Option E** — 8×H100 with bank-on-CPU-shared
- Wallclock: TBD; depends on PCIe transfer overhead at our throughput

## What needs to be built

To unlock Option B (the v2 path):

1. **DDP wrap** for the dense modules in `train-long`. Bank V already
   handles distributed correctly via mmap; dense needs explicit
   wrapping.
2. **Distributed batch sampler** — currently `mix-batch` works on a
   single process. For DDP, each rank needs to sample a different
   slice of the corpus per step (handled trivially with
   `DistributedSampler` for `train_data`, slightly less trivially
   for the mix sampler).
3. **Distributed ckpt save/restore** — only rank 0 should write the
   dense ckpt; all ranks need to load on resume. Bank V is shared so
   that side is already correct.
4. **Tested DDP on a small corpus first** — text8 multi-GPU smoke
   before committing to the v2 run.

Estimate: ~1 week of engineering before we can launch v2.

## Open questions for user

1. **Run on 8×H100 or single H100?** Option B (8×H100) is recommended
   but adds ~$2,500 of one-time engineering cost (the DDP wrap) and
   the 8×H100 hourly rate is ~10× the single-H100 rate. Single H100
   is the cheap-and-slow path.
2. **v2 first, v2.1 later?** Two sequential runs (v2 baseline then
   v2.1 big-bank) gives clean comparisons but doubles the total
   time. Doing them concurrently on separate machines doubles cost
   but cuts wallclock.
3. **Long-tail completion**: do we want to keep training v2 past
   100 B tokens if Δ is still climbing? At the v1 end (305k steps
   on pile-github 5B-plain), Δ was still climbing. Worth budgeting
   for a continuation phase, or call it at 100 B?
