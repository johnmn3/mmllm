# harvest-2way-r818 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R818 ctrl_bpc |
|--------|--------|--------------:|
| M1Cjw | origin/claude/train-sym24-ce37eec1-M1Cjw | 3.0504 |
| Pv0WJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-79a4588d-Pv0WJ | 3.1792 |
| **mean** | | **3.1148** |
| **best** | | **3.0504** |

## Chain progression R817 → R818

Previous harvest: `workers/dispatcher/harvest-7way-r817_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1794         | 3.1148         | -0.0646 |
| ctrl_bpc best  | 3.0375         | 3.0504         | +0.0129 |

## Per-round trajectory (best bird: M1Cjw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 818 | 6576 | 3.0504 | +0.8340 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r817_sym24`

## Output

`workers/dispatcher/harvest-2way-r818_sym24/round-818/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

