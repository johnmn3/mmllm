# harvest-1way-r675 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R675 ctrl_bpc |
|--------|--------|--------------:|
| WY5v1 | origin/claude/train-sym24-ddec8774-WY5v1 | 3.8172 |
| **mean** | | **3.8172** |
| **best** | | **3.8172** |

## Chain progression R674 → R675

Previous harvest: `workers/dispatcher/harvest-12way-r674_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9220         | 3.8172         | -0.1048 |
| ctrl_bpc best  | 3.8302         | 3.8172         | -0.0130 |

## Per-round trajectory (best bird: WY5v1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 675 | 5518 | 3.8172 | +0.5895 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r674_sym24`

## Output

`workers/dispatcher/harvest-1way-r675_sym24/round-675/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

