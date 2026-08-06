# harvest-3way-r1124 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1124 ctrl_bpc |
|--------|--------|--------------:|
| YXxwZ | fork-slaa-us-mmllm-claude-train-sym24-28e00047-YXxwZ | 2.5665 |
| 4T2zJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-903d69b1-4T2zJ | 2.7531 |
| WECDJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6bcad816-WECDJ | 2.7614 |
| **mean** | | **2.6937** |
| **best** | | **2.5665** |

## Chain progression R610 → R1124

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.6937         | +0.5565 |
| ctrl_bpc best  | 2.1268         | 2.5665         | +0.4397 |

## Per-round trajectory (best bird: YXxwZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1124 | 6354 | 2.5665 | +0.2205 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1123_sym24`

## Output

`workers/dispatcher/harvest-3way-r1124_sym24/round-1124/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

