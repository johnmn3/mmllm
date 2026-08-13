# harvest-9way-r1196 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1196 ctrl_bpc |
|--------|--------|--------------:|
| FQw42 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0b247a32-FQw42 | 2.2848 |
| WfTfC | fork-joly-os-mmllm-claude-train-sym24-d6090f45-WfTfC | 2.2917 |
| JPJSq | origin/claude/train-sym24-e7dabb20-JPJSq | 2.2981 |
| KuE2H | origin/claude/train-sym24-1c4196ea-KuE2H | 2.3071 |
| Y1sVi | origin/claude/train-sym24-c67cd0cd-Y1sVi | 2.4814 |
| wUunV | fork-joly-os-mmllm-claude-train-sym24-288bf59d-wUunV | 2.4847 |
| qxWar | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-16a8fb6b-qxWar | 2.4918 |
| 10uLK | fork-slaa-us-mmllm-claude-train-sym24-ffb35ed0-10uLK | 2.7040 |
| XEEnN | fork-slaa-us-mmllm-claude-train-sym24-475c7110-XEEnN | 2.7255 |
| **mean** | | **2.4521** |
| **best** | | **2.2848** |

## Chain progression R1195 → R1196

Previous harvest: `workers/dispatcher/harvest-9way-r1195_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4974         | 2.4521         | -0.0453 |
| ctrl_bpc best  | 2.2812         | 2.2848         | +0.0036 |

## Per-round trajectory (best bird: FQw42)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1196 | 4488 | 2.2848 | +0.2623 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1195_sym24`
  - `workers/dispatcher/harvest-5way-r1195_sym24`

## Output

`workers/dispatcher/harvest-9way-r1196_sym24/round-1196/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

