# harvest-3way-r764 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R764 ctrl_bpc |
|--------|--------|--------------:|
| YKZpJ | fork-slaa-us-mmllm-claude-train-sym24-bb42f1d5-YKZpJ | 3.2591 |
| QWcKI | origin/claude/train-sym24-7bb9c948-QWcKI | 3.3738 |
| q0Ilw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d26c2a23-q0Ilw | 3.6454 |
| **mean** | | **3.4261** |
| **best** | | **3.2591** |

## Chain progression R763 → R764

Previous harvest: `workers/dispatcher/harvest-3way-r763_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3952         | 3.4261         | +0.0309 |
| ctrl_bpc best  | 3.2594         | 3.2591         | -0.0003 |

## Per-round trajectory (best bird: YKZpJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 764 | 4406 | 3.2591 | +0.5865 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r763_sym24`

## Output

`workers/dispatcher/harvest-3way-r764_sym24/round-764/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

