# harvest-1way-r56 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R56 ctrl_bpc |
|--------|--------|--------------:|
| 92nCf | fork-davidwuchn-mmllm-claude-train-d0916fa2-92nCf | 1.0504 |
| **mean** | | **1.0504** |
| **best** | | **1.0504** |

## Chain progression R51 → R56

Previous harvest: `workers/dispatcher/harvest-1way-r51`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0290         | 1.0504         | +0.0214 |
| ctrl_bpc best  | 1.0290         | 1.0504         | +0.0214 |

## Per-round trajectory (best bird: 92nCf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 52 | 513 | 1.0167 | +0.0010 |
| 53 | 520 | 1.0211 | +0.0047 |
| 54 | 543 | 1.0478 | +0.0013 |
| 55 | 564 | 1.0402 | +0.0114 |
| 56 | 549 | 1.0504 | +0.0040 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **280 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r51`

## Output

`workers/dispatcher/harvest-1way-r56/round-56/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

