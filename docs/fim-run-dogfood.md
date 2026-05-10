# FIM run dogfood — JSON single-language POC (v1)

Self-contained prompt to dispatch one full FIM (fill-in-the-middle)
training cycle on the mmllm project. This is the **headline experiment**
from `docs/fim-validation-runbook.md` §5a — the test that determines
whether the FIM hypothesis lives or dies.

Copy everything below the `---` divider into a fresh Claude Code session
in this repo and dispatch.

---

You are dispatched to execute one full FIM training cycle on the mmllm
project and report whether the central FIM hypothesis holds at this
scale. The FIM pipeline (CLI verbs, splitters, loss mask, eval harness)
already exists in this repo's history — your job is to **find it, get
it working on your branch, then run the experiment and report the
numbers**. Do not reimplement FIM infrastructure from scratch; but
also do not bail just because the verbs aren't on your current branch
yet — the code is somewhere reachable (a sibling branch or remote),
and pulling it in is normal setup work, not scope creep.

**Default disposition: make forward progress.** If a step fails in a
way that has an obvious next probe (try another branch, reinstall the
package, fall back to a smaller corpus, halve the LR), take it. Only
stop-and-report if you've genuinely exhausted reasonable options or
the run hit something destructive. The user prefers a partial report
with caveats over a clean abort.

## The hypothesis

mmllm is a byte-level LM that fits `val_bpc ≈ 0.27` on the community
corpus yet produces `format_validity = 0.000` on the xlam agent eval —
zero valid JSON tool-call envelopes. The conjecture in `docs/fim-plan.md`:
causal LM lacks bidirectional structural conditioning. FIM (Bavarian
et al, arxiv:2207.14255) gives the model prefix AND suffix when filling
structural middles — exactly the conditioning that valid JSON envelope
synthesis needs.

You're testing whether **JSON-FIM training moves `format_validity` off
zero**. Any value > 0.0 confirms the hypothesis at first-signal level.

## Background you should skim (3 minutes)

