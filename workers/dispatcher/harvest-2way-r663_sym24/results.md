# harvest-2way-r663 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R663 ctrl_bpc |
|--------|--------|--------------:|
| tDl3P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98c1deb6-tDl3P | 4.3068 |
| ZBCJK | fork-joly-os-mmllm-claude-train-sym24-e4f5cca1-ZBCJK | 4.3225 |
| **mean** | | **4.3147** |
| **best** | | **4.3068** |

## Chain progression R662 → R663

Previous harvest: `workers/dispatcher/harvest-7way-r662_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0935         | 4.3147         | +0.2212 |
| ctrl_bpc best  | 3.9717         | 4.3068         | +0.3351 |

## Per-round trajectory (best bird: tDl3P)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 663 | 4362 | 4.3068 | +0.1621 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r662_sym24`

## Output

`workers/dispatcher/harvest-2way-r663_sym24/round-663/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

