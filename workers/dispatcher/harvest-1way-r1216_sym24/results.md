# harvest-1way-r1216 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1216 ctrl_bpc |
|--------|--------|--------------:|
| JXqbB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10ca2c4f-JXqbB | 2.2672 |
| **mean** | | **2.2672** |
| **best** | | **2.2672** |

## Chain progression R1215 → R1216

Previous harvest: `workers/dispatcher/harvest-10way-r1215_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3999         | 2.2672         | -0.1327 |
| ctrl_bpc best  | 2.2702         | 2.2672         | -0.0030 |

## Per-round trajectory (best bird: JXqbB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1216 | 4269 | 2.2672 | +0.2533 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1215_sym24`

## Output

`workers/dispatcher/harvest-1way-r1216_sym24/round-1216/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

