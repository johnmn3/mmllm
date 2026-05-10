# FIM validation runbook

This runbook turns the Phase 5 hypothesis in `fim-plan.md` into a concrete
sequence of measurable experiments. Each experiment is a self-contained
script you can run on a single CPU box (no GPU needed, no network beyond
optional source-data fetch).

The headline question:

> **Does FIM training on JSON / Clojure / Python code move `format_validity`
> on the xlam agent eval above 0.000?**

The current baseline (causal-LM only, ~val_bpc 0.27 on the community corpus)
sits at `format_validity = 0`. The hypothesis is that bidirectional structural
conditioning (FIM) provides the missing inductive bias for valid JSON
envelope synthesis.

## Pre-flight check

Before running any experiment, verify the FIM pipeline is wired correctly:

```bash
# 1. Build a tiny test corpus
mkdir -p /tmp/fim-sources && cat > /tmp/fim-sources/a.json <<'EOF'
{"tool_calls": [{"name": "search", "args": {"q": "transformers"}}]}
EOF
mmllm fim-build-corpus json /tmp/fim-sources /tmp/fim-smoke 0.7 0.5 42

# 2. Train 50 steps (~10 sec on CPU) to confirm loss mask wired
MMLLM_FIM_LOSS_MASK_MIDDLE_ONLY=true \
  mmllm train-fim /tmp/fim-smoke /tmp/fim-smoke-bank 50 25 25

# 3. Build the eval set and run eval (should produce a per-language table)
python scripts/build_fim_eval.py
mmllm fim-eval /tmp/fim-smoke.ckpts /tmp/mmllm-cpu/fim-eval.jsonl 50
```

If steps 1–3 produce sensible numbers (corpus has FIM markers, train loss
drops, fim-eval emits a per-language table with finite bpc), you're cleared
for the real experiments below.

## Experiment 5a — single-language POC (the headline test)

Hypothesis: training on JSON-only FIM moves `format_validity` on xlam off
zero, even slightly.

### Materials

- Source: JSON tool-call corpus, ~500MB of `{"tool_calls": [...]}`-shaped
  bodies. The `scripts/build_community_corpus.py` script produces some;
  augment with `xlam_function_calling_60k` slices or your own tool-use logs.
- Splitter: `json` (structural value-boundary cuts)
- Hardware: any CPU, ~24h wall for 50k steps at B=4 T=128

### Run

```bash
# Build the JSON-FIM corpus
mmllm fim-build-corpus json /path/to/json/sources /tmp/fim-json 0.7 0.5 0

# Train 50k steps with FIM loss masking
mmllm train-fim /tmp/fim-json /tmp/fim-json-bank 50000 5000 5000

# Measure FIM-bpc / FIM-exact on the eval set
python scripts/build_fim_eval.py
mmllm fim-eval /tmp/fim-json.ckpts /tmp/mmllm-cpu/fim-eval.jsonl

# Measure format_validity on the agent eval (xlam slice)
mmllm agent-eval /tmp/fim-json.ckpts/step-50000 xlam
```

### Decision matrix

| Result | Interpretation | Action |
|---|---|---|
| FIM-bpc on json eval < 2 AND format_validity > 0 | Hypothesis confirmed | Proceed to 5b/c |
| FIM-bpc < 2 BUT format_validity = 0 | FIM trains but doesn't transfer to xlam | Inspect xlam prompts for marker drift; ensure splitter targets right structural sites |
| FIM-bpc ≥ 4 | Training didn't converge | Check corpus size, splitter ratio, loss-mask wiring (env var actually set?) |
| FIM-exact = 0% on json eval | Greedy decoding broken or middles unpredictable | Inspect `fim_greedy_decode`; check that `<|fim_eom|>` terminates |

The single critical bit: **does the format_validity column move off 0.000?**
Magnitude is secondary at this stage.

## Experiment 5b — multi-language consolidation

Hypothesis: K workers each training on one language, harvested into a single
core, produce a stronger model than any single-language worker alone.

### Run

