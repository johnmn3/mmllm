# harvest-1way-r71 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R71 ctrl_bpc |
|--------|--------|--------------:|
| rXSjW | fork-davidwuchn-mmllm-claude-train-d2fe1238-rXSjW | 1.0580 |
| **mean** | | **1.0580** |
| **best** | | **1.0580** |

## Chain progression R66 → R71

Previous harvest: `workers/dispatcher/harvest-1way-r66`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0026         | 1.0580         | +0.0554 |
| ctrl_bpc best  | 1.0026         | 1.0580         | +0.0554 |

## Per-round trajectory (best bird: rXSjW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 67 | 537 | 1.0117 | +0.0157 |
| 68 | 550 | 1.0437 | +0.0124 |
| 69 | 523 | 1.0431 | +0.0051 |
| 70 | 525 | 1.0602 | +0.0108 |
| 71 | 547 | 1.0580 | +0.0058 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **385 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r66`

## Output

`workers/dispatcher/harvest-1way-r71/round-71/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

