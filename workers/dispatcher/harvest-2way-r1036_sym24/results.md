# harvest-2way-r1036 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1036 ctrl_bpc |
|--------|--------|--------------:|
| V85Bo | origin/claude/train-sym24-e8395dd4-V85Bo | 2.5333 |
| wsu4f | origin/claude/train-sym24-e3219fa4-wsu4f | 2.8921 |
| **mean** | | **2.7127** |
| **best** | | **2.5333** |

## Chain progression R1035 → R1036

Previous harvest: `workers/dispatcher/harvest-6way-r1035_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6826         | 2.7127         | +0.0301 |
| ctrl_bpc best  | 2.4881         | 2.5333         | +0.0452 |

## Per-round trajectory (best bird: V85Bo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1036 | 6470 | 2.5333 | +0.1698 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1035_sym24`

## Output

`workers/dispatcher/harvest-2way-r1036_sym24/round-1036/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

