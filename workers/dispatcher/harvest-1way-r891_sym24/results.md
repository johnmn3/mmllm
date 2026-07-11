# harvest-1way-r891 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R891 ctrl_bpc |
|--------|--------|--------------:|
| SMzrn | origin/claude/train-sym24-d660d321-SMzrn | 2.8384 |
| **mean** | | **2.8384** |
| **best** | | **2.8384** |

## Chain progression R890 → R891

Previous harvest: `workers/dispatcher/harvest-4way-r890_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9303         | 2.8384         | -0.0919 |
| ctrl_bpc best  | 2.8163         | 2.8384         | +0.0221 |

## Per-round trajectory (best bird: SMzrn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 891 | 4422 | 2.8384 | +0.1399 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r890_sym24`

## Output

`workers/dispatcher/harvest-1way-r891_sym24/round-891/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

