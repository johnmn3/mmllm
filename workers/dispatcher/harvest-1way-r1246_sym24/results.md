# harvest-1way-r1246 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1246 ctrl_bpc |
|--------|--------|--------------:|
| foLFO | fork-SeniorCareMarket-mmllm-claude-train-sym24-549dabb3-foLFO | 2.6343 |
| **mean** | | **2.6343** |
| **best** | | **2.6343** |

## Chain progression R1245 → R1246

Previous harvest: `workers/dispatcher/harvest-9way-r1245_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3652         | 2.6343         | +0.2691 |
| ctrl_bpc best  | 2.2568         | 2.6343         | +0.3775 |

## Per-round trajectory (best bird: foLFO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1246 | 4004 | 2.6343 | +0.2322 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1245_sym24`

## Output

`workers/dispatcher/harvest-1way-r1246_sym24/round-1246/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

