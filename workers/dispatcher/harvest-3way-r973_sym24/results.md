# harvest-3way-r973 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R973 ctrl_bpc |
|--------|--------|--------------:|
| nJ2sb | fork-joly-os-mmllm-claude-train-sym24-4c2073bf-nJ2sb | 2.5980 |
| pmrUc | fork-SeniorCareMarket-mmllm-claude-train-sym24-1df995d4-pmrUc | 3.0035 |
| IKYiK | origin/claude/train-sym24-f528c2dc-IKYiK | 3.0063 |
| **mean** | | **2.8693** |
| **best** | | **2.5980** |

## Chain progression R972 → R973

Previous harvest: `workers/dispatcher/harvest-5way-r972_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7716         | 2.8693         | +0.0977 |
| ctrl_bpc best  | 2.6081         | 2.5980         | -0.0101 |

## Per-round trajectory (best bird: nJ2sb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 973 | 4330 | 2.5980 | +0.1748 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r972_sym24`

## Output

`workers/dispatcher/harvest-3way-r973_sym24/round-973/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

