# harvest-2way-r1293 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1293 ctrl_bpc |
|--------|--------|--------------:|
| eML8p | fork-slaa-us-mmllm-claude-train-sym24-ad52e57b-eML8p | 4.3090 |
| m1JGH | fork-SeniorCareMarket-mmllm-claude-train-sym24-fa444ef1-m1JGH | 4.8465 |
| **mean** | | **4.5777** |
| **best** | | **4.3090** |

## Chain progression R1292 → R1293

Previous harvest: `workers/dispatcher/harvest-11way-r1292_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.8701         | 4.5777         | -0.2923 |
| ctrl_bpc best  | 4.5577         | 4.3090         | -0.2487 |

## Per-round trajectory (best bird: eML8p)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1293 | 4318 | 4.3090 | +0.0431 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1292_sym24`

## Output

`workers/dispatcher/harvest-2way-r1293_sym24/round-1293/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

