# harvest-3way-r1361 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1361 ctrl_bpc |
|--------|--------|--------------:|
| BZ379 | fork-joly-os-mmllm-claude-train-sym24-7cac15b9-BZ379 | 3.1082 |
| 3ZqoW | fork-slaa-us-mmllm-claude-train-sym24-b0505dd0-3ZqoW | 3.2194 |
| 132eS | origin/claude/train-sym24-105e9d43-132eS | 3.5468 |
| **mean** | | **3.2915** |
| **best** | | **3.1082** |

## Chain progression R1360 → R1361

Previous harvest: `workers/dispatcher/harvest-4way-r1360_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3649         | 3.2915         | -0.0734 |
| ctrl_bpc best  | 3.1348         | 3.1082         | -0.0266 |

## Per-round trajectory (best bird: BZ379)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1361 | 3600 | 3.1082 | +0.1297 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1360_sym24`
  - `workers/dispatcher/harvest-3way-r1360_sym24`

## Output

`workers/dispatcher/harvest-3way-r1361_sym24/round-1361/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

