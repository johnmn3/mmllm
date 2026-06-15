# harvest-9way-r685 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R685 ctrl_bpc |
|--------|--------|--------------:|
| sdKmF | fork-slaa-us-mmllm-claude-train-sym24-c27e09b9-sdKmF | 3.7363 |
| 26Uai | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-629832b0-26Uai | 3.7401 |
| oJxcG | fork-joly-os-mmllm-claude-train-sym24-2a904487-oJxcG | 3.7650 |
| 1lpOd | fork-SeniorCareMarket-mmllm-claude-train-sym24-985e9b0f-1lpOd | 3.7659 |
| ctwuf | fork-slaa-us-mmllm-claude-train-sym24-11ec878d-ctwuf | 3.7876 |
| Nuf6V | fork-davidwuchn-mmllm-claude-train-sym24-13800b75-Nuf6V | 3.7963 |
| lcNUY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0d26976b-lcNUY | 3.8036 |
| o3AAR | origin/claude/train-sym24-6e4d33af-o3AAR | 3.8079 |
| ejxs2 | origin/claude/train-sym24-f0b72381-ejxs2 | 4.2350 |
| **mean** | | **3.8264** |
| **best** | | **3.7363** |

## Chain progression R684 → R685

Previous harvest: `workers/dispatcher/harvest-10way-r684_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8713         | 3.8264         | -0.0449 |
| ctrl_bpc best  | 3.7548         | 3.7363         | -0.0185 |

## Per-round trajectory (best bird: sdKmF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 685 | 6689 | 3.7363 | +0.3887 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r684_sym24`
  - `workers/dispatcher/harvest-3way-r684_sym24`

## Output

`workers/dispatcher/harvest-9way-r685_sym24/round-685/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

