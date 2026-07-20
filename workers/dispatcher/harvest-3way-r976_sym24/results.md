# harvest-3way-r976 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R976 ctrl_bpc |
|--------|--------|--------------:|
| T7KXm | fork-slaa-us-mmllm-claude-train-sym24-e60f696d-T7KXm | 2.6002 |
| 8bZiW | origin/claude/train-sym24-6bd2b070-8bZiW | 2.6229 |
| 7l8aQ | fork-joly-os-mmllm-claude-train-sym24-4554ced5-7l8aQ | 2.6337 |
| **mean** | | **2.6189** |
| **best** | | **2.6002** |

## Chain progression R975 → R976

Previous harvest: `workers/dispatcher/harvest-2way-r975_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8148         | 2.6189         | -0.1959 |
| ctrl_bpc best  | 2.6027         | 2.6002         | -0.0025 |

## Per-round trajectory (best bird: T7KXm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 976 | 4194 | 2.6002 | +0.1708 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r975_sym24`
  - `workers/dispatcher/harvest-2way-r975_sym24`

## Output

`workers/dispatcher/harvest-3way-r976_sym24/round-976/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

