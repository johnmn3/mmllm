# harvest-1way-r1241 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1241 ctrl_bpc |
|--------|--------|--------------:|
| rMLal | fork-joly-os-mmllm-claude-train-sym24-1867e725-rMLal | 2.6577 |
| **mean** | | **2.6577** |
| **best** | | **2.6577** |

## Chain progression R1240 → R1241

Previous harvest: `workers/dispatcher/harvest-7way-r1240_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4513         | 2.6577         | +0.2064 |
| ctrl_bpc best  | 2.2508         | 2.6577         | +0.4069 |

## Per-round trajectory (best bird: rMLal)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1241 | 5356 | 2.6577 | +0.2150 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1240_sym24`

## Output

`workers/dispatcher/harvest-1way-r1241_sym24/round-1241/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

