# harvest-2way-r772 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R772 ctrl_bpc |
|--------|--------|--------------:|
| MJVer | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a5642975-MJVer | 3.2130 |
| DFipy | origin/claude/train-sym24-dafa657a-DFipy | 3.2213 |
| **mean** | | **3.2172** |
| **best** | | **3.2130** |

## Chain progression R771 → R772

Previous harvest: `workers/dispatcher/harvest-3way-r771_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4973         | 3.2172         | -0.2801 |
| ctrl_bpc best  | 3.2597         | 3.2130         | -0.0467 |

## Per-round trajectory (best bird: MJVer)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 772 | 6354 | 3.2130 | +0.6568 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r771_sym24`

## Output

`workers/dispatcher/harvest-2way-r772_sym24/round-772/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

