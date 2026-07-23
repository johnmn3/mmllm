# harvest-1way-r1002 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1002 ctrl_bpc |
|--------|--------|--------------:|
| OfeuA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f1372b4-OfeuA | 2.7398 |
| **mean** | | **2.7398** |
| **best** | | **2.7398** |

## Chain progression R1001 → R1002

Previous harvest: `workers/dispatcher/harvest-6way-r1001_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7599         | 2.7398         | -0.0201 |
| ctrl_bpc best  | 2.5630         | 2.7398         | +0.1768 |

## Per-round trajectory (best bird: OfeuA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1002 | 3699 | 2.7398 | +0.1622 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1001_sym24`

## Output

`workers/dispatcher/harvest-1way-r1002_sym24/round-1002/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

