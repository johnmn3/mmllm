# harvest-10way-r781 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R781 ctrl_bpc |
|--------|--------|--------------:|
| O1ZH9 | fork-slaa-us-mmllm-claude-train-sym24-3f9fd142-O1ZH9 | 3.1777 |
| 5Iiv9 | origin/claude/train-sym24-f08e16f9-5Iiv9 | 3.1817 |
| K3hLn | fork-joly-os-mmllm-claude-train-sym24-ae4cf0ce-K3hLn | 3.1927 |
| mePye | fork-SeniorCareMarket-mmllm-claude-train-sym24-3be763c3-mePye | 3.2160 |
| FIU39 | fork-slaa-us-mmllm-claude-train-sym24-a1730cd6-FIU39 | 3.2175 |
| zwIE2 | fork-davidwuchn-mmllm-claude-train-sym24-dcad8fef-zwIE2 | 3.2217 |
| ZpE7z | fork-joly-os-mmllm-claude-train-sym24-2392e154-ZpE7z | 3.2504 |
| uIYXw | fork-davidwuchn-mmllm-claude-train-sym24-04dc72be-uIYXw | 3.2529 |
| yAQrK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71e00991-yAQrK | 3.3171 |
| XnylI | fork-slaa-us-mmllm-claude-train-sym24-0c778d3b-XnylI | 3.5578 |
| **mean** | | **3.2585** |
| **best** | | **3.1777** |

## Chain progression R780 → R781

Previous harvest: `workers/dispatcher/harvest-9way-r780_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3689         | 3.2585         | -0.1104 |
| ctrl_bpc best  | 3.1952         | 3.1777         | -0.0175 |

## Per-round trajectory (best bird: O1ZH9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 781 | 7312 | 3.1777 | +0.5291 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r780_sym24`
  - `workers/dispatcher/harvest-9way-r780_sym24`

## Output

`workers/dispatcher/harvest-10way-r781_sym24/round-781/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

