# v1 1B-token training launch — runbook

Target: 1B-token slow-walk training on the 60/30/10 mix (60%
aesopian-tiny-clojure-fables, 30% TinyStories+Cosmopedia textbook,
10% prior curricula combined), with FineWeb-Edu as the ambient web
floor.

## Pre-flight (operator)

You need:

- Modal CLI authenticated to the same workspace `modal_app.py`
  targets (see `modal token set` if not already configured)
- HuggingFace token in the Modal secret store (named
  `huggingface-secret` or `huggingface-token`); required for
  the gated datasets (xLAM, the-stack-v2-*)
- The `mmllm-data` Modal Volume already created
- The integration branch `claude/analyze-repo-status-rN0vt` either
  merged to `main`, or your local clone has it checked out before
  invoking `modal run` (Modal builds the image from the local
  repo state)

## Phase 0 — stage every corpus to the Modal Volume

Run these in any order; they're idempotent (resume / skip when
the byte-bin already exists at the target size).

```bash
# 1. The new fable curriculum (the 60% share). ~600 MB at
#    n_per_example=200 — bump n to 400 for ~1.2 GB (more variation
#    within each example, more total bytes).
modal run modal_app.py::build_aesop_curriculum \
    --out-path /data/aesop-curriculum.bin \
    --n-per-example 200

# 2. TinyStories (15% of mix). ~1 GB cap is plenty for slow-walk.
modal run modal_app.py::prepare_hf_dataset \
    --dataset-key tinystories \
    --out-path /data/tinystories.bin \
    --max-bytes 1000000000

# 3. Cosmopedia textbook (15% of mix). 1 GB cap.
modal run modal_app.py::prepare_hf_dataset \
    --dataset-key cosmopedia \
    --out-path /data/cosmopedia.bin \
    --max-bytes 1000000000

# 4. Prior curricula (the 10% share). Pick a single
#    representative; rotate across sessions if you want broader
#    coverage. ~500 MB per dataset.
modal run modal_app.py::prepare_hf_dataset \
    --dataset-key commitpackft-clj \
    --out-path /data/commitpackft-clj.bin \
    --max-bytes 500000000

modal run modal_app.py::prepare_hf_dataset \
    --dataset-key xlam \
    --out-path /data/xlam.bin \
    --max-bytes 500000000

modal run modal_app.py::prepare_hf_dataset \
    --dataset-key magicoder \
    --out-path /data/magicoder.bin \
    --max-bytes 500000000

modal run modal_app.py::prepare_hf_dataset \
    --dataset-key theorem-qa \
    --out-path /data/theorem-qa.bin \
    --max-bytes 100000000

# 5. FineWeb-Edu floor (10% baseline). 2 GB cap.
modal run modal_app.py::prepare_hf_dataset \
    --dataset-key fineweb-edu \
    --out-path /data/fineweb-edu.bin \
    --max-bytes 2000000000
```

After Phase 0, on the volume you should see:

```
/data/aesop-curriculum.bin       ~600 MB
/data/aesop-curriculum.train.bin ~500 MB
/data/aesop-curriculum.val.bin    50 MB
/data/aesop-curriculum.test.bin   50 MB
/data/tinystories.bin            ~1 GB
/data/cosmopedia.bin             ~1 GB
/data/commitpackft-clj.bin       ~150 MB (HF source caps the size)
/data/xlam.bin                   ~150 MB
/data/magicoder.bin              ~250 MB
/data/theorem-qa.bin             ~50 MB
/data/fineweb-edu.bin            ~2 GB
(plus .train.bin / .val.bin / .test.bin for each)
```

Sanity-check via `modal volume ls mmllm-data` and inspect the
first few KB of each base:

```bash
modal run modal_app.py::inspect_dataset --path /data/aesop-curriculum.bin
modal run modal_app.py::inspect_dataset --path /data/tinystories.bin
# ...
```

