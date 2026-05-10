# mmllm community workers

This is the public index of compute contributions to the mmllm project. Each
row records one worker's FIM (fill-in-the-middle) training run. The harvester
reads this file to discover and merge contributed ckpts.

To add yourself: open a one-line PR appending a row to the table below.
See [docs/contribute-compute.md](docs/contribute-compute.md) for the full
contribution flow, and [docs/fim-plan.md](docs/fim-plan.md) §4 for why FIM
is the current focus.

## Live workers

| Handle | Language | Steps | Tokens | FIM bpc | FIM exact% | NetBank | Ckpt URL |
|--------|----------|-------|--------|---------|------------|---------|----------|
| _(your row here)_ | _clojure_ | _10000_ | _5.1M_ | _1.42_ | _12.3_ | _yes_ | _hf:.../you/step-10000_ |

## How weighting works

The harvester combines worker ckpts via weighted FedAvg. You choose the weight
function with `--weighted-by`:

- `tokens_trained` (default): proxy for compute spent. Linear in tokens.
- `fim_bpc`: 1 / max(meta.fim.fim_eval_bpc, 0.1). Rewards consolidation
  quality, not just compute.
- `fim_quality`: tokens_trained / max(meta.fim.fim_eval_bpc, 0.1). Combines
  compute spent with measured quality. Recommended default for FIM merges.
- `uniform`: every worker contributes equally regardless of compute.

Workers without `meta.fim.fim_eval_bpc` are excluded from `fim_bpc` and
`fim_quality` merges (weight = 0).

## Required meta.json fields

Your worker upload bundle should include a `meta.json` with at least:

```json
{
  "tokens_trained": 5120000,
  "steps": 10000,
  "label": "your-handle",
  "fim": {
    "language": "clojure",
    "fim_ratio": 0.5,
    "splitter": "clojure-form-boundary",
    "fim_eval_bpc": 1.42,
    "fim_eval_exact_pct": 12.3
  }
}
```

Measure `fim_eval_bpc` locally with:

```
mmllm fim-eval <ckpt-dir> /tmp/mmllm-cpu/fim-eval.jsonl
```

before publishing your ckpt and adding your row here.

## Locally verify a merge

Anyone can clone this repo, pull the ckpts listed above, and reproduce the
merged core:

```
python -m mmllm.harvester \
    --workers ./workers \
    --output  ./core-merged \
    --weighted-by fim_quality
```

The harvester is deterministic for a given set of inputs and weight function;
two contributors running the same command will get bit-identical results.
