# harvest-5way-r1143 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1143 ctrl_bpc |
|--------|--------|--------------:|
| wygXC | fork-joly-os-mmllm-claude-train-sym24-c595f2e9-wygXC | 2.3442 |
| 9KyJr | fork-SeniorCareMarket-mmllm-claude-train-sym24-15d3414c-9KyJr | 2.3464 |
| 9u4gT | fork-slaa-us-mmllm-claude-train-sym24-94e13dd1-9u4gT | 2.5437 |
| AEDhg | origin/claude/train-sym24-3c512251-AEDhg | 2.5459 |
| 3B6rF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4c7b8654-3B6rF | 2.7283 |
| **mean** | | **2.5017** |
| **best** | | **2.3442** |

## Chain progression R1142 → R1143

Previous harvest: `workers/dispatcher/harvest-6way-r1142_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6540         | 2.5017         | -0.1523 |
| ctrl_bpc best  | 2.5373         | 2.3442         | -0.1931 |

## Per-round trajectory (best bird: wygXC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1143 | 6477 | 2.3442 | +0.2443 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1142_sym24`

## Output

`workers/dispatcher/harvest-5way-r1143_sym24/round-1143/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

