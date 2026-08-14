# harvest-2way-r1205 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1205 ctrl_bpc |
|--------|--------|--------------:|
| msQQc | fork-slaa-us-mmllm-claude-train-sym24-d720a5d8-msQQc | 2.2810 |
| aYaPW | origin/claude/train-sym24-3bfab1be-aYaPW | 2.3016 |
| **mean** | | **2.2913** |
| **best** | | **2.2810** |

## Chain progression R1204 → R1205

Previous harvest: `workers/dispatcher/harvest-6way-r1204_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4434         | 2.2913         | -0.1521 |
| ctrl_bpc best  | 2.2789         | 2.2810         | +0.0021 |

## Per-round trajectory (best bird: msQQc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1205 | 4010 | 2.2810 | +0.2516 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1204_sym24`

## Output

`workers/dispatcher/harvest-2way-r1205_sym24/round-1205/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

