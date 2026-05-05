# Slow-walk budget plan

Realistic plan for training a v2 mmllm on a tight, weekly-replenished
budget — sized for ~$100/week, expandable as donations come in.

## The constraint

- Single H100 on Modal: ~$3/hr (varies; cross-check with `modal volume
  ls` or the Modal pricing page before each session).
- Budget: ~$100/week initially, growing with GitHub-page donations.
- Target: train a coherent agentic file-edit model (the v2 corpus mix
  → JSON tool calls — see [`corpus-mix-v2.md`](./corpus-mix-v2.md)).
- No 8×H100 single-shot run (that was Option B in
  [`parallelization-and-bank-sizing.md`](./parallelization-and-bank-sizing.md);
  ~$2.5-4k upfront, out of scope).

## The shape of the plan

**Slow-walk = many short sessions, all resuming from the latest ckpt
on volume.**  Each session:

1. Operator launches `modal run modal_app.py::train_with_bank`
   with `--max-hours <N>` set to budget the session.
2. `train-long` resumes from the latest ckpt under `<base>.ckpts/`.
3. Training runs for at most `max_hours`. Hits the cap → checkpoints
   cleanly + exits + `volume.commit()` durably persists everything.
4. Operator launches local evals (laptop / sandbox CPU) against the
   ckpts pulled via `mmllm fetch-artifacts`. Cheap, GPU-free.
5. Wait until the next batch of budget → repeat.

```
session 1 (8 h, $24)  ──→  step 0     → step ~30k    → ckpt + commit
                          (eval locally between sessions)
session 2 (8 h, $24)  ──→  step 30k   → step ~60k    → ckpt + commit
session 3 (8 h, $24)  ──→  step 60k   → step ~90k    → ckpt + commit
session 4 (8 h, $24)  ──→  step 90k   → step ~120k   → ckpt + commit
                          ← week 1 boundary, $96 spent
session 5 ...
```

Each `volume.commit()` durably persists dense + opt state + bank V
(after the fix in `801e203`), so a session that crashes or runs out
of paid time loses ≤ `ckpt-every` steps.

## Throughput math (refine after first session)

We don't have a precise H100 steps/hour number for the v2 setup yet
— the v1 5B-plain run completed but session-level energy logs aren't
broken out per-step. Conservative estimate:

| Throughput assumption | Steps/$100 (33 h) |
|---|---|
| 0.5 sec/step (optimistic) | ~240k |
| 1.0 sec/step (likely)     | ~120k |
| 2.0 sec/step (pessimistic)| ~60k  |

For reference: v1 5B-plain hit Δ +4.77 at 305k steps. Even on the
pessimistic assumption, $400-600 of total budget gets us into v1-
comparable training-volume territory.

**First session output**: budget ~3-4 hours → that gives a reliable
steps/hour number we can calibrate against. Use `progress_report`
to read it back.

## One-time Modal Secret setup

