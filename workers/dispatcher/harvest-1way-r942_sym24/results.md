# harvest-1way-r942 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R942 ctrl_bpc |
|--------|--------|--------------:|
| cwfQ3 | fork-slaa-us-mmllm-claude-train-sym24-16066d87-cwfQ3 | 2.8853 |
| **mean** | | **2.8853** |
| **best** | | **2.8853** |

## Chain progression R941 → R942

Previous harvest: `workers/dispatcher/harvest-4way-r941_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7404         | 2.8853         | +0.1449 |
| ctrl_bpc best  | 2.6712         | 2.8853         | +0.2141 |

## Per-round trajectory (best bird: cwfQ3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 942 | 6395 | 2.8853 | +0.1685 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r941_sym24`

## Output

`workers/dispatcher/harvest-1way-r942_sym24/round-942/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

