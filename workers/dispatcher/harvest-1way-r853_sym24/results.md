# harvest-1way-r853 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R853 ctrl_bpc |
|--------|--------|--------------:|
| 1n8HJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-583a8f79-1n8HJ | 2.9257 |
| **mean** | | **2.9257** |
| **best** | | **2.9257** |

## Chain progression R852 → R853

Previous harvest: `workers/dispatcher/harvest-4way-r852_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9601         | 2.9257         | -0.0344 |
| ctrl_bpc best  | 2.9180         | 2.9257         | +0.0077 |

## Per-round trajectory (best bird: 1n8HJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 853 | 4279 | 2.9257 | +0.3115 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r852_sym24`

## Output

`workers/dispatcher/harvest-1way-r853_sym24/round-853/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

