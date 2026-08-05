# harvest-8way-r1114 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1114 ctrl_bpc |
|--------|--------|--------------:|
| KyD6Q | origin/claude/train-sym24-1f0df6e1-KyD6Q | 2.3741 |
| YS4Nt | origin/claude/train-sym24-99b16eef-YS4Nt | 2.3835 |
| 6CWcN | fork-joly-os-mmllm-claude-train-sym24-44958197-6CWcN | 2.3901 |
| JHhr5 | fork-slaa-us-mmllm-claude-train-sym24-b78771cd-JHhr5 | 2.5695 |
| N4jA3 | fork-joly-os-mmllm-claude-train-sym24-ffbd8f85-N4jA3 | 2.5718 |
| AWOlx | origin/claude/train-sym24-fc79d3d7-AWOlx | 2.5736 |
| I0d7h | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0f34319d-I0d7h | 2.5818 |
| C8MWe | fork-SeniorCareMarket-mmllm-claude-train-sym24-e3cb2336-C8MWe | 2.5839 |
| **mean** | | **2.5035** |
| **best** | | **2.3741** |

## Chain progression R1113 → R1114

Previous harvest: `workers/dispatcher/harvest-9way-r1113_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5449         | 2.5035         | -0.0414 |
| ctrl_bpc best  | 2.3935         | 2.3741         | -0.0194 |

## Per-round trajectory (best bird: KyD6Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1114 | 6762 | 2.3741 | +0.2525 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1113_sym24`
  - `workers/dispatcher/harvest-7way-r1113_sym24`

## Output

`workers/dispatcher/harvest-8way-r1114_sym24/round-1114/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

