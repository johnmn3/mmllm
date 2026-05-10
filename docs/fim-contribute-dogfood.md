# FIM contributor dogfood prompt (v4)

Paste this into your AI coding assistant (Claude Code, etc.) when you want
guided help producing one FIM training contribution end-to-end. The
assistant will walk you through: corpus build → training → eval →
WORKERS.md update, verifying each step against measurable success criteria.

---

You are helping a contributor to the **mmllm** project produce a single
FIM (fill-in-the-middle) training contribution for the community. The
project's central hypothesis is in `docs/fim-plan.md`: byte-level causal
LM fits val_bpc on a small corpus yet produces 0 valid JSON tool-call
envelopes because it lacks bidirectional structural conditioning. FIM
training fixes that. The validation runbook is `docs/fim-validation-runbook.md`.

Your job in this session is to drive the contributor through **one full
cycle** of the FIM contribution flow, measuring real numbers at every
stage, and producing a tangible artifact (their entry on WORKERS.md +
a usable ckpt on HF Hub).

## Inputs you should ask the contributor for (use AskUserQuestion):

1. **Language target**: which language do they want to train on?
   Options: json (highest-impact for the headline test), clojure (well-supported
   splitter), python, generic. Recommend **json** for first-time contributors —
   it's directly on the critical path for the format_validity hypothesis.

2. **Source data**: where is their source corpus? Either
   - a local path (e.g., `~/code/my-projects`), or
   - a download URL (e.g., a HuggingFace dataset slice), or
   - they need you to scrape something locally (use `scripts/build_community_corpus.py`
     as a template — generate a tiny pack locally).

3. **Time budget**: how much wall time are they willing to spend?
   - **smoke** (10 min): 500 steps, just verifies pipeline works on their box
   - **short** (1–2 hr): 5k–10k steps, gives a first non-trivial FIM-bpc number
   - **overnight** (8–24 hr): 50k+ steps, the real contribution

## The cycle to drive:

### 1. Build the FIM corpus

```bash
mmllm fim-build-corpus <language> <source-root> /tmp/mmllm-cpu/fim-<lang> 0.7 0.5 42
```

After this runs, verify:
- `/tmp/mmllm-cpu/fim-<lang>.train.bin` exists and is non-empty
- The stats line shows `n_fim > 0` (FIM examples were actually produced)
- The stats line shows the chosen `language` (not a fallback to generic)

If `n_fim = 0`, the splitter declined every doc — likely the source corpus
has files too short to split. Suggest the contributor check their source
data: average file size should be ≥ 200 bytes for FIM to find cuts.

### 2. Train with FIM loss masking

```bash
mmllm train-fim /tmp/mmllm-cpu/fim-<lang> /tmp/mmllm-cpu/fim-<lang>-bank \
    <total-steps> <eval-every> <ckpt-every>
```

For the time budgets above:
- smoke: `500 100 100`
- short: `10000 1000 1000`
- overnight: `50000 5000 5000`

While it runs, watch the log line per step:
- `loss` should drop monotonically (some bumps OK)
- `tps` (tokens/sec) tells you the actual rate; expect 1k–3k on modern CPU
- `vram` should stay near 0 (this is CPU training)

If `loss` is flat at random (~5.5+) for >500 steps, the FIM loss mask may
not be wired — check that the env var `MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY=true`
is actually set by `train-fim` (it is, but worth confirming with
`echo $MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY` after the cmd runs).

### 3. Measure FIM-bpc and FIM-exact

```bash
# Build the eval JSONL if not already (deterministic, small)
python scripts/build_fim_eval.py

# Run the FIM eval on the latest ckpt
mmllm fim-eval /tmp/mmllm-cpu/fim-<lang>.ckpts /tmp/mmllm-cpu/fim-eval.jsonl
```

Record the OVERALL row from the printed table, AND the row for the
contributor's training language.

| Outcome | Interpretation |
|---|---|
| OVERALL bpc < 2.0 | Strong run — proceed to upload |
| OVERALL bpc 2.0–4.0 | OK run — proceed to upload, room to improve |
| OVERALL bpc > 4.0 AND training was overnight | Investigate: corpus size, splitter ratio, env vars |
| OVERALL bpc > 4.0 AND training was smoke/short | Expected — encourage longer run |

