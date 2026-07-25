# harvest-1way-r1023 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1023 ctrl_bpc |
|--------|--------|--------------:|
| fhLCQ | fork-joly-os-mmllm-claude-train-sym24-34850986-fhLCQ | 2.9148 |
| **mean** | | **2.9148** |
| **best** | | **2.9148** |

## Chain progression R1022 → R1023

Previous harvest: `workers/dispatcher/harvest-8way-r1022_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6228         | 2.9148         | +0.2920 |
| ctrl_bpc best  | 2.5121         | 2.9148         | +0.4027 |

## Per-round trajectory (best bird: fhLCQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1023 | 3625 | 2.9148 | +0.1742 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1022_sym24`

## Output

`workers/dispatcher/harvest-1way-r1023_sym24/round-1023/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

