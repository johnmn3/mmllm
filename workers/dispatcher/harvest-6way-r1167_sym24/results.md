# harvest-6way-r1167 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1167 ctrl_bpc |
|--------|--------|--------------:|
| LRDE0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-1bf66f88-LRDE0 | 2.3192 |
| eUzZa | fork-joly-os-mmllm-claude-train-sym24-2ca08794-eUzZa | 2.3392 |
| 6Fu5X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2a432718-6Fu5X | 2.3461 |
| bb5jy | fork-slaa-us-mmllm-claude-train-sym24-c6aa0efd-bb5jy | 2.5205 |
| Oqg9Z | origin/claude/train-sym24-c2dac651-Oqg9Z | 2.6993 |
| 7TQb4 | origin/claude/train-sym24-9c826297-7TQb4 | 2.7025 |
| **mean** | | **2.4878** |
| **best** | | **2.3192** |

## Chain progression R1166 → R1167

Previous harvest: `workers/dispatcher/harvest-6way-r1166_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4984         | 2.4878         | -0.0106 |
| ctrl_bpc best  | 2.3462         | 2.3192         | -0.0270 |

## Per-round trajectory (best bird: LRDE0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1167 | 5378 | 2.3192 | +0.2547 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1166_sym24`

## Output

`workers/dispatcher/harvest-6way-r1167_sym24/round-1167/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

