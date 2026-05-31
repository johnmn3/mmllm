# mmLLM - Memory Mapped LLM

mmLLM is a new kind of "green llm" - more efficient for many things by offloading some work to disk.

## Use case: lightweight CPU-bound code agents at the edge

mmLLM is shaped for one specific deployment profile: **fast,
local, fill-in-the-middle code completion that runs alongside your
editor on a laptop, dev server, or edge device** — without
depending on a hosted API.

The architecture trades a large mmap-backed semantic memory bank
(~5–20 GB on disk, queried sparsely per token) for tiny active
dense weights (~10M params, ~40 MB resident). The bank gets
faulted from disk into the OS page cache on demand, then shared
across every concurrent editor session on the host.

### Why this fits coding agents better than the alternatives

**vs hosted-API completion (Copilot-style)**:
- Round-trip + queue latency: 100-500 ms; mmLLM target after Phase 5: ~1 ms/token.
- API costs scale linearly with users; mmLLM is one-time disk + CPU.
- Code never leaves the device — fits enterprise dev environments
  with privacy / data-residency constraints.

**vs local dense code models (Qwen-Coder, DeepSeek-Coder, Codestral)**:
- A 7B int8 dense model holds 7 GB resident **per editor**. Open
  3 editors → 21 GB just for inference weights.
