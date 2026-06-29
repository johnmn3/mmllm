# harvest-10way-r799 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R799 ctrl_bpc |
|--------|--------|--------------:|
| 6mayj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-235e4671-6mayj | 3.0997 |
| Eaf5Y | fork-joly-os-mmllm-claude-train-sym24-ab42bdfa-Eaf5Y | 3.1320 |
| mw3O8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-9228ccb7-mw3O8 | 3.2306 |
| Y1Nvj | origin/claude/train-sym24-f78bc646-Y1Nvj | 3.2416 |
| quS6h | fork-joly-os-mmllm-claude-train-sym24-3fbeda60-quS6h | 3.2459 |
| Go2Ux | fork-davidwuchn-mmllm-claude-train-sym24-1521d427-Go2Ux | 3.2482 |
| dW5Rr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ad7f5c6a-dW5Rr | 3.2529 |
| DoAZ1 | origin/claude/train-sym24-a394bd8d-DoAZ1 | 3.4816 |
| iPL5Y | fork-slaa-us-mmllm-claude-train-sym24-b35ace66-iPL5Y | 3.4900 |
| pTKFq | fork-slaa-us-mmllm-claude-train-sym24-51b46c01-pTKFq | 3.4979 |
| **mean** | | **3.2920** |
| **best** | | **3.0997** |

## Chain progression R798 → R799

Previous harvest: `workers/dispatcher/harvest-3way-r798_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2491         | 3.2920         | +0.0429 |
| ctrl_bpc best  | 3.1143         | 3.0997         | -0.0146 |

## Per-round trajectory (best bird: 6mayj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 799 | 5409 | 3.0997 | +0.4552 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r798_sym24`
  - `workers/dispatcher/harvest-3way-r798_sym24`

## Output

`workers/dispatcher/harvest-10way-r799_sym24/round-799/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

