# harvest-12way-r741 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R741 ctrl_bpc |
|--------|--------|--------------:|
| 9qLmW | fork-davidwuchn-mmllm-claude-train-sym24-b51cd4eb-9qLmW | 3.3649 |
| wwuLx | fork-joly-os-mmllm-claude-train-sym24-4838bf65-wwuLx | 3.3708 |
| RoXkn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-287c05ea-RoXkn | 3.3928 |
| tsrAu | fork-joly-os-mmllm-claude-train-sym24-3b2a8b43-tsrAu | 3.4111 |
| GTgqD | fork-davidwuchn-mmllm-claude-train-sym24-1882b4ff-GTgqD | 3.4142 |
| cAEbv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f78b29b2-cAEbv | 3.4154 |
| s4ODC | origin/claude/train-sym24-c12e725d-s4ODC | 3.4169 |
| WRu5x | fork-slaa-us-mmllm-claude-train-sym24-d61a5aa7-WRu5x | 3.4386 |
| Mkmzc | fork-davidwuchn-mmllm-claude-train-sym24-47c330c4-Mkmzc | 3.4470 |
| gY8s8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-afcea2c4-gY8s8 | 3.4569 |
| 5O4kX | origin/claude/train-sym24-95c95202-5O4kX | 3.7317 |
| 9zV5s | fork-slaa-us-mmllm-claude-train-sym24-6d3c180c-9zV5s | 3.7494 |
| **mean** | | **3.4675** |
| **best** | | **3.3649** |

## Chain progression R740 → R741

Previous harvest: `workers/dispatcher/harvest-7way-r740_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6137         | 3.4675         | -0.1462 |
| ctrl_bpc best  | 3.3827         | 3.3649         | -0.0178 |

## Per-round trajectory (best bird: 9qLmW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 741 | 5379 | 3.3649 | +0.5623 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r740_sym24`
  - `workers/dispatcher/harvest-7way-r740_sym24`

## Output

`workers/dispatcher/harvest-12way-r741_sym24/round-741/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

