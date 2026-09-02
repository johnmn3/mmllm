# harvest-2way-r1380 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1380 ctrl_bpc |
|--------|--------|--------------:|
| zrbln | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-df743b41-zrbln | 3.2056 |
| 2YuyP | fork-SeniorCareMarket-mmllm-claude-train-sym24-343cd007-2YuyP | 3.4268 |
| **mean** | | **3.3162** |
| **best** | | **3.2056** |

## Chain progression R1379 → R1380

Previous harvest: `workers/dispatcher/harvest-2way-r1379_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1011         | 3.3162         | +0.2151 |
| ctrl_bpc best  | 3.0921         | 3.2056         | +0.1135 |

## Per-round trajectory (best bird: zrbln)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1380 | 6718 | 3.2056 | +0.1118 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1379_sym24`

## Output

`workers/dispatcher/harvest-2way-r1380_sym24/round-1380/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

