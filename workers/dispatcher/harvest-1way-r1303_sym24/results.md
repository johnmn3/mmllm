# harvest-1way-r1303 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1303 ctrl_bpc |
|--------|--------|--------------:|
| 2ptfy | fork-joly-os-mmllm-claude-train-sym24-1f3b19bc-2ptfy | 3.6245 |
| **mean** | | **3.6245** |
| **best** | | **3.6245** |

## Chain progression R1302 → R1303

Previous harvest: `workers/dispatcher/harvest-5way-r1302_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7319         | 3.6245         | -0.1074 |
| ctrl_bpc best  | 3.5489         | 3.6245         | +0.0756 |

## Per-round trajectory (best bird: 2ptfy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1303 | 3667 | 3.6245 | +0.0603 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1302_sym24`

## Output

`workers/dispatcher/harvest-1way-r1303_sym24/round-1303/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

