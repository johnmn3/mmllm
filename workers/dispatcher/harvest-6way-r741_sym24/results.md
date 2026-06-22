# harvest-6way-r741 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R741 ctrl_bpc |
|--------|--------|--------------:|
| RoXkn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-287c05ea-RoXkn | 3.3928 |
| tsrAu | fork-joly-os-mmllm-claude-train-sym24-3b2a8b43-tsrAu | 3.4111 |
| GTgqD | fork-davidwuchn-mmllm-claude-train-sym24-1882b4ff-GTgqD | 3.4142 |
| s4ODC | origin/claude/train-sym24-c12e725d-s4ODC | 3.4169 |
| gY8s8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-afcea2c4-gY8s8 | 3.4569 |
| 9zV5s | fork-slaa-us-mmllm-claude-train-sym24-6d3c180c-9zV5s | 3.7494 |
| **mean** | | **3.4735** |
| **best** | | **3.3928** |

## Chain progression R740 → R741

Previous harvest: `workers/dispatcher/harvest-7way-r740_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6137         | 3.4735         | -0.1402 |
| ctrl_bpc best  | 3.3827         | 3.3928         | +0.0101 |

## Per-round trajectory (best bird: RoXkn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 741 | 6435 | 3.3928 | +0.6262 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r740_sym24`

## Output

`workers/dispatcher/harvest-6way-r741_sym24/round-741/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

