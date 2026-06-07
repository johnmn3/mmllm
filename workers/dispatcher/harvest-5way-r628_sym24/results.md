# harvest-5way-r628 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R628 ctrl_bpc |
|--------|--------|--------------:|
| AcEhh | origin/claude/train-sym24-b63e269d-AcEhh | 2.1174 |
| 3dQNH | fork-slaa-us-mmllm-claude-train-sym24-eb546bfa-3dQNH | 2.1194 |
| C67lC | fork-joly-os-mmllm-claude-train-sym24-ab08f26f-C67lC | 2.1221 |
| qbPZY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-26c2354f-qbPZY | 2.1327 |
| BDlFc | fork-davidwuchn-mmllm-claude-train-sym24-a63abb65-BDlFc | 2.3354 |
| **mean** | | **2.1654** |
| **best** | | **2.1174** |

## Chain progression R627 → R628

Previous harvest: `workers/dispatcher/harvest-7way-r627_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2188         | 2.1654         | -0.0534 |
| ctrl_bpc best  | 2.1248         | 2.1174         | -0.0074 |

## Per-round trajectory (best bird: AcEhh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 628 | 5309 | 2.1174 | +0.0493 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1150 steps** from 23 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r627_sym24`

## Output

`workers/dispatcher/harvest-5way-r628_sym24/round-628/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

