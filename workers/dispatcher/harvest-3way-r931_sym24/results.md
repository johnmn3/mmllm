# harvest-3way-r931 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R931 ctrl_bpc |
|--------|--------|--------------:|
| ioNOy | fork-slaa-us-mmllm-claude-train-sym24-ac2ed231-ioNOy | 2.6972 |
| yJWdH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e3620322-yJWdH | 2.7542 |
| v8Rct | fork-SeniorCareMarket-mmllm-claude-train-sym24-be42d9fe-v8Rct | 3.0895 |
| **mean** | | **2.8470** |
| **best** | | **2.6972** |

## Chain progression R930 → R931

Previous harvest: `workers/dispatcher/harvest-12way-r930_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8614         | 2.8470         | -0.0144 |
| ctrl_bpc best  | 2.7118         | 2.6972         | -0.0146 |

## Per-round trajectory (best bird: ioNOy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 931 | 6528 | 2.6972 | +0.2236 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r930_sym24`

## Output

`workers/dispatcher/harvest-3way-r931_sym24/round-931/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

