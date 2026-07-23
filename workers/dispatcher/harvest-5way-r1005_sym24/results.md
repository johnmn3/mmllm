# harvest-5way-r1005 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1005 ctrl_bpc |
|--------|--------|--------------:|
| Fcgrz | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7a285cd-Fcgrz | 2.5664 |
| PiKXc | fork-joly-os-mmllm-claude-train-sym24-2797221d-PiKXc | 2.6211 |
| DblxR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5c2f68f9-DblxR | 2.7509 |
| 61dOd | origin/claude/train-sym24-90cbcafe-61dOd | 2.9269 |
| WAg0y | origin/claude/train-sym24-d5559fd6-WAg0y | 2.9325 |
| **mean** | | **2.7596** |
| **best** | | **2.5664** |

## Chain progression R1004 → R1005

Previous harvest: `workers/dispatcher/harvest-5way-r1004_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8269         | 2.7596         | -0.0673 |
| ctrl_bpc best  | 2.5704         | 2.5664         | -0.0040 |

## Per-round trajectory (best bird: Fcgrz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1005 | 6503 | 2.5664 | +0.1565 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1004_sym24`
  - `workers/dispatcher/harvest-5way-r1004_sym24`

## Output

`workers/dispatcher/harvest-5way-r1005_sym24/round-1005/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

