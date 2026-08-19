# harvest-14way-r1248 — sparse-delta merge of 14 birds

## Worker endpoints

| handle | branch | R1248 ctrl_bpc |
|--------|--------|--------------:|
| WF9xC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-67ea098a-WF9xC | 2.2415 |
| hn6Pa | fork-joly-os-mmllm-claude-train-sym24-0505febf-hn6Pa | 2.2517 |
| Ypqu3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-9ba7f71e-Ypqu3 | 2.2571 |
| DPy9l | origin/claude/train-sym24-c9ce3d8a-DPy9l | 2.4346 |
| cDVOp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6e75d032-cDVOp | 2.4399 |
| bqnc4 | fork-slaa-us-mmllm-claude-train-sym24-07a7a9d2-bqnc4 | 2.4402 |
| 7GRSY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e8abce42-7GRSY | 2.4411 |
| UnnAf | fork-joly-os-mmllm-claude-train-sym24-22be5244-UnnAf | 2.4444 |
| y7Qb5 | origin/claude/train-sym24-7db9f885-y7Qb5 | 2.4463 |
| DgmOi | fork-SeniorCareMarket-mmllm-claude-train-sym24-d75c0722-DgmOi | 2.4465 |
| TQkiX | fork-slaa-us-mmllm-claude-train-sym24-4b07eeef-TQkiX | 2.6330 |
| bXntV | fork-SeniorCareMarket-mmllm-claude-train-sym24-80d047bb-bXntV | 2.6424 |
| sULSf | fork-slaa-us-mmllm-claude-train-sym24-f1cad801-sULSf | 2.6435 |
| nJLr4 | origin/claude/train-sym24-7595e6ef-nJLr4 | 2.6528 |
| **mean** | | **2.4582** |
| **best** | | **2.2415** |

## Chain progression R1247 → R1248

Previous harvest: `workers/dispatcher/harvest-5way-r1247_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3312         | 2.4582         | +0.1270 |
| ctrl_bpc best  | 2.2403         | 2.2415         | +0.0012 |

## Per-round trajectory (best bird: WF9xC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1248 | 6572 | 2.2415 | +0.2546 |

## Cumulative training contribution

- This harvest: **1120 steps** from 14 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1247_sym24`
  - `workers/dispatcher/harvest-16way-r1247_sym24`
  - `workers/dispatcher/harvest-5way-r1247_sym24`

## Output

`workers/dispatcher/harvest-14way-r1248_sym24/round-1248/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 14 workers)
- `dense.pt` (averaged across 14 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

