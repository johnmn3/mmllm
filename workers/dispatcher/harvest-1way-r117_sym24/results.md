# harvest-1way-r117 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R117 ctrl_bpc |
|--------|--------|--------------:|
| mCDRQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc0d875a-mCDRQ | 2.7119 |
| **mean** | | **2.7119** |
| **best** | | **2.7119** |

## Chain progression R116 → R117

Previous harvest: `workers/dispatcher/harvest-3way-r116_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0921         | 2.7119         | -0.3802 |
| ctrl_bpc best  | 2.8642         | 2.7119         | -0.1523 |

## Per-round trajectory (best bird: mCDRQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 117 | 5682 | 2.7119 | +0.0567 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **170 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r116_sym24`

## Output

`workers/dispatcher/harvest-1way-r117_sym24/round-117/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

