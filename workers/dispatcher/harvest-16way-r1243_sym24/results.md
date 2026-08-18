# harvest-16way-r1243 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R1243 ctrl_bpc |
|--------|--------|--------------:|
| nTTSg | origin/claude/train-sym24-8c45b1a4-nTTSg | 2.2466 |
| Hyazb | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5ea5780-Hyazb | 2.2478 |
| gpN6L | fork-slaa-us-mmllm-claude-train-sym24-c65948be-gpN6L | 2.2481 |
| CV773 | fork-joly-os-mmllm-claude-train-sym24-c52e861d-CV773 | 2.2521 |
| qn1fy | fork-slaa-us-mmllm-claude-train-sym24-b4f2c235-qn1fy | 2.2525 |
| RGAYE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-44066fe0-RGAYE | 2.2646 |
| 5HWE9 | fork-joly-os-mmllm-claude-train-sym24-7236af3b-5HWE9 | 2.2671 |
| Q8Q5U | fork-SeniorCareMarket-mmllm-claude-train-sym24-1a9eb27a-Q8Q5U | 2.2688 |
| tJYRV | fork-joly-os-mmllm-claude-train-sym24-548ffc0c-tJYRV | 2.4389 |
| dcKcI | fork-joly-os-mmllm-claude-train-sym24-c2bca63e-dcKcI | 2.4486 |
| bPQ2h | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-06acd8bc-bPQ2h | 2.6400 |
| xCTLR | origin/claude/train-sym24-1095073c-xCTLR | 2.6423 |
| 6L43i | fork-SeniorCareMarket-mmllm-claude-train-sym24-0191bb53-6L43i | 2.6446 |
| 3a2Ym | origin/claude/train-sym24-b946b59a-3a2Ym | 2.6447 |
| g6jKG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14ac5d34-g6jKG | 2.6507 |
| XtxPz | fork-slaa-us-mmllm-claude-train-sym24-23e9c5cb-XtxPz | 2.6670 |
| **mean** | | **2.4265** |
| **best** | | **2.2466** |

## Chain progression R1242 → R1243

Previous harvest: `workers/dispatcher/harvest-6way-r1242_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3542         | 2.4265         | +0.0723 |
| ctrl_bpc best  | 2.2500         | 2.2466         | -0.0034 |

## Per-round trajectory (best bird: nTTSg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1243 | 6344 | 2.2466 | +0.2471 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1242_sym24`
  - `workers/dispatcher/harvest-2way-r1242_sym24`
  - `workers/dispatcher/harvest-6way-r1242_sym24`

## Output

`workers/dispatcher/harvest-16way-r1243_sym24/round-1243/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

