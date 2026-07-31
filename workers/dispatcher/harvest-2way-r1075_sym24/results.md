# harvest-2way-r1075 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1075 ctrl_bpc |
|--------|--------|--------------:|
| MP04r | fork-joly-os-mmllm-claude-train-sym24-3dcedfc7-MP04r | 2.6133 |
| kpX94 | origin/claude/train-sym24-c4031c4f-kpX94 | 2.8291 |
| **mean** | | **2.7212** |
| **best** | | **2.6133** |

## Chain progression R1074 → R1075

Previous harvest: `workers/dispatcher/harvest-5way-r1074_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6498         | 2.7212         | +0.0714 |
| ctrl_bpc best  | 2.4634         | 2.6133         | +0.1499 |

## Per-round trajectory (best bird: MP04r)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1075 | 6585 | 2.6133 | +0.2173 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1074_sym24`

## Output

`workers/dispatcher/harvest-2way-r1075_sym24/round-1075/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

