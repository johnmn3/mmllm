# harvest-1way-r1063 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1063 ctrl_bpc |
|--------|--------|--------------:|
| vsS2t | fork-slaa-us-mmllm-claude-train-sym24-9bc10f62-vsS2t | 2.4839 |
| **mean** | | **2.4839** |
| **best** | | **2.4839** |

## Chain progression R1062 → R1063

Previous harvest: `workers/dispatcher/harvest-9way-r1062_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5922         | 2.4839         | -0.1083 |
| ctrl_bpc best  | 2.4487         | 2.4839         | +0.0352 |

## Per-round trajectory (best bird: vsS2t)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1063 | 6596 | 2.4839 | +0.2062 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1062_sym24`

## Output

`workers/dispatcher/harvest-1way-r1063_sym24/round-1063/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

