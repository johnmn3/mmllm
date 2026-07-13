# harvest-11way-r907 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R907 ctrl_bpc |
|--------|--------|--------------:|
| KHRtQ | fork-slaa-us-mmllm-claude-train-sym24-0f63b871-KHRtQ | 2.7690 |
| OXOnN | fork-SeniorCareMarket-mmllm-claude-train-sym24-a02c8b79-OXOnN | 2.7696 |
| aAyZC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0c4218cf-aAyZC | 2.7697 |
| E1qpS | origin/claude/train-sym24-9c67faa1-E1qpS | 2.7714 |
| xXopc | fork-joly-os-mmllm-claude-train-sym24-86fc60f0-xXopc | 2.7728 |
| a9PLe | origin/claude/train-sym24-4b2ab755-a9PLe | 2.7811 |
| BCDAv | fork-joly-os-mmllm-claude-train-sym24-e24c1216-BCDAv | 2.7832 |
| UuGgK | origin/claude/train-sym24-db4a025f-UuGgK | 2.8000 |
| H1BIi | fork-slaa-us-mmllm-claude-train-sym24-81eee7eb-H1BIi | 2.9487 |
| vvArw | fork-SeniorCareMarket-mmllm-claude-train-sym24-1a67ab9c-vvArw | 3.1458 |
| 9AZpE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-566c3029-9AZpE | 3.1582 |
| **mean** | | **2.8609** |
| **best** | | **2.7690** |

## Chain progression R906 → R907

Previous harvest: `workers/dispatcher/harvest-6way-r906_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9313         | 2.8609         | -0.0704 |
| ctrl_bpc best  | 2.7693         | 2.7690         | -0.0003 |

## Per-round trajectory (best bird: KHRtQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 907 | 6471 | 2.7690 | +0.2058 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r906_sym24`
  - `workers/dispatcher/harvest-3way-r906_sym24`
  - `workers/dispatcher/harvest-6way-r906_sym24`

## Output

`workers/dispatcher/harvest-11way-r907_sym24/round-907/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