```bash
# 4 workers, each on one language
for lang in clojure python json javascript; do
    mmllm fim-build-corpus $lang /path/to/$lang/sources /tmp/fim-$lang 0.7 0.5 0
    mmllm train-fim /tmp/fim-$lang /tmp/fim-$lang-bank 25000 2500 2500
    mmllm fim-eval  /tmp/fim-$lang.ckpts /tmp/mmllm-cpu/fim-eval.jsonl > /tmp/eval-$lang.txt
done

# Stage the per-worker payloads (dense.pt + meta.json with FIM stats)
mkdir -p /tmp/workers
for lang in clojure python json javascript; do
    handle="solo-$lang"
    bpc=$(awk '/OVERALL/{print $4}' /tmp/eval-$lang.txt)
    mkdir -p /tmp/workers/$handle/step-25000
    cp /tmp/fim-$lang.ckpts/step-25000/dense.pt /tmp/workers/$handle/step-25000/
    cat > /tmp/workers/$handle/meta.json <<EOF
{
  "tokens_trained": 12800000,
  "steps": 25000,
  "label": "$handle",
  "fim": {"language": "$lang", "fim_ratio": 0.7,
          "splitter": "${lang}-boundary",
          "fim_eval_bpc": $bpc}
}
EOF
done

# Harvest into a single core, weighted by FIM quality
python -m mmllm.harvester \
    --workers /tmp/workers \
    --output  /tmp/fim-merged \
    --weighted-by fim_quality

# Eval the merged core on FIM + agent eval
# (need a small loader that reads merged dense.pt and runs eval —
#  fim-eval ckpt-dir works if you stage merged dense.pt into a step-N dir)
mmllm fim-eval /tmp/fim-merged /tmp/mmllm-cpu/fim-eval.jsonl
mmllm agent-eval /tmp/fim-merged xlam
```

### Decision matrix

| Result | Interpretation |
|---|---|
| Merged FIM-bpc < any single-language worker's bpc on that worker's language | Consolidation works; NetBank carries cross-language signal |
| Merged FIM-bpc only ≈ avg of workers | Pure FedAvg averaging, no synergy. Try `fim_quality` weighting or distill |
| Merged format_validity > best single-language format_validity | Cross-language structural knowledge composes — the architecture is the right shape |

## Experiment 5c — FIM vs causal at matched compute

Hypothesis: at identical token budget, the FIM model beats the causal model
on `format_validity` even though it might lag on raw val_bpc.

### Run

```bash
# Run A: causal-only on the same JSON source (no FIM markers, no loss mask)
mmllm fim-build-corpus json /path/to/json/sources /tmp/run-a-causal 0.0 0.0 0   # fim_ratio=0
mmllm train-cpu /tmp/run-a-causal /tmp/run-a-bank 50000 5000 5000

# Run B: FIM (PSM + SPM mix) on the same source
mmllm fim-build-corpus json /path/to/json/sources /tmp/run-b-fim 0.7 0.5 0
mmllm train-fim /tmp/run-b-fim /tmp/run-b-bank 50000 5000 5000

# Compare on val_bpc and format_validity
mmllm agent-eval /tmp/run-a-causal.ckpts/step-50000 xlam > /tmp/run-a-result.txt
mmllm agent-eval /tmp/run-b-fim.ckpts/step-50000    xlam > /tmp/run-b-result.txt
diff /tmp/run-a-result.txt /tmp/run-b-result.txt
```

### Decision matrix

| run-a (causal) | run-b (FIM) | Interpretation |
|---|---|---|
| format_validity 0.000 | format_validity > 0 | **Hypothesis confirmed.** Promote FIM to default training mix |
| both at 0.000 | both at 0.000 | FIM (alone) is insufficient. Either need scale, or FIM isn't the right inductive bias |
| run-a > run-b on format_validity | (counter-expected) | Re-check splitter, loss mask, eval correctness |

## What good telemetry looks like

Each run should produce a `step-N/meta.json` describing the run, plus a
log line per FIM eval pass that the harvester can read:

```json
{
  "language": "json",
  "step": 50000,
  "fim_bpc_overall": 1.42,
  "fim_exact_pct_overall": 12.3,
  "per_language": {
    "json":     {"bpc": 0.93, "exact_pct": 25.0},
    "clojure":  {"bpc": 1.85, "exact_pct":  5.0},
    "python":   {"bpc": 2.12, "exact_pct":  0.0},
    "generic":  {"bpc": 1.78, "exact_pct":  0.0}
  }
}
```

These per-language numbers tell you whether the model is over-fitting to
its training language (the diagonal element dominates) or generalizing
(other languages improve too).

## Reading the result

The hypothesis is binary: **does format_validity ever exceed 0.000?** If yes
on any single-language run, the architecture is sound and the work shifts
to scaling. If no on multiple sufficiently-trained runs, the hypothesis is
falsified and we re-think (likely: vocabulary, attention pattern, or training
data shape rather than the FIM objective itself).
