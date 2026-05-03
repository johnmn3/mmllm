# mmLLM - Memory Mapped LLM

## Architecture

mmLLM is a decoder-only transformer with a hard-split three-tier attention
mechanism inside every block. Q heads are permanently assigned to one of two
groups; each group draws from a different memory store with different lifetime,
mutability, and sharing semantics.

```
Q heads split per block (default 5 short / 7 long out of 12):

  SHORT heads (5/12)
    RoPE'd, causal SDPA
    K/V lives in-RAM — recent working memory, per-conversation, mutable

  LONG heads (7/12) — two sources, summed:
    (a) Episodic KV cache: set-style SDPA over per-conversation K/V activations
        (k-proj-l / v-proj-l → K_l, V_l). Paged LRU mmap at inference;
        grows unbounded. Mutable, per-conversation (or shared per team).
    (b) Semantic memory: product-key memory bank — sqrt_n² learned weight
        rows retrieved by content-addressed top-K search. Frozen at inference,
        shared via mmap across all parallel instances.
```

The three tiers correspond to three classical memory categories:

| Tier | Memory type | Origin | Mutable? | Shared? |
|---|---|---|---|---|
| Short KV cache | Working memory | Activations: `k_proj_s(x)`, `v_proj_s(x)` | Yes | No — per-instance |
| Long KV cache | Episodic memory | Activations: `k_proj_l(x)`, `v_proj_l(x)` | Yes | Optional — per-conv or per-team |
| Bank V | Semantic memory / weights | Learned params, updated by SGD | No (frozen at inference) | Yes — all instances share one mmap |

The bank is **not** a cache. It is weights: learned via gradient descent like
any Linear layer, content-addressed rather than position-addressed, persistent
across all conversations, and frozen once training ends. The product-key
mechanism is what makes a very large weight matrix cheap to query — at small N
it is literally equivalent to full attention over a fixed K-V parameter matrix;
product-key retrieval only earns its keep when N is large enough that top-K << N.

No cross-attention, no RAG seam — all three sources are computed inside the
same attention call and summed at the output.

### Product-key memory bank

Two sub-key matrices `K_a`, `K_b` each of size `sqrt_n × (q_dim/2)` factor
an `N = sqrt_n²` entry bank into a product space. Top-K retrieval costs
O(sqrt(N)) instead of O(N): score each half independently, outer-sum the
top sub-candidates, re-rank to get the final K. At `sqrt_n=2048` that's
~4M entries per layer retrievable with ~2048 dot products instead of 4M.

Bank V is a sparse `nn.Embedding` so backward produces sparse gradients —
only the top-K retrieved rows get an update each step. SparseAdam writes only
those rows back through the mmap, so both gradient compute and disk I/O scale
with K, not N.

### Parallel inference cost

The bank is frozen weights on a shared mmap — every parallel inference instance
maps the same files read-only through the OS page cache. 100 instances cost the
same RAM as 1. The long-tier KV cache is the knob: share one file across
instances for a shared episodic pool, or give each instance its own file for
private conversation history. The short-tier cache is always per-instance.

| Resource | Per-instance cost | Sharing |
|---|---|---|
| Dense weights (~10M params) | one copy per process | — |
| Bank V weights (~1 GB default, up to ~19 GB at sqrt_n=2048) | near-zero marginal | shared read-only mmap |
| Long-tier KV cache (episodic) | ~10–100 MB on disk | per-instance or per-team |
| Short-tier KV cache (recent) | few MB in RAM | always per-instance |

### Training

Two optimizers run in parallel:

- **AdamW** for dense params (Q/K/V projections, FFN, norms, `K_a`/`K_b`)
- **SparseAdam** for bank V — only updates touched rows each step

For large banks (`sqrt_n=2048`, ~19 GB/layer), `CPUOffloadSparseAdam` keeps
the m/v moment tensors on CPU (~38 GB total) rather than GPU, freeing VRAM at
the cost of one extra PCIe round-trip per step.

Multi-GPU Hogwild training is supported via Modal Volumes: N workers share one
mmap'd bank file, each committing dirty pages every `sync_every` steps.
Commit/reload is Modal's global volume sync; page-level conflicts are accepted
as Hogwild noise.

## Setup

```
pip install -e .
```

Installs `basilisp`, `torch` (CPU), and `numpy`.

> **Intel Mac note:** PyTorch tops out at 2.2.x on Intel; `nn.RMSNorm` requires
> 2.4+. A polyfill is included in `_entry.py` so local CPU runs work out of the
> box. GPU runs (Modal, Linux) get the real implementation.

## Commands

### Quick start (toy corpus)

```
mmllm train [short|long]    # train a tiny transformer on a toy corpus
mmllm sample [short|long]   # train then sample 200 chars
mmllm compare               # compare short vs long-memory configs
mmllm probe [short|long]    # copy-from-far recall accuracy
```

### text8 / enwik8 (standard byte-LM benchmarks)

```
mmllm fetch-text8  [out-path]     # download Matt Mahoney's text8
mmllm fetch-enwik8 [out-path]     # download Matt Mahoney's enwik8
mmllm split-text8  [base-path]    # 90M/5M/5M Mikolov split → <base>.{train,val,test}.bin
mmllm train-text8  [base-path] [mmap-path] [steps]
                                  # train + eval BPC on val/test
```

### Clojure corpus

```
mmllm build-corpus [out-path] [source-dir]   # gather local .clj/.cljc/.cljs/.edn files
mmllm clone-clojure [target-dir]             # shallow-clone Clojure-heavy upstream repos
mmllm train-corpus [corpus-path] [mmap-path] [steps]
                                             # train on any binary corpus file
```

### mmap / long-running

```
mmllm train-mmap [base-path]                 # train with mmap-backed bank (creates <path>.0.bin … <path>.N.bin)
mmllm train-long [base-path] [mmap-path] [total-steps] [eval-every] [ckpt-every]
                                             # periodic eval-BPC + checkpoints; resumes from <base>.ckpts/
```

## Hack

Everything lives in `src/mmllm/core.lpy` — tokenizer, model, training loop,
sampler, CLI dispatch — by design. One file is easier to read top-to-bottom
than four. Split it once it grows past ~200 lines.

Defaults are intentionally tiny (~10M params, byte vocab, 200 train steps) so
a full `train` finishes in seconds on CPU. To go bigger, edit `default-config`
in `core.lpy`.

## Layout

```
mmllm/
├── pyproject.toml
├── modal_app.py             # Modal cloud training (text8, Pile-Github, Hogwild)
├── src/mmllm/
│   ├── __init__.py
│   ├── _entry.py            # python shim → basilisp bootstrap + torch polyfills
│   ├── core.lpy             # model, training loop, CLI — all of it
│   ├── memory.py            # ProductKeyMemory, CPUPinnedEmbedding, PagedMmapStorage
│   ├── longcache.py         # paged LRU mmap KV cache (long-tier episodic store)
│   ├── corpus.py            # text8, enwik8, Pile-Github, Clojure corpus loaders
│   └── optim.py             # CPUOffloadSparseAdam
└── tests/
    ├── __init__.py
    └── test_smoke.lpy       # forward-pass shape + cache checks
```
