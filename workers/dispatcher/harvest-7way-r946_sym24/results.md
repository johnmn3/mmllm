# harvest-7way-r946 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R946 ctrl_bpc |
|--------|--------|--------------:|
| 03Vf9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0fe709e1-03Vf9 | 2.6733 |
| X0LF2 | fork-slaa-us-mmllm-claude-train-sym24-938210ab-X0LF2 | 2.6860 |
| jdVa7 | origin/claude/train-sym24-a45a0cbe-jdVa7 | 2.6919 |
| YFbeq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82b0621f-YFbeq | 2.8609 |
| WOczx | fork-joly-os-mmllm-claude-train-sym24-296f39bd-WOczx | 2.8659 |
| ARV0F | fork-SeniorCareMarket-mmllm-claude-train-sym24-c1b76b72-ARV0F | 2.8683 |
| wVj6g | origin/claude/train-sym24-3b7bbb63-wVj6g | 3.1198 |
| **mean** | | **2.8237** |
| **best** | | **2.6733** |

## Chain progression R945 → R946

Previous harvest: `workers/dispatcher/harvest-8way-r945_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8717         | 2.8237         | -0.0480 |
| ctrl_bpc best  | 2.6833         | 2.6733         | -0.0100 |

## Per-round trajectory (best bird: 03Vf9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 946 | 4336 | 2.6733 | +0.2151 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r945_sym24`
  - `workers/dispatcher/harvest-6way-r945_sym24`
  - `workers/dispatcher/harvest-8way-r945_sym24`

## Output

`workers/dispatcher/harvest-7way-r946_sym24/round-946/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

