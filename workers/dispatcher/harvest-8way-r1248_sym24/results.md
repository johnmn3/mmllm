# harvest-8way-r1248 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1248 ctrl_bpc |
|--------|--------|--------------:|
| hn6Pa | fork-joly-os-mmllm-claude-train-sym24-0505febf-hn6Pa | 2.2517 |
| Ypqu3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-9ba7f71e-Ypqu3 | 2.2571 |
| cDVOp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6e75d032-cDVOp | 2.4399 |
| bqnc4 | fork-slaa-us-mmllm-claude-train-sym24-07a7a9d2-bqnc4 | 2.4402 |
| 7GRSY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e8abce42-7GRSY | 2.4411 |
| DgmOi | fork-SeniorCareMarket-mmllm-claude-train-sym24-d75c0722-DgmOi | 2.4465 |
| TQkiX | fork-slaa-us-mmllm-claude-train-sym24-4b07eeef-TQkiX | 2.6330 |
| nJLr4 | origin/claude/train-sym24-7595e6ef-nJLr4 | 2.6528 |
| **mean** | | **2.4453** |
| **best** | | **2.2517** |

## Chain progression R1247 → R1248

Previous harvest: `workers/dispatcher/harvest-16way-r1247_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3643         | 2.4453         | +0.0810 |
| ctrl_bpc best  | 2.2403         | 2.2517         | +0.0114 |

## Per-round trajectory (best bird: hn6Pa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1248 | 6532 | 2.2517 | +0.2439 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1247_sym24`
  - `workers/dispatcher/harvest-5way-r1247_sym24`

## Output

`workers/dispatcher/harvest-8way-r1248_sym24/round-1248/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

