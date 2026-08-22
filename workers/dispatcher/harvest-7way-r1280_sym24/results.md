# harvest-7way-r1280 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1280 ctrl_bpc |
|--------|--------|--------------:|
| shUh6 | fork-slaa-us-mmllm-claude-train-sym24-f067effc-shUh6 | 2.2204 |
| xdUo2 | origin/claude/train-sym24-509c6fc6-xdUo2 | 2.2393 |
| pky0u | origin/claude/train-sym24-0049c7ca-pky0u | 2.2436 |
| F2EUA | fork-slaa-us-mmllm-claude-train-sym24-4279b51b-F2EUA | 2.4158 |
| mvPEF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f2ca899-mvPEF | 2.6170 |
| kpGUB | fork-joly-os-mmllm-claude-train-sym24-3abc2404-kpGUB | 2.6186 |
| 8qt2H | fork-SeniorCareMarket-mmllm-claude-train-sym24-26c3aaf1-8qt2H | 2.6240 |
| **mean** | | **2.4255** |
| **best** | | **2.2204** |

## Chain progression R1279 → R1280

Previous harvest: `workers/dispatcher/harvest-8way-r1279_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4284         | 2.4255         | -0.0029 |
| ctrl_bpc best  | 2.2426         | 2.2204         | -0.0222 |

## Per-round trajectory (best bird: shUh6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1280 | 6476 | 2.2204 | +0.2492 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1279_sym24`
  - `workers/dispatcher/harvest-8way-r1279_sym24`

## Output

`workers/dispatcher/harvest-7way-r1280_sym24/round-1280/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