- mmLLM holds **40 MB dense per editor** + one shared 4.7 GB
  bank in the OS page cache (regardless of editor count).
  Crossover at ~30 concurrent editor sessions per host;
  asymptotic ~16× lower per-user RAM (see [Memory access energy](#memory-access-energy)).
- Idle editor sessions cost ~zero RAM in mmLLM; in dense local
  they keep their full weight set hot.

**vs distillation-down-to-tiny dense models**:
- A 100M-dense distillation has hard quality limits — it can't
  encode the long tail of identifiers/APIs/idioms a real codebase
  needs.
- mmLLM's bank is the long-tail catchall: 21M entries today,
  scalable to ~1T entries on disk (~2 TB int8) without the
  per-user RAM cost growing.

### Fill-in-the-middle is the natural attention shape

The three-tier attention maps cleanly to the FIM completion task:

| tier | what it does | role for code completion |
|---|---|---|
| **Short** (RoPE'd, in-RAM) | local positional context | the immediate prefix and suffix around the cursor |
| **Long-cache** (set, in-RAM) | recent unbounded context | the rest of the open file + adjacent open buffers |
| **Long-bank** (mmap-backed PKM) | cross-corpus semantic memory | "I've seen function signatures like this before; here's the typical body" — content-addressed retrieval over millions of trained code patterns |

The bank's product-key lookup is `O(√N)` regardless of bank size,
so growing it from 21M entries (current 5B run) to 1B+ entries on
a laptop is a disk-space question, not a latency question.

### Green concerns are now developer concerns

LLM training and inference energy footprints have become a
first-order concern for the developer community. The cost of a
GPT-4-class model is on the order of 1,287 MWh just for the
training run (Patterson 2021), and a high-traffic Copilot-style
deployment burns through GPU-hours at a rate the same teams that
sweat their AWS bills are increasingly unwilling to accept. There's
real demand for "AI infrastructure that respects power budgets" —
both for laptops where battery life matters and for data centers
where every kilowatt is metered.

mmLLM is built around this constraint from the architecture up.
Concrete near-term wins (numbers in the [Green value](#green-value)
section, derived from the architecture, not aspirational):

- **At-scale serving**: ~16× lower per-user RAM than a dense model
  of comparable quality, asymptotically. At 100 concurrent users
  per host: ~10× lower idle power per user. At 1000+ users per
  host: ~36× lower.
- **Per-token energy**: comparable to dense at single-instance,
  but ~700× lower at a hypothetical 1T-class scale because the
  bank avoids loading 2 TB of weights into HBM (worked numbers in
  [1T scale extrapolation](#1t-scale-extrapolation)).

**Long-term goal: enable 1T-parameter-class models in under
1,000 watts of total system power**, by holding only the active
dense network in fast memory and paging the bank from local
NVMe on demand. A 1T dense model today demands 25 GPUs at full
TDP (~17.5 kW); the same effective parameter budget as a sparse
mmap-backed bank can run on a single 700 W GPU + ~75 W of DDR
page-cache RAM, because nothing is hot that doesn't need to be.
Whether quality scaling holds at that bank size is the open
research question the project is set up to answer; the energy
math is straightforward.

If you'd like to help push the green-LLM thesis forward — paying
for the next batch of training runs, the inference benches that
will produce real measured kWh/gCO2 numbers, or just the disk
storage these large banks live on — consider donating via the
**Buy Me a Coffee** button at the top-right of [the GitHub
repo](https://github.com/johnmn3/mmllm). Every cup keeps a future
GPU spinning a few minutes longer.

### Roadmap toward a Clojure assistant

The eventual product target is a purpose-built Clojure code
assistant — Clojure has a small enough community that mainstream
tooling (Copilot, Cursor) underweights its idioms (immutable data,
threading macros, REPL-driven workflow, namespaced keywords, EDN).
A model trained specifically on Clojure, lightweight enough to run
beside your editor with no API calls, fills a real gap.

The path:

1. **Now** — train on Pile-Github (~95 GB mixed-language code) to
   validate the bank-as-substrate thesis at scale (active 5B
   `ctx-add+fb` run; see Results below).
2. **Next** — train on a Clojure-heavy corpus. Infrastructure
   already exists: `mmllm clone-clojure` shallow-clones curated
   Clojure-heavy upstream repos (clojure/clojure, core.async,
   clojurescript, babashka, clj-kondo, shadow-cljs, ...);
   `mmllm build-corpus` gathers `.clj/.cljc/.cljs/.edn` files into
   a flat byte stream.
3. **Multi-task** — train one shared bank simultaneously across
   Pile-Github + Clojure corpora (`train_multi_b` in
   `modal_app.py` already supports N corpora → 1 shared
   mmap-backed bank). Tests whether bank-as-substrate transfers
   general code knowledge into Clojure-specific completions
   without catastrophic forgetting.
4. **Edge packaging** — int8-quantize the trained bank (Phase 3
   shipped, 4× compression) → 4.7 GB on disk. Ship as an editor
   extension that spawns a local mmllm inference process;
   multiple editors share the same bank file via the OS page
   cache.
5. **Specialized inference loops** — continuous batching for
   multi-cursor completion, speculative decoding for 2× throughput,
   eventual fine-tuning on Clojure-specific FIM templates and
   REPL-driven workflows. Target: 1000 tok/sec on a modern
   laptop CPU (see `docs/inference-optimization.md`).

The overall pitch: a code assistant that respects the user's
machine, the user's data, and the long tail of patterns specific
to a language community that mainstream tooling doesn't prioritize.

## Current training mission (v2): agentic file editing

The v1 series (5B-plain on Pile-Github, results below) validated
the bank-as-substrate thesis for free-form code continuation. The
v2 series targets a **byte-level model that emits JSON tool calls
to edit files** — a small agentic LLM that can act on common text
files and source code from the command line.

**Output schema (locked!)** — every assistant turn is a JSON object
in the canonical OpenAI-/Anthropic-style tool-call shape:

```json
{"tool_calls": [{"name": "Edit", "args": {"old_str": "...", "new_str": "..."}}]}
```

The model learns this format end-to-end from the byte stream — no
tokenizer hacks, no constrained decoding at inference. Same vocab
(256 bytes), same architecture, just a chat-template-wrapped corpus.

### Corpus mix (curated public HF datasets)

Every formatter and HF source is wired into `mmllm.datasets.DATASET_REGISTRY`
and stages onto the volume in the standard `<base>.{train,val,test}.bin`
shape that `train-long` consumes. Pull each one independently with
`modal run modal_app.py::prepare_hf_dataset --dataset-key <key>` or
all-at-once with the smoke runbook below.

| key | HF source | role | ~size at full prep |
|---|---|---|---|
| `commitpackft-py` | `bigcode/commitpackft` (python) | Python file-edit signal — the primary corpus for "given source + edit instruction, emit Edit tool call" | ~1 GB |
| `commitpackft-md` | `bigcode/commitpackft` (markdown) | Markdown editing | ~700 MB |
| `commitpackft-sh` | `bigcode/commitpackft` (shell) | Shell script editing | ~600 MB |
| `commitpackft-js` | `bigcode/commitpackft` (javascript) | JavaScript editing | ~700 MB |
| `commitpackft-clj` | `bigcode/commitpackft` (clojure) | Clojure file-edit signal — fast path to the eventual Clojure-assistant target | ~150 MB |
| `magicoder` | `ise-uiuc/Magicoder-Evol-Instruct-110K` | Code instruction-following scaffolding | ~250 MB |
| `cosmopedia` | `HuggingFaceTB/cosmopedia-v2` | Synthetic textbook-quality general text — distillation flavor without doing the distillation | up to 25 GB |
| `fineweb-edu` | `HuggingFaceFW/fineweb-edu` (10BT sample) | Curated educational web text — general world knowledge | up to 30 GB |
| `open-web-math` | `open-web-math/open-web-math` | 14.7B tokens of mathematical web text (proofs, derivations, math.SE). Formal-reasoning signal. | up to 50 GB |
| `algebraic-stack` | `EleutherAI/proof-pile-2` (algebraic-stack) | Math + code from arXiv: Lean, Coq, Isabelle proofs + algorithmic implementations. The "successful proof tactic" trail. | up to 10 GB |
| `code-contests` | `deepmind/code_contests` | Competitive programming problems paired with **both accepted and rejected solutions**. Each chat-wrapped record is `(problem, code, verdict)` so the model sees the boundary between code that works and code that doesn't. | ~5 GB |
| `theorem-qa` | `TIGER-Lab/TheoremQA` | Theorem statements + answers across Calculus, Topology, Number Theory, etc. Compact formal-reasoning Q&A. | <100 MB |
| `xlam` (gated) | `Salesforce/xlam-function-calling-60k` | Native JSON function-call traces; teaches the canonical tool-call shape. Requires HF token. | ~150 MB |
| `the-stack-v2-{py,md,sh,clj}` (gated) | `bigcode/the-stack-v2-dedup` | Per-language code subsets — Python, Markdown, Shell, **Clojure**. Requires HF token + license click-through. | TB-scale, capped per slice |

**Default mix proportions** for a slow-walk session (operator sets via
`--mix "<path1>:<weight>,..."`; see [`docs/slow-walk-budget-plan.md`](./docs/slow-walk-budget-plan.md)).
Math + code-with-failure-modes are weighted in **from the first session**,
not phased — code-as-reasoning-substrate is hypothesized to lift general
capability throughout training, not just at fine-tune time.

```
20%  commitpackft-py     file-edit signal (primary)
15%  cosmopedia          synthetic textbook (already math-heavy)
12%  fineweb-edu         general web text
10%  open-web-math       formal math + proofs
 8%  algebraic-stack     math + Lean/Coq + arXiv code
 8%  code-contests       successful + failing competitive solutions ← polynomial-hierarchy boundary
 7%  commitpackft-md     markdown editing
 6%  magicoder           instruction-following scaffold
 4%  commitpackft-sh     shell scripting
 2%  commitpackft-js     JavaScript
 2%  theorem-qa          formal Q&A
```

That's ~30% math/CS-theory + ~35% code (with failure boundary signal) +
~35% general/SFT — code+math heavy from the start. xLAM + the-stack-v2
added when the HF token is configured.

### Architecture knobs (v2 vs v1)

| | v1 (5B-plain, completed) | v2 (slow-walk, in progress) |
|---|---|---|
| `bank_query_mode` | `plain` | `ctx-add` (additive `W_ctx · x`) |
| `bank_feedback_mode` | `plain` (no feedback) | `feedback` (probe→bank→`W_back`) |
| Bank | `sqrt_n=2048` fp32 (18.8 GB) | same |
| Output | free-form continuation | JSON tool calls |
| Corpus | Pile-Github (~95 GB) | curated HF mix (~50-100 GB) |

### Slow-walk training (budget-bounded sessions)

Training proceeds in many short sessions that resume from the
latest ckpt. Each session is bounded by `--max-hours <N>` so the
operator caps spend per launch. Real H100 throughput at production
config: **~6 steps/sec → ~22k steps/hour → ~7,300 steps per $1**.
That puts v1-comparable scale (305k steps) at ~14 hours / ~$42 of
H100, achievable in 3 weeks of $14/wk pace.

Auto-publish to GitHub Release: each session optionally
quantizes the bank to int8 and uploads to `agent-step-<N>`
(immutable per-step) + `agent-latest` (force-replaced moving tag)
so external machines can pull ckpts via `mmllm fetch-artifacts`
without Modal access. See [`docs/slow-walk-budget-plan.md`](./docs/slow-walk-budget-plan.md)
for the full runbook.

### Per-ckpt eval harness

Two metric families run automatically against each ckpt as it
lands (via `eval_watcher` on a cheap A10G alongside the H100
training session):

- **BPC evals** on pretraining-style splits (cosmopedia, fineweb-edu,
  the-stack-v2-py) — straightforward bits-per-byte.
- **Agentic evals** on SFT splits (commitpackft-{py,md,sh,js},
  magicoder, xlam) — generation-driven scoring of
  `format_validity` (fraction emitting valid JSON), `tool_name_match`,
  `tool_args_match`, `exact_match`. The first metric crawls off
  zero once the model has seen enough format-tagged training data;
  the others lag.

All metrics land in the same `<base>.eval.jsonl` as `train-long`'s
in-training events so they plot on the same step axis.

### Pre-flight smoke tests

Two smokes verify the rig before any paid training:

```bash
# Local CPU smoke (free, ~45-90s) — synthetic data, full pipeline:
python scripts/smoke_phase0.py

# Modal smoke (~$0.10-0.40) — real HF prep + optional H100 train + eval:
modal run modal_app.py::smoke_pipeline_modal                          # prep+inspect only
modal run modal_app.py::smoke_pipeline_modal --include-train          # +3-min H100
modal run modal_app.py::smoke_pipeline_modal --include-train --include-eval
modal run modal_app.py::smoke_pipeline_modal --include-train --include-eval --include-publish
```

Per-dataset failures are captured + reported in the summary
rather than aborting the whole smoke. Run before launching any
real session.

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

### Knobs

Three orthogonal architectural axes, all defaulting to baseline behavior:

| axis | values | env var | what | params added |
|---|---|---|---|---|
| `bank-query-mode` | `plain` (def) / `ctx-add` | `MMLLM_BANK_QUERY_MODE` | dense → bank: shapes the query sent to the bank. `ctx-add` adds `W_ctx · x` (zero-init) before lookup | 0 / +d_model·q_dim per layer (~86k × n_layers) |
| `long-tier-mix` | `sum` (def) / `scalar` / `switch` | `MMLLM_LONG_TIER_MIX` | how long-head SDPA path and bank path combine. `scalar` = α[h]·sdpa + β[h]·mem (init 1,1). `switch` = sigmoid(Q·w_h) convex mix (init 0.5/0.5) | 0 / +2n_long_heads / +n_long_heads·head_dim |
| `bank-feedback-mode` | `plain` (def) / `feedback` | `MMLLM_BANK_FEEDBACK_MODE` | bank → dense: lets bank output prime x before q-proj. `feedback` adds `W_back · bank(W_probe · x)` (W_back zero-init) | 0 / +2·d_model·q_dim per layer (~170k × n_layers) |

Each lives in its own module alongside `mmllm.memory`: `mmllm.gating`,
`mmllm.bank_query`, `mmllm.bank_feedback`. Each defines a small `build_*`
factory that returns the chosen variant; the attention block holds it
under `:long-gate`, `:bank-query`, `:bank-feedback`.

Operational env vars:

| env var | default | what |
|---|---|---|
| `MMLLM_DEVICE` | `auto` | `cpu` / `cuda` / `auto` |
| `MMLLM_LR` | `3e-3` | peak lr (both AdamW and SparseAdam) |
| `MMLLM_BATCH` | `4` | batch size |
| `MMLLM_SQRT_N` | (config) | bank side length; total entries = sqrt_n² |
| `MMLLM_LR_WARMUP` | `0` | linear-warmup steps; >0 enables cosine decay to lr/10 over remaining steps |
| `MMLLM_LR_MIN` | `lr/10` | cosine floor when warmup > 0 |
| `MMLLM_BANK_ON_GPU` | `true` | bank V on GPU vs mmap-backed CPU (see Storage modes) |
| `MMLLM_CPU_OFFLOAD` | `false` | legacy alias for `MMLLM_SPARSE_OPT=adam-cpu`. When `MMLLM_SPARSE_OPT` is unset and this is `true`, the bank optimizer is `CPUOffloadSparseAdam` |
| `MMLLM_SPARSE_OPT` | unset | bank optimizer choice — `adam` (stock SparseAdam; dense m/v state), `adam-cpu` (`CPUOffloadSparseAdam`; touched-row-sparse m/v on CPU), or `sgd` (`CPUSparseSGD`; zero state). At `N_TRUNKS>1` `adam` will OOM; use `adam-cpu` or `sgd`. Takes precedence over `MMLLM_CPU_OFFLOAD`. |
| `MMLLM_N_TRUNKS` | `1` | shared-trunk multi-stream training (option A). When >1, Local Bank V is sized `(N×sqrt_n², q_dim)` and per-batch-row `trunk_ids` route each row to its own slice. Dense weights + K_a/K_b + NetBank stay shared. Batch interpretation: `MMLLM_BATCH` becomes B-per-trunk; effective batch = N × B-per-trunk. Old N=1 ckpts auto-migrate to (1×n, q_dim) shape on load. |
| `MMLLM_SHORT_WINDOW` | unset | sliding-window cap on short-tier KV cache (RoPE-safe) |
| `MMLLM_LONG_WINDOW` | unset | sliding-window cap on long-tier in-RAM KV cache |
| `MMLLM_ABLATE_EVERY` | `0` | log Δ trajectory every N steps; must be a multiple of eval-every |
| `MMLLM_SYNC_EVERY` | `0` | multi-trainer Hogwild bank-sync interval; 0 disables |
| `MMLLM_VOLUME_NAME` | `mmllm-data` | Modal volume for cross-worker bank sync |

### Storage modes

The bank V and its SparseAdam state are the largest tensors in the model;
where they live determines what hardware the run can target.

| mode | bank V | SparseAdam state | per-step cost | bank size ceiling | use when |
|---|---|---|---|---|---|
| GPU + GPU | VRAM | VRAM | fast — no PCIe in the bank path | ~30 GB on A100-80GB after dense + activations + opt | bank fits VRAM, single-process |
| GPU + CPU-offload | VRAM | host RAM | + 1 PCIe round-trip per step (touched-row delta only) | bank V up to ~50 GB on A100-80GB; opt-state limited by host RAM | bank fits VRAM but moments push past combined ceiling |
| Mmap + CPU | disk + page cache | CPU | per-query top-K gather CPU→GPU, ~10× slower vs in-VRAM at B=64 | unbounded by VRAM; bounded by disk | bank too big for VRAM, or multi-trainer Hogwild |

Toggle via `MMLLM_BANK_ON_GPU` and `MMLLM_CPU_OFFLOAD`.

The long-tier KV cache has the same axis at smaller scale:

| mode | location | sharing | for |
|---|---|---|---|
| in-RAM | per-process tensors | per-conversation | training, short conversations |
| paged-LRU mmap (`longcache.py`) | disk + page cache | per-conversation or per-team via shared file | inference with conversation history that grows past RAM |

The short-tier cache is always per-process in-RAM — small (recent tokens
only) and per-conversation by definition.

Multi-trainer Hogwild: when `MMLLM_SYNC_EVERY > 0` and the bank is
mmap-backed, N workers each write to the same bank file via Modal Volume.
`mem/sync_banks` handles the close → commit → reload → rebind dance every N
training steps; last-writer-wins on per-page conflicts is accepted as
Hogwild noise.

### Training

Two optimizers run in parallel:

- **AdamW** for dense params (Q/K/V projections, FFN, norms, `K_a`/`K_b`,
  any of the new gating/query/feedback modules' learned weights)
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

### Laptop quickstart (no Modal account needed)

To run a local bench / generation against a pre-trained checkpoint
on your laptop without provisioning Modal:

```bash
# 1. Install
pip install -e .

# 2. Fetch the public artifact bundle from a GitHub Release
#    (~4.5 GB: int8 bank + dense.pt; ~5 min on a 100 Mbps link)
mmllm fetch-artifacts ./mmllm-artifacts

# 3. Point the bench at the local copy
MMLLM_DEVICE=auto \
MMLLM_BANK_DTYPE=int8 \
MMLLM_BANK_ON_GPU=false \
MMLLM_SQRT_N=2048 \
mmllm bench-batch ./mmllm-artifacts/pile-github.bin 305000 \
                  ./mmllm-artifacts/pile-bank-3tier-int8 20 100 16
```

`MMLLM_DEVICE=auto` picks the best available backend in order
**cuda → mps → cpu**. On Apple Silicon laptops this routes the
dense matmuls through Metal Performance Shaders (the M-series
SoC GPU); the bank stays on CPU mmap and per-token top-K rows
are gathered+dequantized on CPU before being shipped back to the
GPU. Same pattern as our cuda + mmap-bank Modal benches.

Override the artifact source with `MMLLM_ARTIFACTS_URL` or pass
the URL as the second arg to `mmllm fetch-artifacts`.

To **publish** a release of artifacts you've trained yourself,
`scripts/release-artifacts.sh` wraps `gh release create` with the
right file labeling. Run it from any machine where the artifacts
are cached locally (e.g., after `modal volume get`).

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

### Pile-Github corpus

```
mmllm fetch-pile-github [out-path] [max-bytes] [workers]
                                             # download Pile-Github corpus (parallel streaming)
mmllm split-pile-github [in-path] [val-bytes] [test-bytes]
                                             # split into train/val/test
```

### mmap / long-running

```
mmllm train-mmap [base-path]                 # train with mmap-backed bank (creates <path>.0.bin … <path>.N.bin)
mmllm train-long [base-path] [mmap-path] [total-steps] [eval-every] [ckpt-every]
                                             # periodic eval-BPC + checkpoints; resumes from <base>.ckpts/
```

### Inference benchmarking

```
mmllm bench       [base] [ckpt-step] [bank-path] [n-warm] [n-time]
                                             # B=1 single-sequence tok/sec
mmllm bench-batch [base] [ckpt-step] [bank-path] [n-warm] [n-time] [B]
                                             # B parallel sequences; reports per-seq and aggregate tok/sec
mmllm bench-spec  [base] [ckpt-step] [bank-path] [n-warm] [n-time] [K]
                                             # speculative decoding: draft K, verify in parallel
```

### Artifacts & quantization

```
mmllm fetch-artifacts [out-dir] [url]        # download release artifacts from GitHub
mmllm bank-quantize [in-prefix] [out-prefix] [n-layers]
                                             # fp32 bank → int8 + per-row fp16 scale (~4× compression)
```

## Metrics

`train-long` emits one JSON-per-line event stream to `<base>.log.jsonl`.

| event | when | fields | how to read |
|---|---|---|---|
| `eval` | every `eval-every` steps during training | `step, loss, val_bpc, val_ppl, wall_s` | per-step learning curve. `val_bpc` here is capped at 50k tokens for speed — slightly pessimistic vs the full eval below |
| `ablation_intermediate` | every `ablate-every` steps if `MMLLM_ABLATE_EVERY > 0` | `step, control_bpc, ablated_bpc, delta_bpc, ablation_s, wall_s` | trajectory of "how load-bearing is the bank?" across training. Δ growing = bank's role expanding; flat or shrinking = dense weights absorbing more |
| `final` | once at end of training | `step, val_bpc, val_ppl, wall_s` | authoritative end-of-training bpc on full 100k-token val slice. ~0.05–0.10 lower than the periodic 50k-cap evals on the same checkpoint |
| `bank_saved` | once after `final`, when bank is mmap-backed | `step, bank_path, wall_s` | bank V dumped to `<path>.<i>.bin` mmap files; usable for warm-starting future runs |
| `ablation` | once after `bank_saved` | `step, control_bpc, ablated_bpc, delta_bpc, wall_s` | end-of-training Δ. See "interpreting Δ" below |
| `sync` | every `sync-every` steps under Hogwild | `step, dirty_pages, n_layers, sync_s, wall_s` | per-worker Modal Volume commit/reload telemetry |

### Interpreting Δ

Δ = `ablated_bpc - control_bpc`, measured by zeroing V across all blocks
and re-running eval. Positive Δ = the bank carries learned signal that
dense weights can't immediately reproduce.

Δ alone doesn't disambiguate "bank is dead weight" from "bank trained
slowly because it has more parameters than dense and got fewer SGD updates
per element." With sqrt_n=2048 and ~10M dense, the bank holds ~21M sparse-
trained entries vs ~10M densely-trained params — bank training rate per
element is ~470× slower. Expected behavior:

- **Early training**: small Δ regardless of architecture (bank not yet
  saturated; dense covers the patterns it can).
- **Mid-training**: Δ grows as bank rows accumulate enough updates to
  encode patterns dense can't.
- **Late training**: with `bank-query-mode=plain`, Δ continues to grow
  (bank becomes the long-tail catchall). With `ctx-add`, Δ may plateau
  lower — interpretation contested (see Results).

Use `MMLLM_ABLATE_EVERY` to log Δ across training; the trajectory
disambiguates "dead weight" from "still saturating" in any single run.

### Caveats

- 50k-cap periodic evals are systematically pessimistic vs the 100k
  `final` eval. Plan on a ~0.05–0.10 bpc drop between the last `eval`
  event and `final` on the same checkpoint.
- Seed noise at small scale is large: ~±0.1 bpc at 200-step / sqrt_n=128
  spike, dropping to ~±0.02 at 1B-token / sqrt_n=2048 prod scale. Don't
  read spike-scale comparisons as architectural rulings.
- Δ is confounded by total bank-update steps. A 5B-step plain run has had
  5× more bank-update steps than a 1B-step run; some of its larger Δ is
  bank-training-time, not architecture.

## Results

Tracked training runs on Pile-Github (~95 GB byte-level), default-config
dimensions (d_model=384, 5 layers, ~10M dense params).

| run | tokens | bank-query | long-mix | feedback | control bpc | Δ bpc | notes |
|---|---|---|---|---|---|---|---|
| 5B plain | 5.0B | plain | sum | plain | **1.273** | **+4.77** | reference baseline; bank carries massive signal at scale |
| 1B ctx-add | 1.0B | ctx-add | sum | plain | 1.354 | +0.75 | wins matched-token bpc through step 38k; smaller Δ → ctx-add lets dense weights absorb some content the bank otherwise would |
| 1B ctx-add+fb | 1.0B | ctx-add | sum | feedback | **1.352** | **+1.44** | bidirectional retrieval-augmented attention; raw bpc tied with ctx-add+plain; **Δ is 1.93× bigger** — feedback genuinely uses the bank harder |
| 5B ctx-add+fb | 5.0B | ctx-add | sum | feedback | (in flight) | (in flight) | sqrt_n=2048, ablate-every=5000 (60 Δ datapoints across training); CodeCarbon-instrumented for kWh/gCO2eq; ~17h on H100 |

All runs use `sqrt_n=2048` (~21M bank entries × 5 layers ≈ 18.8 GB bank V).

**The 1B ctx-add vs ctx-add+fb comparison is the cleanest architectural test**
in the matrix: same compute, same dense architecture except for the addition
of W_probe + W_back (bidirectional bank↔dense flow). At matched compute,
feedback wins on the structural metric (Δ) by roughly 2× without losing on
raw bpc. The 5B run scales this up to validate at compute parity with the 5B
plain reference.

Loose Pythia placement (Pile vs Pile-Github subset, byte-level vs BPE — not
strictly comparable but a sanity reference): mmllm at ~1.3 bpc lands
between Pythia-70M and Pythia-160M on the Pile-Github-equivalent measure,
with ~10M active dense params and an 18.8 GB bank vs Pythia's 70-160M dense
and no bank.

To plot trajectories from a log:

```python
import json
rows = [json.loads(l) for l in open('pile-github.bin.log.jsonl') if l.strip()]
evals     = [r for r in rows if r['event'] == 'eval']
abl_traj  = [r for r in rows if r['event'] == 'ablation_intermediate']
abl_final = next(r for r in rows if r['event'] == 'ablation')
energy    = next(r for r in rows if r['event'] == 'training_energy')
```

### Inference benchmark on the 5B-trained checkpoint

Quality preserved across all paths: BPC=1.27 with bank, ablation control
vs zeroed-V Δ=+4.77.

#### Single-stream (one user, autoregressive)

| setup | tok/sec | ms/tok |
|---|---|---|
| H100 + bank in VRAM (fp32) | **206** | 4.85 |
| 8-vCPU + bank mmap (fp32, Modal) | 107 | 9.37 |
| 4-vCPU + int8 bank mmap (local) | **163** | 6.12 |

Phase-1 + Phase-3 (int8 bank quantization, 4× compression: 18.8 GB →
4.5 GB) shipped. Single-stream optimizations explored and **rejected
on findings**:

| attempt | result | why |
|---|---|---|
| torch.compile | -83% GPU / -91% CPU | basilisp persistent vectors untraceable; sympy `pow_by_natural` crashes on dynamic narrow; recompile-limit thrash |
| speculative decoding (bank-zeroed draft) | -48% to -70% | at 10M dense, verify-K costs K× a single forward (matmuls compute-bound at small sizes), and skip_bank saves only ~17% per-step. The textbook 2× speedup requires a much larger model |

The Python kernel port (`mmllm.attention_kernel`) replaced basilisp-
side hot-path data flow with native Python tuples for caches; recovered
a -34% CPU regression and gave +18% on GPU vs the initial baseline.

#### Multi-stream (the architecturally interesting axis)

The autoregressive sequential bottleneck is fundamental — single-token
TPS is bounded by per-token forward latency. **The architecture's
multi-tenant story is where the wins compound.** Two paths shipped:

**Multi-process parallel inference** (4 vCPU, int8 bank, 4 procs × 1 thread):

| concurrency | per-proc | aggregate | scaling |
|---|---|---|---|
| 1 process × 4 threads | 158 | 158 | 1.0× |
| 4 processes × 1 thread | 104 each | **414** | **2.6×** |

Each process holds its own dense weights; all share one mmap'd 4.5 GB
int8 bank via the OS page cache. Bank cost amortizes; per-instance
RAM is just dense + per-conversation KV cache.

**Continuous batching** (`mmllm bench-batch`, single process serves N
sequences with one shared dense and one shared bank):

| batch B | per-seq tok/s | aggregate tok/s | hardware |
|---|---|---|---|
| 1 | 102 | 102 | i7-9750H (2019 Mac, AVX2 only) |
| 16 | 40 | 636 | i7-9750H |
| 64 | 12 | **758** | i7-9750H |
| 1 | 155 | 155 | 4-vCPU Sapphire Rapids (AMX, AVX-512 BF16) |
| 8 | 88 | 704 | 4-vCPU SPR |
| 32 | 48 | **1523** | 4-vCPU SPR |
| 128 | 14 | 1755 | 4-vCPU SPR |
| 1 | 228 | 228 | H100 |
| 64 | 197 | 12,598 | H100 |
| 256 | 209 | 53,630 | H100 |
| 512 | 143 | 73,048 | H100 |
| 1024 | 111 | **114,085** | H100 |

**One H100 = 114K aggregate tok/sec at B=1024, with per-sequence
latency staying above 100 tok/sec.** The unexpected finding: per-seq
latency stays usable all the way through B=1024 — no early collapse
from KV-cache pressure. The product-key bank's content-addressed
lookup batches efficiently (one (B, q_dim) × (sqrt_n, q_dim).T matmul
handles all B users) and the per-sequence KV caches are small enough
(~21 MB/seq at MAX_T=4096) to fit cleanly in HBM up to B=1024+.

**The 7-year-old i7-9750H result is the green-pitch's concrete
floor**: a 2019 consumer laptop with no AVX-512 and no matrix
accelerators (AMX/VNNI/BF16 hardware all absent on Coffee Lake)
still serves **~750 aggregate tok/sec at B=64 with a 4.5 GB shared
bank** — that's ~7 simultaneous editor sessions at 100 tok/sec each,
on a laptop that's been depreciated off corporate IT inventories.
The same architecture on Sapphire Rapids (newer silicon, narrower
core count, AMX present) more than doubles that. The gap is silicon
generation, not core count or memory: per-core throughput on AVX-512
BF16 hardware is roughly 2× AVX2-only at the same matmul size.

#### Multi-GPU extrapolation

Independent batches scale linearly across GPUs since each H100 holds
its own dense + bank-in-VRAM (the bank fits 80 GB VRAM trivially at
fp32, much more so at int8):

| hardware | aggregate tok/s | simultaneous users at 100 tok/s each |
|---|---|---|
| 4-vCPU laptop, B=32 | ~1,500 | ~30 |
| 32-core workstation, B=64 (projected) | ~10,000-15,000 | ~150 |
| 1× H100, B=1024 | 114,085 | ~1,100 |
| 8× H100 DGX (projected) | ~900,000 | ~9,000 |
| 64× H100 cluster (projected) | ~7,300,000 | ~73,000 |

For perspective, the entire active Clojure community (~50-100K devs)
fits comfortably on a small H100 cluster at simultaneous-FIM-user
quality of service.

See `docs/inference-optimization.md` for the full Phase-1-through-5
roadmap with implementation notes on what shipped, what didn't pay
off at this scale, and what's deferred (continuous-batching server
with heterogeneous prompts; CUDA graphs; AMX / BF16 dense — all of
which become wins as either model size or hardware tier grows).

## Green value

mmllm's architectural pitch is that a small dense network plus a large
mmap-shared sparse bank uses dramatically less RAM and power per
concurrent serving instance than a fully-dense model of comparable
quality. This section defines the units we measure, the formulas that
combine them, and the worked numbers we can cite today.

### Units

We use the same vocabulary as the green-AI literature so cross-comparison
is direct.

| metric | unit | reference |
|---|---|---|
| Joules per output token | `J/tok` | TokenPowerBench (arXiv 2512.03024); EuroMLSys 2025 ("Advocating Energy-per-Token in LLM Inference") |
| Tokens per Joule | `tok/J = 1 / J/tok` | MLPerf Power v5.1; ML.ENERGY (arXiv 2505.06371) |
| Training energy | `kWh` | CodeCarbon, pynvml; Patterson 2021 (arXiv 2104.10350) |
| CO2 emissions | `gCO2eq = kWh × PUE × grid_intensity` | Lacoste 2019 (arXiv 1910.09700); ML CO2 Impact Calculator |
| Per-instance VRAM at serving | `MB` | architectural; static |
| Reference grid intensity | 475 gCO2eq/kWh (global avg); range 20 (Quebec) to 736 (Iowa) | ML CO2 Impact |
| Reference PUE | 1.15 hyperscale; 1.5–1.8 enterprise | Uptime Institute |

`train-long` emits a `training_energy` event per run with `kwh`, `gco2eq`,
`j_per_tok`, `tok_per_s`, `peak_w`, `pue`, `grid_g_per_kwh` (see
`mmllm.metrics.EnergyTracker`). Backend auto-selects: CodeCarbon →
pynvml-only polling → wall+TDP fallback. The `backend` field tells you
which one ran. Override defaults via `MMLLM_GRID_INTENSITY` and `MMLLM_PUE`
env vars when you know your region/datacenter.

### Green-value formula

```
green_value = w_t · E_train_savings  +  w_i · E_inf_savings  +  w_m · M_density_advantage
```

Each component is independently measurable; pick weights based on your
deployment profile (heavy-training vs heavy-serving). All three are
unitless ratios in [0, 1].

#### 1. Training energy savings

```
E_train_savings = 1 - (kWh_mmllm / kWh_dense_baseline)
```

`kWh_mmllm` comes from the `training_energy` event. `kWh_dense_baseline`
is the kWh a dense model with comparable bpc would consume — estimated
via `gpu_hours × avg_power × PUE` from a published recipe (Patterson 2021
formula). At the FLOPs-per-token level, mmllm and a dense baseline of
similar parameter count are roughly comparable per training step; the
savings here are mostly from converging in fewer tokens (bank acts as a
larger effective parameter budget without the dense-FLOP cost).

#### 2. Inference energy savings (per concurrent user)

```
E_inf_savings = 1 - (J/tok_mmllm / J/tok_dense_baseline)
```

Reference dense numbers: Llama-3.3-70B FP8 on H100 ≈ 0.39 J/tok; Llama-65B
on A100 ≈ 3–4 J/tok; ~3 Wh/query at typical query lengths. mmllm at the
same hardware: TBD until the inference bench lands; expected to be
competitive at single-instance serving and dominant at multi-instance.

#### 3. Memory-density advantage (the mmllm-specific argument)

```
RAM_per_user_mmllm  = dense_bytes_per_instance + (bank_bytes / n_instances)
RAM_per_user_dense  = full_model_bytes_per_instance
M_density_advantage = 1 - (RAM_per_user_mmllm / RAM_per_user_dense)
```

The bank is shared via mmap — the OS page cache holds it once on a host
regardless of how many inference instances run. Per-instance dense weights
still scale linearly with concurrency. As `n_instances → ∞`, mmllm's
per-user RAM cost asymptotes to `dense_bytes_per_instance` alone (the
bank amortizes to zero).

Worked example with current architecture (10M dense fp32 = 40 MB,
18.8 GB bank at sqrt_n=2048) vs Pythia-160M (640 MB):

| concurrent users | mmllm VRAM | Pythia-160M VRAM | M_density |
|---|---|---|---|
| 1 | 40 MB + 18.8 GB = 18.84 GB | 640 MB | -28× (mmllm worse — bank dominates at low concurrency) |
| 10 | 400 MB + 18.8 GB = 19.2 GB | 6.4 GB | -3× (still worse) |
| 50 | 2.0 GB + 18.8 GB = 20.8 GB | 32 GB | +35% |
| 100 | 4.0 GB + 18.8 GB = 22.8 GB | 64 GB | +64% |
| 1000 | 40 GB + 18.8 GB = 58.8 GB | 640 GB (won't fit) | +91% |

Crossover around 30 concurrent users. Below that, dense Pythia-160M is
more memory-efficient because the bank is overhead. Above it, mmllm wins
asymptotically by ~16× (the per-instance dense ratio).

This curve is exact and doesn't need instrumentation to verify — it's an
architectural property of the config (`n_dense_params`, `sqrt_n`, `q_dim`,
`n_layers`).

### Memory access energy

The "shared mmap bank" claim is fundamentally about avoiding the cost of
holding parameters hot. Reference per-byte energy (Patterson 2017 "On
Computer Architecture for the Post-Moore Era", JEDEC DDR5 spec, Samsung
HBM2e datasheets):

| storage | read energy | idle power |
|---|---|---|
| HBM2e (A100/H100 VRAM) | ~60 pJ/byte | ~0.5 W/GB |
| DDR5 (host RAM / page cache) | ~240 pJ/byte | ~0.15 W/GB |
| NVMe SSD | ~1–10 nJ/byte | ~0 W/GB idle |

`EnergyTracker` records `peak_vram_gb` per run (via pynvml
`nvmlDeviceGetMemoryInfo`), and emits `vram_idle_kwh_estimate =
peak_vram_gb × 0.5 W/GB × wall_s` as the order-of-magnitude
attribution of run energy to "VRAM resident state."

Per-token forward-pass read traffic at fp16 (typical serving):

| | mmllm (default config) | Pythia-160M dense |
|---|---|---|
| dense weights touched | 10M × 2 B = 20 MB | 160M × 2 B = 320 MB |
| bank traffic per token | top_k × q_dim × 4 B × layers + key matrices ≈ 4.7 MB | n/a |
| total per-token weight read | ~25 MB | ~320 MB |
| memory-access energy (HBM @ 60 pJ/B) | ~1.5 mJ | ~19 mJ |
| ratio | 1× | ~13× |

This is the *moving-bytes* cost only — compute energy is hundreds of
mJ/token and dominates the per-token budget on both architectures. The
~13× memory advantage compounds with mmllm's smaller compute footprint
(~16× fewer dense FLOPs/token), but the headline savings still come
from compute, not memory access.

**The big "hot RAM cost" lives in idle power.** Per-instance steady-
state, comparing VRAM-resident state:

| state | VRAM | page cache | idle power | idle kWh / 24 h |
|---|---|---|---|---|
| 1× Pythia-160M | 320 MB | — | 0.16 W | 3.8 Wh |
| 1× mmllm (cold) | 20 MB | 0 (bank not faulted) | 0.01 W | 0.2 Wh |
| 1× mmllm (steady-state, 30% bank cached) | 20 MB | ~5.6 GB | 0.85 W | 20.4 Wh |
| 1× mmllm (all bank cached, fp32 18.8 GB) | 20 MB | 18.8 GB | 2.83 W | 67.9 Wh |

A SINGLE mmllm instance with the bank fully cached pays MORE idle power
than Pythia-160M (because the bank is bigger than the dense model). The
mmllm advantage shows up at concurrency, when bank cache is amortized:

| concurrent instances | mmllm idle (20 MB×N HBM + 18.8 GB DDR) | Pythia-160M idle (320 MB×N HBM) | mmllm advantage |
|---|---|---|---|
| 1 | 2.83 W | 0.16 W | -18× (mmllm worse) |
| 10 | 2.93 W | 1.6 W | -1.8× (still worse) |
| 100 | 3.83 W | 16 W | +4.2× |
| 1000 | 12.8 W | 160 W | +12.5× |
| 10,000 | 102.8 W | 1,600 W (won't fit) | +15.6× (asymptote) |

Crossover at ~30 concurrent instances per host (matches the RAM crossover
above — same physics, different units). Above ~1000 instances the bank
amortizes to zero per-instance overhead and idle power per user
asymptotes to dense-VRAM-only at the smaller dense size, ~16× lower
than dense baseline.

### 1T scale extrapolation

The architectural premise scales: a hypothetical mmllm with sqrt_n=10^6
(~1T entries × 250 dim ≈ 4 TB bank on disk fp32, 2 TB at fp16) and 1B
dense params, attempting to deliver GPT-4-class quality:

| | 1T dense (e.g., GPT-4 class) | 1T mmllm (1B dense + 2 TB bank on disk) |
|---|---|---|
| weights footprint | ~2 TB fp16 | 2 GB dense (per instance) + 2 TB on disk |
| GPUs for weights resident | ~25× H100 (tensor-parallel) | 1× H100 per inference batch |
| HBM idle power for weights | 25 × 80 GB × 0.5 W/GB ≈ 1,000 W | 1 × 2 GB × 0.5 W/GB ≈ 1 W |
| Page-cache DRAM (hot working set) | n/a (all in HBM) | ~100–500 GB DDR (working set fraction) |
| DDR idle for page cache | n/a | ~75 W (500 GB × 0.15) |
| Active inference power | ~17.5 kW (25 GPUs at full TDP) | ~700 W (1 GPU) |
| Disk capacity | 0 | ~2 TB NVMe (~$200) |
| Per-instance power at saturation | 17.5 kW | 700 W → **25× lower** |
| Per-instance idle (weights only) | 1,000 W | ~75 W → **13× lower** |

Per-token energy at this scale:
- 1T dense forward: ~2 TB read per token × 60 pJ/byte ≈ 120 J/tok memory
  + compute ≈ another ~1–10 J/tok depending on activation tier ≈ **~120 J/tok**
- 1T mmllm forward: ~2 GB dense + ~10 MB bank rows ≈ ~0.12 J/tok memory
  + ~50 mJ/tok compute (1B-dense scale) ≈ **~0.17 J/tok**

The ratio is **~700×** at the per-token energy budget if both could
deliver equivalent quality. The huge gap is dominated by memory traffic,
not compute — at 1T scale the parameters are too big to keep hot, so
moving them dominates.

Caveats on this extrapolation:

- **Quality parity is unproven.** No published evidence that a sparse
  bank of N entries equals a dense model of N parameters on language
  benchmarks. The 5B Pile-Github runs (~21M bank entries, sub-Pythia-
  160M-equivalent quality at byte-level) are the most recent data
  point. Scaling laws to 1T need research.
- **Disk bandwidth bottleneck.** Working set must fit in DRAM page
  cache, or per-token latency drops by a factor of 100× (NVMe vs DDR).
  Practical limit: working set ≤ ~512 GB on a single 1 TB host.
- **Page-fault tail latency.** First-time access to a cold bank row
  pays a 100 µs SSD read instead of a 100 ns DRAM read — multi-second
  p99 latency on cold prompts unless the bank is pre-warmed.
- **Numbers above use 0.5 W/GB HBM idle; real measured numbers vary
  ~2× depending on workload, ECC, and ambient.**

What this section is and isn't: this IS a case for serving 1T-class
quality on commodity hardware via the mmap-shared-bank architecture, IF
quality scaling holds. It is NOT a guarantee — it's the thesis the
architecture is designed to test, and the next several orders of
magnitude of training will tell us whether it does.

### Reading these numbers

- **Training energy** alone is comparable to dense models of similar
  active param count. mmllm doesn't fundamentally save energy per training
  step; it saves it per achieved-bpc (bigger effective param budget at
  similar dense FLOPs).
- **Single-instance inference** is also roughly comparable. The bank-side
  PKM lookup is sub-linear (O(√N)) but per-token compute is dominated by
  attention and FFN, both shared with dense.
- **Multi-instance serving** is where the architecture earns its "green"
  pitch. Above ~30 concurrent users on the current config, per-user RAM
  drops fast; above 100 users, mmllm fits on a single GPU what would need
  a multi-GPU dense deployment.

The strongest honest claim today: **at high serving concurrency, mmllm
delivers 60–90% lower per-user VRAM** than a dense model of comparable
serving quality. Power savings track memory savings closely (idle GPU
power scales sub-linearly with VRAM, but DRAM refresh + replicated KV
caches on dense scale linearly with users). BLOOM (Luccioni 2023, arXiv
2211.02001) explicitly broke out idle GPU power as ~22% of dynamic — a
useful upper bound on the multi-instance savings ceiling.

### Caveats

- Training kWh from the `training_energy` event is real when the backend
  is `codecarbon` or `pynvml`. If `backend = wall`, the value is a TDP
  fallback estimate — order-of-magnitude only, do not cite as a measured
  number.
- We don't yet have a production inference path; J/tok numbers here are
  TBD until the inference bench lands. Memory-density is exact today.
- The crossover concurrency depends on the bank size — at sqrt_n=512
  (default config) the bank is only 1.17 GB and crossover happens at ~2
  users. The "high-concurrency advantage" only matters at sqrt_n=2048+
  scale where the bank is large.
- Numbers above are byte-level / Pile-Github specific. BPE-tokenized
  models have different J/tok and bpc relationships; cross-tokenizer
  energy comparisons should normalize on tokens-per-byte.

## mmllm-moe: disk-offload inference for stock HuggingFace MoE models

`mmllm-moe` is a companion CLI that takes any HuggingFace Mixture-of-Experts
checkpoint (Qwen3, DeepSeek V4, Gemma 4, Mixtral, OLMoE, Granite, ...) and
converts it to a disk-offloaded mmap layout for inference on consumer GPUs
that can't fit the full model in VRAM.

The idea: keep only the **router + attention + embeddings resident on GPU**
(~3 GB for a 30B model), store the **expert weights on disk as int8**, and
page them into a **workload-adaptive LRU cache** in VRAM on demand. The
cache converges to the actually-routed experts for the running prompt —
no wasted VRAM on experts the router never selects.

### Quick start

```bash
pip install mmllm[moe]

# One-shot convert (downloads from HF, writes mmap layout to ~/.cache/mmllm-moe/)
mmllm-moe convert Qwen/Qwen3-30B-A3B --quant int8

# Generate
mmllm-moe gen Qwen/Qwen3-30B-A3B "Write a Fibonacci function in Python" \
  --hot-experts 64 --n-tokens 200

# Interactive chat
mmllm-moe chat Qwen/Qwen3-30B-A3B --hot-experts 64

# OpenAI-compatible server
mmllm-moe serve Qwen/Qwen3-30B-A3B --hot-experts 64 --port 8080

# Status
mmllm-moe info Qwen/Qwen3-30B-A3B
```

### Results: L4 (24 GB, $1/hr)

Two models, same hardware, same pipeline:

| Model | Total / active params | Experts | Throughput | On-disk | $/M tokens |
|---|---|---|---|---|---|
| **Qwen3-30B-A3B** | 30B / 3B | 128 × top-8, 48 layers | **5.66 tok/sec** | 27 GB int8 | $0.049 |
| **DeepSeek V4 Flash** | 284B / 13B | 256 × top-8, 43 layers | **1.12 tok/sec** | 258 GB fp8 | $0.25 |

Qwen3-30B-A3B at bf16 is ~60 GB — it doesn't fit on any consumer GPU.
`mmllm-moe` runs it at chat-usable throughput on a $1/hr L4 by keeping
3 GB resident and paging experts from disk.

DeepSeek V4 Flash is 284B parameters. At fp8 the raw weights are ~284 GB
— it normally needs a data-center GPU (≥80 GB) or multi-GPU. `mmllm-moe`
runs it coherently on the same $1/hr 24 GB GPU at >1 tok/sec.

### Cross-GPU results (Qwen3-30B-A3B, int8 + LRU)

| GPU | VRAM | $/hr | Best tok/sec | Budget | $/M tokens |
|---|---|---|---|---|---|
| T4 | 16 GB | $0.50 | 2.14 | h_e=48 | $0.065 |
| **L4** | **24 GB** | **$1.00** | **5.66** | **h_e=96** | **$0.049** |
| H100 | 80 GB | $5.00 | 14.08 | h_e=128 | $0.099 |

The L4 is the cost-performance sweet spot. The H100 is faster in absolute
terms but costs nearly 2× more per token.

### Optimization stack

Each layer stacks on the previous. Numbers are Qwen3-30B-A3B on H100:

| Optimization | h_e=0 | h_e=16 | h_e=32 | h_e=64 | h_e=128 |
|---|---|---|---|---|---|
| Static pinning [0..N) | 1.33 | 1.50 | 1.71 | 2.28 | 9.11 |
| LRU expert cache | 1.25 | 2.27 | 2.76 | 5.06 | 7.42 |
| LRU + `grouped_mm` | 1.75 | 3.07 | 4.23 | 9.39 | 16.38 |
| LRU + grouped_mm + int8 | 3.18 | 4.95 | 6.38 | **10.64** | 14.08 |

At the consumer-GPU budget (h_e=64): **2.28 → 10.64 tok/sec (4.7×)**.

### What didn't work

- **Global static pinning** — ranking experts by aggregate hits across
  layers and pinning the top-K globally. Throughput *regressed* monotonically.
  Each MoE layer specializes to different experts; global ranking wastes
  slots in every layer. Per-layer LRU is the correct architecture.

- **Speculative decoding** — disk-offload MoE breaks the amortization
  assumption. K-token verification activates proportionally more unique
  experts, scaling PCIe traffic linearly with K. 32% slowdown vs baseline.

### Tested checkpoints

No manual config needed — the converter auto-detects the MoE layout:

- `Qwen/Qwen3-30B-A3B` (128 × 48, deepseek-stacked)
- `deepseek-ai/DeepSeek-V4-Flash` (256 × 43, deepseek-stacked, fp8)
- `google/gemma-4-26B-A4B` (128 × 30, gemma4-stacked)
- `ibm-granite/granite-3.0-1b-a400m-base` (32 × 24, granite-stacked)
- `allenai/OLMoE-1B-7B-0924` (64 × 16, per-expert)
- `mistralai/Mixtral-8x7B-v0.1` (8 × 32, per-expert)
- `Qwen/Qwen1.5-MoE-A2.7B` (60 × 24, per-expert)
- `deepseek-ai/DeepSeek-V2-Lite` (66 × 26, per-expert)

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
├── scripts/
│   └── release-artifacts.sh # publish trained artifacts to GitHub Releases
├── docs/
│   └── inference-optimization.md  # phased inference optimization roadmap
├── src/mmllm/
│   ├── __init__.py
│   ├── _entry.py            # python shim → basilisp bootstrap + torch polyfills
│   ├── core.lpy             # model, training loop, CLI — all of it
│   ├── memory.py            # ProductKeyMemory, Int8ProductKeyMemory, PagedMmapStorage
│   ├── longcache.py         # paged LRU mmap KV cache (long-tier episodic store)
│   ├── corpus.py            # text8, enwik8, Pile-Github, Clojure corpus loaders
│   ├── optim.py             # CPUOffloadSparseAdam
│   ├── gating.py            # SumGate, ScalarGate, SwitchGate (long-tier path mixing)
│   ├── bank_query.py        # PlainBankQuery, CtxAddBankQuery (dense→bank query shaping)
│   ├── bank_feedback.py     # bank→dense feedback path (bidirectional retrieval)
│   ├── metrics.py           # EnergyTracker (kWh, gCO2eq, J/tok instrumentation)
│   ├── artifacts.py         # fetch-artifacts: download release bundles from GitHub
│   ├── attention_kernel.py  # custom attention kernels
│   ├── runtime.py           # inference runtime helpers (torch.compile wrapper)
│   ├── spec_decode.py       # speculative decoding
│   ├── moe.py               # MMapExpert, mmap tensor I/O, int8/fp8 quantization
│   ├── moe_cli.py           # mmllm-moe CLI (convert, gen, chat, serve, info)
│   ├── moe_loader.py        # HF checkpoint → mmap converter, LRU expert cache,
│   │                        #   cross-device forward, grouped_mm, self-contained loader
│   └── moe_server.py        # OpenAI-compatible HTTP server for mmap'd MoE models
├── docs/
│   ├── inference-optimization.md  # phased inference optimization roadmap
│   └── qwen3-30b-disk-offload-result.md  # full L4/T4/H100 benchmark results
└── tests/
    ├── __init__.py
    ├── test_smoke.lpy       # forward-pass shape + cache checks
    └── test_moe_synthetic.py  # MoE mmap round-trip + forward correctness
```

## License

mmLLM is released under the [BSD Zero Clause License (0BSD)](./LICENSE) —
a permissive, public-domain-equivalent license. You can use, modify,
redistribute, and ship the code (and any models trained with it) for
any purpose, commercial or otherwise, with no attribution requirement.

Why 0BSD specifically: the project's pitch is that AI infrastructure
should be cheap to deploy alongside your editor / on edge devices /
in privacy-constrained environments. Permissive licensing on the
training rig + inference code keeps that promise — anyone can fork,
specialize, and ship without a legal review cycle. Trained checkpoint
artifacts published to GitHub Releases inherit the same terms.