## Phase 1 — launch 1B-token training

The `--mix` flag takes `<path1>:<weight>,<path2>:<weight>,...`.
For 60/30/10 + 10% FineWeb floor:

```bash
MIX='/data/aesop-curriculum.train.bin:0.55,'\
'/data/tinystories.train.bin:0.135,'\
'/data/cosmopedia.train.bin:0.135,'\
'/data/commitpackft-clj.train.bin:0.025,'\
'/data/xlam.train.bin:0.025,'\
'/data/magicoder.train.bin:0.025,'\
'/data/theorem-qa.train.bin:0.015,'\
'/data/fineweb-edu.train.bin:0.09'

modal run --detach modal_app.py::train_with_bank \
    --base /data/aesop-v1 \
    --bank /data/aesop-v1-bank \
    --total-steps 250000 \
    --eval-every 2500 \
    --ckpt-every 5000 \
    --lr 1.4e-3 \
    --batch 128 \
    --sqrt-n 2048 \
    --bank-query-mode ctx-add \
    --bank-feedback-mode feedback \
    --max-hours 8.0 \
    --mix "$MIX"
```

At ~4K-byte sequences × batch 128 × 250K steps ≈ 1.3B tokens. Each
8-hour H100 session covers ~30K-50K steps depending on bank-query
overhead. Expect 5-8 sessions to land 1B tokens.

## Phase 2 — between sessions

The `--detach` lets the run continue if your terminal exits. The
ckpt cadence (every 5K steps) means each session checkpoints
several times even if it doesn't reach the time cap. Pull artifacts
locally for evaluation:

```bash
mmllm fetch-artifacts --base /data/aesop-v1 --to ./artifacts/aesop-v1/
```

Then evaluate on CPU using the eval harness referenced in the
README ("Per-ckpt eval harness" section, line 237).

The two key signals at each ckpt:
1. **Eval-tool-call format compliance** on a held-out fable record
   (does the model emit valid JSON tool calls?)
2. **Form parses + evaluates correctly** when the form is round-
   tripped through `mmllm.aesop.curriculum.form_parser` + `expr.py`
   (does the answer match what the form computes?)

## Phase 3 — monitor

```bash
# Live training log
modal logs --tail 100 -f <run_id>

# Eval log lines
tail -f /tmp/aesop-v1/aesop-v1.eval.jsonl | jq .

# Or use the existing slow-walk dashboard if you have one wired
```

## What I built / what I didn't

I built (on this branch):
- `mmllm.aesop.generate.generate_curriculum_corpus` — walks the
  K-12 curriculum × 5 fables, dedupes, splits into byte-bin
- `mmllm aesop generate --curriculum` CLI flag
- `modal_app.py::build_aesop_curriculum` Modal function that
  invokes the above on the volume

I did NOT (sandbox limitations):
- Authenticate to your Modal account
- Stage anything to your `/data` volume
- Launch any actual training

You invoke the Phase 0 + Phase 1 commands above from your
terminal. Each takes a few minutes (Phase 0 staging) to several
hours (Phase 1 training session) to run. Slow-walk the rest.

## If something breaks

- Curriculum generation crashes on Modal: re-run with smaller
  `--n-per-example` (e.g. 50) to confirm the import surface works,
  then bump back up.
- A `prepare_hf_dataset` call hangs on a gated dataset: confirm
  the HF secret is wired (`modal secret list` should show
  `huggingface-secret` or `huggingface-token`).
- `train_with_bank` launches but loss diverges: bisect by
  reducing `--mix` weights to put 100% on aesop-curriculum and
  confirming that loss converges; then re-introduce other corpora
  one at a time.
- Verifier mismatches creep in during generation: the parametric
  verifier is in `mmllm.aesop.curriculum.generator._draw_and_verify`
  — failures raise `VerifierMismatch` with the offending form +
  draws. Check / report which subject is failing.
