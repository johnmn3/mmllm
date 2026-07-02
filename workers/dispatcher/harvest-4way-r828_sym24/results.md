# harvest-4way-r828 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R828 ctrl_bpc |
|--------|--------|--------------:|
| s6Zmt | fork-SeniorCareMarket-mmllm-claude-train-sym24-48a95a9b-s6Zmt | 2.9988 |
| 706Zq | fork-slaa-us-mmllm-claude-train-sym24-6e5382f5-706Zq | 3.0014 |
| 6F6o5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-53dfaa2e-6F6o5 | 3.0122 |
| YHhcA | origin/claude/train-sym24-2a43d9ba-YHhcA | 3.3666 |
| **mean** | | **3.0948** |
| **best** | | **2.9988** |

## Chain progression R827 → R828

Previous harvest: `workers/dispatcher/harvest-1way-r827_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0039         | 3.0948         | +0.0909 |
| ctrl_bpc best  | 3.0039         | 2.9988         | -0.0051 |

## Per-round trajectory (best bird: s6Zmt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 828 | 4457 | 2.9988 | +0.4583 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r827_sym24`

## Output

`workers/dispatcher/harvest-4way-r828_sym24/round-828/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

