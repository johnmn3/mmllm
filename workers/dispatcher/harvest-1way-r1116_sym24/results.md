# harvest-1way-r1116 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1116 ctrl_bpc |
|--------|--------|--------------:|
| DH6cL | origin/claude/train-sym24-ff2df38e-DH6cL | 2.3941 |
| **mean** | | **2.3941** |
| **best** | | **2.3941** |

## Chain progression R1115 → R1116

Previous harvest: `workers/dispatcher/harvest-6way-r1115_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4778         | 2.3941         | -0.0837 |
| ctrl_bpc best  | 2.3667         | 2.3941         | +0.0274 |

## Per-round trajectory (best bird: DH6cL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1116 | 6626 | 2.3941 | +0.2302 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1115_sym24`

## Output

`workers/dispatcher/harvest-1way-r1116_sym24/round-1116/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

