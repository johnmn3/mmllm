# harvest-1way-r871 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R871 ctrl_bpc |
|--------|--------|--------------:|
| Ku8TB | fork-slaa-us-mmllm-claude-train-sym24-f5e56d47-Ku8TB | 3.0262 |
| **mean** | | **3.0262** |
| **best** | | **3.0262** |

## Chain progression R870 → R871

Previous harvest: `workers/dispatcher/harvest-3way-r870_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9984         | 3.0262         | +0.0278 |
| ctrl_bpc best  | 2.8703         | 3.0262         | +0.1559 |

## Per-round trajectory (best bird: Ku8TB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 871 | 4356 | 3.0262 | +0.4137 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r870_sym24`

## Output

`workers/dispatcher/harvest-1way-r871_sym24/round-871/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

