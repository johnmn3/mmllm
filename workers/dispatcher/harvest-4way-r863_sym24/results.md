# harvest-4way-r863 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R863 ctrl_bpc |
|--------|--------|--------------:|
| FgeYA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9288eb1e-FgeYA | 2.8813 |
| su4Md | fork-slaa-us-mmllm-claude-train-sym24-d5d5f32a-su4Md | 3.2645 |
| 1hxLd | origin/claude/train-sym24-7042da62-1hxLd | 3.2726 |
| QVVJA | fork-SeniorCareMarket-mmllm-claude-train-sym24-cac9d8f7-QVVJA | 3.2755 |
| **mean** | | **3.1735** |
| **best** | | **2.8813** |

## Chain progression R862 → R863

Previous harvest: `workers/dispatcher/harvest-4way-r862_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9813         | 3.1735         | +0.1922 |
| ctrl_bpc best  | 2.8844         | 2.8813         | -0.0031 |

## Per-round trajectory (best bird: FgeYA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 863 | 6401 | 2.8813 | +0.4480 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r862_sym24`

## Output

`workers/dispatcher/harvest-4way-r863_sym24/round-863/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

