# harvest-2way-r968 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R968 ctrl_bpc |
|--------|--------|--------------:|
| 5oWx7 | origin/claude/train-sym24-30fe2a66-5oWx7 | 2.6511 |
| a8Xkw | fork-joly-os-mmllm-claude-train-sym24-d0a2108e-a8Xkw | 2.8164 |
| **mean** | | **2.7337** |
| **best** | | **2.6511** |

## Chain progression R967 → R968

Previous harvest: `workers/dispatcher/harvest-13way-r967_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8013         | 2.7337         | -0.0676 |
| ctrl_bpc best  | 2.6160         | 2.6511         | +0.0351 |

## Per-round trajectory (best bird: 5oWx7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 968 | 5266 | 2.6511 | +0.1493 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r967_sym24`

## Output

`workers/dispatcher/harvest-2way-r968_sym24/round-968/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