- `docs/fim-plan.md` (architecture story; skim §1–§3)
- `docs/fim-validation-runbook.md` (your decision matrices; read §5a in full)
- `WORKERS.md` (the meta.json format you'll produce at the end)

You do NOT need to read the implementation files unless something
fails — the CLI verbs are stable.

## Run plan

Total wall budget: **3–6 hours on a modern CPU**. If you blow past 8h
without reaching step 4, abort and report.

### Step 0 — Verify pipeline is wired (and get it wired if it isn't)

```bash
mmllm 2>&1 | grep -E "fim-build-corpus|train-fim|fim-eval"
```

Should print three FIM verbs. If empty, the FIM code exists in this
repo's history but not on your current branch yet. Find it and pull
it in:

```bash
# 1. Locate the FIM branch (it'll be a claude/* branch with "fim" or
#    "analyze-repo" in the name; the marker bytes <|fim_pre|> are a
#    reliable grep target)
git fetch --all --quiet
git branch -r | grep -iE "fim|analyze-repo"
git log --all --oneline --grep="FIM" | head -10

# 2. Merge it in (replace BRANCH with what you found above)
git merge --no-edit origin/BRANCH

# 3. Re-install so the new CLI verbs register
pip install -e . --quiet

# 4. Re-verify
mmllm 2>&1 | grep -E "fim-build-corpus|train-fim|fim-eval"
```

If after a merge + reinstall the verbs still don't show, try
`pip install -e . --force-reinstall --quiet` (basilisp sometimes
caches). Only stop and report if you've tried merging every plausible
branch AND a force reinstall AND the verbs still aren't there.

### Step 1 — Acquire JSON source data

Prefer xlam (it's the eval target, so training distribution matches):

```bash
mkdir -p /tmp/mmllm-cpu/sources
mmllm prepare-hf-dataset xlam /tmp/mmllm-cpu/sources/xlam 200000000 5000000 5000000
ls -lh /tmp/mmllm-cpu/sources/xlam.*.bin
```

This should produce `xlam.train.bin` (~200MB), `xlam.val.bin`,
`xlam.test.bin`. The .bin files are raw byte streams — fim-build-corpus
expects a directory of source files, not a bin. So unpack a slice to
.json files for FIM splitting:

```bash
mkdir -p /tmp/mmllm-cpu/sources/xlam-json
python3 - <<'PY'
from pathlib import Path
data = Path("/tmp/mmllm-cpu/sources/xlam.train.bin").read_bytes()
# xlam bin is concatenated turns separated by \n\n; split into ~50k docs
docs = [d for d in data.split(b"\n\n") if 100 < len(d) < 4096]
print(f"{len(docs)} candidate docs from xlam train")
out = Path("/tmp/mmllm-cpu/sources/xlam-json")
for i, doc in enumerate(docs[:20000]):   # cap at 20k to keep build_fim_corpus fast
    (out / f"doc-{i:05d}.json").write_bytes(doc)
print(f"wrote {min(20000, len(docs))} files to {out}")
PY
```

If xlam isn't available, fall back to any locally-available JSON
corpus (e.g. an existing tool-call log directory). Note the source in
your final report.

### Step 2 — Build the FIM corpus

```bash
mmllm fim-build-corpus json /tmp/mmllm-cpu/sources/xlam-json \
    /tmp/mmllm-cpu/fim-json 0.7 0.5 42
```

Expected stats line: `n_fim > 5000`, train_bytes > 10MB, language=json.

**Abort condition**: if `n_fim < 100`, the splitter rejected nearly
every doc — the source corpus has the wrong shape. Report and stop.

### Step 3 — Train

10,000 steps. Eval every 1,000, ckpt every 1,000. Default cpu-tiny
config; train-fim auto-enables the middle-only loss mask.

```bash
mmllm train-fim /tmp/mmllm-cpu/fim-json /tmp/mmllm-cpu/fim-json-bank \
    10000 1000 1000 2>&1 | tee /tmp/mmllm-cpu/fim-json.train.log
```

Monitor the streaming log lines:
- `loss` should drop from ~5.5 (random) → ~1–2 by step 10k
- `tps` should be 1k–5k tokens/sec on CPU
- Periodic `eval-bpc` lines report val_bpc — should drop from ~3 → ~1
- Each `ckpt at step N` produces `/tmp/mmllm-cpu/fim-json.ckpts/step-N/dense.pt`

**Abort conditions**:
- Loss flat at ~5.5 for ≥2k steps → FIM mask not firing. Check
  `echo $MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY` (should be "true").
- Loss diverges to NaN → numerical instability. Halve LR (env
  MMLLM_LR=1.5e-3) and rerun.
- tps < 100 → environment misconfigured. Check MMLLM_NUM_THREADS.

You may want to run training in the background (`run_in_background: true`
in your Bash call) so you can poll periodically without blocking.

### Step 4 — FIM evals

```bash
python /home/user/mmllm/scripts/build_fim_eval.py
mmllm fim-eval /tmp/mmllm-cpu/fim-json.ckpts \
    /tmp/mmllm-cpu/fim-eval.jsonl 10000 \
    2>&1 | tee /tmp/mmllm-cpu/fim-json.fim-eval.txt
```

Record from the printed table:
- OVERALL bpc
- OVERALL exact%
- `json`-row bpc + exact% (the training-language row — should be the
  strongest by far)
- `clojure`/`python`/`generic`-row bpc (cross-language generalization
  signal — expected to be weaker but not random)

### Step 5 — Agent eval (the headline)

```bash
mmllm eval-agent /tmp/mmllm-cpu/fim-json 10000 \
    /tmp/mmllm-cpu/fim-json-bank \
    /tmp/mmllm-cpu/sources/xlam.test.bin xlam 100 256 \
    2>&1 | tee /tmp/mmllm-cpu/fim-json.agent-eval.txt
```

100 samples, 256 byte generation length. Records:
- **format_validity** ← the headline number
- name_match
- args_match
- exact_match

Look at the actual decoded outputs printed in the log — even a single
sample with a properly-closed `{"tool_calls": [{...}]}` envelope
counts as movement off zero.

### Step 6 — Write meta.json with measured numbers

DO NOT MAKE UP NUMBERS. Use the actual values from steps 4 and 5.

```bash
# Compute tokens_trained = steps × batch_size × seq_len
TOKENS=$((10000 * 4 * 128))   # = 5,120,000

# Write the meta.json
cat > /tmp/mmllm-cpu/fim-json.ckpts/step-10000/meta.json <<EOF
{
  "tokens_trained": $TOKENS,
  "steps": 10000,
  "label": "fim-dogfood-$(date -u +%Y%m%dT%H%MZ)",
  "fim": {
    "language": "json",
    "fim_ratio": 0.7,
    "psm_ratio": 0.5,
    "splitter": "json-value-boundary",
    "fim_eval_bpc": <OVERALL bpc from step 4>,
    "fim_eval_exact_pct": <OVERALL exact% from step 4>,
    "agent_format_validity": <format_validity from step 5>,
    "agent_name_match": <name_match from step 5>,
    "agent_args_match": <args_match from step 5>
  }
}
EOF
cat /tmp/mmllm-cpu/fim-json.ckpts/step-10000/meta.json
```

### Step 7 — Journal + commit on a fresh branch

```bash
git checkout -b claude/fim-run-json-$(date -u +%Y%m%d)
mkdir -p docs/journal
TS=$(date -u +%Y-%m-%d-%H%M)
cat > docs/journal/${TS}-fim-run-json-10k.md <<EOF
# FIM run — JSON 10k steps

## Setup
- date (UTC): $(date -u)
- language: json
- source: xlam train.bin (200MB → 20k docs filtered to 100–4096 bytes)
- splitter: json-value-boundary
- fim_ratio: 0.7  /  psm_ratio: 0.5
- steps: 10000  /  batch: 4  /  seq_len: 128
- tokens: 5,120,000
- bank: cpu-tiny mmap

## Results (raw)

### Train trajectory
<final loss, final val_bpc, tps, wall time>

### FIM eval (step 10000)
<paste the printed table>

### Agent eval (xlam, 100 samples)
<paste the printed metrics + 2-3 representative decoded outputs>

## Decision

<which row of step 7's matrix applied; one-paragraph rationale>

## Notes / surprises

<anything unexpected, error traces, behavior worth flagging>
EOF

git add docs/journal/${TS}-fim-run-json-10k.md \
        /tmp/mmllm-cpu/fim-json.ckpts/step-10000/meta.json   # path doesn't apply if /tmp isn't tracked — adapt
git commit -m "FIM dogfood run: JSON 10k steps — <hypothesis result one-liner>"
git push -u origin $(git branch --show-current)
```

(If `/tmp/...` isn't a tracked path, just copy the meta.json into the
repo at `docs/journal/${TS}-fim-run-json-10k.meta.json` and commit that
alongside the journal.)

### Step 8 — Decision matrix and report

| format_validity | FIM-bpc OVERALL | Decision | Recommendation |
|---|---|---|---|
| > 0.0  | < 2.0  | **HYPOTHESIS CONFIRMED.** Bidirectional conditioning is the missing piece. | Proceed to Phase 5b (multi-language consolidation) and 5c (matched-compute ablation). |
| > 0.0  | 2.0–4.0 | Confirmed but weak. | Run a 50k extension on the same ckpt; investigate splitter quality. |
| = 0.0  | < 2.0  | Training converged but doesn't transfer to xlam. | Inspect xlam prompts for marker/format drift; consider mixing PSM and SPM differently. |
| = 0.0  | ≥ 4.0  | Training under-converged. | Run a 50k extension before claiming refutation. |
| = 0.0  | ≥ 4.0 after >30k steps | Hypothesis weakened. | Re-examine: vocab? attention pattern? data shape? |
| NaN / aborted | — | Pipeline bug or environment issue. | Report with log excerpts. |

## What to post back to the user

A single message (under ~30 lines) with:

1. **Headline**: hypothesis status (confirmed / weakened / aborted) and
   `format_validity = <value>`.
2. **Numbers table**:
   ```
   train final loss:           <X>
   val_bpc final:              <X>
   FIM-bpc OVERALL:            <X>
   FIM-exact OVERALL:          <X>%
   FIM-bpc json (trained):     <X>
   FIM-exact json (trained):   <X>%
   agent format_validity:      <X>
   agent name_match:           <X>
   agent args_match:           <X>
   wall time:                  <Xh Ym>
   ```
3. **One example decoded agent output** (success or representative
   failure — pasted verbatim from step 5's log).
4. **Decision matrix row** that applied and **recommended next step**.
5. **Any surprises** worth flagging (env quirks, unexpected curve shape,
   etc.).

Brevity matters here — the user is going to scan this fast to decide
whether to fund a 50k run or pivot.

## Hard rules

- **Do not fake numbers.** Every value in meta.json and the journal must
  come from a real `mmllm fim-eval` / `mmllm eval-agent` invocation in
  this session.
- **Do not commit `opt-*.pt` or `bank-latest.<i>.bin`** — those are
  per-worker state, not for sharing. Only `dense.pt` + meta.json.
- **Do not push to `main`.** Push to the `claude/fim-run-json-<date>`
  branch you created in step 7.
- **If the run dies mid-stream**, save the partial log and report rather
  than retrying silently. We want to know about failures.
- **If you find a pipeline bug** (e.g. loss mask not firing), file it as
  a separate commit on a separate branch — do not entangle pipeline
  fixes with this experiment commit.
