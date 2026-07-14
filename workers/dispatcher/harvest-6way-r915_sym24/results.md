# harvest-6way-r915 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R915 ctrl_bpc |
|--------|--------|--------------:|
| jEmK6 | fork-joly-os-mmllm-claude-train-sym24-9d1fd118-jEmK6 | 2.7381 |
| IJgnh | origin/claude/train-sym24-66a20752-IJgnh | 2.7591 |
| lj0uU | fork-slaa-us-mmllm-claude-train-sym24-169b55a5-lj0uU | 2.7671 |
| n8EQc | fork-joly-os-mmllm-claude-train-sym24-918ca793-n8EQc | 2.7710 |
| 3dYz9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a1eab1fb-3dYz9 | 3.1283 |
| yzIbQ | origin/claude/train-sym24-9dd3a4db-yzIbQ | 3.1476 |
| **mean** | | **2.8852** |
| **best** | | **2.7381** |

## Chain progression R914 → R915

Previous harvest: `workers/dispatcher/harvest-2way-r914_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7747         | 2.8852         | +0.1105 |
| ctrl_bpc best  | 2.7730         | 2.7381         | -0.0349 |

## Per-round trajectory (best bird: jEmK6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 915 | 3834 | 2.7381 | +0.2082 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r914_sym24`
  - `workers/dispatcher/harvest-2way-r914_sym24`

## Output

`workers/dispatcher/harvest-6way-r915_sym24/round-915/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

