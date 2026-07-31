# harvest-1way-r1074 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1074 ctrl_bpc |
|--------|--------|--------------:|
| g2sZM | fork-joly-os-mmllm-claude-train-sym24-6169b6b2-g2sZM | 2.8218 |
| **mean** | | **2.8218** |
| **best** | | **2.8218** |

## Chain progression R1073 → R1074

Previous harvest: `workers/dispatcher/harvest-4way-r1073_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6873         | 2.8218         | +0.1345 |
| ctrl_bpc best  | 2.4531         | 2.8218         | +0.3687 |

## Per-round trajectory (best bird: g2sZM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1074 | 6556 | 2.8218 | +0.2074 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1073_sym24`

## Output

`workers/dispatcher/harvest-1way-r1074_sym24/round-1074/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

