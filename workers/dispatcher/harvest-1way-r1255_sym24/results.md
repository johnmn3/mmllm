# harvest-1way-r1255 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1255 ctrl_bpc |
|--------|--------|--------------:|
| rkoA7 | fork-joly-os-mmllm-claude-train-sym24-d3f33f51-rkoA7 | 2.2357 |
| **mean** | | **2.2357** |
| **best** | | **2.2357** |

## Chain progression R1254 → R1255

Previous harvest: `workers/dispatcher/harvest-6way-r1254_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5481         | 2.2357         | -0.3124 |
| ctrl_bpc best  | 2.2375         | 2.2357         | -0.0018 |

## Per-round trajectory (best bird: rkoA7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1255 | 3591 | 2.2357 | +0.2443 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1254_sym24`

## Output

`workers/dispatcher/harvest-1way-r1255_sym24/round-1255/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

