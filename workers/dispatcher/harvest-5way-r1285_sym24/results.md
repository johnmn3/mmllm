# harvest-5way-r1285 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1285 ctrl_bpc |
|--------|--------|--------------:|
| BbO38 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-39e7b5a4-BbO38 | 2.2170 |
| ZpT9n | fork-SeniorCareMarket-mmllm-claude-train-sym24-cbd93f5a-ZpT9n | 2.2252 |
| E1w2c | fork-slaa-us-mmllm-claude-train-sym24-d1651741-E1w2c | 2.2335 |
| uM7EO | origin/claude/train-sym24-e3e8cb3f-uM7EO | 2.4219 |
| FJbnb | fork-joly-os-mmllm-claude-train-sym24-93ed221d-FJbnb | 2.6135 |
| **mean** | | **2.3422** |
| **best** | | **2.2170** |

## Chain progression R1284 → R1285

Previous harvest: `workers/dispatcher/harvest-12way-r1284_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3368         | 2.3422         | +0.0054 |
| ctrl_bpc best  | 2.2154         | 2.2170         | +0.0016 |

## Per-round trajectory (best bird: BbO38)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1285 | 6980 | 2.2170 | +0.2504 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1284_sym24`

## Output

`workers/dispatcher/harvest-5way-r1285_sym24/round-1285/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

