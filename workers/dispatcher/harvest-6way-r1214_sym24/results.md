# harvest-6way-r1214 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1214 ctrl_bpc |
|--------|--------|--------------:|
| qyMoQ | fork-joly-os-mmllm-claude-train-sym24-fdea8c1b-qyMoQ | 2.2686 |
| Pu8p7 | fork-slaa-us-mmllm-claude-train-sym24-800da532-Pu8p7 | 2.4625 |
| HI8SU | fork-SeniorCareMarket-mmllm-claude-train-sym24-67db59d8-HI8SU | 2.4654 |
| 797TT | origin/claude/train-sym24-b641e1ff-797TT | 2.4785 |
| 3wdxU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3b27d79-3wdxU | 2.6686 |
| U43xa | fork-joly-os-mmllm-claude-train-sym24-89d564c8-U43xa | 2.6695 |
| **mean** | | **2.5022** |
| **best** | | **2.2686** |

## Chain progression R1213 → R1214

Previous harvest: `workers/dispatcher/harvest-8way-r1213_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4460         | 2.5022         | +0.0562 |
| ctrl_bpc best  | 2.2718         | 2.2686         | -0.0032 |

## Per-round trajectory (best bird: qyMoQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1214 | 6458 | 2.2686 | +0.2496 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1213_sym24`

## Output

`workers/dispatcher/harvest-6way-r1214_sym24/round-1214/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

