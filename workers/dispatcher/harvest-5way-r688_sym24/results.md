# harvest-5way-r688 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R688 ctrl_bpc |
|--------|--------|--------------:|
| cLxuP | fork-slaa-us-mmllm-claude-train-sym24-b81f6c21-cLxuP | 3.6959 |
| zZd4n | fork-joly-os-mmllm-claude-train-sym24-16ef5bfc-zZd4n | 3.7394 |
| ja8bB | fork-davidwuchn-mmllm-claude-train-sym24-08b01677-ja8bB | 3.7524 |
| G5iJB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7460823f-G5iJB | 3.7542 |
| YJFIp | origin/claude/train-sym24-e2cc792b-YJFIp | 4.0597 |
| **mean** | | **3.8003** |
| **best** | | **3.6959** |

## Chain progression R687 → R688

Previous harvest: `workers/dispatcher/harvest-6way-r687_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8522         | 3.8003         | -0.0519 |
| ctrl_bpc best  | 3.7212         | 3.6959         | -0.0253 |

## Per-round trajectory (best bird: cLxuP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 688 | 6486 | 3.6959 | +0.3243 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r687_sym24`
  - `workers/dispatcher/harvest-6way-r687_sym24`

## Output

`workers/dispatcher/harvest-5way-r688_sym24/round-688/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

