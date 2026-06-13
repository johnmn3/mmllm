# harvest-7way-r663 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R663 ctrl_bpc |
|--------|--------|--------------:|
| giHcS | origin/claude/train-sym24-d78a9a6a-giHcS | 3.9529 |
| OYW4u | fork-SeniorCareMarket-mmllm-claude-train-sym24-bda45993-OYW4u | 3.9842 |
| WRdwR | fork-davidwuchn-mmllm-claude-train-sym24-4e0dcdad-WRdwR | 3.9972 |
| hgriC | fork-slaa-us-mmllm-claude-train-sym24-49df4cb5-hgriC | 4.2852 |
| tDl3P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98c1deb6-tDl3P | 4.3068 |
| 6yron | fork-joly-os-mmllm-claude-train-sym24-ccb95df3-6yron | 4.3187 |
| ZBCJK | fork-joly-os-mmllm-claude-train-sym24-e4f5cca1-ZBCJK | 4.3225 |
| **mean** | | **4.1668** |
| **best** | | **3.9529** |

## Chain progression R662 → R663

Previous harvest: `workers/dispatcher/harvest-7way-r662_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0935         | 4.1668         | +0.0733 |
| ctrl_bpc best  | 3.9717         | 3.9529         | -0.0188 |

## Per-round trajectory (best bird: giHcS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 663 | 6625 | 3.9529 | +0.1712 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r662_sym24`
  - `workers/dispatcher/harvest-7way-r662_sym24`

## Output

`workers/dispatcher/harvest-7way-r663_sym24/round-663/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

