# harvest-4way-r1362 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1362 ctrl_bpc |
|--------|--------|--------------:|
| ghqhj | origin/claude/train-sym24-4b18552a-ghqhj | 3.1484 |
| BSkZL | origin/claude/train-sym24-06506847-BSkZL | 3.2066 |
| axdk8 | fork-slaa-us-mmllm-claude-train-sym24-b711058d-axdk8 | 3.5269 |
| CKbCe | origin/claude/train-sym24-6dccee0d-CKbCe | 3.5331 |
| **mean** | | **3.3538** |
| **best** | | **3.1484** |

## Chain progression R1361 → R1362

Previous harvest: `workers/dispatcher/harvest-7way-r1361_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2939         | 3.3538         | +0.0599 |
| ctrl_bpc best  | 3.1082         | 3.1484         | +0.0402 |

## Per-round trajectory (best bird: ghqhj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1362 | 4062 | 3.1484 | +0.1188 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1361_sym24`
  - `workers/dispatcher/harvest-7way-r1361_sym24`

## Output

`workers/dispatcher/harvest-4way-r1362_sym24/round-1362/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

