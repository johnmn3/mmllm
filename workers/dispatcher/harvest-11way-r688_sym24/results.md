# harvest-11way-r688 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R688 ctrl_bpc |
|--------|--------|--------------:|
| cLxuP | fork-slaa-us-mmllm-claude-train-sym24-b81f6c21-cLxuP | 3.6959 |
| zZd4n | fork-joly-os-mmllm-claude-train-sym24-16ef5bfc-zZd4n | 3.7394 |
| 5g5ml | fork-joly-os-mmllm-claude-train-sym24-9518c37a-5g5ml | 3.7492 |
| ja8bB | fork-davidwuchn-mmllm-claude-train-sym24-08b01677-ja8bB | 3.7524 |
| YE8jP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-120a3d4d-YE8jP | 3.7540 |
| G5iJB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7460823f-G5iJB | 3.7542 |
| VsQ0p | fork-SeniorCareMarket-mmllm-claude-train-sym24-f02f99db-VsQ0p | 3.7544 |
| XwxlR | fork-slaa-us-mmllm-claude-train-sym24-e8029365-XwxlR | 3.7954 |
| 6VjNn | fork-davidwuchn-mmllm-claude-train-sym24-0b77a603-6VjNn | 3.8752 |
| vNBG0 | origin/claude/train-sym24-40b408c0-vNBG0 | 4.0438 |
| YJFIp | origin/claude/train-sym24-e2cc792b-YJFIp | 4.0597 |
| **mean** | | **3.8158** |
| **best** | | **3.6959** |

## Chain progression R687 → R688

Previous harvest: `workers/dispatcher/harvest-6way-r687_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8522         | 3.8158         | -0.0364 |
| ctrl_bpc best  | 3.7212         | 3.6959         | -0.0253 |

## Per-round trajectory (best bird: cLxuP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 688 | 6486 | 3.6959 | +0.3243 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r687_sym24`
  - `workers/dispatcher/harvest-6way-r687_sym24`

## Output

`workers/dispatcher/harvest-11way-r688_sym24/round-688/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

