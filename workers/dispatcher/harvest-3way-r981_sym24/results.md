# harvest-3way-r981 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R981 ctrl_bpc |
|--------|--------|--------------:|
| crjGB | fork-SeniorCareMarket-mmllm-claude-train-sym24-23e192f2-crjGB | 2.6232 |
| fvBCN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ef69708c-fvBCN | 2.7925 |
| DIENE | fork-joly-os-mmllm-claude-train-sym24-1a8b8918-DIENE | 2.9880 |
| **mean** | | **2.8012** |
| **best** | | **2.6232** |

## Chain progression R610 → R981

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.8012         | +0.6640 |
| ctrl_bpc best  | 2.1268         | 2.6232         | +0.4964 |

## Per-round trajectory (best bird: crjGB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 981 | 6364 | 2.6232 | +0.1400 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r980_sym24`
  - `workers/dispatcher/harvest-4way-r980_sym24`

## Output

`workers/dispatcher/harvest-3way-r981_sym24/round-981/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

