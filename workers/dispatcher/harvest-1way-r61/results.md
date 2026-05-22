# harvest-1way-r61 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R61 ctrl_bpc |
|--------|--------|--------------:|
| ISySR | fork-davidwuchn-mmllm-claude-train-d335505f-ISySR | 1.0890 |
| **mean** | | **1.0890** |
| **best** | | **1.0890** |

## Chain progression R56 → R61

Previous harvest: `workers/dispatcher/harvest-1way-r56`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0504         | 1.0890         | +0.0386 |
| ctrl_bpc best  | 1.0504         | 1.0890         | +0.0386 |

## Per-round trajectory (best bird: ISySR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 57 | 539 | 1.0396 | +0.0096 |
| 58 | 512 | 1.0555 | +0.0092 |
| 59 | 553 | 1.1128 | +0.0107 |
| 60 | 539 | 1.0486 | +0.0034 |
| 61 | 534 | 1.0890 | +0.0093 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **315 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r56`

## Output

`workers/dispatcher/harvest-1way-r61/round-61/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

