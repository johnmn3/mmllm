# harvest-2way-r1342 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1342 ctrl_bpc |
|--------|--------|--------------:|
| 2Px2s | origin/claude/train-sym24-9d2f3e6a-2Px2s | 3.2795 |
| lE8Li | fork-slaa-us-mmllm-claude-train-sym24-a33c93e5-lE8Li | 3.3276 |
| **mean** | | **3.3035** |
| **best** | | **3.2795** |

## Chain progression R1341 → R1342

Previous harvest: `workers/dispatcher/harvest-1way-r1341_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3261         | 3.3035         | -0.0225 |
| ctrl_bpc best  | 3.3261         | 3.2795         | -0.0466 |

## Per-round trajectory (best bird: 2Px2s)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1342 | 6516 | 3.2795 | +0.1208 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1341_sym24`

## Output

`workers/dispatcher/harvest-2way-r1342_sym24/round-1342/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

