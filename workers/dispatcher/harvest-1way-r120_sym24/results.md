# harvest-1way-r120 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R120 ctrl_bpc |
|--------|--------|--------------:|
| Z8XmL | fork-SeniorCareMarket-mmllm-claude-train-sym24-f5594743-Z8XmL | 2.8199 |
| **mean** | | **2.8199** |
| **best** | | **2.8199** |

## Chain progression R119 → R120

Previous harvest: `workers/dispatcher/harvest-1way-r119_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9943         | 2.8199         | -0.1744 |
| ctrl_bpc best  | 2.9943         | 2.8199         | -0.1744 |

## Per-round trajectory (best bird: Z8XmL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 120 | 5665 | 2.8199 | +0.0757 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **300 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r119_sym24`

## Output

`workers/dispatcher/harvest-1way-r120_sym24/round-120/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

