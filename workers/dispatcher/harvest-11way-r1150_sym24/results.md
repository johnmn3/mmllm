# harvest-11way-r1150 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1150 ctrl_bpc |
|--------|--------|--------------:|
| xljQl | fork-joly-os-mmllm-claude-train-sym24-5b9a0837-xljQl | 2.3280 |
| 79XmG | fork-SeniorCareMarket-mmllm-claude-train-sym24-a1c69a53-79XmG | 2.3323 |
| qSz6z | fork-joly-os-mmllm-claude-train-sym24-11582c87-qSz6z | 2.3335 |
| VNRdd | fork-slaa-us-mmllm-claude-train-sym24-deb5b624-VNRdd | 2.3496 |
| JJPng | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-375bdbc5-JJPng | 2.3512 |
| P7ox9 | origin/claude/train-sym24-f39dc345-P7ox9 | 2.3524 |
| J1HYt | origin/claude/train-sym24-49867397-J1HYt | 2.5282 |
| Lgukg | fork-slaa-us-mmllm-claude-train-sym24-571edfe5-Lgukg | 2.5313 |
| qFJ3X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6c1a6cce-qFJ3X | 2.5339 |
| hZgET | fork-SeniorCareMarket-mmllm-claude-train-sym24-ee66b8d9-hZgET | 2.5380 |
| EVn00 | origin/claude/train-sym24-6a51ec96-EVn00 | 2.7218 |
| **mean** | | **2.4455** |
| **best** | | **2.3280** |

## Chain progression R1149 → R1150

Previous harvest: `workers/dispatcher/harvest-9way-r1149_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4541         | 2.4455         | -0.0086 |
| ctrl_bpc best  | 2.3364         | 2.3280         | -0.0084 |

## Per-round trajectory (best bird: xljQl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1150 | 6418 | 2.3280 | +0.2522 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1149_sym24`
  - `workers/dispatcher/harvest-6way-r1149_sym24`
  - `workers/dispatcher/harvest-9way-r1149_sym24`

## Output

`workers/dispatcher/harvest-11way-r1150_sym24/round-1150/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

