# harvest-5way-r1135 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1135 ctrl_bpc |
|--------|--------|--------------:|
| UYLMl | fork-SeniorCareMarket-mmllm-claude-train-sym24-a7c2b746-UYLMl | 2.3522 |
| afkc0 | origin/claude/train-sym24-dd17193b-afkc0 | 2.3575 |
| BKcva | origin/claude/train-sym24-8da0386b-BKcva | 2.3584 |
| 6JAAD | fork-joly-os-mmllm-claude-train-sym24-158039ec-6JAAD | 2.3718 |
| fG9R6 | fork-slaa-us-mmllm-claude-train-sym24-332110ed-fG9R6 | 2.5464 |
| **mean** | | **2.3973** |
| **best** | | **2.3522** |

## Chain progression R1134 → R1135

Previous harvest: `workers/dispatcher/harvest-5way-r1134_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5507         | 2.3973         | -0.1534 |
| ctrl_bpc best  | 2.3468         | 2.3522         | +0.0054 |

## Per-round trajectory (best bird: UYLMl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1135 | 4238 | 2.3522 | +0.2464 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1134_sym24`
  - `workers/dispatcher/harvest-5way-r1134_sym24`

## Output

`workers/dispatcher/harvest-5way-r1135_sym24/round-1135/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

