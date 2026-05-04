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

## Per-session knobs

Recommended settings for a slow-walk session:

```bash
modal run --detach modal_app.py::train_with_bank \
  --base   /data/agent-corpus \
  --bank   /data/agent-bank \
  --total-steps 1000000 \
  --max-hours    8           \
  --eval-every   2500        \
  --ckpt-every   2500        \
  --batch        128         \
  --sqrt-n       2048        \
  --lr           1.4e-3      \
  --lr-warmup    3000        \
  --bank-query-mode    ctx-add  \
  --bank-feedback-mode feedback \
  --ablate-every 5000        \
  --mix          "/data/the-stack-v2-py.train.bin:30,/data/fineweb-edu.train.bin:20,/data/cosmopedia.train.bin:15,/data/the-stack-v2-md.train.bin:10,/data/commitpackft.train.bin:8,/data/the-stack-v2-sh.train.bin:7,/data/magicoder.train.bin:5,/data/xlam.train.bin:5"
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

## Eval workflow between sessions

Local CPU evals (laptop or sandbox) — no Modal cost:

```bash
# Pull the latest ckpt + bank int8 from GitHub release (one-time).
mmllm fetch-artifacts /tmp/agent-bench

# Or, if you have Modal access:
modal volume get mmllm-data /agent-corpus.ckpts/step-30000/dense.pt ./
modal volume get mmllm-data /agent-bank-int8.<i>.bin ./

# Run BPC evals on the prepared test splits (cheap; CPU-friendly).
mmllm eval-bpc-on-path  ./agent-corpus  30000  ./agent-bank-int8 \
    /data/cosmopedia.test.bin   cosmopedia    /tmp/agent.eval.jsonl
mmllm eval-bpc-on-path  ./agent-corpus  30000  ./agent-bank-int8 \
    /data/fineweb-edu.test.bin  fineweb-edu   /tmp/agent.eval.jsonl

# Run agentic evals (generates JSON tool calls; CPU is slow but doable).
mmllm eval-agent ./agent-corpus 30000 ./agent-bank-int8 \
    /data/commitpackft.test.bin  commitpackft  20  256 \
    /tmp/agent.eval.jsonl
mmllm eval-agent ./agent-corpus 30000 ./agent-bank-int8 \
    /data/xlam.test.bin          xlam          20  256 \
    /tmp/agent.eval.jsonl
```

Fewer samples (`20` vs the Modal default `50`) and shorter generation
(`256` vs `512`) keep CPU eval under a minute per (ckpt × dataset).

## Progress check

```bash
modal run modal_app.py::progress_report --base /data/agent-corpus
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
