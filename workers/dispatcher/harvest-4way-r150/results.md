# harvest-4way-r150 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R150 ctrl_bpc |
|--------|--------|--------------:|
| cVGhQ | fork-slaa-us-mmllm-claude-train-139f848e-cVGhQ | 1.0689 |
| 9ryiI | fork-SeniorCareMarket-mmllm-claude-train-faf56c6c-9ryiI | 1.1068 |
| Niqqj | origin/claude/train-697bde5c-Niqqj | 1.1132 |
| reSjH | fork-joly-os-mmllm-claude-train-0b944c98-reSjH | 1.1155 |
| **mean** | | **1.1011** |
| **best** | | **1.0689** |

## Chain progression R147 → R150

Previous harvest: `workers/dispatcher/harvest-1way-r147`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0663         | 1.1011         | +0.0348 |
| ctrl_bpc best  | 1.0663         | 1.0689         | +0.0026 |

## Per-round trajectory (best bird: cVGhQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 146 | 603 | 1.0502 | -0.0002 |
| 147 | 571 | 1.0816 | +0.0033 |
| 148 | 535 | 1.0496 | -0.0022 |
| 149 | 547 | 1.0979 | +0.0013 |
| 150 | 530 | 1.0689 | -0.0055 |

## Cumulative training contribution

- This harvest: **140 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **3397 steps** from 92 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r145`

## Output

`workers/dispatcher/harvest-4way-r150/round-150/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

