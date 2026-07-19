# harvest-8way-r968 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R968 ctrl_bpc |
|--------|--------|--------------:|
| KluQJ | fork-joly-os-mmllm-claude-train-sym24-e7cf73a8-KluQJ | 2.6163 |
| L3VE7 | fork-slaa-us-mmllm-claude-train-sym24-fd3c12e2-L3VE7 | 2.6233 |
| cLU0y | origin/claude/train-sym24-ddb5a88f-cLU0y | 2.6261 |
| FtIKT | fork-SeniorCareMarket-mmllm-claude-train-sym24-018787f7-FtIKT | 2.6358 |
| EM8Zj | fork-joly-os-mmllm-claude-train-sym24-9286dcea-EM8Zj | 2.6420 |
| fcnB5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6f7c00b4-fcnB5 | 2.6444 |
| 5oWx7 | origin/claude/train-sym24-30fe2a66-5oWx7 | 2.6511 |
| a8Xkw | fork-joly-os-mmllm-claude-train-sym24-d0a2108e-a8Xkw | 2.8164 |
| **mean** | | **2.6569** |
| **best** | | **2.6163** |

## Chain progression R967 → R968

Previous harvest: `workers/dispatcher/harvest-9way-r967_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7837         | 2.6569         | -0.1268 |
| ctrl_bpc best  | 2.6160         | 2.6163         | +0.0003 |

## Per-round trajectory (best bird: KluQJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 968 | 5266 | 2.6163 | +0.1799 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r967_sym24`
  - `workers/dispatcher/harvest-9way-r967_sym24`

## Output

`workers/dispatcher/harvest-8way-r968_sym24/round-968/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

