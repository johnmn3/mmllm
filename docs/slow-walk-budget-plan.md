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
2. **Bank int8 distribution via GH Release**: the existing
   `scripts/release-artifacts.sh` flow from v1 needs to be re-run
   per-ckpt as the v2 trajectory unfolds. Worth scripting "after
   each session, publish the latest ckpt to a rolling release tag."
3. **Free local eval cadence**: laptop CPU can run BPC + a small
   agentic eval suite in ~5 min per ckpt. With `ckpt-every 2500`,
   that's ~12 ckpts/session — manageable. If it becomes annoying,
   run evals only on every 4th ckpt.
