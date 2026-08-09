# harvest-1way-r1155 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1155 ctrl_bpc |
|--------|--------|--------------:|
| B1A7Z | origin/claude/train-sym24-35a2f051-B1A7Z | 2.3277 |
| **mean** | | **2.3277** |
| **best** | | **2.3277** |

## Chain progression R1154 → R1155

Previous harvest: `workers/dispatcher/harvest-6way-r1154_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6273         | 2.3277         | -0.2996 |
| ctrl_bpc best  | 2.3659         | 2.3277         | -0.0382 |

## Per-round trajectory (best bird: B1A7Z)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1155 | 6702 | 2.3277 | +0.2562 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1154_sym24`

## Output

`workers/dispatcher/harvest-1way-r1155_sym24/round-1155/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

