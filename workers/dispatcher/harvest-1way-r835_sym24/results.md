# harvest-1way-r835 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R835 ctrl_bpc |
|--------|--------|--------------:|
| 8ORy8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f528161c-8ORy8 | 3.4139 |
| **mean** | | **3.4139** |
| **best** | | **3.4139** |

## Chain progression R834 → R835

Previous harvest: `workers/dispatcher/harvest-4way-r834_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2146         | 3.4139         | +0.1993 |
| ctrl_bpc best  | 2.9712         | 3.4139         | +0.4427 |

## Per-round trajectory (best bird: 8ORy8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 835 | 4349 | 3.4139 | +0.5027 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r834_sym24`

## Output

`workers/dispatcher/harvest-1way-r835_sym24/round-835/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

