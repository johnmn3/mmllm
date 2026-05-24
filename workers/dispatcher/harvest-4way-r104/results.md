# harvest-4way-r104 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R104 ctrl_bpc |
|--------|--------|--------------:|
| DXgxJ | fork-SeniorCareMarket-mmllm-claude-train-23f12a03-DXgxJ | 0.9970 |
| YuZUz | fork-joly-os-mmllm-claude-train-60b4e06a-YuZUz | 1.0961 |
| tf3bC | origin/claude/train-2d405f97-tf3bC | 1.1027 |
| a7Usb | fork-slaa-us-mmllm-claude-train-84ac876f-a7Usb | 1.1617 |
| **mean** | | **1.0894** |
| **best** | | **0.9970** |

## Chain progression R103 → R104

Previous harvest: `workers/dispatcher/harvest-1way-r103`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0209         | 1.0894         | +0.0685 |
| ctrl_bpc best  | 1.0209         | 0.9970         | -0.0239 |

## Per-round trajectory (best bird: DXgxJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 100 | 653 | 1.0033 | +0.0085 |
| 101 | 545 | 1.0036 | +0.0058 |
| 102 | 572 | 1.0513 | +0.0082 |
| 103 | 510 | 1.0209 | +0.0089 |
| 104 | 563 | 0.9970 | +0.0131 |

## Cumulative training contribution

- This harvest: **140 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **2298 steps** from 58 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r99`

## Output

`workers/dispatcher/harvest-4way-r104/round-104/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

