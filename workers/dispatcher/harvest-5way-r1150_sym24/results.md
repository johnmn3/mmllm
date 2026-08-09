# harvest-5way-r1150 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1150 ctrl_bpc |
|--------|--------|--------------:|
| 79XmG | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1c69a53-79XmG | 2.3323 |
| qSz6z | fork-joly-os-mmllm-claude-train-sym24-11582c87-qSz6z | 2.3335 |
| VNRdd | fork-slaa-us-mmllm-claude-train-sym24-deb5b624-VNRdd | 2.3496 |
| qFJ3X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6c1a6cce-qFJ3X | 2.5339 |
| EVn00 | origin/claude/train-sym24-6a51ec96-EVn00 | 2.7218 |
| **mean** | | **2.4542** |
| **best** | | **2.3323** |

## Chain progression R1149 → R1150

Previous harvest: `workers/dispatcher/harvest-9way-r1149_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4541         | 2.4542         | +0.0001 |
| ctrl_bpc best  | 2.3364         | 2.3323         | -0.0041 |

## Per-round trajectory (best bird: 79XmG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1150 | 6554 | 2.3323 | +0.2526 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1149_sym24`
  - `workers/dispatcher/harvest-6way-r1149_sym24`

## Output

`workers/dispatcher/harvest-5way-r1150_sym24/round-1150/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

