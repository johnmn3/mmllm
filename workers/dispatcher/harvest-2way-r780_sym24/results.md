# harvest-2way-r780 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R780 ctrl_bpc |
|--------|--------|--------------:|
| 5lJrO | origin/claude/train-sym24-66ba2304-5lJrO | 3.3140 |
| db1Bs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bd9e59be-db1Bs | 3.3313 |
| **mean** | | **3.3227** |
| **best** | | **3.3140** |

## Chain progression R779 → R780

Previous harvest: `workers/dispatcher/harvest-3way-r779_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3528         | 3.3227         | -0.0301 |
| ctrl_bpc best  | 3.2283         | 3.3140         | +0.0857 |

## Per-round trajectory (best bird: 5lJrO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 780 | 6801 | 3.3140 | +0.5193 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r779_sym24`

## Output

`workers/dispatcher/harvest-2way-r780_sym24/round-780/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

