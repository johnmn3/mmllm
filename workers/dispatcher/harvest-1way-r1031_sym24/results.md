# harvest-1way-r1031 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1031 ctrl_bpc |
|--------|--------|--------------:|
| NpqFl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95c69427-NpqFl | 2.5119 |
| **mean** | | **2.5119** |
| **best** | | **2.5119** |

## Chain progression R1030 → R1031

Previous harvest: `workers/dispatcher/harvest-6way-r1030_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8657         | 2.5119         | -0.3538 |
| ctrl_bpc best  | 2.7134         | 2.5119         | -0.2015 |

## Per-round trajectory (best bird: NpqFl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1031 | 3629 | 2.5119 | +0.1873 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1030_sym24`

## Output

`workers/dispatcher/harvest-1way-r1031_sym24/round-1031/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

