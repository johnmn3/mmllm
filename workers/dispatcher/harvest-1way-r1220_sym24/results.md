# harvest-1way-r1220 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1220 ctrl_bpc |
|--------|--------|--------------:|
| EaQYK | origin/claude/train-sym24-16be6ffc-EaQYK | 2.2654 |
| **mean** | | **2.2654** |
| **best** | | **2.2654** |

## Chain progression R1219 → R1220

Previous harvest: `workers/dispatcher/harvest-7way-r1219_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4445         | 2.2654         | -0.1791 |
| ctrl_bpc best  | 2.2691         | 2.2654         | -0.0037 |

## Per-round trajectory (best bird: EaQYK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1220 | 4456 | 2.2654 | +0.2747 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1219_sym24`

## Output

`workers/dispatcher/harvest-1way-r1220_sym24/round-1220/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

