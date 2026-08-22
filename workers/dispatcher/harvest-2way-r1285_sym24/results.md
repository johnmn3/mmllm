# harvest-2way-r1285 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1285 ctrl_bpc |
|--------|--------|--------------:|
| ZpT9n | fork-SeniorCareMarket-mmllm-claude-train-sym24-cbd93f5a-ZpT9n | 2.2252 |
| E1w2c | fork-slaa-us-mmllm-claude-train-sym24-d1651741-E1w2c | 2.2335 |
| **mean** | | **2.2294** |
| **best** | | **2.2252** |

## Chain progression R1284 → R1285

Previous harvest: `workers/dispatcher/harvest-12way-r1284_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3368         | 2.2294         | -0.1075 |
| ctrl_bpc best  | 2.2154         | 2.2252         | +0.0098 |

## Per-round trajectory (best bird: ZpT9n)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1285 | 3782 | 2.2252 | +0.2682 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1284_sym24`

## Output

`workers/dispatcher/harvest-2way-r1285_sym24/round-1285/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

