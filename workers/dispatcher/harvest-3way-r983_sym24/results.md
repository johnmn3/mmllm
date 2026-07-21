# harvest-3way-r983 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R983 ctrl_bpc |
|--------|--------|--------------:|
| 9D24e | fork-SeniorCareMarket-mmllm-claude-train-sym24-96b7766a-9D24e | 2.6125 |
| pwUTS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c87e91d6-pwUTS | 2.7832 |
| Jfdy4 | origin/claude/train-sym24-1563c072-Jfdy4 | 2.9812 |
| **mean** | | **2.7923** |
| **best** | | **2.6125** |

## Chain progression R982 → R983

Previous harvest: `workers/dispatcher/harvest-2way-r982_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6261         | 2.7923         | +0.1662 |
| ctrl_bpc best  | 2.6227         | 2.6125         | -0.0102 |

## Per-round trajectory (best bird: 9D24e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 983 | 6688 | 2.6125 | +0.1752 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r982_sym24`

## Output

`workers/dispatcher/harvest-3way-r983_sym24/round-983/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

