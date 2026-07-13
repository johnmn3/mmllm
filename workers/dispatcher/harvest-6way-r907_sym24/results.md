# harvest-6way-r907 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R907 ctrl_bpc |
|--------|--------|--------------:|
| OXOnN | fork-SeniorCareMarket-mmllm-claude-train-sym24-a02c8b79-OXOnN | 2.7696 |
| xXopc | fork-joly-os-mmllm-claude-train-sym24-86fc60f0-xXopc | 2.7728 |
| BCDAv | fork-joly-os-mmllm-claude-train-sym24-e24c1216-BCDAv | 2.7832 |
| UuGgK | origin/claude/train-sym24-db4a025f-UuGgK | 2.8000 |
| H1BIi | fork-slaa-us-mmllm-claude-train-sym24-81eee7eb-H1BIi | 2.9487 |
| 9AZpE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-566c3029-9AZpE | 3.1582 |
| **mean** | | **2.8721** |
| **best** | | **2.7696** |

## Chain progression R906 → R907

Previous harvest: `workers/dispatcher/harvest-11way-r906_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9102         | 2.8721         | -0.0381 |
| ctrl_bpc best  | 2.7678         | 2.7696         | +0.0018 |

## Per-round trajectory (best bird: OXOnN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 907 | 6805 | 2.7696 | +0.3269 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r906_sym24`
  - `workers/dispatcher/harvest-6way-r906_sym24`

## Output

`workers/dispatcher/harvest-6way-r907_sym24/round-907/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

