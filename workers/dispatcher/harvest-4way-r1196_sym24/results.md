# harvest-4way-r1196 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1196 ctrl_bpc |
|--------|--------|--------------:|
| WfTfC | fork-joly-os-mmllm-claude-train-sym24-d6090f45-WfTfC | 2.2917 |
| JPJSq | origin/claude/train-sym24-e7dabb20-JPJSq | 2.2981 |
| qxWar | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-16a8fb6b-qxWar | 2.4918 |
| 10uLK | fork-slaa-us-mmllm-claude-train-sym24-ffb35ed0-10uLK | 2.7040 |
| **mean** | | **2.4464** |
| **best** | | **2.2917** |

## Chain progression R1195 → R1196

Previous harvest: `workers/dispatcher/harvest-9way-r1195_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4974         | 2.4464         | -0.0510 |
| ctrl_bpc best  | 2.2812         | 2.2917         | +0.0105 |

## Per-round trajectory (best bird: WfTfC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1196 | 6417 | 2.2917 | +0.2557 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1195_sym24`

## Output

`workers/dispatcher/harvest-4way-r1196_sym24/round-1196/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