Two Modal Secrets unlock optional features. Both are conditional —
the app loads fine without them, you just lose the corresponding
features. Set them up once via the `modal` CLI from your terminal
(NOT in chat — pasting a token in chat triggers GitHub's auto-revoke):

```bash
# (a) HuggingFace token — unlocks gated datasets:
#       bigcode/the-stack-v2-dedup (Python/Markdown/Shell/Clojure subsets)
#       Salesforce/xlam-function-calling-60k
#     Get from huggingface.co/settings/tokens (read-only is fine).
#     Also click the license-acknowledgement on each gated dataset's HF page.
modal secret create huggingface-secret HF_TOKEN=hf_xxxxxxxxxxxx

# (b) GitHub token — unlocks --publish-after for train_with_bank.
#     Each session ends with the bank quantized to int8 + uploaded to a
#     `agent-step-<N>` (immutable) + `agent-latest` (force-replaced) GitHub
#     release. Get a fine-grained PAT from
#     github.com/settings/personal-access-tokens with `Contents: Read+Write`
#     scope on the johnmn3/mmllm repo.
modal secret create github-token GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

Verify:

```bash
modal secret list
```

Both Secret refs in `modal_app.py` are conditional via `_maybe_secret`
+ `_hf_secret` helpers — they probe `modal secret list` at module-import
time and only inject the Secret into function decorators when the named
Secret exists. So:

| Secret state | Behavior |
|---|---|
| Neither set up | Public datasets prep fine; gated datasets fail with clear "DatasetNotFoundError" warn; `--publish-after` fails clearly post-training |
| Only `huggingface-secret` | Gated dataset preps work; publish skipped |
| Only `github-token` | Public datasets only; publish works |
| Both | Full feature set |

## Clojure-specific corpus prep (separate from prepare_for_prod)

mmllm's eventual product target is a Clojure assistant, so the v2
warmup is biased Clojure-heavy. Three Clojure-specific Modal functions
run independently of `prepare_for_prod`:

```bash
# 1. mfikes/coal-mine: 4Clojure submissions, ~100 MB, polynomial-
#    hierarchy "many solutions per problem" goldmine. EPL-1.0.
modal run --detach modal_app.py::prepare_coal_mine

# 2. Clojars permissively-licensed libs: walks the Clojars feed,
#    license-filters, downloads source jars, extracts .clj files.
#    Multi-GB of real-world Clojure code. ~$0.20-0.50 to run.
modal run --detach modal_app.py::prepare_clojars_permissive

# 3. (When you're ready) the-stack-dedup (v1) Clojure config —
#    has actual `content` (unlike v2-dedup metadata-only). Needs the
#    HF license click-through at huggingface.co/datasets/bigcode/the-stack-dedup.
#    Then: edit DATASET_REGISTRY's the-stack-v2-clj entry to point at
#    the-stack-dedup with the-stack v1 schema, and re-run prepare_for_prod.
```

`humaneval-clj` (MultiPL-E HumanEval ported to Clojure, 161 problems)
is staged as part of `prepare_for_prod` but **eval-only** by convention
— it's the held-out benchmark for Clojure code-gen ability. Operator
does NOT include it in `--mix` for training; eval_watcher includes it
in `agent_evals` to score per-ckpt Clojure capability.

## One-time prod prep

Before the first paid training session, stage all the public datasets
on the Modal Volume at production caps (~30 GB total). Single command:

```bash
modal run --detach modal_app.py::prepare_for_prod
```

What it does:
- Spawns 11 parallel HF prep jobs (one per public dataset key in
  `mmllm.datasets.DATASET_REGISTRY`), each on its own Modal CPU
  container.
- Caps per `PROD_CAPS` in `modal_app.py`: SFT-style at 0.5-2 GB each,
  pretraining-style at 5 GB each. Tweak there if you want a different
  shape.
- Sets up symlinks `/data/agent-corpus-v2.bin.{train,val,test}.bin` →
  `/data/agent-corpus-v2/<primary>.bin.{train,val,test}.bin` (default
  primary is `fineweb-edu`) so `train-long` has a `<base>.val.bin` to
  drive in-training eval-bpc.

Cost: ~$1-3 of CPU container time. Wall time: 30-90 min.
Idempotent — re-running skips already-prepped datasets.

After it completes, smoke-check a few:

```bash
modal run modal_app.py::inspect_dataset_remote --path /data/agent-corpus-v2/code-contests.bin
modal run modal_app.py::inspect_dataset_remote --path /data/agent-corpus-v2/open-web-math.bin
```

## Curriculum: Clojure warmup → full v2 mix

The v2 architecture's product target is a Clojure assistant. The
slow-walk's session-boundary model lets us front-load Clojure
exposure during the first session ("born thinking in lambda
calculus through Clojure code") so the early gradients shape the
dense weights and bank toward S-expression / functional-style
substrate before the broader mix kicks in.

**Session 1 — Clojure-heavy warmup** (~30k steps, ~$18, ~2h H100):

```bash
modal run --detach modal_app.py::train_with_bank \
  --base /data/agent-corpus-v2.bin --bank /data/agent-bank-v2 \
  --total-steps 1000000 --max-hours 2.0 \
  --eval-every 2500 --ckpt-every 2500 --ablate-every 5000 \
  --batch 128 --sqrt-n 2048 --cpu-offload \
  --lr 1.4e-3 --lr-warmup 3000 \
  --bank-query-mode ctx-add --bank-feedback-mode feedback \
  --publish-after \
  --mix "/data/agent-corpus-v2/coal-mine.bin.train.bin:40,/data/agent-corpus-v2/clojars-permissive.bin.train.bin:25,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:15,/data/agent-corpus-v2/algebraic-stack.bin.train.bin:20"
```

40% coal-mine (multi-solution-per-problem signal) + 25% clojars
(raw Clojure scale) + 15% commitpackft-clj (file-edit signal) +
20% algebraic-stack (lambda-calculus reinforcement via Lean/Coq
proofs). The model spends ~500 M tokens in this Clojure-functional
substrate before broadening.

**Session 2+ — full v2 mix** (each ~$24 / 8 h):

The model resumes from session 1's ckpt with all the Clojure-shaped
weights and bank state intact; the broader mix from here on expands
its repertoire on top of that foundation.

## Per-session knobs

Recommended settings for a slow-walk session against the prod-prepped
corpora:

```bash
modal run --detach modal_app.py::train_with_bank \
  --base   /data/agent-corpus-v2.bin \
  --bank   /data/agent-bank-v2 \
  --total-steps 1000000 \
  --max-hours    8           \
  --eval-every   2500        \
  --ckpt-every   2500        \
  --batch        128         \
  --sqrt-n       2048        \
  --cpu-offload              \
  --lr           1.4e-3      \
  --lr-warmup    3000        \
  --bank-query-mode    ctx-add  \
  --bank-feedback-mode feedback \
  --ablate-every 5000        \
  --publish-after            \
  --mix "/data/agent-corpus-v2/commitpackft-py.bin.train.bin:20,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:12,/data/agent-corpus-v2/open-web-math.bin.train.bin:10,/data/agent-corpus-v2/algebraic-stack.bin.train.bin:8,/data/agent-corpus-v2/code-contests.bin.train.bin:8,/data/agent-corpus-v2/commitpackft-md.bin.train.bin:7,/data/agent-corpus-v2/magicoder.bin.train.bin:6,/data/agent-corpus-v2/commitpackft-sh.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-js.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2"
```

Notes:
- `total-steps 1_000_000` is high enough that we won't accidentally
  hit it during the slow walk; sessions just run for `max_hours` and
  exit on the timeout branch. Bump higher if we ever do.
- `ckpt-every 2500` (vs the previous 5000) → smaller blast radius if
  a session dies between scheduled ckpts. Each ckpt write costs ~few
  minutes of Modal volume IO (18.8 GB bank + dense + opt state).
- `eval-every 2500` keeps the val-BPC trajectory dense so the
  eval-watcher can score plenty of points.
- `ablate-every 5000` — ablation Δ measurement every 5k steps.
- The `--mix` argument enables the multi-corpus weighted sampler
  (`MMLLM_MIX` env var). Drop it (or pass `""`) to fall back to a
  single train-path.

### "Rolling" mix between sessions

The `--mix` argument is a **static string** at session launch — it
isn't auto-discovered, isn't auto-updated. Between sessions you (or
a script you keep) edit the `--mix` arg to add newly-staged datasets.
Concretely, what slow-walk looks like in the first weeks:

```
session 1:  only commitpackft + xlam + magicoder are staged (small,
            fast prep) →
            --mix "/data/commitpackft.train.bin:30,/data/xlam.train.bin:20,/data/magicoder.train.bin:50"

session 2:  cosmopedia finished its background prep →
            --mix "/data/cosmopedia.train.bin:40,/data/commitpackft.train.bin:25,/data/xlam.train.bin:15,/data/magicoder.train.bin:20"

session 3:  the-stack-v2-py finished →
            --mix "/data/the-stack-v2-py.train.bin:30,/data/cosmopedia.train.bin:30,/data/commitpackft.train.bin:15,..."
```

This produces a **distribution shift mid-training** — early steps see
a smaller, more SFT-heavy mix; later steps see the full pretraining-
style mix. For a slow walk this is acceptable (each step samples
whatever the current mix says; gradient direction adapts). The
alternative is "wait until everything is staged before starting,"
which means burning weeks of wall time on data prep with no training
progress.

If you want clean stationarity, hold off launching session 1 until
all sources are prepped. If you want training to start earlier and
don't mind the early sessions being a different distribution, start
small and grow the mix.

## Auto-eval against checkpoints during the run

Run `eval_watcher` in parallel with the training session — cheap A10G
container that polls `<base>.ckpts/` for new `step-<N>` directories
and runs the full eval battery (BPC + agentic) on each. Output goes
to the same `<base>.eval.jsonl` that `train-long` writes, so the
metrics plot on the same step axis as the in-training events.

Launch in a second terminal (or detached) right after kicking off
the training session:

```bash
modal run --detach modal_app.py::eval_watcher \
  --base /data/agent-corpus-v2.bin \
  --bank /data/agent-bank-v2 \
  --sqrt-n 2048 \
  --bank-on-gpu \
  --bank-query-mode ctx-add \
  --bank-feedback-mode feedback \
  --bpc-evals "fineweb-edu:/data/agent-corpus-v2/fineweb-edu.bin.test.bin,cosmopedia:/data/agent-corpus-v2/cosmopedia.bin.test.bin,open-web-math:/data/agent-corpus-v2/open-web-math.bin.test.bin,algebraic-stack:/data/agent-corpus-v2/algebraic-stack.bin.test.bin,code-contests:/data/agent-corpus-v2/code-contests.bin.test.bin,theorem-qa:/data/agent-corpus-v2/theorem-qa.bin.test.bin" \
  --agent-evals "commitpackft-py:/data/agent-corpus-v2/commitpackft-py.bin.test.bin,commitpackft-md:/data/agent-corpus-v2/commitpackft-md.bin.test.bin,commitpackft-sh:/data/agent-corpus-v2/commitpackft-sh.bin.test.bin,magicoder:/data/agent-corpus-v2/magicoder.bin.test.bin" \
  --n-samples 30 \
  --gen-len 256 \
  --poll-seconds 300
```

Watcher behavior:
- Polls every 5 min for new `step-<N>` ckpts.
- Runs BPC eval on the 6 pretraining-style splits — pure perplexity
  measurement, fast.
- Runs agentic eval on the 4 SFT-style splits — generates 30 samples
  per dataset, scores `format_validity` / `tool_name_match` /
  `tool_args_match` / `exact_match`.
- Idempotent: keeps a `<base>.eval.jsonl.seen.txt` of already-evaled
  steps, so a watcher restart picks up where it left off.
- Cost: ~$1/h A10G; eval per ckpt typically <2 min so the watcher is
  mostly idle.  Killing it stops billing immediately.

## Local eval against published ckpts (no Modal cost)

The `eval_watcher` runs evals on Modal as ckpts arrive (cheap A10G).
This section is the parallel laptop/sandbox path — pull a published
ckpt over HTTPS, run the same eval verbs locally on CPU. Free, useful
for sanity-checking what the published ckpts actually do without
spinning up a Modal container.

Prerequisite: the training session was launched with `--publish-after`
and the `github-token` Modal Secret is set up. Each session ends with
a release at `agent-step-<N>` (immutable) + `agent-latest`
(force-replaced).

```bash
# Pull the latest published ckpt to a local dir.
MMLLM_ARTIFACTS_URL=https://github.com/johnmn3/mmllm/releases/download/agent-latest \
  mmllm fetch-artifacts /tmp/agent-bench

# Pull the held-out test splits (each ~20 MB) — one-time, reuse across
# many ckpts. From your dev box if you have Modal access:
modal volume get mmllm-data /agent-corpus-v2/cosmopedia.bin.test.bin /tmp/agent-bench/
modal volume get mmllm-data /agent-corpus-v2/fineweb-edu.bin.test.bin /tmp/agent-bench/
modal volume get mmllm-data /agent-corpus-v2/commitpackft-py.bin.test.bin /tmp/agent-bench/
modal volume get mmllm-data /agent-corpus-v2/code-contests.bin.test.bin /tmp/agent-bench/
modal volume get mmllm-data /agent-corpus-v2/open-web-math.bin.test.bin /tmp/agent-bench/

# Run BPC evals on the prepared test splits (cheap; CPU-friendly).
# Args: <base> <ckpt-step> <bank-prefix> <test.bin> <name> <log.jsonl>
mmllm eval-bpc-on-path  /tmp/agent-bench/pile-github.bin  $STEP \
    /tmp/agent-bench/pile-bank-3tier-int8 \
    /tmp/agent-bench/cosmopedia.bin.test.bin   cosmopedia \
    /tmp/agent-bench/local.eval.jsonl
mmllm eval-bpc-on-path  /tmp/agent-bench/pile-github.bin  $STEP \
    /tmp/agent-bench/pile-bank-3tier-int8 \
    /tmp/agent-bench/fineweb-edu.bin.test.bin  fineweb-edu \
    /tmp/agent-bench/local.eval.jsonl

# Run agentic evals (generates JSON tool calls; CPU is slow but works).
# Args: <base> <ckpt-step> <bank-prefix> <test.bin> <name> <n-samples> <gen-len> <log.jsonl>
mmllm eval-agent /tmp/agent-bench/pile-github.bin  $STEP \
    /tmp/agent-bench/pile-bank-3tier-int8 \
    /tmp/agent-bench/commitpackft-py.bin.test.bin  commitpackft-py \
    20  256 \
    /tmp/agent-bench/local.eval.jsonl
```

Settings tuned for laptop CPU (vs the watcher's A10G defaults):
- `n_samples=20` (vs watcher's 30) keeps CPU eval under a minute per
  (ckpt × dataset).
- `gen-len=256` (vs watcher's 256-512). Lower → faster, but trims long
  tool-call payloads.
- Set `MMLLM_BANK_DTYPE=int8 MMLLM_BANK_ON_GPU=false MMLLM_SQRT_N=2048`
  in env before running so the int8 quantized bank gets loaded
  correctly via mmap (matches the v0.1-bench laptop runbook).

Local eval results land in `local.eval.jsonl` in the same shape as
the Modal-side eval log, so you can paste the rows together for
plotting.

## Progress check

```bash
modal run modal_app.py::progress_report --base /data/agent-corpus-v2.bin
```

Prints sessions completed, total wall hours, est $ spent (defaults
to $3/hr), latest training step, latest val bpc, and the last 10
ckpt step numbers on the volume. Use it to confirm a session ran the
expected duration before paying for the next one.

## Pre-flight smoke tests

**Local CPU smoke** — free, ~45-90s, runs the full pipeline against
synthetic data:

```bash
python scripts/smoke_phase0.py
```

Exercises ChatTemplate, formatters, mix sampler, max-hours session
timeout branch, save-checkpoint! → bank-latest writes, eval-bpc-on-path,
eval-agent. Catches integration bugs that would otherwise burn Modal $.

**Modal smoke** — exercises every dataset formatter against real HF
sources + (optionally) training, eval, and publish:

```bash
# Default: prep + inspect every public dataset (~$0.05-0.15)
modal run modal_app.py::smoke_pipeline_modal

# Add a 3-min training session on H100 (+ ~$0.15)
modal run modal_app.py::smoke_pipeline_modal --include-train

# Add the eval battery on A10G (+ ~$0.10)
modal run modal_app.py::smoke_pipeline_modal --include-train --include-eval

# Add the GitHub Release publish (+ ~$0.02; needs github-token Secret)
modal run modal_app.py::smoke_pipeline_modal \
    --include-train --include-eval --include-publish

# Include gated bigcode/the-stack-v2-dedup datasets (needs HF token setup)
modal run modal_app.py::smoke_pipeline_modal --include-gated
```

Default cost ~$0.10. Everything-on ~$0.40. Per-dataset failures are
captured in the summary rather than aborting the whole smoke. Run
this before the first real session to confirm the cloud paths work.

## Auto-publishing ckpts to GitHub Release

Each session's output (dense.pt + int8-quantized bank V) can be
auto-uploaded to a GitHub Release after training, so any machine
can pull the latest ckpt without Modal access.

### One-time setup

1. Create a GitHub Personal Access Token with `repo` + `write:packages`
   scope on `johnmn3/mmllm`. (Settings → Developer settings → Personal
   access tokens → Fine-grained.)
2. Stash it as a Modal Secret:
   ```bash
   modal secret create github-token GITHUB_TOKEN=ghp_xxxxxxxxxxxx
   ```

### Per-session: auto-publish at end

Pass `--publish-after` to `train_with_bank`. After training exits
cleanly, Modal spawns `publish_ckpt_to_github` on a separate
container (with `gh` CLI installed) which:

1. Quantizes `bank-latest.<i>.bin` → `bank-publish-int8.<i>.int8.bin`
   (~18.8 GB → ~4.7 GB total, fits GitHub's 2 GB-per-file limit per
   layer).
2. Creates a per-step release `agent-step-<N>` (immutable; idempotent
   if it already exists).
3. Force-replaces the moving `agent-latest` release with the same
   bundle so external pullers always have a fixed URL.

```bash
modal run --detach modal_app.py::train_with_bank \
  --base /data/agent-corpus --bank /data/agent-bank \
  --max-hours 8 \
  --publish-after \
  --tag-prefix agent \
  ...other knobs...
```

### Manual publish (for re-runs or out-of-band)

```bash
modal run modal_app.py::publish_ckpt_to_github \
  --base /data/agent-corpus \
  --tag-prefix agent
  # ckpt-step defaults to 0 = latest on disk
```

### Pulling published ckpts (from any non-Modal box)

```bash
# Latest (force-replaced each session).
MMLLM_ARTIFACTS_URL=https://github.com/johnmn3/mmllm/releases/download/agent-latest \
  mmllm fetch-artifacts /tmp/agent-bench

# Specific step (immutable, citable).
MMLLM_ARTIFACTS_URL=https://github.com/johnmn3/mmllm/releases/download/agent-step-30000 \
  mmllm fetch-artifacts /tmp/agent-bench
```

### Constraint to watch

`bank-latest.<i>.bin` is overwritten on every save-checkpoint! call.
`publish_ckpt_to_github` therefore only supports publishing the
**latest** ckpt — passing an older `--ckpt-step` errors out with
"bank state was overwritten." If you forget to publish a session
before starting the next one, the prior step's bank V is gone (only
its dense.pt remains in `step-<N>/`). Fix: enable `--publish-after`
so every session publishes automatically.

## Donation routing

The README has a Buy-Me-a-Coffee link. As contributions land:

- **First $100-300**: stays on the v2 base run. Each session bumps
  step count further toward the slow-walk target.
- **Any one-shot $500+ contribution**: consider a single Option B
  burst (8×H100 for ~12 h ≈ $400) to leapfrog several weeks of
  slow-walk steps in a day. Only worth it once we know the v2 corpus
  is well-formed (a bad mix burned at 8×H100 is just expensive
  garbage).

## Knobs we kept the same as v1 on purpose

To keep v2's results comparable to v1 5B-plain's Δ +4.77 baseline:

- **Bank**: `sqrt_n=2048 fp32` (18.8 GB). Same as v1.
- **Architecture**: 5 layers, q_dim=224, hard-split attention. Same.
- **Optimizer**: AdamW (dense) + SparseAdam (bank). Same.
- **Batch**: B=128 (same as v1 final).

What's different (intentional):
- **Corpus**: v2 mix (multi-source) vs v1 pile-github only.
- **Output schema**: JSON tool calls (chat-template wrapped) vs
  free-form continuation.
- **bank_query_mode**: `ctx-add` (vs v1 `plain`).
- **bank_feedback_mode**: `feedback` (vs v1 `plain`).

If the v2 trajectory underperforms v1 at comparable step count, the
explanation is in those four. Architecture, bank, batch all held
constant.

## Open items

1. **First-session calibration**: actual steps/hour. Will refine the
   above estimates after one short session lands a number.
2. **Free local eval cadence**: laptop CPU can run BPC + a small
   agentic eval suite in ~5 min per ckpt. With `ckpt-every 2500`,
   that's ~12 ckpts/session — manageable. If it becomes annoying,
   run evals only on every 4th ckpt.
3. **GH Release storage**: each `agent-step-<N>` release stores
   ~5 GB. After ~50 sessions that's ~250 GB on the public release
   storage. GitHub doesn't bill on public release size for normal
   usage, but if you want to tidy up, manually delete older
   `agent-step-<N>` tags via `gh release delete`. The latest tag
   always points at the most recent.
