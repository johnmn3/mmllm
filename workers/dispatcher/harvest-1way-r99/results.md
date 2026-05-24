# harvest-1way-r99 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R99 ctrl_bpc |
|--------|--------|--------------:|
| mUtSc | fork-joly-os-mmllm-claude-train-9ce3b3dc-mUtSc | 1.0369 |
| **mean** | | **1.0369** |
| **best** | | **1.0369** |

## Chain progression R94 → R99

Previous harvest: `workers/dispatcher/harvest-fold9way-r94`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9974         | 1.0369         | +0.0395 |
| ctrl_bpc best  | 0.9403         | 1.0369         | +0.0966 |

## Per-round trajectory (best bird: mUtSc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 95 | 698 | 0.9674 | +0.0095 |
| 96 | 621 | 1.0008 | +0.0112 |
| 97 | 541 | 1.0669 | +0.0093 |
| 98 | 535 | 1.0248 | +0.0146 |
| 99 | 587 | 1.0369 | +0.0094 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2158 steps** from 54 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r94`

## Output

`workers/dispatcher/harvest-1way-r99/round-99/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

