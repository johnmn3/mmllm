# harvest-1way-r1237 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1237 ctrl_bpc |
|--------|--------|--------------:|
| Ux5CE | fork-slaa-us-mmllm-claude-train-sym24-0d79adbb-Ux5CE | 2.6479 |
| **mean** | | **2.6479** |
| **best** | | **2.6479** |

## Chain progression R1236 → R1237

Previous harvest: `workers/dispatcher/harvest-6way-r1236_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4293         | 2.6479         | +0.2186 |
| ctrl_bpc best  | 2.2630         | 2.6479         | +0.3849 |

## Per-round trajectory (best bird: Ux5CE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1237 | 5278 | 2.6479 | +0.2171 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1236_sym24`

## Output

`workers/dispatcher/harvest-1way-r1237_sym24/round-1237/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

