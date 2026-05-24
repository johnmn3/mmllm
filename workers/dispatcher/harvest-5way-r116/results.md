# harvest-5way-r116 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R116 ctrl_bpc |
|--------|--------|--------------:|
| qtc8L | fork-slaa-us-mmllm-claude-train-9befe603-qtc8L | 0.9211 |
| TaUgN | fork-joly-os-mmllm-claude-train-48150056-TaUgN | 0.9372 |
| o0K9d | origin/claude/train-ae31d529-o0K9d | 0.9597 |
| N7VrV | fork-SeniorCareMarket-mmllm-claude-train-48b190d9-N7VrV | 1.0194 |
| dRHeH | fork-SeniorCareMarket-com-mmllm-claude-train-e75a0031-dRHeH | 1.0890 |
| **mean** | | **0.9853** |
| **best** | | **0.9211** |

## Chain progression R114 → R116

Previous harvest: `workers/dispatcher/harvest-1way-r114`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9911         | 0.9853         | -0.0058 |
| ctrl_bpc best  | 0.9911         | 0.9211         | -0.0700 |

## Per-round trajectory (best bird: qtc8L)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 112 | 567 | 0.9595 | +0.0074 |
| 113 | 563 | 0.9553 | +0.0122 |
| 114 | 550 | 0.9439 | +0.0110 |
| 115 | 529 | 0.9387 | +0.0117 |
| 116 | 528 | 0.9211 | +0.0084 |

## Cumulative training contribution

- This harvest: **175 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **2627 steps** from 68 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r111`

## Output

`workers/dispatcher/harvest-5way-r116/round-116/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

