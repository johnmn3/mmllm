# harvest-4way-r685 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R685 ctrl_bpc |
|--------|--------|--------------:|
| 26Uai | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-629832b0-26Uai | 3.7401 |
| oJxcG | fork-joly-os-mmllm-claude-train-sym24-2a904487-oJxcG | 3.7650 |
| ctwuf | fork-slaa-us-mmllm-claude-train-sym24-11ec878d-ctwuf | 3.7876 |
| ejxs2 | origin/claude/train-sym24-f0b72381-ejxs2 | 4.2350 |
| **mean** | | **3.8819** |
| **best** | | **3.7401** |

## Chain progression R684 → R685

Previous harvest: `workers/dispatcher/harvest-10way-r684_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8713         | 3.8819         | +0.0106 |
| ctrl_bpc best  | 3.7548         | 3.7401         | -0.0147 |

## Per-round trajectory (best bird: 26Uai)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 685 | 6591 | 3.7401 | +0.4569 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r684_sym24`

## Output

`workers/dispatcher/harvest-4way-r685_sym24/round-685/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

