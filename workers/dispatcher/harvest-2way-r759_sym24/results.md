# harvest-2way-r759 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R759 ctrl_bpc |
|--------|--------|--------------:|
| aQvod | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9099cd32-aQvod | 3.2945 |
| DM5oN | origin/claude/train-sym24-1686e261-DM5oN | 3.6570 |
| **mean** | | **3.4758** |
| **best** | | **3.2945** |

## Chain progression R758 → R759

Previous harvest: `workers/dispatcher/harvest-6way-r758_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3938         | 3.4758         | +0.0819 |
| ctrl_bpc best  | 3.2876         | 3.2945         | +0.0069 |

## Per-round trajectory (best bird: aQvod)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 759 | 6638 | 3.2945 | +0.6425 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r758_sym24`

## Output

`workers/dispatcher/harvest-2way-r759_sym24/round-759/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

