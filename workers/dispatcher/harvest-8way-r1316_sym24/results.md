# harvest-8way-r1316 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1316 ctrl_bpc |
|--------|--------|--------------:|
| i3H2Z | fork-joly-os-mmllm-claude-train-sym24-746556ca-i3H2Z | 3.3853 |
| Nrmfz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b58d8d96-Nrmfz | 3.4162 |
| KWxDd | origin/claude/train-sym24-dff016e2-KWxDd | 3.4873 |
| K10ZZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-6694c034-K10ZZ | 3.4900 |
| neQ1Q | fork-joly-os-mmllm-claude-train-sym24-fb37eb07-neQ1Q | 3.4978 |
| jZnBs | fork-slaa-us-mmllm-claude-train-sym24-2eacaf56-jZnBs | 3.5274 |
| 6XNIi | fork-slaa-us-mmllm-claude-train-sym24-2ab59362-6XNIi | 3.7372 |
| H29M8 | origin/claude/train-sym24-f07105c7-H29M8 | 3.7711 |
| **mean** | | **3.5390** |
| **best** | | **3.3853** |

## Chain progression R1315 → R1316

Previous harvest: `workers/dispatcher/harvest-6way-r1315_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5997         | 3.5390         | -0.0607 |
| ctrl_bpc best  | 3.3720         | 3.3853         | +0.0133 |

## Per-round trajectory (best bird: i3H2Z)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1316 | 3853 | 3.3853 | +0.0685 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1315_sym24`
  - `workers/dispatcher/harvest-6way-r1315_sym24`

## Output

`workers/dispatcher/harvest-8way-r1316_sym24/round-1316/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

