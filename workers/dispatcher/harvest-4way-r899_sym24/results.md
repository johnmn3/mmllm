# harvest-4way-r899 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R899 ctrl_bpc |
|--------|--------|--------------:|
| tnvOa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68f94186-tnvOa | 2.8029 |
| PSaBp | fork-slaa-us-mmllm-claude-train-sym24-cd33fcb5-PSaBp | 2.8147 |
| DQlXJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-2f1c521e-DQlXJ | 2.9634 |
| 19oCC | fork-joly-os-mmllm-claude-train-sym24-9c2dba47-19oCC | 2.9797 |
| **mean** | | **2.8902** |
| **best** | | **2.8029** |

## Chain progression R610 → R899

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.8902         | +0.7530 |
| ctrl_bpc best  | 2.1268         | 2.8029         | +0.6761 |

## Per-round trajectory (best bird: tnvOa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 899 | 4478 | 2.8029 | +0.2132 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r898_sym24`
  - `workers/dispatcher/harvest-8way-r898_sym24`

## Output

`workers/dispatcher/harvest-4way-r899_sym24/round-899/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

