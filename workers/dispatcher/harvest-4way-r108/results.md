# harvest-4way-r108 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R108 ctrl_bpc |
|--------|--------|--------------:|
| waJJj | origin/claude/train-6f33f464-waJJj | 0.9448 |
| pOdvQ | fork-SeniorCareMarket-mmllm-claude-train-2ffff242-pOdvQ | 0.9892 |
| mpzBU | fork-SeniorCareMarket-mmllm-claude-train-36bcd4d5-mpzBU | 0.9904 |
| O56Nb | fork-joly-os-mmllm-claude-train-0dbd6063-O56Nb | 1.1220 |
| **mean** | | **1.0116** |
| **best** | | **0.9448** |

## Chain progression R104 → R108

Previous harvest: `workers/dispatcher/harvest-4way-r104`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0894         | 1.0116         | -0.0778 |
| ctrl_bpc best  | 0.9970         | 0.9448         | -0.0522 |

## Per-round trajectory (best bird: waJJj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 104 | 659 | 0.9901 | +0.0016 |
| 105 | 538 | 1.0005 | +0.0115 |
| 106 | 574 | 1.0887 | -0.0016 |
| 107 | 545 | 0.9656 | +0.0064 |
| 108 | 513 | 0.9448 | +0.0041 |

## Cumulative training contribution

- This harvest: **133 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **2431 steps** from 62 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r103`
  - `workers/dispatcher/harvest-4way-r104`

## Output

`workers/dispatcher/harvest-4way-r108/round-108/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

