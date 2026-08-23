# harvest-1way-r1296 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1296 ctrl_bpc |
|--------|--------|--------------:|
| v3Ans | fork-SeniorCareMarket-mmllm-claude-train-sym24-66eb3f00-v3Ans | 3.9397 |
| **mean** | | **3.9397** |
| **best** | | **3.9397** |

## Chain progression R1295 → R1296

Previous harvest: `workers/dispatcher/harvest-4way-r1295_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1864         | 3.9397         | -0.2467 |
| ctrl_bpc best  | 4.0499         | 3.9397         | -0.1102 |

## Per-round trajectory (best bird: v3Ans)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1296 | 4053 | 3.9397 | +0.0325 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1295_sym24`

## Output

`workers/dispatcher/harvest-1way-r1296_sym24/round-1296/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

