# harvest-3way-r1162 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1162 ctrl_bpc |
|--------|--------|--------------:|
| dColN | fork-slaa-us-mmllm-claude-train-sym24-ab2110e3-dColN | 2.5163 |
| cNZxD | origin/claude/train-sym24-1b71ef79-cNZxD | 2.5196 |
| qACKn | fork-joly-os-mmllm-claude-train-sym24-2c311650-qACKn | 2.7094 |
| **mean** | | **2.5818** |
| **best** | | **2.5163** |

## Chain progression R1161 → R1162

Previous harvest: `workers/dispatcher/harvest-6way-r1161_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6199         | 2.5818         | -0.0381 |
| ctrl_bpc best  | 2.3258         | 2.5163         | +0.1905 |

## Per-round trajectory (best bird: dColN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1162 | 6475 | 2.5163 | +0.2252 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1161_sym24`

## Output

`workers/dispatcher/harvest-3way-r1162_sym24/round-1162/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

