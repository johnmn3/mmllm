# harvest-9way-r1005 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1005 ctrl_bpc |
|--------|--------|--------------:|
| WgpSf | origin/claude/train-sym24-ecf4e1bb-WgpSf | 2.5466 |
| Fcgrz | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7a285cd-Fcgrz | 2.5664 |
| PiKXc | fork-joly-os-mmllm-claude-train-sym24-2797221d-PiKXc | 2.6211 |
| rWfuB | fork-SeniorCareMarket-mmllm-claude-train-sym24-a9c3de4a-rWfuB | 2.7394 |
| DblxR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5c2f68f9-DblxR | 2.7509 |
| 61dOd | origin/claude/train-sym24-90cbcafe-61dOd | 2.9269 |
| WAg0y | origin/claude/train-sym24-d5559fd6-WAg0y | 2.9325 |
| ZDdyy | origin/claude/train-sym24-06ca0034-ZDdyy | 2.9444 |
| rZVhL | fork-slaa-us-mmllm-claude-train-sym24-9e9617f3-rZVhL | 2.9851 |
| **mean** | | **2.7793** |
| **best** | | **2.5466** |

## Chain progression R1004 → R1005

Previous harvest: `workers/dispatcher/harvest-5way-r1004_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8269         | 2.7793         | -0.0476 |
| ctrl_bpc best  | 2.5704         | 2.5466         | -0.0238 |

## Per-round trajectory (best bird: WgpSf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1005 | 6728 | 2.5466 | +0.1743 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1004_sym24`
  - `workers/dispatcher/harvest-5way-r1004_sym24`

## Output

`workers/dispatcher/harvest-9way-r1005_sym24/round-1005/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

