# harvest-2way-r991 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R991 ctrl_bpc |
|--------|--------|--------------:|
| t7VOI | origin/claude/train-sym24-be391c96-t7VOI | 2.7666 |
| fh5Q7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e1752984-fh5Q7 | 2.7778 |
| **mean** | | **2.7722** |
| **best** | | **2.7666** |

## Chain progression R990 → R991

Previous harvest: `workers/dispatcher/harvest-6way-r990_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6573         | 2.7722         | +0.1149 |
| ctrl_bpc best  | 2.5818         | 2.7666         | +0.1848 |

## Per-round trajectory (best bird: t7VOI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 991 | 4360 | 2.7666 | +0.1598 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r990_sym24`

## Output

`workers/dispatcher/harvest-2way-r991_sym24/round-991/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

