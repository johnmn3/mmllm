# harvest-1way-r1187 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1187 ctrl_bpc |
|--------|--------|--------------:|
| 5AzPM | fork-slaa-us-mmllm-claude-train-sym24-64b0ec87-5AzPM | 2.4990 |
| **mean** | | **2.4990** |
| **best** | | **2.4990** |

## Chain progression R1186 → R1187

Previous harvest: `workers/dispatcher/harvest-8way-r1186_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5968         | 2.4990         | -0.0978 |
| ctrl_bpc best  | 2.2986         | 2.4990         | +0.2004 |

## Per-round trajectory (best bird: 5AzPM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1187 | 3671 | 2.4990 | +0.2276 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1186_sym24`

## Output

`workers/dispatcher/harvest-1way-r1187_sym24/round-1187/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

