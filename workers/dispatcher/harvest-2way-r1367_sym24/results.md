# harvest-2way-r1367 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1367 ctrl_bpc |
|--------|--------|--------------:|
| ONIeK | origin/claude/train-sym24-d315493e-ONIeK | 3.2239 |
| ps0mH | origin/claude/train-sym24-5c18b374-ps0mH | 3.5845 |
| **mean** | | **3.4042** |
| **best** | | **3.2239** |

## Chain progression R1366 → R1367

Previous harvest: `workers/dispatcher/harvest-6way-r1366_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2853         | 3.4042         | +0.1189 |
| ctrl_bpc best  | 3.1281         | 3.2239         | +0.0958 |

## Per-round trajectory (best bird: ONIeK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1367 | 3766 | 3.2239 | +0.1771 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1366_sym24`

## Output

`workers/dispatcher/harvest-2way-r1367_sym24/round-1367/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