### 4. Stage the upload payload

The mmllm community uses HF Hub at `<TBD>/mmllm-workers` for uploads
(check `docs/contribute-compute.md` for the current target). Stage:

```bash
HANDLE=<their-handle>
STEP=<their-final-step>
LANG=<their-language>
mkdir -p /tmp/mmllm-upload/$HANDLE/step-$STEP
cp /tmp/mmllm-cpu/fim-$LANG.ckpts/step-$STEP/dense.pt \
   /tmp/mmllm-upload/$HANDLE/step-$STEP/dense.pt
# Optional: include the NetBank if they trained one
if [ -e /tmp/mmllm-cpu/fim-$LANG.ckpts/step-$STEP/bank-net-latest.0.bin ]; then
    cp /tmp/mmllm-cpu/fim-$LANG.ckpts/step-$STEP/bank-net-latest.*.bin \
       /tmp/mmllm-upload/$HANDLE/step-$STEP/
fi
```

Then write the `meta.json` using the actual measured numbers (DO NOT
make these up):

```json
{
  "tokens_trained": <steps * batch_size * seq_len, computed exactly>,
  "steps": <their-final-step>,
  "label": "<their-handle>",
  "fim": {
    "language": "<their-language>",
    "fim_ratio": 0.7,
    "splitter": "<lang>-form-boundary",
    "fim_eval_bpc": <OVERALL bpc from step 3>,
    "fim_eval_exact_pct": <OVERALL exact% from step 3>
  }
}
```

Critical: the bpc and exact_pct fields are **the** community signal. They
gate the FIM-quality weighting in the harvester. Lying about them isn't
just unfair — it actively poisons future merges. Treat them like checked-in
build artifacts.

### 5. Upload + WORKERS.md PR

Run the HF Hub upload (instructions in `docs/contribute-compute.md`),
then open a one-line PR adding their row to `WORKERS.md`:

```markdown
| <handle> | <language> | <steps> | <tokens> | <fim_eval_bpc> | <fim_eval_exact_pct> | <yes|no> | hf:.../<handle>/step-<step> |
```

The PR should be **literally one-line of diff** — no other changes. This
keeps review friction-free.

### 6. Verify by re-running the harvester locally

Have the contributor download a few other workers' ckpts and run:

```bash
python -m mmllm.harvester \
    --workers ./workers \
    --output  ./core-merged-local \
    --weighted-by fim_quality
```

Then compare their `meta.json` output to what other contributors produced.
This is the "trust but verify" step — anyone can reproduce the merge.

## What to report at the end of the session

A brief summary the contributor can paste into their PR description:

```
FIM contribution:
- language: <lang>
- steps: <N>
- tokens trained: <T>
- FIM-bpc OVERALL: <bpc>
- FIM-exact OVERALL: <pct>%
- per-language FIM-bpc on training lang: <bpc>
- training wall time: <Xh>
- hardware: <CPU model>
```

## Anti-patterns to flag

- **Don't fake the FIM stats**: bpc/exact% must be the actual numbers
  `mmllm fim-eval` printed. The harvester is deterministic; lying gets
  caught the first time someone reproduces the merge.
- **Don't upload the bank Vs unless the contributor opted into NetBank
  training**: Local Bank V is per-worker cortex and must never be in the
  upload. Only `dense.pt` + (optionally) `bank-net-latest.<i>.bin`
  belong in the upload.
- **Don't upload optimizer state**: `opt-dense.pt` and `opt-sparse.pt`
  are ~270MB each and never used after restart. Filter them out at
  upload-staging time.
- **Don't skip the eval**: a contribution without `fim_eval_bpc` is
  invisible to the FIM-aware harvester (gets weight 0 under `fim_bpc`
  / `fim_quality` modes).

## When in doubt

Read in order:
1. `docs/fim-plan.md` — why FIM, full architecture story
2. `docs/fim-validation-runbook.md` — what we're measuring
3. `docs/contribute-compute.md` — community / harvester mechanics
4. `WORKERS.md` — the live worker index format
