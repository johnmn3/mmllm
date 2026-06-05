# harvest-3way-r613 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R613 ctrl_bpc |
|--------|--------|--------------:|
| lFG2S | fork-slaa-us-mmllm-claude-train-sym24-da4951ed-lFG2S | 2.1473 |
| u0rZO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f1226936-u0rZO | 2.3437 |
| nS6Lr | origin/claude/train-sym24-564fa736-nS6Lr | 2.6002 |
| **mean** | | **2.3637** |
| **best** | | **2.1473** |

## Chain progression R612 → R613

Previous harvest: `workers/dispatcher/harvest-2way-r612_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6037         | 2.3637         | -0.2400 |
| ctrl_bpc best  | 2.6027         | 2.1473         | -0.4554 |

## Per-round trajectory (best bird: lFG2S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 613 | 5287 | 2.1473 | +0.0231 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **450 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r612_sym24`

## Output

`workers/dispatcher/harvest-3way-r613_sym24/round-613/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

