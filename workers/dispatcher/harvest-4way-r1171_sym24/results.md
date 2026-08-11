# harvest-4way-r1171 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1171 ctrl_bpc |
|--------|--------|--------------:|
| H7YH9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a7f508f4-H7YH9 | 2.3349 |
| qWIs9 | origin/claude/train-sym24-90423764-qWIs9 | 2.3409 |
| zdgtt | fork-joly-os-mmllm-claude-train-sym24-1be47852-zdgtt | 2.5143 |
| lCb1l | fork-joly-os-mmllm-claude-train-sym24-cfe7e503-lCb1l | 2.7315 |
| **mean** | | **2.4804** |
| **best** | | **2.3349** |

## Chain progression R1170 → R1171

Previous harvest: `workers/dispatcher/harvest-7way-r1170_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4127         | 2.4804         | +0.0677 |
| ctrl_bpc best  | 2.3084         | 2.3349         | +0.0265 |

## Per-round trajectory (best bird: H7YH9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1171 | 4427 | 2.3349 | +0.2451 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1170_sym24`
  - `workers/dispatcher/harvest-7way-r1170_sym24`

## Output

`workers/dispatcher/harvest-4way-r1171_sym24/round-1171/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

