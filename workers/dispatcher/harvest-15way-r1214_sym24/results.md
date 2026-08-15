# harvest-15way-r1214 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R1214 ctrl_bpc |
|--------|--------|--------------:|
| QXiEg | origin/claude/train-sym24-dbf78a18-QXiEg | 2.2674 |
| qyMoQ | fork-joly-os-mmllm-claude-train-sym24-fdea8c1b-qyMoQ | 2.2686 |
| W31H4 | fork-joly-os-mmllm-claude-train-sym24-5094a927-W31H4 | 2.2724 |
| CScWq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-36701889-CScWq | 2.2731 |
| oRjAU | fork-SeniorCareMarket-mmllm-claude-train-sym24-d4adc8ab-oRjAU | 2.2744 |
| mjjZx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8bb60367-mjjZx | 2.2983 |
| Pu8p7 | fork-slaa-us-mmllm-claude-train-sym24-800da532-Pu8p7 | 2.4625 |
| aw8Oq | origin/claude/train-sym24-0d63c37f-aw8Oq | 2.4632 |
| HI8SU | fork-SeniorCareMarket-mmllm-claude-train-sym24-67db59d8-HI8SU | 2.4654 |
| 797TT | origin/claude/train-sym24-b641e1ff-797TT | 2.4785 |
| vu9Ae | fork-slaa-us-mmllm-claude-train-sym24-fd6109ac-vu9Ae | 2.6636 |
| 3wdxU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3b27d79-3wdxU | 2.6686 |
| K4aFQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-ceffad04-K4aFQ | 2.6694 |
| U43xa | fork-joly-os-mmllm-claude-train-sym24-89d564c8-U43xa | 2.6695 |
| CqB3v | fork-slaa-us-mmllm-claude-train-sym24-9dd8c3a0-CqB3v | 2.6870 |
| **mean** | | **2.4588** |
| **best** | | **2.2674** |

## Chain progression R1213 → R1214

Previous harvest: `workers/dispatcher/harvest-8way-r1213_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4460         | 2.4588         | +0.0128 |
| ctrl_bpc best  | 2.2718         | 2.2674         | -0.0044 |

## Per-round trajectory (best bird: QXiEg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1214 | 6732 | 2.2674 | +0.2758 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1840 steps** from 23 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1213_sym24`
  - `workers/dispatcher/harvest-4way-r1213_sym24`
  - `workers/dispatcher/harvest-8way-r1213_sym24`

## Output

`workers/dispatcher/harvest-15way-r1214_sym24/round-1214/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

